#!/usr/bin/env python3
"""Decide sozinho quais chamadas ao Supabase (MCP) precisam de autorização.

- Leitura, consultas e alterações de dados (SELECT, INSERT, UPDATE, DELETE com WHERE):
  liberadas, sem perguntar.
- Mudança de estrutura, RLS, permissões, migrações e operações destrutivas no projeto:
  o Claude Code pergunta ao William antes.
- Ferramenta desconhecida ou erro neste script: pergunta (nunca libera por engano).
"""
import json
import re
import sys

# Sempre liberadas: só leem ou não mexem na estrutura do banco.
LIBERADAS = {
    "list_organizations", "get_organization", "list_projects", "get_project",
    "get_project_url", "get_publishable_keys", "get_anon_key", "get_cost", "confirm_cost",
    "list_tables", "list_extensions", "list_migrations", "list_branches",
    "list_edge_functions", "get_edge_function", "get_logs", "query_logs",
    "get_advisors", "search_docs", "generate_typescript_types",
    "deploy_edge_function", "create_branch", "rebase_branch",
}

# Sempre perguntam: mudam a estrutura, aplicam migração ou afetam o projeto inteiro.
PERGUNTAR = {
    "apply_migration": "aplica uma migração (muda a estrutura do banco)",
    "merge_branch": "leva as migrações de uma branch para a produção",
    "reset_branch": "apaga e recria os dados de uma branch",
    "delete_branch": "apaga uma branch do Supabase",
    "pause_project": "pausa o projeto (o site sai do ar)",
    "restore_project": "religa um projeto pausado",
    "create_project": "cria um projeto novo (pode gerar custo)",
    "create_edge_function_secret": "cria ou troca um segredo das funções",
}

# Em execute_sql: palavras que indicam mudança de estrutura, RLS ou permissões.
SQL_ESTRUTURA = [
    (r"\bcreate\b", "CREATE"),
    (r"\balter\b", "ALTER"),
    (r"\bdrop\b", "DROP"),
    (r"\btruncate\b", "TRUNCATE"),
    (r"\bgrant\b", "GRANT"),
    (r"\brevoke\b", "REVOKE"),
    (r"\bpolicy\b", "política de RLS"),
    (r"\brow\s+level\s+security\b", "RLS"),
    (r"\bsecurity\s+definer\b", "SECURITY DEFINER"),
    (r"\bcomment\s+on\b", "COMMENT ON"),
    (r"\bdo\b", "bloco DO (pode executar qualquer coisa)"),
    (r"\bcopy\b", "COPY"),
    (r"\bset\s+(session\s+)?role\b", "SET ROLE"),
    (r"\breindex\b|\bvacuum\b|\bcluster\b", "manutenção do banco"),
]


def limpar_sql(sql: str) -> str:
    """Tira comentários e textos entre aspas, para não confundir conteúdo com comando."""
    sql = re.sub(r"--[^\n]*", " ", sql)
    sql = re.sub(r"/\*.*?\*/", " ", sql, flags=re.S)
    sql = re.sub(r"\$([A-Za-z_]\w*)?\$.*?\$\1\$", " '' ", sql, flags=re.S)
    sql = re.sub(r"'(?:[^']|'')*'", "''", sql)
    sql = re.sub(r'"(?:[^"]|"")*"', "x", sql)
    return sql.lower()


def motivo_sql(sql: str):
    limpo = limpar_sql(sql)
    for padrao, nome in SQL_ESTRUTURA:
        if re.search(padrao, limpo):
            return f"o SQL contém {nome}"
    # DELETE ou UPDATE sem WHERE atinge a tabela inteira.
    for comando in re.split(r";", limpo):
        c = comando.strip()
        if re.match(r"^(with\b.*\)\s*)?(delete|update)\b", c, flags=re.S) and not re.search(r"\bwhere\b", c):
            return "DELETE/UPDATE sem WHERE (atinge a tabela inteira)"
    return None


def decidir(entrada: dict):
    nome = entrada.get("tool_name", "").split("__")[-1]
    if nome == "execute_sql":
        motivo = motivo_sql(entrada.get("tool_input", {}).get("query", ""))
        return ("ask", f"Supabase: {motivo}.") if motivo else ("allow", "Supabase: consulta ou alteração de dados.")
    if nome in LIBERADAS:
        return "allow", f"Supabase: {nome} liberado."
    if nome in PERGUNTAR:
        return "ask", f"Supabase: {nome} {PERGUNTAR[nome]}."
    return "ask", f"Supabase: ferramenta {nome} não está na lista; confirme."


def main():
    try:
        decisao, motivo = decidir(json.load(sys.stdin))
    except Exception as erro:  # na dúvida, pergunta
        decisao, motivo = "ask", f"Supabase: não consegui analisar a chamada ({erro})."
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decisao,
            "permissionDecisionReason": motivo,
        }
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

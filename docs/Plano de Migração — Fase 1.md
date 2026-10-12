# Portal Educação Paulínia — Plano de Migração da Fase 1

Oct 12, 2026 · Secke Sistemas · **Para aprovação: nada deste plano foi aplicado.**

Continuação de *Banco de Dados — Diagnóstico e Decisões*. Tudo aqui é genérico: serve a qualquer organização da base (prefeitura, secretaria, câmara). O que é da SMEDU entra como dado, não como código.

## 1. Regras que todas as migrações seguem

- **Só acréscimos.** Nada é apagado ou renomeado.
- **Isolamento por organização:**
  - toda tabela nova tem `municipio_id`;
  - toda referência usa FK composta `(id, municipio_id)`;
  - RLS desde a criação;
  - `GRANT` explícito (D-13).
- **Registro:** gatilhos de auditoria e de `atualizado_em/por` em todas as tabelas novas.
- **Cache do portal:** o gatilho de limpeza de cache só é criado onde a 0011 existe (ver pergunta 3).
- **Testes antes de aplicar:** cada regra nova ganha teste em `rls.test.mjs`. A ordem é suíte com 0 falhas, depois homologação, depois produção.

## 2. Ponto central: os papéis antigos continuam valendo

Hoje, as 90 policies e o painel de Jeriquara dependem de `membros.papel` (admin, publicador, editor). Trocar isso de uma vez quebraria um cliente em operação. Proposta em duas fases:

| Fase | O que muda | Jeriquara |
| --- | --- | --- |
| **1A (este plano)** | Cria o sistema de permissões configuráveis. Os **módulos novos** (escolas, equipe gestora, permissões) já nascem protegidos por ele. Notícias, páginas, destaques e serviços seguem com os papéis antigos. | Nada muda. |
| **1B (plano seguinte)** | Os papéis antigos viram papéis do sistema (Administrador, Publicador, Editor) com as mesmas permissões de hoje, e as policies antigas passam a consultar `pode()`. Notícias ganham escopo por escola (ex.: diretor publica só da sua unidade). | Mesmo comportamento, garantido pela suíte de testes atual (114 verificações). |

Na fase 1A, quem administra a SMEDU recebe as duas coisas: `membros.papel = admin` (módulos antigos) e o papel **Administrador** novo (módulos novos).

## 3. Migrações propostas

### 0018_permissoes: papéis e permissões configuráveis

| Tabela | Para quê | Principais colunas |
| --- | --- | --- |
| `permissoes` | Catálogo **global**, gerado a partir do código | `codigo` (ex.: `equipe.editar`), `modulo`, `nome`, `descricao`, `escopos` (quais escopos fazem sentido) |
| `papeis` | Papéis **de cada organização** | `municipio_id`, `nome`, `slug`, `descricao`, `sistema` (criado pelo provisionamento), `protegido` |
| `papel_permissoes` | A chave liga/desliga | `papel_id`, `permissao_codigo`, `ativo`, `escopo` (`rede`, `regiao`, `unidade`, `proprio`) |
| `usuario_papeis` | Quem tem qual papel (vários por pessoa) | `user_id`, `papel_id`, `unidade_id` ou `regiao_id` (para escopo) |
| `log_permissoes` | Histórico (preenchido por gatilho) | quem, quando, papel, permissão, de → para |

**Função de autorização.** A função central é `pode(organização, permissão, unidade opcional)`. Ela fica em `seguranca` (fora da API), com uma função de mesmo nome em `public`, como na 0016. Responde verdadeiro quando:
- a pessoa é da Secke (master); ou
- tem um papel ativo com a permissão ligada, e o escopo cobre a unidade pedida:
  - `rede`: tudo;
  - `regiao`: unidades da região do vínculo;
  - `unidade`: só a unidade do vínculo;
  - `proprio`: decidido pela policy, comparando `criado_por` com o usuário.

**Salvaguardas** (aprovadas no brainstorm):
- **Master protegido:** o papel master não é uma linha de `papeis`. É a `equipe_plataforma`, que nenhum painel enxerga nem desliga: ninguém tranca a Secke para fora.
- **Administrador protegido:** o papel Administrador de cada organização não perde `permissoes.gerenciar`, impedido por gatilho. Assim a organização nunca fica sem quem configure.
- **Papéis novos pelo painel:** coordenador pedagógico, secretário de escola etc., sem tocar em código.
- **Funcionalidade nova aparece desligada:** quando o catálogo ganha uma permissão, ela surge desligada para todos os papéis.

**Catálogo gerado do código.** O painel terá um arquivo de registro (ex.: `permissoes.ts`) onde cada tela, botão e ação declara seu código. Um script de deploy envia a lista para `seguranca.sincronizar_permissoes(jsonb)`, que só pode ser executada com a chave de serviço. Esse script insere as permissões novas e marca as que saíram do código, sem apagar o histórico. Uma verificação no build falha se o código usar uma permissão que não está no registro.

**Papéis padrão de cada organização.** Criados pelo provisionamento, todos editáveis menos o Administrador:
- Administrador;
- Diretor (escopo unidade);
- Professor;
- Estudante.

**Permissões iniciais da fase 1A:**
- `permissoes.ver` e `permissoes.gerenciar`;
- `papeis.gerenciar`;
- `usuarios.vincular`;
- `unidades.ver_restrito`, `unidades.editar`, `unidades.gerenciar`;
- `equipe.editar`, `equipe.publicar`.

### 0019_unidades_equipe: escolas, regiões, supervisores e equipe gestora

| Tabela | Para quê | Principais colunas |
| --- | --- | --- |
| `regioes` | Agrupamento de unidades (setor, polo, região) | `nome`, `slug`, `ordem` |
| `unidades` | Escolas, creches, conveniadas (PROEB) e unidades administrativas. Genérico: na Saúde seriam UBS. | `nome`, `sigla`, `slug`, `tipo`, `etapas[]`, `codigo_inep`, `regiao_id`, endereço, `bairro`, `telefone`, `email`, `latitude/longitude`, `conveniada`, `supervisor_id`, `foto_id`, `ativo` |
| `equipe` | Equipe Gestora (3 níveis) | `nome`, `cargo`, `nivel` (1 Secretária/Adjunta · 2 Supervisores · 3 Diretores de divisão), `orgao_id` (a divisão, no organograma `orgaos`), `foto_id`, `autorizacao_imagem`, `email`, `telefone`, `ordem`, `visivel`, `dados_confirmados`, `user_id` (opcional) |

Regras e uso:

- **Busca do supervisor (card 5):** a função `buscar_unidade(organização, termo)` procura pelo nome da escola ou pelo bairro, sem acento. Devolve a escola e o supervisor com o contato institucional visível.
- **Foto só com autorização:** uma restrição no banco impede gravar `foto_id` sem `autorizacao_imagem`. Sem foto, o portal mostra o avatar neutro. É a regra do ECA/LGPD feita no banco, não só na tela.
- **Dados pendentes:** `dados_confirmados = falso` marca o registro como pendente no painel (regra "não inventar dados oficiais").
- **Leitura pública:**
  - unidades ativas;
  - membros da equipe visíveis;
  - a seção inteira some quando `config.modulos.equipe_gestora = false`.
- **Escrita:** por `pode()`. Um diretor com `unidades.editar` no escopo unidade edita só a própria escola.

### 0020_home_portal: destaques, avisos, serviços e prioridade

Só colunas novas em tabelas existentes:

| Tabela | Colunas novas | Para quê |
| --- | --- | --- |
| `destaques` | `botao_rotulo`, `frequencia` (`uma_vez`, `por_sessao`, `sempre`; padrão `uma_vez`), `versao`, `publicacao_id` | Botão do slide ("Faça a matrícula"); aviso que aparece uma vez por visitante (o navegador guarda `id + versao`; editar o aviso sobe a versão e ele reaparece); ligar o slide ou aviso à notícia. Tipo + nível já existem: alerta urgente vira modal, alerta informativo vira faixa, banner vira slide do carrossel. O fim automático usa o `fim_em`, que já existe. |
| `publicacoes` | `prioridade` (`principal`, `secundaria`; padrão `secundaria`) | Manchete maior na grade de notícias. "Urgente" e "principal do momento" viram um destaque ligado à notícia (promover/rebaixar no painel). |
| `servicos` | `icone`, `ordem`, `na_home`, `em_breve`, `sistema_id` | Cards da Área de Serviços, com estado "em breve" e ligação ao sistema satélite. |
| `sistemas_externos` | `em_breve`, `icone`, `ordem`; categoria nova `satelite`; `url` passa a aceitar vazio quando `em_breve` | Botões dos satélites (Área do Estudante, CI Eletrônica) antes de existirem. |

### Depois das migrações (dados, não código)

- **Equipe gestora:** registros com nome e cargo deixados em branco e marcados como pendentes, até você fornecer.
- **Cards de serviço da SMEDU:** os 6 cards do brainstorm. "Área do Estudante" e "Ouvidoria" entram como "em breve".
- **Sistemas satélites da SMEDU:** Área do Estudante, CI Eletrônica, Bolsa +, SIMAPE Escolar e Apoio à Recepção, todos como "em breve" até você passar os endereços.

## 4. Testes que entram na suíte (amostra)

- **Isolamento entre organizações:**
  - papel de uma organização não dá acesso a outra;
  - `usuario_papeis` não vincula usuário a papel nem a unidade de outra organização.
- **Permissões e escopos:**
  - permissão desligada bloqueia no banco, não só na tela;
  - diretor com escopo unidade edita a própria escola e não a vizinha;
  - escopo região cobre só as escolas da região;
  - permissão nova do catálogo nasce desligada.
- **Salvaguardas:**
  - Administrador não perde `permissoes.gerenciar`;
  - ninguém se promove sozinho;
  - todo liga/desliga gera linha em `log_permissoes`.
- **Equipe gestora:**
  - foto sem autorização é recusada;
  - membro oculto não aparece ao visitante.
- **Avisos e busca:**
  - aviso vencido some sozinho;
  - busca de escola por bairro sem acento encontra o supervisor.
- **Regressão:** os 114 testes atuais continuam passando, ou seja, Jeriquara não muda.

## 5. Perguntas para decidir antes de aplicar

1. **Fases 1A/1B:** aprova manter os papéis antigos nos módulos atuais agora e migrar na 1B? *(Recomendado.)*
2. **Supervisor:** cada escola tem **um** supervisor? Se puder ter mais de um, troco `supervisor_id` por uma tabela de vínculo.
3. **Produção atrasada:** as migrações 0011–0014 (cache, links, exportação) estão só na homologação. Aplico na produção antes da 0018, para as duas bases ficarem iguais? *(Recomendado. Exige configurar no Vault da produção os segredos do cache, `portal_cache_url` e `portal_cache_segredo`, senão a rotina de cache só fica parada, sem erro.)*
4. **Estudante e professor:** na fase 1 os papéis existem só como configuração (ninguém entra como aluno ainda). Confirma?

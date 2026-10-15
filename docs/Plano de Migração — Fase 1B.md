# Plano de Migração — Fase 1B (para aprovação)

15/10/2026 · preparado pela conta 2 · **aprovado pelo William e aplicado na homologação em 15/10/2026 (D-78); produção pendente**

## Objetivo
Fazer o conteúdo do portal (notícias, páginas, documentos, serviços, agenda, perguntas, banners, menus, transparência, identidade) obedecer aos **papéis configuráveis** (D-38), para que a equipe da SMEDU trabalhe só com eles. Jeriquara, que usa os papéis antigos (`membros`), não pode mudar em nada.

## O que já está pronto (fase 1A + painel, 15/10/2026)
- No banco (0018–0019, já em produção): papéis, permissões com escopo, vínculos, histórico, unidades, regiões, equipe gestora.
- No painel (branch `main` do `portal-municipal`): telas de Papéis e permissões, Vínculos de usuários, Unidades e regiões e Equipe gestora; menu e rotas montados pelas permissões; registro das permissões no código e script de sincronização.
- **Limite atual:** quem tem só papéis configuráveis ainda não edita conteúdo, não vê o nome dos colegas e não convida pessoas. Essas três regras ainda dependem de `membros`.

## A ideia: ampliar três funções em vez de reescrever 70 regras
Todas as regras de conteúdo do banco passam por três funções (`0001_base.sql`):

| Função | Hoje (só `membros`) | Depois (1B) |
|---|---|---|
| `is_membro(org)` | qualquer papel antigo | papel antigo **ou** `conteudo.editar`, `conteudo.publicar` ou `organizacao.administrar` |
| `pode_publicar(org)` | publicador ou admin | publicador ou admin **ou** `conteudo.publicar` ou `organizacao.administrar` |
| `is_admin(org)` | admin | admin **ou** `organizacao.administrar` |

- Os papéis antigos continuam valendo exatamente como hoje, então Jeriquara não muda. A parte nova só soma.
- As ~70 políticas e o gatilho de publicação (`checar_permissao_publicacao`) não são tocados.

## Migração `0021_permissoes_conteudo.sql`
1. **Catálogo:** 3 permissões novas.
   - `conteudo.editar`: criar e editar rascunhos.
   - `conteudo.publicar`: publicar, agendar, retirar do site, excluir.
   - `organizacao.administrar`: menus, transparência, identidade, categorias, redirecionamentos, auditoria, exportação.
   - Também entram no registro do painel (`permissoes.catalogo.json`).
2. **As três funções** ampliadas como na tabela acima: mesmo nome e assinatura, sem `drop`, SECURITY INVOKER como as originais (quem lê sem RLS são `tem_papel` e `seguranca.pode`).
3. **Colegas visíveis:** a política `perfis: próprio ou colega` passa a considerar também quem tem vínculo em `usuario_papeis` na mesma organização.
4. **Papéis da SMEDU** (só para organizações que já têm papéis; Jeriquara não tem):
   - Administrador: liga as 3 novas, alcance "toda a rede";
   - Diretor e Professor: continuam desligadas, e o Administrador liga no painel o que decidir.
5. **Testes (PGlite, `supabase/tests/rls.test.mjs`):** os 164 atuais precisam continuar passando. Casos novos:
   - Administrador configurável da SMEDU cria e publica notícia;
   - Professor sem `conteudo.editar` não cria;
   - pessoa com só `conteudo.editar` cria rascunho mas não publica;
   - nada disso vaza para outra organização;
   - Jeriquara igual.

## Fora da migração, no mesmo pacote
- **Convite (`convidar-usuario`):** passa a aceitar um papel configurável (`papel_id`). Autoriza por `usuarios.vincular` (ou admin antigo) e grava o vínculo em `usuario_papeis` com o token de quem convida, como já faz com `membros`.
- **Painel:**
  - o acesso ao conteúdo passa a aceitar também as permissões novas (`podePublicar`/`isAdmin` derivados de `conteudo.publicar`/`organizacao.administrar`);
  - o convite com papel configurável ficou na tela **Vínculos** (quem só tem `usuarios.vincular` não abre a tela Usuários).

## Ordem de aplicação
1. Homologação (branch `kvilgamsyneenjtlllcf`): migração + função + painel. Depois, testes manuais com um usuário de teste da SMEDU.
2. Conferir Jeriquara na homologação (login de admin, editor e publicador antigos).
3. Produção: mesma migração. Em seguida, `npm run permissoes:sincronizar` com a chave de serviço.

## Fica para depois (fase 1C)
- Notícias com **escopo por unidade** (ex.: diretor publica só notícias da sua escola). Exige a coluna `unidade_id` em `publicacoes` e um ajuste no gatilho de publicação.
- Converter os papéis antigos de Jeriquara em papéis configuráveis, com a SECKE e a prefeitura.

## Situação
- Aprovado pelo William ("pode sim") em 15/10/2026 e aplicado na **homologação**: migração, função `convidar-usuario` (v4) e painel (na `main`). Testes de banco 183/183.
- **Falta:** conferir com usuário de teste da SMEDU e os logins antigos de Jeriquara (passos 1 e 2 da ordem acima) e, com nova aprovação, a produção (passo 3).

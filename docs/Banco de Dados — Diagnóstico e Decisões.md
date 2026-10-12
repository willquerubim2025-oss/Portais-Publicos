# Portal Educação Paulínia — Banco de Dados: Diagnóstico e Decisões

Oct 12, 2026 · Secke Sistemas

Registro do diagnóstico do projeto Supabase **Portal Municipal** (`qgywucdnaeheqndcxtho`) e das mudanças aplicadas para receber o Portal Educação.

## 1. Onde está cada coisa

| O quê | Onde |
| --- | --- |
| Banco de produção | Supabase `qgywucdnaeheqndcxtho` (sa-east-1) |
| Banco de homologação | Branch `homologacao`, projeto `kvilgamsyneenjtlllcf`. Toda migração vai primeiro para cá. |
| Migrações 0001–0015, testes de RLS, painel e portal genéricos | Repositório `willquerubim2025-oss/portal-municipal` (fonte da verdade da base) |
| Migrações novas do Portal Educação | `supabase/migrations/` deste repositório, com a mesma numeração da base |
| Patch para levar as migrações e os testes ao `portal-municipal` | `supabase/portal-municipal-0016-0017.patch` (`git apply` na raiz daquele repositório) |

Situação das migrações em 12/10/2026:

- **Homologação:** 0001–0017.
- **Produção:** 0001–0010, 0015, 0016 e 0017. **As migrações 0011–0014 (cache, verificação de links, exportação) ainda não foram aplicadas na produção.** Isso já era assim antes desta sessão; as novas migrações não dependem delas.

## 2. Diagnóstico (resumo)

- **Isolamento.** Toda tabela de conteúdo tem `municipio_id`, e as referências usam FK composta `(id, municipio_id)`: um registro não consegue apontar para dado de outra organização. As 34 tabelas têm RLS, o evento `rls_auto_enable` liga o RLS em toda tabela nova e nada é exposto sem `GRANT` explícito (D-13). O Storage separa por pasta `midias/{municipio_id}/`.
- **Papéis.** São fixos (`admin`, `publicador`, `editor`, enum `papel_usuario`) mais a `equipe_plataforma` (Secke). Não existe catálogo de permissões, escopo por unidade nem histórico de permissões: entram na próxima etapa.
- **Dados.** Em produção, só a Prefeitura de Jeriquara (outro cliente) e agora a SMEDU de Paulínia.

## 3. Decisão: a linha de `municipios` é a organização contratante (opção A)

Cada portal é uma organização isolada, seja uma prefeitura inteira, uma secretaria, uma câmara ou uma autarquia. **A SMEDU de Paulínia é uma organização própria**, com seus dados, usuários e domínio, totalmente separada de qualquer outra organização, inclusive de uma futura Prefeitura de Paulínia ou de outra secretaria da cidade.

- **Por quê.** O isolamento por `municipio_id` já está construído e testado: 90 policies, FKs compostas, Storage, busca e provisionamento. Criar um nível "órgão" abaixo do município exigiria reescrever tudo isso e mexer nos dados de Jeriquara, arriscando justamente a separação que funciona hoje.
- **Custo.** O nome da coluna `municipio_id` fica com sentido menos exato. É só semântica: a tabela foi documentada como "organização contratante".
- **Dentro da organização.** `orgaos` continua sendo o organograma (divisões e departamentos da SMEDU). Unidades escolares e o escopo do diretor entram em tabela própria na próxima etapa.

Migração **0017_organizacao_contratante**:

- **Colunas novas em `municipios`:**
  - `tipo_ente`: prefeitura, secretaria, câmara, autarquia, fundação, consórcio ou outro;
  - `cidade`;
  - `codigo_ibge`.
- **Identidade protegida:** o gatilho de identidade oficial (D-20) passou a proteger também esses três campos. Só a Secke os altera; o admin da organização continua alterando apenas `tema` e `config`.

Organização cadastrada pela Secke (dados, não migração; produção e homologação):

| Campo | Valor |
| --- | --- |
| slug | `paulinia-educacao` |
| nome | Secretaria Municipal de Educação de Paulínia |
| tipo_ente / cidade / UF | secretaria / Paulínia / SP |
| config.site_prefeitura | https://www.paulinia.sp.gov.br (link do botão "voltar ao site da Prefeitura"; confirmar) |
| Pacote padrão | 21 categorias, 3 menus, 6 páginas em rascunho, 18 seções da Central de Transparência |

Também foi preenchida a `cidade` de Jeriquara.

## 4. Correções de segurança (migração 0016_seguranca)

| # | Problema | Correção |
| --- | --- | --- |
| 1 | Admin de qualquer organização podia criar a ficha `perfis` de qualquer usuário, inclusive de outra organização (único ponto que cruzava organizações). | A policy exige que o usuário seja membro de uma organização da qual quem grava é admin. O convite (Edge Function `convidar-usuario`) grava o perfil com a chave de serviço e não é afetado. |
| 2 | Funções `SECURITY DEFINER` chamáveis pela API (`/rest/v1/rpc`): `is_plataforma`, `tem_papel`, `registrar_acesso_redirecionamento`. | Corpo movido para o schema `seguranca`, que não é exposto pela Data API. Em `public` ficam funções `SECURITY INVOKER` com o mesmo nome e assinatura: policies, painel e portal funcionam sem mudança. |
| 3 | A tabela `midias` era legível por qualquer visitante, de todas as organizações. O `storage_path` de anexos em rascunho (ex.: edital ainda não publicado) permitia baixá-los pelo bucket público. | O visitante só lê a mídia usada em conteúdo visível: notícia, destaque, evento ou documento publicado, ou órgão ativo. Membros da organização continuam vendo tudo. A checagem fica em `seguranca.midia_publica()`, porque uma consulta direta entraria em recursão com a policy de `documento_arquivos`. Imagens dentro do texto das notícias usam a URL do bucket e não dependem desta tabela. |
| 4 | Proteção contra senhas vazadas desligada no Auth. | **Pendente, é opção do painel do Supabase** (não há SQL para isso): Authentication → Sign In / Providers → Email → *Prevent use of leaked passwords*. Ligar na produção e na homologação. |

Mantidos de propósito:

- `categorias`, `menus` e `municipio_dominios` continuam com leitura pública: o portal precisa delas e não há dado sensível.
- O bucket `midias` continua público, por causa do cache longo na borda (D-15). Com a tabela fechada, o caminho de um arquivo em rascunho não é mais descobrível.

Os avisos de segurança do Supabase ficaram zerados na produção, exceto o item 4.

## 5. Testes

A suíte `supabase/tests/rls.test.mjs` do `portal-municipal` (PGlite, todas as migrações) passou de 98 para **114 verificações, 0 falhas**.

Os 16 testes novos cobrem:
- o perfil entre organizações;
- a ausência de funções `SECURITY DEFINER` chamáveis em `public`;
- o contador de redirecionamentos e as policies, que continuam funcionando para o visitante;
- a mídia de rascunho invisível ao visitante e a outra organização;
- a galeria da notícia publicada, que continua visível;
- a proteção de tipo, cidade e código IBGE contra o admin;
- a secretaria cadastrada como organização isolada da prefeitura.

## 6. Pendências

- [ ] Ligar a proteção contra senhas vazadas (item 4), na produção e na homologação.
- [ ] Aplicar o patch `supabase/portal-municipal-0016-0017.patch` no repositório `portal-municipal` (migrações + testes) e registrar lá a decisão (D-37) e o schema (doc 03), conforme o CLAUDE.md daquele repositório.
- [ ] O `CLAUDE.md` do `portal-municipal` diz que o repositório é privado, mas ele está **público** (contém inventário do site de Jeriquara e arquivos `.env.*` com chaves publicáveis). Avaliar torná-lo privado.
- [ ] Domínio do portal (`educacao.paulinia.sp.gov.br` sugerido) para cadastrar em `municipio_dominios`; sem ele, o portal não resolve a organização pelo endereço.
- [ ] Código IBGE de Paulínia e CNPJ da organização (deixados em branco até confirmação).
- [ ] O pacote padrão do provisionamento é pensado para prefeitura (Lei Orgânica, licitações, PPA etc.). Adaptá-lo por `tipo_ente` antes de publicar a Central de Transparência da SMEDU.
- [ ] Próxima etapa (plano a apresentar antes de aplicar): catálogo de permissões por papel com escopo e histórico; unidades escolares e vínculo escola → supervisor; equipe gestora; avisos com prioridade e frequência; prioridade nas publicações.

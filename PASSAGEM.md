# Passagem entre contas — Portal Educação Paulínia

William trabalha com **duas contas do Claude**, alternando por causa dos limites de uso. Este arquivo garante que nenhuma informação se perca na troca.

**Regra para o Claude, em qualquer conta:**
1. **Ao começar:** leia este arquivo inteiro antes de qualquer trabalho. Depois, leia o `CLAUDE.md` e os docs do repositório `portal-municipal` (seção "Onde está cada coisa").
2. **Ao terminar** (ou antes de o limite acabar): acrescente uma entrada no **topo** do "Diário das sessões", atualize o "Estado atual" e faça commit e push.
3. Use datas absolutas (dd/mm/aaaa). Escreva para quem não viu a conversa: o que foi feito, onde está, o que falta e qual é o próximo passo.

---

## Onde está cada coisa

| O quê | Onde |
|---|---|
| **Código do portal (Astro) e do painel (React)** | Repositório `willquerubim2025-oss/portal-municipal`, branch `main`, que já inclui o padrão visual aprovado (D-57 a D-75). O layout da SMEDU é o **"vitrine"**: `portal/src/components/vitrine/` e `portal/src/styles/vitrine.css` |
| **Decisões técnicas e de design (D-01 a D-80)** | `portal-municipal/docs/06-decisoes.md`. Não reabrir decisão sem motivo novo |
| **Pendências** | `portal-municipal/docs/07-pendencias.md` |
| **Regras do código** | `portal-municipal/CLAUDE.md` |
| **Especificação e contexto do Portal Educação** | Este repositório: `docs/Especificação do Brainstorm.md`, `docs/Arquivo de Contexto.md` |
| **Diagnóstico do banco e plano da fase 1** | Este repositório: `docs/Banco de Dados — Diagnóstico e Decisões.md`, `docs/Plano de Migração — Fase 1.md` |
| **Prévias navegáveis (HTML autocontido, abre sem internet)** | Este repositório: `docs/previa/` (`index.html` é a página inicial). Todas no padrão aprovado. Para gerá-las, veja `ferramentas/LEIA-ME.md` |
| **Sistema visual, marca e capturas** | Este repositório: `docs/design/` |
| **Roteiro do que falta para concluir** | Este repositório: `docs/Roteiro para Concluir.md` |
| **Pendências com a SMEDU (tudo o que depende da Secretaria/Prefeitura)** | Este repositório: `docs/reuniao/smedu-pendencias.md` |
| **Supabase, produção** | Projeto **Portal Municipal**, ref `qgywucdnaeheqndcxtho` (sa-east-1) |
| **Supabase, homologação** | **Não existe mais** (branch `homologacao` apagada em ~20/10/2026, D-105). Tudo roda na produção |
| **Site publicado (produção, D-105)** | Portal: https://portal-municipal.willquerubim2025.workers.dev · Painel: https://painel-municipal.willquerubim2025.workers.dev · Publicar: GitHub → Actions → "Publicar produção". Os endereços `*-homologacao` dão erro 500 (banco apagado): não usar |

### Branches deste repositório
- **`main` é a referência** (15/10/2026): contém todo o trabalho de 12 a 14/10, ou seja, docs, design, prévias, este arquivo e o `CLAUDE.md`. Comece sempre por ela.
- `claude/charming-cray-jecgm6` (conta 1) e `claude/fervent-turing-szzwyu` (conta 2) já estão contidos na `main`.
- No `portal-municipal`, a `main` também já tem todo o código do padrão visual (D-57 a D-75).

---

## Estado atual (atualizado em 27/10/2026)

> **Sistema de Pesquisas (27/10/2026): no ar e ligado ao cartão do portal.** Quem responde, painel do gestor, resultados, aprovação, Minhas respostas, grupos e administração prontos (repositório `pesquisas`, D-01 a D-64). Falta: envio automático por WhatsApp/e-mail (depende da Prefeitura; até lá o gestor manda o link à mão), assistente de IA (depende do de acordo), guia e apresentação, e os dados reais da SMEDU.

> **Apresentação impressa do Portal da Educação (25/10/2026, D-136 do `portal-municipal`):** `docs/portfolio/apresentacao/Portal-Educacao-Apresentacao.pdf`, 31 páginas A4, gerada por código (passo a passo no `LEIA-ME.md` da pasta). Substitui o portfólio antigo para entregar à Secretária. **Falta:** telefone e e-mail de contato na contracapa (marcadores `[telefone]` e `[e-mail]`).

> **CI Eletrônica (24/10/2026): pronta até onde não depende da Prefeitura.** Decisões D-69 a D-74 no repositório `ci-eletronica` (`docs/01`). Tela de Administração completa (unidades, pessoas e papéis, calendário com período, grupos, configuração, pedidos de ajuda, CIs só pela estrutura, importar pessoas por planilha, corrigir nome/e-mail); visual novo de cliente de e-mail corporativo (D-71/D-72; tela de entrada aprovada, não mexer); impressão/PDF com QR Code real, CI para fora, cancelar/retificar, exportar listas, "Esqueci a senha". Material para o futuro guia do administrador: `ci-eletronica/docs/06-material-para-o-guia.md` (atualizar a cada função nova). **Falta só o que depende da SMEDU/Prefeitura:** servidor de e-mail (avisos e lembretes), de acordo para usar IA, domínios para o login único e os dados reais (pessoas, cargos, iniciais, calendário, grupos), que o administrador já cadastra pela tela.


> **Atenção (21/10/2026):** de 18 a 22/10 o trabalho foi registrado só no `portal-municipal` (decisões **D-101 a D-126** em `docs/06-decisoes.md`; pendências em `docs/07-pendencias.md`). Resumo:
> - **Sem homologação (D-105):** a branch `homologacao` do Supabase foi apagada. Portal e painel rodam **só na produção** (endereços na tabela acima). O conteúdo da SMEDU foi restaurado do backup de 19/10 (D-106), inclusive os dados fictícios, que precisam sair antes do domínio oficial.
> - **Design de 20 e 21/10:** brasão maior (D-107, D-113 a D-115), cores configuráveis (D-109 a D-112), vídeos nas páginas de serviço (D-116 a D-120), bloco **Sistemas** na página inicial (D-121, D-122).
> - **CI Eletrônica (D-123, D-125):** **no ar desde 22/10/2026** em https://ci-eletronica.willquerubim2025.workers.dev e ligada ao cartão "CI Eletrônica" da página inicial. O painel do Supabase não aplicou o "Exposed schemas"; a lista de schemas foi gravada no banco (`pgrst.db_schemas` no papel `authenticator`, D-125). **Regra:** schema novo entra na tela Data API **e** nessa lista; erro `PGRST106` = conferir essa lista primeiro. Chamado ao Supabase pendente.
> - **Bloco Sistemas (D-126, 22/10):** caixa na largura das outras seções, círculos de 84 px; 6 sistemas, entre eles **Pesquisas da Educação** ("Em breve", a construir em 22/10).
> - Os itens abaixo que falam de homologação são de antes da D-105.


- **Jeriquara está fora (D-82):** dispensa não ganha; não fazer nada para Jeriquara. O produto é multi-organização; a organização em foco é a SMEDU.
- **Banco:** migrações 0001 a 0023 aplicadas na produção e na homologação. Permissões por papel, unidades, equipe gestora e página inicial configurável (fase 1A, D-38) já existem.
- **Permissões fase 1B (D-78/D-83):** 0021 e `convidar-usuario` na **homologação e na produção** desde 15/10/2026; conferida com usuários de teste na homologação. Plano: `docs/Plano de Migração — Fase 1B.md`.
- **Painel:** telas de permissões (D-77) e conteúdo por permissão (D-78) publicadas na homologação da Cloudflare (testado em 15/10/2026: login responde e aponta para a homologação).
- **Publicar homologação:** botão no GitHub (Actions → "Publicar homologação", D-79); segredos cadastrados e funcionando.
- **Portal Educação (layout vitrine):** página inicial pronta na homologação. Ordem dos blocos: destaque, Notícias, Em foco, Eventos, Serviços, Equipe gestora (D-56). A última decisão de design é a **D-56**.
- **Conteúdo fictício na homologação, para a apresentação:** equipe gestora, fotos `ficticio-*`, imagens do "Em foco" (Unsplash) e 6 dos 7 eventos. Tudo isso precisa ser removido antes de publicar (detalhes em `07-pendencias.md`).
- **Em andamento:** melhorias de design e layout do portal.
- **APROVADO pelo William em 14/10/2026 (D-75): padrão visual do cabeçalho claro (D-57 a D-74).**
  - Prévias: `docs/previa/` (desde D-76, uma só versão). Capturas: `docs/design/capturas/d57/`.
  - O código já está na `main` do `portal-municipal` e é o padrão do vitrine (D-76).
  - Para ligar na homologação: `config.cabecalho.estilo = 'claro'` e `config.cabecalho.botao = {"rotulo": "Fale com a Educação", "url": "/fale-com-o-supervisor"}` em `municipios` (slug `paulinia-educacao`, branch de homologação `kvilgamsyneenjtlllcf`). Depois, publicar o Worker de homologação.
  - D-58 (bloco de cima com 1290 px), D-60 (todo o conteúdo nessa largura), D-61 (seções sem fundo, régua na largura do conteúdo), D-62 (fonte Raleway no cabeçalho, `tema.fonte_cabecalho = 'Raleway'`), D-63/D-64 (cabeçalho em uma linha; largura de 1290 px; menu sem Agenda e Transparência — remover no banco), D-65 (títulos das seções sem faixa), D-66 (destaque deslizando; botão "Fale com a Educação"), D-67 (Serviços no estilo do modelo), D-68 (destaque a cada 4,5 s), D-69 (cabeçalho 10% mais alto), D-70 (Em foco mais perto das Notícias), D-71 (sem a faixa colorida), D-72 (rodapé no estilo da Prefeitura), D-73 (revisão do celular), D-74 (moldura verde nos cards de Serviços) e D-59 (Notícias com 3 cards, `config.home.noticias_fileira = 3`) estão no mesmo branch.
  - ~~Remover Agenda e Transparência do menu da SMEDU na homologação~~ (feito em 15/10/2026). O cabeçalho está em uma linha (brasão + nome, 6 itens do menu, lupa, botão), conferido de 1280 a 1920 px.
- **Fonte Raleway em todo o portal da SMEDU (homologação):** `tema.fonte_texto` e `tema.fonte_titulos` = Raleway desde 15/10/2026, a pedido do William (ele quer manter). Era Prompt.
- **D-81 (menu em 0,8rem) foi revertida** no mesmo dia, a pedido do William: o tamanho do menu do cabeçalho continua 0,88rem. Não mexer no CSS do cabeçalho sem pedido explícito.
- Veja também as propostas abertas abaixo.

### Propostas de design da revisão de 14/10/2026 (tratadas em 15/10/2026: ver D-84 a D-86 no `portal-municipal`)
1. **Espaços vazios entre as seções:** antes de cada régua de título há uma faixa vazia de cerca de 70 px, com o fundo da seção anterior ou seguinte. A régua deveria colar no início da seção.
2. **Cabeçalho no celular:** o botão de acessibilidade fica por cima da palavra "Educação" no nome da Secretaria.
3. **Notícias no celular:** os 7 cards ficam empilhados com foto grande, e a seção ocupa várias telas. Opções: carrossel com deslize lateral, ou cards compactos com foto pequena ao lado.
4. **Destaque:** a imagem tem cantos arredondados, margens brancas e uma emenda com o cinza das Notícias. A especificação pede largura total, de ponta a ponta.
5. **Rodapé:** a metade direita fica vazia. Pode receber o brasão, o link para o site da Prefeitura (pedido na especificação, 3.1), redes sociais e acessibilidade.
6. **Equipe gestora:** o último card das divisões fica sozinho numa linha. Os avatares podem ganhar as iniciais (a especificação, 3.7, sugere iniciais sobre a cor do portal).

---

## Avisos técnicos

- **Rede do ambiente na nuvem:** na conta usada em 14/10/2026, a política de rede do ambiente bloqueia `*.supabase.co` e `workers.cloudflare.com`. Com isso, o `npm run dev` do portal não carrega os dados (erro de DNS no workerd). As ferramentas MCP do Supabase funcionam normalmente. Para ver o portal ao vivo nessa conta, é preciso liberar esses domínios em "Network access" do ambiente (https://code.claude.com/docs/en/cloud-environments#network-access). Enquanto isso, dá para avaliar o visual pelas prévias de `docs/previa/`.
- O `.env` do `portal/` nunca vai para o git (D-25). Os valores da homologação estão em `portal/.env.example` e `portal/wrangler.jsonc` (a chave publicável não é segredo).

---

## Diário das sessões (mais recente no topo)

### 27/10/2026 (tarde) — sessão `affectionate-maxwell`
- **Pesquisas:** assistente de IA funcionando com a chave paga e testado (criar conversando, ditar perguntas, colar questionário pronto, ajustes; D-65/D-66); opção "Vale sozinha" em várias escolhas (D-67, regra também no banco). William vai testar o que está pronto.
- **Falta (Pesquisas):** (1) envio automático por WhatsApp e e-mail, a construir pronto para ligar; (2) Guia do Usuário e apresentação impressa (molde D-137); (3) da SMEDU/Prefeitura: WhatsApp oficial, servidor de e-mail, de acordo da IA, lista de pessoas, quem aprova pela Secretaria, tipos/etapas oficiais; (4) antes de abrir: tirar a conta de teste, encerrar as demonstrações, conferir o schema `pesquisa` na tela Data API, domínio oficial.
- **Duas decisões pendentes com o William** (`pesquisas/docs/01`): **Q-29** pesquisa permanente (sem data de fim) e **Q-25** publicar resultado no portal.
- **Próximo passo:** depois do teste do William, envio automático pronto para ligar e, em seguida, o guia e a apresentação.

### 26 e 27/10/2026 — sessão `affectionate-maxwell`
- **Pesquisas, passos 3 e 4 no ar** (https://pesquisas.willquerubim2025.workers.dev):
  - **Resultados:** gráficos por pergunta, filtros (tipo, região, etapa, unidade), "Comparar", modo apresentação, PDF e planilha.
  - **Aprovação** de pesquisa para pais e comunidade pelo link `/aprovar/...` (aprovar ou devolver com comentário, D-62) e portal do destinatário "Minhas respostas".
  - **Grupos** (criar com segmentos, "quem, e onde", escolas, pessoas e exceções; compartilhar com outro gestor).
  - **Administração:** pessoas com contato e lotação, importar planilha colando do Excel, papéis pelo e-mail do portal, segmentos, escolas e setores, envelope das pesquisas e "passar para outro gestor", configuração e histórico (D-63).
  - Migrações `pesquisa_0011` a `pesquisa_0013` aplicadas e testadas em transação desfeita.
- **Cartão "Pesquisas da Educação" ligado no portal** (D-64 de `pesquisas`): saiu do "Em breve" e abre o sistema (público servidor).
- **Assistente de IA pronto (27/10, D-65/D-66 de `pesquisas`):** "Criar com o assistente" (montar a pesquisa conversando ou colando um questionário pronto) e o assistente do editor com sugestões e "Ver como ficaria". Edge Function `pesquisa-ia` no ar. **Funcionando desde 27/10:** chave paga guardada pelo William nos segredos do Supabase (`ANTHROPIC_API_KEY`); IA ligada na SMEDU só para teste (gestores hoje: William e conta de teste). Antes de criar outros gestores, ter o de acordo da Secretaria ou desligar em Administração → Configuração.
- **Antes de ir ao ar de verdade:** cadastrar as pessoas da SMEDU (planilha), escolher quem aprova pela Secretaria (Administração → Configuração), tirar a conta de teste e encerrar as pesquisas "(demonstração)".
- **Próximo passo:** envio automático (WhatsApp e e-mail, depende da conta oficial e do SMTP da Prefeitura) e assistente de IA prontos para ligar; depois o Guia do Usuário e a apresentação impressa (molde D-137).

### 25/10/2026 — sessão `peaceful-edison`, conta 2
- **Autorizações do Supabase automáticas:** `.claude/settings.json` + `.claude/hooks/supabase-guard.py`. Leitura, consultas e alterações de dados (SELECT, INSERT, UPDATE/DELETE com WHERE), logs, advisors, tipos, branches e deploy de Edge Function passam sem perguntar. **Pergunta antes:** CREATE/ALTER/DROP/TRUNCATE, RLS e políticas, GRANT/REVOKE, blocos DO, UPDATE/DELETE sem WHERE, `apply_migration`, `merge_branch`, `reset_branch`, `delete_branch`, pausar/criar projeto, segredos e qualquer ferramenta nova. Vale a partir da próxima sessão. Para outro projeto, copiar a pasta `.claude/` para o repositório dele e fazer commit.

### 25/10/2026 — sessão `affectionate-maxwell`, computador de casa
- **Apresentação impressa do Portal da Educação (D-136 do `portal-municipal`):** `docs/portfolio/apresentacao/`. Página inicial dividida em 4 partes (página de imagem + página de explicação), destaque de abertura, matrícula com vídeos, serviços, notícias, transparência, acessibilidade, celular, integração com os sistemas e a CI Eletrônica, painel (papéis, cores, destaques, menus), perguntas sobre segurança, problemas e o que fazer e, por último, a tecnologia. Fotos tiradas do portal publicado; refazer com `fonte/capturar.cjs`, `fonte/preparar.py` e `fonte/montar.py`.
- **Sistema de Pesquisas — levantamento fechado:** repositório novo `willquerubim2025-oss/pesquisas` (privado). Decisões D-01 a D-55 em `docs/01-levantamento-de-requisitos.md`; resumo e 8 regras em `docs/02-funcionalidades-consolidadas.md`. Banco no Supabase Portal Municipal, schema `pesquisa`, autônomo e destacável (D-43). WhatsApp oficial: item 21 de `docs/reuniao/smedu-pendencias.md`.
- **Protótipo aprovado** (`pesquisas/prototipo/index.html`, 5 telas) e modelo de dados em `pesquisas/docs/04-modelo-de-dados.md`.
- **Banco pronto e testado (26/10, D-60 de `pesquisas`):** migrações `pesquisa_0001` a `pesquisa_0007` aplicadas no Supabase principal; regras testadas em transação desfeita, tudo passou. Situação, testes e pendências em `pesquisas/docs/04`, seção 10. Falta marcar o schema `pesquisa` na tela Data API do Supabase.
- **Aplicativo, passo 1 pronto (26/10):** tela de quem responde em `pesquisas/app` (link pessoal `/r/:token`, pesquisa aberta `/p/:id`, comprovante `/v/:codigo`), testada com o banco. Duas pesquisas "(demonstração)" no banco. **No ar** em https://pesquisas.willquerubim2025.workers.dev (segredos da Cloudflare cadastrados no repositório `pesquisas`).
- **Painel do gestor no ar (26/10, passo 2):** entrar, Início com situação/lembrar/parciais/"Mandar à mão" (D-61), Minhas pesquisas, editor completo, Para quem, enviar. Conta de teste `teste.pesquisas@secke.dev` (gestora) só para testes: tirar antes de ir ao ar.
- **Próximo passo:** resultados completos (passo 3: gráficos, comparar, PDF, planilha), depois grupos e administração (4), envio automático e IA (5).

### 24/10/2026 — sessão `affectionate-maxwell`, computador de casa
- **CI testada com login:** modelo do e-mail "Magic Link" com o código `{{ .Token }}` (feito pelo William); PIN criado.
- **CI Eletrônica — D-69 a D-74 (`ci-eletronica/docs/01`):** Administração (migrações 0033 e 0034 aplicadas na produção); material do guia do administrador (D-70); redesenho em estilo de cliente de e-mail (D-71) e ajustes de zonas/resumo (D-72); impressão e PDF com QR Code, CI para fora, cancelar e retificar (D-73); pedidos de ajuda, CIs (estrutura), exportação, período no calendário, importação por planilha, "Esqueci a senha", timbre vindo do cadastro do portal (D-74). Correção de sessão vencida ("JWT expired").
- **Portal — D-134:** Edge Function `alterar-pessoa` (corrige nome e e-mail/login; recusa quem atende outra organização).
- **Guia do Usuário da CI (D-75):** `ci-eletronica/docs/guia/Guia-CI-Eletronica.pdf`, 57 páginas, uma unidade por papel (operador, gestor, administrador), gerado por código com as telas reais e dados fictícios. Padrão para todos os manuais: D-135 no `portal-municipal`.
- **Próximo passo:** a CI fica parada esperando a SMEDU (servidor de e-mail, de acordo com IA, domínios, lista de pessoas). **Próximo sistema satélite: Pesquisas da Educação.**


### 22/10/2026 (tarde) — sessão `affectionate-maxwell`
- **Material de portfólio:** `docs/portfolio/Portal-Educacao-Paulinia-SECKE.pdf` (28 páginas): capa, visão geral de tudo o que o portal tem (cidadão, comunicação, transparência, acessibilidade, painel, tecnologia, sistemas integrados) e uma folha por página do portal (26), com título, descrição e captura da página inteira, tiradas do portal publicado em 22/10. Também existe uma apresentação de vendas em slides (artifact privado no Claude do William).
- **Portal (D-127 a D-133 no `portal-municipal`):** só o brasão no cabeçalho, 20% menor; moldura branca nos cards de notícia (página inicial e /noticias, com o fundo da página inicial); destaque com "arte pronta" e a arte "Novo Portal da Educação" como 1º slide (2000 × 722, preenche a área no computador); "Em foco" 1 cm mais abaixo; faixa vermelha de homologação escondida (`config.faixa_homologacao = false`; o portal continua fora do Google).

### 22/10/2026 (manhã) — sessão `affectionate-maxwell`, computador do trabalho
- **CI Eletrônica no ar:** banco da CI aplicado na produção (versão consolidada, D-66 do repositório `ci-eletronica`), SMEDU configurada (63 caixas; William gestor de 2 caixas, iniciais WQ), aplicativo publicado pela rotina "Publicar produção" do `ci-eletronica` (segredos da Cloudflare cadastrados pelo William). Cartão do portal virou link.
- **D-125:** o "Exposed schemas" do Supabase foi salvo, mas não aplicado (nem com reinício do projeto). Contorno aprovado: `alter role authenticator set pgrst.db_schemas = 'public, graphql_public, ci'`. Segurança conferida (visitante só usa `ci.verificar`). Pendência: chamado ao Supabase e depois desfazer o contorno.
- **D-126:** seção Sistemas na largura das outras seções, círculos e textos menores; novo cartão **Pesquisas da Educação** (em breve).
- **Falta:** testar a CI com login (o William entra com o e-mail e a senha do painel); o e-mail "Magic Link" do Supabase precisa mostrar o código `{{ .Token }}` para a criação do PIN; endereço do sistema de pesquisas quando estiver pronto.

### 22/10/2026 — sessão `nifty-lamport`, computador de casa
- **D-124, tela dos vídeos dos serviços no painel** (pendência da D-116), na `main` do `portal-municipal`: Carta de Serviços → editar serviço → "Vídeos explicativos". Envia o vídeo (MP4/WebM, até 50 MB, até 6), gera a capa sozinha, ordena, edita o título da seção e o texto de apoio com botão ao lado de cada vídeo. Testado com o Supabase simulado (17 verificações, axe limpo).
- **Painel de produção publicado** (rotina "Publicar produção" #23, verde). **Falta:** o William abrir a Matrícula Escolar no painel e conferir os 2 vídeos com o banco real.
- Visto no teste: o menu lateral do painel passa da largura no celular (anotado em `07-pendencias.md`).

### 21/10/2026 (noite) — sessão `nifty-lamport`, computador de casa
- Conferido o GitHub: as `main` dos dois repositórios estão em dia (código até a D-123). Este arquivo estava parado em 17/10 e foi atualizado (aviso no "Estado atual" e endereços da produção na tabela).
- Produção no ar: portal (início, notícias, serviços) e painel respondem 200. Homologação dá 500, esperado (banco apagado, D-105).
- CI Eletrônica: o schema `ci` continua fora da API (`PGRST106`, só `public` e `graphql_public`).
- O usuário de teste `redator.teste@secke.dev` (15/10) ficava na homologação e foi apagado junto com ela.

### 17/10/2026 — sessão `great-newton`
- **Revisão das páginas internas** e, com o OK do William ("manda bala"), **D-100**: Carta de Serviços em cards, coluna lateral (Nesta seção, Mais procurados, Atendimento) em páginas, serviços e órgãos, **foto de capa** opcional em páginas e serviços (migração 0027, aplicada pelo William nos dois bancos), resumo da notícia sem repetição, link interno de serviço na mesma aba. Tudo no ar na homologação; axe sem violações.
- **Manual do portal e do painel** (pedido do William): `docs/manual/index.html` + 41 fotos em `docs/manual/img/` (homologação). Portal seção por seção, painel, perfis e permissões, passo a passo (notícia, edição, foto, escola, avisos, pessoas), quem acessa o quê; pendências marcadas em âmbar (falta definir) e violeta (falta implementar). Publicado como página privada: https://claude.ai/artifact/HPTDxtqfr8YC6gYS4pHZHW. Ao mudar o painel, atualizar o manual.
- **Próximo satélite: CI eletrônica**, que o William começou em outro projeto.
- **Conteúdo provisório** com dado público: 9 perguntas frequentes, 5 leis federais de referência, competências dos 4 órgãos, capas em Sobre, Área do Estudante e Matrícula. Item 20 de `smedu-pendencias.md`.

### 16/10/2026 (tarde) — sessão `great-newton`
- **Cópia dos arquivos (D-96) configurada pelo William** (bucket `portal-municipal-arquivos` na conta Cloudflare da Secke, mesma do backup do banco; só produção) e verde. **Senha do backup trocada** e guardada no gerenciador do Google; backup #18 verde. **VLibras conferido.** Falta só o UptimeRobot.
- **D-97, notícias das unidades (fase 1C):** migração `0026_noticias_por_unidade.sql` (257 testes ok), painel (campo "Unidade" no editor; quem só tem permissão na escola vê só Notícias) e portal (nome da unidade na notícia). **0026 aplicada pelo William nos dois bancos (conferido); painel e portal da homologação publicados; baterias `noticias` (20) e `escola` (15) com 0 falhas.** Contas de teste a apagar antes da ida ao ar: lista na D-98. Pergunta à SMEDU: item 19 de `smedu-pendencias.md`.
- **D-98, testes automáticos do painel na SMEDU:** baterias reescritas, sem senhas no código (`painel/e2e/.env.e2e`, fora do git; modelo `.env.e2e.exemplo`). Conta `redator.e2e@secke.dev` criada por `node e2e/preparar.mjs`. Conteúdo 31, estrutura 26, administração 19, notícias 20, escola 15: **0 falhas**; limpeza feita. O arquivo de senhas dos testes (`painel/e2e/.env.e2e`) fica só no computador onde foi criado: em outro, copiar o modelo e preencher.
- **D-99, contraste de todas as cores do layout** na Identidade visual do painel. Achou a cor coral da SMEDU em 4,49:1; trocada para `#bd3f2c` na homologação.

### 16/10/2026 (manhã) — sessão `great-newton`
- **Redator x administrador:** William entrou como redator e não viu o painel completo. É o esperado: o menu sai das permissões; o "Redator (teste)" só tem `conteudo.editar`. O painel completo é o do `admin.teste@secke.dev`.
- **Auditoria técnica da homologação:** Security e Performance Advisors da produção revisados (nada urgente; registro em `07-pendencias.md`). Lighthouse no celular: acessibilidade 100, boas práticas 96, velocidade 90 (início) e 97 (notícias). SEO conferido (sitemap, robots, canônico, Open Graph, JSON-LD).
- **D-95:** a página de Serviços no celular "pulava" (CLS 0,49) porque o menu e os avisos eram fechados pelo JavaScript depois de pintar. Corrigido (CLS < 0,02). O sitemap ganhou "Fale com o supervisor" quando há escolas. **Importação de redirecionamentos em lote** no painel (Redirecionamentos → "Importar uma lista", CSV `endereço antigo;leva para;tipo`), testada de ponta a ponta. Publicado na homologação.
- **D-96:** rotina nova `backup-arquivos.yml` (cópia diária das fotos e PDFs do Storage para o R2, sem apagar nada). **Configurada pelo William em 16/10** (só produção; bucket `portal-municipal-arquivos` na conta Cloudflare da Secke, a mesma do backup do banco) e primeira execução verde. O backup diário do banco está verde desde 05/10.
- **Jeriquara fora das instruções (pedido do William):** os READMEs, o checklist e o doc de backup ainda citavam Jeriquara (textos de antes da D-82). Corrigido; regra nova nos dois `CLAUDE.md`. A cópia dos arquivos (D-96) é **só da produção**: a homologação tem ~7,4 GB de arquivos de Jeriquara, que não devem ir para o R2.
- **Senha do backup (`BACKUP_SENHA`):** a original não estava guardada; William criou outra, guardou no gerenciador de senhas do Google e trocou no GitHub (16/10). Backup #18 verde. Backups de antes de 16/10 não abrem (expiram até 15/11). **VLibras conferido** pelo William no navegador. Falta só o UptimeRobot.
- **Testes automáticos do painel (`npm run e2e`):** ainda usam os usuários e textos de Jeriquara (um deles troca o slogan da organização). Não rodar. Precisam ser adaptados para a SMEDU antes de valer como critério de ir ao ar.

### 15/10/2026 (tarde) — sessão `great-newton`
- **Cabeçalho da SMEDU arrumado (homologação).** Numa sessão paralela, um pedido pelo chat gerou a D-81 (menu menor no CSS) e a troca das fontes para Raleway; a D-81 foi revertida lá mesmo. O menu continuava em duas linhas porque **Agenda e Transparência nunca tinham saído do banco** (pendência desde a D-64). William apagou os dois itens pelo SQL Editor (branch homologacao). Conferido: 6 itens, uma linha só, menu em 0,88rem, Raleway mantida.
- **Exclusões pelo MCP do Supabase não funcionam na sessão na nuvem:** o `DELETE` sempre excede 60 s (o conector pede confirmação para comando destrutivo e o pedido não aparece). Mesmo depois de o William liberar as permissões nos conectores, continuou igual nesta sessão (talvez valha só para sessões novas). Contorno: SQL Editor do Supabase, escolhendo a branch **homologacao** no topo.
- **Administrador de teste da SMEDU criado na homologação:** `admin.teste@secke.dev` (papel Administrador; senha passada ao William na conversa). Login e `is_admin` conferidos. Antes não havia administrador, e o painel não editava os Menus da SMEDU. **Apagar antes de qualquer uso real**, junto com o redator.
- Docs do `portal-municipal` atualizados (`07-pendencias.md`, nota na D-81), na `main`.
- **Fase 1B conferida na homologação (aprovada pelo William):** o redator edita rascunho e não tem opção de publicar; no banco, publicar com o login dele é recusado. O admin publicou e despublicou; o portal atualiza em ~1 min (cache). Notícia "Teste de notícia" ficou despublicada (pode apagar).
- Visto no teste: notícia sem foto no card grande vira um bloco branco. Proposta de imagem padrão, aguardando o William.
- **Fase 1B na produção (D-83, aprovada pelo William):** 0021 aplicada, `convidar-usuario` publicada (v2 na produção, mesmo código da v4 da homologação). Sincronizar não foi preciso: o catálogo da produção já é igual ao do código.
- **Jeriquara fora do projeto (D-82):** a dispensa não foi ganha; o site de Jeriquara não será feito. Dados ficam no banco sem manutenção: **não testar, conferir nem planejar nada para Jeriquara.** O produto é multi-organização; o foco é a SMEDU. Registrado no `CLAUDE.md` e nos docs do `portal-municipal`.
- **Fotos novas do "Em foco" na homologação:** `carga/foco-matricula-2.jpg` e `carga/foco-bolsa-2.jpg` (enviadas com o admin de teste pela API do Storage), `config.home.foco` e textos alternativos trocados. Antes de ir ao ar: autorização de imagem da foto da criança.
- **Design (publicado na homologação, rotina #5):** D-84 notícia sem foto com imagem padrão; D-85 Notícias no celular em lista compacta (página a 390 px: de ~8.740 para ~7.510 px); D-86 equipe ocupa a fileira inteira. Das 6 propostas de 14/10: 2 e 5 já estavam resolvidas (D-73, D-72), 1 já reduzida (D-61/D-70) e **4 (destaque de ponta a ponta) não foi feita porque contraria a D-58**, aprovada pelo William. Conferido: 0 problemas de 320 a 768 px e axe sem violações.
- **Dica técnica:** nesta sessão o `npm run dev` do portal funcionou com os dados da homologação (`.env` com `DOMINIO_DEV=educacao.paulinia.teste`).
- **D-87:** cabeçalho branco 15% mais alto no computador (116 → 133 px, a partir de 1181 px; celular igual), a pedido do William. Publicado na homologação.
- **Revisão das páginas internas (15/10/2026):** 21 endereços, no computador e no celular: acessibilidade (axe) sem violações e sem rolagem horizontal. Problema achado: os links do rodapé **Acesso à Informação, Ouvidoria e Privacidade** abrem "página não encontrada", porque as páginas estão em rascunho e dependem de dados da Prefeitura (pedidos no item 8 de `docs/reuniao/smedu-pendencias.md`). A página de **Acessibilidade** foi escrita e publicada na homologação.
- **Documento único de pendências com a SMEDU (D-89):** `docs/reuniao/smedu-pendencias.md` (era `smedu-dados-a-confirmar.md`), com 16 itens, resumo e o que está provisório no site. Regra do William: não parar esperando a Prefeitura; usar dado público, foto de banco ou placeholder e marcar no documento. Só parar se travar.
- **Páginas legais publicadas (provisórias):** Ouvidoria, Acesso à Informação e Privacidade, com dados públicos da Ouvidoria da Prefeitura (item 8 do documento). Os 4 links do rodapé funcionam; axe sem violações.
- **D-88:** Raleway em todo o portal da SMEDU (decisão do William).
- **Bolsa de Estudo preenchida (provisória)** com os dados públicos do Programa Bolsa Educação (item 13).
- **D-90, Transparência por tipo de organização:** migração `0022_pacote_por_tipo_ente` no `portal-municipal` (pacote de secretaria; a SMEDU perde as 18 seções de prefeitura vazias e ganha 9 próprias, com "Contas Públicas" levando ao site da Prefeitura). 198 testes ok. **Aplicada na homologação** pelo William (SQL Editor) e portal publicado (rotina #8): Transparência com 9 seções de secretaria e "Legislação" sem "municipal". Produção: falta, com aprovação.
- **Conteúdo provisório (15/10):** Matrícula com as datas de 2027 (item 5), Área do Estudante montada e Ouvidoria ativa nos Serviços (item 15), Bolsa com o período do PAS (19/10 a 11/12). Nenhum card "Em breve" na home.
- **"Sobre a Secretaria"** escrita (provisória, dados públicos), publicada e no menu "A Secretaria".
- **Prévias novas:** `docs/previa/` agora é capturada do portal publicado (`ferramentas/capturar_previa.py`): 24 páginas, abrem sem internet.
- **D-91, pré-visualização de rascunho:** botão "Pré-visualizar no site" no editor de notícias; link temporário (30 min) em `/previa/<token>`. Migração `0023_previa_rascunho`. 208 testes ok.
- **Migrações aplicadas pelo William no SQL Editor (15/10):** `0022` e `0023` na **produção** e na **homologação** (conferido nos dois bancos). Painel e portal da homologação publicados; pré-visualização testada de ponta a ponta. **O MCP do Supabase não aplica migração nesta conta (sempre excede o tempo): usar o SQL Editor, com atenção ao seletor de branch no topo.**
- **D-92, biblioteca de mídias (16/10):** no campo de imagem do painel (notícias, eventos, banners, identidade, órgãos, equipe, unidades), "Escolher da biblioteca": janela com as imagens já enviadas, busca e 24 por página. Testada no painel (axe ok) e publicada. As fotos novas do "Em foco" foram cadastradas em `midias` para aparecer na biblioteca.
- **D-93 (16/10):** pré-visualização também em páginas, serviços e eventos (migração `0024`, 218 testes ok) e biblioteca de mídias também na galeria e no editor de texto (testadas no painel local). **Falta: o William rodar a `0024` no SQL Editor nos dois bancos; depois publicar painel e portal** (o portal novo chama `previa_conteudo`, que só existe depois da 0024: não publicar antes).
- **Roteiro completo do que falta:** `docs/Roteiro para Concluir.md` (16/10), com foco no acesso dos servidores e nos sistemas satélites. Novo item 18 em `smedu-pendencias.md` (sistemas que os servidores usam).
- **D-94 (16/10):** "Meus sistemas" no painel (migração 0025, 227 testes ok), link "Acesso do servidor" no rodapé do portal e VLibras. **0024 e 0025 aplicadas nos dois bancos; painel e portal da homologação publicados e testados (16/10).**
- **Banco:** migrações 0001 a 0025 na produção e na homologação.
- **Painel:** os sistemas ganharam item próprio no menu, **Estrutura → Sistemas** (a aba em Transparência continua). Publicado e conferido.
- **Acesso de teste à homologação:** `admin.teste@secke.dev` (senha passada ao William na conversa; não fica no git).
- **Próximo passo:** William conferir o VLibras no navegador; pacote padrão para câmara e autarquia; o resto depende da SMEDU (`smedu-pendencias.md`) ou da ida ao ar (`Roteiro para Concluir.md`). Depende da SMEDU: ver `docs/reuniao/smedu-pendencias.md`.

### 15/10/2026 — sessão `nifty-lamport`
- **Teste da Cloudflare (homologação), tudo funcionando:**
  - portal (`/` e `/noticias`) responde 200, carrega as notícias do banco, sem imagens quebradas nem erros no console;
  - painel abre a tela "Entrar" e fala com o Supabase de **homologação** (`kvilgamsyneenjtlllcf`): um login inválido de propósito devolveu "E-mail ou senha incorretos".
- **Redirect URLs (Supabase, homologação):** William incluiu `https://painel-municipal-homologacao.willquerubim2025.workers.dev/**` em 15/10/2026. A entrada antiga do endereço de antes da D-80 foi removida; a de `localhost:5190` fica, para testar o painel no computador.
- **Usuário de teste da fase 1B (só homologação):** `redator.teste@secke.dev`, papel novo **"Redator (teste)"** (`redator-teste`) da SMEDU, só com `conteudo.editar` (rede); não está em `membros`. A senha foi passada ao William na conversa. Login conferido no painel publicado: o menu mostra só as telas de conteúdo (Notícias, Documentos, Páginas, Serviços, Agenda, Perguntas, Banners, Chamados), sem as de administração. **Apagar o usuário e o papel antes de qualquer uso real.**
- **Ainda falta:** William testar com esse usuário e, com aprovação, levar a 0021 e a função `convidar-usuario` v4 à produção.

### 16/10/2026 — conta 2 (sessão `fervent-turing`)
- **Publicação da homologação por botão (D-79):** rotina `.github/workflows/publicar-homologacao.yml` no `portal-municipal` (na `main`). Em GitHub → Actions → "Publicar homologação" → Run workflow, escolhe painel, portal ou os dois. Só homologação; a produção continua manual.
- **Segredos cadastrados e rotina rodada com sucesso (execução #2, painel e portal verdes).** A #1 falhou porque o `CLOUDFLARE_ACCOUNT_ID` foi colado com uma quebra de linha; a rotina agora limpa espaços e quebras dos segredos. Depois, incluir o endereço do painel de homologação em Redirect URLs do Supabase (branch de homologação).
- **Endereços (D-80, conta pessoal, escolha do William):** portal https://portal-municipal-homologacao.willquerubim2025.workers.dev (cadastrado no banco para a SMEDU) e painel https://painel-municipal-homologacao.willquerubim2025.workers.dev. Falta o William incluir `https://painel-municipal-homologacao.willquerubim2025.workers.dev/**` nas Redirect URLs do Supabase (branch homologacao).
- **Produção da fase 1B:** não aplicada. William ainda não confirmou; o combinado é testar antes na homologação com o painel publicado.

### 15/10/2026 (manhã) — conta 2 (sessão `fervent-turing`)
- **Fase 1B aprovada ("pode sim") e aplicada na homologação (D-78)**; código na `main` do `portal-municipal`:
  - migration `0021_permissoes_conteudo`: 3 permissões novas (`conteudo.editar`, `conteudo.publicar`, `organizacao.administrar`); `is_membro`, `pode_publicar` e `is_admin` aceitam o papel antigo **ou** essas permissões; colegas visíveis por `usuario_papeis`; o Administrador de cada organização recebe as três;
  - testes de banco: 183/183 (19 novos);
  - painel: `nivel` no AuthContext (papel antigo ou permissão equivalente) rege menu, rotas e publicação; convite com papel configurável na tela **Vínculos** ("Dar papel a alguém" com o e-mail de quem não tem conta);
  - função `convidar-usuario` v4 publicada na homologação (aceita `papel_id`).
  - Conferido na homologação: catálogo, Administradores com as três, política de `perfis`, admin antigo de Jeriquara igual. Ainda não há vínculos configuráveis lá, então ninguém mudou de acesso.
- **Próximo passo:** publicar o painel de homologação (Cloudflare) e testar com um usuário da SMEDU que tenha só `conteudo.editar`; conferir os logins antigos de Jeriquara. Depois, **com aprovação do William**, levar a 0021 e a função à produção e rodar `npm run permissoes:sincronizar`.

### 15/10/2026 (madrugada, 3) — conta 2 (sessão `fervent-turing`)
- **Painel administrativo, parte A (D-77)**, já na `main` do `portal-municipal`:
  - telas de Papéis e permissões, Vínculos de usuários, Unidades e regiões e Equipe gestora;
  - menu e rotas montados pelas permissões;
  - registro das permissões no código (`painel/src/lib/permissoes.catalogo.json`) e `npm run permissoes:sincronizar`.
  - Testado com Playwright e o Supabase simulado: 8 telas, axe limpo, gravações conferidas, Jeriquara igual.
- **Fase 1B: plano escrito, aguardando aprovação do William:** `docs/Plano de Migração — Fase 1B.md`. A ideia é ampliar `is_membro`, `pode_publicar` e `is_admin` com 3 permissões novas, em vez de reescrever ~70 políticas.
- **Próximo passo:** com a aprovação, escrever a 0021 com testes no PGlite, aplicar na homologação e ajustar o convite e o painel. Também falta publicar o painel e o portal de homologação (Cloudflare) e rodar o sincronizar com a chave de serviço.

### 15/10/2026 (madrugada, 2) — conta 2 (sessão `fervent-turing`)
- D-76, a pedido do William ("não faz sentido continuar com dois lugares"): **uma só versão**.
  - **Prévias:** `docs/previa/` agora contém as 15 páginas no padrão aprovado, com os nomes originais. Saíram `cabecalho-claro.html`, `docs/previa/claro/`, os testes de cor `cabecalho-00a693-*` e o zip antigo. A prévia de 13/10 ficou só como base da ferramenta, em `ferramentas/base-previa-13-10/`.
  - **Código:** no `portal-municipal`, o cabeçalho claro passou a ser o **padrão do layout vitrine**. Não depende mais de `config.cabecalho.estilo = 'claro'`; o cabeçalho antigo em carrossel só volta com `estilo: 'carrossel'`.

### 15/10/2026 (madrugada) — conta 2 (sessão `fervent-turing`)
- Com a autorização do William, o branch `claude/fervent-turing-szzwyu` foi juntado na **`main`** dos dois repositórios (avanço direto, sem conflitos; build conferido antes). A `main` é a referência a partir de agora.
- **Próximo passo:** publicar o Worker de homologação (precisa de Cloudflare) e começar o painel administrativo (permissões fase 1B).

### 14/10/2026 (fim da noite) — conta 2 (sessão `fervent-turing`)
- **William aprovou o padrão visual** (D-75): "é a cara do portal". As próximas páginas seguem esse padrão.
- **Homologação:** configuração ligada pelo MCP (cabeçalho claro, botão "Fale com a Educação", 3 notícias, Raleway). A remoção de Agenda/Transparência do menu continua pendente: o DELETE em `menu_itens` excede o tempo pelo MCP; o UPDATE em `municipios` funcionou.
- **Páginas internas conferidas** com o CSS atual. Prévias em `docs/previa/claro/` (index, notícias, notícia, matrícula, serviços, supervisor, números, bolsa). Sem rolagem horizontal e com axe limpo. Ajustada a área de toque da trilha de navegação.
- Atenção: as páginas internas antigas de `docs/previa/` (raiz) têm CSS de 13/10. Use as de `docs/previa/claro/`. A ferramenta `ferramentas/previa_cabecalho_claro.py` agora injeta o `global.css` + `vitrine.css` atuais e funciona em qualquer página da prévia antiga.
- **Próximos passos (na ordem do Arquivo de Contexto):**
  1. publicar: merge na `main` do `portal-municipal` e deploy do Worker de homologação (precisa de Cloudflare);
  2. pendências de conteúdo: menu, fotos do "Em foco", dados a confirmar com a SMEDU;
  3. **painel administrativo**: permissões fase 1B e telas de papéis, unidades e equipe (D-38; `07-pendencias.md`);
  4. carga de conteúdo real;
  5. revisão de acessibilidade manual (leitor de tela).

### 14/10/2026 (noite, 17) — conta 2 (sessão `fervent-turing`)
- D-74, a pedido do William: os cards de Serviços ganham uma moldura verde-petróleo ao passar o mouse, como a moldura azul do modelo da PBH. Captura: `servicos-hover.png`.

### 14/10/2026 (noite, 16) — conta 2 (sessão `fervent-turing`)
- D-73: revisão da página inicial no celular (320 a 768 px). Corrigidos:
  - rolagem horizontal a 320–360 px (a lupa cobria o nome);
  - áreas de toque abaixo de 24 px;
  - textos abaixo de 12 px.
- Agora há 0 problemas nas cinco larguras. O script de verificação está em `ferramentas/verificar_responsivo.cjs` (Playwright; argumentos: HTML e prefixo das capturas).

### 14/10/2026 (noite, 15) — conta 2 (sessão `fervent-turing`)
- D-72, a pedido do William: o rodapé foi refeito no estilo do portal da Prefeitura de Paulínia, sem a newsletter:
  - brasão e nome grandes;
  - contatos com ícones em círculos;
  - links institucionais;
  - faixas de baixo com Mapa do site, Site da Prefeitura, Radar e direitos.
- **Em aberto:** incluir ou não o crédito do fornecedor (Secke) e o "Portal atualizado em". Capturas: `rodape-1920.png` e `rodape-celular.png`.

### 14/10/2026 (noite, 14) — conta 2 (sessão `fervent-turing`)
- D-70: a distância entre as Notícias e o "Em foco" ficou em 58 px (três reduções pedidas).
- D-71, a pedido do William: saiu a faixa fina colorida sob a barra verde. Agora ela só aparece se o órgão cadastrar `tema.cores_faixa`. A prévia foi atualizada.

### 14/10/2026 (noite, 13) — conta 2 (sessão `fervent-turing`)
- D-70, a pedido do William: a distância entre as Notícias e o "Em foco" diminuiu em três passos (15%, 15% e 10%: 88 → 75 → 64 → 58 px no computador; 37 px no celular). A prévia foi atualizada.

### 14/10/2026 (noite, 12) — conta 2 (sessão `fervent-turing`)
- D-69, a pedido do William: o cabeçalho branco ficou 10% mais alto (de 105 para 117 px). A prévia e a captura `cabecalho-mais-alto-1920.png` foram atualizadas.

### 14/10/2026 (noite, 11) — conta 2 (sessão `fervent-turing`)
- D-68, a pedido do William: o destaque troca de slide a cada **4,5 s** (antes 7,5 s; passou por 6,5 s); a animação continua em 0,9 s. A prévia foi atualizada.

### 14/10/2026 (noite, 10) — conta 2 (sessão `fervent-turing`)
- D-67, a pedido do William: a seção de Serviços passou ao estilo do modelo da PBH:
  - fundo cinza claro **#f5f7f9**, medido no print, só nessa seção;
  - cards brancos centralizados, com ícone num quadrado turquesa claro, título em negrito e descrição; sem o "Acessar →".
- A prévia e a captura `servicos-modelo-1920.png` foram atualizadas.

### 14/10/2026 (noite, 9) — conta 2 (sessão `fervent-turing`)
- D-66, a pedido do William:
  - o botão do cabeçalho passou a "Fale com a Educação" (o link ainda é `/fale-com-o-supervisor`);
  - o carrossel do destaque desliza da direita para a esquerda ao avançar, e no sentido inverso ao voltar.
- A prévia foi atualizada; ela usa o script novo do carrossel embutido.

### 14/10/2026 (noite, 8) — conta 2 (sessão `fervent-turing`)
- D-65, a pedido do William: os títulos das seções perderam a faixa verde-água e o marcador e ficaram como no modelo da PBH (texto em petróleo, alinhado à esquerda, um pouco maior), para mais limpeza. A prévia e as capturas foram atualizadas.

### 14/10/2026 (noite, 7) — conta 2 (sessão `fervent-turing`)
- D-64, a pedido do William (ele não queria a largura de tudo alterada em D-63):
  - a largura volta a **1290 px** em tudo e a fonte do menu volta ao tamanho original;
  - **Agenda** e **Transparência** saem do menu do cabeçalho. Com 6 itens, cabe numa linha a partir de 1280 px de tela.
- **Pendente no banco:** remover os dois itens do menu principal da SMEDU na homologação, pelo painel (Menus) ou por SQL. As escritas pelo MCP do Supabase excederam o tempo nesta sessão (leituras funcionam). A prévia já está sem eles.

### 14/10/2026 (noite, 6) — conta 2 (sessão `fervent-turing`)
- D-63, a pedido do William: o cabeçalho ficou em **uma linha só**, como no modelo: brasão + nome, menu no meio, lupa + "Fale com o supervisor" à direita. Para caber:
  - menu um pouco menor;
  - marca e botão mais compactos;
  - largura útil de 1290 para **1360 px** (≈ 7,4 cm de margem em tela de 1920 px), aplicada a todo o conteúdo.
- Fica numa linha a partir de 1366 px de tela; abaixo disso, o menu desce sozinho. A prévia e as capturas (`cabecalho-uma-linha-*.png`, `pagina-inteira-*.png`) foram atualizadas.

### 14/10/2026 (noite, 5) — conta 2 (sessão `fervent-turing`)
- D-62, a pedido do William: o cabeçalho (barra de acessibilidade e cabeçalho branco) passou a usar a fonte do portal da PBH, identificada pelo print como **Raleway**. Ela está auto-hospedada e é configurável em `tema.fonte_cabecalho`. O resto do portal segue em Prompt.
- **Confirmar** a fonte da PBH pelo F12. A prévia foi atualizada; captura em `docs/design/capturas/d57/cabecalho-raleway.png`.
- Para ligar na homologação junto com o D-57: `tema.fonte_cabecalho = 'Raleway'`. A ferramenta da prévia lê a Raleway de `portal-municipal/portal/node_modules/@fontsource/raleway` (rodar `npm install` no `portal/` antes).

### 14/10/2026 (noite, 4) — conta 2 (sessão `fervent-turing`)
- William enviou fotos novas para o "Em foco":
  - estudantes na escadaria → Bolsa de estudo;
  - criança chegando à escola → Matrícula escolar.
- As fotos estão em `docs/design/fotos/` (`foco-bolsa.jpg`, `foco-matricula.jpg`; JPEG otimizado). A prévia `docs/previa/cabecalho-claro.html` já as usa. Para regerar a prévia: `python3 ferramentas/previa_cabecalho_claro.py <prévia de 13/10> <saída> <vitrine.css> docs/design/marca/brasao-colorido.png docs/design/fotos`.
- **Pendente** (registrado em `portal-municipal/docs/07-pendencias.md`):
  - enviar as fotos ao Storage da homologação e trocar `config.home.foco[].imagem_path`/`imagem_alt`. Esta conta não alcança o Storage;
  - confirmar a autorização de imagem da foto da matrícula (criança e adultos reconhecíveis) e a licença da foto dos estudantes.

### 14/10/2026 (noite, 3) — conta 2 (sessão `fervent-turing`)
- D-61, a pedido do William: as seções da home ficaram sem fundo próprio (branco) e as réguas de título passaram a ter a mesma largura das seções (1290 px), com cantos arredondados. O espaço vertical entre as seções diminuiu. A prévia e as capturas da página inteira foram atualizadas.

### 14/10/2026 (noite, 2) — conta 2 (sessão `fervent-turing`)
- D-60, a pedido do William: todo o conteúdo da home (Em foco, Eventos, Serviços, Equipe gestora), as páginas internas e o rodapé passaram a seguir a largura de 1290 px do bloco de cima. Os cards de Serviços agora ocupam a largura toda (3 por linha). Capturas da página inteira: `docs/design/capturas/d57/pagina-inteira-*.png`. A prévia foi atualizada.

### 14/10/2026 (noite) — conta 2 (sessão `fervent-turing`)
- D-59, a pedido do William: a fileira de cima das Notícias passou de 5 para 3 cards maiores, na mesma largura do bloco de cima (1290 px). Os dois cards grandes continuam. Configuração: `config.home.noticias_fileira`. A prévia `docs/previa/cabecalho-claro.html` foi atualizada.
- Para ligar na homologação junto com o D-57: `config.home.noticias_fileira = 3`.

### 14/10/2026 (fim da tarde) — conta 2 (sessão `fervent-turing`)
- Ajuste pedido pelo William (D-58): o destaque e todo o bloco de cima foram estreitados para a largura do modelo da PBH, com máximo de 1290 px (≈ 8 cm de margem em tela de 1920 px). A altura do destaque passou a 290–340 px. A prévia `docs/previa/cabecalho-claro.html` e as capturas em `docs/design/capturas/d57/` foram atualizadas.
- **Próximo passo:** segue o mesmo. William avalia; se aprovar, merge na `main` do `portal-municipal`, ligar o campo na homologação e publicar.

### 14/10/2026 (tarde) — conta 2 (sessão `fervent-turing`)
- A pedido do William, a parte de cima do portal foi refeita no estilo do portal da PBH (https://prefeitura.pbh.gov.br/; o print está na conversa e a descrição, em D-57):
  - barra estreita de acessibilidade no verde-petróleo, com faixa colorida embaixo;
  - cabeçalho branco mais alto, com brasão em cores, menu, lupa e o botão "Fale com o supervisor";
  - aviso em caixa;
  - destaque mais baixo (300 a 400 px), com setas, pausa redonda e números.
- Tudo fica atrás de um campo de configuração. Sem o campo, o portal não muda.
- Verificação: axe sem violações (1440 e 390 px, normal e alto contraste) e `astro build` passando.
- A prévia foi gerada por `ferramentas/previa_cabecalho_claro.py`, que aplica a marcação nova à prévia de 13/10. Motivo: o ambiente desta conta não acessou o Supabase, nem depois de o William liberar a rede (a mudança provavelmente só vale para sessões novas).
- **Próximo passo:** William avalia a prévia e diz se segue essa linha. Se seguir: merge na `main` do `portal-municipal`, ligar o campo na homologação e publicar o Worker. A outra conta pode fazer isso numa sessão com acesso à Cloudflare.

### 14/10/2026 — conta 2 (sessão `fervent-turing`)
- **Diagnóstico da conexão com o Supabase:** a conexão está OK pelo MCP. São 43 tabelas, todas com RLS, e 20 migrações aplicadas. Advisors de segurança: só avisos informativos. Desempenho: 31 avisos de múltiplas políticas permissivas.
- **Diferenças entre o banco e a especificação:**
  - a SMEDU é uma linha de `municipios` (organização contratante, D-37), não um órgão de `orgaos`;
  - `sistemas_externos` só tem registros de Jeriquara;
  - o catálogo `permissoes` tem só 5 códigos;
  - Paulínia não tem domínio cadastrado na produção;
  - não há usuários vinculados à SMEDU.
- Descoberto que o código está em `portal-municipal` e o trabalho de design no branch `claude/charming-cray-jecgm6`, que foi trazido para este branch.
- Feita a revisão visual da prévia de 13/10 (D-56), no computador e no celular. As propostas estão na seção "Estado atual".
- Criados este `PASSAGEM.md` e o `CLAUDE.md` deste repositório, a pedido do William, para a troca entre contas.
- **Próximo passo:** William escolhe quais propostas de design implementar. A implementação é feita em `portal-municipal`, com registro em D-57 e seguintes.

### 12 e 13/10/2026 — conta 1 (sessões anteriores)
- Fase 1A do banco (migrações 0016 a 0020), carga de dados públicos da SMEDU na homologação, layout vitrine e uma sequência de ajustes de design a pedido do William (D-39 a D-56). Detalhes em `portal-municipal/docs/06-decisoes.md` e no histórico do branch `claude/charming-cray-jecgm6`.

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
| **Pendências com a SMEDU (tudo o que depende da Secretaria/Prefeitura)** | Este repositório: `docs/reuniao/smedu-pendencias.md` |
| **Supabase, produção** | Projeto **Portal Municipal**, ref `qgywucdnaeheqndcxtho` (sa-east-1) |
| **Supabase, homologação** | Branch `homologacao` do mesmo projeto, ref `kvilgamsyneenjtlllcf`. O portal em desenvolvimento lê daqui (D-14) |
| **Homologação publicada (conta Cloudflare pessoal willquerubim2025, D-80)** | Portal (abre a SMEDU): https://portal-municipal-homologacao.willquerubim2025.workers.dev · Painel: https://painel-municipal-homologacao.willquerubim2025.workers.dev · Publicar: GitHub → Actions → "Publicar homologação" (D-79) |

### Branches deste repositório
- **`main` é a referência** (15/10/2026): contém todo o trabalho de 12 a 14/10, ou seja, docs, design, prévias, este arquivo e o `CLAUDE.md`. Comece sempre por ela.
- `claude/charming-cray-jecgm6` (conta 1) e `claude/fervent-turing-szzwyu` (conta 2) já estão contidos na `main`.
- No `portal-municipal`, a `main` também já tem todo o código do padrão visual (D-57 a D-75).

---

## Estado atual (atualizado em 15/10/2026)

- **Jeriquara está fora (D-82):** dispensa não ganha; não fazer nada para Jeriquara. O produto é multi-organização; a organização em foco é a SMEDU.
- **Banco:** migrações 0001 a 0021 aplicadas na produção. Permissões por papel, unidades, equipe gestora e página inicial configurável (fase 1A, D-38) já existem.
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
- **Para o William rodar no SQL Editor** (o MCP não aplica migração): homologação → `0023`; produção (aprovada em 15/10) → `0022` e depois `0023`. Depois, publicar painel e portal (Actions).
- **Próximo passo:** biblioteca de mídias no painel.

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

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
| **Código do portal (Astro) e do painel (React)** | Repositório `willquerubim2025-oss/portal-municipal`, branch `main`. O experimento D-57 (cabeçalho claro) está no branch `claude/fervent-turing-szzwyu`, ainda fora da `main`. O layout da SMEDU é o **"vitrine"**: `portal/src/components/vitrine/` e `portal/src/styles/vitrine.css` |
| **Decisões técnicas e de design (D-01 a D-56)** | `portal-municipal/docs/06-decisoes.md`. Não reabrir decisão sem motivo novo |
| **Pendências** | `portal-municipal/docs/07-pendencias.md` |
| **Regras do código** | `portal-municipal/CLAUDE.md` |
| **Especificação e contexto do Portal Educação** | Este repositório: `docs/Especificação do Brainstorm.md`, `docs/Arquivo de Contexto.md` |
| **Diagnóstico do banco e plano da fase 1** | Este repositório: `docs/Banco de Dados — Diagnóstico e Decisões.md`, `docs/Plano de Migração — Fase 1.md` |
| **Prévias navegáveis (HTML autocontido, abre sem internet)** | Este repositório: `docs/previa/` (`index.html` é a página inicial) |
| **Sistema visual, marca e capturas** | Este repositório: `docs/design/` |
| **Dados a confirmar com a SMEDU** | Este repositório: `docs/reuniao/smedu-dados-a-confirmar.md` |
| **Supabase, produção** | Projeto **Portal Municipal**, ref `qgywucdnaeheqndcxtho` (sa-east-1) |
| **Supabase, homologação** | Branch `homologacao` do mesmo projeto, ref `kvilgamsyneenjtlllcf`. O portal em desenvolvimento lê daqui (D-14) |
| **Portal de homologação publicado** | Worker `portal-municipal-homologacao` na Cloudflare (D-27) |

### Branches deste repositório
- `main`: só o commit inicial.
- `claude/charming-cray-jecgm6`: todo o trabalho de 12 e 13/10/2026 (docs, design, prévias, migrações).
- `claude/fervent-turing-szzwyu`: inclui tudo do anterior, mais este arquivo e o `CLAUDE.md`.
- **Recomendado:** juntar na `main` para que as duas contas partam do mesmo ponto.

---

## Estado atual (atualizado em 14/10/2026)

- **Banco:** migrações 0001 a 0020 aplicadas na produção. Permissões por papel, unidades, equipe gestora e página inicial configurável (fase 1A, D-38) já existem.
- **Portal Educação (layout vitrine):** página inicial pronta na homologação. Ordem dos blocos: destaque, Notícias, Em foco, Eventos, Serviços, Equipe gestora (D-56). A última decisão de design é a **D-56**.
- **Conteúdo fictício na homologação, para a apresentação:** equipe gestora, fotos `ficticio-*`, imagens do "Em foco" (Unsplash) e 6 dos 7 eventos. Tudo isso precisa ser removido antes de publicar (detalhes em `07-pendencias.md`).
- **Em andamento:** melhorias de design e layout do portal.
- **Aguardando avaliação do William: D-57, cabeçalho claro + destaque compacto, inspirado no portal da PBH.**
  - Prévia: `docs/previa/cabecalho-claro.html`. Capturas: `docs/design/capturas/d57/`.
  - O código está em `portal-municipal`, branch `claude/fervent-turing-szzwyu` (ainda não está na `main`).
  - Para ligar na homologação: `config.cabecalho.estilo = 'claro'` e `config.cabecalho.botao = {"rotulo": "Fale com a Educação", "url": "/fale-com-o-supervisor"}` em `municipios` (slug `paulinia-educacao`, branch de homologação `kvilgamsyneenjtlllcf`). Depois, publicar o Worker de homologação.
  - D-58 (bloco de cima com 1290 px), D-60 (todo o conteúdo nessa largura), D-61 (seções sem fundo, régua na largura do conteúdo), D-62 (fonte Raleway no cabeçalho, `tema.fonte_cabecalho = 'Raleway'`), D-63/D-64 (cabeçalho em uma linha; largura de 1290 px; menu sem Agenda e Transparência — remover no banco), D-65 (títulos das seções sem faixa), D-66 (destaque deslizando; botão "Fale com a Educação"), D-67 (Serviços no estilo do modelo), D-68 (destaque a cada 4,5 s), D-69 (cabeçalho 10% mais alto), D-70 (Em foco mais perto das Notícias) e D-59 (Notícias com 3 cards, `config.home.noticias_fileira = 3`) estão no mesmo branch.
  - Se aprovado: juntar o branch na `main` do `portal-municipal`, ligar os campos na homologação e publicar.
- Veja também as propostas abertas abaixo.

### Propostas de design em aberto (revisão de 14/10/2026, aguardando escolha do William)
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

### 14/10/2026 (noite, 13) — conta 2 (sessão `fervent-turing`)
- D-70, a pedido do William: a distância entre as Notícias e o "Em foco" diminuiu duas vezes cerca de 15% (88 → 75 → 64 px no computador; 41 px no celular). A prévia foi atualizada.

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

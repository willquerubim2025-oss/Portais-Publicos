# Apresentação impressa do Portal da Educação (D-142 e D-148 do `portal-municipal`)

**O material:** [Portal-Educacao-Apresentacao.pdf](Portal-Educacao-Apresentacao.pdf), 46 páginas A4, para entregar na mão. Ordem: o desafio e a virada → a página inicial em 4 partes (imagem e explicação) → a página de destaque (carrossel) → vídeos de orientação (matrícula) → **tela por tela** (uma tela inteira do portal por página) → acessibilidade e celular → **sistemas em órbita** (diagrama, a faixa de sistemas, CI Eletrônica, Pesquisas da Educação e SIMAPE: geolocalização, planejamento de vagas e "Aluno novo") → **uma página para cada escola** (simulação, ainda não existe no portal) → o painel → perguntas, problemas, tecnologia e próximos passos.

**Para refazer** (quando o portal ou os sistemas mudarem), a partir desta pasta:
1. Portal: `mkdir -p img-bruto && NODE_PATH=$(npm root -g) node fonte/capturar.cjs`.
2. Simulação da página da escola: `NODE_PATH=$(npm root -g) node fonte/escola_mock.cjs` (usa `img-bruto/escola.html`, fotos tiradas dos destaques do portal).
3. Sistemas (fotos guardadas em uma pasta temporária, ver `SC` em `fonte/preparar.py`):
   - CI Eletrônica: no repositório `ci-eletronica`, compilar com o Supabase de mentira e rodar `docs/guia/fonte/fotos.cjs` (ver o LEIA-ME do guia) com `inicio,ci-receber,caminho,nova-op,impressao,celular,verificar`.
   - Pesquisas e SIMAPE: fotos do sistema publicado com uma conta de teste (no SIMAPE, a conta entra em `geoescola.usuarios` só durante as fotos).
4. `python3 fonte/preparar.py` (cortes e JPEG) e `python3 fonte/montar.py` (gera o PDF). Texto em `fonte/montar.py`, visual em `fonte/apresentacao.css`. Os números do sumário saem sozinhos.

Contato na contracapa ainda com marcadores: `[telefone]` e `[e-mail]`.

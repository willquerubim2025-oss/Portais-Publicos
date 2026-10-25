# Apresentação impressa do Portal da Educação (D-136 do `portal-municipal`)

**O material:** [Portal-Educacao-Apresentacao.pdf](Portal-Educacao-Apresentacao.pdf), 31 páginas A4, feito para entregar na mão. A ordem é: primeiro conquistar com o portal (a página inicial em 4 partes, cada uma com página de imagem e página de explicação), depois os serviços para a família, a acessibilidade e o celular, a integração (sistemas e CI Eletrônica) e o painel; só no fim vêm as perguntas e respostas, os problemas e a parte técnica.

**Para refazer** (quando o portal mudar), a partir desta pasta:
1. `mkdir -p img-bruto && NODE_PATH=$(npm root -g) node fonte/capturar.cjs` (fotos do portal publicado);
2. `python3 fonte/preparar.py` (cortes e JPEG; usa também as fotos do manual do painel e do guia da CI);
3. `python3 fonte/montar.py` (gera o PDF). Texto e páginas em `fonte/montar.py`, visual em `fonte/apresentacao.css`.

Contato na contracapa ainda com marcadores: `[telefone]` e `[e-mail]`.

# Ferramentas das prévias

As prévias de `docs/previa/` são páginas HTML autocontidas (abrem sem internet) no padrão visual aprovado (D-57 a D-76).

- **`gerar_previa.py`**: gera uma prévia a partir da base de 13/10 (`base-previa-13-10/`). Aplica a marcação nova do cabeçalho, do destaque e do rodapé e injeta o CSS atual do portal (`global.css` + `vitrine.css` do `portal-municipal`), a fonte Raleway e as fotos de `docs/design/fotos/`.
  ```bash
  # dentro de Portais-Publicos, com o portal-municipal em ../portal-municipal e `npm install` feito em portal/
  for f in ferramentas/base-previa-13-10/*.html; do
    python3 ferramentas/gerar_previa.py "$f" "docs/previa/$(basename $f)" ../portal-municipal/portal/src/styles/vitrine.css docs/design/marca/brasao-colorido.png docs/design/fotos
  done
  ```
- **`verificar_responsivo.cjs`**: verifica uma página a 320, 360, 390, 414 e 768 px (rolagem horizontal, elementos fora da tela, toque < 24 px, texto < 12 px) e salva capturas. Uso: `node ferramentas/verificar_responsivo.cjs <arquivo.html> <prefixo-das-capturas>`.
- **`base-previa-13-10/`**: a prévia gerada do portal de homologação em 13/10, antes do padrão novo. Não é para consulta, só a base da geração.

Quando o portal de homologação for publicado com o código da `main`, as prévias deixam de ser necessárias: o próprio portal passa a ser a referência.

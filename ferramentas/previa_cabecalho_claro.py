# Gera a prévia do cabeçalho claro (D-57) a partir da prévia autocontida de 13/10:
# mesma marcação do Base.astro/Destaque.astro novos + o bloco de CSS D-57 do vitrine.css.
import base64, sys, re
from bs4 import BeautifulSoup
entrada, saida, css_path, brasao_path = sys.argv[1:5]
botao = ('Fale com a Educação', '/fale-com-o-supervisor')
s = open(entrada, encoding='utf-8').read()
css = open(css_path, encoding='utf-8').read()
# CSS atual completo do portal (global.css + vitrine.css), depois do CSS antigo da prévia: as regras novas vencem
# mesmo nas páginas internas, cuja prévia de 13/10 traz um CSS mais velho.
import os
css = open(os.path.join(os.path.dirname(css_path), 'global.css'), encoding='utf-8').read() + '\n' + css
brasao = 'data:image/png;base64,' + base64.b64encode(open(brasao_path, 'rb').read()).decode()
d = BeautifulSoup(s, 'html.parser')
frag = lambda h: BeautifulSoup(h, 'html.parser')

d.html['class'] = d.html.get('class', []) + ['v-claro']
d.head.append(frag(f'<style>{css}</style>'))
# Fonte do cabeçalho (D-62): Raleway embutida como data URI, como o portal faria com @fontsource.
import glob, os
RALEWAY = '/home/user/portal-municipal/portal/node_modules/@fontsource/raleway/files'
if os.path.isdir(RALEWAY):
    faces = ''.join(f"@font-face{{font-family:'Raleway';font-style:normal;font-display:swap;font-weight:{w};src:url(data:font/woff2;base64,{base64.b64encode(open(f'{RALEWAY}/raleway-latin-{w}-normal.woff2','rb').read()).decode()}) format('woff2')}}" for w in (400, 500, 600, 700, 800))
    d.head.append(frag(f'<style>{faces}</style>'))
    d.html['class'] = d.html.get('class', []) + ['v-fonte-cab']
    d.html['style'] = d.html.get('style', '') + ';--v-fonte-cab:"Raleway"'


# Barra de acessibilidade visível + ferramentas com texto + site da Prefeitura
barra = d.select_one('.barra-acessibilidade')
barra['class'] = ['barra-acessibilidade', 'v-topo']
simbolo = '<svg class="simbolo-acessibilidade" viewBox="0 0 24 24" width="18" height="18" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="11" fill="none" stroke="currentColor" stroke-width="1.6" /><circle cx="12" cy="6.2" r="1.6" fill="currentColor" /><path d="M6.5 9.2l5.5 1 5.5-1M12 10.2v4.2m0 0l-2.6 4.6m2.6-4.6l2.6 4.6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" /></svg>'
barra.select_one('.container').append(frag(f'''<div class="v-topo-direita"><ul class="ferramentas"><li><a href="/acessibilidade" class="link-acessibilidade">{simbolo} Acessibilidade</a></li><li><span class="tamanho-texto" role="group" aria-label="Tamanho do texto"><button type="button" data-fonte="-1" aria-label="Diminuir o tamanho do texto">A-</button><button type="button" data-fonte="0" aria-label="Tamanho normal do texto">A</button><button type="button" data-fonte="1" aria-label="Aumentar o tamanho do texto">A+</button></span></li><li><button type="button" id="botao-contraste" aria-pressed="false">Alto contraste</button></li></ul><a class="v-topo-prefeitura" href="https://www.paulinia.sp.gov.br"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>Site da Prefeitura</a></div>'''))
# D-71: sem a faixa colorida (a SMEDU não cadastra tema.cores_faixa).

# Cabeçalho branco
velho = d.select_one('header.v-cab')
menu = velho.select_one('.v-cab-tela-2 .menu-lista')
nome = velho.select_one('.marca')['aria-label']
tipo = velho.select_one('.marca-tipo').get_text(); nomec = velho.select_one('.marca-nome').get_text()
velho.replace_with(frag(f'''<header class="cabecalho v-cab v-cab-claro"><div class="v-cab-linha"><a href="/" class="marca" aria-label="{nome}"><img class="v-cab-claro-brasao" src="{brasao}" alt="" width="80" height="80"><span class="marca-texto"><span class="marca-tipo">{tipo}</span><span class="marca-nome">{nomec}</span></span></a><nav id="menu" class="menu-principal" aria-label="Menu principal"><details class="menu-movel" open><summary>Menu</summary>{menu}</details></nav><div class="v-cab-acoes"><button type="button" class="v-cab-lupa" data-painel="v-painel-busca" aria-expanded="false" aria-controls="v-painel-busca" aria-label="Buscar no portal" title="Buscar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5L21 21"/></svg></button><a class="v-cab-fale" href="{botao[1]}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 5h11a2 2 0 0 1 2 2v6a2 2 0 0 1-2 2H9l-4 3v-3H4a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2z"/><path d="M19 9h1a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-1v3l-4-3h-3"/></svg><span>{botao[0]}</span></a></div></div><div class="v-cab-painel" id="v-painel-busca"><form class="busca" action="/busca" method="get" role="search"><label for="busca" class="sr-only">Buscar no portal</label><input id="busca" name="q" type="search" placeholder="O que você procura?" required /><button type="submit">Buscar</button></form></div></header>'''))

# Destaque compacto
dest = d.select_one('section.v-destaque')  # só na página inicial
if dest is not None:
    dest['class'] = ['v-destaque', 'v-destaque-compacto']
    pausa = dest.select_one('[data-pausa]')
    pausa.clear()
    pausa.append(frag('<svg class="v-icone-pausar" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14M16 5v14" stroke="currentColor" stroke-width="3" stroke-linecap="round" fill="none"/></svg><svg class="v-icone-continuar" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5l11 7-11 7z" fill="currentColor"/></svg><span data-rotulo class="sr-only">Pausar</span><span class="sr-only"> a troca automática dos destaques</span>'))
    pausa.insert_after(frag('<button type="button" class="v-carrossel-seta v-carrossel-anterior" data-passo="-1" aria-label="Destaque anterior"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg></button><button type="button" class="v-carrossel-seta v-carrossel-proximo" data-passo="1" aria-label="Próximo destaque"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg></button>'))
    for i, b in enumerate(dest.select('[data-ir]')):
        b.append(frag(f'<span aria-hidden="true">{i + 1}</span>'))
# BLOCOS_V: a prévia de 13/10 não tem a classe v-bloco-<bloco> nas seções (o index.astro novo tem).
for h in d.select('.v-secao h2[id^="titulo-"]'):
    sec = h.find_parent('section')
    if sec is not None: sec['class'] = sec.get('class', []) + ['v-bloco-' + h['id'][len('titulo-'):]]
# Notícias (D-59): fileira com 3 cards na largura do bloco de cima.
if d.select_one('#titulo-noticias') is not None:
    FILEIRA = 3
    secao = d.select_one('#titulo-noticias').find_parent('section')
    secao['class'] = secao.get('class', []) + ['v-bloco-noticias']
    linha = secao.select_one('.v-noticias-linha')
    for c in linha.select('article')[FILEIRA:]: c.decompose()
    linha['class'] = ['v-noticias-linha'] + (['v-noticias-linha-larga'] if FILEIRA <= 3 else [])
    linha['style'] = f'--v-fileira:{FILEIRA}'
# Em foco: fotos novas enviadas pelo William (14/10/2026), se o argumento 5 apontar a pasta delas.
if len(sys.argv) > 5:
    fotos = sys.argv[5]
    novas = {'Matrícula escolar': ('foco-matricula.jpg', 'Criança com mochila de rodinhas chegando ao portão da escola, acompanhada pela família e recebida por funcionárias'),
             'Bolsa de estudo': ('foco-bolsa.jpg', 'Quatro estudantes sorrindo e conversando sentados na escadaria de um prédio, com notebook e cadernos')}
    for item in d.select('.v-foco-item'):
        t = item.select_one('h3').get_text(strip=True)
        if t in novas:
            img = item.select_one('img.v-foco-foto')
            img['src'] = 'data:image/jpeg;base64,' + base64.b64encode(open(f'{fotos}/{novas[t][0]}', 'rb').read()).decode()
            img['alt'] = novas[t][1]
            for k in ('srcset',): img.attrs.pop(k, None)
# Menu (14/10/2026, a pedido do William): sem Agenda e Transparência no cabeçalho.
SEM_NO_MENU = {'Agenda', 'Transparência'}
for li in d.select('.v-cab-claro .menu-lista > li'):
    a_ = li.find(['a', 'button', 'span'], recursive=False)
    if a_ and a_.get_text(strip=True) in SEM_NO_MENU: li.decompose()
# CARROSSEL_D66: o script compilado da prévia de 13/10 só esmaece; desliga-o (sem data-carrossel) e usa
# a mesma lógica do Destaque.astro novo, em JavaScript puro.
if dest is not None:
    dest['data-carrossel-previa'] = ''
    del dest['data-carrossel']
    d.body.append(frag('''<script>
    document.querySelectorAll('[data-carrossel-previa]').forEach(function (raiz) {
      var INTERVALO = 4500, slides = [].slice.call(raiz.querySelectorAll('.v-slide')), pontos = [].slice.call(raiz.querySelectorAll('[data-ir]'));
      var pausa = raiz.querySelector('[data-pausa]'), rotulo = pausa && pausa.querySelector('[data-rotulo]');
      var reduzir = matchMedia('(prefers-reduced-motion: reduce)').matches, atual = 0, parado = reduzir, suspenso = false, relogio;
      var deslizar = raiz.classList.contains('v-destaque-compacto') && !reduzir;
      function mostrar(n, sentido) { sentido = sentido || 1; var anterior = atual; atual = (n + slides.length) % slides.length;
        if (deslizar && atual !== anterior) { slides.forEach(function (s) { s.classList.remove('v-slide-sai-esq', 'v-slide-sai-dir'); });
          slides[anterior].classList.add(sentido > 0 ? 'v-slide-sai-esq' : 'v-slide-sai-dir'); var novo = slides[atual];
          novo.style.transition = 'none'; novo.style.transform = 'translateX(' + (sentido > 0 ? 100 : -100) + '%)'; void novo.offsetWidth; novo.style.transition = ''; novo.style.transform = ''; }
        slides.forEach(function (s, i) { var ativo = i === atual; s.classList.toggle('v-slide-ativo', ativo); if (ativo) s.removeAttribute('aria-hidden'); else s.setAttribute('aria-hidden', 'true');
          s.querySelectorAll('a').forEach(function (a) { if (ativo) a.removeAttribute('tabindex'); else a.setAttribute('tabindex', '-1'); }); });
        pontos.forEach(function (p, i) { if (i === atual) p.setAttribute('aria-current', 'true'); else p.removeAttribute('aria-current'); }); }
      function agendar() { clearInterval(relogio); if (!parado && !suspenso) relogio = setInterval(function () { mostrar(atual + 1, 1); }, INTERVALO); }
      function atualizarPausa() { if (pausa) pausa.setAttribute('aria-pressed', String(parado)); if (rotulo) rotulo.textContent = parado ? 'Continuar' : 'Pausar'; }
      pontos.forEach(function (p, i) { p.addEventListener('click', function () { mostrar(i, i < atual ? -1 : 1); agendar(); }); });
      raiz.querySelectorAll('[data-passo]').forEach(function (b) { b.addEventListener('click', function () { var passo = Number(b.dataset.passo); mostrar(atual + passo, passo); agendar(); }); });
      if (pausa) pausa.addEventListener('click', function () { parado = !parado; atualizarPausa(); agendar(); });
      raiz.addEventListener('mouseenter', function () { suspenso = true; agendar(); }); raiz.addEventListener('mouseleave', function () { suspenso = false; agendar(); });
      raiz.addEventListener('focusin', function () { suspenso = true; agendar(); });
      raiz.addEventListener('focusout', function (e) { if (!raiz.contains(e.relatedTarget)) { suspenso = false; agendar(); } });
      document.addEventListener('visibilitychange', function () { suspenso = document.hidden; agendar(); });
      atualizarPausa(); agendar();
    });
    </script>'''))
# RODAPE_D72: rodapé no estilo do portal da Prefeitura, com os dados da SMEDU (config da homologação).
SMEDU = {'email': 'educacao@paulinia.sp.gov.br', 'telefone': '(19) 3874-5750',
         'endereco': 'Paço Municipal · Av. Prefeito José Lozano de Araújo, 1551 · Parque Brasil 500 · Paulínia/SP · CEP 13141-901',
         'horario': 'segunda a sexta, das 8h às 17h'}
ic_tel = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>'
ic_pin = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>'
ic_rel = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'
links = ''.join(f'<li><a href="{h}">{r}</a></li>' for r, h in [('Acesso à Informação', '/acesso-a-informacao'), ('Ouvidoria', '/ouvidoria'), ('Transparência', '/transparencia'), ('Privacidade', '/privacidade'), ('Acessibilidade', '/acessibilidade')])
rod = d.select_one('footer#rodape')
rod.replace_with(frag(f'''<footer id="rodape" class="rodape v-rodape-claro"><div class="container v-rod-principal"><div class="v-rod-marca"><img src="{brasao}" alt="" width="96" height="96"><p><span class="v-rod-nome">{nomec}</span><span class="v-rod-tipo">{tipo}</span></p></div><address class="v-rod-contatos"><p class="v-rod-item"><span class="v-rod-icone" aria-hidden="true">{ic_tel}</span><span><a href="mailto:{SMEDU['email']}">{SMEDU['email']}</a><a href="tel:1938745750">{SMEDU['telefone']}</a></span></p><p class="v-rod-item"><span class="v-rod-icone" aria-hidden="true">{ic_pin}</span><span>{SMEDU['endereco']}</span></p><p class="v-rod-item"><span class="v-rod-icone" aria-hidden="true">{ic_rel}</span><span>Atendimento ao público: {SMEDU['horario']}</span></p></address></div><div class="container v-rod-links"><nav aria-label="Links institucionais"><ul>{links}</ul></nav></div><div class="v-rod-faixa"><div class="container v-rod-faixa-linha"><a href="/mapa-do-site">Mapa do site</a><a href="https://www.paulinia.sp.gov.br">Site da Prefeitura</a><a href="https://radardatransparencia.atricon.org.br/" rel="noopener" target="_blank">Radar da Transparência Pública<span class="sr-only"> (abre em nova aba)</span></a></div></div><div class="v-rod-direitos"><div class="container">© 2026 Secretaria Municipal de Educação de Paulínia. Todos os direitos reservados.</div></div></footer>'''))
# Na prévia, o script compilado antigo não conhece as setas nem a lupa: um script mínimo faz o mesmo.
d.body.append(frag('''<script>
document.querySelectorAll('a[href="#busca"]').forEach(function (a) { a.addEventListener('click', function (e) { var l = document.querySelector('.v-cab-lupa'); if (l && l.getAttribute('aria-expanded') !== 'true') { e.preventDefault(); l.click(); } }); });
var cabClaro = document.querySelector('.v-cab-claro');
if (cabClaro) { var nav = cabClaro.querySelector('.menu-principal'), lista = nav.querySelector('.menu-lista');
  var medir = function () { cabClaro.classList.add('v-cab-uma-linha'); if (!matchMedia('(min-width: 1181px)').matches || lista.scrollWidth > nav.clientWidth + 1) cabClaro.classList.remove('v-cab-uma-linha'); };
  medir(); addEventListener('resize', medir); document.fonts && document.fonts.ready.then(medir); }
</script>'''))
out = str(d)
out = out.replace('<title>', '<title>Prévia cabeçalho claro (D-57) · ', 1)
open(saida, 'w', encoding='utf-8').write(out)
print('ok', len(out))

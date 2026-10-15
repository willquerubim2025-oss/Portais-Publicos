# Gera as prévias de docs/previa/ a partir do portal PUBLICADO (homologação): cada página vira um HTML
# autocontido, que abre sem internet. CSS, fontes, imagens e scripts são embutidos (data URI) e os links
# entre as páginas capturadas apontam para os arquivos locais. Substitui gerar_previa.py desde 15/10/2026:
# o portal de homologação já roda o código da main, então ele é a referência.
#
#   python3 ferramentas/capturar_previa.py [endereço do portal] [pasta de saída]
import base64, mimetypes, re, sys, urllib.parse, urllib.request
from bs4 import BeautifulSoup

BASE = (sys.argv[1] if len(sys.argv) > 1 else 'https://portal-municipal-homologacao.willquerubim2025.workers.dev').rstrip('/')
SAIDA = sys.argv[2] if len(sys.argv) > 2 else 'docs/previa'

# Caminho no portal → arquivo da prévia. Só estes viram páginas locais; os demais links vão para o portal no ar.
PAGINAS = {
    '/': 'index.html',
    '/noticias': 'noticias.html',
    '/servicos': 'servicos.html',
    '/servicos/matricula-escolar': 'matricula.html',
    '/servicos/bolsa-de-estudo': 'bolsa.html',
    '/servicos/area-do-estudante': 'area-do-estudante.html',
    '/fale-com-o-supervisor': 'supervisor.html',
    '/educacao-em-numeros': 'numeros.html',
    '/sobre': 'sobre.html',
    '/estrutura-organizacional': 'estrutura.html',
    '/eventos': 'eventos.html',
    '/transparencia': 'transparencia.html',
    '/legislacao': 'legislacao.html',
    '/acessibilidade': 'acessibilidade.html',
    '/ouvidoria': 'ouvidoria.html',
    '/acesso-a-informacao': 'acesso-a-informacao.html',
    '/privacidade': 'privacidade.html',
}
cache = {}

def baixar(url):
    if url not in cache:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'previa-secke'}), timeout=60) as r:
            cache[url] = (r.read(), r.headers.get_content_type())
    return cache[url]

def data_uri(url):
    corpo, tipo = baixar(url)
    if tipo in (None, 'application/octet-stream', 'text/plain'):
        tipo = mimetypes.guess_type(urllib.parse.urlparse(url).path)[0] or tipo
    return f'data:{tipo};base64,{base64.b64encode(corpo).decode()}'

def css_embutido(css, origem):
    # url(...) dentro do CSS (fontes, imagens) → data URI.
    def troca(m):
        u = m.group(2)
        if u.startswith('data:') or u.startswith('#'):
            return m.group(0)
        return f'url("{data_uri(urllib.parse.urljoin(origem, u))}")'
    return re.sub(r'url\((["\']?)([^)"\']+)\1\)', troca, css)

def local(href):
    p = urllib.parse.urlparse(href)
    if p.netloc and not href.startswith(BASE):
        return href
    caminho = p.path.rstrip('/') or '/'
    if caminho in PAGINAS:
        return PAGINAS[caminho] + (f'#{p.fragment}' if p.fragment else '')
    if caminho.startswith('/noticias/'):
        return 'n-' + caminho.split('/')[-1][:40] + '.html'
    return BASE + href if href.startswith('/') else href

def capturar(caminho, arquivo):
    url = BASE + caminho
    html = baixar(url)[0].decode('utf-8')
    d = BeautifulSoup(html, 'html.parser')
    for link in d.select('link[rel="stylesheet"]'):
        origem = urllib.parse.urljoin(url, link['href'])
        estilo = d.new_tag('style')
        estilo.string = css_embutido(baixar(origem)[0].decode('utf-8'), origem)
        link.replace_with(estilo)
    for estilo in d.select('style'):
        if estilo.string and 'url(' in estilo.string:
            estilo.string = css_embutido(estilo.string, url)
    for s in d.select('script[src]'):
        origem = urllib.parse.urljoin(url, s['src'])
        novo = d.new_tag('script')
        if s.get('type'):
            novo['type'] = s['type']
        novo.string = baixar(origem)[0].decode('utf-8')
        s.replace_with(novo)
    for img in d.select('img[src]'):
        img['src'] = data_uri(urllib.parse.urljoin(url, img['src']))
        for a in ('srcset', 'sizes', 'loading'):
            img.attrs.pop(a, None)
    for el in d.select('[style*="url("]'):
        el['style'] = css_embutido(el['style'], url)
    for tag in d.select('link[rel~="icon"], link[rel="preload"], link[rel="canonical"], link[rel="alternate"]'):
        tag.decompose()
    for a in d.select('a[href]'):
        a['href'] = local(a['href'])
    for f in d.select('form[action]'):
        f['action'] = BASE + f['action'] if f['action'].startswith('/') else f['action']
    aviso = BeautifulSoup('<p style="margin:0;padding:.4rem 1rem;background:#fff3cd;color:#5c4400;font:14px/1.4 sans-serif;text-align:center">'
                          f'Prévia do portal em {sys_data()}: cópia para ver sem internet. Busca e formulários só funcionam no portal no ar.</p>', 'html.parser')
    d.body.insert(0, aviso)
    open(f'{SAIDA}/{arquivo}', 'w', encoding='utf-8').write(str(d))
    return d

def sys_data():
    import datetime
    return datetime.date.today().strftime('%d/%m/%Y')

noticias = set()
for caminho, arquivo in PAGINAS.items():
    d = capturar(caminho, arquivo)
    for a in d.select('a[href^="n-"]'):
        noticias.add(a['href'].split('#')[0])
    print('ok', arquivo)
# Notícias linkadas nas páginas capturadas (slug curto → caminho completo, lido da página de notícias).
lista = BeautifulSoup(baixar(BASE + '/noticias')[0].decode('utf-8'), 'html.parser')
for a in lista.select('a[href^="/noticias/"]'):
    caminho = a['href']
    arquivo = 'n-' + caminho.split('/')[-1][:40] + '.html'
    if arquivo in noticias:
        capturar(caminho, arquivo)
        noticias.discard(arquivo)
        print('ok', arquivo)

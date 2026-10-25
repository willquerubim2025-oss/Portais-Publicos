"""Corta as fotos tiradas por capturar.cjs nas partes usadas na apresentação (JPEG leve em ../img).

    NODE_PATH=$(npm root -g) node fonte/capturar.cjs     (grava as fotos em ./img-bruto, a partir do portal publicado)
    python3 fonte/preparar.py
    python3 fonte/montar.py
"""
from pathlib import Path
import numpy as np
from PIL import Image

BASE = Path(__file__).resolve().parent.parent
S = BASE / 'img-bruto'
D = BASE / 'img'
D.mkdir(exist_ok=True)
PAINEL = BASE.parent.parent / 'manual' / 'img'                       # fotos do painel (manual do portal)
CI = BASE.parent.parent.parent.parent / 'ci-eletronica' / 'docs' / 'guia' / 'img'  # fotos da CI (guia da CI)


def salvar(im, nome, larg=1600):
    im = im.convert('RGB')
    if im.width > larg:
        im = im.resize((larg, round(im.height * larg / im.width)), Image.LANCZOS)
    im.save(D / f'{nome}.jpg', quality=82, optimize=True, progressive=True)


def sem_rodape(im):
    """Corta onde começa o rodapé verde-escuro do portal."""
    a = np.asarray(im.convert('RGB'))
    for y in range(1200, a.shape[0], 8):
        r, g, b = a[y].mean(axis=0)
        if r < 20 and 50 < g < 80 and 60 < b < 90:
            return im.crop((0, 0, im.width, y))
    return im


home = Image.open(S / 'home.png')
# partes da página inicial (px CSS da página com 1440 px de largura; a foto é em dobro)
for i, (a, b) in enumerate([(0, 1525), (1525, 2734), (2734, 4044), (4044, 5491)], 1):
    salvar(home.crop((0, a * 2, home.width, b * 2)), f'home-{i}')
salvar(home.crop((0, 0, home.width, 1270 * 2)), 'home-capa', 1800)
salvar(home.crop((0, 4044 * 2, home.width, 4482 * 2)), 'sistemas')
for i in range(3):
    salvar(Image.open(S / f'destaque-{i}.png'), f'destaque-{i}', 1800)
m = Image.open(S / 'matricula.png')
salvar(m.crop((0, 0, m.width, 4000)), 'matricula-topo')
salvar(m.crop((0, 1560, m.width, 3150)), 'matricula-videos')
for n in ['servicos', 'noticia', 'transparencia', 'numeros', 'estudante', 'legislacao', 'evento', 'estrutura']:
    salvar(sem_rodape(Image.open(S / f'{n}.png')), n)
salvar(Image.open(S / 'contraste.png'), 'contraste')
for n in ['cel-home', 'cel-matricula', 'cel-noticias', 'cel-servicos']:
    salvar(Image.open(S / f'{n}.png'), n, 900)
for n in ['painel-noticia-editar', 'painel-biblioteca', 'painel-destaque-novo', 'painel-identidade', 'painel-menus', 'painel-papeis', 'painel-escola-noticia']:
    salvar(Image.open(PAINEL / f'{n}.jpg'), n)
for n in ['inicio', 'impressao']:
    salvar(Image.open(CI / f'{n}.png'), f'ci-{n}')
print('ok')

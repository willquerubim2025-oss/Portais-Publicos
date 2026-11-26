"""Apresentação impressa do Portal da Educação (D-136 do portal-municipal).

Material de convencimento, para entregar na mão: primeiro o portal (imagens grandes, uma parte por
página), depois a explicação; a integração e o painel; e só no fim as perguntas, os problemas e a
tecnologia. Páginas A4 de layout fixo.

    node fonte/capturar.cjs          (fotos do portal publicado; ver o cabeçalho do arquivo)
    python3 fonte/montar.py          -> Portal-Educacao-Apresentacao.pdf
"""
import json, os, subprocess
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BASE = AQUI.parent

# Ícones de traço (desenho Lucide, licença ISC)
I = {
    'casa': '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
    'busca': '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    'celular': '<rect width="14" height="20" x="5" y="2" rx="2"/><path d="M12 18h.01"/>',
    'video': '<path d="m22 8-6 4 6 4V8Z"/><rect width="14" height="12" x="2" y="6" rx="2"/>',
    'seta': '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    'relogio': '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    'carro': '<path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9L18 10l-2.7-3.6A2 2 0 0 0 13.7 6H7.3a2 2 0 0 0-1.6.9L3 10l-1.5.6C.7 10.9 0 11.7 0 12.6V16c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/>',
    'fone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2Z"/>',
    'ok': '<path d="M20 6 9 17l-5-5"/>', 'x': '<path d="M18 6 6 18M6 6l12 12"/>',
    'escudo': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10"/><path d="m9 12 2 2 4-4"/>',
    'cadeado': '<rect width="18" height="11" x="3" y="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    'olho': '<path d="M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z"/><circle cx="12" cy="12" r="3"/>',
    'caneta': '<path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/>',
    'imagem': '<rect width="18" height="18" x="3" y="3" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.1-3.1a2 2 0 0 0-2.8 0L6 21"/>',
    'paleta': '<circle cx="13.5" cy="6.5" r=".5"/><circle cx="17.5" cy="10.5" r=".5"/><circle cx="8.5" cy="7.5" r=".5"/><circle cx="6.5" cy="12.5" r=".5"/><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.9 0 1.6-.7 1.6-1.7 0-.4-.2-.8-.4-1.1-.3-.3-.4-.7-.4-1.1a1.6 1.6 0 0 1 1.6-1.6H16c3 0 5.5-2.5 5.5-5.6C21.9 6 17.5 2 12 2z"/>',
    'pessoas': '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    'documento': '<path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5z"/><path d="M14 2v6h6"/><path d="M8 13h8M8 17h5"/>',
    'enviar': '<path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/>',
    'calendario': '<rect width="18" height="18" x="3" y="4" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    'grafico': '<path d="M3 3v18h18"/><path d="M7 16v-5M12 16V8M17 16v-8"/>',
    'acess': '<circle cx="12" cy="4.5" r="2"/><path d="M5 8h14M12 8v6M9 21l3-7 3 7"/>',
    'mundo': '<circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>',
    'banco': '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5v14c0 1.7 4 3 9 3s9-1.3 9-3V5"/><path d="M3 12c0 1.7 4 3 9 3s9-1.3 9-3"/>',
    'nuvem': '<path d="M17.5 19H9a7 7 0 1 1 6.7-9h1.8a4.5 4.5 0 1 1 0 9Z"/>',
    'raio': '<path d="M13 2 3 14h9l-1 8 10-12h-9l1-8z"/>',
    'link': '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
    'pergunta': '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>',
    'alerta': '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4M12 17h.01"/>',
    'chave': '<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6M15.5 7.5l3 3L22 7l-3-3"/>',
    'estrela': '<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01z"/>',
    'escola': '<path d="m4 6 8-4 8 4"/><path d="m18 10 4 2v8a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-8l4-2"/><path d="M14 22v-4a2 2 0 0 0-4 0v4"/><path d="M18 5v17M6 5v17"/>',
    'livro': '<path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>',
    'engrenagem': '<path d="M4 21v-7M4 10V3M12 21v-9M12 8V3M20 21v-5M20 12V3M2 14h4M10 8h4M18 16h4"/>',
    'treino': '<path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>',
    'orbita': '<circle cx="12" cy="12" r="3"/><ellipse cx="12" cy="12" rx="10" ry="4.5"/><ellipse cx="12" cy="12" rx="4.5" ry="10" transform="rotate(45 12 12)"/>',
    'pin': '<path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    'ia': '<path d="M12 3l1.9 4.6L18.5 9l-4.6 1.9L12 15.5l-1.9-4.6L5.5 9l4.6-1.4z"/><path d="M19 15l.9 2.1L22 18l-2.1.9L19 21l-.9-2.1L16 18l2.1-.9z"/>',
    'mapa': '<path d="M14.1 6 9.9 4.1a2 2 0 0 0-1.8 0L3.6 6.3A1 1 0 0 0 3 7.2v12.6a1 1 0 0 0 1.4.9l4.5-2.2a2 2 0 0 1 1.8 0l4.2 1.9a2 2 0 0 0 1.8 0l4.5-2.2a1 1 0 0 0 .6-.9V4.7a1 1 0 0 0-1.4-.9l-4.5 2.2a2 2 0 0 1-1.8 0Z"/><path d="M15 6v15M9 3v15"/>',
}


def ic(n, t=22, cor='currentColor'):
    return (f'<svg width="{t}" height="{t}" viewBox="0 0 24 24" fill="none" stroke="{cor}" stroke-width="1.8" stroke-linecap="round" '
            f'stroke-linejoin="round" style="flex:none;vertical-align:-4px">{I[n]}</svg>')


def img(n):
    return f'../img/{n}.jpg'


ROTULOS = {'ci': 'CI Eletrônica · Secretaria Municipal de Educação', 'pq': 'Pesquisas da Educação · Secretaria Municipal de Educação',
           'sim': 'SIMAPE · Planejamento Escolar', 'escola': 'Portal da Educação · página da escola (simulação)'}


def navegador(nome, marcas=(), cls=''):
    """Foto do portal dentro de uma janela de navegador, com números (x%, y%)."""
    b = ''.join(f'<span class="mc" style="left:{x}%;top:{y}%">{i}</span>' for i, (x, y) in enumerate(marcas, 1))
    return (f'<div class="nav {cls}"><div class="nav-barra"><i></i><i></i><i></i><span>{ROTULOS.get(nome.split("-")[0], "Portal da Educação · Secretaria Municipal de Educação")}</span></div>'
            f'<div class="nav-img"><img src="{img(nome)}">{b}</div></div>')


def numerados(itens, claro=False):
    return '<ol class="numerados' + (' claro' if claro else '') + '">' + ''.join(
        f'<li><span class="mc-p">{i}</span><div><b>{t}</b><span>{d}</span></div></li>' for i, (t, d) in enumerate(itens, 1)) + '</ol>'


def rodape(n, claro=False):
    return f'<div class="rodape{" claro" if claro else ""}"><span>Portal da Educação · SECKE Sistemas</span><span>{n:02d}</span></div>'


# ---------- coordenadas (px da página de 1440 px) das marcas na página inicial
CORTES = [(0, 1525), (1525, 2734), (2734, 4044), (4044, 5491)]


def m(parte, pontos):
    a, b = CORTES[parte - 1]
    return [(round(x / 1440 * 100, 2), round((y - a) / (b - a) * 100, 2)) for x, y in pontos]


HOME = {
    1: {'titulo': 'A abertura', 'sub': 'O que a família vê ao entrar',
        'marcas': m(1, [(1235, 19), (150, 105), (600, 105), (1265, 105), (720, 220), (720, 470), (520, 930)]),
        'porque': 'Nos primeiros segundos, a família já vê o que é da época (matrícula, uniforme) e sabe para onde ir. Nada de procurar no meio de dezenas de secretarias.',
        'itens': [('Barra de acessibilidade', 'Alto contraste, tamanho do texto, atalhos de teclado e Libras (VLibras), sempre à mão.'),
                  ('Identidade da Secretaria', 'Brasão e nome. Cores, fontes e logotipo são configurados pela própria Secretaria.'),
                  ('Menu simples', 'Início, A Secretaria, Matrícula, Escolas e supervisores, Notícias e Serviços: o que as famílias mais procuram.'),
                  ('Fale com a Educação', 'Um botão fixo que leva ao contato certo.'),
                  ('Aviso do dia', 'Uma faixa para recados urgentes (“o cadastro do uniforme já está aberto”), que a pessoa pode fechar.'),
                  ('Carrossel de destaques', 'Fotos com título e botão, ou artes de campanha prontas, como a do novo portal.'),
                  ('Em foco', 'Os serviços da época em destaque, com atalhos diretos: inscrição na creche, situação, lista de espera.')]},
    2: {'titulo': 'Notícias', 'sub': 'A Educação contando o que faz',
        'marcas': m(2, [(280, 1850), (720, 2679)]),
        'porque': 'A Secretaria passa a ter a sua própria vitrine: o trabalho das escolas aparece, com fotos, e cada notícia pode ser compartilhada no WhatsApp com um link bonito.',
        'itens': [('Notícias com foto', 'Cards com imagem, data e resumo, numa grade que valoriza as fotos das escolas.'),
                  ('Todas as notícias', 'Página própria com busca e filtro por categoria. Cada notícia tem endereço próprio, pronto para o Google e para o WhatsApp.')]},
    3: {'titulo': 'Agenda e serviços', 'sub': 'Datas importantes e os serviços mais procurados',
        'marcas': m(3, [(330, 3100), (1000, 3100), (285, 3617)]),
        'porque': 'Reuniões, provas e formações deixam de depender de recado: estão no calendário, com data, local e página própria. Os serviços mais procurados ficam a um clique.',
        'itens': [('Calendário de eventos', 'Os dias com evento ficam marcados. Um clique mostra o que vai acontecer.'),
                  ('O evento em destaque', 'Data, horário, local e quem organiza, com página própria para cada evento.'),
                  ('Serviços', 'Matrícula, Área do Estudante, Educação em Números, Fale com o Supervisor, Ouvidoria: cada card leva ao passo a passo.')]},
    4: {'titulo': 'Sistemas, equipe e rodapé', 'sub': 'Tudo conectado num só lugar',
        'marcas': m(4, [(330, 4290), (954, 4276), (400, 4636), (720, 5260)]),
        'porque': 'Quem entra no portal é levado direto ao sistema certo, e quem precisa falar com alguém encontra o nome, o cargo e o contato.',
        'itens': [('Sistemas da Secretaria', 'Os sistemas que a família e o servidor usam, num só lugar: creche, transferência, matrícula, uniforme.'),
                  ('CI Eletrônica integrada', 'A comunicação interna da Secretaria, sem papel, já ligada ao portal. E o próximo: Pesquisas da Educação.'),
                  ('Equipe gestora', 'Quem é quem na Secretaria, com cargo e contato.'),
                  ('Rodapé completo', 'Endereço, telefone, horário, e-mail e os links da transparência e do acesso à informação.')]},
}


TELAS = [('tela-servicos', 'Tela por tela', 'Carta de Serviços', [('documento', 'Todos os serviços', 'Busca e cards; cada um com quem pode pedir, prazo e como fazer.'), ('busca', 'Busca por serviço', 'Digite o que precisa e o serviço aparece.'), ('ok', 'Lei 13.460/2017', 'No modelo da Carta de Serviços ao Usuário.')]), ('tela-estudante', 'Tela por tela', 'Área do Estudante', [('escola', 'Tudo do estudante', 'Vestibulinho, bolsas, uniforme e matrícula numa página só.'), ('link', 'Atalhos diretos', 'Cada item leva ao serviço ou ao sistema certo.'), ('celular', 'No celular', 'Pensada para o aluno que acessa pelo telefone.')]), ('tela-noticias', 'Tela por tela', 'Notícias', [('imagem', 'Com foto', 'Grade que valoriza as fotos das escolas.'), ('busca', 'Busca e categorias', 'A notícia antiga continua fácil de achar.'), ('mundo', 'No Google e no WhatsApp', 'Cada notícia com endereço próprio e prévia bonita.')]), ('tela-noticia', 'Tela por tela', 'A notícia aberta', [('imagem', 'Foto e galeria', 'Foto de destaque, galeria e a fonte da informação.'), ('calendario', 'Datas claras', 'Publicação e atualização, sempre à vista.'), ('enviar', 'Compartilhar', 'Pronta para mandar às famílias no WhatsApp.')]), ('tela-eventos', 'Tela por tela', 'Agenda de eventos', [('calendario', 'Calendário da rede', 'Reuniões, provas e formações com data e local.'), ('relogio', 'Página do evento', 'Horário, local e quem organiza.'), ('olho', 'Sem recado perdido', 'A família e a escola veem a mesma agenda.')]), ('tela-transparencia', 'Tela por tela', 'Central de Transparência', [('olho', 'Por assunto', 'Como pedem a Lei de Acesso à Informação e a LC 131/2009.'), ('documento', 'Documentos', 'Relatórios, convênios, conselhos e prestação de contas.'), ('estrela', 'Radar da Transparência', 'Organizada pelos critérios do PNTP.')]), ('tela-legislacao', 'Tela por tela', 'Legislação com vigência', [('livro', 'Leis e portarias', 'Busca e filtros por tipo, ano e assunto.'), ('ok', 'Situação de cada norma', 'Em vigor, revogada ou alterada, sem dúvida.'), ('documento', 'Texto e arquivo', 'O texto na página e o PDF original.')]), ('tela-numeros', 'Tela por tela', 'Educação em Números', [('grafico', 'Indicadores', 'Unidades, matrículas, IDEB e professores.'), ('documento', 'Com fonte', 'A origem de cada dado, sempre informada.'), ('olho', 'A rede à vista', 'A Secretaria mostra o tamanho do que faz.')]), ('tela-estrutura', 'Tela por tela', 'Estrutura organizacional', [('pessoas', 'Quem é quem', 'Órgãos, responsáveis e competências.'), ('fone', 'Contato direto', 'Telefone e e-mail de cada área.'), ('ok', 'Lei 12.527/2011', 'O que a Lei de Acesso pede, organizado.')]), ('tela-perguntas', 'Tela por tela', 'Perguntas frequentes', [('pergunta', 'As dúvidas de sempre', 'Respondidas antes de a família ligar.'), ('busca', 'Na busca do portal', 'A resposta aparece quando a pessoa procura.'), ('caneta', 'A equipe atualiza', 'Nova dúvida, nova resposta, pelo painel.')]), ('tela-busca', 'Tela por tela', 'Busca no portal inteiro', [('busca', 'Uma busca só', 'Notícias, serviços, páginas, documentos e perguntas.'), ('raio', 'Mostra o que é cada resultado', 'Serviço, pergunta frequente, órgão ou notícia, com a data.'), ('ok', 'Sem se perder', 'A família acha o que precisa sem conhecer o menu.')])]


def tela(nome, sobre, titulo, cards, extra=()):
    """Uma tela inteira do portal na página, com três cartões curtos embaixo."""
    c = ''.join(f'<div>{ic(a, 20)}<b>{t}</b><small>{d}</small></div>' for a, t, d in cards)
    return (f'<span class="sobre">{sobre}</span><h2 class="tela-tit">{titulo}</h2>'
            f'<div class="tela-img">{navegador(nome)}</div>'
            + (f'<ul class="tela-extra">{"".join(f"<li><b>{t}</b> {d}</li>" for t, d in extra)}</ul>' if extra else '')
            + f'<div class="tela-cards">{c}</div>')


def paginas():
    P = []
    n = [1]
    marca = {}

    def M(chave):
        marca[chave] = n[0]

    def nova(html):
        P.append(html)
        n[0] += 1

    # 1. capa
    nova(f'''<section class="pg capa">
<div class="capa-topo"><span class="selo">Proposta · SECKE Sistemas</span></div>
<div class="capa-texto"><h1>Portal da<br><em>Educação</em></h1>
<p>Informação, serviços e sistemas da Secretaria Municipal de Educação num só lugar: no computador e no celular, com a cara da Educação.</p></div>
<div class="capa-arte"><img src="{img("destaque-0")}"></div>
<div class="capa-mock">{navegador("home-capa")}</div>
<div class="capa-cel"><img src="{img("cel-home")}"></div>
<div class="capa-pe"><span>Secretaria Municipal de Educação de Paulínia</span><span>Novembro de 2026</span></div></section>''')

    # 2. o desafio
    nova(f'''<section class="pg escura desafio">
<span class="sobre">O desafio de hoje</span>
<h2>A família precisa de uma informação da Educação.<br><em>Onde ela encontra?</em></h2>
<div class="jornada">
  <div class="passo-j"><span>{ic("busca", 30)}</span><b>Procura no site geral da Prefeitura</b><small>A Educação divide espaço com dezenas de secretarias. O caminho até a matrícula é longo.</small></div>
  <div class="passo-j"><span>{ic("documento", 30)}</span><b>Acha páginas soltas</b><small>Prazos, documentos e links ficam em lugares diferentes, nem sempre atualizados.</small></div>
  <div class="passo-j"><span>{ic("fone", 30)}</span><b>Liga para tirar a dúvida</b><small>Em época de matrícula, a linha ocupada vira fila.</small></div>
  <div class="passo-j"><span>{ic("carro", 30)}</span><b>Vai até a Secretaria</b><small>Perde a manhã de trabalho para resolver presencialmente o que podia ser feito em minutos.</small></div>
</div>
<div class="faixa-final">{ic("relogio", 26)} <span>Cada ida presencial é tempo da família e da equipe da Secretaria. <b>Boa parte disso se resolve com informação clara, no lugar certo.</b></span></div>
{rodape(2, True)}</section>''')

    # 3. a virada
    nova(f'''<section class="pg clara virada">
<span class="sobre">Com o Portal da Educação</span>
<h2>Do celular, em poucos minutos.</h2>
<div class="virada-grid">
  <div class="virada-cel"><img src="{img("cel-matricula")}"></div>
  <div>
    <ol class="linha-tempo">
      <li><span>1</span><div><b>Abre o Portal da Educação</b><small>Endereço próprio da Educação, fácil de lembrar e de achar no Google.</small></div></li>
      <li><span>2</span><div><b>Vê “Matrícula escolar” em destaque</b><small>O que é da época aparece primeiro, na página inicial.</small></div></li>
      <li><span>3</span><div><b>Assiste ao vídeo explicativo</b><small>Vídeos curtos, com legenda, mostram o passo a passo.</small></div></li>
      <li><span>4</span><div><b>Clica e vai direto para a inscrição</b><small>O botão leva ao sistema certo, sem procurar.</small></div></li>
      <li class="fim"><span>{ic("ok", 18)}</span><div><b>Resolvido, sem sair de casa</b><small>E a equipe da Secretaria ganha tempo para o que precisa de atendimento de verdade.</small></div></li>
    </ol>
  </div>
</div>
<div class="numeros-virada">
  <div><b>1</b><span>endereço para tudo da Educação</span></div>
  <div><b>24h</b><span>de informação, todos os dias</span></div>
  <div><b>100%</b><span>pensado para o celular</span></div>
</div>
{rodape(3)}</section>''')

    # 4. sumário
    itens = [('casa', 'O portal', 'A página inicial, parte por parte, e a página de destaque', '@portal'),
             ('video', 'Vídeos de orientação', 'A matrícula explicada em vídeo, com legenda', '@videos'),
             ('documento', 'Tela por tela', 'Serviços, notícias, eventos, transparência, legislação e a rede', '@telas'),
             ('acess', 'Para todos', 'Acessibilidade e celular', '@todos'),
             ('orbita', 'Sistemas em órbita', 'CI Eletrônica, Pesquisas e SIMAPE: geolocalização e vagas', '@orbita'),
             ('escola', 'Uma página para cada escola', 'O próximo passo possível', '@escola'),
             ('caneta', 'O painel', 'A Secretaria no comando, sem programador', '@painel'),
             ('pergunta', 'Perguntas e respostas', 'Segurança, dados, treinamento e o que pode dar errado', '@perguntas'),
             ('escudo', 'Tecnologia e próximos passos', 'A base técnica e o caminho até o ar', '@tecnologia')]
    nova(f'''<section class="pg clara sumario">
<span class="sobre">Neste material</span><h2>O que você vai ver</h2>
<ol class="sum">{"".join(f'<li><span class="s-ic">{ic(a, 26)}</span><div><b>{t}</b><small>{d}</small></div><span class="s-n">{p}</span></li>' for a, t, d, p in itens)}</ol>
<div class="nota-demo">{ic("olho", 20)} <span>Todas as imagens são do portal <b>já construído e funcionando</b> no endereço de demonstração. Algumas fotos e nomes de pessoas são ilustrativos, para a apresentação.</span></div>
{rodape(4)}</section>''')

    # 5..12. página inicial: imagem / explicação
    M('portal')
    for parte in range(1, 5):
        h = HOME[parte]
        nova(f'''<section class="pg vitrine">
<div class="vitrine-topo"><span class="sobre">Página inicial · parte {parte} de 4</span><h2>{h["titulo"]}</h2><p>{h["sub"]}</p></div>
<div class="vitrine-img">{navegador(f"home-{parte}", h["marcas"])}</div>
{rodape(n[0], True)}</section>''')
        nova(f'''<section class="pg clara explica">
<span class="sobre">Página inicial · parte {parte} de 4</span><h2>{h["titulo"]}</h2>
<div class="explica-grid"><div class="explica-mini">{navegador(f"home-{parte}", h["marcas"], "mini")}</div>{numerados(h["itens"])}</div>
<div class="porque"><span>Por que importa</span><p>{h["porque"]}</p></div>
{rodape(n[0])}</section>''')

    # 13. a página de destaque (carrossel)
    nova(f'''<section class="pg clara carrossel">
<span class="sobre">A página de destaque</span><h2>A capa do portal muda com a Secretaria</h2>
<p class="intro">O carrossel de destaques abre o portal. A Secretaria troca fotos, textos e artes de campanha pelo painel, em minutos: o novo portal, o uniforme, o Barco Escola, a matrícula.</p>
<div class="slides quatro">{"".join(f'<div class="slide"><img src="{img(f"destaque-{i}")}"><span>{i + 1}</span></div>' for i in range(4))}</div>
<div class="tres">
  <div>{ic("imagem", 24)}<b>Foto ou arte pronta</b><small>Foto com título e botão, ou a arte inteira da campanha, como um outdoor.</small></div>
  <div>{ic("calendario", 24)}<b>Agendado</b><small>O destaque entra e sai do ar sozinho, na data marcada.</small></div>
  <div>{ic("acess", 24)}<b>Acessível</b><small>Para sozinho com o mouse, tem botão de pausa e texto alternativo.</small></div>
</div>
{rodape(n[0])}</section>''')

    # 14. matrícula (imagem)
    M('videos')
    nova(f'''<section class="pg vitrine">
<div class="vitrine-topo"><span class="sobre">Vídeos de orientação</span><h2>Matrícula escolar</h2><p>A página que mais resolve: explica em vídeo, mostra e leva direto ao sistema</p></div>
<div class="vitrine-img alta">{navegador("matricula-topo")}</div>
{rodape(n[0], True)}</section>''')

    # 15. matrícula (explicação)
    nova(f'''<section class="pg clara explica">
<span class="sobre">Vídeos de orientação</span><h2>A família vê, entende e resolve na mesma página</h2>
<div class="video-destaque">{navegador("matricula-videos")}</div>
{numerados([("Vídeos curtos de orientação", "“Como fazer a inscrição no SISS” e “Como funciona a fila da creche”: cada etapa explicada em vídeo, com legenda. Quem prefere ler tem o mesmo conteúdo ao lado."),
            ("Ao lado de cada vídeo, o resumo e o botão", "“Fazer a inscrição” leva direto ao sistema da creche, sem procurar."),
            ("Quem pode, prazos, documentos e passo a passo", "No modelo da Carta de Serviços (Lei 13.460/2017), em linguagem simples."),
            ("Em qualquer serviço", "A equipe coloca vídeos em qualquer página de serviço pelo painel: vestibulinho, uniforme, bolsa de estudo. Menos fila e menos telefone tocando.")])}
{rodape(n[0])}</section>''')

    # 16..26. tela por tela: uma tela inteira por página
    M('telas')
    for nome, sobre, titulo, cards in TELAS:
        nova(f'''<section class="pg clara tela">{tela(nome, sobre, titulo, cards)}{rodape(n[0])}</section>''')

    # 20. acessibilidade
    M('todos')
    nova(f'''<section class="pg escura acess">
<span class="sobre">Para todos</span><h2>Acessível de verdade</h2>
<p class="intro">Seguindo o eMAG (modelo do Governo Federal) e as diretrizes internacionais WCAG.</p>
<div class="acess-img">{navegador("contraste")}</div>
<div class="acess-lista">
  <div>{ic("olho", 22)}<b>Alto contraste</b><small>Um clique troca o portal para fundo preto e letras amarelas.</small></div>
  <div>{ic("acess", 22)}<b>Libras (VLibras)</b><small>Tradução para Libras em todas as páginas.</small></div>
  <div>{ic("documento", 22)}<b>Tamanho do texto</b><small>A−, A e A+ na barra do topo.</small></div>
  <div>{ic("chave", 22)}<b>Atalhos de teclado</b><small>Conteúdo, menu, busca e rodapé, sem mouse.</small></div>
  <div>{ic("video", 22)}<b>Vídeos legendados</b><small>E o mesmo conteúdo em texto logo abaixo.</small></div>
  <div>{ic("imagem", 22)}<b>Texto alternativo</b><small>Toda imagem descrita para leitores de tela.</small></div>
</div>
{rodape(n[0], True)}</section>''')

    # 21. celular
    nova(f'''<section class="pg clara celular">
<span class="sobre">No celular</span><h2>Feito primeiro para o celular</h2>
<p class="intro">É pelo celular que a maioria das famílias acessa. Menu compacto, botões grandes para o polegar, nada de rolar para os lados.</p>
<div class="celulares">{"".join(f'<div class="cel"><img src="{img(c)}"></div>' for c in ["cel-home", "cel-matricula", "cel-noticias", "cel-servicos"])}</div>
<div class="legendas-cel"><span>Início</span><span>Matrícula</span><span>Notícias</span><span>Serviços</span></div>
{rodape(n[0])}</section>''')

    # sistemas em órbita
    M('orbita')
    sat = [('ci', 'CI Eletrônica', 'Comunicação interna sem papel', 'documento', 'SECKE'),
           ('pq', 'Pesquisas da Educação', 'Questionários com assistente de IA', 'grafico', 'SECKE'),
           ('sim', 'SIMAPE', 'Geolocalização e planejamento de vagas', 'pin', 'SECKE'),
           ('siss', 'SISS · Creches', 'Inscrição e fila de espera', 'escola', 'Prefeitura'),
           ('mat', 'Matrícula escolar', 'Pedido de vaga no Fundamental', 'livro', 'Prefeitura'),
           ('uni', 'Uniforme escolar', 'Cadastro para receber', 'pessoas', 'Prefeitura'),
           ('tra', 'Transferência', 'Troca de creche ou EMEI', 'seta', 'Prefeitura'),
           ('pai', 'Painel do portal', 'Onde a equipe publica', 'caneta', 'SECKE')]
    orb = ''.join(f'<div class="sat s{k}{" secke" if o == "SECKE" else ""}"><span>{ic(a, 22)}</span><b>{t}</b><small>{d}</small></div>' for k, (c, t, d, a, o) in enumerate(sat))
    nova(f'''<section class="pg escura orbita-pg">
<span class="sobre">Sistemas em órbita</span><h2>O portal no centro.<br><em>Os sistemas da Educação em volta.</em></h2>
<p class="intro">O portal é a porta de entrada. Em volta dele giram os sistemas que famílias e servidores usam, com o mesmo login para os servidores e a mesma identidade da Educação.</p>
<div class="orbita"><i class="anel a1"></i><i class="anel a2"></i><div class="nucleo">{ic("casa", 34)}<b>Portal da<br>Educação</b></div>{orb}</div>
<div class="legenda-orb"><span><i class="ponto secke"></i>Sistemas SECKE, integrados ao portal</span><span><i class="ponto"></i>Sistemas da Prefeitura, ligados pelo portal</span></div>
{rodape(n[0], True)}</section>''')

    # integração: a faixa no portal
    nova(f'''<section class="pg clara integracao2">
<span class="sobre">Sistemas em órbita</span><h2>Um clique e a pessoa está no sistema certo</h2>
<p class="intro">A faixa “Sistemas da Secretaria de Educação”, na página inicial, reúne tudo. Os sistemas dos servidores (CI Eletrônica, Pesquisas e SIMAPE) entram com o mesmo e-mail e senha do portal.</p>
<div class="integra-img">{navegador("sistemas")}</div>
<div class="fluxo-integra claro">
  <div><span>{ic("casa", 24)}</span><b>Entra no portal</b><small>pelo celular ou computador</small></div><i>{ic("seta", 22)}</i>
  <div><span>{ic("link", 24)}</span><b>Toca no sistema</b><small>na faixa da página inicial</small></div><i>{ic("seta", 22)}</i>
  <div><span>{ic("chave", 24)}</span><b>Mesmo login</b><small>o servidor usa o e-mail e a senha de sempre</small></div>
</div>
<div class="frase">Um só endereço para lembrar. Uma só senha para o servidor. Uma só cara para a Educação.</div>
{rodape(n[0])}</section>''')

    # CI eletrônica: tela inteira + detalhes
    nova(f'''<section class="pg clara tela">{tela("ci-inicio", "Sistema em órbita · CI Eletrônica", "A comunicação interna, sem papel",
        [("enviar", "Escrever e enviar", "A CI no modelo oficial, numerada sozinha."), ("cadeado", "Assinatura com PIN", "Assinatura eletrônica pessoal, com QR Code."), ("relogio", "Nada fica parado", "Avisa quando uma CI está parada há dias.")],
        [("Início do dia:", "o que chegou, o que está em andamento, o que espera assinatura e o que está parado, numa tela só."),
         ("Por unidade:", "cada setor e cada escola tem a sua caixa; quem troca de unidade troca de caixa num clique."),
         ("Folha oficial:", "a CI sai no modelo da Prefeitura, com número, data, assinatura eletrônica e QR Code."),
         ("Ditado por voz:", "dá para falar em vez de digitar; o sistema escreve o texto na folha."),
         ("Para fora da Secretaria:", "a CI também vai para outros órgãos, em PDF, com verificação pública.")])}{rodape(n[0])}</section>''')
    nova(f'''<section class="pg clara ci">
<span class="sobre">Sistema em órbita · CI Eletrônica</span><h2>O caminho de cada CI, do envio à resposta</h2>
<div class="ci-grid2"><div>{navegador("ci-caminho")}<small>O fluxograma do trâmite: quem recebeu, quando, quanto tempo ficou e o que cada setor despachou.</small></div>
<div class="ci-folha"><img src="{img("ci-impressao")}"><small>A folha oficial, pronta para imprimir ou salvar em PDF, com o código de verificação.</small></div></div>
<div class="tres quatro">
  <div>{ic("mapa", 24)}<b>Tramitação livre</b><small>Cópias em paralelo para várias unidades ao mesmo tempo.</small></div>
  <div>{ic("escudo", 24)}<b>Verificação pública</b><small>Qualquer pessoa confere se a assinatura é verdadeira.</small></div>
  <div>{ic("busca", 24)}<b>Consulta e relatórios</b><small>Pesquisa por número, assunto, unidade e período.</small></div>
  <div>{ic("treino", 24)}<b>Guia do usuário</b><small>57 páginas ilustradas, uma unidade por papel.</small></div>
</div>
{rodape(n[0])}</section>''')

    # Pesquisas
    nova(f'''<section class="pg clara tela">{tela("pq-editor", "Sistema em órbita · Pesquisas da Educação", "Pesquisas e questionários da rede, do jeito certo",
        [("caneta", "Monta em minutos", "Capa, perguntas, escala de satisfação e quantidades por tamanho."), ("pessoas", "Para quem", "Escolas, servidores, pais e comunidade, por grupos."), ("ok", "Uma resposta por pessoa", "Identificada ou anônima, com comprovante.")],
        [("Assistente de IA:", "monta a pesquisa a partir do que a pessoa conta e sugere melhorias, sempre com “Ver como ficaria” antes."),
         ("Aprovação:", "pesquisa para pais e comunidade passa por quem aprova na Secretaria antes de sair."),
         ("Quem falta:", "o gestor vê quem já respondeu e quem falta, e manda o lembrete com o link pessoal de cada um."),
         ("Resultados:", "gráficos por pergunta, comparação entre regiões e tipos de escola, PDF, apresentação e planilha.")])}{rodape(n[0])}</section>''')
    nova(f'''<section class="pg clara pq2">
<span class="sobre">Sistema em órbita · Pesquisas da Educação</span><h2>Do questionário ao resultado, com um assistente de IA</h2>
<div class="pq-grid2"><div>{navegador("pq-assistente")}<small>“Criar com o assistente”: a pessoa conta o que quer saber e o assistente monta a pesquisa (aceita até o PDF ou a foto de um questionário em papel).</small></div>
<div class="pq-cel"><img src="{img("pq-celular")}"><small>Quem responde vê a pesquisa no celular, uma pergunta por tela.</small></div></div>
<div class="pq-res">{navegador("pq-resultados2")}<small>Resultados em gráficos, com filtros por tipo de escola e região, modo apresentação, PDF e planilha.</small></div>
{rodape(n[0])}</section>''')

    # SIMAPE
    nova(f'''<section class="pg clara tela">{tela("sim-bairros", "Sistema em órbita · SIMAPE", "Geolocalização: a rede inteira no mapa",
        [("pin", "Alunos e escolas no mapa", "13 mil alunos e 90 escolas georreferenciados."), ("mapa", "Bairros e setores", "Cobertura de cada escola, bairro por bairro."), ("grafico", "Indicadores na hora", "Alocados, sem vaga e quem precisa de transporte.")],
        [("Geolocalização:", "cada aluno e cada escola no ponto certo do mapa, a partir do endereço."),
         ("Cobertura:", "que bairros cada escola atende dentro do raio, e onde a rede não chega."),
         ("Setores:", "vagas e demanda por setor, para decidir onde abrir turma ou ampliar escola."),
         ("Consulta pública:", "a família consulta a matrícula e a escola de destino pelo CPF do responsável.")])}{rodape(n[0])}</section>''')
    nova(f'''<section class="pg clara sim2">
<span class="sobre">Sistema em órbita · SIMAPE</span><h2>Planejar vagas antes de faltar vaga</h2>
<p class="intro">Cenários de demanda com os alunos reais: o sistema distribui cada aluno na escola mais próxima com vaga na série e mostra onde vai faltar, onde sobra e quem vai precisar de transporte.</p>
<div class="sim-grid">{navegador("sim-demanda")}{navegador("sim-relatorio")}</div>
<div class="tres">
  <div>{ic("raio", 24)}<b>Simulação em segundos</b><small>12 mil alunos distribuídos por proximidade, série a série.</small></div>
  <div>{ic("ia", 24)}<b>Projetor de solução</b><small>Uma IA lê o cenário e sugere onde ampliar ou abrir turmas.</small></div>
  <div>{ic("documento", 24)}<b>Relatórios</b><small>Cobertura por escola e demanda por setor, prontos para imprimir.</small></div>
</div>
{rodape(n[0])}</section>''')
    nova(f'''<section class="pg clara sim3">
<span class="sobre">Sistema em órbita · SIMAPE</span><h2>Aluno novo: a resposta para a família na hora</h2>
<div class="sim3-grid"><div>{navegador("sim-aluno-novo")}<small>Data de nascimento e CEP: o sistema diz a série (idade em 31/03), o setor, o bairro e as escolas mais próximas que atendem a série, com distância e vagas.</small></div>
<div class="sim-folha"><img src="{img("sim-aluno-novo-relatorio")}"><small>O relatório colorido, com o mapa, para entregar à família.</small></div></div>
{rodape(n[0])}</section>''')

    # uma página para cada escola (possibilidade)
    M('escola')
    nova(f'''<section class="pg clara escola-pg">
<span class="sobre">O próximo passo possível</span><h2>Uma página para cada escola</h2>
<p class="intro">Hoje cada escola já publica as próprias notícias pelo painel, só nas dela. O passo seguinte é cada unidade ter a sua página no portal: recados, eventos, equipe, horário e como chegar, mantida pela própria escola.</p>
<div class="escola-img">{navegador("escola-mock")}<span class="selo-sim">Simulação · ainda não está no portal</span></div>
<div class="tres">
  <div>{ic("escola", 24)}<b>Mantida pela escola</b><small>O papel “Escola” do painel já existe: cada uma mexe só no que é seu.</small></div>
  <div>{ic("pin", 24)}<b>Ligada ao mapa</b><small>Endereço e localização vêm do cadastro das unidades e do SIMAPE.</small></div>
  <div>{ic("pessoas", 24)}<b>Perto da família</b><small>Recados e eventos da escola do filho, num endereço só.</small></div>
</div>
{rodape(n[0])}</section>''')

    # 24. painel 1
    M('painel')
    nova(f'''<section class="pg escura painel1">
<span class="sobre">O painel</span><h2>A Secretaria no comando.<br><em>Sem programador.</em></h2>
<p class="intro">Tudo o que aparece no portal é mantido pela própria equipe da Educação, num painel simples. Com um treinamento básico, quem sabe usar e-mail sabe publicar uma notícia.</p>
<div class="painel-grid"><div>{navegador("painel-noticia-editar")}<small>Editar uma notícia: título, foto, texto e quando publicar</small></div>
<div>{navegador("painel-biblioteca")}<small>Biblioteca de imagens: escolher uma foto já enviada</small></div></div>
{rodape(n[0], True)}</section>''')

    # 25. painel 2
    tudo = [('caneta', 'Notícias e páginas', 'Editor visual, rascunho, agendamento e data para sair do ar.'),
            ('imagem', 'Destaques e avisos', 'A capa do portal e a faixa de aviso, com fotos ou artes prontas.'),
            ('video', 'Vídeos dos serviços', 'Vídeos com legenda nas páginas de serviço.'),
            ('paleta', 'Cores e identidade', 'Cores, fontes, brasão e dados de contato.'),
            ('engrenagem', 'Menus e página inicial', 'A ordem dos blocos, os títulos e o menu.'),
            ('link', 'Sistemas', 'Os atalhos para os sistemas da Secretaria.'),
            ('escola', 'Escolas e equipe', 'Unidades, regiões, supervisores e equipe gestora.'),
            ('olho', 'Transparência e leis', 'Documentos, legislação com vigência e a central de transparência.')]
    nova(f'''<section class="pg clara painel2">
<span class="sobre">O painel</span><h2>Tudo o que a equipe pode mudar</h2>
<div class="painel-mini">{navegador("painel-identidade")}{navegador("painel-destaque-novo")}{navegador("painel-menus")}</div>
<div class="grade-oito">{"".join(f'<div>{ic(a, 22)}<b>{t}</b><small>{d}</small></div>' for a, t, d in tudo)}</div>
{rodape(n[0])}</section>''')

    # 26. painel 3: permissões e treinamento
    nova(f'''<section class="pg clara painel3">
<span class="sobre">O painel</span><h2>Cada um mexe só no que é seu</h2>
<div class="papeis">
  <div class="papeis-tit">Papéis configuráveis, por exemplo:</div>
  <div><span>{ic("chave", 24)}</span><b>Administrador</b><small>Configura o portal, os usuários e as permissões.</small></div>
  <div><span>{ic("caneta", 24)}</span><b>Publicador</b><small>Publica, agenda e retira conteúdo do ar.</small></div>
  <div><span>{ic("documento", 24)}</span><b>Redator</b><small>Escreve rascunhos para alguém aprovar.</small></div>
  <div><span>{ic("escola", 24)}</span><b>Escola</b><small>Publica as notícias da própria escola, e só delas.</small></div>
</div>
<div class="dupla-grid">{navegador("painel-escola-noticia")}{navegador("painel-papeis")}</div>
<div class="treino">{ic("treino", 30)}<div><b>Treinamento básico, guia ilustrado e suporte</b><span>A equipe aprende a publicar em uma tarde. Cada função tem passo a passo com as telas, e tudo o que é feito fica registrado na auditoria: quem mudou o quê, e quando.</span></div></div>
{rodape(n[0])}</section>''')

    # 27. perguntas
    M('perguntas')
    pq = [('É seguro?', 'Sim. O acesso ao painel é por usuário e senha pessoais, cada pessoa só vê e altera o que o seu papel permite, e o próprio banco de dados confere essas regras a cada pedido.'),
          ('Onde ficam os dados?', 'Em um banco de dados no Brasil (São Paulo), com cópia de segurança diária guardada por 30 dias.'),
          ('Precisa de programador para atualizar?', 'Não. Notícias, páginas, destaques, cores, menus e sistemas são mantidos pela equipe da Secretaria no painel.'),
          ('Quanto treinamento é preciso?', 'Um treinamento básico. Quem usa e-mail e redes sociais publica uma notícia no primeiro dia.'),
          ('E os endereços do site antigo?', 'Os endereços antigos são redirecionados automaticamente para as páginas novas: quem tem o link salvo não se perde.'),
          ('E a LGPD?', 'O portal não exige cadastro do cidadão nem usa cookies de rastreamento. As fotos de pessoas são publicadas com autorização.'),
          ('Aguenta o pico da matrícula?', 'O portal é servido pela rede global da Cloudflare, com cópias das páginas perto de quem acessa: muitos acessos ao mesmo tempo não derrubam o site.'),
          ('Os dados são da Secretaria?', 'Sim. Todo o conteúdo pode ser exportado a qualquer momento, completo.')]
    nova(f'''<section class="pg clara perguntas">
<span class="sobre">Perguntas e respostas</span><h2>O que costumam perguntar</h2>
<div class="pq-grid">{"".join(f'<div><b>{ic("pergunta", 20)} {p}</b><span>{r}</span></div>' for p, r in pq)}</div>
{rodape(n[0])}</section>''')

    # 28. o que pode dar errado
    pr = [('Publiquei algo errado', 'Retire do ar em um clique e corrija. Tudo fica no histórico, e dá para agendar a publicação para conferir antes.'),
          ('Um link parou de funcionar', 'O portal confere os links automaticamente e avisa no painel quais estão quebrados.'),
          ('Alguém esqueceu a senha', 'A própria pessoa recebe um link para criar outra, pelo e-mail.'),
          ('Uma pessoa saiu da Secretaria', 'O administrador desativa o acesso dela na hora; o que ela publicou continua.'),
          ('O conteúdo envelheceu', 'Notícias e avisos podem ter data para sair do ar sozinhos.'),
          ('Um sistema externo está fora do ar', 'O portal continua no ar; um aviso no topo informa as famílias enquanto o sistema volta.')]
    nova(f'''<section class="pg clara problemas">
<span class="sobre">Perguntas e respostas</span><h2>Se algo der errado, a solução já está prevista</h2>
<div class="pr-lista">{"".join(f'<div><span class="pr-a">{ic("alerta", 20)}</span><div><b>{p}</b><span>{r}</span></div></div>' for p, r in pr)}</div>
<div class="nota-demo">{ic("pessoas", 20)} <span>Dúvidas e problemas também chegam à SECKE pelo próprio painel (área de chamados), com o registro de quem pediu e da resposta.</span></div>
{rodape(n[0])}</section>''')

    # 29. tecnologia
    M('tecnologia')
    tec = [('nuvem', 'Cloudflare', 'Rede global: o portal abre rápido em qualquer lugar e é protegido contra ataques e picos de acesso.'),
           ('banco', 'Supabase · PostgreSQL', 'Banco de dados profissional, hospedado em São Paulo.'),
           ('cadeado', 'Segurança por registro (RLS)', 'Cada linha do banco tem regra de acesso: a regra vale no banco, não só na tela.'),
           ('escudo', 'Cópias de segurança', 'Backup diário, guardado por 30 dias, e exportação completa dos dados.'),
           ('olho', 'Auditoria', 'Quem mudou o quê e quando, para cada alteração do painel.'),
           ('mundo', 'Pronto para o Google', 'Páginas geradas no servidor, endereços amigáveis, mapa do site e dados estruturados.'),
           ('acess', 'eMAG e WCAG', 'Acessibilidade conferida página por página.'),
           ('raio', 'Uma base para muitos', 'A mesma base atende secretarias, prefeituras e câmaras, cada uma com a sua identidade.')]
    nova(f'''<section class="pg escura tecnologia">
<span class="sobre">Para quem quer os detalhes</span><h2>Construído com o que há de mais robusto</h2>
<p class="intro">A mesma tecnologia usada por empresas e governos no mundo todo, sem servidor para a Prefeitura manter.</p>
<div class="tec-grid">{"".join(f'<div><span>{ic(a, 24)}</span><b>{t}</b><small>{d}</small></div>' for a, t, d in tec)}</div>
{rodape(n[0], True)}</section>''')

    # 30. próximos passos
    nova(f'''<section class="pg clara passos-pg">
<span class="sobre">Próximos passos</span><h2>O portal já existe. Falta ligar.</h2>
<p class="intro">Tudo o que você viu está construído e funcionando no endereço de demonstração. Para ir ao ar:</p>
<ol class="passos-grandes">
  <li><span>1</span><div><b>Apresentação e ajustes</b><small>A Secretaria navega no portal e indica o que quer mudar.</small></div></li>
  <li><span>2</span><div><b>Endereço oficial</b><small>O domínio da Educação (definido com a Prefeitura).</small></div></li>
  <li><span>3</span><div><b>Conteúdo e fotos reais</b><small>Equipe, escolas, serviços e fotos autorizadas no lugar dos exemplos.</small></div></li>
  <li><span>4</span><div><b>Treinamento da equipe</b><small>Uma tarde de prática no painel, com o guia ilustrado.</small></div></li>
  <li class="fim"><span>{ic("ok", 20)}</span><div><b>No ar</b><small>Os endereços do site antigo passam a levar ao portal novo.</small></div></li>
</ol>
{rodape(n[0])}</section>''')

    # 31. contracapa
    nova(f'''<section class="pg contracapa">
<div class="cc-slides">{"".join(f'<img src="{img(f"destaque-{i}")}">' for i in range(3))}</div>
<div class="cc-texto"><span class="selo">SECKE Sistemas</span><h2>Vamos colocar a Educação<br>na palma da mão das famílias?</h2>
<p>Sistemas públicos com foco na experiência de quem usa.</p>
<div class="contato"><span>{ic("fone", 20)} [telefone]</span><span>{ic("enviar", 20)} [e-mail]</span></div></div></section>''')
    # números de página no sumário
    for k, v in marca.items():
        P = [x.replace(f'@{k}<', f'{v:02d}<') for x in P]
    return P


def montar():
    css = (AQUI / 'apresentacao.css').read_text()
    html = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Portal da Educação · Apresentação</title>'
            f'<link href="https://fonts.googleapis.com/css2?family=Raleway:wght@500;600;700;800;900&family=Nunito+Sans:wght@400;600;700&display=swap" rel="stylesheet">'
            f'<style>{css}</style></head><body>{"".join(paginas())}</body></html>')
    (AQUI / 'apresentacao.html').write_text(html)
    pdf = BASE / 'Portal-Educacao-Apresentacao.pdf'
    js = f'''const {{ chromium }} = require('playwright');
(async () => {{ const b = await chromium.launch(); const p = await b.newPage();
  await p.goto('file://{AQUI / "apresentacao.html"}'); await p.waitForLoadState('networkidle'); await p.waitForTimeout(1000);
  await p.pdf({{ path: '{pdf}', width: '210mm', height: '297mm', printBackground: true, margin: {{ top: 0, bottom: 0, left: 0, right: 0 }} }});
  await b.close(); }})();'''
    env = dict(os.environ, NODE_PATH=subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip())
    subprocess.run(['node', '-e', js], check=True, env=env)
    print('ok', pdf)


if __name__ == '__main__':
    montar()

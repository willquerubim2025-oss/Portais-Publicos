// Fotos do portal publicado para a apresentação (D-136 do portal-municipal). Rode a partir de docs/portfolio/apresentacao:
//   mkdir -p img-bruto && NODE_PATH=$(npm root -g) node fonte/capturar.cjs
const { chromium } = require('playwright');
const U = 'https://portal-municipal.willquerubim2025.workers.dev';
(async () => {
  const b = await chromium.launch();
  async function pg(w = 1440, h = 900, dsf = 2) { return b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: dsf }); }
  async function abrir(p, url) {
    await p.goto(U + url, { waitUntil: 'networkidle' }); await p.waitForTimeout(800);
    await p.evaluate(() => { const pz = document.querySelector('[data-pausa]'); if (pz && pz.getAttribute('aria-pressed') !== 'true') pz.click();
      document.querySelector('[data-ir="0"]')?.click(); document.querySelector('#vlibras-access-wrapper')?.remove(); document.querySelectorAll('[vw]').forEach((e) => e.remove()); });
    // carrega as imagens "preguiçosas": rola até o fim e volta, e espera todas terminarem
    await p.evaluate(async () => { document.querySelectorAll('img[loading="lazy"]').forEach((i) => { i.loading = 'eager'; });
      for (let y = 0; y < document.body.scrollHeight; y += 600) { scrollTo(0, y); await new Promise((r) => setTimeout(r, 120)); } scrollTo(0, 0); });
    await p.waitForFunction(() => [...document.images].every((i) => i.complete), null, { timeout: 15000 }).catch(() => {});
    await p.waitForTimeout(900);
  }
  // home inteira (depois é cortada em partes)
  let p = await pg(); await abrir(p, '/'); await p.screenshot({ path: 'img-bruto/home.png', fullPage: true });
  for (const i of [1, 2]) { await p.evaluate((i) => document.querySelector(`[data-ir="${i}"]`)?.click(), i); await p.waitForTimeout(1200);
    await p.locator('.v-destaque').screenshot({ path: `img-bruto/destaque-${i}.png` }); }
  await p.evaluate(() => document.querySelector('[data-ir="0"]')?.click()); await p.waitForTimeout(1200);
  await p.locator('.v-destaque').screenshot({ path: 'img-bruto/destaque-0.png' });
  await p.close();
  for (const [n, url] of [['matricula', '/servicos/matricula-escolar'], ['servicos', '/servicos'], ['noticias', '/noticias'],
    ['noticia', '/noticias/paulinia-abre-cadastro-para-uniforme-escolar-de-2027'], ['transparencia', '/transparencia'], ['legislacao', '/legislacao'],
    ['supervisor', '/fale-com-o-supervisor'], ['numeros', '/educacao-em-numeros'], ['estrutura', '/estrutura-organizacional'], ['estudante', '/servicos/area-do-estudante'],
    ['perguntas', '/perguntas-frequentes'], ['acessibilidade', '/acessibilidade'], ['bolsa', '/servicos/bolsa-de-estudo'], ['evento', '/eventos/prova-do-vestibulinho-2027']]) {
    p = await pg(); await abrir(p, url); await p.screenshot({ path: `img-bruto/${n}.png`, fullPage: true }); await p.close(); console.log('ok', n);
  }
  // alto contraste
  p = await pg(); await abrir(p, '/');
  await p.evaluate(() => { const bt = [...document.querySelectorAll('button')].find((x) => /contraste/i.test(x.textContent || x.getAttribute('aria-label') || '')); bt?.click(); });
  await p.waitForTimeout(700); await p.screenshot({ path: 'img-bruto/contraste.png' }); await p.close();
  // celular
  for (const [n, url] of [['cel-home', '/'], ['cel-matricula', '/servicos/matricula-escolar'], ['cel-noticias', '/noticias'], ['cel-servicos', '/servicos']]) {
    p = await pg(390, 844, 3); await abrir(p, url); await p.screenshot({ path: `img-bruto/${n}.png` }); await p.close();
  }
  await b.close();
})();

// Simulação da "página da escola" (ainda não existe no portal): rode a partir de docs/portfolio/apresentacao
const { chromium } = require('playwright');
const fs = require('fs');
fs.copyFileSync('fonte/escola.html', 'img-bruto/escola.html'); // o HTML fica versionado em fonte/; as fotos (escola-foto, t1..t3) saem dos destaques
(async () => { const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1440, height: 1200 }, deviceScaleFactor: 2 });
  await p.goto('file://' + process.cwd() + '/img-bruto/escola.html'); await p.waitForTimeout(1500);
  await p.screenshot({ path: 'img-bruto/escola-mock.png', fullPage: true }); await b.close(); })();

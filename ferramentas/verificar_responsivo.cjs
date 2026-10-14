const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  for (const w of [320, 360, 390, 414, 768]) {
    const ctx = await b.newContext({ viewport: { width: w, height: 800 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 });
    const p = await ctx.newPage();
    await p.route(/^https?:/, r => r.abort()); await p.goto('file://' + process.argv[2]);
    await p.evaluate(() => { document.querySelectorAll('dialog[open]').forEach(d => d.close()); document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager'); });
    await p.waitForTimeout(500);
    const r = await p.evaluate(() => {
      const W = document.documentElement.clientWidth;
      const vis = (e) => { const s = getComputedStyle(e); const r = e.getBoundingClientRect(); return s.display !== 'none' && s.visibility !== 'hidden' && r.width > 0 && r.height > 0 && !e.closest('.sr-only,[aria-hidden="true"],.v-pular,dialog:not([open])'); };
      const nome = (e) => (e.id ? '#' + e.id : '') + (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\s+/).slice(0, 2).join('.') : '') + ' ' + (e.textContent || e.getAttribute('aria-label') || '').trim().slice(0, 30);
      const vaza = [];
      document.querySelectorAll('body *').forEach((e) => { if (!vis(e)) return; const r = e.getBoundingClientRect();
        if ((r.right > W + 1 || r.left < -1) && !e.closest('.v-destaque, .v-slide, .v-secao-titulo, .v-cab-pista')) vaza.push(`${e.tagName.toLowerCase()}${nome(e)} [${Math.round(r.left)}..${Math.round(r.right)}]`); });
      const toque = [];
      document.querySelectorAll('a, button, input, summary').forEach((e) => { if (!vis(e)) return; const r = e.getBoundingClientRect();
        if ((r.width < 24 || r.height < 24) && !e.closest('p, li > p, address, .v-noticia h3, .v-rod-links, .v-topo .atalhos')) toque.push(`${e.tagName.toLowerCase()}${nome(e)} ${Math.round(r.width)}x${Math.round(r.height)}`); });
      const fonte = new Set();
      document.querySelectorAll('body *').forEach((e) => { if (!vis(e) || !e.childNodes.length || ![...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) return;
        const f = parseFloat(getComputedStyle(e).fontSize); if (f < 12) fonte.add(`${e.tagName.toLowerCase()}${nome(e)} ${f}px`); });
      return { rolagemHorizontal: document.documentElement.scrollWidth - W, altura: document.documentElement.scrollHeight, vaza: vaza.slice(0, 12), toquePequeno: toque.slice(0, 15), fontePequena: [...fonte].slice(0, 12) };
    });
    console.log('\n=== ' + w + ' px'); console.log(JSON.stringify(r, null, 1));
    await p.screenshot({ path: `${process.argv[3]}-${w}.png`, fullPage: true });
    await ctx.close();
  }
  await b.close();
})();

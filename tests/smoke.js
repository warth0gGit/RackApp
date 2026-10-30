// Smoke test: opens an offline build of RackApp and walks the main flows.
// Run: python3 tools/build.py example-rack dist && node tests/smoke.js [path/to/rackapp-offline.html]
// Needs the `playwright` package (npm i -D playwright, or a global install with NODE_PATH set).
const { chromium } = require("playwright");
const path = require("path");
const file = "file://" + path.resolve(process.argv[2] || path.join(__dirname, "..", "dist", "rackapp-offline.html"));
const shots = process.env.SHOTS_DIR;
(async () => {
  const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
  const fails = [];
  const check = (ok, msg) => { if (!ok) fails.push(msg); console.log((ok ? "  ok   " : "  FAIL ") + msg); };
  for (const [w, h, scheme] of [[1366, 900, "light"], [400, 860, "dark"]]) {
    console.log(`viewport ${w}x${h} ${scheme}`);
    const p = await browser.newPage({ viewport: { width: w, height: h }, colorScheme: scheme });
    const errs = []; p.on("pageerror", e => errs.push(e.message));
    await p.goto(file); await p.waitForSelector(".panel");
    check((await p.textContent("#rack-name")).trim().length > 0, "rack name shown");
    // first visit starts the tour
    await p.waitForSelector(".tour-card:not([hidden])", { timeout: 4000 });
    let steps = 0;
    while (await p.isVisible('.tour-card [data-t="next"]')) {
      if (shots && steps === 0) await p.screenshot({ path: `${shots}/tour-${w}.png` });
      await p.click('.tour-card [data-t="next"]'); steps++; if (steps > 20) break;
    }
    check(steps >= 6, `tour ran through ${steps} steps`);
    check(await p.isHidden(".tour-card"), "tour closes at the end");
    // rack
    const panels = await p.$$("#cases .panel:not(.power)");
    check(panels.length > 0, `${panels.length} modules drawn`);
    const first = panels[0]; const label = (await first.getAttribute("aria-label")).split(",")[0];
    await first.click();
    check((await p.textContent("#detail h3")) === label, "selecting a module opens its details");
    await p.click("#cat-chips .chip");
    check((await p.$$("#cases .hit")).length > 0, "category filter lights up matching modules");
    if (shots) await p.screenshot({ path: `${shots}/rack-${w}.png` });
    // manuals
    await p.click("#tab-manuals");
    await p.fill("#man-search", label);
    await p.waitForTimeout(300);
    check((await p.$$("#man-list .hit-item")).length > 0, "manual search finds results");
    await p.click("#man-list .hit-item");
    check((await p.textContent("#reader h3")).length > 0, "search hit opens the manual reader");
    check(await p.isVisible("#chat-off"), "chat explains it needs Claude when offline");
    if (shots) await p.screenshot({ path: `${shots}/manuals-${w}.png` });
    // walkthroughs
    await p.click("#tab-walkthroughs");
    if (await p.$(".wcard")) {
      await p.click(".wcard");
      check((await p.textContent(".sheet h2.title")).length > 0, "walkthrough opens");
      await p.click(".step input");
      check((await p.$$(".step.done")).length === 1, "ticking a step marks it done");
      if (shots) await p.screenshot({ path: `${shots}/walk-${w}.png` });
    } else check(await p.isVisible(".empty-cards"), "empty walkthrough library explains how to add one");
    // replay tour from the header
    await p.click("#tour-btn");
    check(await p.isVisible(".tour-card"), "tour can be replayed");
    await p.keyboard.press("Escape");
    check(await p.evaluate(() => document.documentElement.scrollWidth <= innerWidth), "no horizontal page scroll");
    check(errs.length === 0, "no page errors" + (errs.length ? ": " + errs.join("; ") : ""));
    await p.close();
  }
  await browser.close();
  if (fails.length) { console.log(`\n${fails.length} check(s) failed`); process.exit(1); }
  console.log("\nAll checks passed");
})();

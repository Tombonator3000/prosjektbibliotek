---
id: playwright-swiftshader-three-lokalt
tittel: Nettleserttester av three.js-spill uten skjermkort og uten nett
domene: testing
stikkord: Playwright, headless, Chromium, SwiftShader, WebGL, CDN, importmap, route, node_modules, skjermbilder, offline, CI
stack: Playwright med headless Chromium, three.js fra jsdelivr via importmap
status: PASS
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:tools/test/shot.mjs#L20
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# Nettleserttester av three.js-spill uten skjermkort og uten nett

## Symptom

Testene i en sky- eller CI-maskin gir svart lerret, «WebGL not supported», eller henger fordi three.js ikke kan hentes fra CDN.

## Årsak

Maskinen har ikke noe skjermkort, og nettet er ofte stengt eller tregt. Spillet henter three.js fra jsdelivr.

## Løsning

- Start Chromium med SwiftShader: `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist`.
- Rut forespørslene til three.js mot den lokale `node_modules/three`:

```js
await page.route(/cdn\.jsdelivr\.net\/npm\/three@[^/]+\/(.*)$/, async route => {
  const m = route.request().url().match(/three@[^/]+\/(.*)$/);
  await route.fulfill({ status: 200, contentType: 'application/javascript', body: fs.readFileSync(path.join(THREE_DIR, m[1])) });
});
```

- Stopp eller server skriftene selv (fontsource lokalt), så siden ikke venter på Google Fonts.
- Ta handlingene som JSON (`eval`, `wait`, `key`, `shot`), og skriv loggen til en fil.

## Fallgruver

- SwiftShader bruker 5 til 30 s per bilde i store scener. Vent på en tilstand (for eksempel `G.state === 'world'`), ikke på et fast antall millisekunder.
- Skriv utdata til en fil. Piper du til `tail` og kjøringen tidsavbrytes, er alt borte.
- Tall for fps fra SwiftShader sier ingenting om ekte maskiner. Merk ytelse som UNVERIFIED.
- SwiftShader kan regne dybden feil på én stor bakkeflate som går bak kameraet. Del den opp i mindre celler.

## Slik verifiseres det

`node tools/test/shot.mjs file://$PWD/dist/index.html ut.png 4000 '[{"t":"shot"}]'` gir et bilde med scenen og ingen feil i loggen.

## Bevis

- [memory.md i DoD-Roguelite, testriggen](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/memory.md?plain=1#L160) og [fellene](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/memory.md?plain=1#L172).
- [Loggen 9. oktober 00:48: alle testene grønne](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/log.md?plain=1#L271).

## Brukt i

- `Tombonator3000/DoD-Roguelite@5e940d2`: alle skjermbilder, stresstester og CI-jobbene siden 0.1.

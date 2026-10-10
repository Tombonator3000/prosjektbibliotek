---
id: en-html-fil-uten-fetch
tittel: Hele spillet i én HTML-fil uten fetch
domene: bygg
stikkord: én fil, single file, base64, data-URI, artifact, sandkasse, fetch blokkert, esbuild, importmap, budsjett, offline
stack: esbuild, three.js r170 fra jsdelivr via importmap, Claude-artifact og GitHub Pages
status: PASS
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:build.mjs#L30
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# Hele spillet i én HTML-fil uten fetch

## Symptom

Spillet virker lokalt, men som Claude-artifact lastes ikke modeller og teksturer, fordi sandkassen blokkerer fetch av egne filer.

## Årsak

Artifact-sandkassen tillater bare skript fra noen få CDN-er. Alt annet, også spillets egne filer, må ligge inne i HTML-fila.

## Løsning

- Bygg med esbuild til én fil.
- Legg modeller, teksturer og bilder inn som base64: data-URI-er for bilder, og globale variabler for binærdata.
- Hent three.js fra jsdelivr med en importmap, med eksakt versjon.
- Lag to utgaver: `index.html` (vanlig side) og `artifact.html` uten doctype og head, for publisering.

```js
images[name] = `data:image/${ext};base64,${bytes.toString('base64')}`;
const data = `window.DUCK_B64="${duck}";window.TEX=${JSON.stringify(images)};`;
```

## Fallgruver

- En artifact kan være høyst 16 MB. I DoD-Roguelite tok teksturene 3,8 MB og hele fila 6,9 MB.
- base64 gjør filene en tredjedel større. Komprimer bildene først (JPEG 76 til 80).
- Skrifter fra Google Fonts kommer ikke med offline. Se kortet skrifter-med-fontface.
- Fra three.js r171 er `three.module.js` delt i flere filer, og da må importmapen endres.

## Slik verifiseres det

Publiser `artifact.html` og åpne den. Konsollen skal være fri for nettverksfeil, og teksturene skal vises.

## Bevis

- [Loggen, artifact versjon 8 publisert 9. oktober 00:53](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/log.md?plain=1#L274).
- [memory.md, tekniske beslutninger](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/memory.md?plain=1#L25).

## Brukt i

- `Tombonator3000/DoD-Roguelite@5e940d2`: alle utgavene fra 0.2 til 0.7, både som artifact og på GitHub Pages.

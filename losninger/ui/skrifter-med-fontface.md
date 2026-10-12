---
id: skrifter-med-fontface
tittel: Skrifter som virker offline og i en streng CSP
domene: ui
stikkord: skrift, font, FontFace, woff2, base64, offline, CSP, font-src, data-URI, Google Fonts, artifact
stack: Nettleser, FontFace API, én HTML-fil
status: UNVERIFIED
opphav: Tombonator3000/SIGNAL-47@925d61336e95abb9310646be0e0de77271ad0f4a:web/src/core/fonts.ts#L6
dato: 2026-10-09
agent: Claude
lisens: Toms egen kode, ingen lisensfil i repoet
sist_sjekket: 2026-10-09
---

# Skrifter som virker offline og i en streng CSP

## Symptom

Spillet får systemskrift uten nett eller i en sandkasse, fordi skriftene hentes fra Google Fonts. Eller en CSP nekter `data:`-adresser i `@font-face`.

## Årsak

Skrift fra et CDN krever nett. En CSP med `font-src` kan stoppe `data:`-adresser. Den gjelder ikke skrifter som lages fra en ArrayBuffer.

## Løsning

Bygg woff2-filene inn som base64, gjør dem om til ArrayBuffer, og registrer dem med FontFace:

```js
const face = new FontFace(family, arrayBuffer, { weight: '700' });
document.fonts.add(await face.load());
```

## Fallgruver

- Sjekk at skriften har ÆØÅ og ÅÄÖ før du velger den. SIGNAL-47 fant en skrift uten.
- Ta bare med de delene av tegnsettet du trenger (latin og latin-ext). Det holder størrelsen nede.
- Krediter skriftene og lisensen (ofte OFL) i prosjektets kildeliste.

## Slik verifiseres det

Åpne bygget uten nett, og sjekk at `document.fonts` har skriftene med status `loaded`. SIGNAL-47 har også en CSP-test, `web/tools/csptest.py`.

## Bevis

- Koden er lest, men testen er ikke kjørt her: [fonts.ts i SIGNAL-47](https://github.com/Tombonator3000/SIGNAL-47/blob/925d61336e95abb9310646be0e0de77271ad0f4a/web/src/core/fonts.ts#L6).

## Brukt i

- `Tombonator3000/SIGNAL-47@925d613`: alle skriftene i nettutgaven.

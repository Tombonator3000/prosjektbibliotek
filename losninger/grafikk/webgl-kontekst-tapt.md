---
id: webgl-kontekst-tapt
tittel: Når WebGL-konteksten blir borte
domene: grafikk
stikkord: webglcontextlost, webglcontextrestored, context lost, kontekst, krasj, minne, GPU, svart skjerm, mobil, Chrome
stack: three.js r128 og nyere, WebGL
status: UNVERIFIED
opphav: Tombonator3000/morbidium@729219ceb3e77119179deadb9fbfcd25bd8b2a4a:src/04_render.js#L57
dato: 2026-10-09
agent: Claude
lisens: Toms egen kode, ingen lisensfil i repoet
sist_sjekket: 2026-10-09
---

# Når WebGL-konteksten blir borte

## Symptom

Skjermen blir svart eller fryser, særlig på mobil eller etter lang spilling. Konsollen sier noe om at WebGL-konteksten er mistet (context lost).

## Årsak

Nettleseren tar fra siden skjermkortet når minnet er brukt opp eller driveren krasjer. Uten en handler venter spillet for alltid. Etter et krasj i skjermkortet stenger Chrome ofte WebGL for hele domenet til nettleseren startes på nytt.

## Løsning

```js
canvas.addEventListener('webglcontextlost', e => { e.preventDefault(); mistet(); });
canvas.addEventListener('webglcontextrestored', () => hentet());
```

- I `mistet()`: pause spillet, lagre det nødvendige og si fra til spilleren.
- Kommer konteksten ikke tilbake innen 8 s: vis en melding og lagre en lettere kvalitet til neste gang, så spillet ikke krasjer på samme sted.
- I `hentet()`: bygg nivået og teksturene på nytt.

## Fallgruver

- Uten `preventDefault()` kommer konteksten aldri tilbake.
- Ser du etter lekkasjer, sammenlign `renderer.info.memory` (teksturer og geometrier) før og etter at et nivå er bygd flere ganger.

## Slik verifiseres det

Bruk `WEBGL_lose_context`: `renderer.getContext().getExtension('WEBGL_lose_context').loseContext()`, og så `restoreContext()`. Spillet skal pause og komme tilbake.

## Bevis

- Koden er lest, men testen er ikke sett her: [04_render.js i Morbidium, linje 57 til 94](https://github.com/Tombonator3000/morbidium/blob/729219ceb3e77119179deadb9fbfcd25bd8b2a4a/src/04_render.js#L57).

## Brukt i

- `Tombonator3000/morbidium@729219c`: pause, melding og lettere kvalitet når konteksten blir borte.

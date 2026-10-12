---
id: three-r170-composer-msaa
tittel: Kantutjevning når three.js tegner gjennom EffectComposer
domene: grafikk
stikkord: three.js, r170, WebGL2, MSAA, antialias, EffectComposer, kantutjevning, hakkete kanter, aliasing, samples, HalfFloat
stack: three.js r170, WebGL2, EffectComposer med RenderPass, UnrealBloomPass og OutputPass
status: PASS
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:src/main.js#L231
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# Kantutjevning når three.js tegner gjennom EffectComposer

## Symptom

Kantene hakker selv om rendereren er laget med `antialias: true`. Det gjelder alt som går gjennom EffectComposer: bygninger, trær, figurer og skyggekanter.

## Årsak

EffectComposer i r170 lager sin egen target uten MSAA: `new WebGLRenderTarget(w * pr, h * pr, { type: HalfFloatType })` (examples/jsm/postprocessing/EffectComposer.js, linje 27). Scenen tegnes dit og ikke til lerretet. `antialias` på rendereren gjelder bare lerretet, og der tegnes det bare en flate med det ferdige bildet.

## Løsning

Gi komposeren en target med `samples`, og ta `antialias` av rendereren, siden den bare koster minne:

```js
const renderer = new THREE.WebGLRenderer({ antialias: false });
const composer = new EffectComposer(renderer,
  new THREE.WebGLRenderTarget(innerWidth, innerHeight, { type: THREE.HalfFloatType, samples: 4 }));

// etter kvalitet: 4 på høy, 2 på middels, 0 på lav
for (const rt of [composer.renderTarget1, composer.renderTarget2]) {
  if (rt.samples !== n) { rt.samples = n; rt.dispose(); }
}
```

## Fallgruver

- Komposeren kloner targeten, så begge bufferne får MSAA, og hvert pass etter scenen løses opp på nytt. Vil du spare det, gir du MSAA bare til et eget RenderPass og kopierer over.
- Endrer du `samples` på en target som er i bruk, må du kalle `dispose()`, ellers bygges den ikke på nytt.
- HalfFloat med MSAA krever at skjermkortet kan tegne til halvflyt (EXT_color_buffer_half_float), akkurat som komposeren uten MSAA.
- Ting med alphaTest (gresstuster, faner) får ikke glatte kanter av MSAA alene. Det krever `alphaToCoverage: true` på materialet.

## Slik verifiseres det

- `G.composer.renderTarget1.samples` er 4 på høy kvalitet.
- Ta et bilde av den samme scenen før og etter i testriggen, og se på skrå kanter. De skal være glatte.

## Bevis

- [Loggen i DoD-Roguelite, 9. oktober 00:22](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/log.md?plain=1#L262) og [bildene før og etter, 00:29](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/log.md?plain=1#L266).
- [EffectComposer.js i r170, linje 27](https://github.com/mrdoob/three.js/blob/r170/examples/jsm/postprocessing/EffectComposer.js#L27).

## Brukt i

- `Tombonator3000/DoD-Roguelite@7e5ba8e`: kantutjevning på høy og middels kvalitet. Bildene var glatte, og CI-testene var grønne.

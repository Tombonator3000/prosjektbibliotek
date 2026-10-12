---
id: onbeforecompile-i-kjede
tittel: Flere shaderendringer på samme materiale med onBeforeCompile
domene: grafikk
stikkord: onBeforeCompile, customProgramCacheKey, shader, patch, MeshStandardMaterial, overskrives, feil program, cutaway, wetness, sway
stack: three.js r170, MeshStandardMaterial med onBeforeCompile
status: PASS
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:src/wet.js#L27
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# Flere shaderendringer på samme materiale med onBeforeCompile

## Symptom

To endringer på samme materiale, for eksempel fuktighet og vind i trærne, virker ikke sammen: den siste overskriver den første. Eller to materialer med ulike endringer får det samme programmet.

## Årsak

`onBeforeCompile` er én funksjon per materiale. Setter du den på nytt, er den forrige borte. three.js gjenbruker også programmer med samme nøkkel, så uten `customProgramCacheKey` kan to ulike varianter dele ett program.

## Løsning

Kjed funksjonene og nøklene:

```js
function chain(mat, key, fn) {
  const prev = mat.onBeforeCompile;
  const prevKey = mat.customProgramCacheKey ? mat.customProgramCacheKey.bind(mat) : null;
  mat.onBeforeCompile = (sh, r) => { if (prev) prev.call(mat, sh, r); fn(sh); };
  mat.customProgramCacheKey = () => (prevKey ? prevKey() : '') + '|' + key;
}
```

Hver endring kaller `chain(mat, 'wet', sh => { ... })` med sin egen nøkkel.

## Fallgruver

- Endringer som erstatter den samme `#include`-linja, må tåle at en annen endring allerede har gjort det. Bygg videre på teksten som står der, ikke på den opprinnelige chunken.
- Uniformer som deles mellom materialer, legges i et felles objekt og settes inn i `sh.uniforms` i hver endring.

## Slik verifiseres det

Et materiale med både cutaway, fuktighet og vind skal vise alle tre, og et materiale med bare én skal ikke få de andre.

## Bevis

- [memory.md, wet.js](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/memory.md?plain=1#L68).
- [chain() i wet.js](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/wet.js#L27).

## Brukt i

- `Tombonator3000/DoD-Roguelite@5e940d2`: addWetness, addSway og addCutaway på de samme materialene i byen og områdene siden 0.5.

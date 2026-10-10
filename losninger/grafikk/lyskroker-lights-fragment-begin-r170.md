---
id: lyskroker-lights-fragment-begin-r170
tittel: Kroker for lys per lyskilde i lights_fragment_begin (r170)
domene: grafikk
stikkord: lights_fragment_begin, getSpotLightInfo, getDirectionalLightInfo, skyskygger, onBeforeCompile, ShaderChunk, directLight
stack: three.js r170, MeshStandardMaterial
status: UNVERIFIED
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:memory.md#L212
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# Kroker for lys per lyskilde i lights_fragment_begin (r170)

## Symptom

Du vil dempe eller farge lyset fra sola for alle materialer, for eksempel skygger fra skyer som bare treffer direkte lys og ikke fyllyset. Endringen må gjøres per lyskilde.

## Årsak

Det direkte lyset regnes i en løkke i `lights_fragment_begin`. Etter at lysinformasjonen er hentet og før den legges til, kan `directLight.color` endres.

## Løsning

Linjene i r170 som det går an å henge noe på:

```glsl
getSpotLightInfo( spotLight, geometryPosition, directLight );
getDirectionalLightInfo( directionalLight, directLight );
```

Legg til for eksempel `directLight.color *= cloudShadowAt( worldPos );` rett etter, med `.replace()` i onBeforeCompile eller på `THREE.ShaderChunk.lights_fragment_begin` før noe kompileres.

## Fallgruver

- Linjene skifter mellom versjonene. Sjekk dem i `node_modules/three/src/renderers/shaders/ShaderChunk/lights_fragment_begin.glsl.js` for den versjonen du bruker.
- Verdensposisjonen må sendes fra vertex-shaderen. `geometryPosition` ligger i kamerarommet.

## Slik verifiseres det

Sett en tydelig demping, for eksempel halv styrke, og se at bare sollyset blir svakere, ikke fyllyset.

## Bevis

- Strengene er sjekket i r170 (`lights_fragment_begin.glsl.js` linje 97 og 141), men kroken er ikke tatt i bruk ennå. [memory.md](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/memory.md?plain=1#L212).

## Brukt i

- `Tombonator3000/DoD-Roguelite@5e940d2`: notert til skyskygger. Ikke tatt i bruk.

---
id: uniformlister-for-forste-render
tittel: Uniformlister må ha verdier før første render
domene: grafikk
stikkord: uniform, array, uniformliste, ShaderMaterial, krasj, første render, vec4, Vector4, delte uniformer
stack: three.js r170, ShaderMaterial med lister som uniform vec4 uRip[8]
status: PASS
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:src/water.js#L102
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# Uniformlister må ha verdier før første render

## Symptom

Spillet krasjer i three.js ved første render av et materiale med en uniformliste, for eksempel `uniform vec4 uRip[8];` for ringer i vannet.

## Årsak

three.js leser lengden og verdiene i lista når programmet bindes. Er lista tom eller ikke fylt ennå, har den ingenting å laste opp.

## Løsning

Lag listene med full lengde og nøytrale verdier når modulen lastes, og del de samme listene mellom alle materialene:

```js
const SHARED = {
  rip: Array.from({ length: NRIP }, () => new THREE.Vector4(0, 0, -99, 0)),
  lp: Array.from({ length: NL }, () => new THREE.Vector3(0, -99, 0)),
  lc: Array.from({ length: NL }, () => new THREE.Color(0, 0, 0)),
};
uniforms: { uRip: { value: SHARED.rip }, uLP: { value: SHARED.lp }, uLC: { value: SHARED.lc } }
```

Oppdater objektene i lista, ikke bytt ut lista.

## Fallgruver

- Lengden i GLSL (`[NRIP]`) og i JS må være like.
- En nøytral verdi må være ufarlig i shaderen. Her betyr z = -99 at ringen ikke finnes.

## Slik verifiseres det

Last et nivå med vann uten at noe har laget ringer ennå. Konsollen skal være fri for feil.

## Bevis

- [memory.md i DoD-Roguelite, avsnittet om water.js](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/memory.md?plain=1#L64).
- [Listene i water.js](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/water.js#L102).

## Brukt i

- `Tombonator3000/DoD-Roguelite@5e940d2`: vann i byen, i områdene og i kloakken siden 0.5.

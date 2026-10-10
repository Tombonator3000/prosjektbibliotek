---
id: regnstreker-fast-pikselbredde
tittel: Regnstreker med fast bredde i piksler
domene: grafikk
stikkord: regn, regnstreker, dråper, partikler, skjermrom, bredde, enorme, forsvinner, DoubleSide, billboard
stack: three.js r170, ShaderMaterial, instanserte flater bygget i skjermrommet
status: PASS
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:src/weather.js#L103
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# Regnstreker med fast bredde i piksler

## Symptom

De nærmeste regndråpene blir enorme streker over skjermen, eller strekene forsvinner fra noen vinkler.

## Årsak

En strek med bredde i verdensmeter blir bred når den er nær kameraet. Når flaten bygges i skjermrommet, kan den dessuten snus, og da skjuler bakflate-kulling den.

## Løsning

Bygg streken i klipprommet og gi den en fast bredde i piksler, ganget med `w` så den ikke krymper med avstanden. Bruk `DoubleSide`.

```glsl
c.xy += perp * position.x * uPx * c.w;   // uPx er bredden i klipprom-enheter
```

```js
new THREE.ShaderMaterial({ side: THREE.DoubleSide, uniforms: { uPx: { value: 0.002 } } });
```

## Fallgruver

- `uPx` må regnes på nytt når oppløsningen eller pikselforholdet endrer seg.
- Strekker du partikler langs farten, trenger tangenten formen `vec2(d.y, -d.x)`, ellers blir de borte.

## Slik verifiseres det

Bilde i regn med kameraet nær bakken. Strekene skal være like tynne nær og langt unna.

## Bevis

- [memory.md, regnstrekene](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/memory.md?plain=1#L66).
- [Vertex-shaderen i weather.js](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/weather.js#L103).

## Brukt i

- `Tombonator3000/DoD-Roguelite@5e940d2`: regn og storm i byen og områdene siden 0.5.

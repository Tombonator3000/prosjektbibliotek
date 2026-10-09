---
id: bloom-terskel-over-en
tittel: Bloom som bare gløder på lys og ild
domene: grafikk
stikkord: bloom, UnrealBloomPass, threshold, terskel, HDR, emissive, grøtete, gløder, overeksponert, dis
stack: three.js r170, UnrealBloomPass før OutputPass, ACES-tonekurve
status: PASS
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:src/main.js#L1191
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# Bloom som bare gløder på lys og ild

## Symptom

Lyse flater gløder midt på dagen: hvite vegger, markiser og sollys på brostein får en hvit dis rundt seg, og bildet ser grøtete ut.

## Årsak

UnrealBloomPass sto med terskel 0,78 og styrke 0,65. Passet ligger før OutputPass, så det ser HDR-verdiene før tonekurven. Sollyse flater med lys farge kommer over 0,78, og da gløder alt som er lyst, ikke bare lyskildene.

## Løsning

- Sett terskelen over 1, så bare det som er lysere enn hvitt i HDR gløder.
- Gi lamper, ild, vinduer om natta og magi emissive over 1, så de fortsatt gløder.
- La terskelen og styrken følge stedet og tiden:

| Sted | Terskel | Styrke |
| --- | --- | --- |
| Ute om dagen | 1,12 | 0,32 |
| Ute om natta | 0,98 | 0,52 |
| Kloakk og hule | 0,88 | 0,55 |

```js
bloomLook(threshold, strength) { this.bloom.threshold = threshold; this.bloom.strength = strength; }
// ute, n = natt fra 0 til 1
this.bloomLook(1.12 - n * 0.14, 0.32 + n * 0.2);
```

## Fallgruver

- Lamper med lav emissive (under 1) slutter å gløde. Sjekk at `emissiveIntensity` ganger fargen kommer over 1 der det skal gløde.
- `Math.pow` av et negativt tall gir NaN, som blir en hvit klatt i bloom. Klem verdiene før du opphøyer.

## Slik verifiseres det

Ta det samme bildet midt på dagen og om natta. Om dagen skal hvite flater være skarpe, og om natta skal lamper og vinduer fortsatt gløde.

## Bevis

- [Loggen, 9. oktober 00:23](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/log.md?plain=1#L263) og [bildene før og etter, 00:29](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/log.md?plain=1#L266): markisen på torget gløder ikke lenger midt på dagen.

## Brukt i

- `Tombonator3000/DoD-Roguelite@7e5ba8e`: by, områder, kloakk og tittel har hver sin terskel og styrke.

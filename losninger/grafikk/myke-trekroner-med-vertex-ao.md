---
id: myke-trekroner-med-vertex-ao
tittel: Myke trekroner med AO i hjørnefargene
domene: grafikk
stikkord: trær, trekroner, low poly, flatShading, plast, facetter, ikosaeder, vertexColors, AO, InstancedMesh, mergeVertices
stack: three.js r170, InstancedMesh med setColorAt, BufferGeometryUtils.mergeVertices
status: PASS
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:src/treegeo.js#L29
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# Myke trekroner med AO i hjørnefargene

## Symptom

Trærne ser ut som facetterte plastkuler og kjegler i én farge.

## Årsak

Kronene var ikosaedre og kjegler med `flatShading`. Hver flate fikk sin egen normal, og fargen var lik overalt.

## Løsning

- Slå sammen hjørnene med `mergeVertices`, og forskyv dem med støy som bare avhenger av posisjonen. Da flytter like hjørner seg likt, og det blir ingen sprekker.
- Regn normalene på nytt, og vri dem 55 prosent mot retningen ut fra midten, så lyset faller mykt over kronen.
- Legg AO i en fargeattributt: mørkere nederst og i gropene, lysere øverst, og litt flekker. Med `vertexColors: true` ganges den med fargen per instans.
- Graner: kjegler med takket nederkant og mørk underside.

```js
nn.fromBufferAttribute(nrm, i).lerp(dirFromCenter, 0.55).normalize();
const ao = (0.5 + 0.62 * smoothstep(-0.95, 0.75, y)) * (0.82 + 0.18 * smoothstep(0.88, 1.12, lump)) * mottling;
```

## Fallgruver

- `vertexColors: true` krever en fargeattributt på hver geometri som bruker materialet. Uten den blir alt svart (se kortet vertexcolors-uten-fargeattributt).
- Detail 2 gir 320 flater per kule mot 80. I Ekeskogen ble det 524 000 trekanter på høy kvalitet mot 239 000 før. Hvor fine kronene er, bør derfor følge kvaliteten.

## Slik verifiseres det

Bilde av skogen før og etter, og `renderer.info.render.triangles` på høy og lav kvalitet.

## Bevis

- [Loggen, 9. oktober 00:26](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/log.md?plain=1#L265) og [bildene og trekantene, 00:29](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/log.md?plain=1#L266).

## Brukt i

- `Tombonator3000/DoD-Roguelite@7e5ba8e`: alle løvtrær og graner i områdene og rundt Fristaden. På lav kvalitet er trekantene som før.

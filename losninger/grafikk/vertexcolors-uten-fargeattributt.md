---
id: vertexcolors-uten-fargeattributt
tittel: vertexColors uten fargeattributt blir svart
domene: grafikk
stikkord: vertexColors, color, attributt, svart, black, geometri, materiale, instanceColor
stack: three.js r170, WebGL2, MeshStandardMaterial med vertexColors
status: UNVERIFIED
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:src/treegeo.js#L29
se_ogsa: myke-trekroner-med-vertex-ao
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# vertexColors uten fargeattributt blir svart

## Symptom

Et materiale med `vertexColors: true` blir svart på noen meshes, men ikke på andre.

## Årsak

Shaderen ganger fargen med attributten `color`. Har geometrien ingen `color`, bruker WebGL standardverdien for en attributt som ikke er satt, som er (0, 0, 0, 1). Fargen blir da ganget med null.

## Løsning

- Gi hver geometri som deler materialet en fargeattributt, også om den bare er hvit.
- Eller lag et eget materiale uten `vertexColors` til geometrier uten farge.

```js
g.setAttribute('color', new THREE.BufferAttribute(new Float32Array(g.attributes.position.count * 3).fill(1), 3));
```

## Fallgruver

`setColorAt` på en InstancedMesh er noe annet. Den fargen ganges med fargeattributten, så begge må finnes når begge er slått på (se kortet instancedmesh-fargeliste-ved-count-null).

## Slik verifiseres det

Sett `vertexColors: true` på et materiale, og gi det en geometri uten `color`. Den skal bli svart. Legg til attributten, og den skal få farge.

## Bevis

- Ikke gjenskapt i en test. Kortet bygger på hvordan WebGL behandler attributter som ikke er satt, og trekronene i DoD-Roguelite ble laget med fargeattributt på alle geometrier for å unngå det.

## Brukt i

- `Tombonator3000/DoD-Roguelite@7e5ba8e`: alle geometriene til MAT.leaf og M.spruce har fargeattributt.

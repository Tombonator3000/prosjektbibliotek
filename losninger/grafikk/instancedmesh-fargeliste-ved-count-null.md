---
id: instancedmesh-fargeliste-ved-count-null
tittel: InstancedMesh blir svart når fargelista lages mens count er 0
domene: grafikk
stikkord: InstancedMesh, setColorAt, instanceColor, count, svart, partikler, farge, black
stack: three.js r128 og nyere, InstancedMesh
status: UNVERIFIED
opphav: Tombonator3000/morbidium@729219ceb3e77119179deadb9fbfcd25bd8b2a4a:logg/2026-09.md#L1092
se_ogsa: vertexcolors-uten-fargeattributt
dato: 2026-10-09
agent: Claude
lisens: Toms egen kode, ingen lisensfil i repoet
sist_sjekket: 2026-10-09
---

# InstancedMesh blir svart når fargelista lages mens count er 0

## Symptom

Alle instansene i en InstancedMesh, for eksempel partikler, blir svarte, selv om `setColorAt` blir kalt.

## Årsak

`setColorAt` lager fargelista (`instanceColor`) første gang den kalles, med plass til `count` instanser. Er `count` 0 i det øyeblikket, får lista lengde 0, og hver instans tegnes uten farge.

## Løsning

Lag fargelista for full kapasitet før du setter `count` ned, eller lag den selv:

```js
mesh.instanceColor = new THREE.InstancedBufferAttribute(new Float32Array(capacity * 3), 3);
```

## Fallgruver

Det samme gjelder alle steder som lager partikler. Morbidium hadde feilen på 44 steder samtidig.

## Slik verifiseres det

Lag en InstancedMesh, sett `count = 0`, kall `setColorAt`, og øk `count`. Instansene skal ha farge etter rettelsen.

## Bevis

- Årsaken og rettelsen står i loggen til Morbidium, men testen er ikke sett her: [logg/2026-09.md, linje 1092 til 1095](https://github.com/Tombonator3000/morbidium/blob/729219ceb3e77119179deadb9fbfcd25bd8b2a4a/logg/2026-09.md?plain=1#L1092).

## Brukt i

- `Tombonator3000/morbidium@729219c`: partiklene fikk farge da fargelista ble laget for alle plassene.

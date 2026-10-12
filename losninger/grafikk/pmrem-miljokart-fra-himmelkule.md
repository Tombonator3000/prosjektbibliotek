---
id: pmrem-miljokart-fra-himmelkule
tittel: Miljøkart fra en enkel himmelkule
domene: grafikk
stikkord: PMREM, PMREMGenerator, environment, environmentIntensity, miljøkart, refleksjoner, glans, matt, plast, MeshStandardMaterial
stack: three.js r170, MeshStandardMaterial, scene.environment og scene.environmentIntensity
status: PASS
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:src/envlight.js#L58
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# Miljøkart fra en enkel himmelkule

## Symptom

MeshStandardMaterial ser matt og plastaktig ut. Våt stein, metall og rustning blinker ikke, fordi det ikke finnes noe miljø å speile.

## Årsak

Uten `scene.environment` får standardmaterialene ingen refleksjoner fra omgivelsene, bare høylys fra lyskildene.

## Løsning

- Lag en kule med farger fra himmelen: toppen, horisonten og bakken, pluss en myk solflekk i samme retning som sola.
- Gjør den om til PMREM, og sett den som `scene.environment`.
- Hold styrken lav, så sola og fyllyset fortsatt bærer bildet: rundt 0,3 om dagen og 0,08 om natta. Bruk ikke noe miljøkart i mørke kjellere og huler.
- Bygg kartet på nytt bare når himmelen har endret seg merkbart, og høyst hvert sjette sekund.

```js
const pmrem = new THREE.PMREMGenerator(renderer);
// scene: en BackSide-kule med ShaderMaterial som blander uTop, uHorizon og uGround etter retningen
const rt = pmrem.fromScene(skyScene, 0.03, 0.1, 50);
scene.environment = rt.texture;
scene.environmentIntensity = (0.3 - night * 0.22) * (1 - cloud * 0.35);
```

## Fallgruver

- Miljøkartet gir både glans og diffust lys. Står det for høyt, flater det ut lyset og gjør mørke steder grå.
- `fromScene` tegner seks sider og glatter dem ut, og det tar noen millisekunder. Hvor lang tid det tar på mobil, er ikke målt.
- Kast det gamle kartet med `dispose()` når du lager et nytt.

## Slik verifiseres det

Bilde av våt brostein om natta ved en lampe, og av metall i dagslys. Begge skal ha glans. I kjelleren skal `scene.environment` være `null`.

## Bevis

- [Loggen, 9. oktober 00:24](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/log.md?plain=1#L264) og [bildene før og etter, 00:29](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/log.md?plain=1#L266).

## Brukt i

- `Tombonator3000/DoD-Roguelite@7e5ba8e`: by og områder om dagen og natta, ikke i kloakken.

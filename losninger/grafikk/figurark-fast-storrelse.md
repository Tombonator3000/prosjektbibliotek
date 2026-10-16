---
id: figurark-fast-storrelse
tittel: Figurer fra KI-tegnede ark skifter størrelse mellom rutene
domene: grafikk
stikkord: figurark, sprite sheet, spritesheet, ChatGPT, Codex, størrelse, skala, flimrer, hode for stort, myke figurer, myk.py, HD remake, ScummVM
stack: ScummVM med HD-patch (DigHD), Python-pipeline med numpy og Pillow, figurark 1536 x 1024 i glatt stil med ekte alfa
status: PASS
opphav: Tombonator3000/Dig-HD-Remake@091a953b89b522c6d45478315aecefa6dbab1d75:pipeline/dighd/myk.py#L236
dato: 2026-10-10
agent: Claude
lisens: Toms egen pipelinekode, ingen lisensfil i repoet (motorpatchen er GPL sammen med ScummVM)
sist_sjekket: 2026-10-13
se_ogsa: scumm-v6-kostymer-skygge-og-soppelruter
---

# Figurer fra KI-tegnede ark skifter størrelse mellom rutene

## Symptom

En HD-figur laget fra et figurark (ChatGPT/Codex) blir litt større, mindre, smalere eller bredere fra rute til rute, særlig når den snakker eller gestikulerer. Originalen er jevn. Hodene blir ofte tegnet omtrent 35 prosent for store.

## Årsak

Grafikeren tegner rutene på arket i litt ulik størrelse og form. Mottaket skalerte én faktor per gruppe (animasjon, lag, rad) til originalens høyde, så høyden stemte, men bredden fulgte tegningen: målt spredning i bredde opptil 7 prosent innen samme kostyme i The Dig. Grafikeren fikk heller ikke vite hvor stor hver rute skulle være, og kunne ikke sjekke det selv før levering.

## Løsning

1. Mottaket: tilpass hver rute til originalens omriss i bredde og høyde for seg, innenfor et lite spenn rundt gruppens faktor, og bruk det bare når overlappet med originalen ikke blir tydelig dårligere.

```python
def fit_scales(drawing, original, scale, rng=0.12, s=4):
    core = drawing[..., 3] >= 128
    ys, xs = np.nonzero(core); oy, ox = np.nonzero(original[..., 3] > 0)
    sx = (ox.max() - ox.min() + 1) * s / (xs.max() - xs.min() + 1)
    sy = (oy.max() - oy.min() + 1) * s / (ys.max() - ys.min() + 1)
    lo, hi = scale * (1 - rng), scale * (1 + rng)
    return min(hi, max(lo, sx)), min(hi, max(lo, sy))
# bruk (sx, sy) når snitt/union >= snitt/union med gruppens faktor - 0.03
```

2. Før levering (Sam & Max HD, 13. oktober): skriv målet på hver rute i 4x inn i prompten («rute 3: 280 x 288 px»), si at hoder, hender og øyne ikke gjøres større, og legg et frittstående kontrollskript i arbeidsgrenen som grafikeren kjører før commit. Skriptet finner omrisset i hver rute og sammenligner med originalen ganger 4: avvik over 6 prosent er advarsel, over 12 prosent feil, og spredning over 5 prosent innen samme ark er advarsel.

3. Mottaket måler hvor stort hver gruppe faktisk er tegnet mot 4x, og merker gruppen «sjekk» når den avviker mer enn 12 prosent fra medianen for arket (`myk.py` versjon 4 i Sam & Max HD).

## Fallgruver

- En rute der grafikeren har tegnet noe helt annet (en arm mangler) rettes ikke; den må fanges av kontrollen (snitt/union under 0,6).
- Spennet må holdes lite, ellers strekkes ansikter. Samme regel står i skillen morbidium-spritesheets: fast skala, fotfeste og hodestørrelse, ingen rute skalert for seg for å fylle boksen.
- Kontrollskriptet i arbeidsgrenen må bare trenge Python 3, numpy og Pillow, ellers blir det ikke kjørt.
- Ruter som er søppel i dataene (tusenvis av piksler brede) gir meningsløse mål; hold dem ute før målene skrives i prompten.

## Slik verifiseres det

Mål for hver rute HD-omrissets bredde og høyde delt på originalens ganger 4, og se på spredningen per kostyme. I The Dig: Brink i romdrakt fra 1,9 til 0,3 prosent spredning i bredde, Boston fra 7,2 til 5,9 prosent, snitt/union likt eller bedre. I Sam & Max HD: `python3 tools/sjekk_leveranse.py <ark>` gir OK for et riktig syntetisk ark og FEIL når én rute er 15 prosent for stor.

## Bevis

- Tombonator3000/Dig-HD-Remake@091a953b89b522c6d45478315aecefa6dbab1d75:log.md, pytest `test_soft_cel_keeps_original_size` og måling på 441 ruter.
- Tombonator3000/Sam-Max-HD@ef9c4414562aa73700e2bb9ec06355cebb1c6b42:pipeline/tests/test_pipeline.py, `test_soft_cel_size_spread` og `test_sjekk_leveranse_tool` (43 tester bestått 13. oktober, log.md samme dag).

## Brukt i

- `Tombonator3000/Dig-HD-Remake@091a953b89b522c6d45478315aecefa6dbab1d75`: mottaket av myke figurer, PR 44. UNVERIFIED på ekte skjerm.
- `Tombonator3000/Sam-Max-HD@ef9c4414562aa73700e2bb9ec06355cebb1c6b42`: `myk.py` versjon 3 portet og utvidet med størrelsesrapport, mål per rute i figurpromptene og `tools/sjekk_leveranse.py` i arbeidsgrenen. Ikke prøvd på ekte ChatGPT-leveranser ennå.

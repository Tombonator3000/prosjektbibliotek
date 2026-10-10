# Figurer fra KI-tegnede ark skifter størrelse mellom rutene

Symptom: en HD-figur laget fra et figurark (ChatGPT/Codex) blir litt større, mindre, smalere eller bredere fra rute til rute, særlig når den snakker eller gestikulerer. Originalen er jevn.

Kontekst: The Dig HD (Dig-HD-Remake), ScummVM med HD-patch, figurark i glatt stil med ekte alfa som tas inn av `dighd myke-figurer` (`pipeline/dighd/myk.py`). Gjelder alle spill der tegnede ark skal erstatte pikselruter med kjent originalomriss.

Årsak: grafikeren tegner rutene på arket i litt ulik størrelse og form. Mottaket skalerte én faktor per gruppe (animasjon, lag, rad) til originalens høyde, så høyden stemte, men bredden fulgte tegningen: målt spredning i bredde opptil 7 prosent innen samme kostyme.

Løsning: tilpass hver rute til originalens omriss i bredde og høyde for seg, innenfor et lite spenn rundt gruppens faktor, og bruk det bare når overlappet med originalen ikke blir tydelig dårligere.

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

Fallgruver: en rute der grafikeren har tegnet noe helt annet (en arm mangler) rettes ikke; den må fanges av kontrollen (snitt/union under 0,6). Spennet må holdes lite, ellers strekkes ansikter. Samme regel står i skillen morbidium-spritesheets: fast skala, fotfeste og hodestørrelse, ingen rute skalert for seg for å fylle boksen.

Slik verifiseres det: mål for hver rute HD-omrissets bredde og høyde delt på originalens ganger 4, og se på spredningen per kostyme. I The Dig: Brink i romdrakt fra 1,9 til 0,3 prosent spredning i bredde, Boston fra 7,2 til 5,9 prosent, snitt/union likt eller bedre.

Status: PASS for mottaket (pytest `test_soft_cel_keeps_original_size`, måling på 441 ruter). UNVERIFIED på ekte skjerm.

Opphav: Tombonator3000/Dig-HD-Remake, PR 44, `pipeline/dighd/myk.py` (`fit_scales`, `place_fitted`), 10. oktober 2026, Claude.

Lisens: koden i Dig-HD-Remake (GPL sammen med ScummVM-patchen; pipeline-koden er Toms egen).

Brukt i: Dig-HD-Remake, PR 44.

Sist sjekket: 2026-10-10.

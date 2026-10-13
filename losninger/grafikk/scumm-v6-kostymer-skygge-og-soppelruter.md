---
id: scumm-v6-kostymer-skygge-og-soppelruter
tittel: Magenta skygger og kjempestore ruter i SCUMM v6-kostymer
domene: grafikk
stikkord: SCUMM, Sam & Max, COST, klassiske kostymer, magenta, rosa, skygge, shadow table, palettindeks 13, søppelruter, garbage cels, speilvending, figurark, ScummVM
stack: SCUMM v5 og nyere, testet i v6 (Sam & Max Hit the Road), ScummVM c9091321, egne Python-dekodere for COST (format 0x58 til 0x61)
status: PASS
opphav: Tombonator3000/Sam-Max-HD@ef9c4414562aa73700e2bb9ec06355cebb1c6b42:pipeline/smhd/figur.py#L306
dato: 2026-10-13
agent: Claude
lisens: Toms egen pipelinekode, ingen lisensfil i repoet (motorpatchen er GPL sammen med ScummVM)
sist_sjekket: 2026-10-13
offentlig_kontrollert: 2026-10-13
se_ogsa: figurark-fast-storrelse
---

# Magenta skygger og kjempestore ruter i SCUMM v6-kostymer

## Symptom

Når kostymerutene trekkes ut som RGBA-bilder, får noen figurer magenta eller rosa felt (255, 87, 255) under seg eller rundt seg, og noen kostymer er bare en magenta flekk. Noen få ruter er flere tusen piksler brede eller høye og ser ut som støy. Figurarkene til en KI-grafiker får da magenta former og ruter som ikke går an å tegne.

## Årsak

- Skygge: i klassiske kostymer tegnes palettindeks 13 gjennom skyggetabellen, ikke som farge. ScummVM `base-costume.cpp`: `if (pcolor == 13 && _shadowTable) pcolor = _shadowTable[*dst];`. Pikselen mørkner det som allerede står på skjermen. Tolket som farge blir den magenta. I Sam & Max er kostyme 127, 132, 153, 211 og 280 bare skygge.
- Søppelruter: noen animasjoner peker på rutekoder utenfor kostymet. Motoren leser dem bare om et skript ber om det, men en dekoder som tar ut alle ruter animasjonene nevner, leser tilfeldige bytes som en rute (i Sam & Max seks ruter, 4163 til 6189 px).
- Speilvending: rutene mot venstre finnes ikke. `ClassicCostumeRenderer` tegner rutene mot høyre speilvendt når kostymet ikke har eget speilflagg (`_drawActorToRight` i `costume.cpp`).

## Løsning

Les indeksbildet (`_idx.png`) ved siden av RGBA-bildet og fjern skyggepikslene før ruten går på arket; hopp over kostymer som da blir tomme. Sett en øvre grense for rutestørrelse (ekte ruter er høyst 320 x 200):

```python
SHADOW_INDEX = 13
MAX_CEL = (640, 400)

def cel_rgba(extract, name):
    im = np.array(Image.open(extract / "costumes" / f"{name}.png").convert("RGBA"))
    idx = np.array(Image.open(extract / "costumes" / f"{name}_idx.png"))
    im[idx == SHADOW_INDEX, 3] = 0          # skyggen lages av motoren, ikke av grafikeren
    return im if im[..., 3].any() else None

def valid_cel(c):
    return 0 < c["w"] <= MAX_CEL[0] and 0 < c["h"] <= MAX_CEL[1]
```

Be ikke grafikeren tegne ruter mot venstre; si i prompten at spillet speilvender.

## Fallgruver

- Skyggeregelen gjelder bare SCUMM v5 og nyere. ScummVM setter `_shadowTable` i `actor.cpp` bare når `_game.version >= 5`; ellers er den null, og indeks 13 tegnes som vanlig farge. I Zak McKracken FM-Towns (v3) bruker kostyme 8 indeks 13 som farge, så pikslene skal ikke fjernes der (målt 2026-10-13).
- Ikke tolk magenta som maske ut fra RGB alene: indeks 13 kan ha en annen farge i andre rom. Bruk indeksbildet, og RGB-regelen bare som reserve.
- Noen kostymer har både skygge og en ekte form (i Sam & Max 95 og 194, en hvit og en svart form); de skal fortsatt ha ark.
- Bare palettindeks 0 til 15 er like i alle rom. Kostymefargene må tas fra paletten i rommet der kostymet faktisk vises (finn det i de dekompilerte skriptene), ellers blir for eksempel Sams skjorte oransje.
- Kroppen er oftest lag 1 i v6 (lag 0 i The Dig), og en animasjon endrer bare sine egne lag. Et sammensatt bilde av en figur må starte med startanimasjonen, ellers mangler hodet.

## Slik verifiseres det

`pytest -k "shadow_pixels or palette_table"` i Sam-Max-HD: skyggepiksler forsvinner fra arket, en 400 x 60-rute godtas og en på 6000 px stoppes. Mot spillfilene: `smhd gpt-pakke --figurer alle` gir 1758 figurark fra 343 kostymer, uten ark for de fem skyggekostymene. Sett i motoren: rom 92 viser figurene i samme farger som uttrekket.

## Bevis

- Tombonator3000/Sam-Max-HD@ef9c4414562aa73700e2bb9ec06355cebb1c6b42:pipeline/tests/test_pipeline.py, `test_figure_shadow_pixels_and_invalid_cels` og `test_costume_palette_table_real_game`, 43 tester bestått 13. oktober (log.md samme dag).
- Tombonator3000/Sam-Max-HD@ef9c4414562aa73700e2bb9ec06355cebb1c6b42:docs/ANALYSE.md, avsnitt 11 med tellingene og motorkjøringen i rom 92.

## Brukt i

- `Tombonator3000/Sam-Max-HD@ef9c4414562aa73700e2bb9ec06355cebb1c6b42`: figurarkene til ChatGPT (fig-jobbene) og hovedarkene for Sam og Max. Ikke sett med ekte HD-leveranser ennå.

---
id: logg-over-det-som-mangler-hd
tittel: Hvilke figurruter og objekter mangler faktisk HD når spillet spilles
domene: testing
stikkord: mangler HD, uten HD, gult felt, originalpiksler, figurruter, kostymeruter, objekter, filmer, dighd-uten-hd.txt, spilltest, prioritering, ScummVM, HD remake
stack: ScummVM med HD-patch (DigHD) for SCUMM v7, C++11, motoren bygger HD-bildet per piksel fra kilder (rom, objekt, rute, film)
status: PASS
opphav: Tombonator3000/Dig-HD-Remake@6221c6eecd0ca3071c5b5adfdd1b48c115ee7c0f:engine/patches/0001-dighd-hd-grafikk.patch#L4509
dato: 2026-10-15
agent: Claude
lisens: Motorpatchen er GPL-3.0 sammen med ScummVM; pipelinen er Toms egen kode uten lisensfil
sist_sjekket: 2026-10-15
offentlig_kontrollert: 2026-10-15
se_ogsa: publisert-mod-er-fasit, figurark-fast-storrelse
---

# Hvilke figurruter og objekter mangler faktisk HD når spillet spilles

## Symptom

Tellinger fra spillfilene sier at tusenvis av figurruter mangler HD (10 158 i The Dig), men ikke hvilke som vises. Å bestille alt koster mye, og en gjennomspilling uten funn sier ikke hva som mangler. Gult felt (Ctrl+Shift+H) viser hullene bare mens noen ser på.

## Årsak

Kostymedataene har ruter som aldri vises: animasjoner skriptene ikke bruker, tekniske ruter og skyggemerker. Eksporten av animasjoner lister ruter som kan nås, ikke det som faktisk spilles. Bare motoren vet hva som står på skjermen.

## Løsning

Der motoren bestemmer at en piksel blir originalpiksel fordi HD mangler, lagres hvem den tilhører, og én gang per bilde telles det som står på skjermen:

1. Per skjermpiksel en eier: `kMissCel | kostyme << 12 | rute`, `kMissObject | objekt << 8 | tilstand`, `kMissRoom | rom` eller `kMissFilm | film`, ellers 0. Sett den samme sted som kilden for pikselen (`blitVirtScreen()`, `blitSmush()`), og nullstill den overalt ellers kilden settes (`blit8()`, `moveScreen()`, romskifte).
2. Før hver skjermoppdatering: tell eierne på skjermen, hopp over svarte piksler med gjeldende palett, og legg tallene i en tabell per bilde og rom: hvor mange bilder det sto der og flest piksler i ett bilde.
3. Skriv tabellen som tekst (tabulator) i lagringsmappen hvert 20. sekund og ved avslutning, og les den inn ved start, så flere kvelder blir én liste.
4. Et lite skript samler rutene per kostyme og sorterer etter hvor mye de ble vist.

```cpp
for (uint i = 0; i < _missOwner.size(); i++) {
	uint32 o = _missOwner[i];
	if (o) {
		const byte *c = _pal + _shadow[i] * 3;
		if (!(c[0] | c[1] | c[2]))
			o = 0;  // svart ser likt ut i HD
	}
	if (o == runOwner) { run++; continue; }
	if (runOwner) _missCount[runOwner] += run;
	runOwner = o; run = 1;
}
```

## Fallgruver

- Tell det som står på skjermen, ikke det som tegnes på nytt. Første utkast talte pikslene i de skitne områdene, og tavla i rom 28 fikk 8 320 piksler i stedet for 63 906.
- Svarte flater og tilstanden uten rom (rom 0, før spillet og mellom filmer) gir falske linjer.
- Sjekk svart når det telles, ikke når pikselen tegnes: en fade bygger skjermen på nytt uten å tegne pikslene.
- Et testhopp til et rom setter ingen figurer der. Bruk en testkrok som setter inn en skuespiller med kostymet for å prøve rutetellingen.
- I klassisk grafikk telles ingenting; det som vises da, er originalt med vilje.
- Lagringsmappen i nettleseren er ikke lett å hente filer fra, så lista er mest nyttig fra pakken på PC.

## Slik verifiseres det

Kjør uten skjerm med en mod uten figurer og objekter og en testskuespiller: ruter og objekter skal komme i fila. Med den ekte modden skal de samme stedene ikke gi noe. Kontrollen mot full nytegning (`DIGHD_VERIFY=1`) skal være uten avvik, og CPU-tiden lik som før.

## Bevis

- Tombonator3000/Dig-HD-Remake@6221c6eecd0ca3071c5b5adfdd1b48c115ee7c0f:docs/HD-MOTOR.md?plain=1#L217, avsnittet om lista med testene 15. oktober: 31 Boston-ruter og tavla `obj241_01` med en mod uten figurer og objekter, ingenting med r12-modden, 34 av 34 kontroller uten avvik, 10,3 til 10,6 sekunder CPU før og etter.
- Tombonator3000/Dig-HD-Remake@6221c6eecd0ca3071c5b5adfdd1b48c115ee7c0f:pipeline/tests/test_modflett.py, `test_missing_list_groups_cels_per_costume_and_sorts_by_exposure`.

## Brukt i

- `Tombonator3000/Dig-HD-Remake@6221c6eecd0ca3071c5b5adfdd1b48c115ee7c0f`: `dighd-uten-hd.txt` i lagringsmappen og `dighd mangler` (PR 52). Ikke testet på ekte skjerm, i nettleseren eller på Windows.

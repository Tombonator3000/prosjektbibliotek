---
id: publisert-mod-er-fasit
tittel: En ny bygging av HD-modden visker ut rettinger som bare finnes i den publiserte
domene: bygg
stikkord: hd-mod, mod, modpakke, fletting, flett, overstyringer, overrides, tvangspush, force push, sjekksummer, SHA256SUMS, regresjon, rettinger forsvinner, ScummVM, HD remake
stack: ScummVM med HD-patch (DigHD), Python-pipeline (dighd), modden i en egen git-gren med én commit som erstattes (hd-mod), flere agenter som leverer til samme mod
status: PASS
opphav: Tombonator3000/Dig-HD-Remake@b612c3151838b5b2e117b49343582b7577e107a4:pipeline/dighd/modflett.py#L115
dato: 2026-10-15
agent: Claude
lisens: Toms egen pipelinekode, ingen lisensfil i repoet (motorpatchen er GPL sammen med ScummVM)
sist_sjekket: 2026-10-15
se_ogsa: logg-over-det-som-mangler-hd, figurark-fast-storrelse
---

# En ny bygging av HD-modden visker ut rettinger som bare finnes i den publiserte

## Symptom

Etter en ny runde er rettinger borte fra den publiserte modden: figurer, lysfaser eller objekter som var rettet, vises som før igjen. Nettsiden og nattbygget av pakken henter modden fra grenen, så feilen går rett ut til spilleren. Ingen feilmelding; runden melder bare at modden er publisert.

## Årsak

Runden slettet modmappen, bygget modden på nytt fra arbeidsbordet og tvangspushet den som én commit. Den publiserte modden hadde rettinger som ikke kan bygges på nytt derfra: en annen agent (Codex) hadde lagt dem inn lokalt på en annen maskin, med egne manifester (r3 til r12 i The Dig HD, 4 635 filer bare i r12). Neste bygging fra null ville mistet dem, og grenen har ingen historikk å gå tilbake til.

## Løsning

Den publiserte modden er fasit. Runden bygger en kandidat som før, henter den publiserte og fletter:

1. Del filene i enheter: alle filene for samme bilde (`room022.png` og `room022_idx.png`; `costume014_003.png`, `_hd.png` og `_idx.png`).
2. En enhet som ikke er publisert, tas fra kandidaten. En publisert enhet med bare indeksbilde får kandidatens bilde, mens de publiserte filene står.
3. En publisert enhet byttes bare med `--erstatt MØNSTER` og tas ut bare med `--fjern MØNSTER`. Da byttes alle filene i enheten.
4. Runden noteres i `mod.json` (`runder`: hva som ble lagt til, erstattet og fjernet).
5. Publiseringen henter bare sjekksummene til den publiserte modden og stopper hvis filer forsvinner eller endres uten at enheten står som erstattet eller fjernet i siste runde. `--tving` bare når eieren vil erstatte hele modden.

```python
_UNIT = re.compile(r"^(rooms|objects|costumes)/(.+?)(_idx|_hd|_mask)?\.png$")

def unit_of(rel):
    m = _UNIT.match(rel)
    return f"{m.group(1)}/{m.group(2)}" if m else ("fonts" if rel.startswith("fonts/") else rel)

# vernet før push
removed = [r for r in pub if r not in new and unit_of(r) not in allowed]
changed = [r for r in pub if r in new and new[r] != pub[r] and unit_of(r) not in allowed]
ok = not (removed or changed) or force
```

Sjekksummene hentes uten bildene, i en egen tom git-mappe:

```sh
git -C "$tmp" init -q && git -C "$tmp" remote add origin "$url"
git -C "$tmp" fetch -q --depth 1 --filter=blob:none origin refs/heads/hd-mod
git -C "$tmp" cat-file -p FETCH_HEAD:SHA256SUMS > "$sums"
```

## Fallgruver

- Flett per enhet, ikke per fil. Motoren bruker `_hd.png` før den vanlige `.png`, så en gammel myk rute som blir liggende, vinner over en ny.
- Hent ikke sjekksummene med `--filter=blob:none` i arbeidskopien. Den blir da en delvis klone, og en senere `git archive` av grenen henter bildene ett og ett.
- Skriv README før sjekksummene lages. Ellers stemmer ikke `sha256sum -c` neste gang modden hentes.
- En avvist leveranse forsvinner ikke lenger av seg selv ved neste bygging; den må tas ut med `--fjern`.
- To git-kommandoer i samme repo samtidig gir `index.lock`-feil; hent spillfiler og mod etter hverandre.
- Vernet er mot uhell, ikke en sikkerhetsgrense: `mod.json` sier selv hva som kan endres.

## Slik verifiseres det

`cd pipeline && pytest tests/test_modflett.py`: ti tester, blant dem en som kjører `tools/mod_gren.sh` mot et lokalt git-repo (første publisering, en mod fra null som stoppes, en flettet som går gjennom). Mot den ekte modden: hent den publiserte, lag en kandidat med eldre og manglende filer, flett, og sammenlign sjekksummene. Alle publiserte filer skal stå, bare de nye skal komme til.

## Bevis

- Tombonator3000/Dig-HD-Remake@b612c3151838b5b2e117b49343582b7577e107a4:pipeline/tests/test_modflett.py, 49 tester bestått 15. oktober.
- Tombonator3000/Dig-HD-Remake@6221c6eecd0ca3071c5b5adfdd1b48c115ee7c0f:log.md, oppføringen 2026-10-15 00:35: mot `hd-mod` 05179ed lot en fletting med 13 nye filer alle 28 470 publiserte filer stå (25 sekunder for 1,2 GB), og sjekken stoppet en mod som manglet dem.

## Brukt i

- `Tombonator3000/Dig-HD-Remake@b612c3151838b5b2e117b49343582b7577e107a4`: `dighd flett-mod`, vernet i `tools/mod_gren.sh send` og runden i `tools/gpt_runde.sh` (PR 52). Ikke brukt i en ekte runde ennå.

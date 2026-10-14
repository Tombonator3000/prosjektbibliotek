# Logg

Arbeid i prosjektbiblioteket, nyeste nederst. Klokkeslett i norsk tid (Europe/Oslo). Skriv hvem du er hvis du ikke er Claude.

## 2026-10-09, løsningskort

- 04:39 Tom ba om løsningskort i prosjektbiblioteket, etter forslaget i DoD-Roguelite docs/gjenbruk.md: Toms egne løste problemer skal kunne finnes på tvers av spillene.
- 04:42 Leste AGENTS.md, docs/BRUK.md, docs/METODE.md og skriptene. verify.py var grønn før endringene (115 kildefiler, 341 lenker).
- 04:44 Prøvde å oppdatere det offentlige inventaret, så DoD-Roguelite (opprettet 8. oktober) kommer med. Proxyen i skyøkta gir 403 på users/Tombonator3000/starred, så inventaret er ikke oppdatert. Kortene fra DoD-Roguelite bruker derfor offentlig_kontrollert: 2026-10-09 (GitHub viser repoet som public).
- 04:46 La til scripts/build_solution_index.py (leser kortene og bygger data/losninger.json og LOSNINGER.md), en sjekk av kortene i verify.py (format, bevis ved PASS og FAIL, offentlig opphav, at oversikten er bygd), og kortene i find.py. find.py søker nå også i forbeholdene (caveats), så for eksempel BY-NC gir treff.
- 04:48 Skrev malen losninger/MAL.md og 19 kort: 15 fra DoD-Roguelite, 2 fra Morbidium og 2 fra SIGNAL-47. 14 er PASS og 5 UNVERIFIED.
- 04:49 Negativ kontroll i en kopi: et kort uten bevis, et med feil id og ugyldig status, og et med opphav i et privat repo ble alle stoppet av verify.py.
- 04:50 Beskrev kortene i README.md, docs/BRUK.md og AGENTS.md. Laget log.md, memory.md og todo.md.

## 2026-10-13, løsningskort fra Sam & Max HD

- 09:24 Under klargjøringen av grafikkjobbene i Sam-Max-HD: nytt kort `scumm-v6-kostymer-skygge-og-soppelruter` (palettindeks 13 er skygge i klassiske SCUMM-kostymer, søppelruter fra animasjoner utenfor kostymet, speilvending). Opphav Sam-Max-HD@ef9c441, PASS med pytest der.
- 09:24 Kortet `figurark-fast-storrelse` stoppet verify.py (manglet nøkkelblokken). Skrevet om etter MAL.md med opphav festet til Dig-HD-Remake@091a953b, og utvidet med det Sam & Max HD gjør før levering: mål per rute i prompten og et kontrollskript grafikeren kjører selv.
- 09:24 Begge repoene står ikke i det offentlige inventaret; offentlig_kontrollert 2026-10-13 (Sam-Max-HD: api private false, Dig-HD-Remake: README åpen uten innlogging).
- 09:24 build_solution_index.py og verify.py: 21 kort, OK. build_catalog.py byttet bare rekkefølgen på søkeord med store og små bokstaver i seks profiler og catalog.json; de endringene er ikke tatt med.

## 2026-10-14, løsningskort fra Zak McKracken HD

- 16:30 Under arbeidet med å få Zak McKracken HD til å kjøre fra GitHub Pages: nytt kort `nettside-med-github-api-i-sandkassen` (teste en Pages-side som henter spillfilene fra api.github.com, fra Claude-sandkassen: Playwright-rutene hentes med requests gjennom proxyen, dummy-nøkkel, vent på tilstand i bildet). Opphav ZakMcKracken-HD@7147a72, PASS med `tools/nettsidetest.py` der.
- 16:30 ZakMcKracken-HD står ikke i det offentlige inventaret; offentlig_kontrollert 2026-10-14 (api private false). Repoet var privat tidligere samme dag, så lenkene i kortet slutter å virke hvis det blir privat igjen.
- 16:30 build_solution_index.py og verify.py: 22 kort, OK. build_catalog.py byttet bare rekkefølgen på søkeord i fire profiler og catalog.json; de endringene er ikke tatt med.

## 2026-10-15, løsningskort fra The Dig HD

- 01:23 To nye kort fra arbeidet i Dig-HD-Remake (PR 52): `publisert-mod-er-fasit` (bygg: runden fletter inn i den publiserte HD-modden i stedet for å erstatte den, og publiseringen stopper ved tap; opphav Dig-HD-Remake@b612c315) og `logg-over-det-som-mangler-hd` (testing: motoren skriver det som står på skjermen uten HD til en fil i lagringsmappen; opphav Dig-HD-Remake@6221c6ee). Begge PASS med tester i Dig-HD-Remake.
- 01:23 Dig-HD-Remake står ikke i det offentlige inventaret; offentlig_kontrollert 2026-10-15 (visibility public i GitHub-listen).
- 01:23 build_solution_index.py og verify.py: 24 kort, OK. build_catalog.py byttet bare rekkefølgen på søkeord i seks profiler og catalog.json; de endringene er ikke tatt med.

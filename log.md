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

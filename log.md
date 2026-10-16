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
- 04:33 Tom: lag PR. PR 3 laget fra grenen ccr-4d55edba-vg2olf mot main. Repoet har ingen CI.

## 2026-10-16, stjerner og decomp.wtf

- 17:52 Codex: hentet prosjektbibliotek på nytt og sammenlignet offentlige stjerner med inventaret fra 5. oktober etter repo-ID. 20 nye stjerner; dagens inventar har 75 offentlige stjerner og 37 egne offentlige repoer. Sammenlignet også med offentlige stjerner i den innloggede kontoens komplette, paginerte svar.
- 17:52 Codex: opprettet offentlig fork Tombonator3000/decomp.wtf. Originalen er arkivert fra 15. oktober. Begge main-grenene pekte til 575b4a30ed481ff5497dfb9ce4f599368a95a04a ved kontrollen. Bevarte README, LICENSE og pyproject.toml fra denne revisjonen, med kontrollsummer og eget notat og manifest under repoer/.
- 17:52 Codex: oppdaterte skilldekningen for alle 101 unike offentlige repoer, med 55 nye eller endrede kilder. Indeksen har 274 skillfiler, 247 ulike dokumentinnhold og 26 kilderepoer. Originalen og egen decomp.wtf-fork har samme skillinnhold. Ingen tredjepartverktøy eller skills er installert eller kjørt.
- 17:52 Codex: la til norske notater for de 20 nye stjernene og forken. find.py bruker notatene også for nye inventaroppføringer, og decomp.wtf peker til gjennomgangen. Arkiverte stjerner merkes i det genererte inventaret. Tidligere norske notater, historiske profiler og kildefiler er beholdt.
- 17:52 Codex: fjernet 20 midlertidige offentlig_kontrollert-felt fra kort som nå har offentlig opphav i inventaret. Bygget løsningsindeksen med alle 24 kort beholdt. build_catalog.py er kjørt; bare kjent sorteringsstøy er tatt ut igjen.
- 17:55 Codex: verify.py passerer med 118 kildefiler, 24 løsningskort og 391 lokale lenker. Kontrollerte også alle 20 tillegg mot autentisert offentlig stjernesvar, søk og profillenker, at eldre norske notater er uendret, og skillendringene 40 nye, 2 erstattede og 46 endrede filer. Git-diffkontrollen er uten feil for egne filer; bevarte originaltekster kontrolleres med hash.

## 2026-10-16, bedre søk og fast biblioteksrutine

- 18:36 Codex: Tom ba om bedre søk og nøkkelord, en skill for biblioteket og fast rutine for å søke før nye løsninger. find.py har nå relevansrangering, 39 norske og engelske synonymgrupper med 170 aliaser, behovsord, forklaring, antallsgrense og filtre. Eksisterende profiler får også ferske norske notater i søket.
- 18:36 Codex: leste navn og beskrivelse fra 248 festede offentlige skillblobber, kontrollert mot Git blob-SHA uten å kjøre skillinstruksjoner. 273 av de 274 indekserte skillfilene har beskrivelse. Identiske skillkopier er ett treff med alle kildestedene beholdt.
- 18:36 Codex: bygget START_HER.md, SOK.md og data/search-index.json med 397 søkeoppføringer. verify.py avviser utdaterte indekser og feil i søkeordoppsettet. Historiske katalogdata og kildeversjoner er uendret; sortering av like søkeord er gjort stabil.
- 18:36 Codex: laget skills/prosjektbibliotek med søkehjelper og GitHub-rute, og scripts/setup_agents.py for avgrenset installasjon i Codex og Claude Code. Oppsettet bevarer øvrige brukerinnstillinger, er gjentakbart og dokumenterer at lokal installasjon ikke aktiverer skyøkter.
- 18:36 Codex: 14 tester passerer, med 12 konkrete behovssøk blant de tre første treffene, filtre, skillkopier, metadata, stabil katalogbygging, utdatert indeks og installasjon i midlertidig brukerområde. verify.py passerer med 121 kildefiler, 24 løsningskort og 675 lokale lenker; skill-creator-valideringen passerer.
- 18:40 Codex: installerte skillen lokalt i ~/.agents/skills/prosjektbibliotek og ~/.claude/skills/prosjektbibliotek, med fast instruks i ~/.codex/AGENTS.md og ~/.claude/CLAUDE.md. Fast bibliotekkopi ligger i ~/.local/share/prosjektbibliotek med GitHub som origin. Begge søkehjelpere er prøvd fra /tmp uten miljøoverstyring og finner riktig kantutjevningskort. Pakkefilene er identiske med repoet; begge skillvalideringer passerer og hver instruksjonsfil har én rutineblokk.
- 18:40 Codex: laget portabel prosjektbibliotek-skill.zip utenfor repoet med tre pakkefiler, uten lokale konfigurasjonsstier. Skyoppsettet er dokumentert i docs/AGENTOPPSETT.md; ingen skyinnstillinger er endret.

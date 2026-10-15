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

## 2026-10-15, natteskift for Claude og Codex

- 18:20 Tom: Claude og ChatGPT er på samme PC (Linux) med full tilgang; få dem til å samarbeide og kontrollere hverandre automatisk, og jobbe til i morgen.
- 18:30 Første utkast av `samarbeid/samarbeid.mjs` kjørte begge agentene med alle sperrer av. Kontrollen i Claude-økta stoppet det (agenter uten tilsyn og uten sperrer). Ikke committet.
- 18:45 Codex 0.162.1 sjekket: `codex mcp-server` finnes ikke lenger, `codex exec` tar prompten fra stdin, `image_generation` er på. I `--sandbox workspace-write` er `.git` skrivebeskyttet og nettet stengt, så Codex kan ikke committe selv (prøvd med `codex sandbox`).
- 18:50 Skrevet om: grafikksporet (Codex tegner i gpt-arbeid, skriptet committer bare resultat.png, notat.md, hovedark og rapporter/, Claude kjører tools/gpt_runde.sh og ser på bildene) og kodesporet (Claude koder på `samarbeid/natt-<dato>`, Codex kontrollerer, Claude retter). Claude i `--permission-mode auto`, Codex i sandkassen. `installer.sh`, `natt.sh` og README.
- 18:57 Testet med falske claude og codex mot en lokal origin: begge sporene, beskyttede filer holdt utenfor og lagt i stash, push av begge grenene, stopp når sporene er tomme. `claude -p --permission-mode auto` prøvd med ekte Claude. Codex godtar flaggene, men er ikke kjørt med innlogging.
- 18:59 verify.py OK.
- 19:08 Tom kjørte installer.sh: maskinen hadde ikke Node, så installasjonen stoppet, og natt.sh ga «Failed to execute». installer.sh legger nå Node 22 fra nodejs.org i ~/.local/share/node uten sudo (sjekksum kontrollert), og stiene i ~/.bashrc. Ingen apt-kommandoer lenger, siden maskinen ikke nødvendigvis bruker apt. natt.sh legger de samme stiene i PATH og sier tydelig fra hvis node, claude, codex eller repoet mangler. Testet i en falsk hjemmemappe uten Node: Node 22.23.3 installert, npm installerte Codex 0.162.1.
- 19:41 Toms PC krasjet og ble startet på nytt. samarbeid.mjs tåler nå omstart: en gammel index.lock fjernes når ingen git-prosess kjører, og halvferdige endringer på en samarbeid/-gren legges i stash i stedet for at skriptet nekter å starte (på andre grener nekter det fortsatt). Samme gren fortsetter samme dag. installer.sh sjekker at claude og codex faktisk starter (ikke bare at filen finnes), og installerer Codex med --force så en avbrutt npm-installasjon blir ryddet. Testet med falske agenter: lås og endringer fra en "krasj" ble ryddet og natten fortsatte.
- 19:46 Tom: krasjen kom av Flight Simulator 2024 med for høye grafikkinnstillinger på RTX 3080, ikke av natteskiftet. Rettelsene for omstart beholdes uansett.
- 20:21 Tom: GPT lager ingen grafikk, og ingenting er pushet fra natteskiftet (ingen samarbeid/natt-gren, siste commit i gpt-arbeid er Claude sin ordre 18:47). Tom ba om en markdown med alt Claude prøver å gjøre, så GPT kan utføre det på PC-en. Skrev samarbeid/OPPDRAG-GPT.md: oppdatering, status for kjøringen, installasjon og innlogging, test av Codex-sandkassen (med AppArmor-profil for bwrap hvis Ubuntu sperrer user namespaces), test av Claude i auto-modus, klargjøring av Sam-Max-HD, test av bildeverktøyet i sandkassen, prøvetur, natteskift og plan B. GPT skal ikke skru av sperrene, og skal skrive funnene i log.md og pushe.

## 2026-10-15 20:37 (Codex)

- Hentet og fulgt samarbeid/OPPDRAG-GPT.md. Fant at forrige prøvetur faktisk laget bilder, men commit feilet med «Author identity unknown» og push med «Authentication failed». Løpet fortsatte likevel og la leveranser i stash. Stoppet med STOPP-filen; avslutning bekreftet 20:25.
- installer.sh besto: Node 22.23.3, Claude Code 2.1.300, Codex 0.162.1. Codex logget inn med ChatGPT, Claude svarer. Codex-sandkassen ga SANDKASSE_OK, ingen sudo/AppArmor-endring. Claude i auto-modus kjørte git status. Spilldata, smhd og uttrekk finnes.
- Ekte codex exec med workspace-write laget et blått testbilde med bildeverktøyet og kopierte det til jobbmappen. PNG-en visuelt kontrollert; testfilen fjernet fra grafikkarbeidstreet etter lokal sikring. Ingen sperrer slått av.
- Git-forfatter satt bare i Sam-Max-HD-repoet til KI-samarbeid. GitHub CLI 2.102.0 lagt lokalt uten sudo, SHA-256 kontrollert mot offisiell utgivelse. Tom fullførte nettleserinnlogging. gh auth setup-git og tørr push til nattgrenen besto. Ingen nøkler eller innloggingskoder logget.
- fig091_04 sikret fra stash, egenkontroll 6/6 OK, committet på gpt-arbeid. Stashene beholdt. Avvist obj187_05 er ikke lagt over produksjonsfilen.
- Skriptet sjekker nå Git-identitet og push før agentarbeid, stopper ved commit-/push-/hente-/stashfeil og beholder leveransen ved commitfeil. Fire regresjonstester med falske agenter besto. Prøvetur/natt gjenstår til grafikk- og kodeleveransene fra denne chatten er sikret.

## 2026-10-15 20:49 (Codex)

- Prøveturen startet 20:43 med workspace-write og Claude auto. Motorretting PR32 er opprettet, oppdatert mot siste main og har grønn CI. Grafikkrettinger og gjenopprettet fig091_04 er pushet. 53 pipelinetester består på nattgrenen, 52 på motorgrenen etter oppdatering mot main.
- Tom presiserte automatisk samarbeid gjennom natten til mest mulig er ferdig i morgen. Lagt til nattevakt.mjs: følger prøveturen, krever faktisk grafikkleveranse, push og Claude-runde, avslutter prøven kontrollert etter første komplette runde og starter natt.sh til 08:00. Oppsett-/agentfeil setter STOPP og gir ingen automatisk omstart. Nattevakten følger også nattløpet. Sju tester for Git-feil og overgangsbetingelser besto.
- Nattevakten kjører løsrevet fra chatten. Status og logger ligger i ki-samarbeid-logg. Ingen tmux på maskinen, derfor start_new_session med loggfiler; natt.sh holder maskinen våken. Ingen endring eller push til main.

## 2026-10-15 20:56 (Codex)

- Utvidet kontrollen til ti tester, inkludert full prosessovergang med lokalt falskt nattskript og synlig feil ved manglende program. Alle består. Aktiv vakt oppdatert før prøverunden er ferdig.
- Opprettet lokal trådkontroll «Nattkontroll Sam & Max», hvert 20. minutt gjennom natten med en siste morgenkontroll. Selve arbeidsløpet slutter 08:00; kontrollen kan avslutte rapporteringen etterpå og settes deretter på pause.
- Første prøverunde produserer obj187_05. Codex bruker bildeverktøyet, sammenligner original/stil og kjører kontroll mellom rettingene. Ingen oppsettfeil i den nye prøven så langt. Python-tillatelsen fra Tom til rensing/plassering er ført videre til nattprompten.

## 2026-10-15 21:03 (Claude)

- Leste Codex sine oppføringer og endringer fra 20:37 til 20:56. Sperrene er uendret (Claude auto, Codex workspace-write). Codex sine 10 tester består her.
- Natten er i gang på PC-en: gpt-arbeid har GPT (natt): fig091_04 og obj187_05, nattgrenen har Claude sine kontroller og myk.py versjon 6.
- Én endring: push stopper ikke lenger natten ved første feil. Den prøves tre ganger til (30 s, 2 min og 5 min, SAMARBEID_PUSH_VENT) før det blir en oppsettfeil, så et kort nettbrudd ikke avslutter natten. Testen for push-feil kjører med ventetid 0 og sjekker at nye forsøk logges. 10 av 10 tester består.

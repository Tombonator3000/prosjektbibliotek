# Minne for prosjektbiblioteket

Beslutninger og fallgruver som neste person trenger. Dagbok hører hjemme i log.md.

## Løsningskort (fra 2026-10-09)

- Kortene er de eneste kildefilene: `losninger/<domene>/<id>.md` med en nøkkel: verdi-blokk øverst og faste seksjoner (Symptom, Årsak, Løsning, Fallgruver, Slik verifiseres det, Bevis, Brukt i). `data/losninger.json` og `LOSNINGER.md` er generert av `scripts/build_solution_index.py`.
- Domenene er grafikk, lyd, testing, ui, bygg og regler. De samme står i skillen spill-gjenbruk i Toms Claude-konto, så endrer du lista, må skillen også endres.
- `opphav` har formen `eier/repo@<40 tegn>:sti#Llinje`. Status gjelder opphavet på datoen i kortet; biblioteket kjører ikke koden.
- `verify.py` krever at opphavet står i `data/offentlig-inventar.json` (owned_public eller starred), eller at kortet har `offentlig_kontrollert`. Når inventaret er synkronisert og har fått repoet, kan nøkkelen fjernes.
- Nøkkelblokken tåler bare enkle verdier. Lister skrives med komma (stikkord, se_ogsa), og bevis og bruk som punkter i sine seksjoner.
- Lenker til Markdown-filer på GitHub trenger `?plain=1#L<linje>` for å vise linjen.

## Fallgruver

- `scripts/sync_public_inventory.py` får 403 fra proxyen i Claudes skyøkter (users/Tombonator3000/starred). Kjør den på en egen maskin.
- `build_skill_index.py --refresh` krever at alle repoene i inventaret er skannet. Et repo i owned_public uten skillskann gjør at verify.py feiler.
- Biblioteket er offentlig. Ingen navn, stier eller kode fra private repoer, heller ikke i kort, log.md eller memory.md.
- `build_catalog.py` sorterer søkeord ustabilt når de bare skiller seg i store og små bokstaver (Blender og blender). Kjøringen gir da diff i catalog.json og profilene uten at noe er endret. Ta ikke med den støyen (sett 2026-10-13).

## Natteskift (samarbeid/, fra 2026-10-15)

- `samarbeid/samarbeid.mjs` lar Claude og Codex jobbe gjennom natten på Toms Linux-maskin. Roller som i Sam-Max-HD: Codex tegner, Claude kontrollerer grafikken; Claude koder, Codex kontrollerer koden.
- Ingen av dem kjører uten sperrer. Claude: `--permission-mode auto`. Codex: `--sandbox workspace-write` (ikke nett, `.git` skrivebeskyttet), så skriptet committer for Codex og bare filtypene grafikeren skal levere.
- `codex mcp-server` er borte i Codex 0.162. Kommunikasjonen går via `codex exec` og `claude -p`.
- Grafikksporet bruker samme arbeidstre som `tools/gpt_gren.sh` (`work/.gpt-gren`), ellers nekter git to arbeidstrær på gpt-arbeid.

- Erfaring fra PC-prøven 15. oktober: innlogging i Codex/Claude er ikke GitHub-innlogging for git. Kontroller Git-identitet og push før agentkall. Commitfeil skal bevare leveransen i arbeidstreet, ikke gjemme den i stash og melde den levert. Skriptet stopper nå ved slike Git-feil.
- Ekte codex exec 0.162.1 på Linux er prøvd med workspace-write: bildeverktøyet laget PNG under generated_images og kopierte den inn i gpt-arbeid. SANDKASSE_OK; ingen sudo-løsning nødvendig på denne maskinen.
- En 503 med «Selected model is at capacity» avbrøt et kall etter at fire bilder var ferdig skrevet. Bevar filene, kontroller dem og sikre commit før gjenopptak. Samme modell svarte igjen i separat helsesjekk. STOPP må kontrolleres under venting, ikke bare før den; regresjonstest dekker dette. Nattevakten kan følge gjenopptatt prosess med nattPid/nattLogg uten å starte et ekstra løp.

- Nattens importretting d968287b i Sam-Max-HD er Codex-kontrollert med 59 pipelinetester. Tørrkjøringen teknisk godkjenner tolv eksisterende sjekk-jobber; det er ikke nye grafikkleveranser. De elleve som ikke var visuelt sett, ble kontrollert av Codex 16. oktober rundt 01:42 mot original og mottaksforhåndsvisning, uten åpenbar ny feilplassering eller avklipping. Obj602_01 var allerede sett av Claude. Alle tolv har dermed visuell plasseringskontroll; tell dem separat fra nattens grafikkleveranser. Dette er ikke Toms stilgodkjenning eller runtimekontroll. Bruk orkestratorens faktiske klokkeslett; agentenes egne loggklokkeslett kan være feil.

- Små figurark: alfa-klassifisering b26e80eb er separat Codex-kontrollert (59 pipelinetester, faktisk fig259_02 og 73 leverte ark). Bare fig259_02 endrer klassifisering. Feilen gjaldt unødvendig retur; myk-importen hadde allerede tatt håndrutene med. Grafikkstegets kodeendringer faller utenfor koordinatorens vanlige kodekontroll, så neste nattefokus legger kodeendringer til kodesporet. Vaktretting 2d3691b skiller bestilt STOPP fra reelle feillinjer, med femten Node-tester.

- Ikonglorie: nattkode 6ea6d4b0 er Codex-godkjent med 60 pipelinetester og brukt i hd-mod 8f3f82a7. Codex har sammenlignet ikon01s fire PNG-filer mot original og førbilder: kraftig magentaglorie redusert, uendret alfa/størrelse, men små grønne/lilla kantpiksler gjenstår på bilene. Neste retting er ført i Sam-Max-HD todo.md og dokumentert i nattgrenens 04cb9f81 (bare dokumentasjon). Før/etter og hasher finnes i Codex-arbeidsmappens output/natt-ikonfargelas-20261016. Ikonark 07 til 09 er sett i mottaksforhåndsvisninger; hver native PNG er ikke isolert kontrollert. Ikke regn kantene som helt pikselrene eller motorverifiserte. Fem av ni ikonark er pikselidentiske før/etter kodeendringen, fire får justert fargelås; status og geometrikontroll er uendret.


- Neste ikonretting ecd9ec0e er Codex-godkjent 16. oktober klokken 03:21 med 62 pipelinetester og tørrkjøring på 163 ikoner; pushet i c7fc54b4. Den renser arkfarge fra kanten med vern for ekte farger i originalen og lar alfa stå. Ny modd og visuell etterkontroll gjenstår. Førbilder av alle 163 faktiske ikon-PNG fra hd-mod 001e2405 er sikret lokalt i /home/tom/Documents/Codex/2026-10-15-sjekk-sam-max-repo-vi-var/output/natt-kantrens-20261016/for, med hasher i kilder.json. Bruk disse ved neste import for mørk/lys sammenligning, særlig obj661_01 til obj663_01, obj670_01 og obj824_01 (bladet skal forbli grønt), samt ikon07/08. Ikke bland denne kantrensen med motorfeilene i PR32 eller tell den som runtimeverifisert.


- Kantrens ecd9ec0e er tatt i bruk i hd-mod 55f976de og har fått separat Codex-etterkontroll rundt 04:00 den 16. oktober. Alle 163 ikon-PNG har identisk størrelse/alfa mot 001e2405; 159 har synlig RGB-endring. 22 navngitte PNG er visuelt sett på mørk og lys bakgrunn, med tydelig færre grønne/magenta kantrester og ingen åpenbar ny skade på ekte farger i utvalget. Tynne mørke/lilla streker og trappetrinn fra uendret alfa gjenstår på bilene. Ikke helt pikselrent eller motorverifisert. Før/etter, åtte paneler og etter-kontroll.json ligger i output/natt-kantrens-20261016 i Codex-arbeidsmappen. Sam-Max-HD todo-punktene for kodekontroll og nybygd visuell etterkontroll kan kvitteres i en ledig fase; ikke skriv der mens Claude bruker logg/todo i grafikkontrollen.

# Natteskift: Claude og ChatGPT (Codex) jobber sammen

Lar Claude Code og Codex jobbe i samme repo på egen hånd gjennom natten og kontrollere hverandre. Laget for Linux og for HD-remake-repoene (Sam-Max-HD, Dig-HD-Remake og de andre med `tools/gpt_runde.sh`), men kodesporet virker i alle repoer med `AGENTS.md` og `todo.md`.

## Hvem gjør hva

Rollene er de samme som i `AGENTS.md` i Sam-Max-HD, bare uten at Tom flytter filer mellom dem:

| Spor | Lager | Kontrollerer |
| --- | --- | --- |
| Grafikk | Codex tegner de neste jobbene i `ORDRE.md` i grenen `gpt-arbeid` | Claude kjører `tools/gpt_runde.sh` (sjekker, bygger HD-modden, skriver ny `ORDRE.md` med retur) og ser selv på bildene mot originalen |
| Kode | Claude tar en oppgave fra `todo.md`, tester og committer | Codex går gjennom endringene og svarer GODKJENT eller ENDRINGER; Claude retter, opptil to ganger |

Sporene går etter tur: to grafikkrunder, så en kodeoppgave (`--spor`). Det Claude avviser, havner i `ORDRE.md` og blir det første Codex tar i neste runde. Når et spor er tomt, fortsetter det andre alene.

Det som trenger deg, blir liggende: godkjenning av stil og resultater, testing med skjerm og lyd, og at koden fra natten flettes inn i `main`.

## Sikkerhet

Ingen av dem kjører med sperrene av:

- **Claude** kjører i `--permission-mode auto`. Den stopper ikke for å spørre, men en kontroll avviser handlinger som er farlige eller går utenfor oppgaven.
- **Codex** kjører i sin egen sandkasse (`--sandbox workspace-write`). Den kan bare skrive i arbeidsmappen, har ikke nett og kan ikke endre `.git`. Bildeverktøyet virker fortsatt, siden det kjører hos OpenAI.
- **Skriptet** committer det Codex lager, men bare `resultat.png`, `notat.md`, hovedark og `rapporter/`. Endrer Codex andre filer (for eksempel `prompt.txt`, `jobb.json` eller `ORDRE.md`), tas de ikke med, og de legges i `git stash`.
- Koden fra natten ligger på grenen `samarbeid/natt-ÅÅÅÅ-MM-DD`, aldri i `main`.
- Ingenting slettes. Det en agent lar ligge uten å committe, havner i `git stash list`.

## Første gang

```sh
git clone https://github.com/Tombonator3000/prosjektbibliotek ~/prosjektbibliotek
~/prosjektbibliotek/samarbeid/installer.sh
```

`installer.sh` trenger bare git og curl. Mangler Node, legger den Node 22 fra nodejs.org i `~/.local/share/node` (sjekksummen kontrolleres, ingen sudo). Så installerer den Claude Code og Codex hvis de mangler, og ber deg logge inn. For Codex velger du «Sign in with ChatGPT»; da brukes ChatGPT-abonnementet ditt. Stiene legges i `~/.bashrc`, så åpne en ny terminal etterpå (eller bruk `natt.sh`, som finner dem selv).

Får du det ikke i gang, gi [OPPDRAG-GPT.md](OPPDRAG-GPT.md) til ChatGPT/Codex på PC-en. Den går gjennom installasjon, innlogging, sandkassen, bildeverktøyet og en prøvetur steg for steg, og skriver hva den fant i log.md.

## Starte

Repoet må være rent (`git status` uten endringer). Grafikksporet trenger at `./spill.sh` eller `tools/gpt_runde.sh` har kjørt på maskinen før, så spillfilene og `.venv` er på plass.

Kjør det først en kort stund mens du ser på, så du vet at begge er logget inn og at Codex får laget bilder:

```sh
~/prosjektbibliotek/samarbeid/natt.sh ~/Sam-Max-HD --timer 1 --jobber 1
```

Se i `~/ki-samarbeid-logg/` at Codex leverte et bilde og Claude kjørte runden. Så natteskiftet:

```sh
tmux new -s natt
~/prosjektbibliotek/samarbeid/natt.sh ~/Sam-Max-HD
```

Det går til 08:00, holder maskinen våken med `systemd-inhibit` og pusher arbeidsgrenen og `gpt-arbeid` etter hver runde, så du kan følge med fra telefonen på GitHub. Med `tmux` kan du lukke terminalen (Ctrl+B, så D) og hente den igjen med `tmux attach -t natt`.

Valg kan legges til bak:

```sh
natt.sh ~/Sam-Max-HD --til 07:00
natt.sh ~/Sam-Max-HD --spor grafikk               # bare grafikk
natt.sh ~/Sam-Max-HD --jobber 6                   # flere jobber per grafikkrunde
natt.sh ~/Sam-Max-HD --fokus "bare figurarkene for Sam og Max"
```

`node samarbeid.mjs --help` viser alle valgene.

## All grafikken som mangler

Natteskiftet kan gå i flere døgn, bare med grafikk, til Codex ikke finner flere jobber:

```sh
tmux new -s grafikk
~/prosjektbibliotek/samarbeid/natt.sh ~/Sam-Max-HD --spor grafikk --jobber 8 --timer 168
```

`--timer 168` er en uke; skriptet stopper før hvis alle jobbene er tegnet. Med 8 jobber per runde går mindre tid med til kontrollrundene til Claude. Det som begrenser farten, er kvoten på bildeverktøyet i ChatGPT: leverer Codex ingen bilder to runder på rad, tar grafikken 30 minutters pause og prøver igjen.

Kjører gjennomspillingsagenten (`tools/gjennomspill.sh` i Sam-Max-HD) samtidig, leser Claude funnene dens i hver grafikkontroll og sender feil grafikk tilbake til Codex.

## Stoppe

- Ctrl+C: stopper etter steget som pågår. Ctrl+C to ganger stopper med en gang.
- Fra en annen terminal eller over ssh: `touch ~/ki-samarbeid-logg/STOPP`

STOPP avbryter også venting før et nytt agent- eller pushforsøk, innen ett sekund. En pågående agent får fullføre steget; stoppbeskjeden starter ingen nye agentkall. Committer som ikke ble pushet, blir liggende lokalt.

## Om morgenen

- `~/ki-samarbeid-logg/<dato>_<klokke>.md`: hva som skjedde, med klokkeslett, og kodecommitene til slutt.
- `~/ki-samarbeid-logg/<dato>_<klokke>/`: prompten og hele utskriften fra hvert kall, også funnene fra kontrollene.
- `log.md` i repoet og `work/gpt/RAPPORT.md`: det agentene selv har skrevet.
- HD-modden i `hd-mod` er bygget med det Claude godkjente i natt. `./spill.sh` henter den.
- Koden: se gjennom `samarbeid/natt-<dato>` og lag PR mot `main` hvis du vil ha den inn.
- `git stash list`: det som ikke ble tatt med.

## Verdt å vite

- Bruken går av kvotene på abonnementene. Feiler et kall, venter skriptet 5, 15 og 30 minutter før det gir opp det steget. Leverer Codex ingen bilder to runder på rad (typisk grensen på bildeverktøyet), tar grafikken 30 minutters pause.
- Ett kall får maks 90 minutter (`--kall-minutter`).
- Skriptet stopper ved fire feil på rad, når begge sporene er tomme, eller når tiden er ute.
- Testet med falske `claude` og `codex` mot en lokal origin. Ekte PC-prøve 15. oktober har også levert, pushet og fått Claude-kontrollert grafikk med Codex 0.162.1 i workspace-write og Claude auto. Testene dekker Git-feil, avbrudd under venting og tilkobling til et eksisterende nattløp.
- Eldre Codex hadde `codex mcp-server`, som Claude kunne bruke som MCP-server. Den finnes ikke i 0.162, så de snakker sammen via `codex exec` og `claude -p`.

## Git-feil ved oppstart og levering

Fra PC-kontrollen 15. oktober sjekkes Git-forfatter og, med --push, en tørr push før agentarbeidet. Codex/Claude-innlogging er separat fra GitHub-innlogging for terminalen. Sett user.name/user.email lokalt i spillrepoet, og logg inn med GitHub CLI ved behov. En commit- eller pushfeil stopper løpet. Ved commitfeil beholdes leveransen i arbeidstreet; den blir ikke meldt vellykket eller lagt i stash. Henting, fast-forward og sikring i stash må også lykkes.

Regresjonstest: `node --test samarbeid/samarbeid.test.mjs`. Testene bruker bare midlertidige lokale repoer og falske agenter.

## Automatisk overgang etter prøvetur

`node samarbeid/nattevakt.mjs KONFIGURASJON.json` kan følge en pågående prøvetur og starte natt.sh til 08:00 etter en levert, pushet og Claude-kontrollert grafikkrunde. Prøvens timegrense er en øvre grense; vakten går videre når den komplette runden er bekreftet. Den setter STOPP ved feil og starter ikke automatisk om igjen. Konfigurasjon, PID og status ligger lokalt i loggmappen, ikke i repoet. STOPP fra brukeren avbryter overgangen. Tester: `node --test samarbeid/*.test.mjs`.

Etter undersøkt feil og kontrollert gjenopptak kan vakten kobles til en allerede startet koordinator: sett `nattPid` og `nattLogg` til den nye prosessen og dens egen logg i konfigurasjonen. Behold `frist`, `nattStdout`, `loggmappe`, `statusfil` og `vaktlogg`. Denne modusen hopper over prøveturen og starter ingen ekstra koordinator. Manglende prosess eller logg setter STOPP. Den er ikke en automatisk omstart etter feil.

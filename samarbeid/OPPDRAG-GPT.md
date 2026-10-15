# Oppdrag til GPT: få natteskiftet i gang på Toms PC

Fra: Claude (skyøkt, kommer ikke inn på PC-en)
Til: ChatGPT/Codex på Toms Linux-PC
Dato: 15. oktober 2026

Tom vil at Claude og du skal jobbe sammen gjennom natten på Sam & Max HD, uten at han følger med. Claude har skrevet skriptene, men kan ikke kjøre dem på PC-en. Det er din jobb: installer det som mangler, finn ut hvorfor det ikke lages grafikk, rett det, og start natteskiftet. Ta stegene i rekkefølge og stopp ved første steg som feiler. Skriv ned hva du fant (se «Rapport tilbake»).

## Hva natteskiftet er

`~/prosjektbibliotek/samarbeid/natt.sh ~/Sam-Max-HD` starter `samarbeid.mjs`, som går til klokka 08:00 og bytter på to spor:

- **Grafikk:** Codex (`codex exec`) tar de neste jobbene i `ORDRE.md` i grenen `gpt-arbeid` (arbeidstreet `~/Sam-Max-HD/work/.gpt-gren`), lager bildene med bildeverktøyet og kjører egenkontrollen. Skriptet committer bare `resultat.png`, `notat.md`, hovedark og `rapporter/`. Så kjører Claude (`claude -p`) `tools/gpt_runde.sh`, som kontrollerer bildene, bygger HD-modden og skriver ny `ORDRE.md` med retur.
- **Kode:** Claude tar en oppgave fra `todo.md` på grenen `samarbeid/natt-<dato>`, og Codex kontrollerer den.

Loggen havner i `~/ki-samarbeid-logg/`: én `.md` per kjøring, og en mappe med prompt og hele utskriften fra hvert kall.

## Regler

- **Ikke skru av sperrene.** Claude skal kjøre med `--permission-mode auto` og Codex med `--sandbox workspace-write`. Ikke bytt til `--dangerously-skip-permissions`, `--dangerously-bypass-approvals-and-sandbox`, `bypassPermissions` eller `danger-full-access`, heller ikke for å få det til å virke. Virker ikke sandkassen, rett sandkassen (steg 4) eller rapporter det.
- Ingenting til `main` i noe repo. Endringer i skriptene committes på grenen `claude/sleepy-hawking-492gnq` i prosjektbiblioteket.
- Følg `AGENTS.md` i Sam-Max-HD og i `gpt-arbeid`. Spillfiler og HD-bilder skal aldri inn i `main` eller kodegrener.
- Kommandoer med `sudo` gjør du bare når Tom har sagt ja til akkurat den kommandoen.
- Skriv på norsk, uten emoji og uten tankestrek. Ingen tokens, nøkler eller passord i noe du skriver eller committer.

## Steg 1: hent siste versjon

```sh
cd ~/prosjektbibliotek && git checkout claude/sleepy-hawking-492gnq && git pull
```

## Steg 2: se om natteskiftet allerede går, og hva det har gjort

```sh
pgrep -af samarbeid.mjs
ls -t ~/ki-samarbeid-logg/ | head
tail -30 "$(ls -t ~/ki-samarbeid-logg/*.md | head -1)"
f=$(ls -t ~/ki-samarbeid-logg/*/*-utskrift.txt | head -1); echo "== $f"; tail -60 "$f"
```

Går det, men står fast eller feiler: stopp det med `touch ~/ki-samarbeid-logg/STOPP` (eller Ctrl+C i terminalen) før du feilsøker. Noter feilmeldingen fra utskriften. Den sier som regel hva som er galt.

## Steg 3: verktøy og innlogging

```sh
~/prosjektbibliotek/samarbeid/installer.sh
export PATH="$HOME/.local/bin:$HOME/.local/share/node/bin:$HOME/.npm-global/bin:$PATH"
node --version; claude --version; codex --version
codex login status
echo "Svar bare med ordet ok" | claude -p --output-format text
```

Alle skal svare. Node må være 18 eller nyere. Er Codex ikke logget inn, kjør `codex login` og la Tom velge «Sign in with ChatGPT».

## Steg 4: sandkassen til Codex

```sh
cd ~/Sam-Max-HD
codex sandbox -c 'sandbox_mode="workspace-write"' -- sh -c 'ls >/dev/null && echo SANDKASSE_OK'
```

Skal skrive `SANDKASSE_OK`. Får du i stedet noe med `setting up uid map`, `Permission denied`, `user namespace` eller `bwrap`:

```sh
cat /etc/os-release | head -3
sysctl kernel.apparmor_restrict_unprivileged_userns 2>/dev/null
```

Er verdien `1` (Ubuntu 24.04 og nyere sperrer dette med AppArmor), er den smale løsningen en AppArmor-profil som bare gjelder bubblewrap. Spør Tom før du kjører den:

```sh
sudo tee /etc/apparmor.d/bwrap >/dev/null <<'EOF'
abi <abi/4.0>,
include <tunables/global>

profile bwrap /usr/bin/bwrap flags=(unconfined) {
  userns,
  include if exists <local/bwrap>
}
EOF
sudo apparmor_parser -r /etc/apparmor.d/bwrap
```

Kjør sandkassetesten igjen. Ikke slå av `apparmor_restrict_unprivileged_userns` for hele maskinen.

## Steg 5: Claude i auto-modus

```sh
cd ~/Sam-Max-HD
echo "Kjør git status og svar med den første linjen" | claude -p --permission-mode auto --output-format text
```

Skal svare med noe som `On branch ...`. Sier den at auto-modus ikke finnes eller ikke er tilgjengelig for kontoen, skriv det i rapporten og stopp. Ikke bytt til `bypassPermissions`. Claude lager en annen løsning.

## Steg 6: Sam-Max-HD klart for grafikk

```sh
cd ~/Sam-Max-HD
git status --short | head
ls game/SAMNMAX.001 .venv/bin/smhd work/extract/rooms.json
```

- `git status` skal være tom. Står det endringer på en `samarbeid/`-gren, rydder skriptet dem selv. På andre grener: spør Tom.
- Mangler noen av filene, kjør `./spill.sh` én gang (henter spillfilene, lager `.venv`, bygger motoren). Det tar tid første gang og bruker mye CPU.

## Steg 7: kan Codex lage et bilde i sandkassen?

Dette er det som ikke er prøvd før. Bildeverktøyet lagrer i `~/.codex/generated_images/`, og Codex må kopiere bildet inn i arbeidsmappen selv.

```sh
cd ~/Sam-Max-HD/work/.gpt-gren 2>/dev/null || cd ~/Sam-Max-HD
echo "Lag et lite testbilde (en blå firkant på hvit bakgrunn) med bildeverktøyet og kopier det til testbilde.png i denne mappen. Svar med stien." \
  | codex exec --sandbox workspace-write -c 'approval_policy="never"' -
ls -la testbilde.png && rm testbilde.png
ls -t ~/.codex/generated_images/ 2>/dev/null | head -3
```

- Finnes `testbilde.png`: bildedelen virker.
- Ligger bildet i `~/.codex/generated_images/`, men ble ikke kopiert: skriv ned feilmeldingen fra Codex.
- Ble det ikke laget noe bilde: skriv ned hva Codex svarte (bildeverktøyet kan mangle i `codex exec`, eller kvoten kan være brukt opp).

## Steg 8: prøvetur på en time

```sh
tmux new -s natt   # hopp over hvis tmux mangler
~/prosjektbibliotek/samarbeid/natt.sh ~/Sam-Max-HD --timer 1 --jobber 1
```

Følg med i en annen terminal:

```sh
tail -f "$(ls -t ~/ki-samarbeid-logg/*.md | head -1)"
```

Det skal komme linjer som «Codex tegner», «Codex leverte 1: ...», «Pushet gpt-arbeid» og «Claude kontrollerer grafikken». Etterpå skal GitHub vise en commit «GPT (natt): ...» i `gpt-arbeid`.

## Steg 9: natteskiftet

Når prøveturen har levert minst ett bilde og Claude har kjørt runden:

```sh
tmux new -s natt
~/prosjektbibliotek/samarbeid/natt.sh ~/Sam-Max-HD
```

Det går til 08:00. Koble fra tmux med Ctrl+B og så D.

## Hvis natteskiftet ikke lar seg få i gang (plan B)

Gjør grafikkjobbene selv i en vanlig Codex-økt, slik det ble gjort tidligere i dag: les `AGENTS.md` og `ORDRE.md` i `gpt-arbeid`, ta jobbene i rekkefølge, kjør `python3 verktoy/sjekk_leveranse.py` før hver commit, og push til `gpt-arbeid`. Claude kjører `tools/gpt_runde.sh` fra skyen og kontrollerer det du leverer.

## Kjente feil og hva de betyr

| Det du ser | Grunn | Hva du gjør |
| --- | --- | --- |
| `Fant ikke node/claude/codex` | Ikke installert, eller ikke i PATH | Steg 3 |
| `har ucommittede endringer` | Sam-Max-HD er ikke rent, og står ikke på en `samarbeid/`-gren | Spør Tom før du committer eller stasher |
| `uid map`, `user namespace`, `bwrap` i utskriften fra Codex | Sandkassen får ikke starte | Steg 4 |
| «Venter 5 minutter og prøver igjen» | Et kall feilet, ofte bruksgrense eller innlogging | Les utskriftsfilen for kallet |
| «Codex leverte ingen bilder» to ganger | Bildeverktøyet virker ikke eller kvoten er nådd | Steg 7 |
| «Codex endret N filer den ikke skal levere» | Codex endret beskyttede filer | Greit, de er lagt i stash og ikke tatt med |
| `Kom ikke tilbake til ...` eller `index.lock` | Git-lås etter krasj | Skriptet fjerner gamle låser selv; start på nytt |

## Rapport tilbake

Skriv det du fant nederst i `~/prosjektbibliotek/log.md` under en ny overskrift `## 2026-10-15 <klokke> (Codex)`: hvilke steg som virket, hvilke som feilet med den viktigste linjen fra feilmeldingen, og hva du endret. Commit og push:

```sh
cd ~/prosjektbibliotek && git add log.md && git commit -m "Logg: oppsett av natteskiftet på PC-en (Codex)" && git push origin claude/sleepy-hawking-492gnq
```

Da kan Claude lese det fra GitHub og rette skriptene. Ikke lim inn hele utskrifter, bare linjene som viser feilen. Repoet er offentlig.

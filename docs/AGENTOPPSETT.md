# Bruk biblioteket først i andre prosjekter

Rutinen gjelder implementering, feilsøking og verktøyvalg i Toms prosjekter. Agenten søker fra behov og eksisterende teknologi, leser relevante kilder og oppgir hva som gjenbrukes. En vanlig samtale eller administrativ oppgave trenger ikke biblioteksøk.

## Lokal installasjon for Codex og Claude Code

Lag en fast lokal klon og installer den vedlikeholdte skillpakken:

```sh
git clone https://github.com/Tombonator3000/prosjektbibliotek.git ~/.local/share/prosjektbibliotek
python3 ~/.local/share/prosjektbibliotek/scripts/setup_agents.py
```

Hvis klonen allerede finnes, oppdater den med `git -C ~/.local/share/prosjektbibliotek pull --ff-only`. Behold eventuelle lokale endringer før en oppdatering; ikke bruk tvungen reset. En annen klon kan velges med `--library-root /sti/til/prosjektbibliotek`. `--target codex` eller `--target claude` velger én agent.

Installeringsskriptet:

- Kopierer skillen til `~/.agents/skills/prosjektbibliotek` for Codex og `~/.claude/skills/prosjektbibliotek` for Claude Code.
- Legger en avgrenset rutine i `~/.codex/AGENTS.md` og `~/.claude/CLAUDE.md`, med konkret søkekommando og lokal bibliotekssti.
- Bevarer teksten utenfor markørene `prosjektbibliotek:start` og `prosjektbibliotek:end`. Gjentatt kjøring oppdaterer samme blokk.
- Respekterer `CODEX_HOME` og `CLAUDE_CONFIG_DIR` når de er satt. `PROSJEKTBIBLIOTEK_ROOT` kan overstyre bibliotekkopien ved søk.

Start en ny økt for å få den globale instruksjonen inn i konteksten. Skillen kan også velges eksplisitt som `$prosjektbibliotek` i Codex eller `/prosjektbibliotek` i Claude Code.

Plasseringene følger [Codex sin skilloversikt](https://learn.chatgpt.com/docs/build-skills), [Codex sine globale instruksjoner](https://learn.chatgpt.com/docs/agent-configuration/agents-md), [Claude Code sine skills](https://code.claude.com/docs/en/skills) og [Claude Code sine instruksjonsfiler](https://code.claude.com/docs/en/memory).

## ChatGPT, Claude og andre maskiner

Lokale filer aktiverer ikke automatisk en skill eller rutine i nettskykontoer. Claude Code dokumenterer at personlige skills på maskinen ikke leses av Cowork og skyøkter. For samtaler med GitHub-tilgang kan denne teksten legges i prosjektets instruksjoner eller gis ved oppstart:

> Før implementering, feilsøking eller valg av verktøy: søk i Tombonator3000/prosjektbibliotek etter behov, symptomer og prosjektets eksisterende teknologi. Start med START_HER.md. Bruk den samlede SOK.md-indeksen selektivt og les de relevante kildene før gjenbruk. Kontroller kompatibilitet og teststatus. Ved svake treff, prøv færre ord eller et bredere søk én gang. Ved manglende tilgang, si det kort og fortsett med vanlig undersøkelse. Oppgi hvilke bibliotekskilder som brukes.

[Skillpakken](../skills/prosjektbibliotek/SKILL.md) er også bevart i repoet for installasjon eller opplasting i et miljø som støtter egne skills. Den har en GitHub-rute når terminal eller lokal klon mangler. Tilgang til biblioteket må finnes i den aktuelle økten.

## Vedlikehold og kontroll

Etter endringer i notater, søkeord eller skillpakken:

```sh
python3 scripts/build_catalog.py
python3 scripts/build_skill_index.py
python3 scripts/build_search_index.py
python3 -m unittest discover -s tests -v
python3 scripts/verify.py
```

Ved ny innhenting av offentlige kilder brukes `build_skill_index.py --refresh --describe` før søkeindeksen bygges. Beskrivelsene leses fra festede Git-blobber og kontrolleres mot blob-SHA; upstream-instruksjoner kjøres ikke. Oppdater den faste lokale klonen og kjør `setup_agents.py` igjen etter at skillpakken er endret.

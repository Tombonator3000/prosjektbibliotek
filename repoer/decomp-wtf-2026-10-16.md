# decomp.wtf og egen fork

Kontrollert 16. oktober 2026. [Originalrepo](https://github.com/i12bp8/decomp.wtf), [egen fork](https://github.com/Tombonator3000/decomp.wtf), [innhentingsmanifest](decomp-wtf-2026-10-16.json) og [tilbake til biblioteket](../README.md).

decomp.wtf gir en lokal AI-agent én spillfunksjon om gangen, kompilerer kandidatkode med spillets opprinnelige kompilator og sammenligner maskinkoden byte for byte. Verktøyet kan starte fra en egen spillkopi eller arbeide videre i et eksisterende dekompileringsprosjekt. Dette er matching-dekompilering, med C-kode og gjenbygging som mål.

## Status og versjon

| Felt | Kontrollert verdi |
|---|---|
| Stjernemerket | 2026-10-16T15:33:24Z |
| Originalprosjekt | Arkivert 15. oktober 2026. Utvikleren har avsluttet vedlikeholdet. |
| Egen fork | Tombonator3000/decomp.wtf, offentlig og ikke arkivert ved kontrollen |
| Originalens og forkens main | [575b4a30ed481ff5497dfb9ce4f599368a95a04a](https://github.com/Tombonator3000/decomp.wtf/commit/575b4a30ed481ff5497dfb9ce4f599368a95a04a) |
| Siste oppgitte versjon | 0.10.6 |
| Lisens | MIT, Sam Wolfs, 2026 |
| Python | 3.12 eller nyere ifølge pyproject.toml |
| Plattform | Linux. Windows via egen WSL 2-distribusjon, oppgitt som ustabil. macOS er ikke støttet i denne revisjonen. |
| Lokal runtime-test | UNVERIFIED. Dokumenter og GitHub-metadata er kontrollert; programmet er ikke installert eller kjørt. |

Forkens `main` ble kontrollert mot originalens `main`; begge pekte til committen over. Forken bevarer koden for videre arbeid. Det er ikke gjort kodeendringer i forken som del av denne oppdateringen.

## Mulig gjenbruk

- Studer løkken med funksjonsoppdeling, kandidatkode, opprinnelig kompilator, bytekontroll og konkret diff tilbake til agenten.
- Vurder lokale MCP-verktøy, funksjonsfordeling mellom agenter og håndtering av tidligere godkjente treff som arkitekturreferanse.
- Undersøk flyten for eksisterende dekompileringsprosjekter: koden endres i en lokal gren og vurderes med prosjektets bygg og objdiff.
- Bruk den medfølgende Demo Quest 64 som første avgrensede runtime-prøve i en senere oppgave. Ingen spillkopi eller integrasjon er lagt inn i biblioteket.

README anbefaler GameCube, Wii og Nintendo 64. PlayStation, PlayStation 2, GBA og DS er merket beta. Et byteidentisk treff dokumenterer sammenfall ved valgt bygg; en ferdig PC-port krever videre arbeid.

## Avgrensninger

Originalen får ikke flere feilrettinger eller utgivelser. Den arkiverte README-en har eldre avsnitt om automatiske oppdateringer; disse er ikke et løfte om nye upstream-versjoner. Egen videreutvikling må håndtere vedlikehold og avhengigheter.

MIT-lisensen gjelder verktøyet. Spilldata og kode produsert fra kommersielle spill har egne rettigheter. Følg prosjektets dokumenterte bruk av egne spillkopier og reglene til hvert dekompileringsprosjekt, også om AI-bidrag. Ingen bidrag er sendt til andre prosjekter.

## Bevarte kilder

Kopiene er hentet fra den festede originalrevisjonen og bevart uten endringer. Manifestet har byteantall, SHA-256 og Git blob-SHA; `scripts/verify.py` kontrollerer dem.

| Fil | Festet kilde | Lokal kopi |
|---|---|---|
| README.md | [GitHub](https://github.com/i12bp8/decomp.wtf/blob/575b4a30ed481ff5497dfb9ce4f599368a95a04a/README.md) | [Tekstkopi](../kilder/github/i12bp8--decomp.wtf/575b4a30ed481ff5497dfb9ce4f599368a95a04a/README.md.txt) |
| LICENSE | [GitHub](https://github.com/i12bp8/decomp.wtf/blob/575b4a30ed481ff5497dfb9ce4f599368a95a04a/LICENSE) | [Tekstkopi](../kilder/github/i12bp8--decomp.wtf/575b4a30ed481ff5497dfb9ce4f599368a95a04a/LICENSE.txt) |
| pyproject.toml | [GitHub](https://github.com/i12bp8/decomp.wtf/blob/575b4a30ed481ff5497dfb9ce4f599368a95a04a/pyproject.toml) | [Tekstkopi](../kilder/github/i12bp8--decomp.wtf/575b4a30ed481ff5497dfb9ce4f599368a95a04a/pyproject.toml.txt) |

[decompile-skillen ved samme revisjon](https://github.com/i12bp8/decomp.wtf/blob/575b4a30ed481ff5497dfb9ce4f599368a95a04a/plugins/decomp-wtf/skills/decompile/SKILL.md) er indeksert i [SKILLS.md](../SKILLS.md), både fra originalen og fra forken. De to oppføringene har samme dokumentinnhold. Skillen er ikke installert.

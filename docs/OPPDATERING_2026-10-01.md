# Oppdatering 1. oktober 2026

Sammenlignet med offentlig inventar fra 27. september: **åtte nye stjerner**, én navneendring og ett nytt eget offentlig repo. Totalt 44 stjerner og 29 egne offentlige repoer. Alle sider i de offentlige listene er lest.

## Nye stjerner

| Repo | Inngang |
|---|---|
| [Tencent-Hunyuan/AuK](https://github.com/Tencent-Hunyuan/AuK) | Talegenerering og redigering av tale. |
| [Tombonator3000/Loincloth-Legends](https://github.com/Tombonator3000/Loincloth-Legends) | Eget spill; fire skills for game-tests, new-level, prop-art og stage-forge. |
| [alphanu1/daytona-arcade-recomp](https://github.com/alphanu1/daytona-arcade-recomp) | Kildeprosjekt som må vurderes separat før gjenbruk; GitHub har ikke entydig lisensmetadata. |
| [collabs-inc/collab-public](https://github.com/collabs-inc/collab-public) | Agentarbeidsverktøy med collab-canvas-skill. |
| [kitao/pyxel](https://github.com/kitao/pyxel) | Retrospillmotor for Python. |
| [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder) | Ti skills for modding, assetarbeid, spillautomatisering og relaterte oppgaver. |
| [tigerless-labs/autoharness](https://github.com/tigerless-labs/autoharness) | Skilllaget for Claude Code, med learn-skill. |
| [xikhar/spiderbench](https://github.com/xikhar/spiderbench) | Referanserepo; ingen SKILL.md-filer funnet i den undersøkte revisjonen. |

`chaseleantj/desktop-habitats` er omdøpt til [chaseleantj/deskworlds](https://github.com/chaseleantj/deskworlds). GitHub-repo-id-en er den samme, så dette er ikke en ny stjerne eller en fjernet stjerne. Den historiske Desktop Habitats-profilen og kildekopiene er bevart.

## Skills

Alle 44 stjernerepoer er gjennomgått for SKILL.md. [Skilloversikten](../SKILLS.md) registrerer 187 filer fra 13 repoer, med 186 ulike dokumentinnhold. De 122 Scenario-produkt-skillsene er fortsatt med; antallet har ikke endret seg siden sist. Seks interne Scenario-hjelpere vises som repoarbeid.

De nye stjernerepoene gir 16 skillfiler: Universal Modder (10), AutoHarness (1), Collaborator (1) og Loincloth Legends (4). Den nye indeksen viser også tidligere uindekserte skills fra de eldre stjernerepoene, inkludert SIGNAL-47.

Den eksisterende personlige [Morbidium-spritesheets-skillen](../skills/morbidium-spritesheets/SKILL.md) er kopiert uendret som en komplett pakke med sju filer. Pakken inneholder frame-pakkeren, tre referanser, UI-metadata, ikon og SKILL.md. Kildefiler er kontrollert med SHA-256; den opprinnelige skillens frontmatter bestod valideringen. Dette oppdaterer bibliotekets kildepakke, ikke installasjonen av den allerede eksisterende skillen.

## Kontroll

- `build_catalog.py` viderefører de 46 historiske profilene.
- `build_skill_index.py` bygger skilldata og Markdown fra kildegjennomgangen.
- `verify.py` kontrollerer gamle og nye data, lokale lenker, festede skillkilder og kopierte skillfiler.
- Søk etter `prop-art` og `morbidium-spritesheets` finner de riktige skillene.

Katalogisering og strukturkontroll er ikke en runtime-test av de eksterne verktøyene. Innhentingen gjelder offentlig tilgjengelige stjerner; private stjerner er fortsatt utenfor denne API-tilgangen.

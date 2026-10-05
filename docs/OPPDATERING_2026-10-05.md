# Oppdatering 5. oktober 2026

Sammenlignet med inventaret fra torsdag 1. oktober: **12 nye offentlige stjerner**, **tre nye egne offentlige repoer** og **49 nye SKILL.md-stier** i skilloversikten. Ingen tidligere offentlige stjerner er fjernet eller omdøpt. Totalt **56 offentlige stjerner**, **32 egne offentlige repoer** og **236 skillfiler** med **215 ulike dokumentinnhold** fra 16 kilderepoer, samt den komplette personlige Morbidium-spritesheets-pakken.

Stjernedatoene er nå hentet fra GitHub og lagret i [inventaret](../data/offentlig-inventar.json). Elleve av tilleggene ble stjernemerket etter torsdag. Diablo 3DS ble lagt til torsdag kveld, etter torsdagens innhenting, og er også tatt med. Datoene nedenfor er i UTC.

## Nye stjerner

| Repo | Stjernemerket | Inngang |
|---|---|---|
| [achillean/shodan-python](https://github.com/achillean/shodan-python) | 4. oktober | Offisielt Python-bibliotek for Shodan. |
| [antoniaci/blackbird](https://github.com/antoniaci/blackbird) | 4. oktober | OSINT-verktøy for søk etter kontoer med brukernavn og e-post. |
| [bethington/ghidra-mcp](https://github.com/bethington/ghidra-mcp) | 5. oktober | MCP-integrasjon for Ghidra og reverse engineering. |
| [bhouston/three-dlss-nr](https://github.com/bhouston/three-dlss-nr) | 4. oktober | OpenDLSS-NR-port for Three.js, TSL og WebGPU. |
| [iamtechartist/obsidian](https://github.com/iamtechartist/obsidian) | 4. oktober | Prosedyregenerert Three.js-scene med fragmenter og formoverganger. |
| [Karolynaz/devil-3ds](https://github.com/Karolynaz/devil-3ds) | 1. oktober, 19:41:39 | Diablo-port for Nintendo 3DS basert på DevilutionX. |
| [laramies/theHarvester](https://github.com/laramies/theHarvester) | 4. oktober | OSINT-innsamling av e-post, underdomener og navn. |
| [NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra) | 5. oktober | Ghidras kildekode og verktøy for reverse engineering. |
| [neilsonnn/image-blaster](https://github.com/neilsonnn/image-blaster) | 4. oktober | Åtte skills for bilde-, 3D-, lyd- og verdenarbeid. |
| [OpenCloudGaming/OpenNOW](https://github.com/OpenCloudGaming/OpenNOW) | 5. oktober | GeForce Now-klient, med to skills for frontend og repoarbeid. |
| [smicallef/spiderfoot](https://github.com/smicallef/spiderfoot) | 4. oktober | Automatisert OSINT og kartlegging av angrepsflate. |
| [soxoj/maigret](https://github.com/soxoj/maigret) | 4. oktober | OSINT-verktøy for brukernavnsøk på nettsteder. |

Alle tilleggene er søkbare med `scripts/find.py`; [den komplette offentlige oversikten](../OFFENTLIG_INVENTAR.md) viser beskrivelser, lisensmetadata og nøyaktige stjernedatoer.

## Egne repoer

De nye egne offentlige repoene er [Jonesinthefastlane](https://github.com/Tombonator3000/Jonesinthefastlane), [Lula](https://github.com/Tombonator3000/Lula) og [MOONSTONE](https://github.com/Tombonator3000/MOONSTONE). De er tatt inn som egne kildekodereferanser selv om de ikke er stjernemerket.

Skillgjennomgangen omfatter nå både stjerner og egne offentlige repoer: **78 unike repoer**. To tidligere uindekserte skills fra Guild Life er dermed også med. Dette er utvidet dekning, ikke en påstand om at disse to skillene ble opprettet etter torsdag.

## Nye og endrede skills

| Kilde | Nye SKILL.md-stier i indeksen | Merknad |
|---|---:|---|
| Scenario | 17 | 14 Godot-skills og tre nye produkt-skills. |
| Image Blaster | 8 | 3d, image-edit, plate, project, sfx, uncover, wildcard og world. |
| OpenNOW | 2 | frontend-design og new-pr-and-branch. |
| Universal Modder | 20 | Ekstra kopier av ti eksisterende skills i `.agents` og `.claude`; de telles som filer, ikke som 20 nye ulike skills. |
| Guild Life Adventures | 2 | bug-hunt og test-game; funnet gjennom utvidelsen til alle egne offentlige repoer. |

Scenario har nå **139 produkt-skills**, pluss seks interne hjelpere. De nye Godot-skillene dekker expert, 2d, 3d-world, animation, architecture, audio, gameplay, multiplayer, performance-export, pipeline-automation, rendering-lighting, shaders, ui og vfx. De tre andre er **scenario-kinetic-music-video**, **scenario-side-view-game-kit** og **scenario-walkable-room**.

I tillegg er **23 eksisterende skillfiler endret** siden forrige kildeinnhenting: 17 i Scenario, fem i Universal Modder og én i VoiceStudio. [Skilloversikten](../SKILLS.md) og [skilldataene](../data/skills.json) peker til kontrollerte commits. De personlige skillene har ingen nye endringer etter torsdag; Morbidium-pakken er beholdt uendret.

## Dekning og kontroll

- Alle sider i offentlige stjerne- og repolister er lest; stjernedatoer er bevart.
- Alle 56 offentlige stjerner og 32 egne offentlige repoer er gjennomgått for SKILL.md, uten avkortede Git-trær.
- Commit og tilhørende tre er kontrollert for alle 78 kildeoppføringer.
- `build_catalog.py` viderefører de 46 historiske profilene. Tidligere innhentinger og kildetekster er bevart.
- `build_skill_index.py` bygger den samlede indeksen; `verify.py` kontrollerer dekning, datoer, kildelenker, lokale lenker og kontrollsummer.

Denne innhentingen dekker offentlige kilder. Private stjerner er ikke verifisert eller lagt inn; innloggingen venter på GitHubs tofaktorbekreftelse. Prosjektbiblioteket er fortsatt offentlig, og private oppføringer krever et privat mål. Katalogisering er ikke installasjon eller runtime-test av de eksterne prosjektene.

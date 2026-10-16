# Oppdatering 16. oktober 2026

Sammenlignet med inventaret fra 5. oktober: **20 nye offentlige stjerner**, **sju nye egne offentlige repoer** og **40 nye SKILL.md-stier**. Dagens inventar har **75 offentlige stjerner** og **37 egne offentlige repoer**. Én tidligere stjerneoppføring og to tidligere egne repooppføringer er ikke med i dagens offentlige API-svar; historiske notater er bevart.

Den nye [decomp.wtf-forken](https://github.com/Tombonator3000/decomp.wtf) er opprettet og kontrollert mot originalens siste `main`. [Gjennomgangen](../repoer/decomp-wtf-2026-10-16.md) dokumenterer arkivstatus, versjon 0.10.6, lisens og mulige gjenbruksområder.

## Nye stjerner

Stjernedatoene er hentet fra GitHub og oppgitt i UTC. Tillegg er sammenlignet med stabile repo-ID-er.

| Repo | Stjernemerket | Inngang |
|---|---|---|
| [ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender) | 6. oktober | Blender-kontroll via MCP. |
| [amathislab/terra](https://github.com/amathislab/terra) | 9. oktober | Terrengtilpasset rekonstruksjon, retargeting og styring av muskelskjelettbasert bevegelse. |
| [arielshad/3d-asset-server](https://github.com/arielshad/3d-asset-server) | 6. oktober | API og MCP for 3D-assets. |
| [BlueHeisenberg/SCSKiller](https://github.com/BlueHeisenberg/SCSKiller) | 12. oktober | Forhåndskompilering av spillshadere til GPU-driverens cache på Windows. |
| [EpicGames/unreal-engine-skills-for-claude-code-plugin](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin) | 11. oktober | Skills og MCP-arbeidsflyt for kontroll av Unreal Editor fra Claude Code. |
| [GLinnik21/plx-native](https://github.com/GLinnik21/plx-native) | 9. oktober | Uoffisiell Plex-klient for LG webOS med native grensesnitt. |
| [i12bp8/decomp.wtf](https://github.com/i12bp8/decomp.wtf) | 16. oktober | Lokal agentstyrt matching-dekompilering. Originalen er arkivert; egen fork er opprettet. |
| [joetsoi/OpenMoonstone](https://github.com/joetsoi/OpenMoonstone) | 12. oktober | Åpen nyimplementering av Moonstone: A Hard Day's Knight. |
| [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2) | 13. oktober | Generering av 3D med kompakte strukturerte latenter. |
| [morluto/rea](https://github.com/morluto/rea) | 6. oktober | Agentbasert reverse engineering av apper og native binærfiler. |
| [shader-effects-inc/shaders](https://github.com/shader-effects-inc/shaders) | 6. oktober | WebGPU-komponenter for flere webgrensesnitt og rammeverk. |
| [SimonSchubert/omalauncher](https://github.com/SimonSchubert/omalauncher) | 11. oktober | Android-launcher med agentbygde apper og widgets. |
| [snuri00/ps2-web-recomp](https://github.com/snuri00/ps2-web-recomp) | 14. oktober | Statisk rekompilering av PS2-spill til WebAssembly, med native runtime. |
| [snuri00/ps3recomp](https://github.com/snuri00/ps3recomp) | 14. oktober | Runtime-biblioteker for statisk rekompilering av PS3-titler. |
| [snuri00/psp-web-recomp](https://github.com/snuri00/psp-web-recomp) | 14. oktober | PSP-spill i nettleseren med WebAssembly, HLE-kjerne og WebGL2. |
| [snuri00/turbo-quant](https://github.com/snuri00/turbo-quant) | 14. oktober | Kvantisering av KV-cache for LLM-inferens. |
| [snuri00/turbo-quant-ios](https://github.com/snuri00/turbo-quant-ios) | 14. oktober | Metal-akselerert komprimering av KV-cache på Apple-enheter. |
| [storytold/photocraft](https://github.com/storytold/photocraft) | 6. oktober | Bilderedigering skrevet i Rust. |
| [TencentARC/AnimeSR](https://github.com/TencentARC/AnimeSR) | 16. oktober | Superoppløsning av animasjonsvideo. |
| [Tombonator3000/Dig-HD-Remake](https://github.com/Tombonator3000/Dig-HD-Remake) | 15. oktober | The Dig med HD-grafikk over originalen gjennom en ScummVM-patch. |

Alle tilleggene har norske gjenbruksnotater, kategorier og søkeord i [starred-notes.json](../data/starred-notes.json), og er søkbare med `scripts/find.py`. Søket leser nå også disse notatene for nye inventaroppføringer uten historisk profil. decomp.wtf-treffet peker til den egne gjennomgangen. [Det offentlige inventaret](../OFFENTLIG_INVENTAR.md) og [JSON-dataene](../data/offentlig-inventar.json) har fullstendige stjernetidspunkt, lisensmetadata og kildekodelenker. Arkiverte stjerner vises nå tydelig i inventaret.

## Egne offentlige repoer

Disse sju repoene er nye i inventaret: [DoD-Roguelite](https://github.com/Tombonator3000/DoD-Roguelite), [Sam-Max-HD](https://github.com/Tombonator3000/Sam-Max-HD), [Sam-Max-HD-Web](https://github.com/Tombonator3000/Sam-Max-HD-Web), [ZakMcKracken-HD](https://github.com/Tombonator3000/ZakMcKracken-HD), [Dig-HD-Remake](https://github.com/Tombonator3000/Dig-HD-Remake), [Dig-HD-Web](https://github.com/Tombonator3000/Dig-HD-Web) og [decomp.wtf](https://github.com/Tombonator3000/decomp.wtf). Dette er en endring i bibliotekets dekning, ikke en påstand om når repoene ble opprettet.

Løsningskort fra DoD-Roguelite, Sam-Max-HD, ZakMcKracken-HD og Dig-HD-Remake har nå offentlig opphav i inventaret. De midlertidige `offentlig_kontrollert`-feltene er fjernet der inventaret gir dekningen; testdatoer, bevis og festede commits er beholdt.

## Skills

[Skillmanifestet](../data/skill-sources.json) dekker **101 unike offentlige repoer** fra stjerner og egne repoer. 55 nye eller endrede kilder er hentet på nytt. [Oversikten](../SKILLS.md) har **274 SKILL.md-filer fra 26 repoer**, med **247 ulike dokumentinnhold**, samt den komplette personlige Morbidium-pakken.

| Kilde | Nye stier |
|---|---:|
| GLinnik21/plx-native | 12 |
| scenario-labs/skills | 8 |
| rehan-remade/universal-modder | 6 |
| morluto/rea | 4 |
| EpicGames/unreal-engine-skills-for-claude-code-plugin | 3 |
| arielshad/3d-asset-server | 1 |
| shader-effects-inc/shaders | 1 |
| i12bp8/decomp.wtf | 1 |
| Tombonator3000/decomp.wtf | 1 |
| Tombonator3000/Dig-HD-Remake | 1 |
| Tombonator3000/Sam-Max-HD | 1 |
| Tombonator3000/ZakMcKracken-HD | 1 |

To eldre Scenario-hjelperstier er erstattet, og innholdet i 46 eksisterende skillfiler er endret. Scenario har nå **144 produkt-skills og sju interne hjelpere**. De fem nye produkt-skillene er ad-variants, chatgpt-pet-create, chatgpt-pet-update, multi-reference og thumbnails. Filer i flere mapper og forker telles som filer; decomp.wtf-skillen i originalen og egen fork er samme dokumentinnhold.

## Kontroll

- Alle sider i de offentlige stjerne- og repolistene er hentet. Stjernene er også sammenlignet med den innloggede kontoens offentlige stjerner.
- Skillkildene har festede commits og uavkortede Git-trær. Tidligere kildereferanser og den personlige skillpakken er bevart.
- Den historiske katalogen med 46 profiler er beholdt. Det ferske inventaret og det egne decomp.wtf-notatet supplerer denne.
- `build_catalog.py`, `build_skill_index.py`, `build_solution_index.py` og `verify.py` er kjørt. decomp.wtf-kopiene omfattes nå av kontrollen av byteantall og kontrollsummer.

Innhentingen omfatter offentlige kilder. Ingen nye private opplysninger er lagt inn. Katalogisering, kildekontroll og opprettelse av en fork er ikke en runtime-test av verktøyene.

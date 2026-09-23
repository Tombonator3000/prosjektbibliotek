# Prosjektbibliotek

Privat referansebibliotek for **Tombonator3000**: spill, 3D, simulering, skills, agentverktøy og programmer som kan gjenbrukes på tvers av prosjekter.

**[Åpne hele katalogen](KATALOG.md)** · **[Alle GitHub-stjerner](STARRED.md)** · **[Søk og gjenbruk](docs/BRUK.md)**

Den første GitHub-samlingen, 23. september 2026, omfatter **46 unike repoer**: alle **22 stjernemerkede repoer** på kontoen, samt **24 øvrige referanser** fra tidligere dokumentert research. Alle 15 repoene i de fire vedlagte skjermbildene inngår. Det opprinnelige lokale biblioteket fra 13. september er videreført med Git-historikk og tidligere notater bevart.

## Finn det du trenger

| Område | Startpunkt |
|---|---|
| Skills, agentarbeid, Blender og Unity MCP | [Skills og agentverktøy](KATALOG.md#skills-og-agentverktøy) |
| Spillprosjekter, spillarkitektur og motorintegrasjon | [Spill og spillmotorer](KATALOG.md#spill-og-spillmotorer) |
| Vann, shaderkode, Three.js, WebGPU og splats | [3D og simulering](KATALOG.md#3d-og-simulering) |
| Musikkgenerering | [Lyd og musikk](KATALOG.md#lyd-og-musikk) |
| Verktøy, biblioteker, media og lokale tjenester | [Apper og egen drift](KATALOG.md#apper-og-egen-drift) |
| Egne spill og programmer | [Egne prosjekter](KATALOG.md#egne-prosjekter) |

Hvert repo har en norsk profil med formål, konkrete gjenbruksmuligheter, begrensninger, søkeord, lisensmetadata og festede kildelenker. README- og lisenskilder er bevart som tekst der de finnes, med dato og kontrollsummer. [JSON-katalogen](data/catalog.json) gir samme innhold for søk og senere automatisering.

## Tidligere gjennomganger

- [Ti verktøy fra Sentient](repoer/sentient-2026-09-12.md) – søk, arkivering, oversettelse, media og egen drift; originalinnlegget og repoene er lenket.
- [Kystvann, CUDA WebShader og WebGPU](repoer/coastal-webgpu-2026-09-20.md) – tekniske innganger, Unity-vurderinger, lisenser og festede versjoner.
- [Unity, Blender, skills og splat-research](docs/TIDLIGERE_RESEARCH.md) – tidligere prosjektkilder, tilpassede skills og avgrensede testresultater, med [bevart kildearkiv](docs/historikk/README.md).

Biblioteket er en referansesamling med utvalgte dokumentkilder. Hele upstream-kodebaser og modeller er ikke speilet. Ingen av prosjektene ble installert eller runtime-testet som del av denne innsamlingen; historiske tester beholder sin dato, revisjon og begrensning. Les [kildemetoden](docs/METODE.md) før du tolker en katalogoppføring som en integrasjonsanbefaling.

## Lokal bruk og oppdatering

```sh
python3 scripts/find.py vann
python3 scripts/find.py --category 'Skills og agentverktøy'

# Hent stjerner/kilder, bygg katalog og kontroller resultatet:
python3 scripts/sync_github.py
python3 scripts/build_catalog.py
python3 scripts/verify.py
```

Krever Python 3.10+ og innlogget GitHub CLI for ny innhenting; søk og katalogbygging fungerer offline. [Bruksveiledningen](docs/BRUK.md) forklarer notater, nye referanser og oppdatering. Se [utført kontroll](docs/VERIFISERING.md) for første samling. Ingen automatisk synkronisering er satt opp. Biblioteket skal beholde privat synlighet.

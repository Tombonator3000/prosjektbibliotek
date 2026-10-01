# Prosjektbibliotek

Referansebibliotek for **Tombonator3000**: spill, 3D, simulering, skills, agentverktøy og programmer som kan gjenbrukes på tvers av prosjekter.

**[Stjerner og egne repoer](OFFENTLIG_INVENTAR.md)** · **[Samlet skilloversikt](SKILLS.md)** · **[Kuraterte profiler](KATALOG.md)** · **[Søk og gjenbruk](docs/BRUK.md)**

Oppdatert **1. oktober 2026**: **44 offentlige stjerner**, **29 egne offentlige repoer**, **187 SKILL.md-filer fra 13 stjernerepoer** og den komplette egne **Morbidium-spritesheets-pakken**. Av skillfilene er 122 Scenario-skills og seks Scenario-hjelpere for internt repoarbeid. Én skilltekst finnes i to filer, så de 187 filene har 186 ulike dokumentinnhold. [Se hva som er nytt](docs/OPPDATERING_2026-10-01.md).

[Maskinlesbart inventar](data/offentlig-inventar.json), [skilldata](data/skills.json) og oppdateringsskriptene følger med. Kildekode ligger i de lenkede originalrepoene; skillkildene er festet til kontrollerte commits. Private repoer og private stjerner er ikke med i den offentlige oversikten. `scripts/find.py` søker nå i den historiske katalogen, det ferske inventaret og skills.

Den første kuraterte GitHub-samlingen, 23. september 2026, omfatter **46 unike repoer**: **22 repoer som da var stjernemerket**, samt **24 øvrige referanser** fra tidligere dokumentert research. [STARRED.md](STARRED.md) er en datert historisk liste. Det opprinnelige lokale biblioteket fra 13. september er videreført med Git-historikk og tidligere notater bevart.

## Finn det du trenger

| Område | Startpunkt |
|---|---|
| Skills, agentarbeid, Blender og Unity MCP | [Samlet skilloversikt](SKILLS.md) |
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
python3 scripts/find.py prop-art
python3 scripts/find.py morbidium-spritesheets

# Hent stjerner/kilder, bygg katalog og kontroller resultatet:
python3 scripts/sync_github.py
python3 scripts/build_catalog.py
python3 scripts/verify.py

# Oppdater offentlig inventar (krever ikke innlogging):
python3 scripts/sync_public_inventory.py
python3 scripts/build_skill_index.py --refresh
python3 scripts/verify.py
```

Den historiske kuraterte innhentingen krever Python 3.10+ og innlogget GitHub CLI; offentlig inventar bruker kun Python 3.10+ og offentlig GitHub API. Søk og katalogbygging fungerer offline. [Bruksveiledningen](docs/BRUK.md) forklarer notater, nye referanser og oppdatering. Se [utført kontroll](docs/VERIFISERING.md) for første samling. Ingen automatisk synkronisering er satt opp. GitHub oppgir nå dette repoet som offentlig; ikke legg inn nye private opplysninger her uten å endre synligheten først.

# Kilder, fullstendighet og bevisstatus

Biblioteket ble samlet 23. september 2026 fra tre grunnlag:

1. Hele starlisten til den autentiserte GitHub-kontoen Tombonator3000, via [GET /user/starred](https://docs.github.com/en/rest/activity/starring#list-repositories-starred-by-the-authenticated-user), med `application/vnd.github.star+json`, 100 resultater per side og gjennomgang til siste side. Dette gir star-tidspunkt og tilgjengelige private repoer. [Innhentingsmanifest](../data/github.json) registrerer konto, tid, sider og repo-id-er.
2. Det eksisterende lokale prosjektbiblioteket: [Sentients ti verktøy](../repoer/sentient-2026-09-12.md) og [tre kyst-/WebGPU-repoer](../repoer/coastal-webgpu-2026-09-20.md), med originalkilder, vurderinger og lisenskopier bevart. Historikken er videreført i samme Git-repo.
3. [Tidligere prosjekt- og skillresearch](TIDLIGERE_RESEARCH.md), bevart med egne kildedatoer og versjoner. Dette er et avgrenset funn fra tilgjengelige dokumenter, ikke en påstand om at alle tidligere samtaler eller eksterne kontoer er arkivert.

De fire skjermbildene i bestillingen viser 15 repoer. [Avskrevet bildereferanse](../data/screenshot-references.json) brukes som tilleggskontroll mot API-listen. API-listen inneholder også stjerner som ikke er vist i bildene.

## Dokumentkilder

For hvert repo hentes gjeldende metadata, standardgrenens commit, README og gjenkjennelige lisens-/notice-/credits-filer i roten. `MODEL_LICENSE` tas også med der den finnes. Dokumentene lagres byte-identisk med `.txt`-suffiks i `kilder/github/`, med kildelenke, Git-blob-id, SHA-256 og filstørrelse i manifestet. Tidligere kildetekster bevares under sin commit ved ny innhenting.

Dette er et referansebibliotek med utvalgte dokumentkilder; hele kodebaser, Git-historikk, datasett, modeller og bildevedlegg fra upstream er ikke speilet. Underkomponenter kan ha egne lisenser som må leses ved faktisk bruk. Manglende eller ikke entydig identifisert GitHub-lisensfelt betyr at lisensgrunnlaget må undersøkes, ikke at materialet er fritt for vilkår. Bevarte tredjepartstekster beholder sine respektive vilkår og opphavsangivelser; biblioteket gir dem ingen ny felles lisens.

Kildeinnhenting og kategorisering er ikke en runtime-test. `runtime_tested_in_this_catalog: false` gjelder samtlige oppføringer. Historiske Blender-/Unity-resultater står i sine daterte notater med feil, begrensninger og revisjoner bevart.

## Kontroll av leveransen

`python3 scripts/verify.py` sammenligner star-id-er med katalogen, oppdager duplikater, kontrollerer profiler, lokale lenker og kildehashverdier. Den kontrollerer dokumentstruktur og bevarte bytes; den beviser ikke at upstream-programmer fungerer, at alle eksterne lenker alltid vil bestå eller at alle lisensvilkår er juridisk vurdert.

GitHub-repoet er opprettet privat på brukerens uttrykkelige bestilling. Referanser til private prosjekter og historiske lokale arbeidsstier inngår derfor bare i dette private biblioteket. Ingen credentials eller `.env`-filer inngår.

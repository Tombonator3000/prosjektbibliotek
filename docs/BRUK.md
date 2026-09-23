# Finn og gjenbruk en referanse

Åpne [katalogen](../KATALOG.md) og velg kategori, eller søk i det lokale biblioteket:

```sh
python3 scripts/find.py vann
python3 scripts/find.py Blender
python3 scripts/find.py --category 'Skills og agentverktøy'
```

Hver [prosjektprofil](../repoer/prosjekter/) har norsk formål, mulig gjenbruk, begrensninger, kildelenker, valgt commit, dato og bevarte README-/lisenskilder. GitHubs globale stjernetall er lagret som datert metadata i [JSON-katalogen](../data/catalog.json); det er ingen kvalitetsmåling.

Ved oppstart av et annet prosjekt kan du be:

> Bruk Tombonator3000/prosjektbibliotek som referanse. Finn relevante kandidater for [behov], les gjenbruksnotatene og de festede kildene, og vurder dem mot prosjektets eksisterende stack. Bruk tidligere tester kun for den dokumenterte revisjonen og maskinen.

Gjenbruk skjer i det nye prosjektet: velg en konkret komponent eller idé, les lisensen ved valgt revisjon, bevar opphav, tilpass til eksisterende stack og prøv én representativ integrasjon. Three.js-/WebGPU-demoer er ofte algoritme- og visuelle referanser for Unity; filene er ikke automatisk Unity-pakker. En samling spill eller skills er heller ikke i seg selv en spillmotor.

## Oppdater biblioteket

Fra repoets rot, med Python 3 og GitHub CLI innlogget på Tombonator3000:

```sh
python3 scripts/sync_github.py
python3 scripts/build_catalog.py
python3 scripts/verify.py
git diff --stat
git diff -- KATALOG.md STARRED.md
```

Synkronisering henter alle sider fra den innloggede kontoens star-endepunkt, også tilgjengelige private repoer. Den beholder tidligere lagrede referanser hvis en stjerne senere fjernes, og bevarer norske notater. Kildetekster lagres per commit. Ved nettverks-/tilgangsfeil beholdes forrige katalog, og feil rapporteres; kjør på nytt etter at årsaken er løst.

Nye stjerner får automatisk profiler, men står som **Uklassifisert** fram til det finnes norske notater. Rediger `data/starred-notes.json` for starrepoer og `data/extra-notes.json` for øvrige tilleggsreferanser. Legg ekstra repo-id og lokal provenienskilde i `data/extra-references.json`. De opprinnelige Sentient-/WebGPU-notatene under `repoer/` bevares som historikk.

Genererte filer er `KATALOG.md`, `STARRED.md`, `data/catalog.json` og `repoer/prosjekter/*.md`. Endre kildenotatene og bygg igjen. Synkroniseringsskriptet gjør bare GitHub-lesinger og lokale filskrivinger; det oppretter ingen GitHub-commit, publiserer ingenting og installerer ingen av verktøyene. Commit og push gjøres eksplisitt etter kontroll. Ingen automatisk tidsplan er aktivert.

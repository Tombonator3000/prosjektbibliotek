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

## Løsningskort

Løsningskortene er det Tom og agentene har lært i egne spill: et problem, hvorfor det skjer, hva som løser det og hvordan det sjekkes. Målet er at neste prosjekt finner løsningen her i stedet for å lete på nytt. Oversikten står i [LOSNINGER.md](../LOSNINGER.md).

**Finn et kort.** `python3 scripts/find.py <ord>` søker i tittel, symptom, løsning, fallgruver, stikkord, stack og opphav. `--category Løsningskort` viser bare kortene.

**Skriv et kort** når et problem er løst eller en teknikk er tatt i bruk i et av Toms offentlige repoer:

1. Kopier [malen](../losninger/MAL.md) til `losninger/<domene>/<id>.md`. Domenene er `grafikk`, `lyd`, `testing`, `ui`, `bygg` og `regler`.
2. Fyll ut nøkkelblokken og alle seksjonene: Symptom, Årsak, Løsning, Fallgruver, Slik verifiseres det, Bevis og Brukt i.
3. Fest opphavet til en hel commit: `eier/repo@<40 tegn>:sti#Llinje`. Lenker i Bevis bør også være festet til en commit, med `?plain=1#L<linje>` for Markdown-filer.
4. Kjør `python3 scripts/build_solution_index.py` og `python3 scripts/verify.py`.

**Status** gjelder opphavsprosjektet på datoen i kortet:

- PASS: sjekket der, og Bevis viser hvordan.
- FAIL: prøvd og virket ikke. Det er like nyttig å vite.
- UNVERIFIED: funnet i kode eller notater uten at testen er sett.

Biblioteket kjører ikke koden selv. Den som tar en løsning inn i et annet prosjekt, må sjekke versjon, lisens og prosjektets rammer, og verifisere der.

**Bare offentlige repoer.** Biblioteket er offentlig. `verify.py` godtar bare kort der opphavet står i det offentlige inventaret, eller der `offentlig_kontrollert` sier når noen så at repoet var offentlig. Det siste er ment for repoer som er nyere enn siste synkronisering av inventaret. Løsninger fra private repoer skrives i det private repoets egen `docs/losninger/`.

`data/losninger.json` og `LOSNINGER.md` er generert fra kortene. Endre kortene, ikke de genererte filene. Skillen `spill-gjenbruk` i Toms Claude-konto leser kortene før arbeid i et spill og skriver nye kort etterpå.


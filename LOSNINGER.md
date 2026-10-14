# Løsningskort

Løste problemer og teknikker fra Toms egne spill, skrevet så neste prosjekt kan bruke dem i stedet for å finne dem på nytt. Hvert kort sier hva man ser, hvorfor det skjer, hva som løser det, hvordan det sjekkes og hvor det kommer fra.

**24 kort.** PASS: 19 · FAIL: 0 · UNVERIFIED: 5

[Startside](README.md) · [Mal for nye kort](losninger/MAL.md) · [JSON](data/losninger.json) · [Slik skriver du et kort](docs/BRUK.md#løsningskort)

Status gjelder opphavsprosjektet på datoen i kortet: PASS er sjekket der, FAIL er prøvd og virket ikke, UNVERIFIED er funnet i kode eller notater uten at testen er sett. Biblioteket kjører ikke koden selv. Sjekk versjon, lisens og prosjektets rammer før du tar noe inn, og verifiser i ditt eget prosjekt.

```sh
python3 scripts/find.py msaa
python3 scripts/find.py --category Løsningskort
```

## Grafikk

| Kort | Status | Stack | Opphav | Sist sjekket |
|---|---|---|---|---|
| [Bloom som bare gløder på lys og ild](losninger/grafikk/bloom-terskel-over-en.md) | PASS | three.js r170, UnrealBloomPass før OutputPass, ACES-tonekurve | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/main.js#L1191) | 2026-10-09 |
| [Figurer fra KI-tegnede ark skifter størrelse mellom rutene](losninger/grafikk/figurark-fast-storrelse.md) | PASS | ScummVM med HD-patch (DigHD), Python-pipeline med numpy og Pillow, figurark 1536 x 1024 i glatt stil med ekte alfa | [Dig-HD-Remake@091a953](https://github.com/Tombonator3000/Dig-HD-Remake/blob/091a953b89b522c6d45478315aecefa6dbab1d75/pipeline/dighd/myk.py#L236) | 2026-10-13 |
| [InstancedMesh blir svart når fargelista lages mens count er 0](losninger/grafikk/instancedmesh-fargeliste-ved-count-null.md) | UNVERIFIED | three.js r128 og nyere, InstancedMesh | [morbidium@729219c](https://github.com/Tombonator3000/morbidium/blob/729219ceb3e77119179deadb9fbfcd25bd8b2a4a/logg/2026-09.md#L1092) | 2026-10-09 |
| [Kroker for lys per lyskilde i lights_fragment_begin (r170)](losninger/grafikk/lyskroker-lights-fragment-begin-r170.md) | UNVERIFIED | three.js r170, MeshStandardMaterial | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/memory.md#L212) | 2026-10-09 |
| [Myke trekroner med AO i hjørnefargene](losninger/grafikk/myke-trekroner-med-vertex-ao.md) | PASS | three.js r170, InstancedMesh med setColorAt, BufferGeometryUtils.mergeVertices | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/treegeo.js#L29) | 2026-10-09 |
| [Flere shaderendringer på samme materiale med onBeforeCompile](losninger/grafikk/onbeforecompile-i-kjede.md) | PASS | three.js r170, MeshStandardMaterial med onBeforeCompile | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/wet.js#L27) | 2026-10-09 |
| [Miljøkart fra en enkel himmelkule](losninger/grafikk/pmrem-miljokart-fra-himmelkule.md) | PASS | three.js r170, MeshStandardMaterial, scene.environment og scene.environmentIntensity | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/envlight.js#L58) | 2026-10-09 |
| [Regnstreker med fast bredde i piksler](losninger/grafikk/regnstreker-fast-pikselbredde.md) | PASS | three.js r170, ShaderMaterial, instanserte flater bygget i skjermrommet | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/weather.js#L103) | 2026-10-09 |
| [Magenta skygger og kjempestore ruter i SCUMM v6-kostymer](losninger/grafikk/scumm-v6-kostymer-skygge-og-soppelruter.md) | PASS | SCUMM v6 (Sam & Max Hit the Road), ScummVM c9091321, egne Python-dekodere for COST (format 0x58 til 0x61) | [Sam-Max-HD@ef9c441](https://github.com/Tombonator3000/Sam-Max-HD/blob/ef9c4414562aa73700e2bb9ec06355cebb1c6b42/pipeline/smhd/figur.py#L306) | 2026-10-13 |
| [Kantutjevning når three.js tegner gjennom EffectComposer](losninger/grafikk/three-r170-composer-msaa.md) | PASS | three.js r170, WebGL2, EffectComposer med RenderPass, UnrealBloomPass og OutputPass | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/main.js#L231) | 2026-10-09 |
| [Uniformlister må ha verdier før første render](losninger/grafikk/uniformlister-for-forste-render.md) | PASS | three.js r170, ShaderMaterial med lister som uniform vec4 uRip[8] | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/water.js#L102) | 2026-10-09 |
| [vertexColors uten fargeattributt blir svart](losninger/grafikk/vertexcolors-uten-fargeattributt.md) | UNVERIFIED | three.js r170, WebGL2, MeshStandardMaterial med vertexColors | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/treegeo.js#L29) | 2026-10-09 |
| [Når WebGL-konteksten blir borte](losninger/grafikk/webgl-kontekst-tapt.md) | UNVERIFIED | three.js r128 og nyere, WebGL | [morbidium@729219c](https://github.com/Tombonator3000/morbidium/blob/729219ceb3e77119179deadb9fbfcd25bd8b2a4a/src/04_render.js#L57) | 2026-10-09 |

## Lyd og musikk

| Kort | Status | Stack | Opphav | Sist sjekket |
|---|---|---|---|---|
| [Prosedyrisk lutt med Karplus-Strong og en sequencer med lookahead](losninger/lyd/karplus-strong-lutt-med-lookahead.md) | PASS | WebAudio API i nettleseren, uten lydfiler | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/music.js#L259) | 2026-10-09 |

## Testing og verifikasjon

| Kort | Status | Stack | Opphav | Sist sjekket |
|---|---|---|---|---|
| [Bilder før og etter en grafikkendring med git worktree](losninger/testing/bilder-for-og-etter-med-worktree.md) | PASS | git, Node-bygg, Playwright-testrigg | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/memory.md#L174) | 2026-10-09 |
| [Hvilke figurruter og objekter mangler faktisk HD når spillet spilles](losninger/testing/logg-over-det-som-mangler-hd.md) | PASS | ScummVM med HD-patch (DigHD) for SCUMM v7, C++11, motoren bygger HD-bildet per piksel fra kilder (rom, objekt, rute, film) | [Dig-HD-Remake@6221c6e](https://github.com/Tombonator3000/Dig-HD-Remake/blob/6221c6eecd0ca3071c5b5adfdd1b48c115ee7c0f/engine/patches/0001-dighd-hd-grafikk.patch#L4509) | 2026-10-15 |
| [Teste en Pages-nettside som henter filer fra GitHub-API-et, fra Claude-sandkassen](losninger/testing/nettside-med-github-api-i-sandkassen.md) | PASS | Playwright for Python med headless Chromium 141, en side på github.io som henter spillfiler med fetch fra api.github.com (git/trees og git/blobs) med en lesenøkkel | [ZakMcKracken-HD@7147a72](https://github.com/Tombonator3000/ZakMcKracken-HD/blob/7147a72e2522124c3c5a5874c5e0ce65dcb28db3/tools/nettsidetest.py#L51) | 2026-10-14 |
| [Nettleserttester av three.js-spill uten skjermkort og uten nett](losninger/testing/playwright-swiftshader-three-lokalt.md) | PASS | Playwright med headless Chromium, three.js fra jsdelivr via importmap | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/tools/test/shot.mjs#L20) | 2026-10-09 |

## Brukerflate

| Kort | Status | Stack | Opphav | Sist sjekket |
|---|---|---|---|---|
| [Høye paneler mister toppen når skjermen sentreres med grid](losninger/ui/grid-skjerm-klipper-toppen.md) | PASS | CSS grid, fullskjerms overlegg med overflow-y: auto | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/page.html#L853) | 2026-10-09 |
| [hidden virker ikke på elementer med display: grid](losninger/ui/hidden-attributt-med-display-grid.md) | PASS | HTML og CSS | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/page.html#L26) | 2026-10-09 |
| [Skrifter som virker offline og i en streng CSP](losninger/ui/skrifter-med-fontface.md) | UNVERIFIED | Nettleser, FontFace API, én HTML-fil | [SIGNAL-47@925d613](https://github.com/Tombonator3000/SIGNAL-47/blob/925d61336e95abb9310646be0e0de77271ad0f4a/web/src/core/fonts.ts#L6) | 2026-10-09 |

## Bygg og levering

| Kort | Status | Stack | Opphav | Sist sjekket |
|---|---|---|---|---|
| [Hele spillet i én HTML-fil uten fetch](losninger/bygg/en-html-fil-uten-fetch.md) | PASS | esbuild, three.js r170 fra jsdelivr via importmap, Claude-artifact og GitHub Pages | [DoD-Roguelite@5e940d2](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/build.mjs#L30) | 2026-10-09 |
| [Alle spillene på GitHub Pages deler localStorage](losninger/bygg/pages-deler-localstorage.md) | PASS | Nettleser, GitHub Pages under tombonator3000.github.io | [SIGNAL-47@925d613](https://github.com/Tombonator3000/SIGNAL-47/blob/925d61336e95abb9310646be0e0de77271ad0f4a/web/memory.md#L166) | 2026-10-09 |
| [En ny bygging av HD-modden visker ut rettinger som bare finnes i den publiserte](losninger/bygg/publisert-mod-er-fasit.md) | PASS | ScummVM med HD-patch (DigHD), Python-pipeline (dighd), modden i en egen git-gren med én commit som erstattes (hd-mod), flere agenter som leverer til samme mod | [Dig-HD-Remake@b612c31](https://github.com/Tombonator3000/Dig-HD-Remake/blob/b612c3151838b5b2e117b49343582b7577e107a4/pipeline/dighd/modflett.py#L115) | 2026-10-15 |

## Nytt kort

Kopier [malen](losninger/MAL.md) til `losninger/<domene>/<id>.md`, fyll ut, og kjør:

```sh
python3 scripts/build_solution_index.py
python3 scripts/verify.py
```

Bare innhold fra offentlige repoer hører hjemme her. Denne siden er generert; endre kortene, ikke denne fila.

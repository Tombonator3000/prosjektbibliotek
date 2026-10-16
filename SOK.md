# Samlet søkeoversikt

397 søkeoppføringer for løsningskort, repoer og unike skillinnhold. Like skillkopier er samlet; alle kildeplasseringene står i JSON-indeksen.

[Start her](START_HER.md) · [JSON](data/search-index.json) · [Søkeord og synonymer](data/search-terms.json)

Søk selektivt etter behov, symptomer og teknologi. Åpne kilden før gjenbruk. Nøkkelord og relaterte søkeord er hjelp til gjenfinning, ikke bevis på kompatibilitet. PASS gjelder dokumentert test i opphavet. Historiske oppføringer beholder opprinnelig kildeversjon.

## Løsningskort

### løsning/bygg/en-html-fil-uten-fetch

Hele spillet i én HTML-fil uten fetch

Status: PASS. Stack: esbuild, three.js r170 fra jsdelivr via importmap, Claude-artifact og GitHub Pages.

Mulig gjenbruk: - Bygg med esbuild til én fil. - Legg modeller, teksturer og bilder inn som base64: data-URI-er for bilder, og globale variabler for binærdata. - Hent three.js fra jsdelivr med en importmap, med eksakt versjon. - Lag to utgaver: `index.html` (vanlig side) og `artifact.html` uten doctype og head, for publisering.

Søkeord: artifact, base64, budsjett, data-URI, esbuild, fetch blokkert, importmap, model, modell, modeller, models, offline, sandkasse, single file, tekstur, teksturer, texture, textures, three js, three.js, threejs, én fil

[Profil eller kort](losninger/bygg/en-html-fil-uten-fetch.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/bygg/en-html-fil-uten-fetch.md)

### løsning/bygg/pages-deler-localstorage

Alle spillene på GitHub Pages deler localStorage

Status: PASS. Stack: Nettleser, GitHub Pages under tombonator3000.github.io.

Mulig gjenbruk: - Gi alle nøkler et prefiks per spill, for eksempel `s47.` eller `svartnebb.`. - Legg store ting, som bilder og miniatyrer, i IndexedDB i stedet. - Fang feil ved skriving, og si fra til spilleren i stedet for å miste lagringen.

Søkeord: browser, GitHub Pages, kvote, lagre, lagring, localStorage, nettleser, nøkler, opphav, origin, persistence, prefiks, QuotaExceededError, save, saving, web

[Profil eller kort](losninger/bygg/pages-deler-localstorage.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/bygg/pages-deler-localstorage.md)

### løsning/bygg/publisert-mod-er-fasit

En ny bygging av HD-modden visker ut rettinger som bare finnes i den publiserte

Status: PASS. Stack: ScummVM med HD-patch (DigHD), Python-pipeline (dighd), modden i en egen git-gren med én commit som erstattes (hd-mod), flere agenter som leverer til samme mod.

Mulig gjenbruk: Den publiserte modden er fasit. Runden bygger en kandidat som før, henter den publiserte og fletter:

Søkeord: character, characters, figur, figurer, flett, fletting, force push, HD remake, hd-mod, mod, modpakke, overrides, overstyringer, regresjon, rettinger forsvinner, ScummVM, SHA256SUMS, sjekksummer, tvangspush

[Profil eller kort](losninger/bygg/publisert-mod-er-fasit.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/bygg/publisert-mod-er-fasit.md)

### løsning/grafikk/bloom-terskel-over-en

Bloom som bare gløder på lys og ild

Status: PASS. Stack: three.js r170, UnrealBloomPass før OutputPass, ACES-tonekurve.

Mulig gjenbruk: - Sett terskelen over 1, så bare det som er lysere enn hvitt i HDR gløder. - Gi lamper, ild, vinduer om natta og magi emissive over 1, så de fortsatt gløder. - La terskelen og styrken følge stedet og tiden:

Søkeord: bloom, dis, emissive, gloed, glow, glowing, glød, gløder, grøtete, HDR, overeksponert, terskel, three js, three.js, threejs, threshold, UnrealBloomPass

[Profil eller kort](losninger/grafikk/bloom-terskel-over-en.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/grafikk/bloom-terskel-over-en.md)

### løsning/grafikk/figurark-fast-storrelse

Figurer fra KI-tegnede ark skifter størrelse mellom rutene

Status: PASS. Stack: ScummVM med HD-patch (DigHD), Python-pipeline med numpy og Pillow, figurark 1536 x 1024 i glatt stil med ekte alfa.

Mulig gjenbruk: 1. Mottaket: tilpass hver rute til originalens omriss i bredde og høyde for seg, innenfor et lite spenn rundt gruppens faktor, og bruk det bare når overlappet med originalen ikke blir tydelig dårligere.

Søkeord: alfa, alpha, character, character sheet, characters, ChatGPT, Codex, fast rutestørrelse, figur, figurark, figurer, flimrer, frame dimensions, gjennomsiktig, gjennomsiktighet, HD remake, hode for stort, myk.py, myke figurer, ScummVM, skala, sprite sheet, sprite sheets, spriteark, spritesheet, spritesheets, størrelse, transparency, transparent

[Profil eller kort](losninger/grafikk/figurark-fast-storrelse.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/grafikk/figurark-fast-storrelse.md)

### løsning/grafikk/instancedmesh-fargeliste-ved-count-null

InstancedMesh blir svart når fargelista lages mens count er 0

Status: UNVERIFIED. Stack: three.js r128 og nyere, InstancedMesh.

Mulig gjenbruk: Lag fargelista for full kapasitet før du setter `count` ned, eller lag den selv:

Søkeord: black, count, farge, instanceColor, InstancedMesh, partikler, setColorAt, svart, three js, three.js, threejs

[Profil eller kort](losninger/grafikk/instancedmesh-fargeliste-ved-count-null.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/grafikk/instancedmesh-fargeliste-ved-count-null.md)

### løsning/grafikk/lyskroker-lights-fragment-begin-r170

Kroker for lys per lyskilde i lights_fragment_begin (r170)

Status: UNVERIFIED. Stack: three.js r170, MeshStandardMaterial.

Mulig gjenbruk: Linjene i r170 som det går an å henge noe på:

Søkeord: directLight, getDirectionalLightInfo, getSpotLightInfo, lights_fragment_begin, onBeforeCompile, shader, ShaderChunk, shaders, shadow, shadows, skygge, skyggelegger, skygger, skyskygger, three js, three.js, threejs

[Profil eller kort](losninger/grafikk/lyskroker-lights-fragment-begin-r170.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/grafikk/lyskroker-lights-fragment-begin-r170.md)

### løsning/grafikk/myke-trekroner-med-vertex-ao

Myke trekroner med AO i hjørnefargene

Status: PASS. Stack: three.js r170, InstancedMesh med setColorAt, BufferGeometryUtils.mergeVertices.

Mulig gjenbruk: - Slå sammen hjørnene med `mergeVertices`, og forskyv dem med støy som bare avhenger av posisjonen. Da flytter like hjørner seg likt, og det blir ingen sprekker. - Regn normalene på nytt, og vri dem 55 prosent mot retningen ut fra midten, så lyset faller mykt over kronen. - Legg AO i en fargeattributt: mørkere nederst og i gropene, lysere øverst, o

Søkeord: AO, facetter, flatShading, ikosaeder, InstancedMesh, low poly, mergeVertices, plast, three js, three.js, threejs, trekroner, trær, vertexColors

[Profil eller kort](losninger/grafikk/myke-trekroner-med-vertex-ao.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/grafikk/myke-trekroner-med-vertex-ao.md)

### løsning/grafikk/onbeforecompile-i-kjede

Flere shaderendringer på samme materiale med onBeforeCompile

Status: PASS. Stack: three.js r170, MeshStandardMaterial med onBeforeCompile.

Mulig gjenbruk: Kjed funksjonene og nøklene:

Søkeord: customProgramCacheKey, cutaway, feil program, MeshStandardMaterial, onBeforeCompile, overskrives, patch, shader, shaders, skyggelegger, sway, three js, three.js, threejs, wetness

[Profil eller kort](losninger/grafikk/onbeforecompile-i-kjede.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/grafikk/onbeforecompile-i-kjede.md)

### løsning/grafikk/pmrem-miljokart-fra-himmelkule

Miljøkart fra en enkel himmelkule

Status: PASS. Stack: three.js r170, MeshStandardMaterial, scene.environment og scene.environmentIntensity.

Mulig gjenbruk: - Lag en kule med farger fra himmelen: toppen, horisonten og bakken, pluss en myk solflekk i samme retning som sola. - Gjør den om til PMREM, og sett den som `scene.environment`. - Hold styrken lav, så sola og fyllyset fortsatt bærer bildet: rundt 0,3 om dagen og 0,08 om natta. Bruk ikke noe miljøkart i mørke kjellere og huler. - Bygg kartet på nyt

Søkeord: environment, environmentIntensity, glans, matt, MeshStandardMaterial, miljøkart, plast, PMREM, PMREMGenerator, reflection, reflections, refleksjon, refleksjoner, scene, scener, scenes, three js, three.js, threejs

[Profil eller kort](losninger/grafikk/pmrem-miljokart-fra-himmelkule.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/grafikk/pmrem-miljokart-fra-himmelkule.md)

### løsning/grafikk/regnstreker-fast-pikselbredde

Regnstreker med fast bredde i piksler

Status: PASS. Stack: three.js r170, ShaderMaterial, instanserte flater bygget i skjermrommet.

Mulig gjenbruk: Bygg streken i klipprommet og gi den en fast bredde i piksler, ganget med `w` så den ikke krymper med avstanden. Bruk `DoubleSide`.

Søkeord: billboard, bredde, DoubleSide, dråper, enorme, forsvinner, partikler, regn, regnstreker, shader, shaders, skjermrom, skyggelegger, three js, three.js, threejs

[Profil eller kort](losninger/grafikk/regnstreker-fast-pikselbredde.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/grafikk/regnstreker-fast-pikselbredde.md)

### løsning/grafikk/scumm-v6-kostymer-skygge-og-soppelruter

Magenta skygger og kjempestore ruter i SCUMM v6-kostymer

Status: PASS. Stack: SCUMM v6 (Sam & Max Hit the Road), ScummVM c9091321, egne Python-dekodere for COST (format 0x58 til 0x61).

Mulig gjenbruk: Les indeksbildet (`_idx.png`) ved siden av RGBA-bildet og fjern skyggepikslene før ruten går på arket; hopp over kostymer som da blir tomme. Sett en øvre grense for rutestørrelse (ekte ruter er høyst 320 x 200):

Søkeord: character, character sheet, characters, COST, figur, figurark, figurer, garbage cels, klassiske kostymer, magenta, palettindeks 13, rosa, Sam & Max, SCUMM, ScummVM, shadow, shadow table, shadows, skygge, skygger, speilvending, sprite sheet, sprite sheets, spriteark, spritesheet, spritesheets, søppelruter

[Profil eller kort](losninger/grafikk/scumm-v6-kostymer-skygge-og-soppelruter.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/grafikk/scumm-v6-kostymer-skygge-og-soppelruter.md)

### løsning/grafikk/three-r170-composer-msaa

Kantutjevning når three.js tegner gjennom EffectComposer

Status: PASS. Stack: three.js r170, WebGL2, EffectComposer med RenderPass, UnrealBloomPass og OutputPass.

Mulig gjenbruk: Gi komposeren en target med `samples`, og ta `antialias` av rendereren, siden den bare koster minne:

Søkeord: aliasing, anti alias, anti aliasing, antialias, antialiasing, character, characters, EffectComposer, figur, figurer, FXAA, hakkete kanter, HalfFloat, kantutjevning, MSAA, r170, samples, shadow, shadows, skygge, skygger, SMAA, TAA, three js, three.js, three.js r170, threejs, WebGL2

[Profil eller kort](losninger/grafikk/three-r170-composer-msaa.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/grafikk/three-r170-composer-msaa.md)

### løsning/grafikk/uniformlister-for-forste-render

Uniformlister må ha verdier før første render

Status: PASS. Stack: three.js r170, ShaderMaterial med lister som uniform vec4 uRip[8].

Mulig gjenbruk: Lag listene med full lengde og nøytrale verdier når modulen lastes, og del de samme listene mellom alle materialene:

Søkeord: array, bølger, delte uniformer, første render, hav, krasj, ocean, sea, shader, ShaderMaterial, shaders, skyggelegger, three js, three.js, threejs, uniform, uniformliste, vann, vec4, Vector4, water, waves

[Profil eller kort](losninger/grafikk/uniformlister-for-forste-render.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/grafikk/uniformlister-for-forste-render.md)

### løsning/grafikk/vertexcolors-uten-fargeattributt

vertexColors uten fargeattributt blir svart

Status: UNVERIFIED. Stack: three.js r170, WebGL2, MeshStandardMaterial med vertexColors.

Mulig gjenbruk: - Gi hver geometri som deler materialet en fargeattributt, også om den bare er hvit. - Eller lag et eget materiale uten `vertexColors` til geometrier uten farge.

Søkeord: attributt, black, color, geometri, instanceColor, materiale, svart, three js, three.js, threejs, vertexColors

[Profil eller kort](losninger/grafikk/vertexcolors-uten-fargeattributt.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/grafikk/vertexcolors-uten-fargeattributt.md)

### løsning/grafikk/webgl-kontekst-tapt

Når WebGL-konteksten blir borte

Status: UNVERIFIED. Stack: three.js r128 og nyere, WebGL.

Mulig gjenbruk: ```js canvas.addEventListener('webglcontextlost', e => { e.preventDefault(); mistet(); }); canvas.addEventListener('webglcontextrestored', () => hentet()); ```

Søkeord: Chrome, context lost, context restoration, GPU, kontekst, kontekst tapt, krasj, minne, mistet webgl kontekst, mobil, svart skjerm, three js, three.js, threejs, webgl context lost, webgl kontekst tapt, webglcontextlost, webglcontextrestored

[Profil eller kort](losninger/grafikk/webgl-kontekst-tapt.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/grafikk/webgl-kontekst-tapt.md)

### løsning/lyd/karplus-strong-lutt-med-lookahead

Prosedyrisk lutt med Karplus-Strong og en sequencer med lookahead

Status: PASS. Stack: WebAudio API i nettleseren, uten lydfiler.

Mulig gjenbruk: - **Lutt**: Karplus-Strong, forhåndsrendret én gang per tone til en AudioBuffer og lagret i et kart. Bruk filtrert støy som startbuffer og et kamfilter for plukkeposisjonen (nasal klang). Dempingen er 0,997, eller 0,9985 for dype toner. - **Avspilling**: en `AudioBufferSourceNode` per note gjennom lavpass, en topp på 240 Hz for kroppen, gain og pan

Søkeord: audio, browser, Karplus-Strong, lookahead, lutt, lyd, lydeffekter, music, musikk, nettleser, playbackRate, pluck, prosedyrisk, sequencer, setInterval, sfx, sound, soundtrack, uten lydfiler, web, WebAudio

[Profil eller kort](losninger/lyd/karplus-strong-lutt-med-lookahead.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/lyd/karplus-strong-lutt-med-lookahead.md)

### løsning/testing/bilder-for-og-etter-med-worktree

Bilder før og etter en grafikkendring med git worktree

Status: PASS. Stack: git, Node-bygg, Playwright-testrigg.

Mulig gjenbruk: ```sh git worktree add <scratch>/before HEAD # forrige commit i en egen mappe ln -s $PWD/node_modules <scratch>/before/node_modules (cd <scratch>/before && node build.mjs) ROOT=<scratch>/before node <testrigg> before.png steg.json node <testrigg> after.png steg.json # de samme stegene på det nye bygget git worktree remove --force <scratch>/before `

Søkeord: A/B, bloom, før og etter, git worktree, gloed, glow, glowing, glød, grafikk, regresjon, sammenligning, skjermbilder, test, testing, verification, verifisering

[Profil eller kort](losninger/testing/bilder-for-og-etter-med-worktree.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/testing/bilder-for-og-etter-med-worktree.md)

### løsning/testing/logg-over-det-som-mangler-hd

Hvilke figurruter og objekter mangler faktisk HD når spillet spilles

Status: PASS. Stack: ScummVM med HD-patch (DigHD) for SCUMM v7, C++11, motoren bygger HD-bildet per piksel fra kilder (rom, objekt, rute, film).

Mulig gjenbruk: Der motoren bestemmer at en piksel blir originalpiksel fordi HD mangler, lagres hvem den tilhører, og én gang per bilde telles det som står på skjermen:

Søkeord: character, characters, dighd-uten-hd.txt, figur, figurer, figurruter, filmer, gult felt, HD remake, kostymeruter, mangler HD, objekter, originalpiksler, prioritering, ScummVM, spilltest, test, testing, uten HD, verification, verifisering

[Profil eller kort](losninger/testing/logg-over-det-som-mangler-hd.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/testing/logg-over-det-som-mangler-hd.md)

### løsning/testing/nettside-med-github-api-i-sandkassen

Teste en Pages-nettside som henter filer fra GitHub-API-et, fra Claude-sandkassen

Status: PASS. Stack: Playwright for Python med headless Chromium 141, en side på github.io som henter spillfiler med fetch fra api.github.com (git/trees og git/blobs) med en lesenøkkel.

Mulig gjenbruk: - Rut forespørslene til github.io og api.github.com i Playwright, og hent dem med requests (som bruker proxyen og CA-en). Gi svarene fra API-et `access-control-allow-origin: *`, og svar selv på OPTIONS. - Gi siden en dummy-nøkkel. Ta den fra en miljøvariabel, så samme skript virker med en ekte nøkkel andre steder. - Start Chromium med `--use-angle=

Søkeord: api.github.com, browser, CA, Chromium, CORS, Emscripten, git blobs, GitHub Pages, lesenøkkel, nettleser, Playwright, proxy, route, sandkasse, ScummVM, SwiftShader, test, testing, verification, verifisering, web

[Profil eller kort](losninger/testing/nettside-med-github-api-i-sandkassen.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/testing/nettside-med-github-api-i-sandkassen.md)

### løsning/testing/playwright-swiftshader-three-lokalt

Nettleserttester av three.js-spill uten skjermkort og uten nett

Status: PASS. Stack: Playwright med headless Chromium, three.js fra jsdelivr via importmap.

Mulig gjenbruk: - Start Chromium med SwiftShader: `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist`. - Rut forespørslene til three.js mot den lokale `node_modules/three`:

Søkeord: browser, CDN, Chromium, CI, headless, importmap, nettleser, node_modules, offline, Playwright, route, skjermbilder, SwiftShader, test, testing, three js, three.js, threejs, verification, verifisering, web, WebGL

[Profil eller kort](losninger/testing/playwright-swiftshader-three-lokalt.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/testing/playwright-swiftshader-three-lokalt.md)

### løsning/ui/grid-skjerm-klipper-toppen

Høye paneler mister toppen når skjermen sentreres med grid

Status: PASS. Stack: CSS grid, fullskjerms overlegg med overflow-y: auto.

Mulig gjenbruk: Sentrer med automatiske marger i stedet. De blir 0 når panelet er for høyt:

Søkeord: CSS, grid, margin auto, mobil, overflow, panel, place-items center, safe center, scroll, toppen klippes

[Profil eller kort](losninger/ui/grid-skjerm-klipper-toppen.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/ui/grid-skjerm-klipper-toppen.md)

### løsning/ui/hidden-attributt-med-display-grid

hidden virker ikke på elementer med display: grid

Status: PASS. Stack: HTML og CSS.

Mulig gjenbruk: ```css [hidden] { display: none !important; } ```

Søkeord: attributt, CSS, CSS hidden, display flex, display grid, element skjules ikke, hidden, hidden display grid, important, skjult, vises likevel

[Profil eller kort](losninger/ui/hidden-attributt-med-display-grid.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/ui/hidden-attributt-med-display-grid.md)

### løsning/ui/skrifter-med-fontface

Skrifter som virker offline og i en streng CSP

Status: UNVERIFIED. Stack: Nettleser, FontFace API, én HTML-fil.

Mulig gjenbruk: Bygg woff2-filene inn som base64, gjør dem om til ArrayBuffer, og registrer dem med FontFace:

Søkeord: artifact, base64, browser, CSP, data-URI, font, font-src, FontFace, Google Fonts, nettleser, offline, skrift, web, woff2

[Profil eller kort](losninger/ui/skrifter-med-fontface.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/losninger/ui/skrifter-med-fontface.md)

## Repoer og verktøy

### achillean/shodan-python

The official Python library for Shodan

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/achillean/shodan-python)

### achimala/dream-loop

Agent-skill for visuell iterasjon: et generert målbilde sammenlignes med skjermbilder fra den faktiske scenen gjennom en egen kritiker.

Mulig gjenbruk: Bruk arbeidsmetoden som referanse for målbildet, faktisk bygg, visuell kritikk og ny korrigering i spill eller interaktive scener. Blender omtales for egne 3D-modeller.

Søkeord: agent-skill, Blender, create, generate, generation, generer, generering, iterasjon, målbilder, scene, scener, scenes, subagenter, visuell QA

[Profil eller kort](repoer/prosjekter/achimala--dream-loop.md) · [Kilde](https://github.com/achimala/dream-loop)

### ahujasid/mcp-for-blender

Opprinnelig Blender MCP-kandidat fra SIGNAL / 47-samtalen.

Mulig gjenbruk: Kilde til tidligere utforsking av Blender-kontroll og sceneinspeksjon via MCP.

Søkeord: 3D, 3d-modeling, ai, Blender, blender, blender-addon, blender-mcp, claude, generative-ai, historisk-kandidat, llm, MCP, mcp, model, model-context-protocol, modell, modeller, models, python

[Profil eller kort](repoer/prosjekter/ahujasid--mcp-for-blender.md) · [Kilde](https://github.com/ahujasid/mcp-for-blender)

### alphanu1/daytona-arcade-recomp



Søkeord: alfa, alpha, gjennomsiktig, gjennomsiktighet, transparency, transparent

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/alphanu1/daytona-arcade-recomp)

### amathislab/terra

TERRA: terrengtilpasset rekonstruksjon, retargeting og styring av muskelskjelettbasert bevegelse.

Mulig gjenbruk: Undersøk metoder for bevegelsesoverføring, terrengkontakt og kontroll av figurer.

Søkeord: animasjon, animate, animated, animation, animations, animere, bevegelse, bevegelsesoverføring, forskning, landscape, retarget, retargeting, TERRA, terrain, terreng

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/amathislab/terra)

### antoniaci/blackbird

An OSINT tool to search for accounts by username and email in social networks.

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/antoniaci/blackbird)

### aras-p/UnityGaussianSplatting

Unity-renderer for forhåndsberegnede splats; historisk Vulkan-/OpenGL-probe bevart.

Mulig gjenbruk: Undersøk konkrete splat-data i et isolert Unity-oppsett og sammenlign visuell kvalitet, okklusjon og ytelse.

Søkeord: 3dgs, Gaussian splatting, gaussian splatting, gaussian-splatting, gaussiske splats, historisk-lokal-test, okklusjon, OpenGL, splat, splats, test, testing, Unity, unity, verification, verifisering, Vulkan

[Profil eller kort](repoer/prosjekter/aras-p--UnityGaussianSplatting.md) · [Kilde](https://github.com/aras-p/UnityGaussianSplatting)

### ArchiveBox/ArchiveBox

Nettarkiv for flere formater, blant annet HTML, PNG, PDF og tekst.

Mulig gjenbruk: Bevare prosjektkilder, dokumentasjon og referansesider før de endres.

Søkeord: archivebox, arkivering, backups, bookmark-archiver, browser, browser-bookmarks, chromium, digipres, firefox, headless-browser, internet-archiving, lagre, lagring, nettleser, nettsider, PDF, persistence, pinboard, pocket, python, research, rss, save, saving, self-hosted, singlefile, warc, wayback-machine, web, web-archiving, wget, youtube-dl

[Profil eller kort](repoer/prosjekter/ArchiveBox--ArchiveBox.md) · [Kilde](https://github.com/ArchiveBox/ArchiveBox)

### arielshad/3d-asset-server

API og MCP for 3D-assets.

Mulig gjenbruk: Vurder assetoppslag og tilgang til 3D-ressurser fra agentverktøy.

Søkeord: 3D, API, assets, MCP, model, modell, modeller, models

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/arielshad/3d-asset-server)

### arloopa/UnitySplats

Unity-splatpakke med historisk test av proxy-relighting og importerinnstillinger.

Mulig gjenbruk: Undersøk trent kildedata, korrekt fargerom, matchet proxy og camera-oppsett før produksjonsbruk.

Søkeord: 3dgs, fargerom, Gaussian splatting, gaussian splatting, gaussiske splats, historisk-lokal-test, proxy, relighting, splat, splats, test, testing, Unity, verification, verifisering, Vulkan

[Profil eller kort](repoer/prosjekter/arloopa--UnitySplats.md) · [Kilde](https://github.com/arloopa/UnitySplats)

### Aureliengmz/clearwater

Real-time, photoreal shallow water in a single HTML file. WebGL2, no libraries, no build step.

Søkeord: bølger, hav, ocean, sea, vann, water, waves

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Aureliengmz/clearwater)

### bethington/ghidra-mcp

Ghidra MCP Server — 200+ MCP tools for AI-powered reverse engineering. GUI plugin + headless server, lazy tool loading, convention enforcement, batch operations, Ghidra Server integration, and Docker deployment.

Søkeord: binary analysis, binæranalyse, reverse engineering, reversering

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/bethington/ghidra-mcp)

### bhouston/three-dlss-nr

A Three.js (TSL / WebGPU) port of OpenDLSS-NR, the open-source reimplementation of NVIDIA's DLSS 5 neural rendering network

Søkeord: three js, three.js, threejs

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/bhouston/three-dlss-nr)

### bilawalsidhu/gods-eye-view

Nettleserapp med CesiumJS-globus og lag for blant annet fly, skip, satellitter, vær og offentlig tilgjengelige geografiske data.

Mulig gjenbruk: Studer modulære kartlag, sanntidsdata med interpolasjon, satellittbaner, kameraføring og et instrumentpreget grensesnitt for kart- og simuleringsprosjekter.

Søkeord: 3d-globe, browser, cesium, CesiumJS, flight-tracking, geospatial, geospatial-intelligence, GIS, gis, HUD, kart, nettleser, osint, photogrammetry, sanntidsdata, satellite-tracking, satellitter, spatial-intelligence, Vite, web, WebGL, webgl, worldview

[Profil eller kort](repoer/prosjekter/bilawalsidhu--gods-eye-view.md) · [Kilde](https://github.com/bilawalsidhu/gods-eye-view)

### BlueHeisenberg/SCSKiller

Verktøy som forhåndskompilerer spillshadere til GPU-driverens cache på Windows.

Mulig gjenbruk: Undersøk håndtering av shaderkompilering og cache for å redusere hakking.

Søkeord: AMD, cache, forhåndskompilering, hakking, hakking i spill, hitching, kompilering, NVIDIA, shader, shader cache, shader compilation, shader stutter, shadercache, shaders, skyggelegger, stutter, stuttering, Windows

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/BlueHeisenberg/SCSKiller)

### bobeff/open-source-games

Sjangerinndelt lenkesamling over spill med åpen kildekode, nyimplementeringer og kildeporter.

Mulig gjenbruk: Finn konkrete referanseprosjekter for FPS, strategi, rollespill, roguelikes, byggespill og andre sjangre før en avgrenset kode- eller arkitekturgjennomgang.

Søkeord: awesome-list, FPS, games, kildeporter, open-source, referanseliste, rollespill, spill, strategi, åpen kildekode

[Profil eller kort](repoer/prosjekter/bobeff--open-source-games.md) · [Kilde](https://github.com/bobeff/open-source-games)

### bpy-dev/blender-mcp

Blender MCP-distribusjon med historisk lokal saved-file-verifikasjon.

Mulig gjenbruk: Inspekter lagrede scener, finn runtime API-signaturer, lag separate checkpoints og verifiser render/FBX-rundtur.

Søkeord: API-oppslag, Blender, FBX, historisk-lokal-test, lagre, lagring, MCP, persistence, save, saved-file, saving, stdio, test, testing, verification, verifisering

[Profil eller kort](repoer/prosjekter/bpy-dev--blender-mcp.md) · [Kilde](https://github.com/bpy-dev/blender-mcp)

### chaseleantj/deskworlds

Interaktive ferskvanns- og revakvarier rendret lokalt med Three.js og WebGL2, med nettleservisning og skrivebordsbakgrunn for macOS.

Mulig gjenbruk: Studer fisk som reagerer på peker og mat, prosedyriske organismer, vannmiljøer og kvalitetsprofiler som pauser eller reduserer rendering når scenen ikke er synlig.

Søkeord: akvarium, browser, fisk, levende bakgrunn, macOS, nettleser, prosedyrisk, three js, Three.js, three.js, threejs, web, WebGL2, ytelse

[Profil eller kort](repoer/prosjekter/chaseleantj--desktop-habitats.md) · [Kilde](https://github.com/chaseleantj/deskworlds)

### chrispository/desktop-habitats-omarchy

Fork av Desktop Habitats som pakker akvariene som Omarchy-plugin med Linux-bakgrunn, skjermtilpasning og innstillingspanel.

Mulig gjenbruk: Referanse for Three.js-scener som skrivebordsbakgrunn på Omarchy, individuelle skjermoppsett og Blender-rigget sjøanemone med bevegelige tentakler.

Søkeord: akvarium, Blender, flereskjermer, Linux, Omarchy, Qt6, three js, Three.js, three.js, threejs, WebGL2

[Profil eller kort](repoer/prosjekter/chrispository--desktop-habitats-omarchy.md) · [Kilde](https://github.com/chrispository/desktop-habitats-omarchy)

### CoderGamester/mcp-unity

Separat Unity MCP-integrasjon, tidligere nevnt som kandidat.

Mulig gjenbruk: Sammenlign funksjoner mot konkrete Unity-editoroppgaver og eksisterende automatisering.

Søkeord: claudecode, codex-cli, copilot, cursor, editor, game-development, historisk-kandidat, MCP, mcp, model, model-context-protocol, modell, modeller, models, openai, openclaw, scene, scener, scenes, Unity, unity, unity-package, unity3d

[Profil eller kort](repoer/prosjekter/CoderGamester--mcp-unity.md) · [Kilde](https://github.com/CoderGamester/mcp-unity)

### collabs-inc/collab-public

Collaborator is a place to create with agents.

Søkeord: create, generate, generation, generer, generering

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/collabs-inc/collab-public)

### CoplayDev/unity-mcp

Unity Editor-kontroll via MCP; historisk kandidat fra SIGNAL / 47.

Mulig gjenbruk: Vurder sceneinspeksjon, objekt-/materialredigering og editorautomatisering når prosjektet trenger det.

Søkeord: ai, ai-integration, anthropic, automatisering, claude, copilot, cursor, editor, game-development, gamedev, gemini, historisk-kandidat, llm, MCP, mcp, model, model-context-protocol, modell, modeller, models, openai, scene, scener, scenes, Unity, unity, unity3d, videogames

[Profil eller kort](repoer/prosjekter/CoplayDev--unity-mcp.md) · [Kilde](https://github.com/CoplayDev/unity-mcp)

### cortiz2894/stylized-components

Three.js-/React Three Fiber-studier som inspirerte Voidcrafts vegetasjon og vannringer.

Mulig gjenbruk: Felles terreng-/vegetasjonsmaske, rotfestet vind, nedtråkking, transmisjon gjennom vegetasjon og vanninteraksjon.

Søkeord: browser, bølger, grass, gress, hav, HLSL, nettleser, ocean, React Three Fiber, scene, scener, scenes, sea, tekstur, teksturer, texture, textures, three js, Three.js, three.js, threejs, Unity, vann, vegetasjon, vegetation, water, waves, web

[Profil eller kort](repoer/prosjekter/cortiz2894--stylized-components.md) · [Kilde](https://github.com/cortiz2894/stylized-components)

### Crosstalk-Solutions/project-nomad

Server og nettgrensesnitt som samler lokale kunnskapsressurser, kurs, kart, notater og valgfri lokal AI gjennom Docker-baserte tjenester.

Mulig gjenbruk: Kandidat til et lokalt kunnskapsbibliotek med Kiwix, Kolibri, kart og dokumentsøk, eller som arkitekturreferanse for et administrasjonspanel over flere selvdriftede verktøy.

Søkeord: Docker, Kiwix, Kolibri, kunnskapsbibliotek, offline, Ollama, Qdrant, RAG, selvdrift

[Profil eller kort](repoer/prosjekter/Crosstalk-Solutions--project-nomad.md) · [Kilde](https://github.com/Crosstalk-Solutions/project-nomad)

### cryptomanavan/ShoreBreak

Interaktiv kystdemo i Three.js/WebGL2 med brytende bølger, skum, grunne vannstrømmer, våt sand og undervannsoptikk.

Mulig gjenbruk: Studer samspillet mellom FFT-hav, egen brytende bølgegeometri, GPU-basert gruntvannsløser, skumfelt og adaptiv renderoppløsning for vann- og strandscener.

Søkeord: bølger, FFT, gruntvann, hav, ocean, sea, skum, three js, Three.js, three.js, threejs, undervann, vann, Vite, water, waves, WebGL2

[Profil eller kort](repoer/prosjekter/cryptomanavan--ShoreBreak.md) · [Kilde](https://github.com/cryptomanavan/ShoreBreak)

### dani-garcia/vaultwarden

Alternativ Bitwarden-kompatibel server skrevet i Rust, for egen drift.

Mulig gjenbruk: Kandidat til separat passordinfrastruktur.

Søkeord: Bitwarden, bitwarden, bitwarden-rs, docker, egen-drift, passord, rocket, rust, vaultwarden

[Profil eller kort](repoer/prosjekter/dani-garcia--vaultwarden.md) · [Kilde](https://github.com/dani-garcia/vaultwarden)

### debpalash/VoiceStudio

VoiceStudio is the open-source, fully-local ElevenLabs alternative — voice cloning, voice design, video dubbing, dictation, transcription & audiobook creation in 646 languages.

Søkeord: audio, lyd, lydeffekter, sfx, sound

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/debpalash/VoiceStudio)

### dgreenheck/tidewater

Coastal town built with Opus 5.5

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/dgreenheck/tidewater)

### dgtlmoon/changedetection.io

Overvåker nettsideendringer med varsler, selektorer, filtre og intervaller.

Mulig gjenbruk: Følge dokumentasjon, release-sider, ressurstilgang eller stillinger.

Søkeord: back-in-stock, browser, change-alert, change-detection, change-monitoring, endringer, monitoring, nettleser, notifications, overvåking, restock-monitor, rss, self-hosted, url-monitor, varsler, web, web-scraping, website-change-detection, website-change-detector, website-change-monitor, website-change-notification, website-change-tracker, website-defacement-monitoring, website-monitor, website-monitoring, website-watcher

[Profil eller kort](repoer/prosjekter/dgtlmoon--changedetection.io.md) · [Kilde](https://github.com/dgtlmoon/changedetection.io)

### ektogamat/threejs-conference

Walk through a rainy cyberpunk alley powered by WebGPU, Three.js, and TSL (Three Shading Language). Neon billboards, wet pavement, GPU rain that respects rooftops and props, cinematic post-processing, and first-person exploration with BVH collision.

Søkeord: collision, collisions, etterbehandling, kollisjon, post processing, postprocessing, screen effects, screenfx, skjermeffekter, three js, three.js, threejs

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/ektogamat/threejs-conference)

### EpicGames/unreal-engine-skills-for-claude-code-plugin

Skills og MCP-arbeidsflyt for å styre Unreal Editor fra Claude Code.

Mulig gjenbruk: Vurder editorverktøy for scener, Blueprints, materialer og animasjon i et eksisterende Unreal-prosjekt.

Søkeord: Blueprints, Claude Code, editor, editorautomatisering, MCP, Unreal, Unreal Editor, Unreal Engine

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin)

### ErwannRobin/ex-nihilo

EX NIHILO — generative audiovisual piece in a single HTML file

Søkeord: audio, lyd, lydeffekter, sfx, sound

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/ErwannRobin/ex-nihilo)

### github/github-mcp-server

GitHub's official MCP Server

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/github/github-mcp-server)

### GLinnik21/plx-native

Uoffisiell Plex-klient for LG webOS med native grensesnitt.

Mulig gjenbruk: Studer TV-grensesnitt og native medieavspilling som alternativ til en nettleserbasert klient.

Søkeord: LG, media, native, Plex, TV, webOS

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/GLinnik21/plx-native)

### haato-w/3d-gabor-splatting

Forskningsreferanse for fine mønstre med 3D Gabor Splatting.

Mulig gjenbruk: Vurder forskningsmetoden for særskilte overflate-/rekonstruksjonsbehov.

Søkeord: 3d-reconstruction, 3dgs, forskning, Gabor, gabor-filter, Gaussian splatting, gaussian splatting, gaussian-splatting, gaussiske splats, high-frequency-data, lisensbegrensning, machine-learning, rekonstruksjon, splat, splats, tekstur, teksturer, texture, textures

[Profil eller kort](repoer/prosjekter/haato-w--3d-gabor-splatting.md) · [Kilde](https://github.com/haato-w/3d-gabor-splatting)

### haato-w/diff-gabor-rasterization

CUDA-rasterizer til 3D Gabor Splatting-forskningen.

Mulig gjenbruk: Teknisk referanse for den tilhørende spesialiserte Gabor-rendereren.

Søkeord: 3dgs, CUDA, forskning, Gabor, Gaussian splatting, gaussian splatting, gaussiske splats, rasterizer, splat, splats

[Profil eller kort](repoer/prosjekter/haato-w--diff-gabor-rasterization.md) · [Kilde](https://github.com/haato-w/diff-gabor-rasterization)

### i12bp8/decomp.wtf

Lokal agentstyrt matching-dekompilering av spill til C med byte-for-byte-kontroll.

Status: ARKIVERT. Stack: Les kilden.

Mulig gjenbruk: Studer funksjonsfordeling, opprinnelig kompilator, bytekontroll og MCP. Egen fork: Tombonator3000/decomp.wtf.

Søkeord: arkivert, binary analysis, binæranalyse, byte matching, bytekontroll, C, decomp.wtf, decompilation, decompile, decompiler, dekompilering, fork, GameCube, matching, matching decompilation, MCP, N64, reverse engineering, reversering, Wii

[Profil eller kort](repoer/decomp-wtf-2026-10-16.md) · [Kilde](https://github.com/i12bp8/decomp.wtf)

### iamtechartist/coastal-simulation

Three.js-kystsimulering beskrevet med gruntvannsløser, brytende dønninger, skum, våt sand, sjøsprøyt og utforskning langs stranden.

Mulig gjenbruk: Visuell og teknisk kandidat for strandkontakt, bølgebryting og vann/sand-overganger; README lenker til en nettleserdemo for senere vurdering.

Søkeord: bølger, demo, gruntvann, hav, kyst, ocean, sea, skum, three js, Three.js, three.js, threejs, vann, våt sand, water, waves

[Profil eller kort](repoer/prosjekter/iamtechartist--coastal-simulation.md) · [Kilde](https://github.com/iamtechartist/coastal-simulation)

### iamtechartist/obsidian

Break a stone and what's inside? A cathedral. Break the cathedral? A whale. Break the whale and you're holding the stone again. 32,000 shards, one endless loop, all procedural Three.js.

Søkeord: three js, three.js, threejs

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/iamtechartist/obsidian)

### imputnet/cobalt

Medienedlasting via nettgrensesnitt og API.

Mulig gjenbruk: Hente egne klipp og tillatte referansemedier.

Søkeord: audio, collaboration, downloader, instagram, javascript, lagre, lagring, lyd, lydeffekter, media, music, musikk, nedlasting, persistence, reddit, save, saving, sfx, social-media, sound, soundcloud, soundtrack, svelte, tiktok, twitter, typescript, video, vimeo, vk, webapp, youtube, youtube-downloader

[Profil eller kort](repoer/prosjekter/imputnet--cobalt.md) · [Kilde](https://github.com/imputnet/cobalt)

### JesusGalindez/threejs-ocean-simulator-skills

Physically based ocean, sky and boats in a single three.js file, plus skills. Claude, Codex and Gemini.

Søkeord: bølger, hav, ocean, sea, three js, three.js, threejs, vann, water, waves

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/JesusGalindez/threejs-ocean-simulator-skills)

### joetsoi/OpenMoonstone

Åpen nyimplementering av Moonstone: A Hard Day's Knight.

Mulig gjenbruk: Undersøk kode og spillarkitektur som referanse for et Moonstone-lignende spill.

Søkeord: kildeport, Moonstone, nyimplementering, spill

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/joetsoi/OpenMoonstone)

### Karolynaz/devil-3ds

Nintendo 3DS finally gets a Diablo port built for comfortable dual-screen play. Based on DevilutionX, whose original 3DS UI and controls were difficult to use.

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Karolynaz/devil-3ds)

### Kenton-GMI/muster-ww2

Muster: a hands-on 3D archive of WWII military models. Browse, configure and arrange soldiers, tanks, artillery and aircraft on a diorama display. All models procedurally built in three.js + TypeScript.

Søkeord: model, modell, modeller, models, three js, three.js, threejs

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Kenton-GMI/muster-ww2)

### laramies/theHarvester

E-mails, subdomains and names Harvester - OSINT

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/laramies/theHarvester)

### lhlGitHub/threejs-architecture-effects

Agent-skill og Vite/React/Three.js-startprosjekt for interaktiv 3D-arkitektur som bygges opp langs en styrbar tidslinje.

Mulig gjenbruk: Referanse for å planlegge bygningsdeler, bruke prosedyriske PBR-materialer og la geometri, skygger og kamera følge en deterministisk konstruksjonstidslinje.

Søkeord: agent-skill, arkitektur, konstruksjon, PBR, React, three js, Three.js, three.js, threejs, tidslinje, Vite

[Profil eller kort](repoer/prosjekter/lhlGitHub--threejs-architecture-effects.md) · [Kilde](https://github.com/lhlGitHub/threejs-architecture-effects)

### LibreTranslate/LibreTranslate

Selvdriftet oversettelses-API basert på Argos Translate, med mulighet for offlinebruk.

Mulig gjenbruk: Utkast til lokalisering og dokumentoversettelse.

Søkeord: API, api, lokalisering, machine, offline, oversettelse, translate, translation, translator

[Profil eller kort](repoer/prosjekter/LibreTranslate--LibreTranslate.md) · [Kilde](https://github.com/LibreTranslate/LibreTranslate)

### localsend/localsend

Deler filer og meldinger mellom enheter på lokalt nettverk uten ekstern server.

Mulig gjenbruk: Flytte bygg, skjermbilder og dokumenter mellom egne enheter.

Søkeord: bygg, dart, fildeling, file-sharing, flutter, flutter-apps, lokalnett, overføring

[Profil eller kort](repoer/prosjekter/localsend--localsend.md) · [Kilde](https://github.com/localsend/localsend)

### marceld23/BlocksBeyondTheStars

Vokselbasert rom- og byggespill med prosedyriske verdener, Unity-klient og separat autoritativ .NET-server.

Mulig gjenbruk: Studer skillet mellom klient og server, deterministisk verdensgenerering, persistens, delte datamodeller og JSON-definert innhold. Dette er også oppstrømsgrunnlaget for Voidcraft.

Søkeord: .NET, AGPL, C#, crafting, create, csharp, dotnet, family-friendly, flerspiller, game, gamedev, generate, generation, generer, generering, indie-game, multiplayer, nettspill, open-source, procedural-generation, romspill, sandbox, self-hosted, space-game, survival-game, Unity, unity, unity3d, URP, verdensgenerering, voksler, voxel, voxel-game

[Profil eller kort](repoer/prosjekter/marceld23--BlocksBeyondTheStars.md) · [Kilde](https://github.com/marceld23/BlocksBeyondTheStars)

### microsoft/TRELLIS.2

3D-generering med kompakte strukturerte latenter.

Mulig gjenbruk: Vurder metoden som referanse for generering av 3D-innhold og en senere avgrenset assetprøve.

Søkeord: 3D, 3D fra bilde, 3d fra bilde, 3D-generering, assets, bilde til 3d, create, generate, generation, generer, generering, image to 3d, image to mesh, image-to-3D, latenter, model, modell, modeller, models, O-Voxel, PBR, tekstur, teksturer, teksturert mesh, texture, textures, TRELLIS.2

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/microsoft/TRELLIS.2)

### mikf/gallery-dl

Kommandolinjeverktøy for bildegallerier og samlinger, med konfigurerbar filnavngivning.

Mulig gjenbruk: Arkivere egne eller lisensierte bildereferanser.

Søkeord: arkivering, bilder, CLI, danbooru, deviantart, downloader, gallerier, gallery, kemono, mangadex, pixiv, tumblr, twitter

[Profil eller kort](repoer/prosjekter/mikf--gallery-dl.md) · [Kilde](https://github.com/mikf/gallery-dl)

### moonpudding/localchannels

Lokalt videobibliotek med søk, filnavnbaserte tagger, kontinuerlige kanaler, avspillingshistorikk og VR/WebXR-visning.

Mulig gjenbruk: Kandidat for å organisere egne referansevideoer, og kodeeksempel for inkrementell medieindeksering, gjenopptatt avspilling, kanalkøer og 180/360-graders video.

Søkeord: Docker, ffmpeg, mediebibliotek, Python, selvdrift, tagger, video, VR, WebXR

[Profil eller kort](repoer/prosjekter/moonpudding--localchannels.md) · [Kilde](https://github.com/moonpudding/localchannels)

### morluto/rea

Agentbasert reverse engineering fra appatferd til native binærfiler.

Mulig gjenbruk: Studer arbeidsflyter for å undersøke appatferd og binærkode med agenter.

Søkeord: agenter, analyse, apper, binary analysis, binæranalyse, binærfiler, reverse engineering, reversering

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/morluto/rea)

### multimodal-art-projection/YuE

YuE2-system for musikkgenerering med redigerbar melodi-/akkordplan, vokal og akkompagnement, samt Python-API og agent-skill.

Mulig gjenbruk: Kandidat for senere vurdering av lokal musikkproduksjon og kontrollert variasjon gjennom eksplisitte komposisjonsplaner; API-et deler planlegging, semantisk generering, syntese og dekoding i steg.

Søkeord: agent-skill, ai, audio, audio-generation, create, CUDA, deep-learning, foundation-models, generate, generation, generer, generering, gpt, huggingface, komposisjon, llama, llms, lokal AI, lyd, lydeffekter, model, modell, modeller, modellvekter, models, music, music-generation, musikk, Python, sfx, sound, soundtrack, style-transfers, voice-cloning, YuE2

[Profil eller kort](repoer/prosjekter/multimodal-art-projection--YuE.md) · [Kilde](https://github.com/multimodal-art-projection/YuE)

### NationalSecurityAgency/ghidra

Ghidra is a software reverse engineering (SRE) framework

Søkeord: binary analysis, binæranalyse, reverse engineering, reversering

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/NationalSecurityAgency/ghidra)

### neilsonnn/image-blaster

An image-to-world skillset for Claude.

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/neilsonnn/image-blaster)

### obra/superpowers

Opphav til den lokalt tilpassede brainstorming-skillen.

Mulig gjenbruk: Strukturer designavklaring og beslutninger før implementering; behold konkret opphavs- og tilpasningslogg.

Søkeord: ai, arbeidsflyt, brainstorming, coding, design, lokal-tilpasning, MIT, obra, sdlc, skills, subagent-driven-development, superpowers

[Profil eller kort](repoer/prosjekter/obra--superpowers.md) · [Kilde](https://github.com/obra/superpowers)

### OpenCloudGaming/OpenNOW

Custom GeForce Now Client Named OpenNOW

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/OpenCloudGaming/OpenNOW)

### playcanvas/splat-transform

Konvertering, transformasjon og filtrering av splat-data.

Mulig gjenbruk: Lag reproduserbare konverteringer med festet verktøyversjon, bevar originaldata og kontroller faktiske kollisjonsmesh.

Søkeord: 3d-gaussian-splatting, 3dgs, cli, collision, collisions, Gaussian splatting, gaussian splatting, gaussian-splatting, gaussiske splats, GLB, kollisjon, konvertering, PlayCanvas, playcanvas, SOG, splat, splats, supersplat, typescript

[Profil eller kort](repoer/prosjekter/playcanvas--splat-transform.md) · [Kilde](https://github.com/playcanvas/splat-transform)

### playcanvas/supersplat

Interaktiv redigering og inspeksjon av Gaussian splats.

Mulig gjenbruk: Klargjør, inspiser og sammenlign splat-data i et støttet verktøy før import i målprosjektet.

Søkeord: 3d-gaussian-splatting, 3dgs, Gaussian splatting, gaussian splatting, gaussian-splatting, gaussiske splats, pcui, PlayCanvas, playcanvas, redigering, splat, splats, SuperSplat, typescript, WebGL, webgl, WebGPU, webgpu

[Profil eller kort](repoer/prosjekter/playcanvas--supersplat.md) · [Kilde](https://github.com/playcanvas/supersplat)

### reactive-resume/reactive-resume

CV-bygger med maler, forhåndsvisning og eksport, blant annet PDF og JSON.

Mulig gjenbruk: CV-er og strukturerte profil-/porteføljedata.

Søkeord: agent-skills, ai, CV, dsh-plugin, hacktoberfest, javascript, mcp-server, PDF, profil, react, resume-builder, self-hosted, typescript

[Profil eller kort](repoer/prosjekter/reactive-resume--reactive-resume.md) · [Kilde](https://github.com/reactive-resume/reactive-resume)

### rehan-remade/universal-modder

Point Claude at any game. Skills, tools and the fal MCP that let Claude Code mod almost any PC game you own: recon, reverse engineering, fal-generated art/3D/audio, in-game testing, showcase videos.

Søkeord: audio, binary analysis, binæranalyse, create, generate, generation, generer, generering, lyd, lydeffekter, reverse engineering, reversering, sfx, sound, test, testing, verification, verifisering

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/rehan-remade/universal-modder)

### SamG-Coder/clearwater

Infinite FFT water in CUDA: WebGPU browser demo and native Windows app with shared kernels. Live demo: https://samg-coder.github.io/clearwater/

Søkeord: browser, bølger, hav, nettleser, ocean, sea, vann, water, waves, web

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/SamG-Coder/clearwater)

### SamG-Coder/coastal-simulation-cuda-webshader

GPU-basert kystsimulering; høy relevans som algoritme- og effektreferanse for Unity.

Mulig gjenbruk: Se bevart gjennomgang av vann, skum, strandkontakt og GPU-arkitektur i historiske notater.

Søkeord: bølger, coastal-simulation, cuda, foam, hav, ocean, sea, shallow-water, shoreline, simulation, spray, three js, three.js, threejs, Unity-port, vann, water, waves, WebGPU, webgpu, wetness

[Profil eller kort](repoer/prosjekter/SamG-Coder--coastal-simulation-cuda-webshader.md) · [Kilde](https://github.com/SamG-Coder/coastal-simulation-cuda-webshader)

### SamG-Coder/cuda-webshader

Kompilator og WebGPU-kjøremiljø som oversetter et avgrenset CUDA C-utvalg til WGSL, med sandbox, partikler og andre demonstrasjoner.

Mulig gjenbruk: Studer GPU-beregning i nettleseren, delte compute/render-buffere, dokumenterte kernel-kontrakter og oppdeling mellom CPU-tester, nettleser-GPU-tester og native CUDA-sammenligninger.

Søkeord: benchmark, browser, CUDA, GPU compute, kompilator, nettleser, partikler, three js, Three.js, three.js, threejs, web, WebGPU, WGSL

[Profil eller kort](repoer/prosjekter/SamG-Coder--cuda-webshader.md) · [Kilde](https://github.com/SamG-Coder/cuda-webshader)

### SamG-Coder/WaterCuda

Vann-/GPU-referanse brukt som inspirasjon i The Deep Ones.

Mulig gjenbruk: Undersøk vannalgoritmer for avgrenset tilpasning til eksisterende renderer.

Søkeord: browser, bølger, GPU, hav, nettleser, ocean, referanse, rendering, sea, Unity-port, vann, water, waves, web

[Profil eller kort](repoer/prosjekter/SamG-Coder--WaterCuda.md) · [Kilde](https://github.com/SamG-Coder/WaterCuda)

### scenario-labs/skills

Get production-ready images, video, audio, and 3D from any AI agent: skills that pick the right model, price before spending, and keep characters and brands consistent through the Scenario MCP, plus expert teams that drive Blender, Maya, ZBrush, Unreal, and Unity.

Søkeord: audio, character, characters, figur, figurer, lyd, lydeffekter, model, modell, modeller, models, sfx, sound

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/scenario-labs/skills)

### ScottieFox/caustic-volume

Real-time water caustics in the browser, built on three.js. Single-file lite and sandbox versions.

Søkeord: browser, bølger, hav, nettleser, ocean, sea, three js, three.js, threejs, vann, water, waves, web

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/ScottieFox/caustic-volume)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills

Samling av Three.js-skills og implementasjonseksempler for materialer, lys, vann, vær, prosedyrisk geometri, VFX og visuell validering.

Mulig gjenbruk: Slå opp avgrensede grafikksystemer og tilhørende eksempler, særlig hav/undervann, materialer, atmosfære, skygger og diagnostiske visninger. Bruk prinsippene om reproduserbare innganger og tidsmessig stabilitet ved egne vurderinger.

Søkeord: agent-skills, bølger, GLSL, hav, ocean, PBR, scene, scener, scenes, sea, three js, Three.js, three.js, threejs, TSL, vann, VFX, visuell QA, water, waves, WebGPU

[Profil eller kort](repoer/prosjekter/scottstts--Threejs-Awesome-Graphics-Agent-Skills.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills)

### searxng/searxng

Metasøk som samler svar fra flere søketjenester.

Mulig gjenbruk: Felles researchverktøy ved egen drift.

Søkeord: bing, brave, degoogle, duckduckgo, google, metasearch, personvern, privacy, python, qwant, research, search, search-engine, searx, searxng, startpage, søk, yahoo

[Profil eller kort](repoer/prosjekter/searxng--searxng.md) · [Kilde](https://github.com/searxng/searxng)

### shader-effects-inc/shaders

WebGPU-komponenter for React, Vue, Svelte, Solid, JavaScript og Framer.

Mulig gjenbruk: Vurder avgrensede shaderkomponenter og visuelle effekter i eksisterende webgrensesnitt.

Søkeord: effekter, Framer, React, shader, shaders, skyggelegger, Solid, Svelte, Vue, WebGPU

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/shader-effects-inc/shaders)

### SimonSchubert/omalauncher

Android-launcher med agentbygde apper og widgets, Omarchy-temaer og Arch Linux uten root.

Mulig gjenbruk: Studer et tilpassbart Android-startgrensesnitt og agentarbeid med apper og widgets.

Søkeord: agenter, Android, Arch Linux, launcher, Omarchy, widgets

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/SimonSchubert/omalauncher)

### smicallef/spiderfoot

SpiderFoot automates OSINT for threat intelligence and mapping your attack surface.

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/smicallef/spiderfoot)

### snuri00/ps2-web-recomp

Statisk rekompilering av PS2-spill til WebAssembly, med native runtime.

Mulig gjenbruk: Undersøk en PS2-rekompileringspipeline og skillet mellom generert kode og runtime.

Søkeord: browser, nettleser, PlayStation 2, PS2, recompilation, recompile, recompiler, rekompilering, runtime, WASM, web, WebAssembly

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/snuri00/ps2-web-recomp)

### snuri00/ps3recomp

Runtime-biblioteker for statisk rekompilering av PS3-titler.

Mulig gjenbruk: Studer runtime-grensesnitt og støttebiblioteker for PS3-rekompilering.

Søkeord: bibliotek, PlayStation 3, PS3, recompilation, recompile, recompiler, rekompilering, runtime

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/snuri00/ps3recomp)

### snuri00/psp-web-recomp

PSP-spill i nettleseren med statisk rekompilering til WebAssembly, HLE-kjerne og WebGL2.

Mulig gjenbruk: Undersøk kombinasjonen av rekompilert kode, systemkall og nettleserrendering.

Søkeord: browser, HLE, nettleser, PSP, recompilation, recompile, recompiler, rekompilering, WASM, web, WebAssembly, WebGL2

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/snuri00/psp-web-recomp)

### snuri00/turbo-quant

TurboQuant: kvantisering av KV-cache for LLM-inferens, med QJL og PolarQuant.

Mulig gjenbruk: Vurder komprimering av KV-cache som referanse for en senere måling av lokal inferens.

Søkeord: inferens, KV-cache, kvantisering, LLM, PolarQuant, QJL, TurboQuant

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/snuri00/turbo-quant)

### snuri00/turbo-quant-ios

Metal-akselerert komprimering av KV-cache for lokal LLM-inferens på Apple-enheter.

Mulig gjenbruk: Studer GPU-akselerert cachekomprimering på iPhone, iPad og Mac.

Søkeord: Apple, compress, compression, iOS, iPad, iPhone, komprimering, KV-cache, LLM, Mac, Metal, TurboQuant

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/snuri00/turbo-quant-ios)

### soxoj/maigret

🕵️‍♂️ Collect a dossier on a person by username from 6K websites

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/soxoj/maigret)

### storytold/photocraft

Åpen bilderedigerer skrevet i Rust.

Mulig gjenbruk: Undersøk arkitektur og bildebehandling som referanse for lokale redigeringsverktøy.

Søkeord: bildebehandling, bilderedigering, PhotoCraft, Rust

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/storytold/photocraft)

### Suwayomi/Suwayomi-Server

Manga-leserserver kompatibel med Mihon/Tachiyomi-utvidelser, med klienter og nettgrensesnitt.

Mulig gjenbruk: Referanse for bibliotek, leseframdrift og klient/server-design.

Søkeord: bibliotek, desktop, hacktoberfest, javalin, kotlin, leser, manga, manga-downloader, manga-reader, mangareader, self-hosted, tachidesk, tachidesk-server, tachiyomi

[Profil eller kort](repoer/prosjekter/Suwayomi--Suwayomi-Server.md) · [Kilde](https://github.com/Suwayomi/Suwayomi-Server)

### Tencent-Hunyuan/AuK

AuK: An Open-Source Foundational Model for Speech Generation and Editing

Søkeord: create, generate, generation, generer, generering, model, modell, modeller, models

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tencent-Hunyuan/AuK)

### TencentARC/AnimeSR

AnimeSR: superoppløsning av animasjonsvideo.

Mulig gjenbruk: Vurder metoden som kandidat for en avgrenset oppskaleringsprøve av animasjon.

Søkeord: animasjon, animate, animated, animation, animations, animere, AnimeSR, model, modell, modeller, models, oppskalering, super resolution, superoppløsning, upscale, upscaling, video

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/TencentARC/AnimeSR)

### tigerless-labs/autoharness

Autoharness — a self-learning skill layer for Claude Code — distills skills from your real sessions, updates them as you work, and prunes the ones that stop getting used. No daemon, no benchmark.

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/tigerless-labs/autoharness)

### Tombonator3000/3044

Geometry 3044: eget retroinspirert nettleserskytespill med fiendeformasjoner, bosser, comboer og synthwave-uttrykk.

Mulig gjenbruk: Referanse for bølge- og formasjonsstyring, poeng/combo-system, lokale rekordlister, attract mode og enkle partikkel-/CRT-effekter i arkadespill.

Søkeord: arkade, browser, combo, CRT, eget prosjekt, formasjoner, JavaScript, nettleser, shooter, synthwave, web

[Profil eller kort](repoer/prosjekter/Tombonator3000--3044.md) · [Kilde](https://github.com/Tombonator3000/3044)

### Tombonator3000/Blocky

Blocky

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/Blocky)

### Tombonator3000/bustville-empire



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/bustville-empire)

### Tombonator3000/connect-play



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/connect-play)

### Tombonator3000/conspiracy-canvas

Eget Lovable-basert prosjekt med dokumentert Vite/TypeScript/React-grensesnitt, shadcn-ui og Tailwind CSS.

Mulig gjenbruk: Mulig referanse for React-grensesnitt og oppsett for bygg/hosting; konkrete gjenbrukbare funksjoner må identifiseres gjennom en senere gjennomgang av kildekoden.

Søkeord: eget prosjekt, GitHub Pages, Lovable, React, shadcn-ui, Tailwind, TypeScript, Vite

[Profil eller kort](repoer/prosjekter/Tombonator3000--conspiracy-canvas.md) · [Kilde](https://github.com/Tombonator3000/conspiracy-canvas)

### Tombonator3000/cthulhu-text-rpg



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/cthulhu-text-rpg)

### Tombonator3000/decomp.wtf

Egen offentlig fork av det arkiverte decomp.wtf, opprettet 16. oktober 2026.

Mulig gjenbruk: Utgangspunkt for videre arbeid med lokal matching-dekompilering og bytekontroll.

Søkeord: byte matching, bytekontroll, decomp.wtf, decompilation, decompile, decompiler, dekompilering, egen fork, fork, matching decompilation, MCP

[Profil eller kort](repoer/decomp-wtf-2026-10-16.md) · [Kilde](https://github.com/Tombonator3000/decomp.wtf)

### Tombonator3000/deep-regrets-digital



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/deep-regrets-digital)

### Tombonator3000/Dig-HD-Remake

HD-versjon av The Dig med grafikk over originalen gjennom en ScummVM-patch.

Mulig gjenbruk: Bruk de eksisterende løsningskortene om figurark, publisert mod og logg over manglende HD.

Søkeord: character, character sheet, characters, figur, figurark, figurer, HD, løsningskort, mod, ScummVM, spill, sprite sheet, sprite sheets, spriteark, sprites, spritesheet, spritesheets, The Dig

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/Dig-HD-Remake)

### Tombonator3000/Dig-HD-Web

The Dig HD browser engine for GitHub Pages. Local game and HD files are never uploaded.

Søkeord: browser, nettleser, web

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/Dig-HD-Web)

### Tombonator3000/DoD-Roguelite



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/DoD-Roguelite)

### Tombonator3000/guild-life-adventures



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/guild-life-adventures)

### Tombonator3000/jones-fastlane



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/jones-fastlane)

### Tombonator3000/Jonesinthefastlane



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/Jonesinthefastlane)

### Tombonator3000/Loincloth-Legends



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/Loincloth-Legends)

### Tombonator3000/Lula



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/Lula)

### Tombonator3000/MOONSTONE



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/MOONSTONE)

### Tombonator3000/morbidium

2D/3D action spill med rpg elementer

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/morbidium)

### Tombonator3000/Mythos-Quest-3D



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/Mythos-Quest-3D)

### Tombonator3000/Nuclear-war-

Nuclear war

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/Nuclear-war-)

### Tombonator3000/pogicity-builder



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/pogicity-builder)

### Tombonator3000/prosjektbibliotek

Privat referansebibliotek: GitHub-stjerner, skills, spillmotorer, 3D, verktøy og tidligere research med kilder og gjenbruksnotater.

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek)

### Tombonator3000/Sam-Max-HD



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/Sam-Max-HD)

### Tombonator3000/Sam-Max-HD-Web

Sam-Max-HD-Web

Søkeord: browser, nettleser, web

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/Sam-Max-HD-Web)

### Tombonator3000/SceneForge



Søkeord: scene, scener, scenes

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/SceneForge)

### Tombonator3000/ShadowGov



Søkeord: shadow, shadows, skygge, skygger

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/ShadowGov)

### Tombonator3000/ShadowGov---Lovable

STRATEGY GAME : CARD GAMES TYPE

Søkeord: shadow, shadows, skygge, skygger

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/ShadowGov---Lovable)

### Tombonator3000/SIGNAL-47

Eget førstepersonsspill om kosmisk etterforskning ved SARO i New Mexico i 1986, bygget med Unity/URP og Blender.

Mulig gjenbruk: Referanse for fysiske interaksjoner, feltkamera og fotoframkalling, kontrollpunktlagring, dokumentert spillerreise, isolerte testprofiler og sporbar sammenheng mellom kilde, bygg og leveranse.

Søkeord: Blender, eget prosjekt, etterforskning, feltkamera, Gauntlet, kosmisk skrekk, Linux, Unity, URP

[Profil eller kort](repoer/prosjekter/Tombonator3000--SIGNAL-47.md) · [Kilde](https://github.com/Tombonator3000/SIGNAL-47)

### Tombonator3000/SIGNAL-47-Playtest

Downloadable SIGNAL / 47 playtest builds. Game source remains in a separate private repository.

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/SIGNAL-47-Playtest)

### Tombonator3000/state-shift-strategy

Paranoid Times: eget satirisk kortstrategispill med React-avisgrensesnitt, delstatskart og konkurranse om innflytelse og nyhetsbildet.

Mulig gjenbruk: Studer datadrevet kortkatalog, strategiheuristikker, synliggjøring av spillekonsekvenser og dokumentert oppfølging av oppstart, lagring, kortflyt og CI-kontroller.

Søkeord: Bun, eget prosjekt, Gauntlet, kortspill, React, spill-AI, strategi, TypeScript

[Profil eller kort](repoer/prosjekter/Tombonator3000--state-shift-strategy.md) · [Kilde](https://github.com/Tombonator3000/state-shift-strategy)

### Tombonator3000/the-deep-ones

Eget kosmisk fiskespill; README skiller den nye The Stillwater Below-spilldelen i v2/ fra den bevarte eldre The Deep Ones-prototypen.

Mulig gjenbruk: Referanse for fiskespenning, oppdagelser, butikk/utstyr, hundefølge, original nattillustrasjon og separat lokal lagring når en gammel prototype bygges om.

Søkeord: 2D, eget prosjekt, fiskespill, illustrasjon, JavaScript, kosmisk skrekk, lagre, lagring, lokal lagring, persistence, prototype, save, saving

[Profil eller kort](repoer/prosjekter/Tombonator3000--the-deep-ones.md) · [Kilde](https://github.com/Tombonator3000/the-deep-ones)

### Tombonator3000/the-deep-ones-3d-downloads

Public Windows and Linux playtest downloads for The Deep Ones. Game source remains private.

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/the-deep-ones-3d-downloads)

### Tombonator3000/tom-erland-showcase



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/tom-erland-showcase)

### Tombonator3000/Transcendensens-Vev-CRPG

Eget repo beskrevet som en CRPG-test; tilgjengelig README består av prosjektnavn og denne korte beskrivelsen.

Mulig gjenbruk: Bevart som gjenfinnbar lenke til eget rollespilleksperiment. Konkrete systemer og gjenbruksmuligheter krever en senere gjennomgang av kildefilene.

Søkeord: CRPG, eget prosjekt, eksperiment, mangelfull dokumentasjon, rollespill, test, testing, verification, verifisering

[Profil eller kort](repoer/prosjekter/Tombonator3000--Transcendensens-Vev-CRPG.md) · [Kilde](https://github.com/Tombonator3000/Transcendensens-Vev-CRPG)

### Tombonator3000/vector-war-games

Eget Lovable/Vite/TypeScript/React-prosjekt med dokumenterte spillrelaterte hooks og Vitest/React Testing Library-oppsett.

Mulig gjenbruk: Mulig referanse for React-baserte spillsystemer og deterministisk testing av tilfeldige hendelser; README nevner useFlashpoints som eksempel.

Søkeord: eget prosjekt, Lovable, React, spilltester, test, testing, tilfeldige hendelser, TypeScript, verification, verifisering, Vite, Vitest

[Profil eller kort](repoer/prosjekter/Tombonator3000--vector-war-games.md) · [Kilde](https://github.com/Tombonator3000/vector-war-games)

### Tombonator3000/Voidcraft

Egen utviklingsfork av Blocks Beyond the Stars med Voidcraft-identitet og The Sleeper Signal-kampanje om prosedyriske verdener og kosmisk skrekk.

Mulig gjenbruk: Referanse for å bevare et Unity/.NET-vokselgrunnlag mens egne fortellinger, lokalisering, lagringsidentitet og en separat Windows-spilltestpipeline legges til.

Søkeord: .NET, AGPL, create, eget prosjekt, fork, fortelling, generate, generation, generer, generering, kosmisk skrekk, romspill, Unity, voksler

[Profil eller kort](repoer/prosjekter/Tombonator3000--Voidcraft.md) · [Kilde](https://github.com/Tombonator3000/Voidcraft)

### Tombonator3000/Wasteland-Racers



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/Wasteland-Racers)

### Tombonator3000/ZakMcKracken-HD



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/Tombonator3000/ZakMcKracken-HD)

### tscherrie/salmon-survival

Live one salmon's whole life in a Nordic river – a browser game (English, Deutsch, 中文)

Søkeord: browser, nettleser, web

[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/tscherrie/salmon-survival)

### xikhar/spiderbench



[Profil eller kort](OFFENTLIG_INVENTAR.md) · [Kilde](https://github.com/xikhar/spiderbench)

## Skills

### achimala/dream-loop:dream-loop

Build a game or app from a description so that a live screenshot matches a generated rendering. Use when the user says "dream loop" or asks for something built to a very high level of graphical fidelity.

Søkeord: create, dream-loop, generate, generation, generer, generering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/achimala/dream-loop/blob/9bddb901f7d071cfefdd21e264267c757177a9df/SKILL.md)

### arielshad/3d-asset-server:3d-assets

Find and download free 3D models, PBR textures/materials, HDRIs and game asset packs (glTF, FBX, Blend, EXR) from 24 sites like Poly Haven, ambientCG, Kenney and BlenderKit via https://3d.shep.bot, with licences. Use when the user needs 3D assets, textures, environment maps or game art for a project.

Søkeord: 3d-assets, content, model, modell, modeller, models, tekstur, teksturer, texture, textures

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/arielshad/3d-asset-server/blob/2efa8d8e284efc03fce5ebe6331e0d21de381c9f/web/src/content/SKILL.md)

### bilawalsidhu/gods-eye-view:community-pr

Review and integrate community pull requests in God's Eye View using its maintainer acceptance workflow. Use for contribution triage, PR acceptance reviews, or authorized integration; not for ordinary implementation work or opening the user's own PR.

Søkeord: community-pr

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/bilawalsidhu/gods-eye-view/blob/537e99dfa45a3f7b239ad6230a65be658b3ea29d/.agents/skills/community-pr/SKILL.md)

### collabs-inc/collab-public:collab-canvas

collab-electron/packages/collab-canvas-skill/skills/collab-canvas/SKILL.md

Søkeord: collab-canvas

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/collabs-inc/collab-public/blob/476b8efc942ee5f430a9b8bf832b8560a8cf76c2/collab-electron/packages/collab-canvas-skill/skills/collab-canvas/SKILL.md)

### debpalash/VoiceStudio:fastapi-python

Expert in FastAPI Python development with best practices for APIs and async operations

Søkeord: fastapi-python

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/debpalash/VoiceStudio/blob/f47221a1f0af89df27c34747471daa30391a9487/.agents/skills/fastapi-python/SKILL.md)

### debpalash/VoiceStudio:vite

Expert guidance for Vite development with modern build tooling, HMR, framework integrations, and performance optimization

Søkeord: vite

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/debpalash/VoiceStudio/blob/f47221a1f0af89df27c34747471daa30391a9487/.agents/skills/vite/SKILL.md)

### debpalash/VoiceStudio:voicestudio

Generate local speech with saved or designed voices, transcribe audio, and automate dubbing or narration workflows through VoiceStudio's REST API or MCP server. Use when the user wants to work with VoiceStudio audio or connect it to an agent or automation.

Søkeord: audio, create, generate, generation, generer, generering, lagre, lagring, lyd, lydeffekter, persistence, save, saving, sfx, sound, voicestudio

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/debpalash/VoiceStudio/blob/f47221a1f0af89df27c34747471daa30391a9487/skills/voicestudio/SKILL.md)

### debpalash/VoiceStudio:voicestudio-maintainer

Triage GitHub issues, review contributor pull requests, diagnose CI, and prepare explicitly requested releases for VoiceStudio's Electron desktop app and Python backend. Use for repository maintenance work, not ordinary VoiceStudio audio generation.

Søkeord: audio, create, generate, generation, generer, generering, lyd, lydeffekter, sfx, sound, voicestudio-maintainer

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/debpalash/VoiceStudio/blob/f47221a1f0af89df27c34747471daa30391a9487/skills/voicestudio-maintainer/SKILL.md)

### EpicGames/unreal-engine-skills-for-claude-code-plugin:create-toolset

Use this skill when authoring or extending an Unreal Engine toolset, a class of static, AI-callable functions registered with `ToolsetRegistry` and exposed through the unreal-mcp server. Trigger when the user wants to add, expose, or register a new tool method, create a new toolset, or extend an existing one such as `BlueprintTools`, `StaticMeshToo

Søkeord: create, create-toolset, generate, generation, generer, generering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/blob/a6aa73ada02a9fb1f5415bec491f9942c519b297/skills/create-toolset/SKILL.md)

### EpicGames/unreal-engine-skills-for-claude-code-plugin:unreal-mcp

Use this skill to perform actions inside an Unreal Engine project via a live-editor MCP connection. Trigger when the user wants to change, query, or run something in their Unreal Engine project, not for conceptual or docs questions. Concrete triggers: spawn/move/duplicate/transform actors in a level, open a `.uproject`, add things around a PlayerSt

Søkeord: browser, create, generate, generation, generer, generering, nettleser, recompilation, recompile, recompiler, rekompilering, unreal-mcp, web

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/blob/a6aa73ada02a9fb1f5415bec491f9942c519b297/skills/unreal-mcp/SKILL.md)

### EpicGames/unreal-engine-skills-for-claude-code-plugin:unreal-skill

Use this skill when creating, editing, or reviewing an Unreal Engine Agent Skill, a named bundle of instructions registered with the unreal-mcp server (distinct from Claude Code's harness skills under `.claude/skills/`). Trigger when the user wants to add or change a skill that the in-editor agent will load. Concrete triggers: 'create a new Agent S

Søkeord: create, generate, generation, generer, generering, unreal-skill

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/blob/a6aa73ada02a9fb1f5415bec491f9942c519b297/skills/unreal-skill/SKILL.md)

### GLinnik21/plx-native:bind-tv-lib-abi

Bind a new function or struct field from one of the TV's own native libraries — FFmpeg (libavformat / libavcodec / libavutil / libswscale), libcurl, or the C++ StarfishMediaAPIs / ACB seam. Use when adding a demuxer, encoder, decoder, muxer, Starfish or ACB call; when adding a whole new stubbed `.so`; when a link fails with "undefined reference to

Søkeord: bind-tv-lib-abi

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/GLinnik21/plx-native/blob/e8125923db9eb27cf0ffb8f45321e01be57b04dd/.agents/skills/bind-tv-lib-abi/SKILL.md)

### GLinnik21/plx-native:crash-triage

Diagnose the app dying on the TV — a crash, a SIGSEGV/SIGILL/SIGABRT, a black screen, the app vanishing mid-run, a harness case failing with "no line found", or the app refusing to relaunch. Symbolizes the crash tracer's raw program counter to a function (or file:line), routes by signal to the right evidence, and rules out the impostors that look l

Søkeord: crash-triage

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/GLinnik21/plx-native/blob/e8125923db9eb27cf0ffb8f45321e01be57b04dd/.agents/skills/crash-triage/SKILL.md)

### GLinnik21/plx-native:cut-release

Cut and publish a release of this app — bump the version, build the .ipk, write the release note, publish through CI, and update the webosbrew listing and PR. Use this whenever the user asks to release, ship, publish, cut, tag or bump a version ("cut 0.2.2", "ship a release", "tag a new version", "put out a build", "release notes for the next one")

Søkeord: audio, cut-release, lyd, lydeffekter, sfx, sound

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/GLinnik21/plx-native/blob/e8125923db9eb27cf0ffb8f45321e01be57b04dd/.agents/skills/cut-release/SKILL.md)

### GLinnik21/plx-native:decompile-tv-lib

Read the TV's own closed, stripped native libraries — libplayerAPIs (StarfishMediaAPIs), libpf (the media pipeline), libAcbAPI, libcbe (the Chromium media stack), the DILE/VPQ layers — by harvesting them off the device and decompiling them locally with Ghidra. Use when a question can only be answered by what the firmware actually DOES: which JSON k

Søkeord: decompilation, decompile, decompile-tv-lib, decompiler, dekompilering, matching decompilation

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/GLinnik21/plx-native/blob/e8125923db9eb27cf0ffb8f45321e01be57b04dd/.agents/skills/decompile-tv-lib/SKILL.md)

### GLinnik21/plx-native:fleet-plan

Plan and launch parallel agent work in this repo — several agents, several git worktrees, one physical television. Use when the ask is "fan this out", "run these in parallel", "use several agents", "spin up a fleet", "split this across worktrees", "can multiple agents work on this at once", and equally when nobody said any of that but you are about

Søkeord: fleet-plan

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/GLinnik21/plx-native/blob/e8125923db9eb27cf0ffb8f45321e01be57b04dd/.agents/skills/fleet-plan/SKILL.md)

### GLinnik21/plx-native:profile-tv

Diagnose a live PlxNative process that is slow, janky, frozen or consuming unexpected CPU/GPU on the rooted LG TV. Use for stack samples, a missing heartbeat while the PID still exists, frame pacing, Mali IRQ activity, HWCNT attribution, or deciding which graphics profiler explains a regression. If the process died, use crash-triage instead.

Søkeord: profile-tv

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/GLinnik21/plx-native/blob/e8125923db9eb27cf0ffb8f45321e01be57b04dd/.agents/skills/profile-tv/SKILL.md)

### GLinnik21/plx-native:setup-environment

Set up (or repair) the cross-compile build environment for this native webOS TV app on a macOS host — the webOS NDK toolchain, the pinned stable Rust toolchain (with its armv7 rust-std) needed for the static lib, and the sysroot the Makefile links against. Use this whenever the build environment isn't ready or is broken: a fresh clone, a new machin

Søkeord: setup-environment

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/GLinnik21/plx-native/blob/e8125923db9eb27cf0ffb8f45321e01be57b04dd/.agents/skills/setup-environment/SKILL.md)

### GLinnik21/plx-native:tv-lock

Take, hold and hand back the ONE dev television, so two jobs never drive it at once. Use before ANY device work — "deploy to the TV", "run the test suite", "screenshot the TV", "reproduce it on device", "measure the frame rate", "capture the video plane" — and whenever a command is refused with "the television is held by another lane", "BLOCKED: th

Søkeord: test, testing, tv-lock, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/GLinnik21/plx-native/blob/e8125923db9eb27cf0ffb8f45321e01be57b04dd/.agents/skills/tv-lock/SKILL.md)

### GLinnik21/plx-native:tv-session

Boot the app on the LG webOS dev TV into a chosen screen, inspect it, drive it live, collect screenshots or logs, and hand the TV back. Use for on-device UI or playback verification, reproducing a bug on the set, navigating a live screen, capturing the video plane, or giving the user a live view. Also covers off-network phone/Safari access through

Søkeord: test, testing, tv-session, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/GLinnik21/plx-native/blob/e8125923db9eb27cf0ffb8f45321e01be57b04dd/.agents/skills/tv-session/SKILL.md)

### GLinnik21/plx-native:ui-sim

Verify UI and Plex data-layer changes in the macOS or Windows/WSLg desktop simulator. Use it for layout, focus, navigation, screenshots, local app runs, and simulator-based validation when a TV is unavailable or unnecessary. It also defines which results still require `tv-session`, including TV frame rate, LG decoding, text rasterization, and the v

Søkeord: ui-sim

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/GLinnik21/plx-native/blob/e8125923db9eb27cf0ffb8f45321e01be57b04dd/.agents/skills/ui-sim/SKILL.md)

### GLinnik21/plx-native:wake-tv

Wake the LG webOS dev TV from standby via Wake-on-LAN and wait for SSH — run this whenever the TV is unreachable, asleep, timing out, or "connection refused / operation timed out" before a deploy, test run, capture, or stream session. Also: put the TV into standby, or check whether it is up.

Søkeord: test, testing, verification, verifisering, wake-tv

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/GLinnik21/plx-native/blob/e8125923db9eb27cf0ffb8f45321e01be57b04dd/.agents/skills/wake-tv/SKILL.md)

### GLinnik21/plx-native:which-tier

Decide WHICH verification tier a change actually needs — and, the half that gets skipped, which tiers are structurally blind to it. Use whenever the question is "how do I verify this", "what should I run", "is make check enough", "do I need the television for this", "which suite covers this", "did I run the right one", or before calling anything ve

Søkeord: animasjon, animate, animated, animation, animations, animere, test, testing, verification, verifisering, which-tier

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/GLinnik21/plx-native/blob/e8125923db9eb27cf0ffb8f45321e01be57b04dd/.agents/skills/which-tier/SKILL.md)

### i12bp8/decomp.wtf:decompile

Decompile a game the user owns (ROM, disc image, ISO, executable) into matching C with decomp.wtf. Use when the user asks to decompile, decomp, reverse engineer, port or mod a game, or to match a game's functions byte for byte (N64, PlayStation 1 and 2, GameCube, Wii, Game Boy Advance, DS, or a public decomp of any platform).

Søkeord: decompilation, decompile, decompiler, dekompilering, matching decompilation

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/i12bp8/decomp.wtf/blob/575b4a30ed481ff5497dfb9ce4f599368a95a04a/plugins/decomp-wtf/skills/decompile/SKILL.md)

### JesusGalindez/threejs-ocean-simulator-skills:agua-y-objetos

Cómo hacer que los objetos interactúen con el agua de forma física - barcos y boya que flotan con inercia, estela de Kelvin simulada, ola de proa, hueco de popa, agua aireada, rocío por contacto con el casco, espuma, reflejo y sombra real del barco - en oceano-fft-threejs.html (three.js/WebGL2). Úsala al añadir un barco u objeto flotante, al tocar

Søkeord: agua-y-objetos, bølger, hav, ocean, sea, three js, three.js, threejs, vann, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/JesusGalindez/threejs-ocean-simulator-skills/blob/cdbebd2105e0679182d0eac4770d4f4e51d9ef2b/.agents/skills/agua-y-objetos/SKILL.md)

### JesusGalindez/threejs-ocean-simulator-skills:cielo-y-nubes

Cómo construir un cielo físico con nubes volumétricas creíbles (cúmulos individuales, estratocúmulos, altocúmulos, cirros, bancos en el horizonte) horneado a un mapa que comparten la cúpula y el reflejo del mar, en three.js/WebGL2. Úsala al crear o retocar cielo, atmósfera, puesta de sol, noche, nubes, su sombra sobre el mar o los tipos de cielo de

Søkeord: bølger, cielo-y-nubes, hav, ocean, sea, three js, three.js, threejs, vann, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/JesusGalindez/threejs-ocean-simulator-skills/blob/cdbebd2105e0679182d0eac4770d4f4e51d9ef2b/.agents/skills/cielo-y-nubes/SKILL.md)

### JesusGalindez/threejs-ocean-simulator-skills:oceano-realista

Cómo se hace el mar realista de oceano-fft-threejs.html - oleaje espectral de Tessendorf con FFT en GPU, espectro de Elfouhaily en tres cascadas, malla proyectada, rugosidad por varianza de pendiente, Fresnel exacto, absorción de Jerlov, espuma por jacobiano calibrada con Monahan, rachas, lluvia, bruma y vista submarina. Úsala al tocar el oleaje, e

Søkeord: bølger, hav, ocean, oceano-realista, sea, three js, three.js, threejs, vann, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/JesusGalindez/threejs-ocean-simulator-skills/blob/cdbebd2105e0679182d0eac4770d4f4e51d9ef2b/.agents/skills/oceano-realista/SKILL.md)

### JesusGalindez/threejs-ocean-simulator-skills:threejs-water-optics

Build production analytic and bounded water in Three.js. Use for shared multi-wave displacement and normals, bounded RGBA heightfield pool simulation, local drops, object-driven ripples, differential-area caustics, ray-traced pool/water/sphere volume optics, derivative-filtered normal bands, analytic sky reflection, side-aware Fresnel, heuristic sc

Søkeord: bølger, hav, ocean, reflection, reflections, refleksjon, refleksjoner, sea, three js, three.js, threejs, threejs-water-optics, vann, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/JesusGalindez/threejs-ocean-simulator-skills/blob/cdbebd2105e0679182d0eac4770d4f4e51d9ef2b/referencias/threejs-skills/skills/threejs-water-optics/SKILL.md)

### JesusGalindez/threejs-ocean-simulator-skills:verificar-en-gpu-real

Método para verificar efectos visuales y de rendimiento en WebGL con GPU real antes de entregarlos - sonda en Safari con escenas JSON, capturas y medidas por escena, A/B alternado de fps, convertir lo visual en números, estabilidad temporal (parpadeos), aislar causas con copias de prueba y comparar con un vídeo de referencia. Úsala después de cualq

Søkeord: bølger, hav, ocean, sea, three js, three.js, threejs, vann, verificar-en-gpu-real, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/JesusGalindez/threejs-ocean-simulator-skills/blob/cdbebd2105e0679182d0eac4770d4f4e51d9ef2b/.agents/skills/verificar-en-gpu-real/SKILL.md)

### JesusGalindez/threejs-ocean-simulator-skills:yate-procedural

Cómo modelar un yate a motor realista por código en three.js (sin archivos 3D) - plano de formas del casco a partir de fotos, casco de planeo con pantoque duro, cubiertas, timonera, techo, muebles, interior completo con camarotes, baño y sala de máquinas, texturas de lienzo, cortes para ver dentro, verificación contra fotos y cómo meterlo en el mar

Søkeord: bølger, hav, model, modell, modeller, models, ocean, sea, three js, three.js, threejs, vann, water, waves, yate-procedural

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/JesusGalindez/threejs-ocean-simulator-skills/blob/cdbebd2105e0679182d0eac4770d4f4e51d9ef2b/.agents/skills/yate-procedural/SKILL.md)

### lhlGitHub/threejs-architecture-effects:threejs-architecture-effects

Build or refine real Three.js architectural construction animations, especially Chinese pavilions, pagodas and clock towers with brick-by-brick growth, timber framing, layered eaves, procedural PBR materials and interactive detail cameras. Use for 3D建筑生长、古建搭建特效、楼台逐层建造、建筑动态组装 or similar architectural miniatures; not for flat image reveals or generic

Søkeord: animasjon, animate, animated, animation, animations, animere, camera, cameras, kamera, kameraføring, three js, three.js, threejs, threejs-architecture-effects

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/lhlGitHub/threejs-architecture-effects/blob/693ca2ec1193e7355054f14d7deb1427439a24d0/SKILL.md)

### morbidium-spritesheets

Create consistent animated 2D character sprite sheets, paper-doll art, and effect sheets for the Morbidium Three.js game, with frame validation, atlases, metadata, visual QA, and a handoff Claude can integrate. Use for requests to animate a Morbidium character, make a spritesheet/spriteark, add directional walk/attack/death frames, or prepare game-

Søkeord: animasjon, animate, animated, animation, animations, animere, atlas, character, character sheet, characters, create, figur, figurark, figurer, generate, generation, generer, generer spriteark, generering, morbidium-spritesheets, paper doll, sprite sheet, sprite sheets, spriteark, spritesheet, spritesheets, three js, three.js, threejs

[Profil eller kort](skills/morbidium-spritesheets/SKILL.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/skills/morbidium-spritesheets/SKILL.md)

### morluto/rea:rea-changelog-update

Prepare or rewrite REA release changelogs and GitHub release notes from pinned Git history, with verified contributor thanks and Release Please synchronization.

Søkeord: rea-changelog-update

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/morluto/rea/blob/9a82046b07244e62df22076b64ded05ff9abc5db/.agents/skills/rea-changelog-update/SKILL.md)

### morluto/rea:rea-ci-tests-audit

Audit REA CI and test suites for correctness, fixture drift, false passes, and measured performance; use for suite or workflow investigations and efficiency changes, rather than ordinary feature testing or a single test failure.

Søkeord: rea-ci-tests-audit, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/morluto/rea/blob/9a82046b07244e62df22076b64ded05ff9abc5db/.agents/skills/rea-ci-tests-audit/SKILL.md)

### morluto/rea:rea-tool-design

Design or change REA investigation tools, CLI/MCP contracts, provider capabilities, and Evidence semantics.

Søkeord: rea-tool-design

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/morluto/rea/blob/9a82046b07244e62df22076b64ded05ff9abc5db/.agents/skills/rea-tool-design/SKILL.md)

### morluto/rea:reverse-engineer-anything

Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA. Use shipped-artifact or requested runtime evidence to explain features, compare versions, decompile code, or guide a reconstruction. Skip REA for ordinary source-repository architecture analysis.

Søkeord: browser, decompilation, decompile, decompiler, dekompilering, matching decompilation, nettleser, reverse-engineer-anything, web

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/morluto/rea/blob/9a82046b07244e62df22076b64ded05ff9abc5db/.agents/skills/reverse-engineer-anything/SKILL.md)

### multimodal-art-projection/YuE:yue2-instrumental

用 YuE2 生成纯音乐或制作纯音乐 cover。默认由 YuE2 写谱，自动将 Vocal 音符移到 Ins 后生成；只有用户明确要求 agent 作曲时才由 agent 写谱。支持文字描述、ABC 或音频参考，交付试听、真实 prompt 和转谱检查。

Søkeord: instrumental, yue2-instrumental

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/multimodal-art-projection/YuE/blob/1647252d68b70cbead046ffd3f7caf036dde47ee/skills/yue2-music/instrumental/SKILL.md)

### multimodal-art-projection/YuE:yue2-music

Generate instrumental music and songs, cover, transcribe, and edit with YuE2 and SheetSage2/MERT2. Use for text-to-instrumental generation, instrumental covers, YuE2 full/melody/off generation, audio-to-ABC covers, style or lyric changes, score editing, agentic reharmonization, melody preservation, singable lyric adaptation, and reproducible listen

Søkeord: audio, create, generate, generation, generer, generering, lyd, lydeffekter, music, musikk, sfx, sound, soundtrack, yue2-music

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/multimodal-art-projection/YuE/blob/1647252d68b70cbead046ffd3f7caf036dde47ee/skills/yue2-music/SKILL.md)

### neilsonnn/image-blaster:image-blast-3d

Generate one specified atomic 3D object. Use when the user names exactly one object instance to make, or provides one image plus the object name/description.

Søkeord: create, generate, generation, generer, generering, image-blast-3d

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/neilsonnn/image-blaster/blob/4acb43ba126a12358f71838d1b1a05e856b10eaf/.claude/skills/image-blast-3d/SKILL.md)

### neilsonnn/image-blaster:image-blast-image-edit

Generate one image edit from explicit input images and a prompt. Use for source cleanup, clean plates, object removal, or other FAL-backed image edits.

Søkeord: create, generate, generation, generer, generering, image-blast-image-edit

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/neilsonnn/image-blaster/blob/4acb43ba126a12358f71838d1b1a05e856b10eaf/.claude/skills/image-blast-image-edit/SKILL.md)

### neilsonnn/image-blaster:image-blast-plate

Generate one clean plate/source cleanup image for an IMAGE-BLASTER world. Use after confirmed objects exist, when removing foreground objects or other specified content from a source image.

Søkeord: create, generate, generation, generer, generering, image-blast-plate

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/neilsonnn/image-blaster/blob/4acb43ba126a12358f71838d1b1a05e856b10eaf/.claude/skills/image-blast-plate/SKILL.md)

### neilsonnn/image-blaster:image-blast-project

Create, inspect, and manage an IMAGE-BLAST project envelope under worlds/<slug>. Use before other image-blast skills (image-blast-uncover, image-blast-world, image-blast-3d, etc.) or whenever the user asks about active project state.

Søkeord: create, generate, generation, generer, generering, image-blast-project

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/neilsonnn/image-blaster/blob/4acb43ba126a12358f71838d1b1a05e856b10eaf/.claude/skills/image-blast-project/SKILL.md)

### neilsonnn/image-blaster:image-blast-sfx

Generate and post-process a clean sound effect, object impact, or ambient loop.

Søkeord: audio, create, generate, generation, generer, generering, image-blast-sfx, lyd, lydeffekter, sfx, sound

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/neilsonnn/image-blaster/blob/4acb43ba126a12358f71838d1b1a05e856b10eaf/.claude/skills/image-blast-sfx/SKILL.md)

### neilsonnn/image-blaster:image-blast-uncover

Main image analysis skill, object generation, plate decisionmaking, and initial scene description. Use this skill when user wants to create objects and necessary for main image analysis.

Søkeord: create, generate, generation, generer, generering, image-blast-uncover, scene, scener, scenes

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/neilsonnn/image-blaster/blob/4acb43ba126a12358f71838d1b1a05e856b10eaf/.claude/skills/image-blast-uncover/SKILL.md)

### neilsonnn/image-blaster:image-blast-wildcard

Discover and run any FAL API model or operation the user requests. Use this as a generic FAL escape hatch when the user wants to generate something that does not fit a narrower Image Blast skill.

Søkeord: create, generate, generation, generer, generering, image-blast-wildcard, model, modell, modeller, models

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/neilsonnn/image-blaster/blob/4acb43ba126a12358f71838d1b1a05e856b10eaf/.claude/skills/image-blast-wildcard/SKILL.md)

### neilsonnn/image-blaster:image-blast-world

Generate the 3D static environment of a world from a source or plate image.

Søkeord: create, generate, generation, generer, generering, image-blast-world

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/neilsonnn/image-blaster/blob/4acb43ba126a12358f71838d1b1a05e856b10eaf/.claude/skills/image-blast-world/SKILL.md)

### OpenCloudGaming/OpenNOW:frontend-design

Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, artifacts, posters, or applications (examples include websites, landing pages, dashboards, React components, HTML/CSS layouts, or when styling/beautifying any web UI). Generates creative, polished code

Søkeord: browser, create, frontend-design, generate, generation, generer, generering, nettleser, web

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/OpenCloudGaming/OpenNOW/blob/60ce69a07bf94ba484af7406d386ccb28e5a13e6/.agents/skills/frontend-design/SKILL.md)

### OpenCloudGaming/OpenNOW:new-pr-and-branch

Create a new branch, commits changes, then opens pr against the dev branch.

Søkeord: create, generate, generation, generer, generering, new-pr-and-branch

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/OpenCloudGaming/OpenNOW/blob/60ce69a07bf94ba484af7406d386ccb28e5a13e6/.agents/skills/new-pr-and-branch/SKILL.md)

### prosjektbibliotek

Finn eksisterende løsninger, verktøy og skills i Tombonator3000/prosjektbibliotek før implementering, feilsøking eller verktøyvalg i Toms prosjekter.

Søkeord: prosjektbibliotek

[Profil eller kort](skills/prosjektbibliotek/SKILL.md) · [Kilde](https://github.com/Tombonator3000/prosjektbibliotek/blob/main/skills/prosjektbibliotek/SKILL.md)

### rehan-remade/universal-modder:asset-pipeline

Turn generated or hand-made art into exactly what a game engine loads. Covers sprite cutout, trim and nearest-neighbour fitting to frame sizes, pixelation to a palette, sprite sheets and strips, player/team-colour masks, seamless textures, and rendering a 3D model into sprite frames from the game's own camera (isometric/RTS 8 or 16 headings, side v

Søkeord: animasjon, animate, animated, animation, animations, animere, asset-pipeline, camera, cameras, character sheet, create, figurark, generate, generation, generer, generering, kamera, kameraføring, model, modell, modeller, models, sprite sheet, sprite sheets, spriteark, spritesheet, spritesheets, tekstur, teksturer, texture, textures

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/rehan-remade/universal-modder/blob/23902ef42e8ea9b077bfbbf6911eb8ea0348e55a/skills/asset-pipeline/SKILL.md)

### rehan-remade/universal-modder:fal-assets

Generate game assets with fal (fal.ai) through the fal MCP server, the `um fal` CLI (REST) or `fal api`. Covers sprites and icons with transparent backgrounds, consistent variants and animation frames, pixel art, seamless textures, PBR material maps, image-to-3D models, remeshing, auto-rigging, sound effects, music, voice lines, and trailer or cuts

Søkeord: 3d fra bilde, alfa, alpha, animasjon, animate, animated, animation, animations, animere, audio, bilde til 3d, create, fal-assets, generate, generation, generer, generering, gjennomsiktig, gjennomsiktighet, image to 3d, image to mesh, lyd, lydeffekter, model, modell, modeller, models, music, musikk, sfx, sound, soundtrack, tekstur, teksturer, texture, textures, transparency, transparent

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/rehan-remade/universal-modder/blob/23902ef42e8ea9b077bfbbf6911eb8ea0348e55a/skills/fal-assets/SKILL.md)

### rehan-remade/universal-modder:game-automation

Launch, see and drive a real game so an agent can test its own mods. Covers launching via Steam or the exe, windowed mode at a fixed size, screenshots of the game window (GPU-safe capture), clicking and typing into menus, holding keys, relative mouse, crash-reporter cleanup, killing by PID, reading logs, scripted test scenes, and an in-game JSON br

Søkeord: game-automation, scene, scener, scenes, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/rehan-remade/universal-modder/blob/23902ef42e8ea9b077bfbbf6911eb8ea0348e55a/skills/game-automation/SKILL.md)

### rehan-remade/universal-modder:game-recon

Figure out how a specific installed game can be modded, before writing any mod code. Covers where it's installed, the engine and version, managed vs native code, anti-cheat, loaders already present, save and config folders, and the community's modding route. Use when the user asks "can I mod <game>?", "what engine is <game>", "how do people mod <ga

Søkeord: character, characters, figur, figurer, game-recon, lagre, lagring, persistence, save, saving

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/rehan-remade/universal-modder/blob/23902ef42e8ea9b077bfbbf6911eb8ea0348e55a/skills/game-recon/SKILL.md)

### rehan-remade/universal-modder:game-research-websearch

Research a game, engine or modding technique on the open web with archive-aware, rate-limit-safe searches — Wayback Machine/archive.today for dead forums (XeNTaX, Zenhax, old threads), GitHub code/repo search, Nexus/Steam Workshop/Thunderstore APIs, Reddit JSON, YouTube transcripts, plus archive snapshots as evidence. Use when starting work on a ga

Søkeord: browser, game-research-websearch, nettleser, web

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/rehan-remade/universal-modder/blob/23902ef42e8ea9b077bfbbf6911eb8ea0348e55a/skills/game-research-websearch/SKILL.md)

### rehan-remade/universal-modder:mashup-mods

Build cross-game mashups and total conversions, the "Minecraft inside Elden Ring" or "skateboarding in MW2" kind. Covers passthrough mods (two games running at once and exchanging state, rendering and collision), porting one game's content or mechanics into another, embedding a decompiled game as a library, and clean reimplementations that read the

Søkeord: collision, collisions, decompilation, decompile, decompiler, dekompilering, kollisjon, mashup-mods, matching decompilation

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/rehan-remade/universal-modder/blob/23902ef42e8ea9b077bfbbf6911eb8ea0348e55a/skills/mashup-mods/SKILL.md)

### rehan-remade/universal-modder:mod-any-game

Mod a PC game the user owns, taking an idea to working in the real game and recorded. It covers new items, weapons, enemies, bosses, units, civilizations, mechanics, art, sound, VR and cross-game mashups. Use when the user wants to mod, extend, hack on, reverse engineer or mash up a game ("add a nuke to Terraria", "make a new civ for Age of Empires

Søkeord: audio, create, generate, generation, generer, generering, lyd, lydeffekter, mod-any-game, sfx, sound, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/rehan-remade/universal-modder/blob/23902ef42e8ea9b077bfbbf6911eb8ea0348e55a/skills/mod-any-game/SKILL.md)

### rehan-remade/universal-modder:port-a-mod

Port an existing mod to a newer game version or another mod loader while keeping its behaviour, values and quirks. Typical cases are an old Forge 1.7.10 or 1.12 Minecraft mod moving to modern Fabric or NeoForge, a Skyrim LE plugin moving to SE/AE, or a tModLoader 1.3 mod moving to 1.4. It covers pinning one source version, a private decompiled refe

Søkeord: decompilation, decompile, decompiler, dekompilering, matching decompilation, port-a-mod, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/rehan-remade/universal-modder/blob/23902ef42e8ea9b077bfbbf6911eb8ea0348e55a/skills/port-a-mod/SKILL.md)

### rehan-remade/universal-modder:publish-mod

Package and release a finished game mod. Covers the pre-release lint (no game files, decompiled code or leaked keys), README and install steps, credits and AI disclosure, versioning, where to upload (Nexus Mods, Steam Workshop, Thunderstore, mod.io, GitHub releases), and the post with a video. Use when the user wants to ship, share, upload, release

Søkeord: decompilation, decompile, decompiler, dekompilering, matching decompilation, publish-mod

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/rehan-remade/universal-modder/blob/23902ef42e8ea9b077bfbbf6911eb8ea0348e55a/skills/publish-mod/SKILL.md)

### rehan-remade/universal-modder:reverse-engineering

Read how a game actually works so a mod can hook it. Decompile .NET/Mono (ILSpy), IL2CPP (Cpp2IL, Il2CppDumper), Java (Vineflower) and native code (Ghidra, IDA, via MCP servers); dump data and asset formats; reverse-engineer a binary file format and prove it with a round trip; read live memory (Cheat Engine, Frida, x64dbg); find render passes (Rend

Søkeord: binary analysis, binæranalyse, decompilation, decompile, decompiler, dekompilering, matching decompilation, reverse engineering, reverse-engineering, reversering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/rehan-remade/universal-modder/blob/23902ef42e8ea9b077bfbbf6911eb8ea0348e55a/skills/reverse-engineering/SKILL.md)

### rehan-remade/universal-modder:share-field-notes

Search and contribute to the shared AI-modding knowledge base, where field notes record how specific games were modded, decompiled or reverse-engineered (exact versions, route, engine facts, verification, gotchas). Use before starting work on a game ("has anyone modded X?"), when stuck on an engine quirk, and at the end of any modding or reverse-en

Søkeord: binary analysis, binæranalyse, decompilation, decompile, decompiler, dekompilering, matching decompilation, reverse engineering, reversering, share-field-notes, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/rehan-remade/universal-modder/blob/23902ef42e8ea9b077bfbbf6911eb8ea0348e55a/skills/share-field-notes/SKILL.md)

### rehan-remade/universal-modder:showcase-video

Record and cut a short showcase video of a game mod, or a compilation of clips, ready to post on X/YouTube. Records the game window with only the game's own audio, picks moments from contact sheets, and edits with one-line animated titles, creator credits, transitions, music, watermark and fade-out via an EDL JSON. Use when the user wants a demo vi

Søkeord: animasjon, animate, animated, animation, animations, animere, audio, bølger, hav, lyd, lydeffekter, music, musikk, ocean, sea, sfx, showcase-video, sound, soundtrack, vann, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/rehan-remade/universal-modder/blob/23902ef42e8ea9b077bfbbf6911eb8ea0348e55a/skills/showcase-video/SKILL.md)

### scenario-labs/skills:pr-handle-comments

Handle review comments received on GitHub for the current branch's PR or a given PR number or URL, by triaging each unresolved thread, fixing what is warranted, pushing, and replying in each thread, when asked to address, fix or answer PR comments. Works in any Scenario repository.

Søkeord: pr-handle-comments

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/.agents/skills/pr-handle-comments/SKILL.md)

### scenario-labs/skills:pr-squash-message

Generate one short Conventional Commits squash message describing only the net diff between the PR's base and head, set its header as the PR title, validate it with the repository's commitlint and both copy its description to the clipboard and display it, when asked for a squash message. Works in any Scenario repository, whatever its default branch

Søkeord: create, generate, generation, generer, generering, pr-squash-message

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/.agents/skills/pr-squash-message/SKILL.md)

### scenario-labs/skills:pr-summary

Refresh the current pull request description from its net changes, following the repository's PR template, when asked to update or write the PR summary. Works in any Scenario repository, whatever its default branch.

Søkeord: pr-summary

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/.agents/skills/pr-summary/SKILL.md)

### scenario-labs/skills:scenario

Use when connecting an AI agent to Scenario (scenario.com) through MCP, or when a task involves generating images, video, 3D, audio, sprites, textures, or game assets. Also when picking a Scenario model, running a LoRA, refining a generation prompt, uploading reference images, waiting on generation jobs, checking credits or quota, hitting Scenario

Søkeord: audio, create, generate, generation, generer, generering, lyd, lydeffekter, model, modell, modeller, models, scenario, sfx, sound, tekstur, teksturer, texture, textures

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario/SKILL.md)

### scenario-labs/skills:scenario-3d

Use when generating or handling 3D assets through the Scenario MCP server, including text-to-3D or image-to-3D meshes, GPT-6 Astra 3D or Claude Opus 5.5 3D, GLB, FBX, OBJ, STL, or VOX files, PBR-textured or game-ready models, voxel models, multi-view reconstruction, editing a mesh by prompt, retexture, remesh, UV unwrap, auto-rigging a biped or qua

Søkeord: 3d fra bilde, animasjon, animate, animated, animation, animations, animere, bevegelsesoverføring, bilde til 3d, image to 3d, image to mesh, model, modell, modeller, models, retarget, retargeting, scenario-3d, tekstur, teksturer, texture, textures

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-3d/SKILL.md)

### scenario-labs/skills:scenario-3d-worlds

Use when generating navigable 3D worlds or Gaussian splat scenes on Scenario via MCP: text-to-world, image-to-world, a 360 panorama or skybox turned into a walkable splat, multi-view photos or a video walkthrough reconstructed as a splat, or one object photo to splat. Keywords: World Labs Marble 1.1, 1.1 Plus, 1.0 Draft, Hunyuan World, HY World, im

Søkeord: 3dgs, create, gaussian splatting, gaussiske splats, generate, generation, generer, generering, scenario-3d-worlds, scene, scener, scenes, splat, splats

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-3d-worlds/SKILL.md)

### scenario-labs/skills:scenario-ace-step

Use when creating or editing music with ACE-Step models on Scenario via MCP: text-to-music songs with sung vocals from a lyric sheet, instrumental tracks, covering or restyling an existing song, repainting one section in place, changing sung lyrics, adding an instrument layer, completing a partial recording into a full arrangement, extracting stems

Søkeord: model, modell, modeller, models, music, musikk, scenario-ace-step, soundtrack

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-ace-step/SKILL.md)

### scenario-labs/skills:scenario-ad-variants

Use when making multiple independent ad or campaign edits from existing footage with Scenario: hook, CTA, copy, end-card, placement, or targeted visual variants. Also for revising one variant or resuming a partially completed batch. Not for a new commercial from a still image, ordinary single-clip grading, or automatic Cartesian combinations.

Søkeord: scenario-ad-variants

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-ad-variants/SKILL.md)

### scenario-labs/skills:scenario-admin-analytics

Use when answering Scenario admin analytics questions about Creative Unit consumption, most-used models, usage by user or project, AI adoption observability, cached usage data, CSV exports, enterprise PDF reports with charts, or a local analytics dashboard. Keywords: usage API, CU, analytics, adoption, reporting, consumption, cache.

Søkeord: model, modell, modeller, models, scenario-admin-analytics

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-admin-analytics/SKILL.md)

### scenario-labs/skills:scenario-asset-analysis

Use when finished Scenario assets have to give something back: a caption for a dataset or alt text, a reusable style description, a verdict against a brief, a canny, depth, pose, or segmentation control map for the next model, or the asset itself found again by text, tags, or visual similarity and filed into a collection. Keywords: caption, describ

Søkeord: model, modell, modeller, models, scenario-asset-analysis

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-asset-analysis/SKILL.md)

### scenario-labs/skills:scenario-audio

Use when generating or handling audio on Scenario via MCP. Triggers include music tracks, full-length songs with vocals written from lyrics, background scores, soundtracks, game sound effects, SFX, foley, ambience, looping audio, voiceover, narration, speech, TTS, text-to-speech, dialogue, voice cloning, re-voicing a recording, scoring or adding so

Søkeord: audio, create, generate, generation, generer, generering, lyd, lydeffekter, music, musikk, scenario-audio, sfx, sound, soundtrack

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-audio/SKILL.md)

### scenario-labs/skills:scenario-blender-animation

Use when animating characters or objects in Blender through Python, a bouncing ball, walk or run cycle, jump, acting shot, lip sync, eye darts or facial animation, blocking in stepped keys, splining, polish, timing and spacing, arcs, overlap, squash and stretch, graph editor handles, slotted actions or NLA layers, staging a playblast, or when anima

Søkeord: animasjon, animate, animated, animation, animations, animere, character, characters, figur, figurer, scenario-blender-animation

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/blender/scenario-blender-animation/SKILL.md)

### scenario-labs/skills:scenario-blender-expert

Use when doing any 3D work in Blender through Python or an MCP bridge, headless or in a live session: modeling, sculpting a character or head, retopology, UV unwrapping, baking, texturing, rigging, animating, previs, geometry nodes, lighting and rendering, grease pencil, or finishing an AI-generated mesh into a production asset. Also when a bpy scr

Søkeord: character, characters, create, figur, figurer, generate, generation, generer, generering, model, modell, modeller, models, scenario-blender-expert

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/blender/scenario-blender-expert/SKILL.md)

### scenario-labs/skills:scenario-blender-geometry-nodes

Use when building or debugging Geometry Nodes, headless or live: procedural modeling, scattering objects on a surface, arrays along a curve, repeat or for-each loops, simulation zones, 5.2 physics (cloth, colliders, forces, effectors), closures, bundles, matrices, node-group assets with gizmos. Also when a GN script links nothing, shows red links,

Søkeord: model, modell, modeller, models, scenario-blender-geometry-nodes

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/blender/scenario-blender-geometry-nodes/SKILL.md)

### scenario-labs/skills:scenario-blender-grease-pencil

Use when drawing or animating with Grease Pencil in Blender 5.x from Python: 2D or 2.5D illustration, frame-by-frame animation, a cutout or part-based 2D character, strokes with pressure, filled shapes with holes, in-betweens and interpolation, onion skin, Line Art outlines, strokes on 3D meshes, NPR or hybrid motion graphics. Also when GP code fai

Søkeord: animasjon, animate, animated, animation, animations, animere, character, characters, figur, figurer, scenario-blender-grease-pencil

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/blender/scenario-blender-grease-pencil/SKILL.md)

### scenario-labs/skills:scenario-blender-hair

Use when grooming hair or fur in Blender with hair curves, such as a character hairstyle, animal fur, procedural fur in geometry nodes, or hair cards and mesh hair for games. Also covers the Essentials hair node assets (Interpolate, Clump, Curl, Frizz, Noise, Trim), density masks, bald spots, parting lines, strand shading in Cycles or EEVEE, and sl

Søkeord: character, characters, figur, figurer, scenario-blender-hair

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/blender/scenario-blender-hair/SKILL.md)

### scenario-labs/skills:scenario-blender-hard-surface

Use when modeling hard-surface objects in Blender (sci-fi panels, props, weapons, vehicles, robots, machined or product parts) with booleans and cutters, bevel modifiers, weighted normals, or subdivision with support loops or creases. Also when shading is broken (smears on flat faces, stretching near a cut, pinching), a bevel shrinks or vanishes af

Søkeord: model, modell, modeller, models, scenario-blender-hard-surface

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/blender/scenario-blender-hard-surface/SKILL.md)

### scenario-labs/skills:scenario-blender-lighting-rendering

Use when lighting, rendering or compositing in Blender: light a character, product or hero shot, interior at dusk or night, three-point or motivated lighting, sun and sky, HDRI, EEVEE vs Cycles settings, light leaks or noise, flat or muddy renders, subject not standing out, AgX/ACES color management, render passes, EXR, light groups, bloom and vign

Søkeord: bloom, character, characters, figur, figurer, gloed, glow, glowing, glød, scenario-blender-lighting-rendering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/blender/scenario-blender-lighting-rendering/SKILL.md)

### scenario-labs/skills:scenario-blender-previs-storyboard

Use when turning a script or story into previs, layout, storyboards or an animatic in Blender: beats to shot list, camera and lens per shot, staging, camera height, 180-degree rule, screen direction, shot sizes, when to cut, camera moves, timing stills in the Video Sequencer, markers bound to cameras, Story Tools, Grease Pencil or 2D/3D hybrid boar

Søkeord: camera, cameras, kamera, kameraføring, scenario-blender-previs-storyboard

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/blender/scenario-blender-previs-storyboard/SKILL.md)

### scenario-labs/skills:scenario-blender-retopology

Use when turning a dense sculpt, scan or AI-generated mesh into clean topology in Blender, for animation, subdivision or a game low poly with a triangle budget. Also when choosing between QuadriFlow or voxel remesh and manual retopo, placing loops around eyes, mouth and joints, deciding pole placement, setting up a Shrinkwrap cage, fixing volume lo

Søkeord: animasjon, animate, animated, animation, animations, animere, create, generate, generation, generer, generering, scenario-blender-retopology

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/blender/scenario-blender-retopology/SKILL.md)

### scenario-labs/skills:scenario-blender-rigging

Use when rigging a character, creature or prop in Blender through Python: "rig this character", Rigify metarig fitting or generation errors, automatic weights or "Bone Heat Weighting failed", weight painting fixes, clothes that do not follow, IK/FK switch, foot roll, twist bones, drivers and custom properties, corrective shape keys, a stylized face

Søkeord: character, characters, create, figur, figurer, generate, generation, generer, generering, scenario-blender-rigging, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/blender/scenario-blender-rigging/SKILL.md)

### scenario-labs/skills:scenario-blender-sculpting

Use when sculpting in Blender through Python: sculpt a head, face or bust, a stylized or cartoon character, a creature or a realistic portrait; block out from primitives; cut planes, a jaw or gonial angle, cheekbones; fix a jaw or face that looks like a ball or balloon; stylized hair clumps; eyelids; an expression or smirk; plan remesh or multires

Søkeord: character, characters, figur, figurer, scenario-blender-sculpting

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/blender/scenario-blender-sculpting/SKILL.md)

### scenario-labs/skills:scenario-blender-texturing-shading

Use when texturing, shading or look-developing in Blender: building a PBR material from a texture set, displacement, procedural materials, edge wear, dirt, grime, color variation, decals, box or triplanar mapping on meshes without UVs, stylized character skin (subsurface, pores), eyes and cornea, hand-painted stylized textures, texture painting or

Søkeord: character, characters, figur, figurer, scenario-blender-texturing-shading, tekstur, teksturer, texture, textures

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/blender/scenario-blender-texturing-shading/SKILL.md)

### scenario-labs/skills:scenario-blender-uv-baking

Use when UV unwrapping, placing seams, straightening or packing UVs, setting texel density, laying out UDIMs or mirrored UVs, or baking normal, AO, curvature, ID or displacement maps from a sculpt or high poly onto a low poly or retopo in Blender, including Multires bakes. Also when a bake has black or inverted patches, flat areas, cracks, seams, w

Søkeord: scenario-blender-uv-baking

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/blender/scenario-blender-uv-baking/SKILL.md)

### scenario-labs/skills:scenario-brand-kit

Use when building a visual identity or brand kit with Scenario: a logo, wordmark, or icon as editable SVG, a color palette and typography spec, logo variants (mono, reversed, favicon), and brand applications like social templates, avatars, banners, or merchandise mockups. Also for a rebrand or refreshing an existing mark. Keywords: brandkit, brand

Søkeord: scenario-brand-kit

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-brand-kit/SKILL.md)

### scenario-labs/skills:scenario-caption-studio

Use when a video needs its spoken words on screen through Scenario via MCP: burned-in styled captions for a TikTok, Reels, or Shorts cut, ad captions for sound-off feeds, YouTube subtitles, an SRT sidecar, transcription of a clip's audio, captions translated into another language, karaoke or word-by-word styles, or restyling and correcting an exist

Søkeord: audio, lyd, lydeffekter, scenario-caption-studio, sfx, sound

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-caption-studio/SKILL.md)

### scenario-labs/skills:scenario-chatgpt-pet-create

Use when creating a ChatGPT pet or Codex pet with Scenario: hatching an animated companion from a text idea, a character, mascot or brand cue, or reference photos and art; making the 1536x2288 v2 pet sprite sheet with nine animation states and sixteen look directions, the 1536x1872 v1 sheet ChatGPT web uploads, a pixel-perfect pixel-art pet, an ani

Søkeord: animasjon, animate, animated, animation, animations, animere, browser, character, character sheet, characters, create, figur, figurark, figurer, generate, generation, generer, generering, nettleser, scenario-chatgpt-pet-create, sprite sheet, sprite sheets, spriteark, spritesheet, spritesheets, web

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-chatgpt-pet-create/SKILL.md)

### scenario-labs/skills:scenario-chatgpt-pet-update

Use when changing an existing ChatGPT pet or Codex pet sprite sheet with Scenario: fixing a broken row, frame, jump or edge, regenerating one animation state, adding the sixteen look directions to a 1536x1872 v1 sheet, giving the pet a new outfit, color or accessory, renaming it in its pet.json, or checking a pet sheet and previewing it as an anima

Søkeord: animasjon, animate, animated, animation, animations, animere, character sheet, figurark, scenario-chatgpt-pet-update, sprite sheet, sprite sheets, spriteark, spritesheet, spritesheets

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-chatgpt-pet-update/SKILL.md)

### scenario-labs/skills:scenario-consistency

Use when one look must hold across Scenario generations: one character across scenes, a turnaround, or a video animated from its references, one product across angles, one style across icon sets, a character from an uploaded drawing, a variant off an approved baseline, or deciding when references stop scaling and a trained model is due. Triggers: m

Søkeord: animasjon, animate, animated, animation, animations, animere, character, characters, create, figur, figurer, generate, generation, generer, generering, model, modell, modeller, models, scenario-consistency, scene, scener, scenes

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-consistency/SKILL.md)

### scenario-labs/skills:scenario-elevenlabs

Use when generating or transforming audio with ElevenLabs models on Scenario via MCP: text-to-speech with inline emotion tags, music from a prompt or sectioned songs, sound effects and loops, dubbing audio or video into another language, re-voicing a recording with a preset or cloned voice, or isolating speech from noise. Keywords: ElevenLabs, Elev

Søkeord: audio, lyd, lydeffekter, model, modell, modeller, models, music, musikk, scenario-elevenlabs, sfx, sound, soundtrack

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-elevenlabs/SKILL.md)

### scenario-labs/skills:scenario-fan-cam

Use when putting a person from a photo into live-broadcast crowd footage with Scenario: a stadium or arena fan-cam reaction, a jumbotron or kiss-cam moment, a spectator cutaway at a match or concert, a courtside or front-row sighting, or a personalized sports-TV still that then animates into video. Keywords: fan cam, crowd reaction, jumbotron, stad

Søkeord: animasjon, animate, animated, animation, animations, animere, scenario-fan-cam

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-fan-cam/SKILL.md)

### scenario-labs/skills:scenario-formats

Use when one approved visual, image or video, must ship at many sizes or placements through Scenario: adapting a master to 1:1, 4:5, 9:16, or 16:9, social formats for feeds and stories, YouTube thumbnails, storefront capsules and app store graphics, marketplace product images, link previews, display banners, a website hero, or choosing between crop

Søkeord: scenario-formats

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-formats/SKILL.md)

### scenario-labs/skills:scenario-game-assets

Use when creating game art through Scenario MCP: sprites, sprite sheets, icons, props, loot, tilesets and autotile terrain transitions, seamless tiles, isometric buildings, top-down maps, pixel art, UI buttons and panels, parallax background layers or depth planes for side-scrollers, and character or concept art; or when assets need transparent bac

Søkeord: alfa, alpha, character, character sheet, characters, figur, figurark, figurer, gjennomsiktig, gjennomsiktighet, landscape, oppskalering, scenario-game-assets, sprite sheet, sprite sheets, spriteark, spritesheet, spritesheets, super resolution, superoppløsning, terrain, terreng, transparency, transparent, upscale, upscaling

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-game-assets/SKILL.md)

### scenario-labs/skills:scenario-gemini-image

Use when generating or editing images with Google's Gemini image models (Nano Banana) on Scenario via MCP: text-to-image, natural-language instruction editing, identity locking or style transfer from reference images, multi-image fusion, pulling stills from a video clip, Google Search grounding, thinking level tuning, 512 to 4K output, or choosing

Søkeord: bildegenerering, image generation, model, modell, modeller, models, scenario-gemini-image, tekst til bilde, text to image

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-gemini-image/SKILL.md)

### scenario-labs/skills:scenario-gemini-omni

Use when generating, extending, or editing video with Gemini Omni models on Scenario via MCP: text-to-video, image-to-video from a first frame, reference-to-video keeping a character, product, or place consistent, appending footage to a clip, restyling footage by prompt (season, wardrobe, art style), native audio with dialogue and ambience, or pick

Søkeord: audio, character, characters, figur, figurer, lyd, lydeffekter, model, modell, modeller, models, scenario-gemini-omni, sfx, sound

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-gemini-omni/SKILL.md)

### scenario-labs/skills:scenario-godot-2d

Use when building a 2D game in Godot 4.7: make a platformer or top-down controller that feels right (coyote time, jump buffer, jump height), TileMapLayer and TileSet in code, terrains and autotiles that pick wrong tiles, a dual grid, a camera that jitters or stutters, pixel art that looks blurry or uneven, stretch and integer scaling, 2D lights and

Søkeord: camera, cameras, create, generate, generation, generer, generering, hakking, hitching, kamera, kameraføring, landscape, scenario-godot-2d, shadow, shadows, skygge, skygger, stutter, stuttering, terrain, terreng

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/godot/scenario-godot-2d/SKILL.md)

### scenario-labs/skills:scenario-godot-3d-world

Use when building 3D levels and worlds in Godot 4.7: third-person or FPS controller, player stuck on stairs, spring arm camera clipping, blockout with CSG, GridMap and MeshLibrary, terrain (heightmap, HeightMapShape3D, Terrain3D regions, textures, painting), scattering trees with MultiMesh, streaming a big world, procedural meshes with SurfaceTool,

Søkeord: camera, cameras, collision, collisions, create, generate, generation, generer, generering, kamera, kameraføring, kollisjon, landscape, model, modell, modeller, models, scenario-godot-3d-world, tekstur, teksturer, terrain, terreng, texture, textures

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/godot/scenario-godot-3d-world/SKILL.md)

### scenario-labs/skills:scenario-godot-animation

Use when animating characters or scenes in Godot 4.7: AnimationPlayer clips and RESET, AnimationTree state machines and blend spaces built in code, Mixamo or glTF import, loop settings, BoneMap retargeting and shared animation libraries, root motion, foot sliding, foot IK with TwoBoneIK3D or custom SkeletonModifier3D, tweens, SpringArm3D cameras, c

Søkeord: animasjon, animate, animated, animation, animations, animere, bevegelsesoverføring, camera, cameras, character, characters, figur, figurer, kamera, kameraføring, retarget, retargeting, scenario-godot-animation, scene, scener, scenes

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/godot/scenario-godot-animation/SKILL.md)

### scenario-labs/skills:scenario-godot-architecture

Use when structuring Godot 4.7 game code: folders, scenes and nodes, signals or an event bus autoload, custom Resources for item data, components (health, hitbox, hurtbox), an inventory, save and load, InputMap and key rebinding for keyboard, mouse and gamepad, GDScript static typing and style, or GDScript vs C#; or when code is spaghetti, a folder

Søkeord: lagre, lagring, persistence, save, saving, scenario-godot-architecture, scene, scener, scenes

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/godot/scenario-godot-architecture/SKILL.md)

### scenario-labs/skills:scenario-godot-audio

Use when adding or fixing sound in Godot 4.7: audio buses and effects, volume sliders, 'too many sounds', combat audio with hundreds of enemies, sounds clipping or distorting, 3D sound too quiet or not panning, reverb zones not working, occlusion, adaptive or interactive music (AudioStreamInteractive, layers, stingers), music loops with gaps, SFX t

Søkeord: audio, create, generate, generation, generer, generering, lyd, lydeffekter, music, musikk, scenario-godot-audio, sfx, sound, soundtrack

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/godot/scenario-godot-audio/SKILL.md)

### scenario-labs/skills:scenario-godot-expert

Use when an agent drives Godot 4.7 on macOS or Windows for any task: headless --script jobs, --import, --check-only, command-line exports, GUT tests, windowed screenshots, the headless editor (-e) or an MCP server into a running editor; when a run hangs or fails silently, a capture is black, Godot 3 code breaks in 4.x, 'Identifier not found', expor

Søkeord: flerspiller, multiplayer, nettspill, scenario-godot-expert, shader, shaders, skyggelegger, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/godot/scenario-godot-expert/SKILL.md)

### scenario-labs/skills:scenario-godot-gameplay

Use when building gameplay systems in Godot 4.7: enemy AI that patrols, chases and attacks, state machines, behavior trees (LimboAI), NavigationAgent3D pathfinding and avoidance for 100 to 1000 enemies, 'agents stack up' or 'path is empty', hitbox and hurtbox combat, fast bullets going through walls, save and load, inventory, quests, dialogue (Dial

Søkeord: lagre, lagring, persistence, save, saving, scenario-godot-gameplay

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/godot/scenario-godot-gameplay/SKILL.md)

### scenario-labs/skills:scenario-godot-multiplayer

Use when a Godot 4 game goes online or co-op: host and join with ENet, WebSocket for a web build, RPCs (@rpc, rpc_id, any_peer), MultiplayerSpawner and MultiplayerSynchronizer, player authority, lobbies and login, a dedicated or headless server export, lag, rubber-banding, prediction or netfox, cheating, bandwidth, Steam, Nakama or WebRTC. Symptoms

Søkeord: browser, flerspiller, multiplayer, nettleser, nettspill, scenario-godot-multiplayer, web

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/godot/scenario-godot-multiplayer/SKILL.md)

### scenario-labs/skills:scenario-godot-performance-export

Use when a Godot game stutters, drops frames, hitches when entering new areas, overheats a phone, or must ship: profiling and Performance monitors, CPU or GPU bound, draw calls, MultiMesh, occlusion culling, LOD, shader compilation hitches, export to macOS, Windows, Linux, Steam, Android (APK, AAB, keystore), iOS (Xcode), web (itch.io, COOP/COEP he

Søkeord: browser, forhåndskompilering, hakking, hitching, nettleser, scenario-godot-performance-export, shader, shader cache, shader compilation, shadercache, shaders, skyggelegger, stutter, stuttering, web

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/godot/scenario-godot-performance-export/SKILL.md)

### scenario-labs/skills:scenario-godot-pipeline-automation

Use when Godot 4.7 work must run without a mouse or at scale: batch import of hundreds of GLB props or an AI image-to-3D art drop, naming rules, import presets and post-import scripts, editor plugins, EditorScript and @tool, EditorImportPlugin, GUT or gdUnit4 tests in CI, a GitHub Actions export workflow, GDExtension basics, or a Godot MCP server;

Søkeord: 3d fra bilde, bilde til 3d, image to 3d, image to mesh, scenario-godot-pipeline-automation, tekstur, teksturer, test, testing, texture, textures, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/godot/scenario-godot-pipeline-automation/SKILL.md)

### scenario-labs/skills:scenario-godot-rendering-lighting

Use when lighting or rendering a Godot 4.7 3D scene: pick a renderer (Forward+, Mobile, Compatibility), choose GI (SDFGI, VoxelGI, LightmapGI, reflection probes), bake lightmaps without a mouse, tune WorldEnvironment, tonemapper (AgX, ACES, Filmic), glow, fog, volumetric fog and god rays, shadows and shadow acne, quality presets for PC and phones,

Søkeord: bloom, gloed, glow, glowing, glød, reflection, reflections, refleksjon, refleksjoner, scenario-godot-rendering-lighting, scene, scener, scenes, shadow, shadows, skygge, skygger

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/godot/scenario-godot-rendering-lighting/SKILL.md)

### scenario-labs/skills:scenario-godot-shaders

Use when writing or fixing Godot 4.7 shaders: .gdshader code (spatial, canvas_item, particles, sky, fog), VisualShader graphs built in code, stylized or toon water, dissolve or burn effects, hit flash, outlines, X-ray or portals with the stencil buffer, depth or screen-texture post-processing, global or per-instance uniforms, compute shaders and Te

Søkeord: bølger, etterbehandling, hakking, hav, hitching, ocean, post processing, postprocessing, scenario-godot-shaders, screen effects, screenfx, sea, shader, shaders, skjermeffekter, skyggelegger, stutter, stuttering, tekstur, teksturer, texture, textures, vann, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/godot/scenario-godot-shaders/SKILL.md)

### scenario-labs/skills:scenario-godot-ui

Use when building or fixing game UI in Godot 4.7: main menu, settings screen, HUD (health bar, ammo, minimap frame), Control layout, containers, anchors, themes in code, 'UI scales wrong on phones', 'text too small on 4K', notch or safe area, stretch mode and aspect, gamepad or keyboard menu navigation, focus lost, input rebinding screen, localizat

Søkeord: scenario-godot-ui

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/godot/scenario-godot-ui/SKILL.md)

### scenario-labs/skills:scenario-godot-vfx

Use when making or fixing particle effects and game feel in Godot 4.7: GPUParticles3D or GPUParticles2D explosion, fireball projectile with trail, impact, sparks, smoke, shockwave, ribbon trails, sub-emitters, particle collision, color curve does nothing, particles pop out or vanish, effect too heavy on mobile, CPUParticles fallback for Compatibili

Søkeord: browser, collision, collisions, kollisjon, nettleser, scenario-godot-vfx, web

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/godot/scenario-godot-vfx/SKILL.md)

### scenario-labs/skills:scenario-gpt-image

Use when generating or editing images with OpenAI's GPT Image models on Scenario via MCP: text-to-image, edits from reference images, inpainting with an alpha mask, in-image text for logos and infographics, transparent cutouts, pixel sizing up to 4K, quality tiers up to xhigh and max, input fidelity for product or face detail, or choosing between F

Søkeord: alfa, alpha, bildegenerering, gjennomsiktig, gjennomsiktighet, image generation, model, modell, modeller, models, scenario-gpt-image, tekst til bilde, text to image, transparency, transparent

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-gpt-image/SKILL.md)

### scenario-labs/skills:scenario-grok-imagine-image

Use when generating or editing images with Grok Imagine models on Scenario via MCP: text-to-image, instruction editing with up to three reference images, posters, packaging, ads, or infographics with exact in-image text, photoreal shots from camera and lighting cues, extended aspect ratios up to 20:9 and 9:20, quality and resolution tiers, or batch

Søkeord: bildegenerering, camera, cameras, image generation, kamera, kameraføring, model, modell, modeller, models, scenario-grok-imagine-image, tekst til bilde, text to image

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-grok-imagine-image/SKILL.md)

### scenario-labs/skills:scenario-grok-imagine-video

Use when generating or editing video with Grok Imagine models on Scenario via MCP: text-to-video, image-to-video from a first frame, reference-to-video with @image tags for consistent people, products, or clothing, prompt-based editing, extending a clip from its last frame, native audio with lip-synced dialogue and sound effects, or choosing betwee

Søkeord: audio, lyd, lydeffekter, model, modell, modeller, models, scenario-grok-imagine-video, sfx, sound

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-grok-imagine-video/SKILL.md)

### scenario-labs/skills:scenario-identity-library

Use when a named character or prop must become a reusable identity in Scenario: creating a character or prop from a brief or interview, building its approved image collection (character: <name> or props: <name>), assembling a character sheet or turnaround, or generating new images of an established one. Triggers include create a new character, desi

Søkeord: character, character sheet, characters, create, figur, figurark, figurer, generate, generation, generer, generering, scenario-identity-library, sprite sheet, sprite sheets, spriteark, spritesheet, spritesheets

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-identity-library/SKILL.md)

### scenario-labs/skills:scenario-ideogram

Use when generating or editing images with Ideogram models on Scenario via MCP: posters, logos, menus, packaging, or signage with exact in-image text, editing an image in place while keeping its exact size, transparent PNG generation, background removal that keeps hair and glass edges, editable text layers for localization, or one consistent charac

Søkeord: alfa, alpha, character, characters, create, figur, figurer, generate, generation, generer, generering, gjennomsiktig, gjennomsiktighet, model, modell, modeller, models, scenario-ideogram, transparency, transparent

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-ideogram/SKILL.md)

### scenario-labs/skills:scenario-image

Use when generating or editing images with Scenario through MCP: text-to-image, image-to-image, instruction editing, inpainting or outpainting with a mask, background control, aspect ratio or resolution sizing, several outputs per run, or choosing between Scenario image models. Also when a run fails on prompt length, a plan-restricted model, or a r

Søkeord: bildegenerering, image generation, model, modell, modeller, models, scenario-image, tekst til bilde, text to image

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-image/SKILL.md)

### scenario-labs/skills:scenario-image-editing

Use when editing an existing image on Scenario through MCP with a tool model, not a new generation: upscale or enhance to 2x, 4K, 8K, super resolution, 3D LUT color grade, color correction, posterize, solarize, vignette, film grain, blur, sharpen, glow, chromatic aberration, oilify, cubism, crystallize, dodge and burn, tint, desaturate, expand or u

Søkeord: bloom, bølger, create, generate, generation, generer, generering, gloed, glow, glowing, glød, hav, model, modell, modeller, models, ocean, oppskalering, scenario-image-editing, sea, super resolution, superoppløsning, upscale, upscaling, vann, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-image-editing/SKILL.md)

### scenario-labs/skills:scenario-inspiration

Use when a creative task has no direction yet: finding inspiration, exploring looks or styles, proposing concept directions to pick between, building a moodboard or reference board, doing visual research, mining existing assets for a style, or escaping generic AI-looking output. Also when a saved Scenario collection should drive a new batch as art

Søkeord: lagre, lagring, persistence, save, saving, scenario-inspiration

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-inspiration/SKILL.md)

### scenario-labs/skills:scenario-kinetic-music-video

Use when turning a song into a kinetic-typography or motion-design music video, lyric video, visualizer or K-pop style MV with Scenario, landscape or vertical 9:16 for TikTok, Reels and Shorts: a generated subject sheet, style frames and footage, plus a deterministic JavaScript/three.js engine for lyric type, mattes and tracked graphics timed to su

Søkeord: create, generate, generation, generer, generering, landscape, music, musikk, scenario-kinetic-music-video, soundtrack, terrain, terreng, three js, three.js, threejs

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-kinetic-music-video/SKILL.md)

### scenario-labs/skills:scenario-kling

Use when generating or editing video with Kling models on Scenario via MCP: text-to-video, image-to-video with first and last frames, multi-shot sequences with per-shot prompts, consistent characters via elements and reference images, prompt-based video editing, motion transfer from a driving video (motion control, mocap), lipsync to audio or text,

Søkeord: audio, character, characters, figur, figurer, lyd, lydeffekter, model, modell, modeller, models, scenario-kling, sfx, sound

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-kling/SKILL.md)

### scenario-labs/skills:scenario-luma-image

Use when generating or editing images with Luma Uni-1 models on Scenario via MCP: text-to-image, prompt-based editing of an existing image, style or character reference images with named roles, web search grounding for real-world subjects, rendering exact title text into posters, aspect ratio control, or choosing between Uni-1 Max and Uni-1. Keywor

Søkeord: bildegenerering, browser, character, characters, figur, figurer, image generation, model, modell, modeller, models, nettleser, scenario-luma-image, tekst til bilde, text to image, web

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-luma-image/SKILL.md)

### scenario-labs/skills:scenario-luma-video

Use when generating or editing video with Luma Ray models on Scenario via MCP: cinematic text-to-video, image-to-video from a start frame, start plus end frame anchors, seamless looping clips, HDR output, restyling footage while preserving motion with edit strengths and face, pose, depth, or trajectory controls, reframing to another aspect ratio by

Søkeord: model, modell, modeller, models, scenario-luma-video

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-luma-video/SKILL.md)

### scenario-labs/skills:scenario-mai-image

Use when generating or editing images with Microsoft MAI Image models on Scenario via MCP: photoreal or stylized text-to-image with legible in-image typography, posters, packaging, magazine covers, ads, key art, or instruction-based editing such as text swaps, recoloring, object removal or replacement, background swaps, lighting changes, and full r

Søkeord: bildegenerering, image generation, model, modell, modeller, models, scenario-mai-image, tekst til bilde, text to image

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-mai-image/SKILL.md)

### scenario-labs/skills:scenario-maya-animation

Use when animating a character or prop in Maya through Python: a walk or run cycle, a jump or landing, a heavy lift, throw or punch, an acting or dialogue shot, lip sync, eye darts and blinks, stepped blocking, splining, polish, Graph Editor tangents, animation layers, mocap cleanup or retargeting, game clips and root motion, or reviewing a playbla

Søkeord: animasjon, animate, animated, animation, animations, animere, bevegelsesoverføring, character, characters, figur, figurer, retarget, retargeting, scenario-maya-animation

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/maya/scenario-maya-animation/SKILL.md)

### scenario-labs/skills:scenario-maya-deformation

Use when skinning a character in Maya ("bind skin", "fix the weights", weight painting, Skin Tools or ngSkinTools layers), when deformation looks wrong (pinching, candy-wrapper wrist, collapsing elbow or shoulder, volume loss, clothes poking through), when mirroring, copying or capping skin weights for Unreal or Unity, building blend shapes, correc

Søkeord: character, characters, figur, figurer, scenario-maya-deformation, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/maya/scenario-maya-deformation/SKILL.md)

### scenario-labs/skills:scenario-maya-expert

Use when doing any Autodesk Maya task through Python or a bridge, headless or live: maya.cmds or OpenMaya 2.0 scripts, mayapy or maya.standalone batch jobs, a commandPort or MCP connection into a running Maya, "Maya 2027", validating or exporting scenes, or a maya.cmds script that fails after the 2025 to 2027 changes (PySide6, OpenPBR, renamed math

Søkeord: model, modell, modeller, models, scenario-maya-expert, scene, scener, scenes

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/maya/scenario-maya-expert/SKILL.md)

### scenario-labs/skills:scenario-maya-fx

Use when a Maya task involves simulation or procedural effects: nCloth or Nucleus (a cape, skirt, flag or garment on an animated character, cloth through the body, jittery or stretchy cloth), nParticles, Bifrost graphs (Aero smoke, dust puff, mist, fire, liquids, MPM cloth, snow, sand, "Bifrost smoke"), MASH scattering or motion graphics, sim cache

Søkeord: animasjon, animate, animated, animation, animations, animere, character, characters, figur, figurer, scenario-maya-fx

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/maya/scenario-maya-fx/SKILL.md)

### scenario-labs/skills:scenario-maya-groom

Use when grooming hair or fur in Maya with XGen (Interactive Groom splines or legacy descriptions): scalp hair, eyebrows, eyelashes, fur, guides, clumps, noise, parting, density maps, a fill layer, aiStandardHair shading, noisy or flickering hair renders, hair that must move (Linear Wire, nHair, Alembic caches), or a groom for Unreal (groom Alembic

Søkeord: scenario-maya-groom

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/maya/scenario-maya-groom/SKILL.md)

### scenario-labs/skills:scenario-maya-lighting-rendering

Use when lighting or rendering in Maya with Arnold: a product hero shot, a character close-up or a sequence (master and shot lighting), key, fill and rim placement, "the Arnold render is noisy" or fireflies, render settings and time budgets, AOVs, light groups and EXRs for Nuke, OIDN or noice denoising, ACES or OCIO color, renders that look flat or

Søkeord: character, characters, figur, figurer, scenario-maya-lighting-rendering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/maya/scenario-maya-lighting-rendering/SKILL.md)

### scenario-labs/skills:scenario-maya-lookdev

Use when shading an asset in Maya with Arnold: OpenPBR or aiStandardSurface materials, hooking up Substance Painter or UDIM texture sets, color spaces (sRGB, Raw, ACEScg), a normal map that looks wrong, displacement with black holes or faceting, skin SSS, chrome and metals, glass or crystal, car paint, aiStandardHair, porting Standard Surface to Op

Søkeord: scenario-maya-lookdev, tekstur, teksturer, texture, textures

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/maya/scenario-maya-lookdev/SKILL.md)

### scenario-labs/skills:scenario-maya-modeling

Use when modeling in Autodesk Maya, such as hard-surface props, weapons, vehicles, a sci-fi crate, a game-ready or SubD film model, or a character or creature base mesh, or when asked to "clean up this model" or a scene before rigging or UVs. Also for support loops vs bevels vs creases, Smart Bevel, weighted normals, hard edges, pinching or wobbly

Søkeord: character, characters, figur, figurer, model, modell, modeller, models, scenario-maya-modeling, scene, scener, scenes

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/maya/scenario-maya-modeling/SKILL.md)

### scenario-labs/skills:scenario-maya-pipeline-scripting

Use when writing or fixing Maya pipeline code in Python: mayapy batch jobs over many scenes, validating and auto-fixing scenes, FBX export for Unreal or Unity (static, skeletal, animation clips, Game Exporter), Alembic or GPU caches, USD export, stages and layers, references and namespaces, PySide6 tool windows, OpenMaya 2.0 plug-ins, or slow playb

Søkeord: animasjon, animate, animated, animation, animations, animere, scenario-maya-pipeline-scripting, scene, scener, scenes

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/maya/scenario-maya-pipeline-scripting/SKILL.md)

### scenario-labs/skills:scenario-maya-retopology-uv

Use when turning a dense sculpt, scan, ZBrush export or AI-generated mesh into animation-ready or game-ready topology in Maya without a mouse ("clean up this AI mesh", "retopo this character", Quad Draw, Retopologize), testing it deforms before rigging (bad elbow or wrist bend, lids popping through the eyes), or unwrapping UVs, cutting seams, setti

Søkeord: animasjon, animate, animated, animation, animations, animere, character, characters, create, figur, figurer, generate, generation, generer, generering, scenario-maya-retopology-uv, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/maya/scenario-maya-retopology-uv/SKILL.md)

### scenario-labs/skills:scenario-maya-rigging

Use when rigging a character, creature or prop in Maya: "rig this character", placing or orienting joints, Orient Joint doing nothing, IK/FK switch and matching, pole vector flips or elbow drift, space switching, foot roll, spline IK spine, offsetParentMatrix, blendMatrix or matrix rigging, controls and lockdown for animators, Quick Rig, HumanIK, A

Søkeord: character, characters, figur, figurer, scenario-maya-rigging

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/maya/scenario-maya-rigging/SKILL.md)

### scenario-labs/skills:scenario-meshy

Use when creating or refining 3D assets with Meshy models on Scenario via MCP: image-to-3D from one photo or 1-4 multi-view angles, text-to-3D, retexturing an existing GLB, remeshing to a target polycount, UV unwrapping, auto-rigging a humanoid character, or applying a library animation clip. Keywords: Meshy 7 and Meshy 6, Ultra mode, Smart Topolog

Søkeord: 3d fra bilde, animasjon, animate, animated, animation, animations, animere, bilde til 3d, character, characters, figur, figurer, image to 3d, image to mesh, model, modell, modeller, models, scenario-meshy, tekstur, teksturer, texture, textures

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-meshy/SKILL.md)

### scenario-labs/skills:scenario-minimax-music

Use when generating music with MiniMax models on Scenario via MCP: full songs with vocals from a lyric sheet, structure tags like [Verse] and [Chorus], auto-written lyrics from a plain-language brief, instrumental tracks from a style prompt, or covering an uploaded MP3 or WAV in a new genre while keeping the melody. Keywords: MiniMax Music 3.0, Mus

Søkeord: audio, create, generate, generation, generer, generering, lyd, lydeffekter, model, modell, modeller, models, music, musikk, scenario-minimax-music, sfx, sound, soundtrack

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-minimax-music/SKILL.md)

### scenario-labs/skills:scenario-minimax-video

Use when generating or editing video with MiniMax Hailuo models on Scenario via MCP: text-to-video, image-to-video, first and last frame anchors, reference images, videos, or audio, native stereo audio, bracketed camera commands, extending a clip, inserting a new scene into one, or recasting the people in it from photos. Keywords: MiniMax, Hailuo 3

Søkeord: audio, camera, cameras, kamera, kameraføring, lyd, lydeffekter, model, modell, modeller, models, scenario-minimax-video, scene, scener, scenes, sfx, sound

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-minimax-video/SKILL.md)

### scenario-labs/skills:scenario-model-comparison

Use when comparing Scenario models on the same brief through MCP: a bake-off with shared prompts and inputs, cost, generation time and quality measured side by side, choosing a default model, testing a new release against the incumbent, or finding which model handles a style, edit, or reference image best. Keywords: model comparison, benchmark, bak

Søkeord: create, generate, generation, generer, generering, model, modell, modeller, models, scenario-model-comparison, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-model-comparison/SKILL.md)

### scenario-labs/skills:scenario-model-training

Use when generated assets must keep a consistent style, character, or product look and references stop scaling, or when a user asks to train a custom model through the Scenario MCP, fine-tune a LoRA, clone a voice, curate a training dataset, choose a base model, set epochs and sample prompts, estimate training cost, diagnose a trained model that lo

Søkeord: character, characters, create, figur, figurer, generate, generation, generer, generering, model, modell, modeller, models, scenario-model-training

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-model-training/SKILL.md)

### scenario-labs/skills:scenario-moderation

Use when a Scenario generation is blocked, refused, or returns a moderation or sensitive-content error, when a video is rejected after rendering or its audio track is flagged, when an output is flagged for likeness to a real person or for IP and copyright detection, when the same prompt passes on one model and fails on another, or when a team's own

Søkeord: audio, character, characters, create, figur, figurer, generate, generation, generer, generering, lyd, lydeffekter, model, modell, modeller, models, scenario-moderation, sfx, sound

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-moderation/SKILL.md)

### scenario-labs/skills:scenario-multi-reference

Use when one image must be composed from several reference pictures through the Scenario MCP server, each lending one thing: the character from one, the place, pose, style, light, palette, material, outfit, or layout from others. Also when a reference leaks into the result (its object, colors, or face showing where it should not) or a reference's r

Søkeord: character, characters, figur, figurer, scenario-multi-reference

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-multi-reference/SKILL.md)

### scenario-labs/skills:scenario-orbit-views

Use when a single image of a character, creature, prop, vehicle, or building must be seen from new camera angles through the Scenario MCP server: turnarounds, a 360 orbit, views from behind, above, below, or straight down, consistent multi-angle renders on the same grounded background or on transparency, or novel views that go through a 3D intermed

Søkeord: alfa, alpha, camera, cameras, character, characters, figur, figurer, gjennomsiktig, gjennomsiktighet, kamera, kameraføring, scenario-orbit-views, transparency, transparent

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-orbit-views/SKILL.md)

### scenario-labs/skills:scenario-patina-retexture

Use when retexturing an existing 3D asset with PATINA PBR materials through the Scenario MCP server: a GLB or Blender scene (an image-to-3D result with flat colors, a prop, a diorama) whose surfaces need basecolor, normal, roughness, metalness, and height maps per material family with geometry untouched, or a matched before-and-after comparison fil

Søkeord: 3d fra bilde, bilde til 3d, camera, cameras, image to 3d, image to mesh, kamera, kameraføring, scenario-patina-retexture, scene, scener, scenes

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-patina-retexture/SKILL.md)

### scenario-labs/skills:scenario-product-shots

Use when producing product photography with Scenario from a real product photo: e-commerce packshots on white, transparent, or brand backgrounds, lifestyle scenes placing the product in an environment, hero shots for a landing page or marketplace listing, angle and colorway sets, relighting or shadow fixes, or any shot where the label, logo, and sh

Søkeord: alfa, alpha, gjennomsiktig, gjennomsiktighet, scenario-product-shots, scene, scener, scenes, shadow, shadows, skygge, skygger, transparency, transparent

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-product-shots/SKILL.md)

### scenario-labs/skills:scenario-quality-gate

Use when a generated Scenario image needs a quality check or a brand-brief compliance verdict before it ships: pass/warn/fail scoring, on-brand review against a configured brief, QA gating a batch, pricing or refreshing a stored verdict, or iterating a generation until it clears the gate. Keywords: quality gate, quality check, QA, verdict, brief co

Søkeord: create, generate, generation, generer, generering, scenario-quality-gate

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-quality-gate/SKILL.md)

### scenario-labs/skills:scenario-refine-loop

Use when a Scenario output must be checked and improved rather than accepted first roll: iterating a generation until it matches the brief, fixing a batch that came back off-brief, retrying failed shots methodically, wiring an automated generate, review, revise loop, or deciding whether to re-prompt, swap references, inpaint, post-process, or chang

Søkeord: create, generate, generation, generer, generering, model, modell, modeller, models, scenario-refine-loop

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-refine-loop/SKILL.md)

### scenario-labs/skills:scenario-report

Use when a Scenario user wants to report a bug or request a change, on the public tracker at github.com/scenario-labs/skills or by email to support@scenario.com: turning a failed generation, MCP tool error, or unclear skill into a reproducible report, collecting trace ids with diagnostics_run, stripping keys, signed asset URLs, and personal data, a

Søkeord: create, generate, generation, generer, generering, scenario-report

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-report/SKILL.md)

### scenario-labs/skills:scenario-reve

Use when generating or editing images with Reve models on Scenario via MCP: text-to-image from a prompt alone, instruction edits (swap poster text, recolor a product, change materials, relight or restyle a scene), merging references with consistent subjects, blending up to 6 images into one composite, or choosing between Reve v2.1 and Reve Remix. K

Søkeord: bildegenerering, image generation, model, modell, modeller, models, scenario-reve, scene, scener, scenes, tekst til bilde, text to image

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-reve/SKILL.md)

### scenario-labs/skills:scenario-rodin

Use when generating 3D assets with Rodin Hyper3D models on Scenario via MCP: image-to-3D from up to five multiview stills, text-to-3D from a prompt, fast prototyping versus full quality tiers, quad or triangle topology, PBR materials, HighPack 4K textures, T-pose or A-pose characters for rigging, or splitting a finished mesh into parts and retextur

Søkeord: 3d fra bilde, bilde til 3d, character, characters, figur, figurer, image to 3d, image to mesh, model, modell, modeller, models, scenario-rodin, tekstur, teksturer, texture, textures

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-rodin/SKILL.md)

### scenario-labs/skills:scenario-runway

Use when generating or editing video with Runway models on Scenario via MCP: text-to-video or image-to-video from a first frame with Gen4.5 (cinematic motion, sequenced actions, camera choreography), or video-to-video editing of real footage with Aleph 2 (remove objects, swap products, restyle or relight shots, keyframe-pinned reference images, mot

Søkeord: audio, camera, cameras, kamera, kameraføring, lyd, lydeffekter, model, modell, modeller, models, scenario-runway, sfx, sound

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-runway/SKILL.md)

### scenario-labs/skills:scenario-seedance

Use when generating or editing video with Seedance models on Scenario via MCP: text-to-video, image-to-video, first and last frame anchors, reference-to-video from identity, product, or world references, prompt-based editing, extending a clip, audio-conditioned motion or voice, shot sound without music, first-frame versus reference conditioning, or

Søkeord: audio, lyd, lydeffekter, model, modell, modeller, models, music, musikk, scenario-seedance, sfx, sound, soundtrack

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-seedance/SKILL.md)

### scenario-labs/skills:scenario-seedance-music-video

Use when turning a song, track, or audio master into a finished music video with Scenario and Seedance: planning shots against beats and sections, transcribing lyrics, generating clips that cut to music, keeping the shots' own sound while the song stays the only score, assembling a delivery over the untouched master soundtrack, or verifying the fin

Søkeord: audio, lyd, lydeffekter, music, musikk, scenario-seedance-music-video, sfx, sound, soundtrack

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-seedance-music-video/SKILL.md)

### scenario-labs/skills:scenario-seedance-storyboard

Use when a Seedance video must hold continuous movement across shots: dance choreography, fights, sports, or any performance where limbs teleport, feet slide, or motion resets at every cut, or when turning a storyboard and character sheet into a multi-shot sequence that plays as one take. Keywords: storyboard to video, choreography, movement contro

Søkeord: character, character sheet, characters, figur, figurark, figurer, scenario-seedance-storyboard, sprite sheet, sprite sheets, spriteark, spritesheet, spritesheets

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-seedance-storyboard/SKILL.md)

### scenario-labs/skills:scenario-seedream

Use when generating or editing images with Seedream models on Scenario via MCP: text-to-image, image-to-image editing with reference images, posters or packaging with exact in-image text (non-Latin scripts too), subject-preserving edits, sets of related images in one run, editing a transparent asset without losing its alpha, or splitting an image i

Søkeord: alfa, alpha, bildegenerering, gjennomsiktig, gjennomsiktighet, image generation, model, modell, modeller, models, scenario-seedream, tekst til bilde, text to image, transparency, transparent

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-seedream/SKILL.md)

### scenario-labs/skills:scenario-side-view-game-kit

Use when making the art for a side-scroller or 2D platformer: side-view pixel-art sprite sheets for a hero and ground enemies (run, walk, idle, attack, hurt cycles, air spin, jump and fall poses) and per-level layers (parallax background and midground, seamless wall texture, platform strip, props). Also use when a magenta key eats part of a sprite,

Søkeord: character sheet, create, figurark, generate, generation, generer, generering, scenario-side-view-game-kit, sprite sheet, sprite sheets, spriteark, spritesheet, spritesheets, tekstur, teksturer, texture, textures

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-side-view-game-kit/SKILL.md)

### scenario-labs/skills:scenario-skyboxes

Use when a task involves generating or iterating on skyboxes, 360 panoramas, equirectangular images, environment maps, HDRI-style backdrops, or VR backdrops through the Scenario MCP. Triggers include text-to-skybox, turning a photo into a 360 environment, restyling a panorama's mood, upscaling a skybox without breaking the seam wrap, or exporting e

Søkeord: oppskalering, scenario-skyboxes, super resolution, superoppløsning, upscale, upscaling

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-skyboxes/SKILL.md)

### scenario-labs/skills:scenario-sonilo

Use when adding sound to a video or generating standalone audio with Sonilo models on Scenario via MCP: text-to-sound-effects, text-to-music, video-to-sound-effects or video-to-music from a clip, scoring silent AI video, foley, ambience, muxed video-to-video variants returning the clip with the new track mixed in, keeping speech while replacing mus

Søkeord: audio, lyd, lydeffekter, model, modell, modeller, models, music, musikk, scenario-sonilo, sfx, sound, soundtrack

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-sonilo/SKILL.md)

### scenario-labs/skills:scenario-sparc3d

Use when turning images or photos into 3D meshes with Sparc3D models on Scenario via MCP: single-image or multi-view image-to-3D, watertight meshes for game assets, AR/VR, or 3D printing, mesh-only versus PBR-textured output, face count targets, resolution tiers, or reconstructing human heads and busts with the Portrait variants. Keywords: Sparc3D

Søkeord: 3d fra bilde, bilde til 3d, bølger, hav, image to 3d, image to mesh, model, modell, modeller, models, ocean, scenario-sparc3d, sea, tekstur, teksturer, texture, textures, vann, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-sparc3d/SKILL.md)

### scenario-labs/skills:scenario-sprite-animation

Use when animating 2D game art with Scenario: walk, idle or attack cycles in 4 or 8 directions, isometric sprite sheets, animated GIFs, frame-by-frame pixel art animation, VFX loops such as fire or smoke, looping a sprite seamlessly, animating an existing character image, a full animation sheet from one prompt, extracting animation frames from a ge

Søkeord: animasjon, animate, animated, animation, animations, animere, character, character sheet, characters, create, figur, figurark, figurer, generate, generation, generer, generer spriteark, generering, scenario-sprite-animation, sprite sheet, sprite sheets, spriteark, spritesheet, spritesheets

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-sprite-animation/SKILL.md)

### scenario-labs/skills:scenario-storyboards

Use when a story must unfold across a sequence of Scenario images: a comic page or strip, manga or webtoon panels, a children's storybook, a film, game, or ad storyboard, animatic pre-viz frames, or any shot list where the same characters and world must persist from panel to panel and dialogue must stay legible. Keywords: storyboard, comic, panel,

Søkeord: character, characters, figur, figurer, scenario-storyboards, scene, scener, scenes

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-storyboards/SKILL.md)

### scenario-labs/skills:scenario-team-admin

Use when administering a Scenario team from an agent through MCP: restricting which models a team or project can run (model access control, allowlist, blocklist), inviting or removing team and project members, changing roles, capping a member's Creative Unit spend, auditing API keys and their roles or scopes, or attributing consumption per user or

Søkeord: model, modell, modeller, models, scenario-team-admin

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-team-admin/SKILL.md)

### scenario-labs/skills:scenario-text-overlay

Use when text must appear letter-perfect on generated media: taglines, CTAs, prices, legal supers, lower thirds, end cards, nameplates, or styled rich cards composited over Scenario images and video. Keywords: text overlay, text card, caption card, CTA, legal super, tagline, end card, lower third, price card, HUD text, transparent PNG.

Søkeord: alfa, alpha, create, generate, generation, generer, generering, gjennomsiktig, gjennomsiktighet, scenario-text-overlay, transparency, transparent

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-text-overlay/SKILL.md)

### scenario-labs/skills:scenario-textures

Use when a task involves game textures or materials through the Scenario MCP: seamless or tileable textures, themed texture packs (brick, wood, stone, floors, hand-painted), PBR materials (albedo, metallic, roughness, normal) on 3D assets, retexturing a mesh, material iteration from reference images, texture upscaling that must preserve tiling, or

Søkeord: oppskalering, scenario-textures, super resolution, superoppløsning, tekstur, teksturer, texture, textures, upscale, upscaling

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-textures/SKILL.md)

### scenario-labs/skills:scenario-thumbnails

Use when creating or revising finished video thumbnails or cover images with Scenario: game trailers, boss reveals, patch updates, devlogs, or community videos needing readable composition, exact headline text and consistent characters. Not for title ideas or critique alone, in-video title cards, or a generic image without a thumbnail deliverable.

Søkeord: character, characters, figur, figurer, scenario-thumbnails

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-thumbnails/SKILL.md)

### scenario-labs/skills:scenario-ugc

Use when producing UGC-style creator video with Scenario: a talking-head ad or testimonial from a portrait and a script, a founder clip, a product demo or unboxing, a reaction or before-after cut, a faceless voiceover over b-roll, or vertical social video for TikTok, Reels, or Shorts that must feel filmed on a phone rather than produced. Keywords:

Søkeord: scenario-ugc, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-ugc/SKILL.md)

### scenario-labs/skills:scenario-unity-2d

Use when building a 2D game in Unity 6.3 URP: pixel-art or HD sprite import and PPU, sprite atlases, Tilemaps, Rule Tiles and reskins, the 2D Renderer and 2D lights with normal maps, 2D animation, a platformer or top-down controller ("make a platformer controller that feels good", coyote time, jump buffer, one-way platforms, spikes), Pixel Perfect

Søkeord: animasjon, animate, animated, animation, animations, animere, camera, cameras, kamera, kameraføring, scenario-unity-2d

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unity/scenario-unity-2d/SKILL.md)

### scenario-labs/skills:scenario-unity-animation

Use when a Unity 6.3 task involves character animation or cameras: Mixamo or mocap humanoid import and retargeting, Animator Controllers, blend trees, layers and avatar masks, root motion, foot sliding, IK and Animation Rigging, Playables, Timeline cutscenes, custom tracks and markers, Cinemachine 3 cameras, camera jitter, flipping blends or camera

Søkeord: animasjon, animate, animated, animation, animations, animere, bevegelsesoverføring, camera, cameras, character, characters, figur, figurer, kamera, kameraføring, retarget, retargeting, scenario-unity-animation

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unity/scenario-unity-animation/SKILL.md)

### scenario-labs/skills:scenario-unity-architecture

Use when structuring Unity 6.3 C# code: ScriptableObject data vs runtime state, events and services, inventory, health, save and load, Input System actions and key rebinding, async with Awaitable, assembly definitions, Enter Play Mode and domain reload, .meta files, Git, Smart Merge and LFS. Also when 'my save works in the Editor but not in the bui

Søkeord: lagre, lagring, persistence, save, saving, scenario-unity-architecture, scene, scener, scenes

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unity/scenario-unity-architecture/SKILL.md)

### scenario-labs/skills:scenario-unity-expert

Use when an agent drives Unity 6.3 (6000.3) on a Mac for any task: batch mode and -executeMethod jobs, a running editor (the user's GUI editor or a headless one), the Unity CLI and com.unity.pipeline, MCP servers, the Test Framework, command-line builds; when a batch run fails silently, 'Scripts have compiler errors', a capture comes back black or

Søkeord: scenario-unity-expert, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unity/scenario-unity-expert/SKILL.md)

### scenario-labs/skills:scenario-unity-gameplay

Use when building or debugging Unity gameplay systems: enemy AI that patrols, chases and attacks, NavMesh baking and agents (AI Navigation 2), feet sliding on agents, state machines or behavior trees, physics projectiles that tunnel, the physics spiral, layers and the collision matrix, CharacterController vs Rigidbody characters, object pooling, 'h

Søkeord: audio, character, characters, collision, collisions, figur, figurer, flerspiller, kollisjon, lyd, lydeffekter, multiplayer, nettspill, scenario-unity-gameplay, sfx, sound

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unity/scenario-unity-gameplay/SKILL.md)

### scenario-labs/skills:scenario-unity-mobile

Use when a Unity 6.3 game targets Android or iOS: phone frame budget, overheating after 20 minutes, 'my game stutters on phones', ASTC or ETC2 textures, audio import, URP mobile settings, touch controls, on-screen joystick, UI under the notch or safe area, slow startup, ANRs, 'Android build fails', AAB, keystore signing, target API 36, Google Play

Søkeord: audio, hakking, hitching, lyd, lydeffekter, scenario-unity-mobile, sfx, sound, stutter, stuttering, tekstur, teksturer, texture, textures

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unity/scenario-unity-mobile/SKILL.md)

### scenario-labs/skills:scenario-unity-performance

Use when a Unity 6.3 game is slow or stutters: low fps, frame spikes, hitches when entering areas or on first effects, GC spikes, too many draw calls or SetPass calls, CPU vs GPU bound questions, Profiler, Profile Analyzer, Memory Profiler, Frame Debugger or Project Auditor work, GPU Resident Drawer or SRP Batcher setup, LOD and Mesh LOD, shader wa

Søkeord: hakking, hitching, scenario-unity-performance, shader, shaders, skyggelegger, stutter, stuttering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unity/scenario-unity-performance/SKILL.md)

### scenario-labs/skills:scenario-unity-pipeline-automation

Use when automating a Unity 6.3 content pipeline or build: importing an art drop (FBX, PNG) with AssetPostprocessor rules and naming conventions, generating prefabs or editing scenes from script with correct Undo and SetDirty, Addressables groups, labels and content builds, content-validation tests, batch-mode, command-line or CI builds (Build Prof

Søkeord: scenario-unity-pipeline-automation, scene, scener, scenes, tekstur, teksturer, test, testing, texture, textures, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unity/scenario-unity-pipeline-automation/SKILL.md)

### scenario-labs/skills:scenario-unity-rendering-lighting

Use when setting up URP (or choosing URP vs HDRP), configuring URP assets and quality tiers for PC and phones, lighting a stylized or realistic Unity scene (sun, sky, baked or mixed lightmaps, Shadowmask, Adaptive Probe Volumes, reflection probes), or fixing blurry shadows, light leaks, gray bakes, washed-out images, tonemapping and grading, bloom

Søkeord: anti alias, anti aliasing, antialiasing, bloom, FXAA, gloed, glow, glowing, glød, kantutjevning, MSAA, reflection, reflections, refleksjon, refleksjoner, scenario-unity-rendering-lighting, scene, scener, scenes, shader, shaders, shadow, shadows, skygge, skyggelegger, skygger, SMAA, TAA

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unity/scenario-unity-rendering-lighting/SKILL.md)

### scenario-labs/skills:scenario-unity-shaders

Use when a Unity 6.3 URP task involves shaders: hand-written HLSL, Shader Graph water, toon, dissolve or outline, Custom Function nodes, a renderer feature or full-screen effect on Render Graph, compute shaders, shader variants, keywords, stripping, Shader Build Settings, PSO warm-up, or shader cost; or when a material turns pink or invisible, cast

Søkeord: bølger, hakking, hav, hitching, ocean, scenario-unity-shaders, sea, shader, shaders, shadow, shadows, skygge, skyggelegger, skygger, stutter, stuttering, vann, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unity/scenario-unity-shaders/SKILL.md)

### scenario-labs/skills:scenario-unity-ui

Use when building or fixing game UI in Unity 6.3: main menu, settings screen (resolution, quality, volume, key rebinding), HUD, health bar, minimap frame; choosing uGUI or UI Toolkit or mixing both; 'UI scales wrong on phones', portrait to 4K, Canvas Scaler, anchors, layout groups collapsing, sort order, UXML/USS, data binding, TextMeshPro or UI To

Søkeord: scenario-unity-ui, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unity/scenario-unity-ui/SKILL.md)

### scenario-labs/skills:scenario-unity-vfx

Use when making or fixing real-time VFX in Unity 6.3: explosions, fireballs, projectiles with muzzle, trail and impact, spells, slashes, shockwaves, smoke, sparks, Particle System (Shuriken) or VFX Graph ('VFX Graph explosion', 'particles look bad', 'effect kills fps on mobile', 'too much overdraw'), mesh effects with scrolling textures, an uber VF

Søkeord: scenario-unity-vfx, shader, shaders, skyggelegger, tekstur, teksturer, texture, textures

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unity/scenario-unity-vfx/SKILL.md)

### scenario-labs/skills:scenario-unity-web

Use when a Unity 6.3 game must run in a browser: 'export to WebGL', Web build settings or Build Profiles, gzip or Brotli, Decompression Fallback, server headers, 'Unable to parse .framework.js.br', build too big or slow to load, itch.io, CrazyGames or Poki limits, Addressables or AssetBundles on the Web, 'Could not produce class with ID', Task.Run

Søkeord: browser, nettleser, scenario-unity-web, web

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unity/scenario-unity-web/SKILL.md)

### scenario-labs/skills:scenario-unity-world-building

Use when building a Unity 6.3 level or open world: terrain from code or heightmaps, procedural islands, erosion, splat and foliage rules, trees and grass, ProBuilder graybox, level gym, modular kit and prefab placement, set dressing, landmarks and player guidance, the island's edge, spline roads, WFC, fog, additive scene streaming, or a world that

Søkeord: 3dgs, gaussian splatting, gaussiske splats, grass, gress, landscape, scenario-unity-world-building, scene, scener, scenes, splat, splats, terrain, terreng, vegetasjon, vegetation

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unity/scenario-unity-world-building/SKILL.md)

### scenario-labs/skills:scenario-unreal-animation

Use when a UE5 task involves characters in motion: "import FBX from Maya" with a skeleton, "retarget animations", IK Rig, IK Retargeter, feet sinking or floating after retarget, mocap cleanup, Motion Matching, Pose Search, Choosers, GASP, state machine vs motion matching, root motion, offset root bone, foot IK, Control Rig, Animation Blueprint cost

Søkeord: animasjon, animate, animated, animation, animations, animere, bevegelsesoverføring, character, characters, figur, figurer, retarget, retargeting, scenario-unreal-animation

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unreal/scenario-unreal-animation/SKILL.md)

### scenario-labs/skills:scenario-unreal-cinematics

Use when making a trailer, cutscene, cinematic or short film in Unreal Engine 5.8 with Sequencer: shot lists, master and shot sequences, cameras, lenses, depth of field, camera cuts, spawnables, character animation in shots, per-shot lighting, Movie Render Graph or Movie Render Queue EXR renders, "render darker than the viewport", "first frames pop

Søkeord: animasjon, animate, animated, animation, animations, animere, camera, cameras, character, characters, figur, figurer, kamera, kameraføring, scenario-unreal-cinematics

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unreal/scenario-unreal-cinematics/SKILL.md)

### scenario-labs/skills:scenario-unreal-expert

Use when an agent drives Unreal Engine 5.8 on a Mac for any task: Editor Python (the unreal module), headless UnrealEditor-Cmd -run=pythonscript jobs, Epic's Unreal MCP server, the Remote Control API, console commands and cvars; when a script breaks on 5.8 (EditorLevelLibrary, Remote Control calls refused, Substrate materials black, MRQ presets); w

Søkeord: scenario-unreal-expert

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unreal/scenario-unreal-expert/SKILL.md)

### scenario-labs/skills:scenario-unreal-gameplay

Use when building or debugging UE5 gameplay: a character with double jump or dash, abilities with cooldowns, enemy AI that patrols, chases and attacks, a health bar or HUD; choosing Blueprint vs C++, GAS or not, StateTree vs Behavior Tree, EQS or Mass; setting up Enhanced Input, Common UI or UMG; replication, RepNotify, save games, World Partition

Søkeord: character, characters, figur, figurer, lagre, lagring, persistence, save, saving, scenario-unreal-gameplay, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unreal/scenario-unreal-gameplay/SKILL.md)

### scenario-labs/skills:scenario-unreal-lighting-rendering

Use when lighting or rendering in Unreal Engine 5.8: physical light units and exposure (EV100, lux, lumens), Lumen GI and reflections, MegaLights, virtual shadow maps, sky, fog and clouds, post process and color grading, the path tracer, or Movie Render Graph stills. Triggers: "Lumen is noisy", "MegaLights noise", "the interior is too dark", "light

Søkeord: reflection, reflections, refleksjon, refleksjoner, scenario-unreal-lighting-rendering, scene, scener, scenes, shadow, shadows, skygge, skygger

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unreal/scenario-unreal-lighting-rendering/SKILL.md)

### scenario-labs/skills:scenario-unreal-materials

Use when a UE5 task involves materials or textures: a master material and instances for a kit, Substrate or legacy, Blendable vs Adaptive GBuffer, glass, emissive screens, decals, edge wear and dirt, landscape layers and RVT, toon or cel shading, "too many shaders" or shader permutations, static switches, usage flags, texture compression (BC7, norm

Søkeord: compress, compression, komprimering, landscape, scenario-unreal-materials, shader, shaders, skyggelegger, tekstur, teksturer, terrain, terreng, texture, textures

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unreal/scenario-unreal-materials/SKILL.md)

### scenario-labs/skills:scenario-unreal-performance

Use when an Unreal Engine 5.8 project misses its frame rate or stutters: "optimize to 60 fps", "we run at 38 fps", CPU or GPU bound, game or render thread too long, hitches, traversal or shader stutter (PSO), GC spikes, camera-cut spikes, Lumen, Nanite, VSM, ray tracing, foliage, crowds or Niagara too expensive, async compute, stat unit, ProfileGPU

Søkeord: camera, cameras, hakking, hitching, kamera, kameraføring, scenario-unreal-performance, shader, shaders, skyggelegger, stutter, stuttering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unreal/scenario-unreal-performance/SKILL.md)

### scenario-labs/skills:scenario-unreal-pipeline-automation

Use when importing FBX, USD, OBJ or glTF from Maya, ZBrush or Blender into Unreal Engine 5.8 in bulk or reimporting changed files, writing Editor Python tools, Interchange pipelines or import presets, enforcing naming conventions, assigning material instances by script, setting Nanite, collision and LODs per asset class, writing data validators or

Søkeord: collision, collisions, kollisjon, scenario-unreal-pipeline-automation, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unreal/scenario-unreal-pipeline-automation/SKILL.md)

### scenario-labs/skills:scenario-unreal-vfx

Use when a UE5 task involves Niagara or Chaos destruction: a Niagara fireball, projectile trail, impact explosion, muzzle flash, spell, smoke, sparks, debris, Niagara fluids or flipbooks; "Niagara is too expensive", stat NiagaraOverview, Effect Types, pooling, Data Channels, lightweight emitters, VFX scalability; judging an effect's readability, va

Søkeord: scenario-unreal-vfx

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unreal/scenario-unreal-vfx/SKILL.md)

### scenario-labs/skills:scenario-unreal-world-building

Use when building or fixing an Unreal Engine 5 level or open world: World Partition, OFPA, Data Layers, Level Instances, Packed Level Actors, HLOD, landscape size, heightmap import or clipping, edit layers, terrain material rules, foliage and grass, a PCG forest or rock scatter, runtime GPU grass, Nanite and tessellation choices, modular kits, a ri

Søkeord: grass, gress, landscape, scenario-unreal-world-building, terrain, terreng, vegetasjon, vegetation

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/game-engines/unreal/scenario-unreal-world-building/SKILL.md)

### scenario-labs/skills:scenario-veo

Use when generating or extending video with Google Veo models on Scenario via MCP: text-to-video, image-to-video from a first frame, first and last frame transitions, reference-to-video (R2V) with asset or style reference images, native audio with dialogue, sound effects, and ambience, negative prompts, seeded reruns, extending a 16:9 clip, or choo

Søkeord: audio, lyd, lydeffekter, model, modell, modeller, models, scenario-veo, sfx, sound

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-veo/SKILL.md)

### scenario-labs/skills:scenario-video

Use when generating or editing video on Scenario via MCP: text-to-video, a music video from a song, image-to-video (still animation, frame anchors), motion prompting, lipsync and talking avatars, dubbing a clip, video upscale to 4K, prompt-based editing, trim, split, concat, extend, reframe, resize, background removal, frame or audio extraction, lo

Søkeord: animasjon, animate, animated, animation, animations, animere, audio, lyd, lydeffekter, music, musikk, oppskalering, scenario-video, sfx, sound, soundtrack, super resolution, superoppløsning, upscale, upscaling

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-video/SKILL.md)

### scenario-labs/skills:scenario-video-ads

Use when producing a video ad with Scenario from a product shot or brand assets: a mobile 9:16 or landscape 16:9 commercial, a TikTok, Reels, Shorts, YouTube, or CTV spot, or campaign creative needing a creative brief, storyboard, cinematic camera work, brand-faithful product footage, music and voiceover, captions, ad variants, budget planning, or

Søkeord: camera, cameras, kamera, kameraføring, landscape, music, musikk, scenario-video-ads, soundtrack, terrain, terreng

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-video-ads/SKILL.md)

### scenario-labs/skills:scenario-video-assembly

Use when generated clips must become a finished video on Scenario via MCP: cutting a shot list together, laying a timeline, concatenating with transitions, overlaying a logo or title card, adding a music bed or voiceover, burning in or exporting captions and subtitles, trimming and splitting, or producing vertical and square variants of one master.

Søkeord: create, generate, generation, generer, generering, music, musikk, scenario-video-assembly, soundtrack

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-video-assembly/SKILL.md)

### scenario-labs/skills:scenario-video-editing

Use when editing footage that already exists on Scenario through MCP with a tool model instead of a new generation: 3D LUT grading, color correction, film grain, vignette, blur, sharpen, glow, tint, desaturate, posterize, solarize, cubism, crystallize, oilify, chromatic aberration or dodge and burn on a clip; trimming to a time range, splitting at

Søkeord: bloom, create, generate, generation, generer, generering, gloed, glow, glowing, glød, model, modell, modeller, models, scenario-video-editing

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-video-editing/SKILL.md)

### scenario-labs/skills:scenario-vidu

Use when generating video with Vidu models on Scenario via MCP: text-to-video, image-to-video from a single still, start and end frame interpolation, reference-to-video keeping characters and props consistent from up to 7 reference images or reference videos, anime-style motion, movement amplitude control, or deciding between Q3, Q2, Q1, and 2.0 ti

Søkeord: character, characters, figur, figurer, model, modell, modeller, models, music, musikk, scenario-vidu, soundtrack

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-vidu/SKILL.md)

### scenario-labs/skills:scenario-walkable-room

Use when one interior photo, uploaded or generated on Scenario, should become a room a visitor walks into in a web browser and plays with: props lifted out of the photo and rebuilt as 3D objects to grab, throw, and hear land, inside a Gaussian splat world, or restyled variants of one room. Keywords: image-blaster, walkable room, photo to 3D room, c

Søkeord: 3dgs, audio, browser, collision, collisions, create, gaussian splatting, gaussiske splats, generate, generation, generer, generering, kollisjon, lyd, lydeffekter, nettleser, scenario-walkable-room, sfx, sound, splat, splats, web

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-walkable-room/SKILL.md)

### scenario-labs/skills:scenario-wan

Use when generating or editing video with Wan models on Scenario via MCP: text-to-video, image-to-video from a still, first and last frame brackets, extending a clip, instruction-based video editing, character motion transfer or person replacement (Animate), aspect ratio reframing, video outpainting, uploaded-audio sync or auto-generated audio, or

Søkeord: animasjon, animate, animated, animation, animations, animere, audio, character, characters, create, figur, figurer, generate, generation, generer, generering, lyd, lydeffekter, model, modell, modeller, models, scenario-wan, sfx, sound

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-wan/SKILL.md)

### scenario-labs/skills:scenario-workflow-authoring

Use when a task involves creating or editing a Scenario workflow graph through MCP: building an app from a brief, adding or rewiring nodes (models, prompts, approval gates, loops), authoring editor_info, publishing, unpublishing or renaming, importing an exported workflow JSON, migrating a graph built in Weavy, ComfyUI, or another node tool, copyin

Søkeord: model, modell, modeller, models, scenario-workflow-authoring

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-workflow-authoring/SKILL.md)

### scenario-labs/skills:scenario-workflows

Use when a task involves running a Scenario workflow through MCP, including anything the user calls a Scenario app, a saved pipeline, or a multi-step generation graph. Triggers include listing workflows, building workflow_run's inputs object, pricing a run with a dry run, approving or rejecting a stuck approval node, a run rejected for input length

Søkeord: create, generate, generation, generer, generering, lagre, lagring, persistence, save, saving, scenario-workflows

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/scenario-workflows/SKILL.md)

### scenario-labs/skills:scenario-zbrush-automation

Use when automating ZBrush 2026: batch processing a folder of OBJ or ZTL files, a ZBrush Python script or ZScript, recording a macro to learn a palette path, the ZBrush -script command line, scripting UV Master, Decimation Master or Multi Map Exporter, exporting every SubTool, GoZ or GoB round trips with Maya or Blender, renaming SubTools, or batch

Søkeord: scenario-zbrush-automation

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/zbrush/scenario-zbrush-automation/SKILL.md)

### scenario-labs/skills:scenario-zbrush-character-creature

Use when sculpting a realistic head, face, portrait, body or creature in ZBrush (anatomy, landmarks, proportions, "the face looks off", eyes, lips, jaw), adding skin, pores, wrinkles or reptile and dragon scales with alphas, Surface Noise, layers or morph targets, planning subdivision or HD Geometry for a film close-up, reprojecting detail, sculpti

Søkeord: alfa, alpha, character, characters, figur, figurer, gjennomsiktig, gjennomsiktighet, scenario-zbrush-character-creature, transparency, transparent

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/zbrush/scenario-zbrush-character-creature/SKILL.md)

### scenario-labs/skills:scenario-zbrush-expert

Use when an agent drives Maxon ZBrush 2026 for any task (sculpt in ZBrush, DynaMesh, ZRemesher, UVs, export, polypaint, posing, 3D print, clean up an AI mesh in ZBrush), when writing ZBrush Python (zbrush.commands) or ZScript, when the ZBrush bridge is not answering, a palette path or set() does nothing, a scripted stroke does not sculpt or a dialo

Søkeord: scenario-zbrush-expert

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/zbrush/scenario-zbrush-expert/SKILL.md)

### scenario-labs/skills:scenario-zbrush-hard-surface

Use when modeling hard surface in ZBrush 2026 (sci-fi helmet, weapon, prop, armor plates, mechanical parts, kitbash, vents, panel lines, bolts, concept to game asset), when using ZModeler, Dynamic Subdivision and creasing, Live Boolean, Knife, Clip, Slice or Trim curves, IMM, ArrayMesh, NanoMesh or Panel Loops, or when edges look razor sharp, a Mak

Søkeord: model, modell, modeller, models, scenario-zbrush-hard-surface

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/zbrush/scenario-zbrush-hard-surface/SKILL.md)

### scenario-labs/skills:scenario-zbrush-paint-render

Use when polypainting in ZBrush (skin color zones, fills, cavity or AO passes, Spotlight), baking polypaint to a texture or vertex color, rendering a ZBrush model with BPR or Redshift, making render passes, a turntable or portfolio shots, or when paint looks like uniform beige or clown makeup, is blurry, is hidden under a texture or in Redshift, or

Søkeord: model, modell, modeller, models, scenario-zbrush-paint-render, tekstur, teksturer, texture, textures

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/zbrush/scenario-zbrush-paint-render/SKILL.md)

### scenario-labs/skills:scenario-zbrush-pose-print

Use when posing a sculpt or preparing it for 3D printing in ZBrush: "pose this character", Transpose Master, TPoseMesh, Gizmo posing with masks, ZSphere rig, Proxy Pose, weapon in the hand, stretching after posing, "3D print this", 1/6 scale statue, miniature, resin or FDM, hollowing, wall thickness, drain holes, keys and pins, cutting into parts,

Søkeord: character, characters, figur, figurer, scenario-zbrush-pose-print

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/zbrush/scenario-zbrush-pose-print/SKILL.md)

### scenario-labs/skills:scenario-zbrush-retopology-export

Use when a ZBrush sculpt, scan or AI-generated mesh must become production topology and files (ZRemesher and guides, the 2026 Retopo brush, reprojecting detail with Project All, rebuilding subdivision levels, UV Master or native unwrap, normal and displacement maps with Multi Map Exporter, GoZ, OBJ or FBX export, scale and axes, Decimation Master,

Søkeord: create, generate, generation, generer, generering, scenario-zbrush-retopology-export

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/zbrush/scenario-zbrush-retopology-export/SKILL.md)

### scenario-labs/skills:scenario-zbrush-sculpting

Use when an agent sculpts organic forms in ZBrush 2026 (sculpt a head, bust or creature in ZBrush from a sphere, ZSpheres or primitives); when blocking primary and secondary forms, choosing DynaMesh, Sculptris Pro or subdivision levels, or setting ClayBuildup, Dam_Standard, Move or TrimDynamic; when using masks, polygroups, Morph Targets or layers;

Søkeord: scenario-zbrush-sculpting

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/zbrush/scenario-zbrush-sculpting/SKILL.md)

### scenario-labs/skills:scenario-zbrush-stylized

Use when sculpting a stylized or cartoon character, bust, collectible or toy in ZBrush (Overwatch, Fortnite, Disney look), judging shape language (S and C curves, parallel lines, 70/30, silhouette read at a distance), exaggerating proportions on purpose, keeping stylized planes crisp through subdivision, sculpting stylized hair (chunky clumps, curv

Søkeord: character, characters, figur, figurer, scenario-zbrush-stylized

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/skills/dcc/zbrush/scenario-zbrush-stylized/SKILL.md)

### scenario-labs/skills:Skill Development

This skill should be used when the user wants to "create a skill", "add a skill to plugin", "write a new skill", "improve skill description", "organize skill content", or needs guidance on skill structure, progressive disclosure, or skill development best practices for Claude Code plugins.

Søkeord: create, generate, generation, generer, generering, Skill Development, skill-development

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/.agents/skills/skill-development/SKILL.md)

### scenario-labs/skills:skill-creator

Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.

Søkeord: create, generate, generation, generer, generering, skill-creator, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/.agents/skills/skill-creator/SKILL.md)

### scenario-labs/skills:skills-pr-handle

Use when explicitly asked to handle a pull request in the Scenario skills repository, including review comments and skill validation.

Søkeord: skills-pr-handle

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/.agents/skills/skills-pr-handle/SKILL.md)

### scenario-labs/skills:skills-validate

Use when explicitly asked to run a live or plan-only application test for a published Scenario skill.

Søkeord: skills-validate, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scenario-labs/skills/blob/49dd26e47371163ae0020c7f5627d0993626bfc2/.agents/skills/skills-validate/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-atmosphere-aerial-perspective

Implement physically motivated sky and aerial-perspective systems in Three.js. Use for planetary atmospheres, ground-to-space transitions, Rayleigh/Mie scattering, precomputed LUTs, depth-based transmittance and inscattering, sun/moon discs, and atmosphere-aware lighting.

Søkeord: three js, three.js, threejs, threejs-atmosphere-aerial-perspective

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-atmosphere-aerial-perspective/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-bloom

Implement production bloom in advanced Three.js scenes. Use for HDR signal ordering, bloom-node controls, dual selective bloom with guaranteed material restoration, scene-relative emissive hierarchy, and effect-isolation diagnostics.

Søkeord: bloom, gloed, glow, glowing, glød, scene, scener, scenes, three js, three.js, threejs, threejs-bloom

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-bloom/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-camera-direction

Direct advanced Three.js camera systems. Use for scale-aware chase rigs, thrust lag, side/orbit cameras, body-relative up vectors, quaternion handoffs, authored cinematic framing, floating origins, pointer-look controls, camera collision constraints, projection ownership, and lifecycle restoration.

Søkeord: camera, cameras, collision, collisions, kamera, kameraføring, kollisjon, three js, three.js, threejs, threejs-camera-direction

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-camera-direction/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-exposure-color-grading

Build a measured exposure and grading path in Three.js. Use for a 64x36 encoded luminance meter, asynchronous readback, weighted log-average exposure, asymmetric adaptation, single tone-map ownership, and a generated 32-cube post-tone-map LUT.

Søkeord: create, generate, generation, generer, generering, three js, three.js, threejs, threejs-exposure-color-grading

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-exposure-color-grading/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-image-pipeline

Build a deliberate final-image pipeline for advanced Three.js scenes. Use for depth, normal, albedo, and history ownership; GTAO or bent normals; bloom; eye adaptation; tone mapping; 3D LUT grading; effect-local render targets; and pass diagnostics.

Søkeord: bloom, gloed, glow, glowing, glød, scene, scener, scenes, three js, three.js, threejs, threejs-image-pipeline

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-image-pipeline/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-parallax-occlusion-mapping

Build silhouette-aware parallax occlusion mapping in Three.js WebGPU and TSL. Use for height-field ray marching, relief UVs, clipped flat or curved silhouettes, inflated shells, self-shadowing, relief-aware shadow depth, and height-derived normals.

Søkeord: shadow, shadows, skygge, skygger, three js, three.js, threejs, threejs-parallax-occlusion-mapping

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-parallax-occlusion-mapping/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-precipitation-surfaces

Build coupled precipitation and affected surfaces in Three.js. Use for falling snow, snow accumulation, model snow caps, wet asphalt puddles, procedural ripple normals, splash flipbooks, rain streaks, shared weather envelopes, and surface wetness or coverage transitions.

Søkeord: model, modell, modeller, models, three js, three.js, threejs, threejs-precipitation-surfaces

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-precipitation-surfaces/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-procedural-animation

Build advanced procedural animation in Three.js. Use for launch kinematics, gravity turns, staging, spin docking, target-frame decomposition, spring-follow motion, rotating-frame alignment, peeling debris, analytic transform timelines, frame-rate-independent response, and quaternion control.

Søkeord: animasjon, animate, animated, animation, animations, animere, three js, three.js, threejs, threejs-procedural-animation

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-procedural-animation/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-procedural-architecture

Build authored procedural buildings and architectural kits in Three.js. Use for massing grammars, exposed-edge analysis, façade bays, profiles, arches, cornices, roofs, ornaments, material-slot mesh compilation, deterministic variants, and procedural city assets.

Søkeord: three js, three.js, threejs, threejs-procedural-architecture

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-procedural-architecture/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-procedural-fields

Build coherent procedural scalar and vector fields for Three.js materials and geometry. Use for terrain, planets, wear, biomes, clouds, water masks, displacement, roughness, normals, domain warping, and any visual where several channels must derive from shared causes.

Søkeord: bølger, hav, landscape, ocean, sea, terrain, terreng, three js, three.js, threejs, threejs-procedural-fields, vann, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-procedural-fields/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-procedural-geometry

Build well-crafted production procedural meshes in Three.js. Use for complete hard-surface assemblies and humanoid robots, profile extrusion, parameter-curve and spine lofts, pillow panels, exact polygon cuts, inset, revolve, sweep, solidify, bevels and fillets, shell thickness, direct-topology apertures, semantic mesh writers, or diagnosing primit

Søkeord: three js, three.js, threejs, threejs-procedural-geometry

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-procedural-geometry/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-procedural-materials

Author production procedural materials in Three.js. Use for hybrid texture-backed PBR soil and moss with procedural displacement and masks, upward-facing model moss accumulation, atlas filtering, specular AA, planet-space fields, terrain wetness, deformable granular sand with mass-coupled grain shading, simulated tearable denim with implicit yarn m

Søkeord: landscape, model, modell, modeller, models, reflection, reflections, refleksjon, refleksjoner, shadow, shadows, skygge, skygger, tekstur, teksturer, terrain, terreng, texture, textures, three js, three.js, threejs, threejs-procedural-materials

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-procedural-materials/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-procedural-planets

Author procedural planetary bodies in Three.js. Use for spherical terrain, continents, ridges, craters, biome masks, coastlines, material variation, analytic normals, altitude LOD, and bodies that must hold up from orbit through close approach.

Søkeord: landscape, terrain, terreng, three js, three.js, threejs, threejs-procedural-planets

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-procedural-planets/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-procedural-vegetation

Generate authored procedural trees, grass, ivy, flowers, and vegetation in Three.js or raw WebGPU. Use for surface-following vines, painted ivy paths, stylized or GPU grass, GPU-culled virtual flower fields, trunks, recursive branches, roots, canopies, leaf cards, species presets, deterministic growth, distance-tiered plant geometry, and rooted bla

Søkeord: create, generate, generation, generer, generering, grass, gress, three js, three.js, threejs, threejs-procedural-vegetation, vegetasjon, vegetation

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-procedural-vegetation/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-procedural-vfx

Author production real-time VFX in Three.js. Use for filmic HDR lens-flare compositors, highlight-derived ghosts, field-angle pupil deformation, localized glare and bloom, raymarched aurora curtains, finite-footprint emissive slabs, uniform volume integration, equirectangular radiance probes, WebGPU voxel fire and smoke, coupled volumetric fluid fi

Søkeord: bloom, collision, collisions, create, generate, generation, generer, generering, gloed, glow, glowing, glød, kollisjon, scene, scener, scenes, three js, three.js, threejs, threejs-procedural-vfx

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-procedural-vfx/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-raymarched-space-effects

Build raymarched space phenomena in Three.js. Use for black-hole lensing, accretion disks, wormhole throat transits, curved-ray and null-geodesic integration, lensed celestial spheres, procedural star fields and galactic skies, relativistic-looking distortion, bounded volumetric structures, and GPU effects that need controlled numerical integration

Søkeord: three js, three.js, threejs, threejs-raymarched-space-effects

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-raymarched-space-effects/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-screen-space-ambient-occlusion

Implement a production GTAO path in Three.js. Use for half-resolution horizon sampling, reversed-depth reconstruction, bent-normal encoding, full-resolution bilateral reconstruction, environment-light application, contact grounding, and halo diagnosis.

Søkeord: three js, three.js, threejs, threejs-screen-space-ambient-occlusion

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-screen-space-ambient-occlusion/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-shadow-systems

Implement stable, scalable directional-shadow systems for Three.js. Use for large procedural worlds, city scenes, terrain, moving cameras, WebGPU/TSL shadow nodes, cascades, cached clipmaps, texel stabilization, update budgets, and targeted invalidation.

Søkeord: camera, cameras, kamera, kameraføring, landscape, scene, scener, scenes, shadow, shadows, skygge, skygger, terrain, terreng, three js, three.js, threejs, threejs-shadow-systems

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-shadow-systems/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-skill-router

Route ambitious Three.js graphics work to the smallest expert skill set. Use for new visual experiences, graphics rewrites, reference matching, or requests spanning geometry, materials, atmosphere, shadows, temporal effects, and final image treatment.

Søkeord: shadow, shadows, skygge, skygger, three js, three.js, threejs, threejs-skill-router

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-skill-router/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-spectral-ocean

Build large procedural oceans and coast transitions in Three.js. Use for WebGPU/TSL FFT oceans, multi-cascade wavelength bands, coastal breakers, finite-volume shallow-water beach waves, signed-distance coastlines, shallow-water swash films, wet-sand transitions, rock-impact spray, stylized above/below surface optics, permanently submerged Snell-wi

Søkeord: bølger, hav, ocean, reflection, reflections, refleksjon, refleksjoner, sea, three js, three.js, threejs, threejs-spectral-ocean, vann, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-spectral-ocean/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-temporal-surfaces

Build view-aligned and screen-space surface effects in Three.js. Use for touch-history frost and thaw, ping-pong accumulation, reduced-resolution blur, crystalline masks, two-scale refraction, and procedural rain droplets that refract and blur a background through wet glass.

Søkeord: three js, three.js, threejs, threejs-temporal-surfaces

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-temporal-surfaces/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-visual-validation

Validate advanced Three.js graphics as authored systems rather than subjective screenshots. Use for fixed-view visual contracts, field and pass diagnostics, no-post baselines, seed sweeps, camera-scale tests, temporal stability checks, GPU budgets, and regression evidence for procedural scenes.

Søkeord: camera, cameras, kamera, kameraføring, scene, scener, scenes, test, testing, three js, three.js, threejs, threejs-visual-validation, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-visual-validation/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-volumetric-clouds

Implement volumetric cloud systems in Three.js. Use for weather-driven density, bounded raymarching, shape/detail erosion, vertical profiles, lighting cones, silver lining, temporal reconstruction, cloud shadows, multiple layers, and scalable quality modes.

Søkeord: shadow, shadows, skygge, skygger, three js, three.js, threejs, threejs-volumetric-clouds

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-volumetric-clouds/SKILL.md)

### scottstts/Threejs-Awesome-Graphics-Agent-Skills:threejs-water-optics

Build production analytic and bounded water in Three.js. Use for photoreal shallow water with gravity-capillary FFT waves, dispersive caustics and diffraction glare, shared multi-wave displacement and normals, bounded RGBA heightfield pool simulation, local drops, object-driven ripples, differential-area caustics, ray-traced pool/water/sphere volum

Søkeord: bølger, hav, ocean, reflection, reflections, refleksjon, refleksjoner, sea, three js, three.js, threejs, threejs-water-optics, vann, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/scottstts/Threejs-Awesome-Graphics-Agent-Skills/blob/897aaa0a49f9346f342993e1eb74a30479f82614/skills/threejs-water-optics/SKILL.md)

### shader-effects-inc/shaders:shaders

Build WebGPU visual effects with the Shaders component library (npm `shaders`) in React, Vue, Svelte, Solid or vanilla JS. Use when a user asks for a shader, animated background, gradient, aurora, blur, glass, distortion, noise, particles, glow, transition, cursor effect, or any GPU-rendered visual on a web page, or mentions shaders.com, the Shader

Søkeord: animasjon, animate, animated, animation, animations, animere, bloom, browser, gloed, glow, glowing, glød, nettleser, shader, shaders, skyggelegger, web

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/shader-effects-inc/shaders/blob/81fd4ece5d493ca6c424a2af41f0e2c361ec8258/skills/shaders/SKILL.md)

### tigerless-labs/autoharness:learn

Use when users /learn, save, remember, or distill lessons.

Søkeord: lagre, lagring, learn, persistence, save, saving

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/tigerless-labs/autoharness/blob/27d13c1d8091681db05a10ef9626081217da240f/skills/learn/SKILL.md)

### Tombonator3000/Dig-HD-Remake:scumm-hd-remake

Bruk ved HD-remake av LucasArts/SCUMM-spill eller når HD-grafikk lages eller rettes. Avklar originalens motiv, funksjon, figuridentitet og design før produksjon, og følg grafikkreglene og den tekniske fremgangsmåten fra The Dig HD.

Søkeord: character, characters, figur, figurer, scumm-hd-remake

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/Tombonator3000/Dig-HD-Remake/blob/c2c9b8e00ba2e83af4001088bbccb976f0f22d1d/docs/skills/scumm-hd-remake/SKILL.md)

### Tombonator3000/guild-life-adventures:bug-hunt

Spawn parallel agents to search for bugs across game mechanics, UI, AI, and store logic. Use when the user wants a broad bug sweep or suspects hidden issues.

Søkeord: bug-hunt

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/Tombonator3000/guild-life-adventures/blob/52deb0fb037af5d7941a37feaaef925793505b3f/.claude/skills/bug-hunt/SKILL.md)

### Tombonator3000/guild-life-adventures:test-game

Run game tests and report failures with context. Use when the user wants to run tests, verify changes, or check for regressions.

Søkeord: test, test-game, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/Tombonator3000/guild-life-adventures/blob/52deb0fb037af5d7941a37feaaef925793505b3f/.claude/skills/test-game/SKILL.md)

### Tombonator3000/Loincloth-Legends:game-tests

Kjør og skriv Playwright-tester for Loincloth Legends i headless Chromium med SwiftShader, med preview-server, window.__game og window.__lib, faste tidssteg, skjermbilder og pikseltester. Bruk før du sier deg ferdig med en endring i spillet, når en test henger eller er treg, og når en test gir svar som ikke stemmer med det du ser.

Søkeord: game-tests, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/Tombonator3000/Loincloth-Legends/blob/60bc0d1a5604ae405874d00794c8e1bc322d88b6/.claude/skills/game-tests/SKILL.md)

### Tombonator3000/Loincloth-Legends:new-level

Lag et nytt brett i Loincloth Legends fra bunnen av, eller bygg om et brett, med LevelDef i src/data/levels.ts, biom, bølger, farer, ryttere, finale, kartnode, brettfil i src/data/layouts, kulisser i STAGE FORGE og tester. Bruk når Tom vil ha et nytt brett, en ny del av kartet eller en ny arena å slåss i.

Søkeord: bølger, hav, new-level, ocean, sea, test, testing, vann, verification, verifisering, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/Tombonator3000/Loincloth-Legends/blob/60bc0d1a5604ae405874d00794c8e1bc322d88b6/.claude/skills/new-level/SKILL.md)

### Tombonator3000/Loincloth-Legends:prop-art

Bestill og ta imot malte kulisser og bildeserier (sprite sheets) fra ChatGPT til brettene i Loincloth Legends. Filnavn prop_<navn>.png og anim_<navn>_<K>x<R>.png, KULISSE-BLOKKEN, reglene for ruter, tools/process_art.py og justering i STAGE FORGE. Bruk når Tom vil ha nye stolper, telt, trær, bannere, fakler eller andre kulisser, med eller uten anim

Søkeord: animasjon, animate, animated, animation, animations, animere, character sheet, figurark, prop-art, sprite sheet, sprite sheets, spriteark, spritesheet, spritesheets

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/Tombonator3000/Loincloth-Legends/blob/60bc0d1a5604ae405874d00794c8e1bc322d88b6/.claude/skills/prop-art/SKILL.md)

### Tombonator3000/Loincloth-Legends:stage-forge

Lag, endre og sjekk brett i Loincloth Legends med brettverkstedet STAGE FORGE eller brettfilene i src/data/layouts. Bruk når Tom vil legge til, flytte eller fjerne kulisser (stolper, telt, palisade, trær rett foran kameraet), sette sammen kulisser av flere deler, lage rader og varianter, slå av generert pynt, flytte bølger, tønner og farer, eller a

Søkeord: animasjon, animate, animated, animation, animations, animere, bølger, camera, cameras, create, generate, generation, generer, generering, hav, kamera, kameraføring, ocean, sea, stage-forge, vann, water, waves

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/Tombonator3000/Loincloth-Legends/blob/60bc0d1a5604ae405874d00794c8e1bc322d88b6/.claude/skills/stage-forge/SKILL.md)

### Tombonator3000/SIGNAL-47:blender-mcp

Inspect, modify, and verify Blender assets using the bpy-dev/blender-mcp distribution, including saved-file headless execution and runtime API lookup. Use for Blender asset work or evaluating this bridge; retain the project's Blender version and export pipeline.

Søkeord: blender-mcp, lagre, lagring, persistence, save, saving

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/Tombonator3000/SIGNAL-47/blob/82683cf3d074df5618270d6cbd3384ba6b4ec69f/Automation/Skills/blender-mcp/SKILL.md)

### Tombonator3000/SIGNAL-47:brainstorming

Explore intent, constraints and design before creative implementation. Use for new features, components, behavior changes or explicitly requested brainstorming; scale the design work to the task and carry existing authorization forward.

Søkeord: brainstorming

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/Tombonator3000/SIGNAL-47/blob/82683cf3d074df5618270d6cbd3384ba6b4ec69f/Automation/Skills/brainstorming/SKILL.md)

### Tombonator3000/SIGNAL-47:game-production

Develop games and interactive visual experiences from a brief or existing prototype into coherent, testable production slices. Use for game production planning, design bibles, art pipelines, asset review, or coordinated gameplay and visual polish. Adapt to the existing engine and platform; do not apply the full workflow to unrelated small code fixe

Søkeord: game-production, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/Tombonator3000/SIGNAL-47/blob/82683cf3d074df5618270d6cbd3384ba6b4ec69f/Automation/Skills/game-production/SKILL.md)

### Tombonator3000/SIGNAL-47:gauntlet-loop

Build or advance a project through the Universal Gauntlet workflow, comparing an actual working slice with its intended experience and verifying user journey, visuals, performance and delivery. Use when the user invokes Gauntlet or explicitly requests this complete production and verification loop.

Søkeord: gauntlet-loop, test, testing, verification, verifisering

[Profil eller kort](SKILLS.md) · [Kilde](https://github.com/Tombonator3000/SIGNAL-47/blob/82683cf3d074df5618270d6cbd3384ba6b4ec69f/Automation/Skills/gauntlet-loop/SKILL.md)

Bygges med `python3 scripts/build_search_index.py`. Rediger kildenotater, skillmetadata og search-terms.json, og bygg på nytt.

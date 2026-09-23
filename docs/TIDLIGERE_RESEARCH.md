# Tidligere research og erfaringer

Samlet 23. september 2026 fra eksisterende prosjektbibliotek, egne prosjektjournaler og lokale skills. Dette dokumentet bevarer vurderingene som faktisk finnes. Det er ikke en ny installasjon eller runtime-test av prosjektene. Ny metadatahenting i hovedkatalogen erstatter ikke de historiske bevisene nedenfor.

De 13 tilleggene nedenfor var ikke med i den tidligere felleskatalogen eller i GitHub-starlisten hentet i dette oppdraget. De inngår som egne referanser fordi tidligere arbeid har konkrete kilder til dem. [Maskinlesbar tilleggsliste](../data/extra-references.json) og [gjenbruksnotater](../data/extra-notes.json) lar resten av biblioteket indeksere dem.

## Skills og motorstyring

| Referanse | Historisk bevis og versjon | Gjenbruk |
|---|---|---|
| [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp) | Kandidat nevnt i den opprinnelige SIGNAL / 47-samtalen; ingen festet commit eller dokumentert lokal test i det bevarte utdraget. | Undersøk ved behov for Unity Editor-styring. Kontroller dagens installasjon, transport og Unity-versjon før bruk. |
| [CoderGamester/mcp-unity](https://github.com/CoderGamester/mcp-unity) | En separat Unity MCP-kandidat i samme samtale; ingen festet commit eller dokumentert lokal test i utdraget. | Sammenlign mot konkret redigerings-/inspeksjonsbehov. Repoene med lignende navn er ikke samme integrasjon. |
| [ahujasid/blender-mcp](https://github.com/ahujasid/blender-mcp) | Historisk kandidat fra samme samtale. SIGNALs Gauntlet04-kopi sa uttrykkelig at denne broen ikke var installert da. | Bevar som kilde til den opprinnelige diskusjonen. Ikke overfør senere testresultater fra bpy-dev-distribusjonen til dette repoet. |
| [bpy-dev/blender-mcp](https://github.com/bpy-dev/blender-mcp/tree/e8ac4088d4a3e0469d3eff9f9bb2dd717e899219) | Kildelesing og lokal probe 12. september 2026, commit `e8ac4088d4a3e0469d3eff9f9bb2dd717e899219`. GPL-3.0-or-later oppgitt i vurderingen. | Saved-file-inspeksjon, runtime API-oppslag, separate checkpoints, Blender-render og FBX-rundtur ved bevart motor-/eksportløype. |
| [obra/superpowers](https://github.com/obra/superpowers/tree/b36e0829c6d0140e93cfef2ca599b1b07d4a7797) | Lokal brainstorming-skill avledet fra `skills/brainstorming` ved `b36e0829c6d0140e93cfef2ca599b1b07d4a7797`, tilpasset 13. september 2026. MIT-lisens og kildehash bevart. | Designavklaring og beslutningsarbeid før implementering. Lokal skill har endrede godkjenningsregler; den er ikke en uendret kopi av upstream. |

Kilder: [opprinnelig MCP-utdrag](historikk/signal47-mcp-candidates-excerpt.md), [Gauntlet04s daværende verktøystatus](historikk/signal47-gauntlet-tools-excerpt.md), [bpy-dev-vurdering](historikk/blender-mcp-assessment.md), [lokal Blender-verifikasjon](historikk/blender-mcp-local-verification.md), [brainstorming-opphav](historikk/brainstorming-SOURCE.json) og [MIT-lisens](historikk/brainstorming-LICENSE.txt).

Blender-proben gjaldt Blender 4.5.13 LTS, lokal stdio og lagrede testfiler. Initialisering/verktøyfunn, avgrenset sceneinspeksjon, checkpoint/reåpning, CPU-render og FBX-eksport/import fungerte. `BlendData.file_path_foreach` manglet; eksplisitt fallback ble testet. Det generiske FBX-operatoroppslaget var ikke støttet. Utvalgte upstream-suiter ga **83 bestått, 7 hoppet over og 1 feil av 91 tester**. Live add-on/UI, CUDA-bildeverktøy, separat bpy-runtime, full testsuite og benchmark var ikke verifisert. Det bevarte notatet angir maskinens daværende stier; de er ikke universelle installasjonskrav.

## Rendering, vann og vegetasjon

| Referanse | Historisk bevis og versjon | Gjenbruk |
|---|---|---|
| [SamG-Coder/WaterCuda](https://github.com/SamG-Coder/WaterCuda) | Navngitt i The Deep Ones' akvatiske produksjonsjournal som inspirasjonskilde. Ingen upstream-commit oppgitt der. | Vann- og GPU-research. Journalen sier at egen Unity-implementasjon ble skrevet, uten kopiert referansekode; CUDA, FFT-hav og full gruntvannsløser er ikke avhengigheter i den beskrevne kandidaten. |
| [cortiz2894/stylized-components](https://github.com/cortiz2894/stylized-components) | Eget Voidcraft-notat oppgir MIT, copyright 2026 Christian Ortiz (Cortiz). Ingen upstream-commit oppgitt. | Felles terreng-/vegetasjonsmaske, rotfestet vind, nedtråkking, lys gjennom blader og vannringer. Egne Unity C#/HLSL-systemer ble skrevet; Three.js/React-kode, GLB-er, teksturer og demomedier ble ikke vendoret. |

Kilder: [The Deep Ones' vannproveniens](historikk/deep-ones-water-provenance-excerpt.md) og [Voidcrafts tilpasningsnotat](historikk/voidcraft-stylized-components.md). Originalene er festet til henholdsvis [The Deep Ones `e6d893d`](https://github.com/Tombonator3000/the-deep-ones-3d/blob/e6d893dca5ce46d8bcce4fcd60760e14fffdd193/docs/unity/AQUATIC.md) og [Voidcraft `5557e24`](https://github.com/Tombonator3000/Voidcraft/blob/5557e24f717dbffd90c3f06b61588e4864e93060/docs/developer/STYLIZED_COMPONENTS_ADAPTATION.md). Kildedokumentene er byte-identiske med de oppgitte commitene.

De tre kyst-/WebGPU-repoene som allerede var katalogført, beholdes med sine opprinnelige versjoner, kodeinnganger og lisenskopier i [vurderingen fra 20. september](../repoer/coastal-webgpu-2026-09-20.md). Kystportens medfølgende CUDA WebShader-versjon er forskjellig fra versjonen som ble vurdert separat. Behold denne forskjellen ved senere eksperimenter.

## Gaussian splats og relatert forskning

| Referanse | Historisk bevis og versjon | Gjenbruk og begrensning |
|---|---|---|
| [haato-w/3d-gabor-splatting](https://github.com/haato-w/3d-gabor-splatting) | Researchkilde kontrollert 13. september 2026; det lagrede notatet oppgir begrensninger på kommersiell bruk. Ingen commit festet i notatet. | Forskning på fine overflatemønstre. Ekstra frekvens-/fase-/vektdata krever tilpasset renderer; dette er ikke et generelt kvalitetsfilter for vanlige splats. |
| [haato-w/diff-gabor-rasterization](https://github.com/haato-w/diff-gabor-rasterization) | Tilhørende rasterizer; samme historiske lisensforbehold. Ingen festet commit. | CUDA-basert forskningskomponent. Kontroller separat lisens og implementasjonskrav ved konkret bruk. |
| [playcanvas/supersplat](https://github.com/playcanvas/supersplat) | Dokumentert som verktøy for interaktiv splat-redigering; ingen enkeltversjon festet i kilden. | Klargjøring og inspeksjon. Skill mellom WebGL-redigering og eksportmuligheter som krever WebGPU. |
| [playcanvas/splat-transform](https://github.com/playcanvas/splat-transform) | Dokumentert konverterings-, transformasjons- og filtreringsverktøy; ingen enkeltversjon festet i kilden. | Bevar originaler og fest versjon. SOG-komprimering på CPU betyr ikke CPU-støtte for alle operasjoner. GLB med `KHR_gaussian_splatting` er ikke en vanlig trekantmesh. |
| [aras-p/UnityGaussianSplatting](https://github.com/aras-p/UnityGaussianSplatting/tree/2c6fed37da67a217367261fcfcd3316d34c73e76) | Splat21-probe med 1.1.1 ved `2c6fed37da67a217367261fcfcd3316d34c73e76`, Unity 6000.3.22f1 / URP 17.3 / Intel ARL. | Vulkan rendret små syntetiske fixtures; OpenGL feilet med kernel-/Render Graph-feil. En okklusjonsfeil gjensto. Resultatene gjelder dette oppsettet; integrasjon var ikke godkjent. |
| [arloopa/UnitySplats](https://github.com/arloopa/UnitySplats/tree/6c0258189a2b124af1282fa9236fd9b6637f1a1a) | Hybrid23-probe med 1.2.0 ved `6c0258189a2b124af1282fa9236fd9b6637f1a1a`; historisk MIT-sjekk og avgrenset Vulkan-test. | Matchet mesh-proxy ga synlig lysrespons. Kamera, importerinnstillinger, okklusjon og avhengigheter krevde konkrete korreksjoner. Behold komponentmerknader for Unity.WebP/libwebp og DLL-er. |

Den bevarte [splat-vurderingen](historikk/splats-and-generated-characters.md) inneholder primærkildelenker, oppsett, feil og senere korrigeringer. Den er et levende skillnotat kopiert slik det forelå 23. september; innledningens kildekontrolldato 13. september gjelder ikke automatisk datoen for alle senere tilføyde eksperimenter.

Viktige erfaringer fra journalen:

- En trent rekonstruksjon og tilfeldige Gaussians samplet fra en mesh er forskjellige datasett. Hybrid23s mesh-samplede prøve var ikke en gyldig erstatning for en god miljørekonstruksjon ved vurdering av fotorealisme.
- Scan25 oppgir at korrekt Gamma/Linear-innstilling forbedret kildefargegjengivelsen. Beholdt SH3 og 493 869 Gaussians ga omtrent 45,8 FPS i en 60-sekunders kameramåling på den testede Intel-maskinen. Dette er ikke et ytelsesbudsjett for et helt nivå.
- Vellykket filimport eller numerisk integritet verifiserer ikke visuell kvalitet, okklusjon, kollisjon, relighting eller ytelse. Hvert punkt må ha egne observasjoner.
- Splat21s mislykkede OpenGL-probe og maskinens senere OOM/restart er dokumentert uten påstand om fullstendig årsakskjede. Et senere avgrenset cgroup-forsøk er et separat bevis. Ikke slå disse sammen til én generell teststatus.
- Kodelisens, rettigheter til kildebilder/skann og genereringstjenestens vilkår er separate. Notatets historiske omtale av en betalt tjeneste er ikke autorisasjon til nye kjøp eller genereringer.

## Relasjoner til referanser som allerede finnes

**Desktop Habitats → The Deep Ones.** [chaseleantj/desktop-habitats ved `e6ea239e92bb04dcd3953f80758aef61c72b2146`](https://github.com/chaseleantj/desktop-habitats/tree/e6ea239e92bb04dcd3953f80758aef61c72b2146) ble inspisert, særlig `scenes/riverscape/src/fish.js`, `water.js`, `food.js` og atferdstester. The Deep Ones skrev egen Unity-simulering for fisk, krokdrift, tang og partikler. Journalen sier at ingen akvariekode ble kopiert. Se [bevart utdrag](historikk/deep-ones-habitats-excerpt.md) og [versjonert original](https://github.com/Tombonator3000/the-deep-ones-3d/blob/e6d893dca5ce46d8bcce4fcd60760e14fffdd193/docs/unity/LIVING_COAST.md).

**Blocks Beyond the Stars → Voidcraft.** [marceld23/BlocksBeyondTheStars](https://github.com/marceld23/BlocksBeyondTheStars) er faktisk kodegrunnlag for Voidcrafts Unity-klient, autoritative .NET-server, prosedyregenererte verden og øvrige sandbox-systemer. Dette er en sterkere gjenbruksrelasjon enn inspirasjon. Foundation-notatet oppgir AGPL og bevarte interne navn. Se [bevart utdrag](historikk/voidcraft-foundation-excerpt.md) og [versjonert original](https://github.com/Tombonator3000/Voidcraft/blob/5557e24f717dbffd90c3f06b61588e4864e93060/docs/developer/VOIDCRAFT_FOUNDATION.md). Opplysninger om daværende spillstatus skal ikke leses som dagens utgivelsesstatus.

**VT323 → SIGNAL / 47.** [VT323 hos Google Fonts](https://github.com/google/fonts/tree/main/ofl/vt323) er en faktisk brukt fontressurs med SIL Open Font License 1.1. Den eldre journalen oppgir at full lisens og opphavsmerknad ble pakket sammen med spillet. Se [bevart krediteringsutdrag](historikk/signal47-font-credit-excerpt.md). Hele `google/fonts` legges ikke i reposynken; denne avgrensede ressurslenken er tilstrekkelig for gjenfinning.

**Gauntlet og game-production.** De personlige arbeidsflytene samler egne produksjonserfaringer, og skal ikke presenteres som upstream-motorer eller som bevis på installerte integrasjoner. Her er bare de konkrete researchkildene og opphavsnotatene bevart; ingen skill er installert eller aktivert av katalogiseringen.

## Hva som er bevart

Den tidligere [Sentient-katalogen](../repoer/sentient-2026-09-12.md) med ti verktøy og [kyst-/WebGPU-katalogen](../repoer/coastal-webgpu-2026-09-20.md) beholdes som historiske vurderinger. De nye avgrensede dokumentkopiene/utdragene finnes under [historikk](historikk/README.md). [Manifestet](historikk/manifest.json) registrerer originale stier, SHA-256, uttrekkslinjer og kontrollerte Git-commiter. Ingen spillkode, store assets eller fullstendige spillprosjekter er kopiert.

Ved senere bruk: finn relevant referanse, les den festede kilden og sammenlign med valgt ny versjon. Bevar lisens-/opphavsmerknader og registrer eventuell import, endring og faktisk test i målprosjektet. Bibliotekets historiske erfaringer er beslutningsgrunnlag, ikke en automatisk godkjenning av integrasjon.

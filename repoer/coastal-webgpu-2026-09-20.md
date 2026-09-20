# Kystvann, CUDA WebShader og WebGPU

Kontrollert 20. september 2026 for The Deep Ones og senere prosjekter. Tre unike repoer; den gjentatte lenken er slått sammen. Status: dokumentasjon og utvalgt kildekode vurdert, ikke installert, kjørt eller integrert. Dette er et referansearkiv, ikke en komplett kildekodekopi.

## Vurdering

| Referanse | Brukbar til | Tilpasning / begrensning |
|---|---|---|
| [coastal-simulation-cuda-webshader](https://github.com/SamG-Coder/coastal-simulation-cuda-webshader) | Strandbryting, transportert skum/turbulens, våte steiner og sjøsprøyt. GPU-felter beholdes på GPU-en. | Three.js/WebGPU-port av originalen. For Unity anbefales avgrenset portering av algoritmer til HLSL/C#, ikke import av hele nettleserruntime. |
| [coastal-simulation](https://github.com/iamtechartist/coastal-simulation) | Visuell og numerisk grunnreferanse for kystsonen, våt sand og strandkontakt. | Three.js med gruntvannsmodell; JS-simulering og WASM-akselerasjon. Ingen ferdig Unity-integrasjon. |
| [cuda-webshader](https://github.com/SamG-Coder/cuda-webshader) | WebGPU-prototyper, GPU-partikler og utforsking av compute/render uten CPU-rundtur. | Kompilerer et avgrenset CUDA-delsett til WGSL. Ikke generell CUDA-kompatibilitet eller en Unity-plugin. |

CUDA-navnet betyr her oversetting til nettleserens WebGPU, ikke kjøring med NVIDIAs native CUDA-runtime. Et CUDA Toolkit er ikke nødvendig for nettleserapplikasjonen. Den konkrete kystporten krever WebGPU og har ingen WebGL-/CPU-reservevei. Maskin- og driverstøtte må prøves; den er ikke verifisert på vår Intel ARL-maskin.

Kystporten beskriver en 2D høydefeltmodell for grunt vann. Den gir ikke volumetriske bølger som velter over, og løser ikke fiskemodeller, stim-AI eller undervannsmaterialer alene. Ytelsestall i repoene er utviklernes resultater, ikke målinger i The Deep Ones.

Min anbefaling er å bruke kystrepoene som referanse for et lite Unity-forsøk nær stranden. Kompilatorprosjektet er mest relevant for egne nettleserdemoer. Bevar eksisterende motor og målplattform; en ny vannmodell bør vise en målbar forbedring før den erstatter fungerende kode.

## Versjonsfeste og lisenser

- [SamG-Coder/coastal-simulation-cuda-webshader](https://github.com/SamG-Coder/coastal-simulation-cuda-webshader/commit/e5a80fe42b4eeba6c01de1467035bafd69592d3e): `e5a80fe42b4eeba6c01de1467035bafd69592d3e`. [README ved kontrollert commit](https://github.com/SamG-Coder/coastal-simulation-cuda-webshader/blob/e5a80fe42b4eeba6c01de1467035bafd69592d3e/README.md).
- [iamtechartist/coastal-simulation](https://github.com/iamtechartist/coastal-simulation/commit/2e95e1a3e757ca1268247417dee01606e5e3d55c): `2e95e1a3e757ca1268247417dee01606e5e3d55c`. [README ved kontrollert commit](https://github.com/iamtechartist/coastal-simulation/blob/2e95e1a3e757ca1268247417dee01606e5e3d55c/README.md).
- [SamG-Coder/cuda-webshader](https://github.com/SamG-Coder/cuda-webshader/commit/d1abd25c32b93d40ce13c7757fccdd0ce6e2f01a): `d1abd25c32b93d40ce13c7757fccdd0ce6e2f01a`. [README ved kontrollert commit](https://github.com/SamG-Coder/cuda-webshader/blob/d1abd25c32b93d40ce13c7757fccdd0ce6e2f01a/README.md).

Kystportens medfølgende CUDA WebShader er festet til `c272bb782f8458761af2894e8771517f64ecdae6`, som er en annen versjon enn det selvstendige repoet vurdert her. Kystportens GPU-bro sjekker Three.js r185 eksplisitt; det selvstendige prosjektets package.json bruker Three.js 0.186.0. Ikke bytt disse komponentene om uten å verifisere kompatibilitet.

De tre rotlisensene er MIT. Behold tilhørende copyright- og lisensmerknader ved kopiering eller vesentlig tilpasning av koden. Kystporten krediterer både Techartist og SamG-Coder; Three.js og medfølgende komponenter har egne merknader. Eksempelinnhold i kompilatorrepoet må vurderes på komponentnivå før gjenbruk.

[Maskinlesbar katalog](coastal-webgpu-2026-09-20.json) har søkeord, eksakte kildekodelenker og SHA-256 for lokale lisens-/opphavskopier under `kilder/coastal-webgpu-2026-09-20/`. Katalogen skiller vurdert kilde fra installert og runtime-testet teknologi.

## Senere bruk

1. Finn relevant repo og kodeinngang i JSON-katalogen; sammenlign festet commit med siste oppstrømsversjon.
2. Avgrens én effekt og test i målplattformens eksisterende renderer. Behold attribusjon ved kodegjenbruk.
3. Mål GPU-tid, minne og visuell gevinst på faktisk målmaskin. Kontroller lavere kvalitetsnivå og funksjon uten den nye effekten.
4. Registrer hva som faktisk importeres, endres og testes i prosjektets egen produksjonslogg. Referanseføring alene betyr ikke at integrasjonen er godkjent eller ferdig.

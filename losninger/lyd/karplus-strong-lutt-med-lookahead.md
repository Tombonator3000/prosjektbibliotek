---
id: karplus-strong-lutt-med-lookahead
tittel: Prosedyrisk lutt med Karplus-Strong og en sequencer med lookahead
domene: lyd
stikkord: WebAudio, musikk, prosedyrisk, Karplus-Strong, lutt, pluck, sequencer, lookahead, setInterval, playbackRate, uten lydfiler
stack: WebAudio API i nettleseren, uten lydfiler
status: PASS
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:src/music.js#L259
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# Prosedyrisk lutt med Karplus-Strong og en sequencer med lookahead

## Symptom

Du vil ha musikk uten lydfiler (én fil, liten størrelse). Notene skal ligge stødig i takt, selv når fanen er tung eller ligger i bakgrunnen.

## Årsak

`setTimeout` og `setInterval` er unøyaktige. Spiller du noter rett fra dem, hakker takten. Å syntetisere hver note på nytt koster mye.

## Løsning

- **Lutt**: Karplus-Strong, forhåndsrendret én gang per tone til en AudioBuffer og lagret i et kart. Bruk filtrert støy som startbuffer og et kamfilter for plukkeposisjonen (nasal klang). Dempingen er 0,997, eller 0,9985 for dype toner.
- **Avspilling**: en `AudioBufferSourceNode` per note gjennom lavpass, en topp på 240 Hz for kroppen, gain og panorering. `playbackRate` stiller tonehøyden helt nøyaktig.
- **Sequencer**: `setInterval` hvert 25. ms planlegger alle noter som skal spilles de neste 140 ms, med `src.start(t)` på lydklokka.

```js
while (s.next < ctx.currentTime + 0.14) { song.step(this, s, s.n, s.next, s.sd); s.next += s.sd; s.n++; }
if (s.next < ctx.currentTime - 0.5) s.next = ctx.currentTime + 0.05;   // fanen lå i bakgrunnen
```

## Fallgruver

- Lengden på forsinkelseslinja er et heltall. Regn ut den faktiske tonen (`sr / (N + 0.5)`) og rett den med `playbackRate`.
- AudioContext må startes etter et trykk fra spilleren.
- Etter at fanen har ligget i bakgrunnen, må `next` hoppes fram, ellers kommer alle notene på en gang.

## Slik verifiseres det

Rendre en sang i en OfflineAudioContext og mål tidspunktene for notene, eller lytt med fanen i bakgrunnen og så i forgrunnen igjen.

## Bevis

- [memory.md i DoD-Roguelite, musikken](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/memory.md?plain=1#L40), [Karplus-Strong i music.js](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/music.js#L259) og [sequenceren](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/music.js#L244).

## Brukt i

- `Tombonator3000/DoD-Roguelite@5e940d2`: all musikken i spillet siden 0.2: tittel, by, vertshus, kloakk og kamp.

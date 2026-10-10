---
id: pages-deler-localstorage
tittel: Alle spillene på GitHub Pages deler localStorage
domene: bygg
stikkord: localStorage, GitHub Pages, opphav, origin, kvote, QuotaExceededError, lagring, prefiks, nøkler
stack: Nettleser, GitHub Pages under tombonator3000.github.io
status: PASS
opphav: Tombonator3000/SIGNAL-47@925d61336e95abb9310646be0e0de77271ad0f4a:web/memory.md#L166
dato: 2026-10-09
agent: Claude
lisens: Toms egen kode, ingen lisensfil i repoet
sist_sjekket: 2026-10-09
---

# Alle spillene på GitHub Pages deler localStorage

## Symptom

Lagring feiler med QuotaExceededError, eller nøkler kolliderer med et annet spill. Det skjer bare på GitHub Pages, ikke lokalt.

## Årsak

Alle Pages-sidene til Tom ligger under `https://tombonator3000.github.io/`, og det er ett opphav. localStorage og kvoten (rundt 5 MB) deles da av alle spillene.

## Løsning

- Gi alle nøkler et prefiks per spill, for eksempel `s47.` eller `svartnebb.`.
- Legg store ting, som bilder og miniatyrer, i IndexedDB i stedet.
- Fang feil ved skriving, og si fra til spilleren i stedet for å miste lagringen.

## Fallgruver

- `localStorage.setItem(k, undefined)` lagrer strengen "undefined".
- Et privat vindu eller blokkert lagring kan kaste feil allerede ved lesing.

## Slik verifiseres det

Åpne to av spillene på Pages i samme nettleser og se i utviklerverktøyene: nøklene ligger under samme opphav.

## Bevis

- Opphavet følger av adressene: [SIGNAL-47](https://tombonator3000.github.io/SIGNAL-47/) og [DoD-Roguelite](https://tombonator3000.github.io/DoD-Roguelite/) har begge `tombonator3000.github.io`. Se også [same-origin-regelen hos MDN](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy).
- [web/memory.md i SIGNAL-47, linje 166](https://github.com/Tombonator3000/SIGNAL-47/blob/925d61336e95abb9310646be0e0de77271ad0f4a/web/memory.md?plain=1#L166).

## Brukt i

- `Tombonator3000/SIGNAL-47@925d613`: alle nøkler har prefikset `s47.`, og bilder ligger i IndexedDB.
- `Tombonator3000/DoD-Roguelite@5e940d2`: nøklene har prefikset `svartnebb.`. Miniatyrene i lagringene ligger fortsatt i localStorage.

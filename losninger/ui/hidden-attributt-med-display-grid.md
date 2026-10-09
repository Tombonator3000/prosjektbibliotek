---
id: hidden-attributt-med-display-grid
tittel: hidden virker ikke på elementer med display: grid
domene: ui
stikkord: hidden, attributt, display grid, display flex, CSS, skjult, vises likevel, important
stack: HTML og CSS
status: PASS
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:src/page.html#L26
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# hidden virker ikke på elementer med display: grid

## Symptom

`el.hidden = true` skjuler ikke en skjerm eller et panel. Elementet vises fortsatt.

## Årsak

Attributtet `hidden` er bare `display: none` i nettleserens eget stilark. En egen regel som `.screen { display: grid }` er sterkere og vinner.

## Løsning

```css
[hidden] { display: none !important; }
```

## Fallgruver

- Knapper beholder fokus etter klikk, og mellomrom kan da trykke dem igjen. Kall `blur()` når et løp starter eller fortsetter.
- `[hidden=until-found]` bør unntas hvis du bruker den.

## Slik verifiseres det

Sett `hidden` på en skjerm med `display: grid`. Den skal bli borte.

## Bevis

- [memory.md, fallgruver](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/memory.md?plain=1#L180) og [regelen i page.html](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/src/page.html#L26).

## Brukt i

- `Tombonator3000/DoD-Roguelite@5e940d2`: alle skjermene i spillet (meny, pause, dialog, reisekart, verdenskart).

---
id: grid-skjerm-klipper-toppen
tittel: Høye paneler mister toppen når skjermen sentreres med grid
domene: ui
stikkord: CSS, grid, place-items center, overflow, scroll, mobil, toppen klippes, panel, safe center, margin auto
stack: CSS grid, fullskjerms overlegg med overflow-y: auto
status: PASS
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:src/page.html#L853
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# Høye paneler mister toppen når skjermen sentreres med grid

## Symptom

På mobil er toppen av et panel borte, og det går ikke an å rulle opp dit. Nederst ruller det fint.

## Årsak

Skjermen er `display: grid; place-items: center; overflow-y: auto`. Er panelet høyere enn skjermen, sentreres det likevel, og det som stikker over toppen, havner utenfor området det går an å rulle i.

## Løsning

Sentrer med automatiske marger i stedet. De blir 0 når panelet er for høyt:

```css
#world { place-items: start center; }
#world .panel { margin-block: auto; }
```

## Fallgruver

`place-items: safe center` gjør det samme i nyere nettlesere, men margin-trikset virker overalt.

## Slik verifiseres det

Åpne skjermen i 390 x 844 og 844 x 390. Overskriften skal synes øverst, og resten skal kunne rulles fram.

## Bevis

- [Loggen 9. oktober 00:44](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/log.md?plain=1#L270).

## Brukt i

- `Tombonator3000/DoD-Roguelite@bc86711`: verdenskartet på mobil, både på langs og på tvers.

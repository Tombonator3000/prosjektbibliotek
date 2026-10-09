---
id: bilder-for-og-etter-med-worktree
tittel: Bilder før og etter en grafikkendring med git worktree
domene: testing
stikkord: før og etter, sammenligning, skjermbilder, git worktree, regresjon, grafikk, A/B
stack: git, Node-bygg, Playwright-testrigg
status: PASS
opphav: Tombonator3000/DoD-Roguelite@5e940d274364fe068e298c51012a0edb0eca5f5d:memory.md#L174
dato: 2026-10-09
agent: Claude
lisens: MIT
offentlig_kontrollert: 2026-10-09
sist_sjekket: 2026-10-09
---

# Bilder før og etter en grafikkendring med git worktree

## Symptom

Du har endret lys, bloom eller materialer og vil vise hva som ble bedre, men det gamle bygget er borte.

## Årsak

Byggemappa inneholder bare det siste bygget, og å sjekke ut forrige commit i samme mappe rører til arbeidet ditt.

## Løsning

```sh
git worktree add <scratch>/before HEAD          # forrige commit i en egen mappe
ln -s $PWD/node_modules <scratch>/before/node_modules
(cd <scratch>/before && node build.mjs)
ROOT=<scratch>/before node <testrigg> before.png steg.json
node <testrigg> after.png steg.json             # de samme stegene på det nye bygget
git worktree remove --force <scratch>/before
```

Sett bildene side om side (for eksempel med Pillow).

## Fallgruver

- Tilfeldige nivåer blir ulike for hver kjøring. Sammenlign steder som er like hver gang, eller gi spillet et fast frø.
- Bruk de samme innstillingene (kvalitet, vindusstørrelse, tid på døgnet) i begge kjøringene.

## Slik verifiseres det

To bilder fra det samme kamerastedet, der den eneste forskjellen er endringen.

## Bevis

- [Loggen 9. oktober 00:29](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/log.md?plain=1#L266) og [memory.md](https://github.com/Tombonator3000/DoD-Roguelite/blob/5e940d274364fe068e298c51012a0edb0eca5f5d/memory.md?plain=1#L174).

## Brukt i

- `Tombonator3000/DoD-Roguelite@7e5ba8e`: bloom, miljøkart og trekroner før og etter i byen, Ekeskogen og kloakken.

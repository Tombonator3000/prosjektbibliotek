# Minne for prosjektbiblioteket

Beslutninger og fallgruver som neste person trenger. Dagbok hører hjemme i log.md.

## Løsningskort (fra 2026-10-09)

- Kortene er de eneste kildefilene: `losninger/<domene>/<id>.md` med en nøkkel: verdi-blokk øverst og faste seksjoner (Symptom, Årsak, Løsning, Fallgruver, Slik verifiseres det, Bevis, Brukt i). `data/losninger.json` og `LOSNINGER.md` er generert av `scripts/build_solution_index.py`.
- Domenene er grafikk, lyd, testing, ui, bygg og regler. De samme står i skillen spill-gjenbruk i Toms Claude-konto, så endrer du lista, må skillen også endres.
- `opphav` har formen `eier/repo@<40 tegn>:sti#Llinje`. Status gjelder opphavet på datoen i kortet; biblioteket kjører ikke koden.
- `verify.py` krever at opphavet står i `data/offentlig-inventar.json` (owned_public eller starred), eller at kortet har `offentlig_kontrollert`. Når inventaret er synkronisert og har fått repoet, kan nøkkelen fjernes.
- Nøkkelblokken tåler bare enkle verdier. Lister skrives med komma (stikkord, se_ogsa), og bevis og bruk som punkter i sine seksjoner.
- Lenker til Markdown-filer på GitHub trenger `?plain=1#L<linje>` for å vise linjen.

## Fallgruver

- `scripts/sync_public_inventory.py` får 403 fra proxyen i Claudes skyøkter (users/Tombonator3000/starred). Kjør den på en egen maskin.
- `build_skill_index.py --refresh` krever at alle repoene i inventaret er skannet. Et repo i owned_public uten skillskann gjør at verify.py feiler.
- Biblioteket er offentlig. Ingen navn, stier eller kode fra private repoer, heller ikke i kort, log.md eller memory.md.

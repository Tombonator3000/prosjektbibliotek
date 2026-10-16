# Minne for prosjektbiblioteket

Beslutninger og fallgruver som neste person trenger. Dagbok hører hjemme i log.md.

## Biblioteket brukes før prosjektarbeid

- START_HER.md er inngangen. SOK.md og data/search-index.json er generert fra historisk katalog, ferskt inventar, norske notater, skillmetadata og løsningskort. Kjør scripts/build_search_index.py etter endringer; verify.py avviser utdaterte indekser.
- find.py rangerer tittel, symptom og nøkkelord foran brødtekst. data/search-terms.json har synonymer og ekstra behovsord. Standard er ti treff og alle behovsord; --match any utvider eksplisitt. Filtre er dokumenterte ord, ikke kompatibilitetsbevis.
- build_skill_index.py --describe leser navn og beskrivelse fra festede, offentlige Git-blobber uten å kjøre skillinstruksjoner. 273 av 274 skillfiler har beskrivelse. Identiske blobber er ett søketreff med alle kildestedene beholdt.
- skills/prosjektbibliotek er egen vedlikeholdt skillpakke, med lokal søkehjelper og GitHub-rute. scripts/setup_agents.py installerer den for Codex og Claude Code og oppdaterer bare den avgrensede rutineblokken i de globale instruksjonsfilene. Se docs/AGENTOPPSETT.md for andre maskiner og skyøkter.
- Søkerutinen gjelder teknisk prosjektarbeid før ny implementering og verktøyvalg. Svake treff prøves bredere én gang; manglende tilgang rapporteres uten å blokkere resten av oppgaven.
- tests/test_search.py prøver faktiske behovssøk, filtre, skillkopier, indeksens oppdatering og gjentatt installasjon som bevarer brukerinnstillinger. Testene bruker ikke nettverk.

## Offentlig innhenting 2026-10-16

- Siste inventar er fra 16. oktober: 75 offentlige stjerner, 37 egne offentlige repoer og 101 unike repoer i skilldekningen. Sammenlign neste innhenting med repo-ID-ene og stjernedatoene i `data/offentlig-inventar.json`, ikke med den historiske listen i STARRED.md.
- Alle 20 nye stjerner siden 5. oktober har norske notater i `data/starred-notes.json`. `find.py` bruker disse også for inventaroppføringer uten historisk profil. Et valgfritt `profile_path` peker til et eget notat.
- Egen fork `Tombonator3000/decomp.wtf` er opprettet fra `i12bp8/decomp.wtf`. Begge main-grener pekte til `575b4a30ed481ff5497dfb9ce4f599368a95a04a` ved kontrollen. Originalen ble arkivert 15. oktober. Se `repoer/decomp-wtf-2026-10-16.md` og JSON-manifestet; bevarte dokumentkilder kontrolleres av verify.py.
- decomp.wtf 0.10.6 oppgir Linux og ustabil Windows-støtte via WSL 2, uten macOS-støtte. Verktøyet er ikke installert eller runtime-testet her.
- Inventaret dekker nå de offentlige opphavene til alle 24 løsningskort. 20 midlertidige `offentlig_kontrollert`-felt er fjernet uten å endre testdatoer eller bevis.

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
- Sorteringsfeilen i build_catalog.py ble rettet 2026-10-16 med en stabil sekundær sorteringsnøkkel. En test sammenligner genererte profiler og katalog fra to ulike Python-hashfrø.

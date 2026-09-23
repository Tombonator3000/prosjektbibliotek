# Kontroll av første GitHub-samling

Utført 23. september 2026. Katalogens innhenting: `2026-09-23T08:55:18+00:00`.
SHA-256 for kontrollert `data/catalog.json`: `b98717c1779d0dc88f1b85d91e2ff9893047afe78796771fe9fa62920702ea47`.

| Kontroll | Resultat |
|---|---|
| Fullstendig innlogget stjerneliste | PASS – 22 unike repo-id-er; alle sider hentet |
| Separat kontrollhenting | PASS – paginert GitHub-kall med 7 resultater per side ga nøyaktig samme 22 id-er |
| Skjermbildene fra brukeren | PASS – alle 15 viste repoer finnes i starlisten |
| Samlet katalog | PASS – 46 unike repoer, alle med norske profiler og kategorier |
| Navneendring | PASS – ahujasid/blender-mcp videresendes til ahujasid/mcp-for-blender; historisk navn og notater beholdt |
| Kildeintegritet | PASS – 108 kildefiler kontrollert; 90 nye upstream-dokumenter, 12 historikkopier/utdrag og 6 tidligere lisens-/opphavsfiler |
| Lokale dokumentlenker | PASS – authored Markdown-lenker og profiler finnes; rå historiske kildehenvisninger er beholdt i sine dokumenter |
| Søk | PASS – fritekstsøk etter vann ga 7 treff; kategorisøk og kategoriliste kjørt |
| Feildeteksjon | PASS – isolerte negative kontroller avviste manipulert kilde, manglende stjerne og brutt lokal lenke |
| Eksisterende bibliotek | PASS – tidligere repoer/-notater og kildefiler beholdt uendret |

Utførte kommandoer inkluderer `python3 scripts/sync_github.py`, `python3 scripts/build_catalog.py`, `python3 scripts/verify.py`, `python3 scripts/find.py vann`, kategorisøk og Git-diffkontroll av egne filer. Bevarte originaltekster er unntatt stilkontrollen: de har blant annet originale sluttmellomrom og reStructuredText-overskrifter som Git ellers tolker som konfliktmarkører. Disse filene kontrolleres mot kildens byteantall og hash i stedet. Kildene ble hentet via GitHub CLI; ingen upstream-skript ble kjørt.

Kontrollen gjelder katalogens fullstendighet, struktur og bevarte kildebytes. Ingen ny installasjon, runtime-test eller ytelsesmåling av de 46 prosjektene inngår. Tidligere dokumenterte tester gjelder sine opprinnelige revisjoner og miljøer. Eksterne nettadresser og API-innhold kan endres etter innhentingen.

---
id: nettside-med-github-api-i-sandkassen
tittel: Teste en Pages-nettside som henter filer fra GitHub-API-et, fra Claude-sandkassen
domene: testing
stikkord: Playwright, Chromium, SwiftShader, GitHub Pages, api.github.com, git blobs, lesenøkkel, proxy, CA, CORS, route, ScummVM, Emscripten, sandkasse
stack: Playwright for Python med headless Chromium 141, en side på github.io som henter spillfiler med fetch fra api.github.com (git/trees og git/blobs) med en lesenøkkel
status: PASS
opphav: Tombonator3000/ZakMcKracken-HD@7147a72e2522124c3c5a5874c5e0ce65dcb28db3:tools/nettsidetest.py#L51
dato: 2026-10-14
agent: Claude
lisens: Ingen lisensfil i repoet
offentlig_kontrollert: 2026-10-14
se_ogsa: playwright-swiftshader-three-lokalt, pages-deler-localstorage
sist_sjekket: 2026-10-14
---

# Teste en Pages-nettside som henter filer fra GitHub-API-et, fra Claude-sandkassen

## Symptom

Nettsiden (for eksempel ScummVM-sidene til The Dig HD og Zak McKracken HD) virker i Toms nettleser, men kan ikke prøves fra skyøkta: Chromium får sertifikatfeil eller «net::ERR_TUNNEL_CONNECTION_FAILED» mot github.io og api.github.com, og det finnes ingen ekte lesenøkkel i økta. Det er heller ikke lov å slå av sertifikatsjekken.

## Årsak

All trafikk ut fra sandkassen går gjennom en proxy med egen CA. Python (requests) og curl er satt opp for den, men nettleseren til Playwright er ikke. Proxyen legger selv på tilgangen mot api.github.com, så en hvilken som helst nøkkel virker der.

## Løsning

- Rut forespørslene til github.io og api.github.com i Playwright, og hent dem med requests (som bruker proxyen og CA-en). Gi svarene fra API-et `access-control-allow-origin: *`, og svar selv på OPTIONS.
- Gi siden en dummy-nøkkel. Ta den fra en miljøvariabel, så samme skript virker med en ekte nøkkel andre steder.
- Start Chromium med `--use-angle=swiftshader --enable-unsafe-swiftshader`.
- Vent på en tilstand i bildet, ikke på tid: for et SCUMM-spill er setningslinjen og inventaret svarte under mellomsekvensene, så klikk først når den delen av lerretet har tekst.

```python
session = requests.Session(); session.verify = '/root/.ccr/ca-bundle.crt'
CORS = {'access-control-allow-origin': '*'}

def github(route, request):
    if request.method == 'OPTIONS':
        route.fulfill(status=204, headers={**CORS, 'access-control-allow-headers': 'authorization, accept'})
        return
    headers = {k: v for k, v in request.headers.items() if k.lower() in ('authorization', 'accept')}
    r = session.get(request.url, headers=headers, timeout=300)
    route.fulfill(status=r.status_code, body=r.content,
                  headers={**CORS, 'content-type': r.headers.get('content-type', 'application/octet-stream')})

page.route('https://api.github.com/**', github)
page.route('https://tombonator3000.github.io/**', pages)   # samme, uten CORS-hodene
page.fill('#token', os.environ.get('NOKKEL', 'dummy-nokkel'))
```

## Fallgruver

- Behold `content-type` fra github.io, ellers kompileres ikke `scummvm.wasm` som strøm.
- Logg hver URL siden ber om. Da ser du at spillfilene bare kom fra api.github.com og aldri fra nettsiden.
- SwiftShader er tregt: introen i Zak tok 120 til 175 sekunder før spillet var i gang. Som Pixel 7 med stående skjerm (stort lerret) kom testen ikke så langt på to kjerner. Mobilen må prøves på en ekte telefon.
- Klikk mens en mellomsekvens går, gjør ingenting synlig og kan se ut som en feil i musekoordinatene.
- Nøkkelen er ekte for proxyen, ikke for GitHub: et kall som virker i sandkassen, beviser ikke at en finkornet nøkkel med Contents, Read-only er nok.

## Slik verifiseres det

`python3 tools/nettsidetest.py https://tombonator3000.github.io/ZakMcKracken-HD/ work/nettsidetest --sekunder 150 --klikktid 100 --etter 10 --klikk 62.5,55 --klikk h68,31` gir skjermbilder der figuren har gått til gulvpunktet og verbhjulet står åpent over telefonsvareren, og `rapport.json` uten feil i `errors`.

## Bevis

- [Loggen i ZakMcKracken-HD 14. oktober 15:27 til 16:20](https://github.com/Tombonator3000/ZakMcKracken-HD/blob/7147a72e2522124c3c5a5874c5e0ce65dcb28db3/log.md?plain=1#L157): intro med CD-musikk, gå, «Walk to Sushi in fish bowl» og verbhjulet i Chromium mot den publiserte siden.
- [docs/PAGES.md, Verifisering](https://github.com/Tombonator3000/ZakMcKracken-HD/blob/7147a72e2522124c3c5a5874c5e0ce65dcb28db3/docs/PAGES.md?plain=1#L114).

## Brukt i

- `Tombonator3000/ZakMcKracken-HD@7147a72`: testen av nettsiden 14. oktober 2026, før og etter første publisering.

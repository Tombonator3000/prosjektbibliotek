---
id: vite-oppstartspakke-lat-innlasting
tittel: Krymp oppstartspakken i Vite ved å laste sjeldne ruter, biblioteker og språk ved behov
domene: bygg
stikkord: vite, rollup, chunk, bundle, oppstartspakke, lastetid, lazy, React.lazy, dynamic import, three.js, peerjs, webrtc-adapter, i18n, språk, prefetch, requestIdleCallback, chunk larger than 500 kB
stack: Vite 5, React 18, Rollup, three.js 0.180, PeerJS 1.5, GitHub Pages
status: PASS
opphav: Tombonator3000/guild-life-adventures@52deb0fb037af5d7941a37feaaef925793505b3f:src/App.tsx#L15
dato: 2026-10-14
agent: Claude
lisens: Ingen lisensfil i repoet
sist_sjekket: 2026-10-14
---

# Krymp oppstartspakken i Vite ved å laste sjeldne ruter, biblioteker og språk ved behov

## Symptom

Tittelskjermen bruker lang tid før den vises, særlig på nettbrett og mobilnett. `vite build` viser én pakke på over en megabyte som lastes ved oppstart (`App-*.js 1,688 kB`), og varselet "Some chunks are larger than 500 kB after minification". Byggloggen skriver store tall med komma (`1,688.44 kB`), så et `sort -n` på loggen gjemmer den største pakka nederst.

## Årsak

Én statisk import av en sjelden side drar hele avhengighetstreet inn i oppstartspakken. I Guild Life importerte `App.tsx` 3D-laben `Board3D` direkte, så hele three.js (705 kB) kom med, selv om tittelkompasset og været allerede hentet three.js med `import()`. Det samme gjaldt PeerJS med webrtc-adapter (bare brukt i nettspill) og alle språkfilene (de fleste spiller på engelsk).

## Løsning

1. Finn synderne med en liten Rollup-plugin i en lokal byggkonfigurasjon som skriver størrelse per modul i hver pakke (`generateBundle`, `chunk.modules[id].renderedLength`). Grupper etter `node_modules/<pakke>` og mappe.
2. Gjør sjeldne ruter lat. Bruk en `lazy`-innpakning som prøver på nytt og laster siden på nytt ved utdaterte pakker etter en ny publisering.

```tsx
// App.tsx: three.js følger bare med 3D-laben
const Board3D = lazyWithRetry(() => import("./pages/Board3D"));
<Route path="/board-3d" element={<Suspense fallback={<ScreenLoader />}><Board3D /></Suspense>} />
```

3. Last tunge biblioteker ved første bruk, bak én felles laster, og importer bare typen statisk:

```ts
import type Peer from 'peerjs';
let pending: Promise<typeof Peer> | null = null;
export function loadPeerJs() {
  pending ??= import('peerjs').then(m => m.default).catch(e => { pending = null; throw e; });
  return pending;
}
// I createRoom: sett status først, vent så på modulen, lag deretter Peer.
```

4. Bundle bare reservespråket. Andre språk får lastere. En revisjonsteller i abonnementet gjør at React tegner på nytt når tekstene kommer. Vent på lagret språk før første tegning:

```ts
const [{ default: App }, { whenLanguageReady }] = await Promise.all([import("./App.tsx"), import("./i18n")]);
await whenLanguageReady();
```

5. Forhåndslast neste skjerm i ledig tid (`requestIdleCallback`): oppsett fra tittel, brett fra oppsett. Hopp over når `navigator.connection.saveData` er satt, og under animasjoner som en oppstartslogo.

## Fallgruver

- `useSyncExternalStore` med språkkoden som øyeblikksbilde tegner ikke på nytt når tekstene lastes og koden er uendret. Bruk en teller som øker både ved bytte og ved fullført lasting.
- Tester som forventer at et objekt finnes rett etter et kall (for eksempel `peers[0]` etter `createRoom()`) må vente: `await vi.waitFor(() => expect(peers[0]).toBeDefined())`.
- Ikke sett status to ganger. Sett "connecting" før `await`, og fjern det fra inni løftet, ellers får lyttere to like hendelser.
- Mål med kald nettleser per runde. Samme Chromium-prosess deler kompilert kode mellom kontekster, og da ser andre runde mye raskere ut enn den er.
- Google Fonts som feiler i sandkassen gir stor spredning i tidene. Blokker eksterne skrifter i målingen.
- Ubrukt kode kan være montert uten å brukes. Her lå et helt Radix-toastsystem i appen, mens alle 33 kallene brukte Sonner.

## Slik verifiseres det

Bygg og les pakkene, og mål med Playwright: ny nettleser per runde, `Emulation.setCPUThrottlingRate` 4, eksterne skrifter blokkert, en liten statisk server med gzip som GitHub Pages, og `Network.emulateNetworkConditions` med 10 Mbit/s og 150 ms forsinkelse. Mål `performance.now()` når første knapp på tittelskjermen finnes. Median av sju runder. Kjør hele testsuiten etterpå, og sjekk språkbytte, nettspill og den late ruten i nettleseren.

## Bevis

- [Loggen i guild-life-adventures med måletallene](https://github.com/Tombonator3000/guild-life-adventures/blob/52deb0fb037af5d7941a37feaaef925793505b3f/log.md?plain=1#L14578): JavaScript før tittelskjermen fra 1792 kB til 817 kB, tittel fra 1924 ms til 1142 ms, brett etter "Begin Adventure" fra 913 ms til 416 ms.
- [PR #434](https://github.com/Tombonator3000/guild-life-adventures/pull/434), slått sammen som 52deb0f etter grønn validering med alle Playwright-testene.

## Brukt i

- `Tombonator3000/guild-life-adventures@52deb0f`: oppstartspakken `App` fra 1688 kB til 650 kB (494 til 205 kB gzip), tittelskjermen 41 prosent raskere og brettet 54 prosent raskere på emulert mobilnett med treg prosessor.

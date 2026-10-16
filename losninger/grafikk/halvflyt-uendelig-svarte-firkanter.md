---
id: halvflyt-uendelig-svarte-firkanter
tittel: Svarte firkanter i bloom fra høylys som ikke får plass i halvflyt
domene: grafikk
stikkord: svart firkant, svarte firkanter, black square, NaN, Inf, uendelig, HalfFloatType, halvflyt, 65504, bloom, UnrealBloomPass, GTAO, ACES, tonemapping, RTX
stack: three.js r170, WebGL2, EffectComposer med HalfFloatType-mål, GTAOPass, UnrealBloomPass, ACES
status: PASS
opphav: Tombonator3000/SIGNAL-47@58aef5011cd5021645ee4be713a30bf06d9f8261:web/src/core/vhs.ts#L38
dato: 2026-10-16
agent: Claude
lisens: Toms egen kode, ingen lisensfil i repoet
sist_sjekket: 2026-10-16
se_ogsa: bloom-terskel-over-en, three-r170-composer-msaa
---

# Svarte firkanter i bloom fra høylys som ikke får plass i halvflyt

## Symptom

En svart firkant dukker opp på skjermen og forsvinner igjen, eller store deler av bildet blir svart et øyeblikk. Det skjer på et ekte skjermkort (meldt på RTX 3080) når man ser på noe blankt nær et sterkt lys, for eksempel en lommelykt mot krom eller glass. I programvare-rendereren er det sjelden, fordi høylysene sjelden blir store nok der.

## Årsak

Scenen tegnes i et `HalfFloatType`-mål, og den største verdien et slikt mål kan holde er 65504. Et spekulært høylys fra et sterkt punkt- eller spotlys helt nær en blank flate (lav ruhet) kan gå over grensen, og verdien blir uendelig når den skrives. Videre i kjeden blir uendelig til NaN: ACES-tonekurven deler uendelig på uendelig, og GTAO ganger uendelig med en okklusjon nær 0. Bloom gjør resten. Passet blurer og skalerer ned i flere nivåer, og én NaN-piksel smitter hele området rundt seg. På de groveste nivåene dekker én teksel 32 x 32 piksler, og da blir det firkanter, eller hele skjermen.

## Løsning

Hold bildet endelig og klem det før bloom og før tonekurven:

1. Et eget pass etter GTAO og før bloom som klemmer fargen mellom 0 og et tak og gjør NaN til 0.
2. Det samme der et senere pass leser scenen direkte og tonekarter selv.

```glsl
vec3 finite(vec3 c) {
  c = min(max(c, vec3(0.0)), vec3(10.0));   // max og min gir det andre tallet for NaN
  return any(isnan(c)) ? vec3(0.0) : c;     // isnan fanger resten
}
```

```js
const finitePass = () => new ShaderPass({
  uniforms: { tDiffuse: { value: null } },
  vertexShader: VERT,
  fragmentShader: `uniform sampler2D tDiffuse; varying vec2 vUv; ${FINITE}
    void main() { vec4 c = texture2D(tDiffuse, vUv); gl_FragColor = vec4(finite(c.rgb), clamp(c.a, 0.0, 1.0)); }`,
});
composer.addPass(renderPass); composer.addPass(gtao); composer.addPass(finitePass()); composer.addPass(bloom);
```

Taket kan være lavt. Med ACES blir alt over rundt 8 hvitt uansett, og et tak på 10 hindrer også at en flate helt nær et lys blåser ut hele bildet gjennom bloom. Mål først hvor lyse vanlige scener er (her 2 til 12).

Ta også bort det som lager de ekstreme verdiene: et lys som følger kameraet (lommelykt) bør ikke ha fysisk avtagning (decay 1,5 til 2), for da blir det hundrevis av ganger sterkere en håndsbredd unna. Lineær avtagning (decay 1) med lavere styrke ga omtrent samme lys ved 4 m og var mye mildere nært.

## Fallgruver

- `isnan()` kan bli optimalisert bort av noen drivere. Derfor `max` og `min` først: på D3D (ANGLE i Chrome på Windows) og hos NVIDIA gir de det tallet som ikke er NaN.
- Passet må ligge før bloom. Etter bloom er skaden allerede spredd.
- En NaN-piksel blir fortsatt én svart piksel, men den smitter ikke lenger.
- Taket gjør bloom svakere rundt de aller lyseste punktene. Mål vanlige scener først, så det ikke endrer bildet ellers.

## Slik verifiseres det

Legg inn en liten kule med `MeshBasicMaterial` og farge `setScalar(1e6)` midt i bildet (den blir uendelig i halvflyt). Uten passet ble nesten hele bildet svart på PC-nivået med GTAO og bloom i SIGNAL-47; med passet er kula en hvit prikk med glød. En testkrok som tegner scenen i et `FloatType`-mål og teller verdier over 65504 (`S47.hdrStats()` i SIGNAL-47) viser hvor nær grensen vanlige scener er.

## Bevis

- [SIGNAL-47 log.md, 16. oktober 06:46 til 07:09](https://github.com/Tombonator3000/SIGNAL-47/blob/dd5d1f4d9b455061b7718f0d44b0c1d0ff5f6876/web/log.md?plain=1#L648): sonden med kula, nesten hele Ultra-bildet svart før, hvit prikk med glød etter. Sjekket i programvare-rendereren (SwiftShader); på det ekte skjermkortet der feilen ble meldt er resultatet UNVERIFIED til det er prøvd.
- [SIGNAL-47 memory.md, kjente fallgruver](https://github.com/Tombonator3000/SIGNAL-47/blob/dd5d1f4d9b455061b7718f0d44b0c1d0ff5f6876/web/memory.md?plain=1#L159).

## Brukt i

- `Tombonator3000/SIGNAL-47@58aef50`: PC-nivået (GTAO, bloom, VHS-pass) og VHS-passet på High.

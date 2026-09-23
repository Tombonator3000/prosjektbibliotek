# Historisk dokumentutdrag

Kilde: `/home/tombonator3000t/Documents/Codex/the-deep-ones-3d/docs/unity/LIVING_COAST.md`

Originale linjer 23–29; bevart 23. september 2026. Opplysningene nedenfor er historiske kildenotater, ikke en ny verifikasjon.

---

## Aquarium-inspired behaviour

`SchoolSimulation` maintains 60 real individuals at a fixed 30 Hz, with interpolated rendering. A spatial grid supplies neighbours. Separation, alignment and cohesion combine with inertia, limited turning, acceleration, drag, burst/coast effort and boundaries. Saithe form stronger schools; cod and pollack move more loosely. Registered rock volumes and seabed shelves constrain motion and block bait visibility. Cheap bounds rejection avoids unnecessary narrow collision queries. Offscreen fish continue to simulate, while hidden model/animation updates are culled. Ordinary schooling includes small individual variations instead of a perfectly synchronized route.

One shared `CoastalFlow` field influences fish, hook drift, kelp lean and marine particles. The line constrains the hook's movement; this is a shared current and animal simulation, not a computational fluid solver. It is a new Unity implementation informed by the inspected [Desktop Habitats revision](https://github.com/chaseleantj/desktop-habitats/tree/e6ea239e92bb04dcd3953f80758aef61c72b2146), especially `scenes/riverscape/src/fish.js`, `water.js`, `food.js` and the behaviour tests. No aquarium source code was copied.

Nearby eligible fish compete for interest in the real bait. One individual reserves it. Nibbles require sustained mouth contact; a remote or unreserved fish cannot be hooked. The reserved individual, species, fight and landed catch remain connected. An early strike startles neighbours; missed bites produce a cooldown. Keeping a catch removes that individual, releasing it frees the same fish, and replenishment waits until the boat leaves that home area. Rare pale cod remain confined to the deep pocket. Junk, valuables and the compass remain separate bottom snags.

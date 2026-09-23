# Historisk dokumentutdrag

Kilde: `/home/tombonator3000t/Documents/Codex/VOIDCRAFT/docs/developer/VOIDCRAFT_FOUNDATION.md`

Originale linjer 1–18; bevart 23. september 2026. Opplysningene nedenfor er historiske kildenotater, ikke en ny verifikasjon.

---

# Voidcraft foundation

Status: first vertical-slice foundation implemented on 2026-08-07. Live Done/Open status remains in
[../../TODO.md](../../TODO.md).

## Pitch

**Voidcraft is a block-built space survival game about crossing procedural worlds and discovering that the
worlds were built as locks.** Players mine, craft, build and fly through the existing sandbox while a slow
cosmic-horror campaign turns familiar planets into evidence of something older than their stars.

The project is built on the AGPL-licensed
[Blocks Beyond the Stars](https://github.com/marceld23/BlocksBeyondTheStars) codebase. Its authoritative .NET
server, Unity voxel client, procedural galaxy, ship flight, crafting, persistence and multiplayer remain the
technical foundation. `BlocksBeyondTheStars` stays as the internal namespace and data-folder codename for now;
changing it would create a large compatibility migration without improving the first playable experience.

## Player promise

# Handoff to Claude

Write `CLAUDE_ANIMASJON.md` beside the output PNGs and JSON. The note should be tailored to the delivered art, not generic. Include:

1. Character, clip names, `f/b/s` directions, fps, looping and pivot; reference `spritepack.json` as the exact source of frame order and rectangles. State whether left can mirror `s` safely.
2. Art status: approved/experimental, manual QA observations, known missing views, and whether the artwork already lives in the game project. Include the `kontaktark.png` path.
3. The concrete integration request: identify a new atlas player for full-body character frames, or `Doll`/`POSER` changes for paper dolls, or `Anim`/manifest registration for effects. Never suggest `anim_<navn>.png` will animate a whole character in the current code.
4. For a full character player, retain the current Three.js world position, camera-facing plane, ground pivot, `BILL_Y` compensation, lighting, depth order, shadow, hit flash, tint, outline and dissolve. Reuse atlas textures and dispose temporary resources. Frame UV sampling and outline taps must stay inside the active cell to prevent bleeding from adjacent poses. Map facing to front/back/right and mirror right for left where allowed. Choose state changes and attack/hurt/death behavior from gameplay, not just a timer.
5. Verification: test at least idle, walk, attack or relevant special state, direction changes, loop seam, camera yaw, WebGL/mobile texture budget and postprocessing. Mark missing integration steps openly.

Example request to put in the note, adjusted to the actual files:

> Integrer `spritepack.json` og atlas-PNGene for pasienten. Bruk frame-rektanglene og festepunktet som oppgitt, spill av `walk` ved bevegelse og `idle` ellers, og bevar 3D-lys, skygge og postprosessering. Legg til en spiller for figurark; eksisterende `Anim` er laget for effekter. Test fra front, bak og begge sider.

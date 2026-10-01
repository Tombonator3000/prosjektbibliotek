---
name: morbidium-spritesheets
description: Create consistent animated 2D character sprite sheets, paper-doll art, and effect sheets for the Morbidium Three.js game, with frame validation, atlases, metadata, visual QA, and a handoff Claude can integrate. Use for requests to animate a Morbidium character, make a spritesheet/spriteark, add directional walk/attack/death frames, or prepare game-ready figure art for Claude.
---

# Morbidium spritesheets

Produce **assets and an implementation contract**, not a prompt alone. A ChatGPT skill cannot run inside Claude; give Claude the exported PNGs, `spritepack.json`, and an explicit integration note.

## Start from the current game

1. Read the current project's `AGENTS.md`, `DESIGN_BRIEF.md`, `assets/manifest.json`, and relevant code before deciding filenames or animation architecture. See [references/morbidium.md](references/morbidium.md) for the known layout; the project can change.
2. Choose one of two paths per character:
   - **Paper doll** for ordinary interchangeable humanoids: author the six separate head/body views with `maler/mal_figur.png` and `figur_<navn>.png`. Existing `Doll` moves limbs and handles walk, hit, poses, equipment, lighting, shadow and facing in code. Specify extra motion as `POSER` or rig changes for Claude. Do not promise a new frame atlas if none was made.
   - **Full frame animation** for a character or special action needing drawn silhouette changes: make individual frames, pack them with `scripts/pack_frames.py`, and ask Claude to add a dedicated atlas player. The current `anim_<navn>.png` path belongs to effects and is not a character animation loader.
3. For an effect, use `kind: "effect"` in the packer and follow the existing `anim_<navn>` manifest/runtime contract. Do not overwrite an existing manifest key without reviewing the game definition.

## Author frames

- Lock a canonical design: front `f`, back `b`, right-facing side `s`; mirror side for left only if asymmetry, weapon hand, and text still make sense. Use the existing figure as visual reference, including line weight, colors, scale and distinctive features.
- Choose the smallest useful set of clips. Typical baseline: `idle`, `walk`, `attack`, `hurt`, `death`; timing and frames depend on gameplay. For looping motion, draw the cycle so the last frame leads smoothly to the first. State whether death holds or ends.
- Create or edit bitmap art with the image-generation tool when new painted frames are needed. Feed the same canonical reference into each edit. Avoid independently generating a whole sequence with drifting costume or anatomy. Use transparent PNGs; no painted ground shadow or scene background because the game supplies shadows, lighting and postprocessing.
- Place each approved frame on an identical transparent canvas at native resolution. Keep character scale, feet/pivot, head size, outline, eye count, costume, weapon, handedness, and visibility consistent. Do not rescale each frame independently to fill its bounds. Treat the front/back/side turnaround and individual pose frames as editable sources; inspect them at game size as well as full size.
- For compound figures, keep equipment and body parts in sensible depth order. Check weapon arcs and frame-to-frame silhouette. If a frame fails, regenerate or fix it before packing. Automated checks cannot judge identity or animation quality.

## Pack and review

1. Build a JSON spec following [references/frame-spec.md](references/frame-spec.md). Frame paths are ordered explicitly. Set one fixed `cell` and top-left `pivot` for every clip. For characters supply all three views per state unless the package deliberately opts into partial views.
2. Run `python3 scripts/pack_frames.py --spec <pack.json> --out <delivery>` (Pillow required). The script rejects wrong size, missing alpha, blank frames, invalid directions, overlarge strips and excessive estimated RGBA texture memory. Review warnings in `qa.json`; rerun with `--strict` after fixing them.
3. Open `kontaktark.png` and every atlas. Look for drifting face/outfit, clipped motion, jittering feet, transparent halos, gaps between directions, and bad walk-loop closure. Test playback in the game if integrating it now. Do not label a visually unreviewed pack production ready.
4. Follow [references/claude-handoff.md](references/claude-handoff.md) to create a concise handoff next to the package. State exactly which files Claude should use, what still needs implementation, and which game paths to inspect. If asked to implement as well, make the runtime change and verify an animated figure in the Three.js scene.

For sizable deliveries, use a persistent user-facing file location. If files are placed in the user's existing Git project, keep that project's history as the sole code copy. Return the package path and a short status of artwork and integration.

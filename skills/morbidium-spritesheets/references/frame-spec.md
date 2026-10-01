# Frame pack specification

`scripts/pack_frames.py` takes an explicit list of approved RGBA PNG frames. It does not invent intermediate poses or resize frames. All paths are relative to the JSON spec file and remain inside that directory.

Example character spec:

```json
{
  "kind": "character",
  "character": "pasient",
  "cell": [384, 512],
  "pivot": [192, 496],
  "clips": [
    {"name": "idle", "view": "f", "fps": 6, "loop": true,
     "frames": ["frames/idle/f/000.png", "frames/idle/f/001.png"]},
    {"name": "idle", "view": "b", "fps": 6, "loop": true,
     "frames": ["frames/idle/b/000.png", "frames/idle/b/001.png"]},
    {"name": "idle", "view": "s", "fps": 6, "loop": true,
     "frames": ["frames/idle/s/000.png", "frames/idle/s/001.png"]}
  ]
}
```

Repeat the view triplet for further states. To knowingly deliver a partial set, set `"allow_partial_views": true` and explain fallback behavior to Claude. Left-facing is a mirror of `s`; do not render a fourth view unless the current runtime is deliberately extended for it. The side reference faces right.

The packer outputs `figur_<character>_<state>_<view>.png`, a one-row equal-cell atlas per clip, plus `spritepack.json`, `qa.json` and `kontaktark.png`. `spritepack.json` lists frame rectangles in **top-left pixel coordinates**. Pivot coordinates are in a **single cell**, also from top left. The output is a delivery contract, not an entry recognized by today's `assets/manifest.json`.

Example effect spec:

```json
{
  "kind": "effect",
  "character": "ny_sprut",
  "cell": [256, 256],
  "pivot": [128, 230],
  "game_units": {"w": 1.5, "h": 1.5, "ax": 0.75, "ay": 0.12},
  "clips": [{"name": "burst", "fps": 12, "loop": false,
             "frames": ["frames/000.png", "frames/001.png"]}]
}
```

The effect output is `anim_ny_sprut.png` and metadata contains a suggested `morbidium_manifest_entry`. Claude must reconcile it with `ANIM` in `src/16_anim.js` and the current manifest. Do not copy metadata blindly if the key already exists or the game definition differs.

Defaults are 4096 pixels maximum texture dimension and 64 MiB estimated RGBA atlas memory; override with `--max-texture` and `--budget-mib` after testing target devices. PNG file size is not GPU texture size. Use `--strict` to reject QA warnings such as duplicate frames or artwork touching a cell edge. Review the contact sheet manually for character and motion consistency; machine validation cannot verify it.

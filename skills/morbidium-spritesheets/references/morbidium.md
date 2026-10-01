# Current Morbidium conventions to verify against the live project

Observed in Morbidium in September 2026. Inspect the current checkout before relying on these details.

| Area | Current contract |
| --- | --- |
| `maler/mal_figur.png` | Three columns: front, back, right side. Top row head, bottom row body without limbs. |
| `gpt-grafikk/figur_<navn>.png` | Input sheet; `tools/skjaer_ark.py` extracts `hode_<navn>_f/b/s` and `kropp_<navn>_f/b/s`. |
| `gpt-grafikk/<manifest-key>.png` | Input for `tools/behandle_bilder.py`; unknown keys are rejected. Then `build.py` embeds game assets. |
| `src/11_doll.js` | `Doll` assembles art plates and code-drawn arms/legs/shoes; `setFacing` uses `f`, `b`, `s` and mirrors side for left. `update` animates bob, gait, attacks and poses. Camera-relative facing and `BILL_Y` matter. |
| `src/16_anim.js` | `Anim` plays effect sheets; `POSER` supplies named keyframes to `Doll.update`. `anim_<navn>` is registered through manifest/`ANIM_ARK`. |
| `assets/manifest.json` | Effect entry supplies `ruter`, `n`, `fps`, `w`, `h`, `ax`, `ay`. Figure parts have different entries. |

The code already has shader outline, hit flash, dye, rim lighting and dissolve. In 3D, a paper doll is a camera-oriented flat surface. New frame atlases should preserve those effects and pass through the existing postprocessing scene. Keep uncompressed texture memory modest, especially on mobile. Sharing an atlas texture is generally cheaper than making one `CanvasTexture` per character frame.

The older design brief advised against frame-by-frame walking characters because generated frames were inconsistent. A user request for them authorizes trying the new workflow, but that consistency problem remains a QA requirement. Avoid dropping a figure atlas into the effect input folder and claiming it will work without a character player.

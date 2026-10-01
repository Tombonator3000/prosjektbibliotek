#!/usr/bin/env python3
"""Pack individually approved transparent animation frames into one-row atlases.

Requires Pillow. Run with --spec path/to/pack.json --out path/to/delivery.
The input JSON schema is documented in ../references/frame-spec.md.
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


NAME = re.compile(r"^[a-z][a-z0-9_]*$")
VIEWS = {"f", "b", "s"}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def integer_pair(value, label):
    require(isinstance(value, list) and len(value) == 2 and
            all(type(v) is int for v in value), f"{label} must be [int, int]")
    return tuple(value)


def input_path(root, name):
    require(isinstance(name, str), "frame path must be a string")
    rel = Path(name)
    require(not rel.is_absolute() and ".." not in rel.parts and rel.suffix.lower() == ".png",
            f"unsafe or non-PNG frame path: {name}")
    path = root / rel
    require(path.is_file(), f"missing frame: {path}")
    return path


def checker(size, step=12):
    image = Image.new("RGBA", size, "#b8b8b8")
    draw = ImageDraw.Draw(image)
    for y in range(0, size[1], step):
        for x in range(0, size[0], step):
            if (x // step + y // step) % 2 == 0:
                draw.rectangle((x, y, x + step - 1, y + step - 1), fill="#e8e8e8")
    return image


def contact_sheet(clips, cell):
    # Preview every frame in source order; this is for human inspection, not game use.
    thumb_w, thumb_h = min(cell[0], 160), min(cell[1], 200)
    scale = min(thumb_w / cell[0], thumb_h / cell[1])
    shown_w, shown_h = max(1, round(cell[0] * scale)), max(1, round(cell[1] * scale))
    columns = min(8, max(len(c["images"]) for c in clips))
    row_h = shown_h + 32
    total_rows = sum((len(c["images"]) + columns - 1) // columns for c in clips)
    result = Image.new("RGB", (columns * (shown_w + 8) + 8, total_rows * row_h + 8), "#302923")
    draw = ImageDraw.Draw(result)
    row = 0
    for clip in clips:
        label = clip["name"] + ("/" + clip["view"] if clip["view"] else "")
        for i, frame in enumerate(clip["images"]):
            col, offset = i % columns, i // columns
            x, y = 8 + col * (shown_w + 8), 8 + (row + offset) * row_h
            patch = checker((shown_w, shown_h))
            patch.alpha_composite(frame.resize((shown_w, shown_h), Image.Resampling.LANCZOS))
            result.paste(patch.convert("RGB"), (x, y))
            draw.text((x, y + shown_h + 3), f"{label} {i:02d}", fill="white", font=ImageFont.load_default())
        row += (len(clip["images"]) + columns - 1) // columns
    return result


def save_png_checked(image, path):
    """Never leave a successful-looking delivery with a truncated atlas."""
    temporary = path.with_name(path.name + ".part")
    try:
        image.save(temporary, format="PNG", optimize=True)
        with Image.open(temporary) as written:
            written.verify()
        require(temporary.stat().st_size > 0, f"empty PNG output: {temporary}")
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def pack(spec_path, out, max_texture, budget_mib, strict):
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    require(isinstance(spec, dict), "spec must be a JSON object")
    character = spec.get("character")
    require(isinstance(character, str) and NAME.fullmatch(character),
            "character must use lowercase letters, digits, underscores")
    kind = spec.get("kind", "character")
    require(kind in ("character", "effect"), "kind must be character or effect")
    cell = integer_pair(spec.get("cell"), "cell")
    require(16 <= min(cell) and max(cell) <= max_texture, "invalid cell dimensions")
    pivot = integer_pair(spec.get("pivot"), "pivot")
    require(0 <= pivot[0] < cell[0] and 0 <= pivot[1] < cell[1],
            "pivot must be inside every frame, measured from top left")
    clips_in = spec.get("clips")
    require(isinstance(clips_in, list) and clips_in, "clips must be a nonempty array")
    require(kind != "effect" or len(clips_in) == 1, "legacy effect format has one clip")
    if kind == "effect":
        units = spec.get("game_units")
        require(isinstance(units, dict) and all(k in units for k in ("w", "h", "ax", "ay")),
                "effect requires game_units: w, h, ax, ay")
        require(all(type(units[k]) in (int, float) for k in ("w", "h", "ax", "ay")),
                "game_units values must be numbers")
        require(units["w"] > 0 and units["h"] > 0 and
                0 <= units["ax"] <= units["w"] and 0 <= units["ay"] <= units["h"],
                "invalid game_units pivot or size")
    root = spec_path.parent
    seen = set()
    clips = []
    warnings = []
    views_by_name = {}
    estimated_bytes = 0
    for definition in clips_in:
        require(isinstance(definition, dict), "each clip must be an object")
        name, view = definition.get("name"), definition.get("view")
        require(isinstance(name, str) and NAME.fullmatch(name), "invalid clip name")
        require((kind == "effect" and view is None) or
                (kind == "character" and view in VIEWS),
                "character clips require view f/b/s; effects omit view")
        key = (name, view)
        require(key not in seen, f"duplicate clip {key}")
        seen.add(key)
        if view:
            views_by_name.setdefault(name, set()).add(view)
        fps, loop = definition.get("fps"), definition.get("loop")
        require(type(fps) in (int, float) and 0 < fps <= 60, f"invalid fps for {key}")
        require(type(loop) is bool, f"loop must be boolean for {key}")
        frames = definition.get("frames")
        require(isinstance(frames, list) and frames and all(isinstance(f, str) for f in frames),
                f"{key} needs an ordered frame list")
        require(cell[0] * len(frames) <= max_texture,
                f"{key} is wider than {max_texture}px; use fewer/smaller frames")
        images = []
        hashes = set()
        for i, frame_name in enumerate(frames):
            path = input_path(root, frame_name)
            with Image.open(path) as source:
                require("A" in source.getbands(), f"{path} needs a real alpha channel")
                require(source.size == cell,
                        f"{path} is {source.size}; expected cell {cell} (never scale frames silently)")
                im = source.convert("RGBA")
            alpha = im.getchannel("A")
            require(alpha.getextrema()[1] > 16, f"empty frame: {path}")
            require(alpha.getextrema()[0] == 0, f"opaque background: {path}")
            bbox = alpha.point(lambda a: 255 if a > 16 else 0).getbbox()
            require(bbox is not None, f"empty frame: {path}")
            if bbox[0] == 0 or bbox[1] == 0 or bbox[2] == cell[0] or bbox[3] == cell[1]:
                warnings.append(f"{key} frame {i}: art touches a cell edge; check clipping")
            digest = hashlib.sha256(im.tobytes()).digest()
            if digest in hashes:
                warnings.append(f"{key} frame {i}: exact duplicate of an earlier frame")
            hashes.add(digest)
            images.append(im)
        atlas_name = (f"figur_{character}_{name}_{view}.png" if kind == "character"
                      else f"anim_{character}.png")
        clips.append({"name": name, "view": view, "fps": fps, "loop": loop,
                      "images": images, "atlas": atlas_name,
                      "frames": frames})
        estimated_bytes += cell[0] * len(images) * cell[1] * 4
    if kind == "character":
        for name, views in views_by_name.items():
            missing = VIEWS - views
            require(not missing or spec.get("allow_partial_views") is True,
                    f"{name} lacks views {','.join(sorted(missing))}; provide f/b/s or opt in to partial views")
            if missing:
                warnings.append(f"{name}: missing views {','.join(sorted(missing))}")
    mib = estimated_bytes / 1048576
    require(mib <= budget_mib,
            f"estimated RGBA atlas memory {mib:.1f} MiB exceeds {budget_mib:.1f} MiB budget")
    if strict and warnings:
        raise ValueError("QA warnings in strict mode:\n" + "\n".join(warnings))

    out.mkdir(parents=True, exist_ok=True)
    package = {"schema": "morbidium-spritepack-v1", "kind": kind,
               "character": character, "cell_px": list(cell), "pivot_px_top_left": list(pivot),
               "direction": {"f": "front", "b": "back", "s": "right", "left": "mirror s"}
               if kind == "character" else None,
               "estimated_rgba_mib": round(mib, 2), "clips": []}
    for clip in clips:
        frames = clip["images"]
        atlas = Image.new("RGBA", (cell[0] * len(frames), cell[1]), (0, 0, 0, 0))
        for i, frame in enumerate(frames):
            atlas.alpha_composite(frame, (i * cell[0], 0))
        save_png_checked(atlas, out / clip["atlas"])
        record = {"name": clip["name"], "view": clip["view"],
                  "atlas": clip["atlas"], "frames": len(frames),
                  "frame_rects_px_top_left": [[i * cell[0], 0, *cell] for i in range(len(frames))],
                  "fps": clip["fps"], "loop": clip["loop"]}
        package["clips"].append(record)
    if kind == "effect":
        clip = clips[0]
        package["morbidium_manifest_entry"] = {
            "key": f"anim_{character}", "ruter": [len(clip["images"]), 1],
            "n": len(clip["images"]), "fps": clip["fps"], **spec["game_units"]}
    (out / "spritepack.json").write_text(json.dumps(package, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "qa.json").write_text(json.dumps({"warnings": warnings, "input_frames": sum(len(c["images"]) for c in clips),
                                         "estimated_rgba_mib": round(mib, 2)}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    save_png_checked(contact_sheet(clips, cell), out / "kontaktark.png")
    print(f"Packed {len(clips)} clips, {sum(len(c['images']) for c in clips)} frames; {mib:.2f} MiB RGBA")
    print(f"QA: {len(warnings)} warnings; inspect {out / 'kontaktark.png'}")
    for warning in warnings:
        print("WARN:", warning)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--max-texture", type=int, default=4096)
    parser.add_argument("--budget-mib", type=float, default=64)
    parser.add_argument("--strict", action="store_true", help="fail on QA warnings")
    args = parser.parse_args()
    try:
        pack(args.spec.resolve(), args.out.resolve(), args.max_texture, args.budget_mib, args.strict)
    except (ValueError, OSError, json.JSONDecodeError) as error:
        parser.exit(2, f"ERROR: {error}\n")


if __name__ == "__main__":
    main()

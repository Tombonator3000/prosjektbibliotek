#!/usr/bin/env python3
"""Hent alle egne GitHub-stjerner og eksplisitte referanser. Krever Python 3 og gh."""
import argparse
import base64
import concurrent.futures
import datetime as dt
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]


def api(endpoint, accept="application/vnd.github+json"):
    result = subprocess.run(["gh", "api", "-H", f"Accept: {accept}", endpoint],
                            capture_output=True, text=True, timeout=90)
    if result.returncode:
        # No authentication headers, environment variables or credential values are logged.
        raise RuntimeError(f"GitHub-kall mislyktes: {endpoint}: {result.stderr.strip()[:300]}")
    return json.loads(result.stdout)


def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     prefix=".sync-", suffix=".tmp", delete=False) as stream:
        temporary = Path(stream.name)
        stream.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def historical_references():
    refs = {}
    def add(name, path):
        refs.setdefault(name, []).append(path)
    for item in json.loads((ROOT / "repoer/sentient-2026-09-12.json").read_text())["tools"]:
        # Retain the GitHub reference even when canonical development moved to Codeberg.
        name = item["primary_source_url"].removeprefix("https://github.com/").strip("/")
        add(name, "repoer/sentient-2026-09-12.md")
    for item in json.loads((ROOT / "repoer/coastal-webgpu-2026-09-20.json").read_text())["repositories"]:
        add(item["repository"], "repoer/coastal-webgpu-2026-09-20.md")
    extra = ROOT / "data/extra-references.json"
    if extra.exists():
        for item in json.loads(extra.read_text()):
            add(item["full_name"], item["source"])
    return refs


def fetch_repo(name, star, refs):
    requested_name = name
    meta = api(f"repos/{name}")
    name = meta["full_name"]
    branch = meta["default_branch"]
    commit = api(f"repos/{name}/commits/{quote(branch, safe='')}")["sha"]
    root = api(f"repos/{name}/contents?ref={commit}")
    entry = {key: meta.get(key) for key in (
        "id", "full_name", "html_url", "description", "homepage", "private", "fork",
        "archived", "disabled", "default_branch", "language", "topics", "stargazers_count",
        "created_at", "updated_at", "pushed_at")}
    entry.update({"commit": commit, "starred_at": star, "reference_sources": refs,
                  "aliases": [requested_name] if requested_name != name else [],
                  "parent": (meta.get("parent") or {}).get("full_name"),
                  "license": meta.get("license"), "files": [], "warnings": [],
                  "root_entries": [{"path": f["path"], "type": f["type"]} for f in root]})
    selected = {}
    try:
        readme = api(f"repos/{name}/readme?ref={commit}")
        selected[readme["path"]] = readme
    except RuntimeError as exc:
        if "HTTP 404" not in str(exc):
            raise
        entry["warnings"].append("GitHub fant ingen README for valgt revisjon.")
    for item in root:
        if item["type"] == "file" and re.search(r"(^|[._-])(licen[sc]e|copying|notice|credits)([._-]|$)", item["name"], re.I):
            selected[item["path"]] = item
    for path, item in sorted(selected.items()):
        if item.get("size", 0) > 1_000_000:
            entry["warnings"].append(f"Kildetekst over 1 MB ble ikke kopiert via Contents-API: {path}")
            continue
        if "content" not in item:
            item = api(f"repos/{name}/contents/{quote(path, safe='/')}?ref={commit}")
        if item.get("encoding") != "base64":
            raise RuntimeError(f"Uventet kildeformat for {name}/{path}")
        content = base64.b64decode(item["content"])
        content.decode("utf-8")
        local = Path("kilder/github") / name.replace("/", "--") / commit / (path + ".txt")
        (ROOT / local).parent.mkdir(parents=True, exist_ok=True)
        (ROOT / local).write_bytes(content)
        entry["files"].append({"path": path, "local_path": local.as_posix(), "bytes": len(content),
                               "sha256": hashlib.sha256(content).hexdigest(), "git_blob_sha": item["sha"],
                               "source_url": f"https://github.com/{name}/blob/{commit}/{quote(path, safe='/')}"})
    return entry


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--owner", default="Tombonator3000")
    args = parser.parse_args()
    owner = api("user")["login"]
    if owner.casefold() != args.owner.casefold():
        raise SystemExit(f"Feil aktiv GitHub-konto: {owner}; forventet {args.owner}.")
    started = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    stars, pages, page_sizes = [], 0, []
    while True:
        page = api(f"user/starred?per_page=100&page={pages + 1}&sort=created&direction=desc",
                   "application/vnd.github.star+json")
        pages += 1
        page_sizes.append(len(page))
        stars.extend(page)
        if len(page) < 100:
            break
    if len({x["repo"]["id"] for x in stars}) != len(stars):
        raise SystemExit("Duplikater i starlisten; prøv på nytt når listen er stabil.")
    refs = historical_references()
    star_map = {x["repo"]["full_name"]: x["starred_at"] for x in stars}
    previous_path = ROOT / "data/github.json"
    previous = json.loads(previous_path.read_text()) if previous_path.exists() else {"repositories": []}
    old_entries = {r["id"]: r for r in previous["repositories"]}
    # Keep saved references even if the user later removes a star.
    names = sorted(set(refs) | set(star_map) | {r["full_name"] for r in old_entries.values()}, key=str.casefold)
    entries, errors = [], []
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(fetch_repo, n, star_map.get(n), refs.get(n, [])): n for n in names}
        for future in concurrent.futures.as_completed(futures):
            name = futures[future]
            try:
                entry = future.result()
                old = old_entries.get(entry["id"], {})
                entry["previously_starred_at"] = old.get("previously_starred_at") or old.get("starred_at")
                entry["aliases"] = sorted(set(entry["aliases"] + old.get("aliases", [])))
                entry["reference_sources"] = sorted(set(entry["reference_sources"] + old.get("reference_sources", [])))
                entries.append(entry)
                print(f"Hentet {name}", flush=True)
            except Exception as exc:
                errors.append({"full_name": name, "error": str(exc)})
                print(f"FEIL {name}: {exc}", flush=True)
    if errors:
        save_json(ROOT / "data/sync-errors.json", errors)
        raise SystemExit("Ufullstendig henting; forrige katalog er beholdt. Se data/sync-errors.json.")
    # Identity is stable across GitHub renames; avoid accidental duplicate profiles.
    merged = {}
    for e in entries:
        if e["id"] in merged:
            old = merged[e["id"]]
            old["starred_at"] = old["starred_at"] or e["starred_at"]
            old["reference_sources"] = sorted(set(old["reference_sources"] + e["reference_sources"]))
            old["aliases"] = sorted(set(old["aliases"] + e["aliases"]))
        else:
            merged[e["id"]] = e
    data = {"schema_version": 1, "owner": owner, "collected_at": started,
            "finished_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "starred_count": len(stars), "pages": pages, "page_sizes": page_sizes,
            "endpoint": "https://api.github.com/user/starred",
            "pagination_complete": True, "starred_ids": sorted(x["repo"]["id"] for x in stars),
            "starred_names": sorted(star_map, key=str.casefold),
            "repositories": sorted(merged.values(), key=lambda x: x["full_name"].casefold())}
    save_json(ROOT / "data/github.json", data)
    (ROOT / "data/sync-errors.json").unlink(missing_ok=True)
    print(f"Lagret {len(merged)} unike repoer; {len(stars)} stjerner, {pages} side(r).")


if __name__ == "__main__":
    main()

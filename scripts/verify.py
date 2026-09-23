#!/usr/bin/env python3
"""Kontroller katalog, stjerner, lokale kilder og Markdown-lenker uten nettverk.

Dette er en integritetskontroll, ikke kjøring av de katalogførte prosjektene.
Teststatus kontrolleres som strukturerte felt; fri tekst må også gjennomgås.
Lenkekontrollen gjelder lokale filstier, ikke nettadresser eller ankre.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Check:
    def __init__(self, root):
        self.root = root.resolve()
        self.errors = []
        self.snapshots = set()
        self.links = 0

    def require(self, condition, message):
        if not condition:
            self.errors.append(message)
        return bool(condition)

    def local_path(self, value, label):
        if not self.require(isinstance(value, str) and bool(value), f"{label}: mangler filsti"):
            return None
        path = (self.root / value).resolve()
        if not self.require(not Path(value).is_absolute() and path.is_relative_to(self.root),
                            f"{label}: filsti utenfor biblioteket: {value}"):
            return None
        self.require(path.is_file(), f"{label}: mangler fil {value}")
        return path

    def read_json(self, name):
        try:
            return json.loads((self.root / name).read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            self.errors.append(f"{name}: {error}")
            return {}

    def snapshot(self, item, label, historical=False):
        name = item.get("path") if historical else item.get("local_path")
        path = self.local_path(name, label)
        if path is None or not path.is_file():
            return
        content = path.read_bytes()
        self.snapshots.add(path)
        self.require(hashlib.sha256(content).hexdigest() == item.get("sha256"), f"{label}: SHA-256 stemmer ikke: {name}")
        if not historical or "bytes" in item:
            self.require(len(content) == item.get("bytes"), f"{label}: feil byteantall: {name}")
        if not historical or "git_blob_sha" in item:
            blob = b"blob " + str(len(content)).encode("ascii") + b"\0" + content
            self.require(hashlib.sha1(blob).hexdigest() == item.get("git_blob_sha"), f"{label}: Git blob-SHA stemmer ikke: {name}")

    def runtime_status(self, entry, label, required=False, catalog=False):
        # A true status needs a local evidence file. The evidence's substance is
        # deliberately not claimed to be machine-verifiable by this script.
        runtime_key = "runtime_tested_in_this_catalog" if catalog else "runtime_tested"
        for key in (runtime_key, "installed", "integrated_in_game"):
            if key not in entry and not (required and key == runtime_key):
                continue
            value = entry.get(key)
            self.require(type(value) is bool, f"{label}: {key} må være eksplisitt true/false")
            if value is True:
                evidence = entry.get("test_evidence", [])
                if self.require(isinstance(evidence, list) and bool(evidence), f"{label}: {key}=true mangler test_evidence"):
                    for item in evidence:
                        self.local_path(item, f"{label}: test_evidence")

    def markdown_links(self):
        excluded = ("kilder/", "repoer/kilder/", "docs/historikk/", ".git/")
        for path in sorted(self.root.rglob("*.md")):
            relative = path.relative_to(self.root).as_posix()
            if relative.startswith(excluded) and relative != "docs/historikk/README.md":
                continue
            content = path.read_text(encoding="utf-8")
            # Code examples are not clickable links. Fence removal handles both
            # backtick and tilde fenced blocks used in our authored documents.
            content = re.sub(r"(?ms)^\s*(`{3,}|~{3,}).*?^\s*\1\s*$", "", content)
            content = re.sub(r"`+[^`]*`+", "", content)
            targets = re.findall(r"\[[^\]\n]*\]\(\s*(<[^>]*>|[^\s)]+)(?:\s+[\"'][^\n]*?[\"'])?\s*\)", content)
            targets += re.findall(r"(?m)^\s{0,3}\[[^\]\n]+\]:\s*(<[^>]*>|\S+)", content)
            for target in targets:
                target = target.removeprefix("<").removesuffix(">")
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                local = unquote(parsed.path)
                destination = (self.root / local.lstrip("/")) if local.startswith("/") else (path.parent / local)
                destination = destination.resolve()
                self.links += 1
                self.require(destination.is_relative_to(self.root) and destination.exists(),
                             f"{relative}: brutt eller ekstern lokal lenke: {target}")

    def run(self):
        github = self.read_json("data/github.json")
        catalog = self.read_json("data/catalog.json")
        for name in ("README.md", "KATALOG.md", "STARRED.md"):
            self.local_path(name, "Inngang")
        if not github or not catalog:
            return
        stars = github.get("starred_ids", [])
        names = github.get("starred_names", [])
        self.require(isinstance(stars, list) and all(type(i) is int for i in stars), "GitHub: ugyldige starred_ids")
        self.require(len(stars) == len(set(stars)), "GitHub: duplikate stjerne-ID-er")
        self.require(len(names) == len({n.casefold() for n in names}), "GitHub: duplikate stjernenavn")
        self.require(github.get("starred_count") == len(stars) == len(names), "GitHub: antall stjerner stemmer ikke")
        sizes = github.get("page_sizes", [])
        self.require(github.get("pagination_complete") is True, "GitHub: paginering er ikke fullført")
        self.require(bool(sizes) and github.get("pages") == len(sizes) and sum(sizes) == len(stars)
                     and all(size == 100 for size in sizes[:-1]) and 0 <= sizes[-1] < 100,
                     "GitHub: ufullstendig eller inkonsistent sideliste")
        for key, value in github.items():
            if key != "repositories":
                self.require(catalog.get(key) == value, f"Katalog: {key} avviker fra GitHub-snapshot")
        source_entries = github.get("repositories", [])
        entries = catalog.get("repositories", [])
        source_ids = [entry["id"] for entry in source_entries]
        ids = [entry["id"] for entry in entries]
        self.require(len(source_ids) == len(set(source_ids)), "GitHub: duplikate repo-ID-er")
        self.require(len(ids) == len(set(ids)), "Katalog: duplikate repo-ID-er")
        self.require(set(ids) == set(source_ids), "Katalog: repo-ID-er avviker fra GitHub-snapshot")
        self.require(set(stars) <= set(ids), "Katalog: en eller flere stjerner mangler")
        marked_stars = {entry["id"] for entry in entries if entry.get("starred_at")}
        self.require(marked_stars == set(stars), "Katalog: starred_at samsvarer ikke med starred_ids")
        source_by_id = {entry["id"]: entry for entry in source_entries}
        indexes = {}
        for name in ("KATALOG.md", "STARRED.md"):
            path = self.root / name
            indexes[name] = path.read_text(encoding="utf-8") if path.is_file() else ""
        for entry in entries:
            label = entry.get("full_name", str(entry.get("id")))
            source = source_by_id.get(entry["id"], {})
            for key, value in source.items():
                self.require(entry.get(key) == value, f"{label}: {key} avviker fra GitHub-snapshot")
            commit = entry.get("commit", "")
            self.require(bool(re.fullmatch(r"[0-9a-f]{40}", commit)), f"{label}: ugyldig commit")
            for field in ("summary", "reuse", "caveats"):
                self.require(bool(entry.get(field)), f"{label}: mangler {field}")
            for field in ("categories", "tags"):
                value = entry.get(field)
                self.require(isinstance(value, list) and (bool(value) or field == "tags")
                             and all(isinstance(v, str) and v for v in value),
                             f"{label}: {field} må være en tekstliste (minst én kategori)")
            expected_profile = "repoer/prosjekter/" + label.replace("/", "--") + ".md"
            self.require(entry.get("profile_path") == expected_profile, f"{label}: feil profile_path")
            self.local_path(entry.get("profile_path"), label)
            self.require(f"]({expected_profile})" in indexes["KATALOG.md"], f"{label}: mangler i KATALOG.md")
            in_starred_index = f"]({expected_profile})" in indexes["STARRED.md"]
            self.require(in_starred_index == (entry["id"] in stars), f"{label}: STARRED.md samsvarer ikke med starred_ids")
            self.runtime_status(entry, label, required=True, catalog=True)
            for reference in entry.get("reference_sources", []):
                self.local_path(reference, f"{label}: referanse")
            self.require(bool(entry.get("files")) or bool(entry.get("warnings")),
                         f"{label}: ingen kildetekster eller forklaring i warnings")
            for item in entry.get("files", []):
                self.snapshot(item, label)
                prefix = f"https://github.com/{label}/blob/{commit}/"
                self.require(item.get("source_url", "").startswith(prefix), f"{label}: kilde-URL er ikke festet til valgt commit")
        for name, key in (("repoer/coastal-webgpu-2026-09-20.json", "repositories"),
                          ("repoer/sentient-2026-09-12.json", "tools")):
            historical = self.read_json(name)
            for entry in historical.get(key, []):
                label = entry.get("repository", entry.get("name", name))
                self.runtime_status(entry, label, required=True)
                for item in entry.get("snapshots", []):
                    self.snapshot(item, label, historical=True)
        screenshots = self.read_json("data/screenshot-references.json")
        catalog_names = {entry["full_name"].casefold() for entry in entries}
        for filename, referenced_names in screenshots.get("images", {}).items():
            for name in referenced_names:
                self.require(name.casefold() in catalog_names, f"Skjermbilde {filename}: {name} mangler i katalogen")
        history = self.read_json("docs/historikk/manifest.json")
        for item in history.get("sources", []):
            path = "docs/historikk/" + item["snapshot"]
            self.snapshot({"path": path, "sha256": item.get("snapshot_sha256")}, "Historikk", historical=True)
            self.require(bool(re.fullmatch(r"[0-9a-f]{64}", item.get("source_sha256", ""))),
                         f"Historikk: ugyldig source_sha256 for {path}")
            if item.get("scope") == "exact_copy":
                self.require(item.get("source_sha256") == item.get("snapshot_sha256"), f"Historikk: exact_copy har ulike hasher for {path}")
        self.markdown_links()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()
    check = Check(args.root)
    try:
        check.run()
    except (OSError, KeyError, TypeError, ValueError, AttributeError) as error:
        check.errors.append(f"Ugyldig katalogstruktur eller lesefeil: {error}")
    if check.errors:
        print(f"FEIL: {len(check.errors)} kontrollpunkt(er)", file=sys.stderr)
        for error in check.errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"OK: stjerner/katalog, profiler, {len(check.snapshots)} kildefiler og {check.links} lokale lenker kontrollert.")
    print("Dette bekrefter lokal integritet og registrert teststatus; det bekrefter ikke programkjøring eller nettlenker.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

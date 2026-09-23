#!/usr/bin/env python3
"""Bygg Markdown/JSON offline fra hentede GitHub-kilder og egne notater."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ["Skills og agentverktøy", "Spill og spillmotorer", "3D og simulering",
              "Lyd og musikk", "Apper og egen drift", "Egne prosjekter", "Uklassifisert"]


def read(path):
    return json.loads((ROOT / path).read_text())


def write(path, text):
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text.rstrip() + "\n")


def cell(text):
    return str(text or "—").replace("|", "\\|").replace("\n", " ")


def license_label(repo):
    license = repo.get("license") or {}
    spdx = license.get("spdx_id")
    return spdx if spdx and spdx != "NOASSERTION" else "Ikke entydig identifisert"


def notes():
    result = {}
    for item in read("repoer/sentient-2026-09-12.json")["tools"]:
        name = item["primary_source_url"].removeprefix("https://github.com/").strip("/")
        result[name] = {"summary": item["purpose"], "categories": ["Apper og egen drift"],
                        "reuse": item["potential_use"], "caveats": item["caveats"], "tags": item["tags"]}
    for item in read("repoer/coastal-webgpu-2026-09-20.json")["repositories"]:
        result[item["repository"]] = {"summary": item["purpose"], "categories": ["3D og simulering"],
                "reuse": "Se bevart gjennomgang av vann, skum, strandkontakt og GPU-arkitektur i historiske notater.",
                "caveats": "Dokumentasjon og utvalgt kode ble gjennomgått 20. september 2026; ingen installasjon eller runtime-test. Unity krever tilpasning.", "tags": item["tags"]}
    for path in ("data/starred-notes.json", "data/extra-notes.json"):
        if (ROOT / path).exists():
            result.update(read(path))
    return result


def main():
    data, curated = read("data/github.json"), notes()
    entries = data["repositories"]
    date = data["collected_at"][:10]
    for repo in entries:
        name = repo["full_name"]
        note = next((curated[n] for n in [name] + repo.get("aliases", []) if n in curated), None)
        repo.update(note or {"summary": repo["description"] or name,
            "categories": ["Uklassifisert"], "reuse": "Les README og vurder relevans for det konkrete prosjektet.",
            "caveats": "Nytt funn; gjenbruksvurdering gjenstår.", "tags": repo.get("topics", [])})
        repo["runtime_tested_in_this_catalog"] = False
        repo["profile_path"] = f"repoer/prosjekter/{name.replace('/', '--')}.md"
        repo["tags"] = sorted(set(repo["tags"] + (repo.get("topics") or [])), key=str.casefold)
        sha, url = repo["commit"], repo["html_url"]
        status = "Stjernemerket" if repo["starred_at"] else ("Tidligere stjernemerket" if repo.get("previously_starred_at") else "Tidligere dokumentert referanse")
        lines = [f"# {name}", "", repo["summary"], "", f"[Åpne originalrepo]({url}) · [Tilbake til katalog](../../KATALOG.md)", "",
            "## Bruk og avgrensning", "", f"**Mulig gjenbruk:** {repo['reuse']}", "", f"**Merknader:** {repo['caveats']}", "",
            "Kildene er hentet og katalogisert. Ingen ny installasjon, spilltest eller ytelsesmåling er utført i denne katalogiseringen. Historiske tester gjelder bare dokumentert versjon og miljø.", "",
            "## Kilde og versjon", "", "| Felt | Verdi |", "|---|---|",
            f"| Utvalg | {status} |", f"| Kategorier | {cell(', '.join(repo['categories']))} |",
            f"| Kontrollert | {date} |", f"| Festet revisjon | [{sha}]({url}/commit/{sha}) |",
            f"| Standardgren | {cell(repo['default_branch'])} |", f"| Hovedspråk oppgitt av GitHub | {cell(repo['language'])} |",
            f"| Lisens identifisert av GitHub | {cell(license_label(repo))} |",
            f"| Synlighet ved innhenting | {'Privat' if repo['private'] else 'Offentlig'} |",
            f"| Arkivert | {'Ja' if repo['archived'] else 'Nei'} |",
            f"| Sist pushet, ifølge GitHub | {repo['pushed_at']} |"]
        if repo["starred_at"]:
            lines.append(f"| Stjernemerket av {data['owner']} | {repo['starred_at']} |")
        if repo.get("parent"):
            lines.append(f"| Fork av | [{repo['parent']}](https://github.com/{repo['parent']}) |")
        if repo.get("aliases"):
            lines.append(f"| Tidligere navn / videresending | {cell(', '.join(repo['aliases']))} |")
        if repo.get("homepage"):
            lines += ["", f"Oppgitt prosjektside: {repo['homepage']}"]
        lines += ["", "GitHubs lisensfelt er metadata. Les de faktiske lisensene og komponentvilkårene før kode, modeller, data eller assets gjenbrukes.", "",
            "## Bevarte dokumentkilder", "", "Tekstkopiene er festet til revisjonen over og lagret uten endringer med `.txt`-suffiks. Bilder, underlenker og hele kildekodetrær er ikke speilet.", "",
            "| Fil | Original ved festet revisjon | Lokal kopi | SHA-256 |", "|---|---|---|---|"]
        for f in repo["files"]:
            lines.append(f"| {cell(f['path'])} | [GitHub]({f['source_url']}) | [Kilde](../../{f['local_path']}) | `{f['sha256']}` |")
        if repo["reference_sources"]:
            lines += ["", "## Tidligere gjennomgang", ""]
            for source in repo["reference_sources"]:
                lines.append(f"- [Bevart notat](../../{source})")
        if repo.get("warnings"):
            lines += ["", "## Innhentingsmerknader", ""] + [f"- {w}" for w in repo["warnings"]]
        lines += ["", "**Søkeord:** " + ", ".join(repo["tags"])]
        write(repo["profile_path"], "\n".join(lines))
    write("data/catalog.json", json.dumps(data, ensure_ascii=False, indent=2))
    catalogue = ["# Prosjektkatalog", "", f"{len(entries)} unike repoer; {data['starred_count']} er stjernemerket. Innhentet {date}.", "",
        "[Startside](README.md) · [Alle stjernemerkede](STARRED.md) · [Maskinlesbar katalog](data/catalog.json)", "",
        "Kategorier og mulig gjenbruk er våre vurderinger. Repoer kan stå i flere kategorier. ⭐ betyr at repoet var stjernemerket ved siste innhenting."]
    for category in CATEGORIES:
        subset = [r for r in entries if category in r["categories"]]
        if not subset:
            continue
        catalogue += ["", f"## {category}", "", "| Repo / notat | Formål | Lisensmetadata |", "|---|---|---|"]
        for repo in subset:
            mark = "⭐ " if repo["starred_at"] else ""
            catalogue.append(f"| {mark}[{repo['full_name']}]({repo['profile_path']}) | {cell(repo['summary'])} | {cell(license_label(repo))} |")
    write("KATALOG.md", "\n".join(catalogue))
    starred = ["# Alle stjernemerkede GitHub-prosjekter", "",
        f"{data['starred_count']} repoer fra den innloggede kontoen **{data['owner']}**, hentet {data['collected_at']}.", "",
        f"GitHub REST `GET /user/starred`, alle sider lest ({data['pages']} side(r); sidestørrelser: {data['page_sizes']}). Privat tilgjengelig innhold er inkludert.", "",
        "[Startside](README.md) · [Hele katalogen](KATALOG.md)", "",
        "| Repo / notat | Stjernemerket | Kategori |", "|---|---|---|"]
    for repo in sorted((r for r in entries if r["starred_at"]), key=lambda r: r["starred_at"], reverse=True):
        starred.append(f"| [{repo['full_name']}]({repo['profile_path']}) | {repo['starred_at'][:10]} | {cell(', '.join(repo['categories']))} |")
    write("STARRED.md", "\n".join(starred))
    print(f"Genererte {len(entries)} profiler, KATALOG.md, STARRED.md og data/catalog.json.")


if __name__ == "__main__":
    main()

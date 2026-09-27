#!/usr/bin/env python3
"""Oppdater offentlig inventar: egne offentlige repoer, offentlige stjerner og Scenario-skills.

Bruker GitHubs offentlige API uten innlogging. Dette er et supplement til den
kuraterte katalogen, ikke en erstatning for autentisert /user/starred.
"""
import datetime as dt
import json
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OWNER = "Tombonator3000"
SCENARIO = "scenario-labs/skills"
HEADERS = {"User-Agent": "prosjektbibliotek-public-inventory", "Accept": "application/vnd.github+json"}


def get(path):
    with urlopen(Request("https://api.github.com/" + path, headers=HEADERS), timeout=30) as response:
        return json.load(response), response.headers.get("Link", "")


def all_pages(path):
    items = []
    page = 1
    while True:
        batch, links = get(path + f"&page={page}")
        items.extend(batch)
        if 'rel="next"' not in links:
            break
        page += 1
    return items, page


def main():
    stars, star_pages = all_pages(f"users/{OWNER}/starred?per_page=100")
    owned, own_pages = all_pages(f"users/{OWNER}/repos?per_page=100&type=owner&sort=full_name")
    scenario, _ = get(f"repos/{SCENARIO}")
    tree, _ = get(f"repos/{SCENARIO}/git/trees/{scenario['default_branch']}?recursive=1")
    if tree.get("truncated"):
        raise RuntimeError("Scenario-treet er avkortet; inventaret ble ikke oppdatert")
    skills = sorted(({"name": p["path"].split("/")[-2], "path": p["path"]}
                     for p in tree["tree"] if p["path"].startswith("skills/")
                     and p["path"].endswith("/SKILL.md")), key=lambda s: s["name"])
    if not skills or not stars or not owned:
        raise RuntimeError("Uventet tomt API-resultat; inventaret ble ikke oppdatert")
    def repo(r):
        return {"full_name": r["full_name"], "url": r["html_url"],
                "description": r.get("description"), "archived": r["archived"],
                "license_spdx": (r.get("license") or {}).get("spdx_id"),
                "default_branch": r["default_branch"]}
    data = {"collected_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "scope": "Public GitHub API; private repositories and private stars are excluded",
            "owner": OWNER, "star_pages": star_pages, "owned_pages": own_pages,
            "starred": sorted(map(repo, stars), key=lambda r: r["full_name"].casefold()),
            "owned_public": sorted(map(repo, owned), key=lambda r: r["full_name"].casefold()),
            "scenario": {"repository": SCENARIO, "url": scenario["html_url"],
                         "skills_page": "https://skills.sh/scenario-labs/skills",
                         "tree_sha": tree["sha"], "tree_truncated": False,
                         "license_spdx": (scenario.get("license") or {}).get("spdx_id"),
                         "skills": skills}}
    starred = {x["full_name"] for x in data["starred"]}
    lines = ["# Oppdatert prosjektinventar", "",
             f"Hentet {data['collected_at']} fra GitHubs offentlige API. ", "",
             f"**{len(stars)} offentlige stjerner · {len(owned)} egne offentlige repoer · {len(skills)} Scenario-skills.**",
             "Repoer som både er egne og stjernemerket står i begge listene. [JSON-data](data/offentlig-inventar.json).", "",
             "Dette er et søkbart register med lenker til kildekoden, ikke en kopi av alle kodebasene. "
             "Private repoer og eventuelle private stjerner er ikke med i dette offentlige inventaret. "
             "Den [kuraterte katalogen](KATALOG.md) har eldre profiler og vurderinger; "
             "dens stjernetall viser innhentingen 23. september, ikke dagens status.", "",
             "## Stjernemerket på GitHub", "",
             "| Repo | Hva det er | Lisensfelt |", "|---|---|---|"]
    for r in data["starred"]:
        lines.append(f"| [{r['full_name']}]({r['url']}) | {str(r['description'] or 'Ingen beskrivelse').replace('|', '/')} | {r['license_spdx'] or 'Uavklart'} |")
    lines += ["", "## Egne offentlige repoer", "",
              "| Repo | Hva det er | I stjernene |", "|---|---|---|"]
    for r in data["owned_public"]:
        lines.append(f"| [{r['full_name']}]({r['url']}) | {str(r['description'] or 'Ingen beskrivelse').replace('|', '/')} | {'Ja' if r['full_name'] in starred else 'Nei'} |")
    lines += ["", "## Scenario Agent Skills", "",
              f"[Oversikt på skills.sh]({data['scenario']['skills_page']}) · "
              f"[Kildekode ved festet revisjon](https://github.com/{SCENARIO}/tree/{tree['sha']}/skills) · "
              f"GitHubs lisensfelt: {data['scenario']['license_spdx'] or 'uavklart'}.", "",
              "De generelle Scenario-skillsene bruker Scenario MCP og tjenesten deres. "
              "Ekspertfamiliene for Blender, Maya, ZBrush, Unreal og Unity krever den aktuelle appen "
              "og har egne opplysninger om hva som er testet. Ingen skills er installert her.", "",
              "| Skill | Kilde |", "|---|---|"]
    for skill in skills:
        lines.append(f"| `{skill['name']}` | [SKILL.md](https://github.com/{SCENARIO}/blob/{tree['sha']}/{skill['path']}) |")
    lines += ["", "## Bruk i prosjektene", "",
              "- **Morbidium, Guild Life, The Deep Ones:** se `scenario-game-assets`, `scenario-sprite-animation`, `scenario-textures`, `scenario-3d`, `scenario-blender-expert` og `scenario-unity-expert`.",
              "- **Vann og hav:** se stjernene Clearwater, WaterCuda, ShoreBreak, coastal-simulation, Tidewater og Three.js ocean simulator. Undersøk lisens og ytelse i målprosjektet før kode tas inn.",
              "- **SIGNAL / 47 og Transcendensens Vev:** se `scenario-consistency`, `scenario-quality-gate`, `scenario-blender-previs-storyboard` og `scenario-unity-world-building`.",
              "- **Kildekode til spill:** [bobeff/open-source-games](https://github.com/bobeff/open-source-games) er en katalog over mange spill. Hvert underliggende spill har sin egen lisens.", "",
              "Oppdater dette registeret med `python3 scripts/sync_public_inventory.py`. "
              "For fullstendig autentisert starhistorikk, inkludert private tilganger, bruk eksisterende "
              "`scripts/sync_github.py` i et privat bibliotek. Kontroller lisens per kilde før faktisk gjenbruk."]
    (ROOT / "data/offentlig-inventar.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "OFFENTLIG_INVENTAR.md").write_text("\n".join(lines) + "\n")
    print(f"{len(stars)} stjerner, {len(owned)} egne offentlige repoer, {len(skills)} skills")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Oppdater offentlig inventar: egne offentlige repoer, offentlige stjerner og Scenario-skills.

Bruker GitHubs offentlige API uten innlogging. Dette er et supplement til den
kuraterte katalogen, ikke en erstatning for autentisert /user/starred.
"""
import datetime as dt
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OWNER = "Tombonator3000"
SCENARIO = "scenario-labs/skills"
HEADERS = {"User-Agent": "prosjektbibliotek-public-inventory", "Accept": "application/vnd.github+json"}


class ListLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside = False
        self.found_container = False
        self.depth = 0
        self.in_heading = False
        self.names = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id") == "user-list-repositories":
            self.inside = True
            self.found_container = True
        if self.inside and tag == "div":
            self.depth += 1
        if self.inside and tag == "h2":
            self.in_heading = True
        if self.inside and self.in_heading and tag == "a":
            link = attrs.get("href", "")
            if link.startswith("/") and len(link.strip("/").split("/")) == 2:
                self.names.add(link.strip("/"))

    def handle_endtag(self, tag):
        if tag == "h2":
            self.in_heading = False
        if self.inside and tag == "div":
            self.depth -= 1
            if self.depth == 0:
                self.inside = False


def get(path, accept="application/vnd.github+json"):
    headers = {**HEADERS, "Accept": accept}
    with urlopen(Request("https://api.github.com/" + path, headers=headers), timeout=30) as response:
        return json.load(response), response.headers.get("Link", "")


def all_pages(path, accept="application/vnd.github+json"):
    items = []
    page = 1
    while True:
        batch, links = get(path + f"&page={page}", accept)
        items.extend(batch)
        if 'rel="next"' not in links:
            break
        page += 1
    return items, page


def main():
    star_events, star_pages = all_pages(f"users/{OWNER}/starred?per_page=100&sort=created&direction=desc",
                                       "application/vnd.github.star+json")
    if any(not event.get("starred_at") or not event.get("repo") for event in star_events):
        raise RuntimeError("Stjernedatoer mangler; forrige inventar er beholdt")
    stars = [event["repo"] for event in star_events]
    star_dates = {event["repo"]["id"]: event["starred_at"] for event in star_events}
    if len(star_dates) != len(stars):
        raise RuntimeError("Duplikater i starlisten; forrige inventar er beholdt")
    owned, own_pages = all_pages(f"users/{OWNER}/repos?per_page=100&type=owner&sort=full_name")
    scenario, _ = get(f"repos/{SCENARIO}")
    revision, _ = get(f"repos/{SCENARIO}/commits/{scenario['default_branch']}")
    commit = revision['sha']
    tree, _ = get(f"repos/{SCENARIO}/git/trees/{commit}?recursive=1")
    if tree.get("truncated"):
        raise RuntimeError("Scenario-treet er avkortet; inventaret ble ikke oppdatert")
    skills = sorted(({"name": p["path"].split("/")[-2], "path": p["path"]}
                     for p in tree["tree"] if p["path"].startswith("skills/")
                     and p["path"].endswith("/SKILL.md")), key=lambda s: s["name"])
    if not skills or not stars or not owned:
        raise RuntimeError("Uventet tomt API-resultat; inventaret ble ikke oppdatert")
    list_url = f"https://github.com/stars/{OWNER}/lists/inspiration"
    with urlopen(Request(list_url, headers={"User-Agent": "Mozilla/5.0"}), timeout=30) as response:
        parser = ListLinks()
        parser.feed(response.read().decode("utf-8"))
    inspiration = sorted(parser.names, key=str.casefold)
    if not parser.found_container:
        raise RuntimeError("Kunne ikke lese Inspiration-listen; forrige inventar er beholdt")
    def repo(r):
        return {"id": r["id"], "full_name": r["full_name"], "url": r["html_url"],
                "description": r.get("description"), "archived": r["archived"],
                "license_spdx": (r.get("license") or {}).get("spdx_id"),
                "default_branch": r["default_branch"], "pushed_at": r["pushed_at"]}
    data = {"collected_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
            "scope": "Public GitHub API; private repositories and private stars are excluded",
            "owner": OWNER, "star_pages": star_pages, "owned_pages": own_pages,
            "starred": sorted(({**repo(r), "starred_at": star_dates[r["id"]]} for r in stars),
                              key=lambda r: r["full_name"].casefold()),
            "owned_public": sorted(map(repo, owned), key=lambda r: r["full_name"].casefold()),
            "public_lists": [{"name": "✨ Inspiration", "url": list_url,
                              "repositories": inspiration}],
            "scenario": {"repository": SCENARIO, "url": scenario["html_url"],
                         "skills_page": "https://skills.sh/scenario-labs/skills",
                         "commit": commit, "tree_sha": revision['commit']['tree']['sha'], "tree_truncated": False,
                         "license_spdx": (scenario.get("license") or {}).get("spdx_id"),
                         "skills": skills}}
    starred = {x["full_name"] for x in data["starred"]}
    lines = ["# Oppdatert prosjektinventar", "",
             f"Hentet {data['collected_at']} fra GitHubs offentlige API.", "",
             f"**{len(stars)} offentlige stjerner · {len(owned)} egne offentlige repoer · {len(skills)} Scenario-skills.**",
             "Repoer som både er egne og stjernemerket står i begge listene. [JSON-data](data/offentlig-inventar.json).", "",
             "Dette er et søkbart register med lenker til kildekoden, ikke en kopi av alle kodebasene. "
             "Private repoer og eventuelle private stjerner er ikke med i dette offentlige inventaret. "
             "Den [kuraterte katalogen](KATALOG.md) har eldre profiler og vurderinger; "
             "dens stjernetall viser innhentingen 23. september, ikke dagens status. "
             "Se [samlet skilloversikt](SKILLS.md) for skills fra alle undersøkte stjernerepoer og egne skillpakker.", "",
             "## Egen stjerneliste: ✨ Inspiration", "",
             f"[Åpne listen på GitHub]({list_url}). {len(inspiration)} repoer er registrert i listen.", ""]
    for name in inspiration:
        lines.append(f"- [{name}](https://github.com/{name})")
    lines += ["",
             "## Stjernemerket på GitHub", "",
             "Stjernedatoer er oppgitt i UTC.", "",
             "| Repo | Hva det er | Stjernemerket | Lisensfelt |", "|---|---|---|---|"]
    for r in data["starred"]:
        lines.append(f"| [{r['full_name']}]({r['url']}) | {str(r['description'] or 'Ingen beskrivelse').replace('|', '/')} | {r['starred_at']} | {r['license_spdx'] or 'Uavklart'} |")
    lines += ["", "## Egne offentlige repoer", "",
              "| Repo | Hva det er | I stjernene |", "|---|---|---|"]
    for r in data["owned_public"]:
        lines.append(f"| [{r['full_name']}]({r['url']}) | {str(r['description'] or 'Ingen beskrivelse').replace('|', '/')} | {'Ja' if r['full_name'] in starred else 'Nei'} |")
    lines += ["", "## Scenario Agent Skills", "",
              f"[Oversikt på skills.sh]({data['scenario']['skills_page']}) · "
              f"[Kildekode ved festet revisjon](https://github.com/{SCENARIO}/tree/{commit}/skills) · "
              f"GitHubs lisensfelt: {data['scenario']['license_spdx'] or 'uavklart'}.", "",
              "De generelle Scenario-skillsene bruker Scenario MCP og tjenesten deres. "
              "Ekspertfamiliene for Blender, Maya, ZBrush, Unreal og Unity krever den aktuelle appen "
              "og har egne opplysninger om hva som er testet. Ingen skills er installert her.", "",
              "| Skill | Kilde |", "|---|---|"]
    for skill in skills:
        lines.append(f"| `{skill['name']}` | [SKILL.md](https://github.com/{SCENARIO}/blob/{commit}/{skill['path']}) |")
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

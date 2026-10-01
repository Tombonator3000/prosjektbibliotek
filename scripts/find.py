#!/usr/bin/env python3
"""Søk lokalt i referansekatalogen, uten nettverk eller installerte pakker."""
import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def flatten(value):
    if isinstance(value, dict):
        return " ".join(flatten(item) for item in value.values())
    if isinstance(value, list):
        return " ".join(flatten(item) for item in value)
    return str(value) if value is not None else ""


def all_records(root):
    repositories = json.loads((root / 'data/catalog.json').read_text(encoding='utf-8'))['repositories']
    inventory_path = root / 'data/offentlig-inventar.json'
    if inventory_path.exists():
        inventory = json.loads(inventory_path.read_text())
        for current in inventory['starred'] + inventory['owned_public']:
            previous = next((r for r in repositories if r.get('id') == current.get('id')
                             or r['full_name'] == current['full_name']), None)
            if previous is not None:
                previous.update({k: current[k] for k in ('full_name', 'description')})
                previous['html_url'] = current['url']
            else:
                repositories.append({'id': current.get('id'), 'full_name': current['full_name'],
                                     'description': current['description'], 'html_url': current['url'],
                                     'categories': ['Egne prosjekter'] if current['full_name'].startswith('Tombonator3000/') else ['Offentlig inventar'],
                                     'profile_path': 'OFFENTLIG_INVENTAR.md'})
    skills_path = root / 'data/skills.json'
    if skills_path.exists():
        data = json.loads(skills_path.read_text())
        for skill in data['entries']:
            repositories.append({'full_name': f"{skill['repository']}:{skill['name']}",
                                 'summary': skill['path'], 'html_url': skill['url'],
                                 'categories': ['Skills og agentverktøy'], 'profile_path': 'SKILLS.md'})
        for skill in data['personal_bundles']:
            repositories.append({'full_name': skill['name'], 'summary': skill['description'],
                                 'html_url': 'https://github.com/Tombonator3000/prosjektbibliotek/blob/main/' + skill['path'],
                                 'categories': ['Skills og agentverktøy'], 'profile_path': skill['path']})
    return repositories


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="*", help="Søkeord; alle ordene må finnes, uansett store/små bokstaver.")
    parser.add_argument("--category", help="Filtrer på en eksakt kategori, uansett store/små bokstaver.")
    parser.add_argument("--list-categories", action="store_true", help="Vis tilgjengelige kategorier.")
    parser.add_argument("--json", action="store_true", help="Skriv treffene som JSON.")
    parser.add_argument("--root", type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()
    try:
        repositories = all_records(args.root)
        if not isinstance(repositories, list):
            raise ValueError("repositories må være en liste")
        categories = sorted({category for repo in repositories for category in repo["categories"]}, key=str.casefold)
        if args.list_categories:
            print("\n".join(categories))
            return 0
        terms = " ".join(args.query).casefold().split()
        fields = ("full_name", "description", "purpose", "summary", "reuse", "categories", "tags")
        matches = []
        for repo in repositories:
            if args.category and args.category.casefold() not in [c.casefold() for c in repo["categories"]]:
                continue
            haystack = flatten([repo.get(field) for field in fields]).casefold()
            if all(term in haystack for term in terms):
                matches.append(repo)
        matches.sort(key=lambda repo: repo["full_name"].casefold())
        if args.json:
            print(json.dumps(matches, ensure_ascii=False, indent=2))
        else:
            print(f"{len(matches)} treff")
            for repo in matches:
                print(f"\n{repo['full_name']} [{', '.join(repo['categories'])}]")
                print(f"  {flatten(repo.get('summary') or repo.get('purpose') or repo.get('description'))}")
                print(f"  Gjenbruk: {flatten(repo.get('reuse'))}")
                print(f"  {repo['html_url']}")
                print(f"  Profil: {repo['profile_path']}")
        return 0
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(f"Kan ikke søke i katalogen: {error}. Kjør scripts/build_catalog.py og scripts/verify.py.", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())

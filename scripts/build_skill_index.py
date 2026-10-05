#!/usr/bin/env python3
"""Bygg skilloversikt. --refresh sjekker stjerner og egne offentlige repoer."""
import argparse
import concurrent.futures
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]


def api(path):
    if shutil.which('gh'):
        result = subprocess.run(['gh', 'api', path], capture_output=True, text=True, timeout=60)
        if result.returncode:
            raise RuntimeError(f'GitHub-kall feilet: {path}')
        return json.loads(result.stdout)
    with urlopen(Request('https://api.github.com/' + path,
                         headers={'User-Agent': 'prosjektbibliotek-skill-index'}), timeout=30) as response:
        return json.load(response)


def scan(repo):
    name = repo['full_name']
    revision = api(f"repos/{name}/commits/{quote(repo['default_branch'], safe='')}")
    commit = revision['sha']
    tree = api(f'repos/{name}/git/trees/{commit}?recursive=1')
    if tree.get('truncated'):
        raise RuntimeError(f'Avkortet tre for {name}; beholdt forrige manifest')
    return {'repository': name, 'commit': commit, 'tree_sha': revision['commit']['tree']['sha'], 'truncated': False,
            'pushed_at': repo['pushed_at'], 'default_branch': repo['default_branch'],
            'license_spdx': repo.get('license_spdx'),
            'skills': [{'path': p['path'], 'blob_sha': p['sha']} for p in tree['tree']
                       if p['type'] == 'blob' and p['mode'] != '120000'
                       and re.search(r'(^|/)SKILL\.md$', p['path'], re.I)]}


def main():
    args = argparse.ArgumentParser(description=__doc__)
    args.add_argument('--refresh', action='store_true')
    args = args.parse_args()
    inventory = json.loads((ROOT / 'data/offentlig-inventar.json').read_text())
    cache_path = ROOT / 'data/skill-sources.json'
    cached = json.loads(cache_path.read_text()) if cache_path.exists() else {'sources': []}
    sources = {s['repository']: s for s in cached['sources']}
    starred = {r['full_name'] for r in inventory['starred']}
    owned = {r['full_name'] for r in inventory['owned_public']}
    current = {r['full_name']: r for r in inventory['starred'] + inventory['owned_public']}
    if args.refresh:
        pending = [r for n, r in current.items() if n not in sources
                   or sources[n].get('pushed_at') != r.get('pushed_at')]
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            updated = list(pool.map(scan, pending))
        sources.update({s['repository']: s for s in updated})
        # Keep old skill references even after a star is removed.
        cached = {'schema_version': 1, 'collected_at': inventory['collected_at'],
                  'scope': 'Public repositories; SKILL.md documents, not runtime verification',
                  'scanned_count': len(current),
                  'sources': sorted(sources.values(), key=lambda s: s['repository'].casefold())}
        cache_path.write_text(json.dumps(cached, ensure_ascii=False, indent=2) + '\n')
        print(f'Oppdaterte {len(updated)} nye/endrede skillkilder')
    missing = set(current) - set(sources)
    if missing:
        raise RuntimeError('Nye repoer mangler skillgjennomgang; kjør med --refresh')
    entries = []
    for source in sorted(sources.values(), key=lambda s: s['repository'].casefold()):
        if source.get('truncated') or source.get('error'):
            raise RuntimeError(f"Ufullstendig skillkilde: {source['repository']}")
        for skill in source['skills']:
            # These are copies of personal bundles already indexed below.
            if source['repository'] == 'Tombonator3000/prosjektbibliotek' and skill['path'].startswith('skills/'):
                continue
            name = skill['path'].split('/')[-2] if '/' in skill['path'] else source['repository'].split('/')[-1]
            entries.append({'name': name, 'repository': source['repository'], 'path': skill['path'],
                            'blob_sha': skill['blob_sha'], 'commit': source['commit'],
                            'url': f"https://github.com/{source['repository']}/blob/{source['commit']}/{quote(skill['path'], safe='/')}",
                            'kind': 'repoarbeid' if source['repository'] == 'scenario-labs/skills'
                                    and not skill['path'].startswith('skills/') else 'skill',
                            'license_spdx': source.get('license_spdx'),
                            'currently_starred': source['repository'] in starred,
                            'currently_owned': source['repository'] in owned})
    bundles = []
    for path in sorted((ROOT / 'skills').glob('*/SKILL.md')):
        text = path.read_text()
        name = re.search(r'^name:\s*(.+)$', text, re.M).group(1).strip()
        description = re.search(r'^description:\s*(.+)$', text, re.M).group(1).strip()
        files = [{'path': f.relative_to(ROOT).as_posix(),
                  'sha256': hashlib.sha256(f.read_bytes()).hexdigest()}
                 for f in sorted(path.parent.rglob('*')) if f.is_file()]
        bundle = {'name': name, 'description': description, 'path': path.relative_to(ROOT).as_posix(),
                  'source': 'Eksisterende personlig skill, kopiert uten endringer', 'files': files}
        bundles.append(bundle)
    data = {'schema_version': 1, 'collected_at': inventory['collected_at'],
            'scanned_starred_repositories': len(starred),
            'scanned_owned_repositories': len(owned),
            'scanned_unique_repositories': len(current),
            'github_skill_documents': len(entries),
            'github_unique_document_blobs': len({e['blob_sha'] for e in entries}),
            'scenario_product_skills': len(inventory['scenario']['skills']),
            'entries': entries, 'personal_bundles': bundles}
    (ROOT / 'data/skills.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    lines = ['# Skills i prosjektbiblioteket', '',
             f"Oppdatert {inventory['collected_at'][:10]}. Alle {len(starred)} offentlige stjernerepoer og "
             f"{len(owned)} egne offentlige repoer er undersøkt for `SKILL.md` ({len(current)} unike repoer).", '',
             f"**{len(entries)} SKILL.md-filer** ({data['github_unique_document_blobs']} ulike dokumentinnhold) fra "
             f"{len({e['repository'] for e in entries})} repoer, pluss **{len(bundles)} egen komplett skillpakke**.", '',
             '[Startside](README.md) · [Stjerner og egne repoer](OFFENTLIG_INVENTAR.md) · [JSON](data/skills.json)', '',
             'Dette er en kildeoversikt. Noen filer er interne hjelpere for repoarbeid, og like dokumenter kan finnes flere steder. '
             'Ingen tredjepartskills er installert eller kjørt i denne innsamlingen. Lisensfeltet er GitHub-metadata; '
             'kontroller selve lisensen og nødvendige tjenester før bruk.', '', '## Egne skillpakker', '']
    for b in bundles:
        lines += [f"### {b['name']}", '', b['description'], '',
                  f"[SKILL.md]({b['path']}) · [Hele pakken]({Path(b['path']).parent.as_posix()})", '',
                  f"{len(b['files'])} filer er kopiert byte for byte fra den eksisterende personlige skillen. "
                  'Pakken inkluderer scripts, referanser, metadata og ikon. Den er tilgjengelig som kilde i biblioteket.', '']
    for repository in sorted({e['repository'] for e in entries}, key=str.casefold):
        subset = [e for e in entries if e['repository'] == repository]
        lines += [f'## {repository}', '', f"{len(subset)} skilldokumenter. [Originalrepo](https://github.com/{repository}).", '',
                  '| Skill / mappe | Type | Kilde ved festet commit |', '|---|---|---|']
        for e in subset:
            lines.append(f"| `{e['name']}` | {e['kind']} | [SKILL.md]({e['url']}) |")
        lines += ['']
    lines += ['## Oppdater og søk', '', '```sh', 'python3 scripts/sync_public_inventory.py',
              'python3 scripts/build_skill_index.py --refresh', 'python3 scripts/find.py prop-art',
              'python3 scripts/find.py morbidium-spritesheets', '```', '',
              'Skilloversikten kan bygges offline uten `--refresh`. Ved ny innhenting brukes GitHub CLI hvis tilgjengelig, '
              'ellers offentlig API. Private stjerner omfattes ikke.']
    (ROOT / 'SKILLS.md').write_text('\n'.join(lines) + '\n')
    print(f'{len(entries)} skilldokumenter og {len(bundles)} egne skillpakker')


if __name__ == '__main__':
    main()

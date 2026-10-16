#!/usr/bin/env python3
"""Søk offline i verktøy, skills og løsningskort med synonymer og relevansrangering."""
import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
WEIGHTS = {'full_name': 12, 'title': 12, 'tags': 10, 'keywords': 10, 'aliases': 9,
           'symptom': 9, 'stack': 8, 'summary': 7, 'description': 6, 'reuse': 5,
           'categories': 3, 'purpose': 2, 'caveats': 1}


def flatten(value):
    if isinstance(value, dict):
        return ' '.join(flatten(item) for item in value.values())
    if isinstance(value, list):
        return ' '.join(flatten(item) for item in value)
    return str(value) if value is not None else ''


def normalize(value):
    text = flatten(value).casefold().translate(str.maketrans({'æ': 'ae', 'ø': 'o'}))
    text = ''.join(c for c in unicodedata.normalize('NFKD', text) if not unicodedata.combining(c))
    return ' '.join(re.findall(r'[a-z0-9]+', text))


def read(root, name):
    return json.loads((root / name).read_text(encoding='utf-8'))


def configuration(root):
    path = root / 'data/search-terms.json'
    return read(root, 'data/search-terms.json') if path.exists() else {'synonyms': [], 'stop_words': [], 'keywords': {}}


def all_records(root):
    """Bygg én fersk visning; originalkatalog og kildearkiv endres ikke."""
    repositories = read(root, 'data/catalog.json')['repositories']
    notes = {}
    for name in ('starred-notes.json', 'extra-notes.json'):
        if (root / 'data' / name).exists():
            notes.update(read(root, 'data/' + name))
    inventory = read(root, 'data/offentlig-inventar.json') if (root / 'data/offentlig-inventar.json').exists() else {}
    current_ids = {r['id'] for key in ('starred', 'owned_public') for r in inventory.get(key, [])}
    for current in inventory.get('starred', []) + inventory.get('owned_public', []):
        previous = next((r for r in repositories if r.get('id') == current['id']), None)
        if previous is None:
            previous = {'id': current['id'], 'profile_path': 'OFFENTLIG_INVENTAR.md',
                        'categories': ['Egne prosjekter'] if current['full_name'].startswith('Tombonator3000/') else ['Offentlig inventar']}
            repositories.append(previous)
        previous.update({k: current[k] for k in ('full_name', 'description', 'archived', 'pushed_at', 'default_branch', 'license_spdx') if k in current})
        previous['html_url'] = current['url']
        if current.get('starred_at'):
            previous['starred_at'] = current['starred_at']
    records = []
    for repo in repositories:
        note = next((notes[n] for n in [repo['full_name']] + repo.get('aliases', []) if n in notes), {})
        tags = sorted(set(repo.get('tags', []) + repo.get('topics', []) + note.get('tags', [])), key=lambda s: (s.casefold(), s))
        repo.update(note)
        repo.update({'tags': tags, 'record_type': 'repo', 'key': f"repo:{repo['id']}",
                     'current_public': repo['id'] in current_ids})
        records.append(repo)
    if (root / 'data/skills.json').exists():
        data = read(root, 'data/skills.json')
        groups = {}
        # Identical Git blobs are one skill result, also across forks and folders.
        ordered = sorted(data['entries'], key=lambda s: (not s.get('currently_starred'), s.get('currently_owned', False),
                                                         len(s['path']), s['repository'].casefold(), s['path']))
        for skill in ordered:
            key = 'skill:' + skill['blob_sha']
            source = {'repository': skill['repository'], 'path': skill['path'], 'url': skill['url'], 'commit': skill['commit']}
            alias = f"{skill['repository']}:{skill['name']}"
            if key in groups:
                groups[key]['sources'].append(source)
                groups[key]['aliases'].append(alias)
                continue
            name = skill.get('display_name') or skill['name']
            groups[key] = {'key': key, 'record_type': 'skill', 'full_name': f"{skill['repository']}:{name}",
                           'summary': skill.get('description') or skill['path'], 'description': skill.get('description', ''),
                           'aliases': [alias, skill['path']], 'sources': [source], 'tags': [name, skill['name']],
                           'usage': skill['kind'], 'html_url': skill['url'], 'commit': skill['commit'],
                           'license_spdx': skill.get('license_spdx'), 'categories': ['Skills og agentverktøy'], 'profile_path': 'SKILLS.md'}
        records.extend(groups.values())
        for skill in data['personal_bundles']:
            records.append({'key': 'personal:' + skill['name'], 'record_type': 'skill', 'full_name': skill['name'],
                            'summary': skill['description'], 'tags': [skill['name']], 'categories': ['Skills og agentverktøy'],
                            'html_url': 'https://github.com/Tombonator3000/prosjektbibliotek/blob/main/' + skill['path'],
                            'profile_path': skill['path']})
    if (root / 'data/losninger.json').exists():
        for card in read(root, 'data/losninger.json')['cards']:
            records.append({'key': 'solution:' + card['id'], 'record_type': 'solution',
                            'full_name': f"løsning/{card['domain']}/{card['id']}", 'title': card['title'],
                            'summary': card['title'], 'status': card['status'], 'stack': card['stack'],
                            'symptom': card['symptom'], 'description': card['symptom'],
                            'reuse': card['solution'].split('\n\n')[0], 'purpose': card['solution'], 'caveats': card['caveats'],
                            'tags': card['tags'], 'origin': card['origin'], 'commit': card['origin_commit'],
                            'evidence': card['evidence'], 'used_in': card['used_in'], 'categories': ['Løsningskort'],
                            'html_url': 'https://github.com/Tombonator3000/prosjektbibliotek/blob/main/' + card['path'], 'profile_path': card['path']})
    config = configuration(root)
    for record in records:
        names = [record['key'], record['full_name']] + record.get('aliases', [])
        record['keywords'] = sorted({word for name in names for word in config.get('keywords', {}).get(name, [])},
                                    key=lambda s: (s.casefold(), s))
    return records


def query_terms(query, config):
    words = normalize(query).split()
    stops = {normalize(w) for w in config.get('stop_words', [])}
    aliases = {}
    for group in config.get('synonyms', []):
        variants = list(dict.fromkeys(normalize(a) for a in group['aliases']))
        for variant in variants:
            aliases[tuple(variant.split())] = variants
    longest = max((len(a) for a in aliases), default=1)
    terms, seen, index = [], set(), 0
    while index < len(words):
        for length in range(min(longest, len(words) - index), 0, -1):
            phrase = tuple(words[index:index + length])
            if phrase in aliases:
                break
        else:
            length, phrase = 1, (words[index],)
        original = ' '.join(phrase)
        if original not in stops:
            variants = aliases.get(phrase, [original])
            identity = tuple(sorted(variants))
            if identity not in seen:
                terms.append({'query': original, 'variants': [original] + [v for v in variants if v != original]})
                seen.add(identity)
        index += length
    return terms


def occurrence(phrase, text):
    if ' ' + phrase + ' ' in ' ' + text + ' ':
        return 1.0
    if ' ' not in phrase and len(phrase) >= 4 and any(w.startswith(phrase) for w in text.split()):
        return 0.7
    return 0.0


def score_record(record, terms):
    fields = {name: normalize(record.get(name)) for name in WEIGHTS}
    score, matches = 0.0, []
    for term in terms:
        candidates = [(WEIGHTS[field] * occurrence(variant, text) * (1.0 if variant == term['query'] else 0.8), field, variant)
                      for field, text in fields.items() for variant in term['variants']]
        value, field, variant = max(candidates)
        if value:
            score += value
            matches.append({'term': term['query'], 'matched': variant, 'field': field})
    if terms and len(matches) == len(terms):
        score += 10
    if matches and record.get('status') == 'PASS':
        score += 2
    return round(score, 2), matches


def search(records, query, config, *, category=None, record_type=None, stack=None, platform=None, status=None, match='all', limit=10):
    terms = query_terms(query, config)
    results = []
    for record in records:
        if category and category.casefold() not in [c.casefold() for c in record['categories']]:
            continue
        if record_type and record['record_type'] != record_type:
            continue
        if status and record.get('status') != status:
            continue
        context = normalize({k: record.get(k) for k in ('stack', 'tags', 'keywords', 'summary', 'description', 'reuse')})
        filters = [query_terms(value, config) for value in (stack, platform) if value]
        if any(not all(any(occurrence(v, context) for v in term['variants']) for term in values) for values in filters):
            continue
        score, matches = score_record(record, terms)
        if terms and ((match == 'all' and len(matches) != len(terms)) or not matches):
            continue
        results.append({**record, 'score': score, 'matches': matches})
    results.sort(key=lambda r: (-r['score'], r['full_name'].casefold(), r['key']))
    return results[:limit] if limit else results


def public_record(record):
    """Pek til kilden; komplette kildetekster trenger ikke følge hvert treff."""
    fields = ('key', 'record_type', 'full_name', 'title', 'summary', 'description', 'reuse', 'caveats',
              'categories', 'tags', 'keywords', 'aliases', 'html_url', 'profile_path', 'commit', 'origin',
              'status', 'stack', 'archived', 'current_public', 'license_spdx', 'usage', 'sources', 'score', 'matches')
    return {key: record[key] for key in fields if key in record}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('query', nargs='*', help='Behov, symptom eller nøkkelord på norsk eller engelsk.')
    parser.add_argument('--category', help='Eksakt kategori.')
    parser.add_argument('--type', choices=['repo', 'skill', 'solution'], dest='record_type')
    parser.add_argument('--stack', help='Avgrens med dokumenterte teknologiord, for eksempel three.js eller Unity.')
    parser.add_argument('--platform', help='Avgrens med dokumenterte plattformord.')
    parser.add_argument('--status', choices=['PASS', 'FAIL', 'UNVERIFIED'], help='Avgrens til løsningskort med denne statusen.')
    parser.add_argument('--match', choices=['all', 'any'], default='all', help='Alle behov må treffe som standard; any gir bredere søk.')
    parser.add_argument('--limit', type=int, default=10, help='Maksimalt antall treff; 0 viser alle.')
    parser.add_argument('--explain', action='store_true', help='Vis hvilke ord og felt som ga treff.')
    parser.add_argument('--list-categories', action='store_true')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--root', type=Path, default=ROOT, help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args.limit < 0:
        parser.error('--limit kan ikke være negativ')
    try:
        records = all_records(args.root)
        if args.list_categories:
            print('\n'.join(sorted({c for r in records for c in r['categories']}, key=str.casefold)))
            return 0
        results = search(records, ' '.join(args.query), configuration(args.root), category=args.category,
                         record_type=args.record_type, stack=args.stack, platform=args.platform,
                         status=args.status, match=args.match, limit=args.limit)
        if args.json:
            print(json.dumps([public_record(r) for r in results], ensure_ascii=False, indent=2))
        else:
            print(f'{len(results)} treff, rangert etter relevans')
            for record in results:
                state = f" [{record['status']}]" if record.get('status') else (' [ARKIVERT]' if record.get('archived') else '')
                print(f"\n{record['full_name']}{state} ({record['record_type']}, {record['score']:g} poeng)")
                print('  ' + flatten(record.get('summary') or record.get('description'))[:600])
                if record.get('reuse'):
                    print('  Gjenbruk: ' + flatten(record['reuse'])[:400])
                print(f"  {record['html_url']}\n  Profil: {record['profile_path']}")
                if len(record.get('sources', [])) > 1:
                    print(f"  Samme skillinnhold finnes i {len(record['sources'])} kildefiler.")
                if args.explain:
                    print('  Treff: ' + '; '.join(f"{m['term']} → {m['matched']} ({m['field']})" for m in record['matches']))
            if not results:
                print('Prøv færre behovsord eller --match any; null treff er ikke bevis på at ingen løsning finnes.')
        return 0
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        print(f'Kan ikke søke i biblioteket: {error}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""Bygg én reproduserbar søkeoversikt for agenter uten lokal terminal."""
import json
from pathlib import Path
from find import all_records, configuration, normalize, occurrence, public_record

ROOT = Path(__file__).resolve().parents[1]


def index_data(root):
    config = configuration(root)
    entries = []
    for record in all_records(root):
        entry = public_record(record)
        text = normalize({k: record.get(k) for k in ('full_name', 'title', 'summary', 'description', 'symptom', 'tags', 'keywords', 'stack')})
        entry['search_aliases'] = sorted({alias for group in config.get('synonyms', [])
                                          if any(occurrence(normalize(a), text) for a in group['aliases'])
                                          for alias in group['aliases']}, key=lambda s: (s.casefold(), s))
        entries.append(entry)
    entries.sort(key=lambda r: (r['record_type'], r['full_name'].casefold(), r['key']))
    return {'schema_version': 1, 'record_count': len(entries), 'records': entries}


def compact(text, limit=350):
    return ' '.join(str(text or '').split()).replace('|', '/')[:limit].rstrip()


def markdown(data):
    lines = ['# Samlet søkeoversikt', '',
             f"{data['record_count']} søkeoppføringer for løsningskort, repoer og unike skillinnhold. "
             'Like skillkopier er samlet; alle kildeplasseringene står i JSON-indeksen.', '',
             '[Start her](START_HER.md) · [JSON](data/search-index.json) · [Søkeord og synonymer](data/search-terms.json)', '',
             'Søk selektivt etter behov, symptomer og teknologi. Åpne kilden før gjenbruk. '
             'Nøkkelord og relaterte søkeord er hjelp til gjenfinning, ikke bevis på kompatibilitet. '
             'PASS gjelder dokumentert test i opphavet. Historiske oppføringer beholder opprinnelig kildeversjon.', '']
    for kind, title in [('solution', 'Løsningskort'), ('repo', 'Repoer og verktøy'), ('skill', 'Skills')]:
        lines += [f'## {title}', '']
        for record in data['records']:
            if record['record_type'] != kind:
                continue
            state = record.get('status') or ('ARKIVERT' if record.get('archived') else '')
            lines += [f"### {record['full_name']}", '', compact(record.get('summary') or record.get('description')), '']
            if state or record.get('stack'):
                lines += [f"Status: {state or 'Ikke runtime-testet her'}. Stack: {compact(record.get('stack')) or 'Les kilden'}.", '']
            if record.get('reuse'):
                lines += ['Mulig gjenbruk: ' + compact(record['reuse']), '']
            words = record.get('tags', []) + record.get('keywords', []) + record['search_aliases']
            words = sorted(set(words), key=lambda s: (s.casefold(), s))
            if words:
                lines += ['Søkeord: ' + ', '.join(words), '']
            lines += [f"[Profil eller kort]({record['profile_path']}) · [Kilde]({record['html_url']})", '']
    lines += ['Bygges med `python3 scripts/build_search_index.py`. Rediger kildenotater, skillmetadata og search-terms.json, og bygg på nytt.', '']
    return '\n'.join(lines)


def main():
    data = index_data(ROOT)
    (ROOT / 'data/search-index.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    (ROOT / 'SOK.md').write_text(markdown(data))
    print(f"Bygget {data['record_count']} søkeoppføringer i SOK.md og data/search-index.json")


if __name__ == '__main__':
    main()

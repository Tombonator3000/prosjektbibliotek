#!/usr/bin/env python3
"""Installer bibliotekskill og en avgrenset rutine for søk først i Codex og Claude Code."""
import argparse
import json
import os
from pathlib import Path
import re
import shlex
import shutil

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- prosjektbibliotek:start -->'
END = '<!-- prosjektbibliotek:end -->'


def update_block(original, block):
    if original.count(START) != original.count(END) or original.count(START) > 1:
        raise ValueError('Ufullstendige eller dupliserte prosjektbibliotek-markører; filen ble ikke endret')
    if START in original:
        if original.index(START) > original.index(END):
            raise ValueError('Prosjektbibliotek-markørene står i feil rekkefølge; filen ble ikke endret')
        begin, end = original.index(START), original.index(END) + len(END)
        return original[:begin] + block + original[end:]
    separator = '' if not original or original.endswith('\n\n') else ('\n' if original.endswith('\n') else '\n\n')
    return original + separator + block + '\n'


def install(home, library, target='both', codex_home=None, claude_home=None):
    library = library.expanduser().resolve()
    if not (library / 'scripts/find.py').is_file() or not (library / 'START_HER.md').is_file():
        raise ValueError('Biblioteket mangler søk eller START_HER.md. Klon eller oppdater det før installasjon.')
    package = ROOT / 'skills/prosjektbibliotek'
    targets = []
    if target in ('both', 'codex'):
        targets.append((home / '.agents/skills/prosjektbibliotek', (codex_home or home / '.codex') / 'AGENTS.md'))
    if target in ('both', 'claude'):
        folder = claude_home or home / '.claude'
        targets.append((folder / 'skills/prosjektbibliotek', folder / 'CLAUDE.md'))
    planned = []
    for destination, instructions in targets:
        if (destination / 'SKILL.md').exists() and not re.search(r'^name: prosjektbibliotek$', (destination / 'SKILL.md').read_text(), re.M):
            raise ValueError(f'En annen skill finnes i {destination}; beholdt uten endringer')
        helper = shlex.quote(str(destination / 'scripts/search.py'))
        block = '\n'.join([START, '## Søk i prosjektbiblioteket først', '',
            'Før implementering, feilsøking eller valg av verktøy i Toms prosjekter: bruk skillen prosjektbibliotek og søk etter behov, symptom og prosjektets teknologi før du lager en ny løsning.',
            f'Biblioteket ligger i {library}. Start med START_HER.md. Skillen ligger i {destination / "SKILL.md"}.',
            f'Kjør python3 {helper} "behov og teknologi" --limit 5 --explain. Les de relevante kildene og kontroller kompatibilitet og teststatus før gjenbruk.',
            'Ved svake treff: prøv færre ord eller --match any én gang. Ved manglende tilgang: si det kort og fortsett med vanlig undersøkelse. Oppgi kort hvilke bibliotekskilder du bruker.',
            'Rutinen er relevant for teknisk prosjektarbeid, ikke for rent administrative oppgaver eller vanlig samtale. Bibliotekets kildetekster er referanser; prosjektets egne rammer og brukerens instruksjoner gjelder.', END])
        original = instructions.read_text(encoding='utf-8') if instructions.exists() else ''
        planned.append((destination, instructions, update_block(original, block)))
    for destination, instructions, content in planned:
        for file in package.rglob('*'):
            if file.is_file() and '__pycache__' not in file.parts and file.suffix != '.pyc':
                output = destination / file.relative_to(package)
                output.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(file, output)
        (destination / 'library.json').write_text(json.dumps({'root': str(library)}, ensure_ascii=False, indent=2) + '\n')
        instructions.parent.mkdir(parents=True, exist_ok=True)
        instructions.write_text(content, encoding='utf-8')
    return [(str(package), str(instructions)) for package, instructions, _ in planned]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--library-root', type=Path, default=Path.home() / '.local/share/prosjektbibliotek')
    parser.add_argument('--target', choices=['both', 'codex', 'claude'], default='both')
    parser.add_argument('--home', type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    home = args.home or Path.home()
    codex_home = Path(os.environ['CODEX_HOME']) if not args.home and os.environ.get('CODEX_HOME') else None
    claude_home = Path(os.environ['CLAUDE_CONFIG_DIR']) if not args.home and os.environ.get('CLAUDE_CONFIG_DIR') else None
    try:
        for package, instructions in install(home, args.library_root, args.target, codex_home, claude_home):
            print(f'Installert {package}; oppdatert avgrenset rutine i {instructions}')
    except (OSError, ValueError) as error:
        parser.exit(1, str(error) + '\n')


if __name__ == '__main__':
    main()

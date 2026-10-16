#!/usr/bin/env python3
"""Finn den lokale bibliotekkopien og videresend søket uten nettverk eller skriving."""
import json
import os
from pathlib import Path
import subprocess
import sys


def library_root():
    package = Path(__file__).resolve().parents[1]
    configured = package / 'library.json'
    # Explicit configuration must not silently fall back to another library.
    if os.environ.get('PROSJEKTBIBLIOTEK_ROOT'):
        candidates = [Path(os.environ['PROSJEKTBIBLIOTEK_ROOT']).expanduser()]
    elif configured.exists():
        candidates = [Path(json.loads(configured.read_text())['root']).expanduser()]
    else:
        candidates = [package.parent.parent, Path.home() / '.local/share/prosjektbibliotek']
    for root in candidates:
        if (root / 'scripts/find.py').is_file() and (root / 'data/catalog.json').is_file():
            return root.resolve()
    raise FileNotFoundError('Ingen lokal bibliotekkopi funnet. Bruk GitHub-ruten i SKILL.md eller sett PROSJEKTBIBLIOTEK_ROOT.')


def main():
    try:
        root = library_root()
        return subprocess.run([sys.executable, str(root / 'scripts/find.py'), '--root', str(root), *sys.argv[1:]], check=False).returncode
    except (OSError, ValueError, KeyError) as error:
        print(str(error), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())

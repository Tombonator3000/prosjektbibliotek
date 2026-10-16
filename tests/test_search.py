"""Mål faktisk gjenfinning og trygg, gjentakbar installasjon; ingen nettverkskall."""
import json
import os
import hashlib
from pathlib import Path
import subprocess
import sys
import tempfile
import shutil
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import find
from build_skill_index import frontmatter
from setup_agents import install, update_block, START, END


class SearchQuality(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = find.all_records(ROOT)
        cls.config = find.configuration(ROOT)

    def test_real_needs_find_the_relevant_source_in_top_three(self):
        cases = [
            ('antialiasing', 'solution:three-r170-composer-msaa'),
            ('kantutjevning', 'solution:three-r170-composer-msaa'),
            ('anti-aliasing three.js', 'solution:three-r170-composer-msaa'),
            ('gloed', 'solution:bloom-terskel-over-en'),
            ('generer spriteark', 'personal:morbidium-spritesheets'),
            ('3D fra bilde', 'microsoft/TRELLIS.2'),
            ('image-to-3d', 'microsoft/TRELLIS.2'),
            ('decompilation', 'i12bp8/decomp.wtf'),
            ('shader stutter', 'BlueHeisenberg/SCSKiller'),
            ('webgl context lost', 'solution:webgl-kontekst-tapt'),
            ('hidden display grid', 'solution:hidden-attributt-med-display-grid'),
            ('Unreal MCP', 'EpicGames/unreal-engine-skills-for-claude-code-plugin'),
        ]
        for query, expected in cases:
            with self.subTest(query=query):
                hits = find.search(self.records, query, self.config, limit=3)
                keys = {r['key'] for r in hits} | {r['full_name'] for r in hits}
                self.assertIn(expected, keys)

    def test_relevant_title_beats_repeated_incidental_body_text(self):
        records = [
            {'key': 'noise', 'full_name': 'a', 'record_type': 'repo', 'categories': [], 'purpose': 'needle ' * 1000},
            {'key': 'relevant', 'full_name': 'z', 'record_type': 'solution', 'categories': [], 'title': 'needle'},
        ]
        self.assertEqual(find.search(records, 'needle', self.config)[0]['key'], 'relevant')

    def test_no_unrelated_substring_hits(self):
        record = {'key': 'community', 'full_name': 'community', 'record_type': 'repo', 'categories': []}
        self.assertEqual(find.search([record], 'Unity', self.config), [])

    def test_filters_limit_and_deterministic_order(self):
        kwargs = dict(record_type='solution', status='PASS', stack='three.js', limit=2)
        first = find.search(self.records, 'antialiasing', self.config, **kwargs)
        self.assertTrue(first)
        self.assertLessEqual(len(first), 2)
        self.assertTrue(all(r['record_type'] == 'solution' and r['status'] == 'PASS' for r in first))
        self.assertEqual(first, find.search(list(reversed(self.records)), 'antialiasing', self.config, **kwargs))
        windows = find.search(self.records, 'shader stutter', self.config, platform='Windows', limit=1)
        self.assertEqual(windows[0]['full_name'], 'BlueHeisenberg/SCSKiller')

    def test_strict_search_does_not_silently_drop_a_requirement(self):
        self.assertEqual(find.search(self.records, 'shader needlexyz987', self.config), [])
        self.assertTrue(find.search(self.records, 'shader needlexyz987', self.config, match='any'))

    def test_duplicate_skills_keep_all_source_locations(self):
        matches = [r for r in self.records if r['record_type'] == 'skill' and
                   any(s['repository'] == 'i12bp8/decomp.wtf' for s in r.get('sources', []))]
        self.assertEqual(len(matches), 1)
        self.assertIn('Tombonator3000/decomp.wtf', {s['repository'] for s in matches[0]['sources']})

    def test_existing_record_gets_current_notes(self):
        name = 'ahujasid/mcp-for-blender'
        actual = next(r for r in self.records if r['full_name'] == name)
        note = json.loads((ROOT / 'data/starred-notes.json').read_text())[name]
        self.assertEqual(actual['reuse'], note['reuse'])

    def test_query_without_arguments_still_supports_inventory(self):
        self.assertEqual(len(find.search(self.records, '', self.config, limit=0)), len(self.records))

    def test_catalog_build_does_not_depend_on_hash_seed(self):
        inputs = ['data/github.json', 'data/starred-notes.json', 'data/extra-notes.json',
                  'repoer/sentient-2026-09-12.json', 'repoer/coastal-webgpu-2026-09-20.json']
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in inputs:
                (root / name).parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / name, root / name)
            code = "import sys; from pathlib import Path; sys.path.insert(0, sys.argv[1]); import build_catalog; build_catalog.ROOT=Path(sys.argv[2]); build_catalog.main()"
            states = []
            for seed in ['1', '42']:
                subprocess.run([sys.executable, '-c', code, str(ROOT / 'scripts'), str(root)],
                               env={**os.environ, 'PYTHONHASHSEED': seed}, check=True, capture_output=True)
                files = [root / 'data/catalog.json', *sorted((root / 'repoer/prosjekter').glob('*.md'))]
                states.append([hashlib.sha256(p.read_bytes()).hexdigest() for p in files])
            self.assertEqual(states[0], states[1])

    def test_verifier_detects_stale_search_index(self):
        from verify import Check
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            shutil.copytree(ROOT / 'data', root / 'data')
            shutil.copy2(ROOT / 'SOK.md', root / 'SOK.md')
            check = Check(root)
            check.search_index()
            self.assertEqual(check.errors, [])
            data = json.loads((root / 'data/search-index.json').read_text())
            data['records'].pop()
            (root / 'data/search-index.json').write_text(json.dumps(data))
            check = Check(root)
            check.search_index()
            self.assertTrue(check.errors)


class MetadataAndSetup(unittest.TestCase):
    def test_frontmatter_reads_folded_and_quoted_descriptions_only(self):
        content = "---\nname: demo\ndescription: >-\n  Make sprite sheets\n  for games.\nmetadata:\n  secret: not-a-description\n---\nIgnore this body."
        self.assertEqual(frontmatter(content), {'name': 'demo', 'description': 'Make sprite sheets for games.'})
        self.assertEqual(frontmatter("---\nname: demo\ndescription: 'Don''t execute examples'\n---\nbody")['description'], "Don't execute examples")
        self.assertEqual(frontmatter('# No frontmatter'), {})

    def test_install_preserves_preferences_and_is_idempotent(self):
        with tempfile.TemporaryDirectory(prefix='bibliotek setup ') as folder:
            home = Path(folder)
            for path in [home / '.codex/AGENTS.md', home / '.claude/CLAUDE.md']:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('Existing user preferences.\n')
            install(home, ROOT)
            before = {p: p.read_bytes() for p in home.rglob('*') if p.is_file()}
            install(home, ROOT)
            after = {p: p.read_bytes() for p in home.rglob('*') if p.is_file()}
            self.assertEqual(before, after)
            self.assertTrue(all((home / p).read_text().startswith('Existing user preferences.\n')
                                for p in ['.codex/AGENTS.md', '.claude/CLAUDE.md']))
            for package in [home / '.agents/skills/prosjektbibliotek', home / '.claude/skills/prosjektbibliotek']:
                env = {**os.environ, 'PROSJEKTBIBLIOTEK_ROOT': str(ROOT)}
                output = subprocess.check_output([sys.executable, str(package / 'scripts/search.py'), 'antialiasing', '--limit', '1', '--json'], cwd=folder, env=env)
                self.assertEqual(json.loads(output)[0]['key'], 'solution:three-r170-composer-msaa')

    def test_broken_markers_stop_without_replacing_other_instructions(self):
        with self.assertRaises(ValueError):
            update_block('user preferences\n' + START, START + '\nnew\n' + END)
        with self.assertRaises(ValueError):
            update_block(END + '\nuser preferences\n' + START, START + '\nnew\n' + END)

    def test_invalid_explicit_library_does_not_fall_back(self):
        with tempfile.TemporaryDirectory() as folder:
            result = subprocess.run([sys.executable, str(ROOT / 'skills/prosjektbibliotek/scripts/search.py'), 'shader'],
                                    env={**os.environ, 'PROSJEKTBIBLIOTEK_ROOT': folder}, capture_output=True)
            self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    unittest.main()

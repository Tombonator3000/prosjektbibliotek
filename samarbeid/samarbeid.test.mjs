import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const script = fileURLToPath(new URL('./samarbeid.mjs', import.meta.url));
const realGit = spawnSync('sh', ['-c', 'command -v git'], { encoding: 'utf8' }).stdout.trim();

function fixture(t, { identity = true, fail = '' } = {}) {
	const root = fs.mkdtempSync(path.join(os.tmpdir(), 'natt-git-test-'));
	t.after(() => fs.rmSync(root, { recursive: true, force: true }));
	const repo = path.join(root, 'repo'), origin = path.join(root, 'origin.git'), bin = path.join(root, 'bin');
	fs.mkdirSync(repo); fs.mkdirSync(bin);
	const env = { ...process.env, GIT_CONFIG_GLOBAL: '/dev/null', GIT_CONFIG_SYSTEM: '/dev/null', GIT_TERMINAL_PROMPT: '0' };
	for (const name of Object.keys(env))
		if (/^GIT_(AUTHOR|COMMITTER|CONFIG_COUNT|CONFIG_KEY_|CONFIG_VALUE_)/.test(name)) delete env[name];
	function git(cwd, ...args) {
		const r = spawnSync(realGit, args, { cwd, env, encoding: 'utf8' });
		assert.equal(r.status, 0, r.stderr); return r.stdout.trim();
	}
	git(root, 'init', '--bare', origin);
	git(repo, 'init');
	fs.mkdirSync(path.join(repo, 'tools'));
	fs.writeFileSync(path.join(repo, 'tools/gpt_runde.sh'), '# fixture\n');
	fs.writeFileSync(path.join(repo, '.gitignore'), 'work/\n');
	git(repo, 'add', '.');
	git(repo, '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', 'commit', '-m', 'fixture');
	git(repo, 'remote', 'add', 'origin', origin);
	git(repo, 'branch', 'gpt-arbeid'); git(repo, 'push', 'origin', 'gpt-arbeid');
	if (identity) { git(repo, 'config', 'user.name', 'Fixture'); git(repo, 'config', 'user.email', 'fixture@example.invalid'); }
	const tree = path.join(repo, 'work/.gpt-gren');
	git(repo, 'worktree', 'add', tree, 'gpt-arbeid');
	const gitWrapper = `#!/usr/bin/env node
const {spawnSync}=require('node:child_process');
const a=process.argv.slice(2), fail=${JSON.stringify(fail)};
if ((fail==='preflight' && a[0]==='push') || (fail==='commit' && a[0]==='commit') || (fail==='push' && a[0]==='push' && !a.includes('--dry-run'))) {
 process.stderr.write('fixture: Git operation failed\\n');process.exit(128);
}
const r=spawnSync(${JSON.stringify(realGit)},a,{stdio:'inherit'});process.exit(r.status ?? 1);
`;
	fs.writeFileSync(path.join(bin, 'git'), gitWrapper, { mode: 0o755 });
	fs.writeFileSync(path.join(bin, 'codex'), `#!/bin/sh
if [ "$1" = --version ]; then echo fixture; exit 0; fi
cat >/dev/null
mkdir -p jobber/test
echo fixture >jobber/test/resultat.png
echo fixture >jobber/test/notat.md
echo 'LEVERT: test'
`, { mode: 0o755 });
	fs.writeFileSync(path.join(bin, 'claude'), `#!/bin/sh
if [ "$1" = --version ]; then echo fixture; exit 0; fi
touch ${JSON.stringify(path.join(root, 'claude-called'))}
echo 'INGEN OPPGAVE'
`, { mode: 0o755 });
	Object.assign(env, { PATH: bin + path.delimiter + process.env.PATH, CLAUDE_CMD: path.join(bin, 'claude'), CODEX_CMD: path.join(bin, 'codex') });
	const run = (...extra) => spawnSync(process.execPath, [script, '--repo', repo, '--spor', 'grafikk', '--timer', '0.25', '--loggmappe', path.join(root, 'logs'), ...extra], { env, encoding: 'utf8', timeout: 12000 });
	return { root, repo, tree, run, git };
}

test('manglende Git-identitet stopper før agentene starter', (t) => {
	const f = fixture(t, { identity: false }); const r = f.run();
	assert.equal(r.status, 1); assert.match(r.stdout, /Git mangler forfatternavn/);
	assert.equal(fs.existsSync(path.join(f.tree, 'jobber/test/resultat.png')), false);
});

test('manglende push-tilgang stopper før agentene starter', (t) => {
	const f = fixture(t, { fail: 'preflight' }); const r = f.run('--push');
	assert.equal(r.status, 1); assert.match(r.stdout, /Git-push virker ikke før start/);
	assert.equal(fs.existsSync(path.join(f.tree, 'jobber/test/resultat.png')), false);
});

test('commit-feil bevarer leveransen og sender den ikke videre til Claude', (t) => {
	const f = fixture(t, { fail: 'commit' }); const r = f.run();
	assert.equal(r.status, 1); assert.match(r.stdout, /Leveransen er beholdt i arbeidstreet/);
	assert.equal(fs.readFileSync(path.join(f.tree, 'jobber/test/resultat.png'), 'utf8'), 'fixture\n');
	assert.equal(f.git(f.tree, 'stash', 'list'), '');
	assert.equal(fs.existsSync(path.join(f.root, 'claude-called')), false);
});

test('push-feil etter commit stopper før Claude og beholder committen', (t) => {
	const f = fixture(t, { fail: 'push' }); const before = f.git(f.tree, 'rev-parse', 'HEAD');
	const r = f.run('--push');
	assert.equal(r.status, 1); assert.match(r.stdout, /Push av gpt-arbeid feilet/);
	assert.notEqual(f.git(f.tree, 'rev-parse', 'HEAD'), before);
	assert.equal(fs.existsSync(path.join(f.root, 'claude-called')), false);
});

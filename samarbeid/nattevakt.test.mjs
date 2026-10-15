import test from 'node:test';
import assert from 'node:assert/strict';
import { vurderLogg } from './nattevakt.mjs';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawn, spawnSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const hel = '- 20:50 Codex leverte 1: obj187_05.\n- 20:50 Pushet gpt-arbeid.\n- 21:00 Claude: RUNDE: godkjent 0, avvist 1\n';
test('overgang krever faktisk leveranse, push og Claude-runde', () => {
	assert.equal(vurderLogg(hel).klar, true);
	assert.equal(vurderLogg(hel.replace('Pushet gpt-arbeid.', '')).klar, false);
	assert.equal(vurderLogg(hel.replace('Claude: RUNDE:', 'Claude begynner:')).klar, false);
});
test('en tidligere vellykket runde skjuler ikke en senere feil', () => {
	for (const message of ['Commit i gpt-arbeid feilet', 'Push av hd-mod feilet', 'Codex feilet (tegn). Venter 5 minutter', 'Claude brukte mer enn 5 minutter og ble stoppet.']) {
		assert.equal(vurderLogg(hel + message).klar, false);
		assert.ok(vurderLogg(hel + message).feil);
	}
});
test('brukerens stopp avbryter; vaktens egen overgangsstopp kan fullføres', () => {
	assert.equal(vurderLogg(hel + 'Stoppet etter beskjed.').klar, false);
	assert.equal(vurderLogg(hel + 'Stoppet etter beskjed.', true).klar, true);
});

function lokalVakt(t, text, scriptExists = true, attachPid = null) {
	const root = fs.mkdtempSync(path.join(os.tmpdir(), 'nattevakt-test-'));
	t.after(() => fs.rmSync(root, { recursive: true, force: true }));
	fs.writeFileSync(path.join(root, 'prove.md'), text);
	const fake = path.join(root, 'natt.sh');
	if (scriptExists) fs.writeFileSync(fake, '#!/bin/sh\necho "$@" > start-args.txt\n', { mode: 0o755 });
	const c = { provePid: 2147483647, proveLogg: path.join(root, 'prove.md'), proveStdout: path.join(root, 'prove.txt'), repo: root, nattScript: fake, fokus: 'fixture', frist: new Date(Date.now() + 60000).toISOString(), loggmappe: root, statusfil: path.join(root, 'status.json'), vaktlogg: path.join(root, 'vakt.log'), nattStdout: path.join(root, 'natt.txt') };
	if (attachPid !== null) {
		c.nattPid = attachPid; c.nattLogg = path.join(root, 'natt.md');
		fs.writeFileSync(c.nattLogg, 'Ferdig. 1 grafikkrunde.\n');
	}
	const config = path.join(root, 'config.json'); fs.writeFileSync(config, JSON.stringify(c));
	const result = spawnSync(process.execPath, [fileURLToPath(new URL('./nattevakt.mjs', import.meta.url)), config], { timeout: 6000, encoding: 'utf8' });
	return { root, result, status: JSON.parse(fs.readFileSync(c.statusfil, 'utf8')) };
}

test('full overgang starter bare det lokale testskriptet med nattfristen', t => {
	const f = lokalVakt(t, hel);
	assert.equal(f.result.status, 0, f.result.stderr);
	assert.equal(f.status.status, 'FERDIG');
	assert.match(fs.readFileSync(path.join(f.root, 'start-args.txt'), 'utf8'), /--til 08:00 --fokus fixture/);
});

test('manglende kontroll starter ikke natt og setter STOPP', t => {
	const f = lokalVakt(t, 'Codex leverte 1: test.\nPushet gpt-arbeid.');
	assert.equal(f.result.status, 1);
	assert.equal(f.status.status, 'FEIL');
	assert.equal(fs.existsSync(path.join(f.root, 'start-args.txt')), false);
	assert.equal(fs.existsSync(path.join(f.root, 'STOPP')), true);
});

test('feil ved prosessstart gir synlig feilstatus', t => {
	const f = lokalVakt(t, hel, false);
	assert.equal(f.result.status, 1);
	assert.equal(f.status.status, 'FEIL');
	assert.match(f.status.message, /Kunne ikke starte natteskiftet/);
});

test('tilkobling til avsluttet natt starter ingen ekstra koordinator', t => {
	const f = lokalVakt(t, hel, true, 2147483647);
	assert.equal(f.result.status, 1, f.result.stderr);
	assert.equal(f.status.status, 'FEIL');
	assert.equal(fs.existsSync(path.join(f.root, 'start-args.txt')), false);
	assert.equal(fs.existsSync(path.join(f.root, 'STOPP')), true);
});

test('tilkobling følger bare den nye prosessen og ignorerer gammel feillogg', t => {
	const child = spawn('/bin/sh', ['-c', 'sleep 1'], { stdio: 'ignore' });
	t.after(() => { if (child.exitCode === null) child.kill(); });
	const f = lokalVakt(t, 'Codex feilet i det gamle løpet.\n', true, child.pid);
	assert.equal(f.result.status, 0, f.result.stderr);
	assert.equal(f.status.status, 'FERDIG');
	assert.equal(f.status.nightPid, child.pid);
	assert.equal(fs.existsSync(path.join(f.root, 'start-args.txt')), false);
	assert.match(fs.readFileSync(path.join(f.root, 'vakt.log'), 'utf8'), /Følger gjenopptatt nattløp/);
});

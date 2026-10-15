#!/usr/bin/env node
// Overfører en pågående prøvetur til natteskift etter én levert og kontrollert
// grafikkrunde. Overvåker deretter løpet uten å kjøre flere agenter selv.
import fs from 'node:fs';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';

export function vurderLogg(text, kontrollertStopp = false) {
	const feil = text.split('\n').find(line =>
		/\bfeilet\b|Stoppet på grunn av feil|Fire feil på rad|ble stoppet/.test(line) ||
		(!kontrollertStopp && /Stoppet etter beskjed/.test(line)));
	const levert = /Codex leverte [1-9]\d*:/m.test(text);
	const pushet = /Pushet gpt-arbeid\./m.test(text);
	const kontrollert = /Claude: RUNDE:/m.test(text);
	return { feil: feil || null, klar: !feil && levert && pushet && kontrollert };
}

function lever(pid) {
	try {
		const stat = fs.readFileSync(`/proc/${pid}/stat`, 'utf8');
		return stat.slice(stat.lastIndexOf(')') + 2).split(' ')[0] !== 'Z';
	} catch { return false; }
}
const les = p => { try { return fs.readFileSync(p, 'utf8'); } catch { return ''; } };
const vent = ms => new Promise(resolve => setTimeout(resolve, ms));

async function main(configPath) {
	if (!configPath) throw new Error('Bruk: node nattevakt.mjs KONFIGURASJON.json');
	const c = JSON.parse(fs.readFileSync(configPath, 'utf8'));
	const frist = Date.parse(c.frist);
	if (!Number.isFinite(frist)) throw new Error('Ugyldig frist');
	const stoppfil = path.join(c.loggmappe, 'STOPP');
	const folgNatt = c.nattPid !== undefined;
	let phase = folgNatt ? 'NATT' : 'PROVETUR', nightPid = folgNatt ? c.nattPid : null, ownStop = false;
	const skriv = (status, message) => {
		const row = { status, message, time: new Date().toISOString(), trialPid: c.provePid, nightPid };
		fs.writeFileSync(c.statusfil + '.tmp', JSON.stringify(row, null, 2) + '\n');
		fs.renameSync(c.statusfil + '.tmp', c.statusfil);
		fs.appendFileSync(c.vaktlogg, `${row.time} ${status}: ${message}\n`);
		console.log(`${status}: ${message}`);
	};
	const feil = message => {
		fs.writeFileSync(stoppfil, '');
		skriv('FEIL', message + ' Stoppfil satt. Ingen automatisk omstart.');
		process.exitCode = 1;
	};
	if (folgNatt) {
		if (!Number.isSafeInteger(nightPid) || nightPid <= 0 || !lever(nightPid)) {
			feil('Nattprosessen som skulle følges, kjører ikke.'); return;
		}
		if (!c.nattLogg || !fs.existsSync(c.nattLogg)) {
			feil('Gjenopptatt natt mangler sin egen nattlogg.'); return;
		}
		if (Date.now() >= frist || fs.existsSync(stoppfil)) {
			skriv('STOPPET', 'Følger ikke en gjenopptatt natt etter frist eller med stoppfil.'); return;
		}
		skriv(phase, 'Følger gjenopptatt nattløp. Starter ingen ekstra koordinator.');
	} else {
		skriv(phase, 'Følger pågående prøvetur. Natt starter etter levert, pushet og Claude-kontrollert grafikkrunde.');
		while (lever(c.provePid)) {
			if (Date.now() >= frist) { feil('Fristen er nådd før prøven ble ferdig.'); return; }
			if (fs.existsSync(stoppfil) && !ownStop) { skriv('STOPPET', 'Stoppfil fra bruker eller annet løp.'); return; }
			const r = vurderLogg(les(c.proveLogg) + '\n' + les(c.proveStdout), ownStop);
			if (r.feil) { feil(r.feil); return; }
			if (r.klar && !ownStop) {
				ownStop = true;
				fs.writeFileSync(stoppfil, '');
				skriv('PROVE_KLAR', 'En hel grafikkrunde er levert, pushet og kontrollert. Prøveturen avsluttes etter dette steget.');
			}
			await vent(2000);
		}
		const final = vurderLogg(les(c.proveLogg) + '\n' + les(c.proveStdout), ownStop);
		if (!final.klar) { feil(final.feil || 'Prøveturen sluttet uten komplett leveranse/push/kontroll.'); return; }
		if (Date.now() >= frist) { skriv('FERDIG', 'Fristen er nådd. Starter ikke en ny natt.'); return; }
		if (fs.existsSync(stoppfil) && !ownStop) { skriv('STOPPET', 'Starter ikke natt etter ekstern stopp.'); return; }
		const stream = fs.openSync(c.nattStdout, 'a');
		const args = [c.repo, '--til', '08:00', '--fokus', c.fokus];
		const child = spawn(c.nattScript, args, { cwd: c.repo, stdio: ['ignore', stream, stream], detached: true });
		try {
			await new Promise((resolve, reject) => { child.once('spawn', resolve); child.once('error', reject); });
		} catch (error) {
			fs.closeSync(stream); feil(`Kunne ikke starte natteskiftet: ${error.message}`); return;
		}
		nightPid = child.pid; child.unref(); fs.closeSync(stream);
		phase = 'NATT'; skriv(phase, 'Natteskift startet med grafikk og kode, til klokken 08:00.');
	}
	let nightLog = c.nattLogg || null;
	while (lever(nightPid)) {
		if (!nightLog) {
			const candidates = fs.readdirSync(c.loggmappe).filter(p => p.endsWith('.md'))
				.map(p => path.join(c.loggmappe, p)).filter(p => p !== c.proveLogg)
				.sort((a, b) => fs.statSync(b).mtimeMs - fs.statSync(a).mtimeMs);
			if (candidates.length && fs.statSync(candidates[0]).mtimeMs >= Date.now() - 15000) nightLog = candidates[0];
		}
		const r = vurderLogg(les(c.nattStdout) + '\n' + (nightLog ? les(nightLog) : ''));
		if (r.feil) { feil(r.feil); return; }
		await vent(2000);
	}
	const r = vurderLogg(les(c.nattStdout) + '\n' + (nightLog ? les(nightLog) : ''));
	if (r.feil) { feil(r.feil); return; }
	skriv(fs.existsSync(stoppfil) ? 'STOPPET' : 'FERDIG', 'Natteskiftet har avsluttet. Se nattloggen for leveranser og kontroller.');
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url))
	main(process.argv[2]).catch(error => { console.error(error.message); process.exitCode = 1; });

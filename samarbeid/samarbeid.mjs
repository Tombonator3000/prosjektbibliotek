#!/usr/bin/env node
// Natteskift: Claude Code og Codex (ChatGPT) jobber i samme repo og kontrollerer hverandre.
//
// To spor, etter tur:
//   grafikk  Codex lager de neste HD-jobbene fra ORDRE.md i grenen gpt-arbeid. Skriptet committer
//            leveransene. Claude kjører tools/gpt_runde.sh (kontroll, HD-mod, ny ORDRE.md med retur)
//            og ser selv på bildene. Avvisningene går tilbake til Codex i neste runde.
//   kode     Claude gjør en oppgave fra todo.md og committer på arbeidsgrenen. Codex går gjennom
//            endringene, og Claude retter.
//
// Ingen av agentene kjører med sperrene av: Claude går i permission-mode auto, og Codex i sin egen
// sandkasse (skriver bare i arbeidsmappen, uten nett og uten tilgang til .git).
// Se README.md i samme mappe.

import { spawn, spawnSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';

const HJELP = `Bruk: node samarbeid.mjs --repo MAPPE [valg]

  --repo MAPPE          repoet de skal jobbe i (må være rent, uten ucommittede endringer)
  --til HH:MM           stopp ved dette klokkeslettet, neste gang det kommer (standard 08:00)
  --timer N             stopp etter N timer (i stedet for --til)
  --spor LISTE          sporene etter tur, for eksempel grafikk,grafikk,kode
                        (standard grafikk,grafikk,kode når repoet har tools/gpt_runde.sh, ellers kode)
  --jobber N            grafikkjobber Codex tar per runde (standard 4)
  --runder N            maks rettinger per kodeoppgave etter kontroll (standard 2)
  --gren NAVN           arbeidsgrenen for koden (standard samarbeid/natt-ÅÅÅÅ-MM-DD)
  --fokus TEKST         ekstra beskjed til begge, for eksempel "bare punktene under ## Neste"
  --push                push arbeidsgrenen og gpt-arbeid etter hver runde
  --kall-minutter N     maks tid for ett kall til en agent (standard 90)
  --loggmappe MAPPE     hvor loggen skrives (standard ~/ki-samarbeid-logg)

Stopp underveis: Ctrl+C, eller lag filen STOPP i loggmappen (touch ~/ki-samarbeid-logg/STOPP).
Skriptet stopper da etter steget det holder på med.`;

// ---------- valg ----------

function lesValg(argv) {
	const v = {
		repo: null, til: '08:00', timer: null, spor: null, jobber: 4, runder: 2,
		gren: null, fokus: '', push: false, kallMinutter: 90,
		loggmappe: path.join(os.homedir(), 'ki-samarbeid-logg'),
	};
	for (let i = 0; i < argv.length; i++) {
		const a = argv[i];
		const neste = () => {
			if (i + 1 >= argv.length) stopp(`${a} trenger en verdi`);
			return argv[++i];
		};
		switch (a) {
			case '--repo': v.repo = path.resolve(neste()); break;
			case '--til': v.til = neste(); break;
			case '--timer': v.timer = Number(neste()); break;
			case '--spor': v.spor = neste().split(',').map((s) => s.trim()).filter(Boolean); break;
			case '--jobber': v.jobber = Number(neste()); break;
			case '--runder': v.runder = Number(neste()); break;
			case '--gren': v.gren = neste(); break;
			case '--fokus': v.fokus = neste(); break;
			case '--push': v.push = true; break;
			case '--kall-minutter': v.kallMinutter = Number(neste()); break;
			case '--loggmappe': v.loggmappe = path.resolve(neste()); break;
			case '-h': case '--help': console.log(HJELP); process.exit(0);
			default: stopp(`Ukjent valg: ${a}\n\n${HJELP}`);
		}
	}
	if (!v.repo) stopp(HJELP);
	const harGrafikk = fs.existsSync(path.join(v.repo, 'tools', 'gpt_runde.sh'));
	if (!v.spor) v.spor = harGrafikk ? ['grafikk', 'grafikk', 'kode'] : ['kode'];
	for (const s of v.spor) {
		if (!['grafikk', 'kode'].includes(s)) stopp(`Ukjent spor: ${s} (grafikk eller kode)`);
		if (s === 'grafikk' && !harGrafikk) stopp('Sporet grafikk trenger tools/gpt_runde.sh i repoet');
	}
	if (!v.gren) v.gren = `samarbeid/natt-${dato(new Date())}`;
	if (['main', 'master', 'gpt-arbeid', 'hd-mod', 'spilldata'].includes(v.gren)) stopp(`Arbeidsgrenen kan ikke være ${v.gren}`);
	v.frist = v.timer ? new Date(Date.now() + v.timer * 3600e3) : nesteKlokkeslett(v.til);
	v.tre = path.join(v.repo, 'work', '.gpt-gren');
	return v;
}

function nesteKlokkeslett(hhmm) {
	const m = /^(\d{1,2}):(\d{2})$/.exec(hhmm);
	if (!m) stopp('--til må være på formen HH:MM');
	const t = new Date();
	t.setHours(Number(m[1]), Number(m[2]), 0, 0);
	if (t <= new Date()) t.setDate(t.getDate() + 1);
	return t;
}

const to = (n) => String(n).padStart(2, '0');
const dato = (d) => `${d.getFullYear()}-${to(d.getMonth() + 1)}-${to(d.getDate())}`;
const klokke = (d) => `${to(d.getHours())}:${to(d.getMinutes())}`;
const vent = (ms) => new Promise((s) => setTimeout(s, ms));

function stopp(melding) {
	console.error(melding);
	process.exit(1);
}

// ---------- logg ----------

let loggfil = null;
let kjoremappe = null;

function logg(tekst) {
	const linje = `- ${klokke(new Date())} ${tekst}`;
	console.log(linje);
	if (loggfil) fs.appendFileSync(loggfil, linje + '\n');
}

// ---------- git ----------

function git(mappe, ...args) {
	const r = spawnSync('git', args, { cwd: mappe, encoding: 'utf8' });
	return { ok: r.status === 0, ut: (r.stdout || '').trim(), feil: (r.stderr || '').trim() };
}

const head = (mappe) => git(mappe, 'rev-parse', 'HEAD').ut;
const grenNa = (mappe) => git(mappe, 'branch', '--show-current').ut;
const skitten = (mappe) => git(mappe, 'status', '--porcelain').ut !== '';

// Endrede og nye filer, med stier fra roten av arbeidstreet.
function endredeFiler(mappe) {
	const r = spawnSync('git', ['status', '--porcelain', '-z', '--untracked-files=all'], { cwd: mappe, encoding: 'utf8' });
	return (r.stdout || '').split('\0').filter(Boolean).map((l) => l.slice(3));
}

// Legger ucommittede endringer i git stash i stedet for å slette dem.
function ryddOpp(mappe, grunn) {
	if (!skitten(mappe)) return;
	git(mappe, 'stash', 'push', '-u', '-m', `samarbeid: ${grunn}`);
	logg(`Ucommittede endringer lagt i git stash i ${path.relative(path.dirname(mappe), mappe) || mappe} (${grunn}).`);
}

function sikreGren(mappe, gren) {
	const na = grenNa(mappe);
	if (na === gren) return;
	logg(`Grenen i ${mappe} var "${na}". Går tilbake til ${gren}.`);
	ryddOpp(mappe, `etterlatt på ${na}`);
	const r = git(mappe, 'checkout', gren);
	if (!r.ok) throw new Error(`Kom ikke tilbake til ${gren}: ${r.feil}`);
}

function push(mappe, gren) {
	const p = git(mappe, 'push', '-u', 'origin', gren);
	logg(p.ok ? `Pushet ${gren}.` : `Push av ${gren} feilet: ${p.feil.split('\n').at(-1)}`);
}

// Samme arbeidstre for gpt-arbeid som tools/gpt_gren.sh bruker (work/.gpt-gren).
function sikreGrafikktre(v) {
	if (fs.existsSync(path.join(v.tre, '.git'))) {
		git(v.tre, 'fetch', '-q', 'origin', '+refs/heads/gpt-arbeid:refs/remotes/origin/gpt-arbeid');
		git(v.tre, 'merge', '-q', '--ff-only', 'origin/gpt-arbeid');
	} else {
		git(v.repo, 'worktree', 'prune');
		const f = git(v.repo, 'fetch', '-q', 'origin', '+refs/heads/gpt-arbeid:refs/remotes/origin/gpt-arbeid');
		if (!f.ok) throw new Error(`Fikk ikke hentet gpt-arbeid: ${f.feil}`);
		const w = git(v.repo, 'worktree', 'add', '-q', '-B', 'gpt-arbeid', v.tre, 'origin/gpt-arbeid');
		if (!w.ok) throw new Error(`Fikk ikke laget arbeidstre for gpt-arbeid: ${w.feil}`);
	}
	sikreGren(v.tre, 'gpt-arbeid');
	ryddOpp(v.tre, 'før grafikkrunden');
}

// ---------- agentene ----------

const KOMMANDO = {
	claude: process.env.CLAUDE_CMD || 'claude',
	codex: process.env.CODEX_CMD || 'codex',
};
const NAVN = { claude: 'Claude', codex: 'Codex' };

let kallnr = 0;
let aktivtBarn = null;

// Kjører én agent med prompten på stdin. Gir { ok, tekst }.
function kjorAgent(agent, prompt, hva, mappe, v) {
	kallnr++;
	const base = path.join(kjoremappe, `${to(kallnr)}-${agent}-${hva}`);
	const svarfil = base + '-svar.txt';
	const args = agent === 'claude'
		? ['-p', '--permission-mode', 'auto', '--output-format', 'text']
		: ['exec', '--sandbox', 'workspace-write', '-c', 'approval_policy="never"', '-o', svarfil, '-'];
	fs.writeFileSync(base + '-prompt.txt', prompt);

	const grense = Math.max(60e3, Math.min(v.kallMinutter * 60e3, v.frist - Date.now()));

	return new Promise((ferdig) => {
		const ut = fs.openSync(base + '-utskrift.txt', 'w');
		const barn = spawn(KOMMANDO[agent], args, { cwd: mappe, stdio: ['pipe', 'pipe', 'pipe'], detached: true });
		aktivtBarn = barn;
		let stdout = '';
		barn.stdout.on('data', (d) => { stdout += d; fs.writeSync(ut, d); });
		barn.stderr.on('data', (d) => fs.writeSync(ut, d));
		barn.stdin.on('error', () => {});
		barn.stdin.end(prompt);

		const vakt = setTimeout(() => {
			logg(`${NAVN[agent]} brukte mer enn ${Math.round(grense / 60e3)} minutter og ble stoppet.`);
			try { process.kill(-barn.pid, 'SIGTERM'); } catch {}
		}, grense);

		barn.on('error', (e) => {
			clearTimeout(vakt);
			aktivtBarn = null;
			fs.closeSync(ut);
			ferdig({ ok: false, tekst: `Kunne ikke starte ${KOMMANDO[agent]}: ${e.message}` });
		});
		barn.on('close', (kode) => {
			clearTimeout(vakt);
			aktivtBarn = null;
			fs.closeSync(ut);
			let tekst = stdout;
			if (agent === 'codex' && fs.existsSync(svarfil)) tekst = fs.readFileSync(svarfil, 'utf8');
			ferdig({ ok: kode === 0, tekst: tekst.trim() });
		});
	});
}

// Prøver på nytt ved feil (typisk bruksgrense), med økende ventetid.
async function kjorMedForsok(agent, prompt, hva, mappe, v) {
	const ventetider = [5, 15, 30];
	for (let forsok = 0; ; forsok++) {
		const r = await kjorAgent(agent, prompt, hva, mappe, v);
		if (r.ok) return r;
		const min = ventetider[forsok];
		if (min === undefined || Date.now() + min * 60e3 > v.frist || skalStoppe(v)) return r;
		logg(`${NAVN[agent]} feilet (${hva}). Venter ${min} minutter og prøver igjen. Se ${kjoremappe}.`);
		await vent(min * 60e3);
	}
}

function sisteLinje(tekst) {
	const linjer = tekst.split('\n').map((l) => l.trim().replace(/^[*`_]+|[*`_]+$/g, '')).filter(Boolean);
	return linjer.at(-1) || '';
}

// ---------- prompter ----------

function felles(v, mappe, gren) {
	return `Du jobber i ${mappe} på grenen ${gren}. Claude og Codex (ChatGPT) jobber sammen i natt og kontrollerer hverandre: Codex lager HD-grafikken og Claude kontrollerer den, Claude skriver koden og Codex kontrollerer den. Dette går automatisk til ${klokke(v.frist)}, og Tom følger ikke med før i morgen.

Les AGENTS.md (og CLAUDE.md hvis den finnes) og følg reglene der.

Faste regler i natt:
- Bli på grenen ${gren}. Ikke bytt gren, ikke lag PR og ikke flett noe. Ikke skriv om historikk (ingen reset --hard, rebase, amend eller force).
- Ikke endre noe utenfor repoet, og ikke installer noe globalt.
- Hopp over det som trenger Tom: godkjenning av stil, kjøp, innlogging, publisering utenfor repoets vanlige arbeidsflyt, testing med skjerm og lyd. Er noe uklart, skriv spørsmålet i notatet eller log.md og gå videre.
- Skriv uten emoji og tankestrek.${v.fokus ? `\n- Fra Tom: ${v.fokus}` : ''}`;
}

function promptTegn(v, ferdige) {
	return `${felles(v, v.tre, 'gpt-arbeid')}

Du er grafikeren. Les ORDRE.md, BESTILLING.md og AGENTS.md i denne mappen, og ta de neste ${v.jobber} jobbene i den rekkefølgen ORDRE.md sier (først det som er sendt i retur, så videre i GRAFIKKLISTE.md).${ferdige.length ? `\nDisse har du allerede levert i natt og skal ikke tas igjen før Claude har sendt dem i retur: ${ferdige.join(', ')}` : ''}

For hver jobb: se på originalen og stilankeret, lag bildet med bildeverktøyet etter prompt.txt, lagre det som resultat.png, kjør egenkontrollen (python3 verktoy/sjekk_leveranse.py ...) og gjør om det som får FEIL. Skriv notat.md, og for figurark fremdrift og rutekart under rapporter/ slik AGENTS.md sier.

Du kan ikke committe i denne sandkassen. Skriptet som kjører natten, committer resultat.png, notat.md, hovedark og rapporter/ for deg. Andre endringer blir ikke tatt med.

Siste linje i svaret skal være nøyaktig en av disse:
LEVERT: <jobbene, skilt med komma>
INGEN JOBBER
STOPPET: <grunn, for eksempel at bildeverktøyet ikke svarer eller grensen er nådd>`;
}

function promptGrafikkontroll(v, levert, commit) {
	return `${felles(v, v.repo, v.gren)}

Du kontrollerer grafikken. Codex har nettopp levert disse jobbene i gpt-arbeid (commit ${commit.slice(0, 10)} i work/.gpt-gren): ${levert.join(', ')}

1. Kjør tools/gpt_runde.sh. Den henter leveransene, kontrollerer dem, bygger HD-modden og sender ny ORDRE.md med retur til gpt-arbeid. Push til gpt-arbeid og hd-mod er en del av den vanlige runden og er greit.
2. Les work/gpt/RAPPORT.md.
3. Se selv på hver av de nye leveransene mot originalen (referanse.png og forhåndsvisningene), etter kravene i BESTILLING-CHATGPT.md: ingenting flyttet, lagt til eller fjernet, tekst bokstav for bokstav, riktig figur og samme størrelse i figurarkene. Det automatikken slapp gjennom og som er feil, avviser du på den måten repoet bruker (docs/gpt-avvisninger.csv, se memory.md) med grunn og forslag, og kjører runden igjen så returen kommer med i ORDRE.md.
4. Logg i log.md med dato, klokkeslett og navnet ditt, og commit endringene i repoet på ${v.gren}.

Siste linje: RUNDE: godkjent <antall>, avvist <antall>`;
}

function promptOppgave(v, tatt) {
	return `${felles(v, v.repo, v.gren)}

Les memory.md, todo.md og slutten av log.md. Velg én kodeoppgave fra todo.md som du kan gjøre ferdig alene på under en time.${tatt.length ? `\nDisse er allerede gjort eller forsøkt i natt:\n${tatt.map((t) => `- ${t}`).join('\n')}` : ''}

Gjør oppgaven, kjør testene repoet bruker, oppdater todo.md og log.md, og commit alt med en tydelig melding. Codex går gjennom endringene etterpå.

Siste linje i svaret skal være nøyaktig en av disse:
FERDIG: <oppgaven i en kort setning>
INGEN OPPGAVE`;
}

function promptKodekontroll(v, oppgave, base) {
	return `${felles(v, v.repo, v.gren)}

Du kontrollerer koden. Claude har nettopp gjort denne oppgaven: ${oppgave}
Endringene ligger i ${base.slice(0, 10)}..HEAD (se git log ${base}..HEAD og git diff ${base}..HEAD).

Gå kritisk gjennom endringene: feil, brudd på reglene i AGENTS.md, tester som mangler eller feiler, og ting som ikke er gjort slik log.md og commitmeldingen sier. Kjør testene selv hvis sandkassen tillater det. Ikke endre filer; du skal bare rapportere.

Skriv funnene som en kort punktliste med fil og linje der det passer. Siste linje skal være nøyaktig GODKJENT eller ENDRINGER.`;
}

function promptRetting(v, oppgave, funn) {
	return `${felles(v, v.repo, v.gren)}

Codex har gått gjennom arbeidet ditt med oppgaven «${oppgave}» og fant dette:

${funn}

Rett det du er enig i, kjør testene og commit. Skriv i log.md hva du rettet, og hva du lot være og hvorfor.
Siste linje: FERDIG: <hva du gjorde>`;
}

// ---------- sporene ----------

function skalStoppe(v) {
	return fs.existsSync(path.join(v.loggmappe, 'STOPP'));
}

function tidIgjen(v) {
	return v.frist - Date.now() > 10 * 60e3;
}

// Det Codex får levere i gpt-arbeid. Alt annet blir lagt i stash.
const LOVLIG_GRAFIKK = [
	/^jobber\/[^/]+\/(resultat\.png|notat\.md)$/,
	/^hovedark\/[^/]+(\.png|-notat\.md)$/,
	/^rapporter\//,
];

async function grafikkRunde(v, st) {
	sikreGrafikktre(v);
	logg(`Codex tegner (opptil ${v.jobber} jobber).`);
	const r = await kjorMedForsok('codex', promptTegn(v, st.levert), 'tegn', v.tre, v);
	sikreGren(v.tre, 'gpt-arbeid');
	const svar = sisteLinje(r.tekst);

	const filer = endredeFiler(v.tre);
	const lovlige = filer.filter((f) => LOVLIG_GRAFIKK.some((m) => m.test(f)));
	const andre = filer.filter((f) => !lovlige.includes(f));
	const jobber = [...new Set(lovlige.map((f) => /^jobber\/([^/]+)\/resultat\.png$/.exec(f)?.[1]).filter(Boolean))];
	const hovedark = lovlige.filter((f) => /^hovedark\/[^/]+\.png$/.test(f)).map((f) => path.basename(f, '.png'));
	const levert = [...jobber, ...hovedark];

	if (lovlige.length) {
		git(v.tre, 'add', '--', ...lovlige);
		const melding = `GPT (natt): ${levert.join(', ') || 'notater og rapporter'}`;
		const c = git(v.tre, 'commit', '-q', '-m', melding);
		if (!c.ok) logg(`Commit i gpt-arbeid feilet: ${c.feil}`);
	}
	if (andre.length) logg(`Codex endret ${andre.length} filer den ikke skal levere (${andre.slice(0, 5).join(', ')}${andre.length > 5 ? ' ...' : ''}). Ikke tatt med.`);
	ryddOpp(v.tre, 'filer Codex ikke skal levere');

	if (!r.ok && !levert.length) {
		logg(`Codex feilet. Siste linje: ${svar || '(tom)'}`);
		return 'feil';
	}
	if (/^INGEN JOBBER/i.test(svar) && !levert.length) {
		logg('Codex fant ingen flere grafikkjobber.');
		return 'ingen';
	}
	if (!levert.length) {
		logg(`Codex leverte ingen bilder. ${svar || ''}`.trim());
		return 'tom';
	}
	st.levert.push(...levert);
	logg(`Codex leverte ${levert.length}: ${levert.join(', ')}.`);
	if (v.push) push(v.tre, 'gpt-arbeid');

	if (!tidIgjen(v) || skalStoppe(v)) {
		logg('Tiden er ute før Claude fikk kontrollert. Leveransene ligger i gpt-arbeid til neste runde.');
		return 'ferdig';
	}
	logg('Claude kontrollerer grafikken og kjører gpt_runde.sh.');
	const k = await kjorMedForsok('claude', promptGrafikkontroll(v, levert, head(v.tre)), 'grafikkontroll', v.repo, v);
	sikreGren(v.repo, v.gren);
	ryddOpp(v.repo, 'ucommittet etter grafikkontrollen');
	logg(k.ok ? `Claude: ${sisteLinje(k.tekst) || '(uten oppsummering)'}` : 'Claude feilet under grafikkontrollen. Leveransene tas med i neste runde.');
	// Leveransene Claude har avvist, kommer tilbake i ORDRE.md og kan tas igjen.
	st.levert = [];
	return 'ferdig';
}

async function kodeOppgave(v, st) {
	const base = head(v.repo);
	logg('Claude velger og gjør en kodeoppgave.');
	const r = await kjorMedForsok('claude', promptOppgave(v, st.tatt), 'kode', v.repo, v);
	sikreGren(v.repo, v.gren);
	if (!r.ok) {
		logg(`Claude feilet. Siste linje: ${sisteLinje(r.tekst) || '(tom)'}`);
		ryddOpp(v.repo, 'etter feil hos Claude');
		return 'feil';
	}
	const svar = sisteLinje(r.tekst);
	if (/^INGEN OPPGAVE/i.test(svar)) {
		logg('Claude fant ingen kodeoppgave å gjøre alene.');
		ryddOpp(v.repo, 'etter INGEN OPPGAVE');
		return 'ingen';
	}
	const oppgave = svar.replace(/^FERDIG:\s*/i, '') || '(uten beskrivelse)';
	st.tatt.push(oppgave);
	ryddOpp(v.repo, 'ucommittet etter Claude');
	if (head(v.repo) === base) {
		logg(`Claude sier «${oppgave}», men committet ingenting.`);
		return 'feil';
	}
	logg(`Claude ferdig: ${oppgave} (${git(v.repo, 'rev-list', '--count', `${base}..HEAD`).ut} commit).`);

	for (let runde = 0; ; runde++) {
		if (skalStoppe(v) || !tidIgjen(v)) { logg('Stopper før kontrollen er ferdig.'); break; }
		logg('Codex kontrollerer koden.');
		const k = await kjorMedForsok('codex', promptKodekontroll(v, oppgave, base), 'kodekontroll', v.repo, v);
		sikreGren(v.repo, v.gren);
		ryddOpp(v.repo, 'Codex endret filer under kontrollen');
		if (!k.ok) { logg('Codex feilet under kontrollen. Oppgaven står ukontrollert.'); break; }
		if (sisteLinje(k.tekst).toUpperCase().startsWith('GODKJENT')) { logg('Codex: GODKJENT.'); break; }
		const antall = k.tekst.split('\n').filter((l) => /^\s*([-*]|\d+\.)\s/.test(l)).length;
		logg(`Codex: ENDRINGER (${antall} punkter).`);
		if (runde >= v.runder) { logg(`Ikke godkjent etter ${v.runder} rettinger. Funnene ligger i ${kjoremappe}.`); break; }
		logg(`Claude retter (runde ${runde + 1}).`);
		const f = await kjorMedForsok('claude', promptRetting(v, oppgave, k.tekst), 'retting', v.repo, v);
		sikreGren(v.repo, v.gren);
		ryddOpp(v.repo, 'ucommittet etter retting');
		if (!f.ok) { logg('Claude feilet under rettingen.'); break; }
	}
	if (v.push) push(v.repo, v.gren);
	return 'ferdig';
}

// ---------- hovedløkka ----------

async function main() {
	const v = lesValg(process.argv.slice(2));

	if (!git(v.repo, 'rev-parse', '--git-dir').ok) stopp(`${v.repo} er ikke et git-repo`);
	if (skitten(v.repo)) stopp(`${v.repo} har ucommittede endringer. Commit eller stash dem først (git status).`);
	for (const a of ['claude', 'codex']) {
		if (spawnSync(KOMMANDO[a], ['--version'], { encoding: 'utf8' }).status !== 0) {
			stopp(`Fant ikke ${KOMMANDO[a]}. Kjør installer.sh først.`);
		}
	}

	fs.mkdirSync(v.loggmappe, { recursive: true });
	try { fs.unlinkSync(path.join(v.loggmappe, 'STOPP')); } catch {}
	const start = new Date();
	const stempel = `${dato(start)}_${to(start.getHours())}${to(start.getMinutes())}`;
	kjoremappe = path.join(v.loggmappe, stempel);
	fs.mkdirSync(kjoremappe, { recursive: true });
	loggfil = path.join(v.loggmappe, `${stempel}.md`);
	fs.writeFileSync(loggfil, `# Samarbeid ${dato(start)} ${klokke(start)}\n\nRepo: ${v.repo}\nGren: ${v.gren}\nSpor: ${v.spor.join(', ')}\nStopper: ${dato(v.frist)} ${klokke(v.frist)}\nUtskrifter: ${kjoremappe}\n\n`);

	const fraGren = grenNa(v.repo);
	const finnes = git(v.repo, 'rev-parse', '--verify', '--quiet', `refs/heads/${v.gren}`).ok;
	const c = finnes ? git(v.repo, 'checkout', v.gren) : git(v.repo, 'checkout', '-b', v.gren);
	if (!c.ok) stopp(`Kunne ikke gå til grenen ${v.gren}: ${c.feil}`);
	const startHead = head(v.repo);
	logg(`Starter på ${v.gren} (${finnes ? 'fortsetter eksisterende gren' : `ny fra ${fraGren}`}). Stopper ${dato(v.frist)} ${klokke(v.frist)}.`);

	let avbrutt = false;
	process.on('SIGINT', () => {
		if (avbrutt) {
			if (aktivtBarn) try { process.kill(-aktivtBarn.pid, 'SIGTERM'); } catch {}
			process.exit(130);
		}
		avbrutt = true;
		console.log('\nStopper etter dette steget. Ctrl+C en gang til stopper med en gang.');
	});

	const st = { tatt: [], levert: [] };
	const teller = { grafikk: 0, kode: 0 };
	let spor = [...v.spor];
	let nr = 0, feilPaRad = 0, tommePaRad = 0, pauseGrafikkTil = 0;

	while (spor.length) {
		if (avbrutt || skalStoppe(v)) { logg('Stoppet etter beskjed.'); break; }
		if (!tidIgjen(v)) { logg('Tiden er ute.'); break; }
		const s = spor[nr % spor.length];
		nr++;
		if (s === 'grafikk' && Date.now() < pauseGrafikkTil) {
			if (spor.some((x) => x !== 'grafikk')) continue;
			await vent(Math.max(0, Math.min(pauseGrafikkTil, v.frist - 10 * 60e3) - Date.now()));
			continue;
		}

		let res;
		try {
			res = s === 'grafikk' ? await grafikkRunde(v, st) : await kodeOppgave(v, st);
		} catch (e) {
			logg(`Feil i sporet ${s}: ${e.message}`);
			res = 'feil';
		}

		if (res === 'ferdig') {
			teller[s]++; feilPaRad = 0;
			if (s === 'grafikk') tommePaRad = 0;
		} else if (res === 'ingen') {
			logg(`Sporet ${s} er tomt for i natt.`);
			spor = spor.filter((x) => x !== s);
			nr = 0;
		} else if (res === 'tom') {
			tommePaRad++;
			if (tommePaRad >= 2) {
				logg('Codex har ikke levert bilder to ganger på rad. Grafikken tar 30 minutters pause (bildeverktøyet kan ha nådd grensen).');
				pauseGrafikkTil = Date.now() + 30 * 60e3;
				tommePaRad = 0;
			}
		} else {
			feilPaRad++;
			if (feilPaRad >= 4) { logg('Fire feil på rad. Stopper så ikke natten går med til feil.'); break; }
		}
		if (!avbrutt && !skalStoppe(v)) await vent(20e3);
	}
	if (!spor.length) logg('Ingen av sporene har mer å gjøre.');

	const commits = git(v.repo, 'log', '--oneline', `${startHead}..${v.gren}`).ut;
	logg(`Ferdig. ${teller.grafikk} grafikkrunder og ${teller.kode} kodeoppgaver.`);
	fs.appendFileSync(loggfil, `\n## Kodecommits på ${v.gren}\n\n\`\`\`\n${commits || '(ingen)'}\n\`\`\`\n\nKodeoppgaver:\n${st.tatt.map((t) => `- ${t}`).join('\n') || '- (ingen)'}\n`);
	console.log(`\nLogg: ${loggfil}`);
}

main().catch((e) => {
	logg(`Stoppet på grunn av feil: ${e.message}`);
	process.exit(1);
});

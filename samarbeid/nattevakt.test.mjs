import test from 'node:test';
import assert from 'node:assert/strict';
import { vurderLogg } from './nattevakt.mjs';

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

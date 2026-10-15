#!/usr/bin/env bash
# Gjør klar Claude Code og Codex (ChatGPT) på Linux, så samarbeid.mjs kan bruke begge.
# Trygt å kjøre flere ganger: det som allerede er på plass, blir hoppet over.
set -euo pipefail

ok()   { echo "  ok: $*"; }
mangler() { echo "  MANGLER: $*"; FEIL=1; }
FEIL=0

echo "Sjekker verktøyene"
command -v git  >/dev/null && ok "git"  || mangler "git (sudo apt install git)"
if command -v node >/dev/null; then
	major=$(node -p 'process.versions.node.split(".")[0]')
	[ "$major" -ge 18 ] && ok "node $(node --version)" || mangler "node 18 eller nyere (har $(node --version))"
else
	mangler "node 18 eller nyere (https://nodejs.org eller sudo apt install nodejs npm)"
fi
if command -v bwrap >/dev/null; then
	ok "bubblewrap (sandkassen til Codex)"
else
	echo "  installerer bubblewrap, som Codex bruker som sandkasse (trenger sudo)"
	sudo apt-get install -y bubblewrap || mangler "bubblewrap (sudo apt install bubblewrap)"
fi
[ "$FEIL" = 0 ] || exit 1

echo "Claude Code"
if command -v claude >/dev/null; then
	ok "$(claude --version)"
else
	echo "  installerer Claude Code"
	curl -fsSL https://claude.ai/install.sh | bash
	export PATH="$HOME/.local/bin:$PATH"
	command -v claude >/dev/null || { echo "  Fant ikke claude etter installasjonen. Åpne en ny terminal og kjør skriptet igjen."; exit 1; }
fi

echo "Codex (ChatGPT)"
if command -v codex >/dev/null; then
	ok "$(codex --version)"
else
	echo "  installerer Codex med npm"
	if ! npm install -g @openai/codex 2>/dev/null; then
		echo "  npm trenger sudo for globale pakker her. Installerer i ~/.npm-global i stedet."
		npm config set prefix "$HOME/.npm-global"
		npm install -g @openai/codex
		export PATH="$HOME/.npm-global/bin:$PATH"
		grep -q npm-global "$HOME/.bashrc" 2>/dev/null || echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> "$HOME/.bashrc"
	fi
	ok "$(codex --version)"
fi

echo "Innlogging"
if codex login status >/dev/null 2>&1; then
	ok "Codex er logget inn"
else
	echo "  Codex er ikke logget inn. Velg «Sign in with ChatGPT» i nettleseren som åpnes."
	codex login
fi
if claude -p "svar bare ok" --output-format text >/dev/null 2>&1; then
	ok "Claude svarer"
else
	echo "  Claude er ikke logget inn. Starter claude; skriv /login, logg inn, og avslutt med /exit."
	claude
fi

echo
echo "Ferdig. Start natteskiftet med:"
echo "  $(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/natt.sh ~/sti/til/repoet"

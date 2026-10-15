#!/usr/bin/env bash
# Gjør klar Claude Code og Codex (ChatGPT) på Linux, så samarbeid.mjs kan bruke begge.
# Trygt å kjøre flere ganger: det som allerede er på plass, blir hoppet over.
# Trenger ikke sudo: Node, Claude og Codex legges i hjemmemappen hvis de mangler.
set -euo pipefail

ok()      { echo "  ok: $*"; }
mangler() { echo "  MANGLER: $*"; FEIL=1; }
FEIL=0

NODEMAPPE="$HOME/.local/share/node"
export PATH="$HOME/.local/bin:$NODEMAPPE/bin:$PATH"

# Stiene må også være med i nye terminaler.
legg_i_bashrc() {
	grep -qF "$1" "$HOME/.bashrc" 2>/dev/null || echo "$1" >> "$HOME/.bashrc"
}
legg_i_bashrc 'export PATH="$HOME/.local/bin:$HOME/.local/share/node/bin:$PATH"'

# Node LTS (22) fra nodejs.org, lagt i ~/.local/share/node. Sjekksummen kontrolleres.
installer_node() {
	case "$(uname -m)" in
		x86_64) arkitektur=x64 ;;
		aarch64|arm64) arkitektur=arm64 ;;
		*) mangler "node: ukjent arkitektur $(uname -m), installer Node 18 eller nyere selv"; return ;;
	esac
	local base=https://nodejs.org/dist/latest-v22.x
	local tmp
	tmp="$(mktemp -d)"
	curl -fsSL "$base/SHASUMS256.txt" -o "$tmp/SHASUMS256.txt"
	local fil
	fil="$(awk -v a="linux-$arkitektur.tar.gz" '$2 ~ a"$" {print $2}' "$tmp/SHASUMS256.txt")"
	[ -n "$fil" ] || { mangler "node: fant ikke pakken for linux-$arkitektur"; return; }
	echo "  laster ned $fil"
	curl -fsSL "$base/$fil" -o "$tmp/$fil"
	(cd "$tmp" && grep " $fil\$" SHASUMS256.txt | sha256sum -c --quiet -) || { mangler "node: sjekksummen stemmer ikke"; return; }
	rm -rf "$NODEMAPPE"
	mkdir -p "$NODEMAPPE"
	tar -xzf "$tmp/$fil" -C "$NODEMAPPE" --strip-components=1
	rm -rf "$tmp"
	hash -r
	ok "node $(node --version) i $NODEMAPPE"
}

echo "Sjekker verktøyene"
command -v git  >/dev/null && ok "git"  || mangler "git (installer med pakkebehandleren, for eksempel sudo dnf install git eller sudo apt install git)"
command -v curl >/dev/null && ok "curl" || mangler "curl (installer med pakkebehandleren)"
[ "$FEIL" = 0 ] || exit 1

if command -v node >/dev/null && [ "$(node -p 'process.versions.node.split(".")[0]')" -ge 18 ]; then
	ok "node $(node --version)"
else
	echo "  Node 18 eller nyere mangler. Installerer Node 22 i hjemmemappen (uten sudo)."
	installer_node
fi
if command -v bwrap >/dev/null; then
	ok "bubblewrap (sandkassen til Codex)"
else
	echo "  bubblewrap mangler. Codex bruker sin egen kopi, men det er bedre å installere det:"
	echo "  sudo dnf install bubblewrap, sudo apt install bubblewrap eller sudo pacman -S bubblewrap"
fi
[ "$FEIL" = 0 ] || exit 1

echo "Claude Code"
if claude --version >/dev/null 2>&1; then
	ok "$(claude --version)"
else
	echo "  installerer Claude Code"
	curl -fsSL https://claude.ai/install.sh | bash
	hash -r
	command -v claude >/dev/null || { echo "  Fant ikke claude etter installasjonen. Åpne en ny terminal og kjør skriptet igjen."; exit 1; }
	ok "$(claude --version)"
fi

echo "Codex (ChatGPT)"
if codex --version >/dev/null 2>&1; then
	ok "$(codex --version)"
else
	echo "  installerer Codex med npm"
	# --force rydder opp etter en installasjon som ble avbrutt
	if ! npm install -g --force @openai/codex 2>/dev/null; then
		echo "  npm trenger sudo for globale pakker her. Installerer i ~/.npm-global i stedet."
		npm config set prefix "$HOME/.npm-global"
		npm install -g --force @openai/codex
		export PATH="$HOME/.npm-global/bin:$PATH"
		legg_i_bashrc 'export PATH="$HOME/.npm-global/bin:$PATH"'
	fi
	hash -r
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
	echo "  Claude er ikke logget inn. Starter claude; logg inn (eller skriv /login), og avslutt med /exit."
	claude
fi

echo
echo "Ferdig. Prøv natteskiftet en time mens du ser på:"
echo "  $(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/natt.sh ~/Sam-Max-HD --timer 1 --jobber 1"

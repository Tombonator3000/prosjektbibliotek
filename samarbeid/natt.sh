#!/usr/bin/env bash
# Starter natteskiftet: Claude og Codex jobber etter tur i repoet til klokka 08:00 og pusher arbeidsgrenene.
# Maskinen holdes våken så lenge skriptet går.
#
#   ./natt.sh ~/Sam-Max-HD
#   ./natt.sh ~/Sam-Max-HD --til 07:00 --spor grafikk --fokus "bare figurarkene for Sam og Max"
#
# Stopp: Ctrl+C, eller touch ~/ki-samarbeid-logg/STOPP fra en annen terminal.
set -euo pipefail

HER="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="${1:?Bruk: natt.sh REPO [valg til samarbeid.mjs]}"
shift

# Det installer.sh legger i hjemmemappen, også når terminalen er åpnet før installasjonen.
export PATH="$HOME/.local/bin:$HOME/.local/share/node/bin:$HOME/.npm-global/bin:$PATH"

[ -d "$REPO/.git" ] || { echo "Fant ikke git-repoet $REPO. Skriv stien til mappen der du har klonet det."; exit 1; }
for v in node claude codex; do
	command -v "$v" >/dev/null || { echo "Fant ikke $v. Kjør $HER/installer.sh først."; exit 1; }
done

KOMMANDO=(node "$HER/samarbeid.mjs" --repo "$REPO" --til 08:00 --push "$@")

if command -v systemd-inhibit >/dev/null; then
	exec systemd-inhibit --what=sleep:idle --who=ki-samarbeid --why="Claude og Codex jobber" "${KOMMANDO[@]}"
else
	echo "Fant ikke systemd-inhibit. Slå av hvilemodus selv, ellers stopper arbeidet når maskinen sovner."
	exec "${KOMMANDO[@]}"
fi

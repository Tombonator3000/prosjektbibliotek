#!/usr/bin/env bash
# Starter natteskiftet: Claude og Codex jobber etter tur i repoet til klokka 08:00 og pusher arbeidsgrenen.
# Maskinen holdes våken så lenge skriptet går.
#
#   ./natt.sh ~/Sam-Max-HD
#   ./natt.sh ~/Sam-Max-HD --til 07:00 --utforer claude --fokus "bare punktene under ## Neste"
#
# Stopp: Ctrl+C, eller touch ~/ki-samarbeid-logg/STOPP fra en annen terminal.
set -euo pipefail

HER="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="${1:?Bruk: natt.sh REPO [valg til samarbeid.mjs]}"
shift

KOMMANDO=(node "$HER/samarbeid.mjs" --repo "$REPO" --til 08:00 --push "$@")

if command -v systemd-inhibit >/dev/null; then
	exec systemd-inhibit --what=sleep:idle --who=ki-samarbeid --why="Claude og Codex jobber" "${KOMMANDO[@]}"
else
	echo "Fant ikke systemd-inhibit. Slå av hvilemodus selv, ellers stopper arbeidet når maskinen sovner."
	exec "${KOMMANDO[@]}"
fi

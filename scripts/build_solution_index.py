#!/usr/bin/env python3
"""Bygg oversikten over løsningskort: data/losninger.json og LOSNINGER.md.

Et løsningskort er en Markdown-fil i losninger/<domene>/<id>.md med en enkel
nøkkel: verdi-blokk øverst og faste seksjoner under. Malen er losninger/MAL.md.
Kortene er de eneste kildefilene; JSON og LOSNINGER.md er generert herfra.
Kjør scripts/verify.py etterpå. Ingen nettverk eller installerte pakker.
"""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOMAINS = ["grafikk", "lyd", "testing", "ui", "bygg", "regler"]
DOMAIN_NAMES = {"grafikk": "Grafikk", "lyd": "Lyd og musikk", "testing": "Testing og verifikasjon",
                "ui": "Brukerflate", "bygg": "Bygg og levering", "regler": "Spillregler og systemer"}
STATUSES = ["PASS", "FAIL", "UNVERIFIED"]
REQUIRED_KEYS = ["id", "tittel", "domene", "stikkord", "stack", "status", "opphav", "dato", "agent", "lisens", "sist_sjekket"]
OPTIONAL_KEYS = ["offentlig_kontrollert", "se_ogsa"]
SECTIONS = ["Symptom", "Årsak", "Løsning", "Fallgruver", "Slik verifiseres det", "Bevis", "Brukt i"]
ORIGIN = re.compile(r"^(?P<repo>[\w.-]+/[\w.-]+)@(?P<commit>[0-9a-f]{40}):(?P<path>[^#\s]+)(?:#L(?P<line>\d+)(?:-L(?P<end>\d+))?)?$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def card_paths(root=ROOT):
    base = root / "losninger"
    if not base.is_dir():
        return []
    return sorted(p for p in base.glob("*/*.md") if p.is_file())


def parse(path, root=ROOT):
    """Les ett kort. Gir (kort, feil). Feilene er tekst som verify.py viser."""
    rel = path.relative_to(root).as_posix()
    text = path.read_text(encoding="utf-8")
    errors = []
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return None, [f"{rel}: mangler nøkkelblokken mellom --- og --- øverst"]
    meta = {}
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(f"{rel}: ugyldig linje i nøkkelblokken: {line}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key in meta:
            errors.append(f"{rel}: {key} står to ganger")
        meta[key] = value.strip()
    for key in REQUIRED_KEYS:
        if not meta.get(key):
            errors.append(f"{rel}: mangler {key}")
    for key in meta:
        if key not in REQUIRED_KEYS + OPTIONAL_KEYS:
            errors.append(f"{rel}: ukjent nøkkel {key}")
    body = m.group(2)
    heading = re.search(r"^# (.+)$", body, re.M)
    sections = {}
    parts = re.split(r"^## (.+)$", body, flags=re.M)
    for i in range(1, len(parts) - 1, 2):
        sections[parts[i].strip()] = parts[i + 1].strip()
    for name in SECTIONS:
        if not sections.get(name):
            errors.append(f"{rel}: mangler seksjonen «{name}» eller den er tom")
    bullets = lambda name: [l[2:].strip() for l in sections.get(name, "").splitlines() if l.startswith("- ")]
    origin = ORIGIN.match(meta.get("opphav", ""))
    card = {
        "id": meta.get("id", ""),
        "title": meta.get("tittel", ""),
        "domain": meta.get("domene", ""),
        "tags": [t.strip() for t in meta.get("stikkord", "").split(",") if t.strip()],
        "stack": meta.get("stack", ""),
        "status": meta.get("status", ""),
        "origin": meta.get("opphav", ""),
        "origin_repository": origin.group("repo") if origin else None,
        "origin_commit": origin.group("commit") if origin else None,
        "origin_path": origin.group("path") if origin else None,
        "origin_line": int(origin.group("line")) if origin and origin.group("line") else None,
        "date": meta.get("dato", ""),
        "agent": meta.get("agent", ""),
        "license": meta.get("lisens", ""),
        "checked": meta.get("sist_sjekket", ""),
        "public_checked": meta.get("offentlig_kontrollert") or None,
        "see_also": [t.strip() for t in meta.get("se_ogsa", "").split(",") if t.strip()],
        "path": rel,
        "heading": heading.group(1).strip() if heading else "",
        "symptom": sections.get("Symptom", ""),
        "solution": sections.get("Løsning", ""),
        "caveats": sections.get("Fallgruver", ""),
        "evidence": bullets("Bevis"),
        "used_in": bullets("Brukt i"),
        "text": body,
    }
    if card["id"] and card["id"] != path.stem:
        errors.append(f"{rel}: id {card['id']} er ikke likt filnavnet")
    if card["id"] and not SLUG.match(card["id"]):
        errors.append(f"{rel}: id skal bare ha små bokstaver, tall og bindestrek")
    if card["domain"] != path.parent.name:
        errors.append(f"{rel}: domene {card['domain']} er ikke likt mappa {path.parent.name}")
    if card["domain"] not in DOMAINS:
        errors.append(f"{rel}: ukjent domene {card['domain']} (bruk {', '.join(DOMAINS)})")
    if card["status"] not in STATUSES:
        errors.append(f"{rel}: status må være {', '.join(STATUSES)}")
    if card["status"] in ("PASS", "FAIL") and not card["evidence"]:
        errors.append(f"{rel}: {card['status']} krever minst ett punkt under «Bevis»")
    if not card["used_in"]:
        errors.append(f"{rel}: «Brukt i» trenger minst ett punkt")
    if not origin:
        errors.append(f"{rel}: opphav må ha formen eier/repo@<40 tegn commit>:sti#Llinje")
    for key in ("date", "checked"):
        if card[key] and not DATE.match(card[key]):
            errors.append(f"{rel}: datoen {card[key]} skal skrives ÅÅÅÅ-MM-DD")
    if card["public_checked"] and not DATE.match(card["public_checked"]):
        errors.append(f"{rel}: offentlig_kontrollert skal være en dato ÅÅÅÅ-MM-DD")
    if card["heading"] != card["title"]:
        errors.append(f"{rel}: overskriften skal være lik tittel")
    return card, errors


def load(root=ROOT):
    cards, errors = [], []
    for path in card_paths(root):
        card, problems = parse(path, root)
        errors += problems
        if card:
            cards.append(card)
    ids = [c["id"] for c in cards]
    for dup in sorted({i for i in ids if ids.count(i) > 1}):
        errors.append(f"losninger: id {dup} brukes av flere kort")
    cards.sort(key=lambda c: (DOMAINS.index(c["domain"]) if c["domain"] in DOMAINS else 99, c["id"]))
    return cards, errors


def index_data(cards):
    public = [{k: v for k, v in c.items() if k != "text"} for c in cards]
    return {"schema_version": 1,
            "scope": "Løsningskort fra Toms offentlige repoer. Status gjelder opphavet på datoen i kortet; "
                     "biblioteket kjører ikke kodene selv.",
            "domains": DOMAINS, "count": len(cards),
            "status_counts": {s: sum(1 for c in cards if c["status"] == s) for s in STATUSES},
            "cards": public}


def markdown(cards):
    lines = ["# Løsningskort", "",
             "Løste problemer og teknikker fra Toms egne spill, skrevet så neste prosjekt kan bruke dem i stedet for å finne dem på nytt. "
             "Hvert kort sier hva man ser, hvorfor det skjer, hva som løser det, hvordan det sjekkes og hvor det kommer fra.", "",
             f"**{len(cards)} kort.** "
             + " · ".join(f"{s}: {sum(1 for c in cards if c['status'] == s)}" for s in STATUSES), "",
             "[Startside](README.md) · [Mal for nye kort](losninger/MAL.md) · [JSON](data/losninger.json) · [Slik skriver du et kort](docs/BRUK.md#løsningskort)", "",
             "Status gjelder opphavsprosjektet på datoen i kortet: PASS er sjekket der, FAIL er prøvd og virket ikke, "
             "UNVERIFIED er funnet i kode eller notater uten at testen er sett. Biblioteket kjører ikke koden selv. "
             "Sjekk versjon, lisens og prosjektets rammer før du tar noe inn, og verifiser i ditt eget prosjekt.", "",
             "```sh", "python3 scripts/find.py msaa", "python3 scripts/find.py --category Løsningskort", "```", ""]
    for domain in DOMAINS:
        subset = [c for c in cards if c["domain"] == domain]
        if not subset:
            continue
        lines += [f"## {DOMAIN_NAMES[domain]}", "", "| Kort | Status | Stack | Opphav | Sist sjekket |", "|---|---|---|---|---|"]
        for c in subset:
            repo = c["origin_repository"] or "?"
            commit = (c["origin_commit"] or "")[:7]
            url = f"https://github.com/{repo}/blob/{c['origin_commit']}/{c['origin_path']}" + (f"#L{c['origin_line']}" if c["origin_line"] else "")
            cell = lambda s: str(s).replace("|", "/")
            lines.append(f"| [{cell(c['title'])}]({c['path']}) | {c['status']} | {cell(c['stack'])} | [{repo.split('/')[-1]}@{commit}]({url}) | {c['checked']} |")
        lines.append("")
    lines += ["## Nytt kort", "",
              "Kopier [malen](losninger/MAL.md) til `losninger/<domene>/<id>.md`, fyll ut, og kjør:", "",
              "```sh", "python3 scripts/build_solution_index.py", "python3 scripts/verify.py", "```", "",
              "Bare innhold fra offentlige repoer hører hjemme her. Denne siden er generert; endre kortene, ikke denne fila."]
    return "\n".join(lines) + "\n"


def main():
    cards, errors = load()
    if errors:
        print(f"FEIL i løsningskortene ({len(errors)}):", file=sys.stderr)
        for e in errors:
            print(f"- {e}", file=sys.stderr)
        return 1
    (ROOT / "data/losninger.json").write_text(json.dumps(index_data(cards), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "LOSNINGER.md").write_text(markdown(cards), encoding="utf-8")
    print(f"{len(cards)} løsningskort skrevet til data/losninger.json og LOSNINGER.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())

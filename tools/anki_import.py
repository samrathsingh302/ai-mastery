"""Push cloze cards straight into the running Anki via AnkiConnect (add-on 2055492159).

    python tools/anki_import.py <cards.tsv> [--deck "AI Mastery::00 session misses"]

Input: one note per line, `Text<TAB>Extra<TAB>tags` (3 columns) or `Text<TAB>tags`
(2 columns, no extra) — the tags column is always LAST. Text uses Anki cloze markup,
and ONLY {{c1::...}} is allowed (Samrath's law 26/08/2026: never c2/c3 — every blank
is c1 so all parts hide on ONE card, answered together like a Q->A card). Extra goes
into the Cloze type's Back Extra field (answer-side context/further info). Tags are
space-separated. Blank lines and lines starting with # are skipped.
Card style law: anki/CARD-RULES.md — read it before drafting cards. A line with no
cloze, or with any {{c2+::}}, fails the whole import loudly (no half-imports).
Note type = Anki's built-in Cloze (default formatting). The deck is created if
missing. Duplicates (same Text in the deck) are skipped, not doubled — safe to
re-run. Anki must be OPEN; a dead port fails loudly.

Written 26/08/2026 at Samrath's instruction; rewritten same day for the cloze-only
card law (was Front<TAB>Back basic cards), then again for the c1-only + Extra law.
"""

import argparse
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request

API = "http://127.0.0.1:8765"
MODEL = "Cloze"                     # Anki's built-in note type — default formatting by law
DEFAULT_DECK = "AI Mastery::00 session misses"
CLOZE_RE = re.compile(r"\{\{c\d+::")
NON_C1_RE = re.compile(r"\{\{c(?!1::)\d+::")


def call(action: str, **params):
    payload = json.dumps({"action": action, "version": 6, "params": params}).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(API, payload), timeout=10) as r:
            resp = json.load(r)
    except (urllib.error.URLError, OSError) as e:
        sys.exit(f"AnkiConnect unreachable ({e}) — is Anki open?")
    if resp.get("error"):
        sys.exit(f"AnkiConnect error on {action}: {resp['error']}")
    return resp["result"]


def escape(s: str) -> str:
    # Anki renders fields as HTML: unescaped < > eat content like (?P<year>...) or 2>&1.
    # Cards are plain text by law, so escape everything; cloze braces are unaffected.
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def parse_cards(path: pathlib.Path) -> list[tuple[str, str, list[str]]]:
    cards = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        parts = line.split("\t")
        text = parts[0].strip()
        extra = parts[1].strip() if len(parts) == 3 else ""
        tags = parts[-1].split() if len(parts) >= 2 else []
        if len(parts) > 3:
            sys.exit(f"{path.name}:{n}: {len(parts)} columns — format is Text<TAB>Extra<TAB>tags")
        if not text:
            sys.exit(f"{path.name}:{n}: empty card text")
        if not CLOZE_RE.search(text):
            sys.exit(f"{path.name}:{n}: no cloze marker — every card is cloze, see anki/CARD-RULES.md")
        if NON_C1_RE.search(text):
            sys.exit(f"{path.name}:{n}: c2+/c3+ cloze found — ONLY c1 is allowed (Samrath's law, see anki/CARD-RULES.md)")
        cards.append((escape(text), escape(extra), tags))
    if not cards:
        sys.exit(f"{path.name}: no cards found")
    return cards


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("file", type=pathlib.Path)
    ap.add_argument("--deck", default=DEFAULT_DECK)
    args = ap.parse_args()

    cards = parse_cards(args.file)
    call("createDeck", deck=args.deck)  # no-op if it already exists
    notes = [
        {
            "deckName": args.deck,
            "modelName": MODEL,
            "fields": {"Text": text, "Back Extra": extra},
            "tags": tags,
            "options": {"allowDuplicate": False, "duplicateScope": "deck"},
        }
        for text, extra, tags in cards
    ]
    result = call("addNotes", notes=notes)
    added = sum(1 for r in result if r is not None)
    skipped = len(result) - added
    print(f"{args.deck}: {added} added, {skipped} skipped as duplicates (of {len(cards)})")


if __name__ == "__main__":
    main()

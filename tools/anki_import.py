"""Push cloze cards straight into the running Anki via AnkiConnect (add-on 2055492159).

    python tools/anki_import.py <cards.tsv> [--deck "AI Mastery::00 session misses"]

Input: one note per line, `Text<TAB>tags` — Text uses Anki cloze markup ({{c1::...}}),
tags are space-separated and optional; blank lines and lines starting with # are skipped.
Card style law: anki/CARD-RULES.md — read it before drafting cards. Every line MUST
contain at least one cloze; a line without one fails the whole import loudly (no
half-imports). Note type = Anki's built-in Cloze (default formatting, per Samrath's rule).
The deck is created if missing. Duplicates (same Text in the deck) are skipped, not
doubled — safe to re-run. Anki must be OPEN; a dead port fails loudly.

Written 26/08/2026 at Samrath's instruction; rewritten same day for the cloze-only
card law (was Front<TAB>Back basic cards).
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


def parse_cards(path: pathlib.Path) -> list[tuple[str, list[str]]]:
    cards = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        text, _, tags = line.partition("\t")
        text = text.strip()
        if not text:
            sys.exit(f"{path.name}:{n}: empty card text")
        if not CLOZE_RE.search(text):
            sys.exit(f"{path.name}:{n}: no cloze marker — every card is cloze, see anki/CARD-RULES.md")
        # Anki renders fields as HTML: unescaped < > eat content like (?P<year>...) or 2>&1.
        # Cards are plain text by law, so escape everything; cloze braces are unaffected.
        text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        cards.append((text, tags.split()))
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
            "fields": {"Text": text, "Back Extra": ""},
            "tags": tags,
            "options": {"allowDuplicate": False, "duplicateScope": "deck"},
        }
        for text, tags in cards
    ]
    result = call("addNotes", notes=notes)
    added = sum(1 for r in result if r is not None)
    skipped = len(result) - added
    print(f"{args.deck}: {added} added, {skipped} skipped as duplicates (of {len(cards)})")


if __name__ == "__main__":
    main()

"""Push tab-separated cards straight into the running Anki via AnkiConnect (add-on 2055492159).

    python tools/anki_import.py <cards.tsv> [--deck "AI Mastery::00 session misses"]

Input: one card per line, `Front<TAB>Back` (same format as the module drills.md files);
blank lines and lines starting with # are skipped. The deck is created if missing.
Duplicates (same Front already in the deck) are skipped, not doubled — safe to re-run.
Anki must be OPEN; if the port is dead this fails loudly rather than half-importing.

Written 26/08/2026 at Samrath's instruction: /study-session imports its quiz-miss cards
itself — he only opens Anki and reviews.
"""

import argparse
import json
import pathlib
import sys
import urllib.error
import urllib.request

API = "http://127.0.0.1:8765"
MODEL = "AI Mastery basic"          # ships with the ai-mastery.apkg deck build
DEFAULT_DECK = "AI Mastery::00 session misses"


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


def parse_cards(path: pathlib.Path) -> list[tuple[str, str]]:
    cards = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if "\t" not in line:
            sys.exit(f"{path.name}:{n}: no tab separator — every card line is Front<TAB>Back")
        front, _, back = line.partition("\t")
        if not front.strip() or not back.strip():
            sys.exit(f"{path.name}:{n}: empty front or back")
        cards.append((front.strip(), back.strip()))
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
            "fields": {"Front": front, "Back": back},
            "options": {"allowDuplicate": False, "duplicateScope": "deck"},
        }
        for front, back in cards
    ]
    result = call("addNotes", notes=notes)
    added = sum(1 for r in result if r is not None)
    skipped = len(result) - added
    print(f"{args.deck}: {added} added, {skipped} skipped as duplicates (of {len(cards)})")


if __name__ == "__main__":
    main()

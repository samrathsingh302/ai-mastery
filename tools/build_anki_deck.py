"""Build the AI-Mastery Anki deck (.apkg) from every module's drills.md.

Each drills.md holds tab-separated `Front<TAB>Back` lines. This turns them into one
importable package with a subdeck per module, so reviews work fully offline.

    python tools/build_anki_deck.py

Re-running is safe: deck ids are derived from the module name and note GUIDs from the
question text, so a re-import UPDATES existing cards instead of duplicating them.
"""

import hashlib
import pathlib
import re
import sys

import genanki

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = pathlib.Path(__file__).resolve().parent.parent
OUT = REPO / "anki" / "ai-mastery.apkg"

# A skip on anything that is markdown furniture rather than a card.
FURNITURE = re.compile(r"^\s*$|^[#>|]|^\s*[-*]\s|^\s")


def stable_id(text: str) -> int:
    """genanki needs 31-bit ints; derive them so re-runs stay identical."""
    return int(hashlib.sha256(text.encode()).hexdigest()[:8], 16) % (1 << 31)


MODEL = genanki.Model(
    stable_id("ai-mastery-model-v1"),
    "AI Mastery basic",
    fields=[{"name": "Front"}, {"name": "Back"}],
    templates=[
        {
            "name": "Recall",
            "qfmt": '<div class="q">{{Front}}</div>',
            "afmt": '{{FrontSide}}<hr id="answer"><div class="a">{{Back}}</div>',
        }
    ],
    css=(
        ".card{font-family:Georgia,serif;font-size:20px;line-height:1.5;"
        "text-align:left;color:#222;background:#fdfdfb;padding:1.2em}"
        ".q{font-weight:600}.a{margin-top:.6em}"
        "hr#answer{border:none;border-top:1px solid #ccc;margin:1em 0}"
    ),
)


def parse(path: pathlib.Path) -> list[tuple[str, str]]:
    cards = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if "\t" not in line or FURNITURE.match(line):
            continue
        front, _, back = line.partition("\t")
        front, back = front.strip(), back.strip()
        if front and back:
            cards.append((front, back))
    return cards


def pretty(slug: str) -> str:
    """`11-nn-transformers-intuition` -> `11 nn transformers intuition`."""
    num, _, rest = slug.partition("-")
    return f"{num} {rest.replace('-', ' ')}"


def main() -> int:
    decks, total, empty = [], 0, []

    for drills in sorted(REPO.glob("modules/*/drills.md")):
        slug = drills.parent.name
        cards = parse(drills)
        if not cards:
            empty.append(slug)
            continue

        name = f"AI Mastery::{pretty(slug)}"
        deck = genanki.Deck(stable_id(name), name)
        for front, back in cards:
            note = genanki.Note(model=MODEL, fields=[front, back], tags=[f"module-{slug[:2]}"])
            note.guid = genanki.guid_for(front)  # dedupe on the question
            deck.add_note(note)

        decks.append(deck)
        total += len(cards)
        print(f"  {len(cards):3d}  {name}")

    if not decks:
        print("no cards found — nothing written")
        return 1

    OUT.parent.mkdir(exist_ok=True)
    genanki.Package(decks).write_to_file(OUT)

    print(f"\n{total} cards in {len(decks)} subdecks -> {OUT.relative_to(REPO)}")
    if empty:
        print(f"no drills yet (skipped): {', '.join(empty)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Mission 3 — regex on YOUR naming schemes. Compile once at module top (TEACH shows how)."""


def parse_handoff(filename):
    """Handoffs are named YYYY-MM-DD-HHmm-<slug>.md (slug = word chars/hyphens).
    Return {"date": "dd/mm/yyyy", "time": "HH:mm", "slug": slug} — note the date is
    CONVERTED to house format — or None if the name doesn't match exactly.
    parse_handoff("2026-08-04-0053-auto-catchup.md")
      -> {"date": "04/08/2026", "time": "00:53", "slug": "auto-catchup"}"""
    raise NotImplementedError("your code here")


def find_wikilinks(text):
    """Return every [[wiki-link]] target in text, in order, without the brackets.
    find_wikilinks("see [[dev/index]] and [[MODELS]]") -> ["dev/index", "MODELS"]"""
    raise NotImplementedError("your code here")

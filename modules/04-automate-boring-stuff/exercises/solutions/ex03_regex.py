"""Reference solution — mission 3."""
import re

HANDOFF = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(\d{2})(\d{2})-([\w-]+)\.md$")
WIKILINK = re.compile(r"\[\[([^\]]+)\]\]")


def parse_handoff(filename):
    m = HANDOFF.match(filename)
    if not m:
        return None
    year, month, day, hh, mm, slug = m.groups()
    return {"date": f"{day}/{month}/{year}", "time": f"{hh}:{mm}", "slug": slug}


def find_wikilinks(text):
    return WIKILINK.findall(text)

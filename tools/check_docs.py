"""Mechanical checks for HOW-IT-WORKS.md and the eli5\\ folder (chain 20261013-a-ai-mastery-eli5).

    python tools\\check_docs.py how-it-works
    python tools\\check_docs.py eli5 --modules 01-07
    python tools\\check_docs.py eli5 --modules 08-14 --sem1
    python tools\\check_docs.py all

Prints one summary line per part, `<mode>: N checks passed · M failed`, plus one
`FAIL  <what>: <why>` line per failure. Exit 0 only when nothing failed and at least one
check ran; exit 1 on any failure; exit 2 on a usage error (a mode or range that parses to
nothing never passes silently). Stdlib only; the repo root is found from this file's own
location, so the folder you run it from does not matter.

An absolute path under C:\\Users\\samra\\repos\\ai-mastery\\ is checked inside the tree this
file lives in (the same folder once merged; the worktree while a builder runs it).
"""

import re
import sys
from pathlib import Path

R = Path(__file__).resolve().parents[1]
REPO_PREFIX = "c:\\users\\samra\\repos\\ai-mastery"

HOW_H2S = [
    "## How it works",
    "## Everything you needed to learn",
    "## Where you are",
    "## A 6-hour day",
    "## Where Claude fits",
    "## Commands",
]
LANES = ["Python basics", "Java", "KRR", "Data Science", "Coding tests", "Group Project"]
CHECKER_CMD = "python modules\\03-cs50p-accelerated\\exercises\\check.py"
PATH_RE = re.compile(r"C:\\Users\\samra\\[^\s`\"'<>|)]+")

LABELS = ["**Like you're 5:**", "**The real words:**", "**See it:**"]
ELI5_WORD_CAP = 60

SEM1_TERMS = [
    # Java (COMP5911M)
    "Class and object (Java)", "Interface (Java)", "JUnit 5 test", "Test-driven development (TDD)",
    "Refactoring under tests", "Code smell", "SOLID", "Design pattern (GoF)", "Strategy pattern",
    "Observer pattern", "Factory pattern", "UML class diagram",
    # KRR (COMP5450M)
    "Proposition", "Predicate", "First-order logic (FOL)", "Quantifiers (for all, there exists)",
    "Knowledge base", "Prolog fact, rule and query", "Unification", "Backtracking",
    "Resolution proof", "Prover9",
    # Data Science (COMP5122M)
    "Clean, join, chart, findings", "Jupyter notebook",
    # Coding tests
    "Big-O", "Array and list", "Hash map", "Stack and queue", "Recursion (call stack)", "Two pointers",
    # Writing (COMP5530M)
    "LaTeX", "tectonic",
]

USAGE = (
    "usage: python tools\\check_docs.py how-it-works\n"
    "       python tools\\check_docs.py eli5 --modules AA-BB [--sem1]\n"
    "       python tools\\check_docs.py all"
)


class Tally:
    def __init__(self, mode):
        self.mode, self.passed, self.fails = mode, 0, []

    def check(self, ok, what, why):
        if ok:
            self.passed += 1
        else:
            self.fails.append(f"FAIL  {what}: {why}")

    def report(self):
        print(f"{self.mode}: {self.passed} checks passed · {len(self.fails)} failed")
        for line in self.fails:
            print(line)


def read(path):
    return path.read_text(encoding="utf-8") if path.is_file() else None


def module_dirs():
    return sorted(d.name for d in (R / "modules").iterdir() if d.is_dir() and re.match(r"\d{2}-", d.name))


def on_disk(raw):
    """A cited absolute path; ones under the repo resolve inside this tree."""
    if raw.lower() == REPO_PREFIX or raw.lower().startswith(REPO_PREFIX + "\\"):
        rest = [p for p in raw[len(REPO_PREFIX):].split("\\") if p]
        return R.joinpath(*rest)
    return Path(raw)


def how_it_works():
    t = Tally("how-it-works")
    text = read(R / "HOW-IT-WORKS.md")
    if text is None:
        t.check(False, "file", "HOW-IT-WORKS.md is missing")
        return t
    lines = {ln.rstrip() for ln in text.splitlines()}
    for h in HOW_H2S:
        t.check(h in lines, "heading", f"'{h}' not found as its own line")
    for name in module_dirs():
        t.check(name in text, "module", f"{name} is not named")
    paths = []
    for m in PATH_RE.finditer(text):
        p = m.group(0).rstrip(".,;:")
        if p not in paths:
            paths.append(p)
    for p in paths:
        t.check(on_disk(p).exists(), "path", f"{p} does not exist")
    for lane in LANES:
        t.check(lane in text, "lane", f"'{lane}' is not named")
    t.check(CHECKER_CMD in text, "command", f"'{CHECKER_CMD}' does not appear")
    return t


def glossary_terms():
    """{'01': [term, ...]} in glossary order, from the `- **term**` bullets under each `## Module NN`."""
    terms, current = {}, None
    for ln in (read(R / "GLOSSARY.md") or "").splitlines():
        if ln.startswith("## "):
            m = re.match(r"## Module (\d{2})\b", ln)
            current = m.group(1) if m else None
            if current:
                terms.setdefault(current, [])
        elif current and ln.startswith("- **"):
            end = ln.find("**", 4)
            if end > 4:
                terms[current].append(ln[4:end])
    return terms


def check_entries(t, rel, text):
    """Checks (3) and (4) for every `### ` entry; returns the headings found."""
    lines = text.splitlines()
    headings = []
    for i, ln in enumerate(lines):
        if not ln.startswith("### "):
            continue
        head = ln[4:].rstrip()
        headings.append(head)
        nxt = [x.rstrip() for x in lines[i + 1:] if x.strip()][:3]
        shape = len(nxt) == 3 and all(
            x.startswith(lab) and x[len(lab):].strip() for x, lab in zip(nxt, LABELS)
        )
        t.check(shape, "shape", f"{rel} '### {head}' is not followed by the three labelled lines, each non-empty")
        if nxt and nxt[0].startswith(LABELS[0]):
            words = len(nxt[0][len(LABELS[0]):].split())
            t.check(words <= ELI5_WORD_CAP, "words", f"{rel} '### {head}' Like you're 5 is {words} words (cap {ELI5_WORD_CAP})")
        else:
            t.check(False, "words", f"{rel} '### {head}' has no Like you're 5 line")
    return headings


def eli5(lo, hi, sem1):
    t = Tally("eli5")
    gloss = glossary_terms()
    targets = [(f"eli5\\{d}.md", R / "eli5" / f"{d}.md", gloss.get(d[:2], []))
               for d in module_dirs() if lo <= int(d[:2]) <= hi]
    if sem1:
        targets.append(("eli5\\sem1-theory.md", R / "eli5" / "sem1-theory.md", SEM1_TERMS))
    all_heads = []
    for rel, path, terms in targets:
        text = read(path)
        t.check(text is not None, "file", f"{rel} is missing")
        heads = check_entries(t, rel, text) if text is not None else []
        all_heads += heads
        for term in terms:
            t.check(term in heads, "term", f"{term} is not a '### ' heading in {rel}")
    dupes = sorted({h for h in all_heads if all_heads.count(h) > 1})
    t.check(not dupes, "repeat", f"headings repeat: {dupes}")
    return t, targets


def readme_links():
    t = Tally("readme")
    text = read(R / "eli5" / "README.md")
    files = sorted(p.name for p in (R / "eli5").glob("*.md") if p.name != "README.md") if (R / "eli5").is_dir() else []
    if text is None:
        t.check(False, "readme", "eli5\\README.md is missing")
        return t
    for name in files:
        linked = f"]({name})" in text or f"](./{name})" in text
        t.check(linked, "readme", f"eli5\\{name} is not linked from eli5\\README.md")
    return t


def parse_range(s):
    m = re.fullmatch(r"(\d{2})-(\d{2})", s or "")
    if not m or int(m.group(1)) > int(m.group(2)):
        return None
    return int(m.group(1)), int(m.group(2))


def usage(msg):
    print(f"{msg}\n{USAGE}", file=sys.stderr)
    return 2


def main(argv):
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    if not argv:
        return usage("no mode given")
    mode, rest = argv[0], argv[1:]
    if mode == "how-it-works" and not rest:
        parts = [how_it_works()]
    elif mode == "eli5":
        sem1 = "--sem1" in rest
        rest = [a for a in rest if a != "--sem1"]
        if len(rest) != 2 or rest[0] != "--modules":
            return usage("eli5 needs --modules AA-BB")
        rng = parse_range(rest[1])
        if rng is None:
            return usage(f"bad range '{rest[1]}' (want two-digit AA-BB, AA <= BB)")
        if not any(rng[0] <= int(d[:2]) <= rng[1] for d in module_dirs()):
            return usage(f"range {rest[1]} matches no modules\\ directory")
        parts = [eli5(*rng, sem1)[0]]
    elif mode == "all" and not rest:
        parts = [how_it_works(), eli5(1, 14, True)[0], readme_links()]
    else:
        return usage(f"unknown mode or extra arguments: {' '.join(argv)}")
    for p in parts:
        p.report()
    passed = sum(p.passed for p in parts)
    failed = sum(len(p.fails) for p in parts)
    if mode == "all":
        print(f"all: {passed} checks passed · {failed} failed")
    return 0 if failed == 0 and passed > 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

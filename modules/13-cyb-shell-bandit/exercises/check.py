#!/usr/bin/env python3
"""Shell gym for module 13 — builds a sandbox, then asks questions you answer
WITH THE SHELL (not by guessing).

  python check.py            build the sandbox + run the quiz
  python check.py --rebuild  wipe and rebuild the sandbox first

The sandbox lives in ./sandbox/ (gitignored). Open a Git Bash window there and
work it out with real commands; type each answer back here.
"""
import argparse
import hashlib
import random
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
BOX = HERE / "sandbox"

QUESTIONS = [
    ("How many files (not directories) are there anywhere under sandbox/?",
     "find . -type f | wc -l",
     lambda f: str(len(f["files"]))),
    ("How many of those are .log files?",
     "find . -name '*.log' | wc -l",
     lambda f: str(f["logs"])),
    ("What is the NAME (not path) of the single largest file?",
     "find . -type f -printf '%s %p\\n' | sort -rn | head -1   (or: ls -lS in each dir)",
     lambda f: f["biggest"]),
    ("How many lines in total across all .log files?",
     "cat $(find . -name '*.log') | wc -l   (or: find . -name '*.log' | xargs wc -l)",
     lambda f: str(f["logline_total"])),
    ("How many .log lines contain the word ERROR (case-sensitive)?",
     "grep -rc ERROR --include='*.log' . | ...   (simplest: grep -rh ERROR --include='*.log' . | wc -l)",
     lambda f: str(f["errors"])),
    ("Which single word appears most often across the .log files' first column "
     "(the level: INFO/WARN/ERROR)?",
     "grep -rho '^[A-Z]*' --include='*.log' . | sort | uniq -c | sort -rn | head -1",
     lambda f: f["top_level"]),
    ("There is exactly one file whose name starts with a dash. What is its name?",
     "ls -a  (to open it later you need ./-name or -- )",
     lambda f: f["dashfile"]),
    ("One file contains the word BANDIT exactly once. What is its filename?",
     "grep -rl BANDIT .",
     lambda f: f["needle"]),
]


def build(seed=7):
    """Build the sandbox. Deterministic: same seed → same tree, so a failed wipe
    is harmless (Windows locks a folder that a shell is sitting in — likely here,
    since the quiz tells you to cd into it)."""
    rng = random.Random(seed)
    if BOX.exists():
        try:
            shutil.rmtree(BOX)
        except (PermissionError, OSError):
            print("note: couldn't wipe sandbox/ (a shell is probably sitting in it) — "
                  "rewriting in place instead. Same seed, same tree, so answers are "
                  "unchanged.")
    for d in (BOX / "logs" / "archive", BOX / "notes", BOX / "empty"):
        d.mkdir(parents=True, exist_ok=True)

    facts = {"files": [], "logs": 0, "logline_total": 0, "errors": 0}
    levels = ["INFO", "WARN", "ERROR"]
    counts = {lv: 0 for lv in levels}

    def write(path, text):
        path.write_text(text, encoding="utf-8")
        facts["files"].append(path)

    for name, n in (("app.log", 40), ("worker.log", 25), ("archive/old.log", 18)):
        lines = []
        for i in range(n):
            lv = rng.choices(levels, weights=[6, 3, 2])[0]
            counts[lv] += 1
            lines.append(f"{lv} 2026-08-0{rng.randint(1,4)} event {i} in {name}")
        write(BOX / "logs" / name, "\n".join(lines) + "\n")
        facts["logs"] += 1
        facts["logline_total"] += n
    facts["errors"] = counts["ERROR"]
    facts["top_level"] = max(counts, key=counts.get)

    write(BOX / "notes" / "readme.md", "# sandbox\nnothing to see here\n")
    write(BOX / "notes" / "todo.md", "- [ ] learn find\n- [ ] learn grep\n")
    write(BOX / "notes" / "haystack.txt",
          "\n".join("filler " * 4 for _ in range(30)) + "\nthe word BANDIT hides here\n"
          + "\n".join("filler " * 4 for _ in range(20)) + "\n")
    facts["needle"] = "haystack.txt"
    write(BOX / "-oddly-named", "files whose names start with a dash break naive commands\n")
    facts["dashfile"] = "-oddly-named"
    write(BOX / "notes" / "big.dat", "x" * 9000 + "\n")
    facts["biggest"] = "big.dat"
    return facts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rebuild", action="store_true")
    args = ap.parse_args()
    if args.rebuild or not BOX.exists():
        facts = build()
        print(f"sandbox built at {BOX}")
    else:
        facts = build()  # deterministic: same seed, same tree
        print(f"sandbox at {BOX} (deterministic rebuild — your work is unaffected)")

    print("\nOpen Git Bash in the sandbox folder:  cd "
          f"{BOX.as_posix().replace('C:/', '/c/')}\n"
          "Answer each question using SHELL COMMANDS. Guessing defeats the point.\n")
    score = 0
    for i, (q, hint, want_fn) in enumerate(QUESTIONS, 1):
        want = want_fn(facts)
        got = input(f"Q{i}. {q}\n   answer: ").strip()
        if got.lower() == want.lower():
            print("   ✓\n")
            score += 1
        else:
            print(f"   ✗ expected: {want}\n   try: {hint}\n")
    print(f"Score: {score}/{len(QUESTIONS)} (target 6+)")
    print("Then go play Bandit — the sandbox is training wheels; Bandit is the road.")


if __name__ == "__main__":
    main()

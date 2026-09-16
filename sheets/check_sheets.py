#!/usr/bin/env python3
"""Checker for the daily study sheets in this folder (CAREER.md 7K, 16/09/2026).

  python sheets/check_sheets.py     -> run from the repo root (C:\\Users\\samra\\repos\\ai-mastery)

It checks two things and nothing else:

  1. every sheet (sheets/2026-*.md) carries the four fixed headings
     "## Today", "## Do", "## If stuck", "## Close";
  2. every backticked path in a sheet that starts "C:\\Users\\samra\\repos\\ai-mastery\\"
     or "modules\\" or "career\\" exists on disk, so a sheet can never send him to a
     file that is not there. A path followed by "(creates)" is exempt -- that marks a
     file the item itself makes, or an untracked one (career/drafts/ is gitignored).

Absolute "C:\\Users\\samra\\repos\\ai-mastery\\..." paths resolve against the repo this
script sits in, not the literal drive path, so the checker is correct in a worktree too.

Prints "N sheets checked, M paths verified" as its last line; exit 0 all green, exit 1
on any miss (each miss named with file, line and reason first).
"""
import re
import sys

if hasattr(sys.stdout, "reconfigure"):  # keep output printable on a cp1252 console
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

REQUIRED_HEADINGS = ("## Today", "## Do", "## If stuck", "## Close")
R_PREFIX = "c:\\users\\samra\\repos\\ai-mastery\\"
REL_PREFIXES = ("modules\\", "career\\")
TOKEN = re.compile(r"`([^`\n]+)`(\s*\(creates\))?")


def is_path(token):
    low = token.lower()
    return low.startswith(R_PREFIX) or low.startswith(REL_PREFIXES)


def resolve(token):
    rel = token[len(R_PREFIX):] if token.lower().startswith(R_PREFIX) else token
    return ROOT / rel.replace("\\", "/").rstrip("/")


def check(sheet):
    """Return (problems, verified_count) for one sheet."""
    problems = []
    verified = 0
    lines = sheet.read_text(encoding="utf-8").splitlines()
    for heading in REQUIRED_HEADINGS:
        if not any(line.strip() == heading for line in lines):
            problems.append("{0}: missing heading '{1}'".format(sheet.name, heading))
    for number, line in enumerate(lines, 1):
        for match in TOKEN.finditer(line):
            token, creates = match.group(1), match.group(2)
            if not is_path(token) or creates:
                continue
            if resolve(token).exists():
                verified += 1
            else:
                problems.append("{0}:{1}: path not found: {2}"
                                .format(sheet.name, number, token))
    return problems, verified


def main():
    sheets = sorted(HERE.glob("2026-*.md"))
    problems = []
    verified = 0
    for sheet in sheets:
        sheet_problems, sheet_verified = check(sheet)
        problems.extend(sheet_problems)
        verified += sheet_verified
    if not sheets:
        problems.append("no sheets found in {0}".format(HERE))
    for problem in problems:
        print("  MISS  " + problem)
    print("{0} sheets checked, {1} paths verified".format(len(sheets), verified))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

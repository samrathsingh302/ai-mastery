#!/usr/bin/env python3
"""Grader for the history gym. Inspects exercises/playground/'s git graph.

  python check.py     (from this folder, after building the playground repo)
"""
import subprocess
from pathlib import Path

PLAY = Path(__file__).resolve().parent / "playground"


def git(*args):
    r = subprocess.run(["git", *args], capture_output=True, text=True, cwd=PLAY)
    return r.returncode, r.stdout.strip()


def main():
    checks = []
    if not (PLAY / ".git").exists():
        print(f"TODO: no repo at {PLAY} yet — start at step 1 of ex01-history-gym.md")
        return

    rc, out = git("rev-list", "--count", "HEAD")
    n = int(out) if rc == 0 and out.isdigit() else 0
    checks.append((n >= 7, f"history has {n} commits (need ≥7: 3 main + idea + diverge + merge + mistake + revert)"))

    rc, merges = git("log", "--merges", "--oneline")
    checks.append((rc == 0 and bool(merges), "a REAL merge commit exists (two parents)"
                   if merges else "no merge commit found — step 5 (did it fast-forward? "
                   "main must move first, step 4)"))

    rc, tags = git("tag")
    checks.append(("v1" in tags.split(), 'tag "v1" exists' if "v1" in tags.split()
                   else 'tag "v1" missing — step 6'))

    rc, log = git("log", "--oneline")
    has_revert = "revert" in log.lower()
    checks.append((has_revert, 'a revert commit is in the log'
                   if has_revert else "no revert commit — step 7 (revert, don't reset: "
                   "history must SHOW the undo)"))

    checks.append((not (PLAY / "oops.md").exists(),
                   "oops.md correctly gone from the working tree"))

    rc, branches = git("branch", "--list", "feature")
    checks.append((bool(branches.strip()), "branch `feature` still exists"
                   if branches.strip() else "branch `feature` missing (fine ONLY if you did "
                   "the stretch deliberately)"))

    ok = sum(1 for c, _ in checks if c)
    for c, msg in checks:
        print(f"  {'PASS' if c else 'MISS'}  {msg}")
    print(f"\n{ok}/{len(checks)}."
          + (" Graph complete — you built history on purpose. Do the project next."
             if ok == len(checks) else " Re-read the missed step; the gym is repeatable "
             "(delete playground/ and rebuild — it's the point)."))


if __name__ == "__main__":
    main()

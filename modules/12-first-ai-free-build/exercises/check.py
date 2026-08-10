#!/usr/bin/env python3
"""Acceptance harness for the studylog build (module 12).

Point it at your finished tool:
    python check.py ../project/studylog.py

It runs your CLI as a black box in a temp directory — the way a marker would —
and reports which spec behaviours hold. It never reads your source, so it can't
be gamed by looking clever; and it can't grade design, which is why the RUBRIC
in TEACH.md is scored by you, not by this.

Run it only AFTER your own grading pass.
"""
import sys as _sys  # keep the tick/cross marks printable on a cp1252 console
if hasattr(_sys.stdout, "reconfigure"):
    _sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


def run(tool, args, cwd):
    env = dict(os.environ, STUDYLOG_DIR=str(cwd))
    r = subprocess.run([sys.executable, str(tool), *args], capture_output=True,
                       text=True, cwd=cwd, env=env, timeout=30)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return
    tool = Path(sys.argv[1]).resolve()
    if not tool.exists():
        print(f"no tool at {tool}")
        return
    checks = []
    with tempfile.TemporaryDirectory() as d:
        cwd = Path(d)
        rc, out = run(tool, [], cwd)
        checks.append((rc == 0 and len(out.strip()) > 0,
                       "no args → prints usage, exit 0"))

        rc, out = run(tool, ["add", "--module", "03", "--mins", "90",
                             "--note", "loops"], cwd)
        checks.append((rc == 0, "add: a valid entry is accepted (exit 0)"))

        rc, out = run(tool, ["add", "--module", "03", "--mins", "-5"], cwd)
        checks.append((rc != 0 and "traceback" not in out.lower(),
                       "add: negative mins rejected, non-zero exit, NO traceback"))

        rc, out = run(tool, ["add", "--module", "03", "--mins", "9000"], cwd)
        checks.append((rc != 0 and "traceback" not in out.lower(),
                       "add: absurd mins (>600) rejected cleanly"))

        rc, out = run(tool, ["today"], cwd)
        checks.append((rc == 0 and "90" in out, "today: shows the entry and its minutes"))

        rc, out = run(tool, ["week"], cwd)
        checks.append((rc == 0 and "90" in out, "week: aggregates the last 7 days"))

        rc, out = run(tool, ["add", "--module", "03", "--mins", "60", "--ai-free"], cwd)
        rc, out = run(tool, ["quota"], cwd)
        checks.append((rc == 0 and "%" in out, "quota: reports an AI-free percentage"))

        data = [p for p in cwd.rglob("*.json")]
        if data:
            data[0].write_text("{not json at all", encoding="utf-8")
            rc, out = run(tool, ["today"], cwd)
            checks.append(("traceback" not in out.lower(),
                           "corrupt data file → clear message, not a traceback"))
        else:
            checks.append((False, "no JSON data file found (does it honour STUDYLOG_DIR "
                                  "or write beside itself? — either is fine, but the "
                                  "corruption check needs to find it)"))

    ok = sum(1 for c, _ in checks if c)
    for c, msg in checks:
        print(f"  {'PASS' if c else 'FAIL'}  {msg}")
    print(f"\n{ok}/{len(checks)} spec behaviours.")
    print("Design, structure, tests and readability are NOT graded here — "
          "score those yourself in grading.md before you read this output again.")


if __name__ == "__main__":
    main()

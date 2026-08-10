#!/usr/bin/env python3
"""Setup verifier for module 02 (the tutor setup).

Run:  python check.py
Verifies the learning machine's parts. TODO lines are yours to do (they match
ledger items); PASS lines need nothing. Always exits 0 — this is a checklist,
not a gate.
"""
import sys as _sys  # keep the tick/cross marks printable on a cp1252 console
if hasattr(_sys.stdout, "reconfigure"):
    _sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import os
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]


def probe(cmd: list[str]) -> str | None:
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        if out.returncode == 0:
            return (out.stdout or out.stderr).strip().splitlines()[0]
    except Exception:
        pass
    return None


def main() -> None:
    print(__doc__)
    results: list[tuple[bool, str]] = []

    v = sys.version_info
    results.append((v >= (3, 10), f"Python {v.major}.{v.minor}.{v.micro} (need 3.10+)"))

    git = probe(["git", "--version"])
    results.append((git is not None, f"Git — {git or 'not found on PATH'}"))

    code = shutil.which("code")
    results.append((code is not None, "VS Code CLI ('code') on PATH"
                    if code else "VS Code CLI not on PATH (VS Code itself may still be installed)"))

    anki = Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "Anki" / "anki.exe"
    results.append((anki.exists(),
                    f"Anki desktop at {anki}" if anki.exists()
                    else "Anki desktop not found — ledger item 105 (apps.ankiweb.net)"))

    for rel in ("START-HERE.md", "journal.md", "GLOSSARY.md",
                "modules/02-tutor-setup/tutor-contract.md",
                "modules/02-tutor-setup/dojo.md"):
        p = REPO / rel
        results.append((p.exists(), rel if p.exists() else f"{rel} MISSING from repo"))

    print()
    todo = 0
    for ok, msg in results:
        print(f"  {'PASS' if ok else 'TODO'}  {msg}")
        todo += 0 if ok else 1
    print(f"\n{len(results) - todo}/{len(results)} green."
          + (" The machine is assembled — run tomorrow from START-HERE.md."
             if todo == 0 else " TODO items above are yours (or ledger-tracked)."))


if __name__ == "__main__":
    main()

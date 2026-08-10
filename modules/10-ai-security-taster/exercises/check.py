#!/usr/bin/env python3
"""Grader for ex01-classify.md (module 10).

Run: python check.py — for each scenario give the OWASP number (1-10) and the
trifecta legs present (any of P=private data, U=untrusted content, E=external
comms; type NONE for none). Controls are free-text — compare with solutions/.
"""
import sys as _sys  # keep the tick/cross marks printable on a cp1252 console
if hasattr(_sys.stdout, "reconfigure"):
    _sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ANSWERS = {
    1: (1, "PUE", "Indirect prompt injection: issue text obeyed as instruction. "
                  "Private data (keys) + untrusted content (issue) + push = complete trifecta."),
    2: (6, "NONE", "Excessive agency with no attacker: capability (whole-repo push, 5-minutely) "
                   "exceeds contract (one folder). Your ledger item 108."),
    3: (3, "NONE", "Supply chain: an installed instruction file steers every future session. "
                   "(It ENABLES a trifecta later; the risk itself is what you installed.)"),
    4: (10, "NONE", "Unbounded consumption: no attacker, no data loss — availability and cost."),
    5: (9, "U", "Misinformation acted on. Untrusted content is present; without private-data "
                "access or an exfil path the trifecta is incomplete."),
    6: (7, "NONE", "System prompt leakage: doctrine is extractable — treat CLAUDE.md as public-ish."),
    7: (1, "PUE", "Textbook indirect injection AND a complete trifecta: Drive/Gmail data, "
                  "attacker-written email, send-mail as the exfil channel."),
    8: (3, "NONE", "Supply chain again — the code you install runs with your rights, "
                   "no model involved."),
}
LEG = {"P": "private data", "U": "untrusted content", "E": "external comms"}


def main():
    print(__doc__)
    score = 0
    for n in sorted(ANSWERS):
        want_llm, want_legs, why = ANSWERS[n]
        while True:
            raw = input(f"\nScenario {n} — OWASP number (1-10)? ").strip()
            if raw.isdigit() and 1 <= int(raw) <= 10:
                got_llm = int(raw)
                break
            print("  a number 1-10 please")
        while True:
            legs = input("  trifecta legs present (letters from P/U/E, or NONE)? ").strip().upper()
            if legs == "NONE" or (legs and all(c in "PUE" for c in legs)):
                got_legs = "NONE" if legs == "NONE" else "".join(sorted(set(legs)))
                break
            print("  e.g. PUE, PU, U, or NONE")
        ok_llm = got_llm == want_llm
        ok_legs = got_legs == ("NONE" if want_legs == "NONE" else "".join(sorted(want_legs)))
        if ok_llm and ok_legs:
            score += 1
            print("  ✓ both right")
        else:
            if not ok_llm:
                print(f"  ✗ OWASP: LLM{want_llm:02d}, not LLM{got_llm:02d}")
            if not ok_legs:
                pretty = ("none" if want_legs == "NONE"
                          else ", ".join(LEG[c] for c in want_legs))
                print(f"  ✗ trifecta: {pretty}")
        print(f"    → {why}")
    print(f"\nScore: {score}/8 (target 6+)")
    print("Now write the controls and compare with solutions/ex01-answers.md — "
          "the control is the part that would have saved you.")


if __name__ == "__main__":
    main()

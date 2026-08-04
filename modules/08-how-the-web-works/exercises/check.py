#!/usr/bin/env python3
"""Self-checker for ex01-read-the-wire.md (module 08). Answers stored as hashes.
Run: python check.py — answer T/F or A/B/C/D per question."""
import hashlib

SALT = "ai-mastery-m08"
HASHES = {
    1: "7b4c31c40185a6d2b2824cf23f1b9c7702168a7460db8dd4628ab548faa02226",
    2: "caf17c49fdebea8aa9d46c3e0ac251e8ee2edd38b6dfec3c2696ee3de721e232",
    3: "dd2d13c8dbb515bc5a41aa613189833094f0df054541552636555fc31f521551",
    4: "8dd3e04cfecedc3047cf6ce560f7fb68c85c52eb036a97b4e0710cc06e87608c",
    5: "04cbd2c2517b289aa6f5a018de37c53aba4c20e45b5e676ad11ef3a79457053f",
    6: "f97dd9d44da42effda7eeaeaf2e06556b96d9fec7eeba952ba46a44be177d9d2",
    7: "295cd54651c9e3009d931b687fc9f0d5260b2cb440fbe51c1a938b4b483e0b93",
    8: "723e568906295ea058f4df73dc9fbbdfeca6c4dd0e59606e3e4a4c5ae70c451d",
    9: "f28e9578159cff2b37ab6837594ddcb12f4a9a1d729d2127729a40f38f65d797",
    10: "777b1bc2343f8437f0721eb0d81b36fa7934f894d69b2ad577e8f4ac40a908f1",
    11: "b782f6129ca35fa4430c008d430e084d96a17eaf1231291ece63cf81364d6602",
    12: "23ef25d76d2880cc98c9d39f8227755f39b5d61c91201c4d52730c62382c8292",
}
REVIEW = {
    1: "TEACH §6 (the 308 forward)", 2: "TEACH §5 status families / §6",
    3: "TEACH §6", 4: "TEACH §7 (the gate, observed)", 5: "TEACH §2 (whose addresses)",
    6: "TEACH §8 (the Age tell)", 7: "TEACH §5 (security trio)", 8: "TEACH §5 (CSP line)",
    9: "TEACH §5 (-I = HEAD)", 10: "TEACH §4 (HSTS)", 11: "TEACH §5+§7 (307 vs 308)",
    12: "TEACH §7 (servers trust no browser)",
}


def main():
    print(__doc__)
    score, misses = 0, []
    for n in sorted(HASHES):
        while True:
            a = input(f"Q{n:2d} — answer (T/F/A/B/C/D)? ").strip().upper()[:1]
            if a in "TFABCD":
                break
            print("  one of T, F, A, B, C, D please")
        if hashlib.sha256(f"{SALT}:{n}:{a}".encode()).hexdigest() == HASHES[n]:
            print("  ✓")
            score += 1
        else:
            print(f"  ✗ — review {REVIEW[n]}")
            misses.append(n)
    print(f"\nScore: {score}/12 (target 10+)")
    print("Clean — do the project trace." if not misses else
          "Re-read the flagged sections, re-run the live commands, retry tomorrow.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Self-checker for ex03-misconception-hunt.md (module 01).

Run:  python check.py
Answer T or F to each statement. Answers are stored as hashes, so reading
this file won't spoil you. Full explanations: solutions/ex03-answers.md
"""
import hashlib

SALT = "ai-mastery-m01"

# sha256(f"{SALT}:{question_number}:{T|F}") for the correct answer
HASHES = {
    1:  "db38ac71bfb260998f18bcaff605a15feee28903fd90f59752c2b53997dde2da",
    2:  "675af1cdb3edff1a4ece5ad955587a66840aa078958433a444573d8865edc016",
    3:  "5eabcf4a7be529724d95d2dd8638bcedbb4299d3cc6ab4563dd28e3ee87c7038",
    4:  "a231cb21bee6b966ce459ced464f770e087b69b94d737bb234a7b05a4996136f",
    5:  "8bcb0dd365f87007abd9bb87048baf770eab6c111da4bbc879b3ffb2fe83a81a",
    6:  "d124f570f8dcfb4da1ba0234efa9a68dd8ea702a0530ef260107c6eedc0f000c",
    7:  "208792d8feb3a8f387ef1175676cdef6f6a712d46ec903d478396a87c482af03",
    8:  "ff1e2ca29b4ec0b7c942bf9106719dae5ab733d82dc33e8fc819c7d32a5cb4f0",
    9:  "7ceec43ca31f5a63b632d98b57d55242594f4632a149ab55a09cd888e5255806",
    10: "5179f3deb5e7b26017d8dd46593707861058d4b0f4d2197968cdfc8aa885253c",
    11: "fcd93cc26a7731989248bacb1dc146424a02da6ff50eab6ee495baf1395df3c1",
    12: "1634e493f98d3326edd49d256397df3c0483c4a0db64ce331b5e808423e19130",
}

REVIEW = {
    1: "TEACH A1 (compression: vague recollection, not lookup)",
    2: "TEACH A2 (the difference is post-training, not data volume)",
    3: "TEACH A1 (tokens)",
    4: "TEACH A2 (no concept of truth — style + vague memory)",
    5: "TEACH A2 (context window beats weights)",
    6: "TEACH A2 (no knowledge of self)",
    7: "TEACH A2 (models need tokens to think)",
    8: "TEACH A2 (jagged intelligence)",
    9: "TEACH A3 (RL needs verifiable answers)",
    10: "TEACH A3 (RLHF optimises preferred-ness, not truth)",
    11: "TEACH B (Kernighan's law / the dividing line)",
    12: "TEACH C (it's a software engineering role)",
}


def h(n: int, ans: str) -> str:
    return hashlib.sha256(f"{SALT}:{n}:{ans}".encode()).hexdigest()


def main() -> None:
    print(__doc__)
    print("Statements are in ex03-misconception-hunt.md — have it open.\n")
    score, misses = 0, []
    for n in sorted(HASHES):
        while True:
            ans = input(f"Statement {n:2d} — T or F? ").strip().upper()[:1]
            if ans in ("T", "F"):
                break
            print("  just T or F, please")
        if h(n, ans) == HASHES[n]:
            print("  ✓ correct")
            score += 1
        else:
            print(f"  ✗ wrong — review {REVIEW[n]}")
            misses.append(n)
    print(f"\nScore: {score}/12  (target: 10+)")
    if misses:
        print("Re-read the sections above, retype the ideas from memory (ex02 move),")
        print("then re-run me tomorrow — spaced beats crammed.")
    else:
        print("Clean sweep. Move to the project/ folder.")


if __name__ == "__main__":
    main()

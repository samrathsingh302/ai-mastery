#!/usr/bin/env python3
"""Grade an eval run: programmatic checks first, then BLIND rubric grading.

  python grade.py [--dry-run]        (reads outputs/ or outputs-dry/)

Writes results.csv and prints the final table. Do not open the output files
before grading — blindness is the method.
"""
import argparse
import csv
import json
import random
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent


def norm(s):
    return " ".join(s.split()).strip().lower()


def score_exact(t, out):
    return 1 if norm(out) == norm(t["expected"]) else 0


def score_contains_all(t, out):
    return 1 if all(req.lower() in out.lower() for req in t["required"]) else 0


def score_code_tests(t, out):
    code = re.sub(r"^```[a-z]*\n?|```$", "", out.strip(), flags=re.M)
    runner = (code + "\n\nresults = []\n"
              + "\n".join(f"results.append({t['function']}({inp!r}) == {want!r})"
                          for inp, want in t["tests"])
              + "\nprint('OK' if all(results) else 'FAIL')")
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False,
                                     encoding="utf-8") as f:
        f.write(runner)
        path = f.name
    try:
        r = subprocess.run([sys.executable, path], capture_output=True,
                           text=True, timeout=10)
        return 1 if r.stdout.strip() == "OK" else 0
    except Exception:
        return 0
    finally:
        Path(path).unlink(missing_ok=True)


def score_regex_cases(t, out):
    pattern = out.strip().splitlines()[0].strip().strip("`'\"")
    try:
        rx = re.compile(pattern)
    except re.error:
        return 0
    ok_match = all(rx.fullmatch(c) for c in t["match"])
    ok_reject = all(not rx.fullmatch(c) for c in t["reject"])
    return 1 if (ok_match and ok_reject) else 0


PROGRAMMATIC = {"exact": score_exact, "contains-all": score_contains_all,
                "code-tests": score_code_tests, "regex-cases": score_regex_cases}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--seed", type=int, default=None, help="shuffle seed (testing only)")
    args = ap.parse_args()
    outdir = HERE / ("outputs-dry" if args.dry_run else "outputs")
    if not outdir.exists():
        print(f"no {outdir.name}/ yet — run run_eval.py first")
        return 1
    tasks = json.loads((HERE / "tasks.json").read_text(encoding="utf-8"))
    meta = json.loads((outdir / "meta.json").read_text(encoding="utf-8"))
    rng = random.Random(args.seed)

    read = lambda side, tid: (outdir / side / f"{tid}.txt").read_text(encoding="utf-8")
    rows = []

    print("=== programmatic tasks ===")
    for t in tasks:
        if t["type"] not in PROGRAMMATIC:
            continue
        fn = PROGRAMMATIC[t["type"]]
        sa, sb = fn(t, read("a", t["id"])), fn(t, read("b", t["id"]))
        rows.append((t["id"], t["type"], sa, sb))
        print(f"  {t['id']:20s} A={sa}  B={sb}")

    rubric_tasks = [t for t in tasks if t["type"] == "rubric"]
    if rubric_tasks:
        print("\n=== BLIND rubric round ===")
        print("Answers appear as 1/2, shuffled PER TASK. Score each 0-2 against the "
              "criteria. Mapping revealed at the end.\n")
    mapping = {}
    for t in rubric_tasks:
        first_is_a = rng.random() < 0.5
        order = ("a", "b") if first_is_a else ("b", "a")
        mapping[t["id"]] = order
        print(f"--- {t['id']} ---\nPROMPT: {t['prompt'][:180]}\nCRITERIA: {t['criteria']}\n")
        for label, side in zip(("1", "2"), order):
            print(f"[ANSWER {label}]\n{read(side, t['id'])}\n")
        scores = {}
        for label in ("1", "2"):
            while True:
                v = input(f"score for ANSWER {label} (0-2): ").strip()
                if v in ("0", "1", "2"):
                    scores[label] = int(v)
                    break
        sa = scores["1"] if order[0] == "a" else scores["2"]
        sb = scores["1"] if order[0] == "b" else scores["2"]
        rows.append((t["id"], "rubric", sa, sb))

    if rubric_tasks:
        print("\n=== reveal ===")
        for tid, order in mapping.items():
            print(f"  {tid}: ANSWER 1 was model {order[0].upper()}, "
                  f"ANSWER 2 was model {order[1].upper()}")

    a_name, b_name = meta["models"]["a"], meta["models"]["b"]
    with open(HERE / "results.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["task", "type", a_name, b_name])
        w.writerows(rows)

    ta, tb = sum(r[2] for r in rows), sum(r[3] for r in rows)
    maxs = sum(2 if r[1] == "rubric" else 1 for r in rows)
    print(f"\n| task | type | {a_name} | {b_name} |\n|---|---|---|---|")
    for tid, typ, sa, sb in rows:
        print(f"| {tid} | {typ} | {sa} | {sb} |")
    print(f"| **TOTAL** | /{maxs} | **{ta}** | **{tb}** |")
    print("\nresults.csv written. Now findings.md: biggest gap, biggest surprise, "
          "and what n=1 does NOT prove.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

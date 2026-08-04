#!/usr/bin/env python3
"""Run the 10-task eval against two models via the claude CLI (print mode).

  python run_eval.py --model-a haiku --model-b sonnet     # real run (20 CLI calls)
  python run_eval.py --dry-run                            # use fixtures/, no calls

Outputs land in outputs/<a|b>/<task-id>.txt (+ meta.json). Grade with grade.py.
"""
import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent


def ask(model, prompt):
    r = subprocess.run(["claude", "-p", prompt, "--model", model],
                       capture_output=True, text=True, timeout=300, shell=True)
    if r.returncode != 0:
        return f"[CLI ERROR rc={r.returncode}] {r.stderr.strip()[:300]}"
    return r.stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model-a", default="haiku")
    ap.add_argument("--model-b", default="sonnet")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    tasks = json.loads((HERE / "tasks.json").read_text(encoding="utf-8"))
    outdir = HERE / ("outputs-dry" if args.dry_run else "outputs")
    for side in ("a", "b"):
        (outdir / side).mkdir(parents=True, exist_ok=True)

    if args.dry_run:
        for side in ("a", "b"):
            for t in tasks:
                src = HERE / "fixtures" / side / f"{t['id']}.txt"
                shutil.copy(src, outdir / side / f"{t['id']}.txt")
        models = {"a": "fixture-model-A", "b": "fixture-model-B"}
        print(f"dry-run: fixtures copied for {len(tasks)} tasks x 2 models -> {outdir.name}/")
    else:
        models = {"a": args.model_a, "b": args.model_b}
        for side, model in models.items():
            print(f"\n=== model {side.upper()} = {model} ===")
            for t in tasks:
                print(f"  {t['id']} ...", end="", flush=True)
                out = ask(model, t["prompt"])
                (outdir / side / f"{t['id']}.txt").write_text(out, encoding="utf-8")
                print(" done")

    (outdir / "meta.json").write_text(json.dumps(
        {"models": models, "ran": datetime.now().strftime("%d/%m/%Y %H:%M")}, indent=2),
        encoding="utf-8")
    print(f"\nAll outputs in {outdir.name}/ — now: python grade.py"
          + (" --dry-run" if args.dry_run else ""))


if __name__ == "__main__":
    sys.exit(main())

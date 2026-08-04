#!/usr/bin/env python3
"""Self-checker for module 07. Runs against workouts-sample.json (real Hevy schema,
synthetic numbers).

  python check.py              -> your files      python check.py --solutions -> harness self-verify

Needs pandas (TEACH.md venv section). Without it, this prints a friendly TODO and exits.
"""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SAMPLE = HERE / "workouts-sample.json"

try:
    import pandas as pd  # noqa: F401
except ModuleNotFoundError:
    print("TODO first: pandas isn't installed in this Python.\n"
          "  py -m venv .venv && .venv\\Scripts\\activate && pip install pandas matplotlib\n"
          "(TEACH.md 'The venv' section walks it.)")
    sys.exit(0)


def load(name, from_solutions):
    folder = HERE / "solutions" if from_solutions else HERE
    spec = importlib.util.spec_from_file_location(name, folder / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    from_solutions = "--solutions" in sys.argv
    results = []
    try:
        ex01 = load("ex01_flatten", from_solutions)
        df = ex01.flatten_workouts(SAMPLE)
        results.append((len(df) == 24, f"flatten: 24 set-rows expected, got {len(df)}"))
        want_cols = {"date", "workout_title", "exercise", "set_type", "weight_kg", "reps", "volume"}
        results.append((want_cols.issubset(df.columns),
                        f"flatten: columns {sorted(want_cols - set(df.columns))} missing"
                        if not want_cols.issubset(df.columns) else "flatten: all columns present"))
        results.append((str(df["date"].dtype).startswith("datetime"),
                        f"flatten: date must be datetime, got {df['date'].dtype}"))
        results.append((float(df["volume"].sum()) == 9535.0,
                        f"flatten: total volume expected 9535.0, got {float(df['volume'].sum())}"))
    except NotImplementedError:
        print("  TODO  ex01_flatten not written yet — ex02 needs it, stopping here.")
        return
    except Exception as e:
        print(f"  FAIL  ex01_flatten: {type(e).__name__}: {e}")
        return

    try:
        ex02 = load("ex02_analyse", from_solutions)
        ev = ex02.exercise_volume(df)
        results.append((ev.index[0] == "Bench Press (Barbell)" and float(ev.iloc[0]) == 3140.0,
                        f"exercise_volume: top should be Bench Press (Barbell) 3140.0, got "
                        f"{ev.index[0]} {float(ev.iloc[0])}"))
        wv = ex02.weekly_volume(df)
        results.append((list(wv.index) == ["2026-W23", "2026-W24", "2026-W25"],
                        f"weekly_volume: weeks expected ['2026-W23','2026-W24','2026-W25'], got {list(wv.index)}"))
        results.append((float(wv["2026-W24"]) == 3012.5,
                        f"weekly_volume: 2026-W24 expected 3012.5, got {float(wv.get('2026-W24', 'missing'))}"))
        bs = ex02.best_set(df, "Bench Press (Barbell)")
        results.append((bs == (72.5, 5),
                        f"best_set bench: expected (72.5, 5) — tie on 72.5kg broken by reps — got {bs}"))
        rm = ex02.est_1rm(df, "Deadlift (Barbell)")
        results.append((rm == 128.3,
                        f"est_1rm deadlift: expected 128.3 (110x5 Epley beats 120x1), got {rm}"))
    except NotImplementedError:
        print("  (ex01 PASSES)  TODO  ex02_analyse not written yet.")
        for ok, msg in results:
            print(f"  {'PASS' if ok else 'FAIL'}  {msg}")
        return
    except Exception as e:
        results.append((False, f"ex02_analyse: {type(e).__name__}: {e}"))

    ok_n = sum(1 for ok, _ in results if ok)
    for ok, msg in results:
        print(f"  {'PASS' if ok else 'FAIL'}  {msg}")
    print(f"\n{'solutions' if from_solutions else 'your files'}: {ok_n}/{len(results)}")
    if ok_n == len(results) and not from_solutions:
        print("Taster complete — the project points this at your REAL 294 workouts.")


if __name__ == "__main__":
    main()

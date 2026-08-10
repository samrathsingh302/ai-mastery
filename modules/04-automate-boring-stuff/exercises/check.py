#!/usr/bin/env python3
"""Self-checker for module 04. Builds a SANDBOX file tree in a temp folder — your code
is tested there, never on real files (safety law 3).

  python check.py              -> test YOUR files
  python check.py ex03         -> one exercise
  python check.py --solutions  -> harness self-verify against reference solutions
"""
import sys as _sys  # keep the tick/cross marks printable on a cp1252 console
if hasattr(_sys.stdout, "reconfigure"):
    _sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import importlib.util
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, from_solutions):
    folder = HERE / "solutions" if from_solutions else HERE
    spec = importlib.util.spec_from_file_location(name, folder / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def make_tree(d):
    root = Path(d)
    (root / "sub").mkdir()
    (root / "a.md").write_text("x" * 10)
    (root / "b.PY").write_text("x" * 30)
    (root / "notes").mkdir()
    (root / "notes" / "c.md").write_text("x" * 50)
    (root / "sub" / "d.txt").write_text("x" * 20)
    (root / "README").write_text("no suffix")
    return root


def t_ex01(mod):
    with tempfile.TemporaryDirectory() as d:
        root = make_tree(d)
        got = mod.count_by_suffix(root)
        want = {".md": 2, ".py": 1, ".txt": 1, "": 1}
        assert got == want, f"count_by_suffix: expected {want!r}, got {got!r}"
        big = mod.biggest_file(root)
        assert big == ("c.md", 50), f'biggest_file: expected ("c.md", 50), got {big!r}'


def t_ex02(mod):
    with tempfile.TemporaryDirectory() as d:
        root = make_tree(d)
        got = mod.plan_moves(root)
        want = [("a.md", "md"), ("b.PY", "py")]
        assert got == want, f"plan_moves: expected {want!r}, got {got!r} (top-level files with a suffix only)"
    assert mod.unique_name(set(), "a.md") == "a.md"
    assert mod.unique_name({"a.md"}, "a.md") == "a-1.md"
    got = mod.unique_name({"a.md", "a-1.md"}, "a.md")
    assert got == "a-2.md", f'unique_name collision chain: expected "a-2.md", got {got!r}'


def t_ex03(mod):
    got = mod.parse_handoff("2026-08-04-0053-auto-catchup.md")
    want = {"date": "04/08/2026", "time": "00:53", "slug": "auto-catchup"}
    assert got == want, f"parse_handoff: expected {want!r}, got {got!r}"
    assert mod.parse_handoff("notes.md") is None, "non-handoff names must return None"
    assert mod.parse_handoff("2026-08-04-0053-auto catchup.md") is None, \
        "slug with a space must NOT match (anchor your pattern)"
    links = mod.find_wikilinks("see [[dev/index]] and [[MODELS]] ok")
    assert links == ["dev/index", "MODELS"], f"find_wikilinks: got {links!r}"


def t_ex04(mod):
    with tempfile.TemporaryDirectory() as d:
        csv_p = Path(d) / "hevy.csv"
        csv_p.write_text("Exercise,Weight,Reps\nSquat,100,5\nSquat,110,3\nBench,60,8\n",
                         encoding="utf-8")
        got = mod.hevy_summary(csv_p)
        want = {"Squat": {"sets": 2, "volume": 830.0}, "Bench": {"sets": 1, "volume": 480.0}}
        assert got == want, f"hevy_summary: expected {want!r}, got {got!r}"
        back = mod.write_json_report(got, Path(d) / "report.json")
        assert back == got, "write_json_report round-trip: parsed-back dict differs"


def t_ex05(mod):
    v = mod.python_version()
    want = ".".join(map(str, sys.version_info[:3]))
    assert v == want, f"python_version: expected {want!r}, got {v!r}"
    repo_root = HERE.parents[2]
    real = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                          capture_output=True, text=True, cwd=repo_root)
    if real.returncode == 0:
        got = mod.git_head_short(repo_root)
        assert got == real.stdout.strip(), \
            f"git_head_short: expected {real.stdout.strip()!r}, got {got!r}"
    with tempfile.TemporaryDirectory() as d:
        assert mod.git_head_short(d) is None, "non-repo folder must return None"


TESTS = {"ex01_paths": t_ex01, "ex02_organise": t_ex02, "ex03_regex": t_ex03,
         "ex04_data": t_ex04, "ex05_subprocess": t_ex05}


def main():
    from_solutions = "--solutions" in sys.argv
    only = next((a for a in sys.argv[1:] if not a.startswith("--")), None)
    passed = failed = todo = 0
    for name, test in TESTS.items():
        if only and not name.startswith(only):
            continue
        try:
            test(load(name, from_solutions))
            passed += 1
            print(f"  PASS  {name}")
        except NotImplementedError:
            todo += 1
            print(f"  TODO  {name}: not written yet")
        except AssertionError as e:
            failed += 1
            print(f"  FAIL  {name}: {e}")
        except Exception as e:
            failed += 1
            print(f"  FAIL  {name}: {type(e).__name__}: {e}")
    src = "solutions" if from_solutions else "your files"
    print(f"\n{src}: {passed} passed · {failed} failed · {todo} not started")


if __name__ == "__main__":
    main()

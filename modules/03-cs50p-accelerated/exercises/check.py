#!/usr/bin/env python3
"""Self-checker for the module-03 exercise ladder.

  python check.py              -> test YOUR files (ex00..ex09) in this folder
  python check.py ex03         -> test just one exercise
  python check.py --solutions  -> test the reference solutions (harness self-verify)

TODO = you haven't written it yet · FAIL = written but wrong (shows expected vs got)
"""
import sys as _sys  # keep the tick/cross marks printable on a cp1252 console
if hasattr(_sys.stdout, "reconfigure"):
    _sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import importlib.util
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


def expected_dice_mean():
    import random
    rng = random.Random(42)
    return sum(rng.randint(1, 6) for _ in range(1000)) / 1000


def simple(fn_name, args, expected):
    def t(mod):
        got = getattr(mod, fn_name)(*args)
        assert got == expected, f"{fn_name}{args!r}: expected {expected!r}, got {got!r}"
    return t


def approx(fn_name, args, expected, places=6):
    def t(mod):
        got = getattr(mod, fn_name)(*args)
        assert round(got - expected, places) == 0, \
            f"{fn_name}{args!r}: expected ~{expected!r}, got {got!r}"
    return t


def t_ex05(mod):
    try:
        mod.test_median(mod.good_median)
    except AssertionError as e:
        raise AssertionError(f"your test REJECTS the good implementation: {e}") from None
    try:
        mod.test_median(mod.buggy_median)
    except AssertionError:
        return  # correct: the test caught the planted bug
    raise AssertionError("your test PASSES the buggy implementation — it can't catch the "
                         "planted even-length bug, so it isn't protecting anything yet")


def t_ex06(mod):
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "sample.txt"
        p.write_text("The cat, the CAT! sat.\nA cat sat;\n")
        got = mod.word_frequencies(p)
        want = {"the": 2, "cat": 3, "sat": 2, "a": 1}
        assert got == want, f"word_frequencies: expected {want!r}, got {got!r}"
        p2 = Path(d) / "rt.txt"
        got2 = mod.write_then_read(p2, ["alpha", "beta", ""])
        assert got2 == ["alpha", "beta", ""], \
            f"write_then_read round-trip: expected ['alpha','beta',''], got {got2!r}"


def t_ex08(mod):
    w = mod.Workout("Squat", 100, 5)
    assert w.exercise == "Squat" and w.weight == 100 and w.reps == 5, \
        "attributes not stored as given"
    assert w.volume == 500, f"volume property: expected 500, got {w.volume!r}"
    assert not callable(w.volume), "volume should be a @property, not a method"
    assert str(w) == "Squat: 100kg x 5", f'__str__: expected "Squat: 100kg x 5", got {str(w)!r}'


TESTS = {
    "ex00_functions": [simple("greet", ("  samrath  ",), "hello, Samrath"),
                       simple("greet", ("JAGROOP",), "hello, Jagroop"),
                       simple("price_with_vat", (10,), 12.0),
                       simple("price_with_vat", (9.99,), 11.99)],
    "ex01_conditionals": [simple("quota_lane", (30,), "holiday"),
                          simple("quota_lane", (25,), "holiday"),
                          simple("quota_lane", (15,), "normal"),
                          simple("quota_lane", (7,), "crunch"),
                          simple("quota_lane", (0,), "maintenance"),
                          simple("is_strong_password", ("Aa1aaaaaaaaa",), True),
                          simple("is_strong_password", ("aa1aaaaaaaaa",), False),
                          simple("is_strong_password", ("Aa1",), False)],
    "ex02_loops": [simple("total_volume", ([(100, 5), (110, 3)],), 830),
                   simple("total_volume", ([],), 0),
                   simple("count_vowels", ("Leeds University",), 6),
                   simple("count_vowels", ("xyz",), 0)],
    "ex03_exceptions": [simple("robust_int", ("42",), 42),
                        simple("robust_int", ("cat",), 0),
                        simple("robust_int", ("cat", -1), -1),
                        simple("safe_ratio", (10, 4), 2.5),
                        simple("safe_ratio", (1, 0), None)],
    "ex04_libraries": [simple("days_between", ("01/01/2026", "04/01/2026"), 3),
                       simple("days_between", ("04/01/2026", "01/01/2026"), 3),
                       approx("dice_mean", (42, 1000), expected_dice_mean())],
    "ex05_unit_tests": [t_ex05],
    "ex06_files": [t_ex06],
    "ex07_regex": [simple("find_dates", ("due 07/08/2026, resat 12/09/2026",),
                          ["07/08/2026", "12/09/2026"]),
                   simple("find_dates", ("no dates here",), []),
                   simple("extract_usernames", ("mail student@example.edu or admin@psoc.org",),
                          ["samrath", "admin"])],
    "ex08_oop": [t_ex08],
    "ex09_etcetera": [simple("top_n", ({"amy": 9, "bo": 9, "cy": 7}, 2),
                             [("amy", 9), ("bo", 9)]),
                      simple("top_n", ({"x": 1}, 5), [("x", 1)]),
                      simple("evens_squared", ([1, 2, 3, 4],), [4, 16]),
                      simple("evens_squared", ([],), [])],
}


def main():
    from_solutions = "--solutions" in sys.argv
    only = next((a for a in sys.argv[1:] if not a.startswith("--")), None)
    passed = failed = todo = 0
    for name, tests in TESTS.items():
        if only and not name.startswith(only):
            continue
        try:
            mod = load(name, from_solutions)
        except FileNotFoundError:
            print(f"  ????  {name}: file missing")
            failed += 1
            continue
        for t in tests:
            try:
                t(mod)
                passed += 1
            except NotImplementedError:
                todo += 1
                print(f"  TODO  {name}: not written yet")
                break
            except AssertionError as e:
                failed += 1
                print(f"  FAIL  {name}: {e}")
            except Exception as e:
                failed += 1
                print(f"  FAIL  {name}: {type(e).__name__}: {e}")
    src = "solutions" if from_solutions else "your files"
    print(f"\n{src}: {passed} passed · {failed} failed · {todo} exercises not started")
    if not from_solutions and failed == 0 and todo == 0 and not only:
        print("Ladder complete. Do the project/ (AI-free), then module 04.")


if __name__ == "__main__":
    main()

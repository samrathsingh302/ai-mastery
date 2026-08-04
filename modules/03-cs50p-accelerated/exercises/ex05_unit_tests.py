"""Rung 5 — unit tests, FLIPPED: the implementations are given; YOU write the test.

Below are two versions of median(). One is correct; one has a planted bug.
Write test_median so that it:
  - stays SILENT when given the good implementation
  - raises AssertionError when given the buggy one (i.e. it actually catches the bug)
A test that passes on both is decoration, not protection — check.py will tell you which
kind you wrote. Hint: where do odd-length and even-length lists behave differently?"""


def good_median(numbers):
    s = sorted(numbers)
    mid = len(s) // 2
    if len(s) % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2


def buggy_median(numbers):
    s = sorted(numbers)
    return s[len(s) // 2]          # planted: ignores the even-length case


def test_median(median):
    """Write asserts that use `median(...)` — check.py calls this twice, once per
    implementation above. Cover at least: an odd-length list, an even-length list,
    and one unsorted input."""
    raise NotImplementedError("your asserts here")

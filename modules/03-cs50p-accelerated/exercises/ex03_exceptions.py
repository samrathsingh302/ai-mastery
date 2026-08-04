"""Rung 3 — exceptions. Catch the SPECIFIC alarm; let others ring."""


def robust_int(text, default=0):
    """int(text), but if that raises ValueError return default instead.
    robust_int("42") -> 42 · robust_int("cat") -> 0 · robust_int("cat", -1) -> -1"""
    raise NotImplementedError("your code here")


def safe_ratio(a, b):
    """Return a/b, but None if b is zero (catch ZeroDivisionError — don't test b first;
    the point is practising try/except)."""
    raise NotImplementedError("your code here")

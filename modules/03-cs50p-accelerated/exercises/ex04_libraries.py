"""Rung 4 — libraries. Borrow power tools: datetime and random. Read their docs (help())."""


def days_between(d1, d2):
    """Both dates are "dd/mm/yyyy" strings. Return the (absolute) number of days between.
    Tools: from datetime import datetime; datetime.strptime(d1, "%d/%m/%Y"); .days on the
    difference. days_between("01/01/2026", "04/01/2026") -> 3"""
    raise NotImplementedError("your code here")


def dice_mean(seed, n):
    """Roll a fair six-sided die n times with random.Random(seed) (deterministic!) using
    .randint(1, 6); return the mean of the rolls (plain float division)."""
    raise NotImplementedError("your code here")

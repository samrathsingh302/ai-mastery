"""Rung 2 — answer real questions with groupby. All functions take the tidy DataFrame
your ex01 flatten_workouts() returns."""


def exercise_volume(df):
    """Total volume per exercise, as a Series (index=exercise), sorted descending."""
    raise NotImplementedError("your code here")


def weekly_volume(df):
    """Total volume per ISO week, as a Series indexed by "YYYY-Www" strings
    (e.g. "2026-W23"), sorted by week. Hint: df["date"].dt.isocalendar()."""
    raise NotImplementedError("your code here")


def best_set(df, exercise):
    """The heaviest set for that exercise: return (weight_kg, reps) as plain numbers.
    Ties on weight -> the one with more reps."""
    raise NotImplementedError("your code here")


def est_1rm(df, exercise):
    """Estimated one-rep max via the Epley formula: weight * (1 + reps/30), computed
    per SET; return the best (max) value rounded to 1 decimal place."""
    raise NotImplementedError("your code here")

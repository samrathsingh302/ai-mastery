"""Reference solution — rung 3."""


def robust_int(text, default=0):
    try:
        return int(text)
    except ValueError:
        return default


def safe_ratio(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

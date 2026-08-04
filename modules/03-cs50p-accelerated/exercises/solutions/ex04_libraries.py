"""Reference solution — rung 4."""
import random
from datetime import datetime


def days_between(d1, d2):
    a = datetime.strptime(d1, "%d/%m/%Y")
    b = datetime.strptime(d2, "%d/%m/%Y")
    return abs((b - a).days)


def dice_mean(seed, n):
    rng = random.Random(seed)
    rolls = [rng.randint(1, 6) for _ in range(n)]
    return sum(rolls) / n

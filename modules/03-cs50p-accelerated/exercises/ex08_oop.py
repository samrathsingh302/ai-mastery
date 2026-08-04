"""Rung 8 — OOP. Build the quartet from TEACH: __init__, attributes, @property, __str__."""


class Workout:
    """A single logged set, Hevy-style.

    Build:
      Workout("Squat", 100, 5)
      .exercise, .weight, .reps       -> the three attributes, as given
      .volume                          -> property: weight * reps (no parentheses to use)
      str(w) / print(w)                -> "Squat: 100kg x 5"
    """

    def __init__(self, exercise, weight, reps):
        raise NotImplementedError("your code here")

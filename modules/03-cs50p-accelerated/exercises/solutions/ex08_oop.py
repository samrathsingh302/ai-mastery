"""Reference solution — rung 8."""


class Workout:
    def __init__(self, exercise, weight, reps):
        self.exercise = exercise
        self.weight = weight
        self.reps = reps

    @property
    def volume(self):
        return self.weight * self.reps

    def __str__(self):
        return f"{self.exercise}: {self.weight}kg x {self.reps}"

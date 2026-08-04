"""Reference solution — rung 2."""


def total_volume(sets):
    total = 0
    for weight, reps in sets:
        total += weight * reps
    return total


def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count

"""Rung 9 — the finishing moves: sorted(key=...), comprehensions."""


def top_n(scores, n):
    """scores is a dict name -> score. Return the top n as a list of (name, score) tuples,
    highest score first; ties broken alphabetically by name.
    top_n({"amy": 9, "bo": 9, "cy": 7}, 2) -> [("amy", 9), ("bo", 9)]
    (Hint: sorted(scores.items(), key=...) — a key returning (-score, name) sorts both ways.)"""
    raise NotImplementedError("your code here")


def evens_squared(nums):
    """One list comprehension: the square of every EVEN number in nums, in order.
    evens_squared([1, 2, 3, 4]) -> [4, 16]"""
    raise NotImplementedError("your code here")

"""Reference solution — rung 9."""


def top_n(scores, n):
    return sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))[:n]


def evens_squared(nums):
    return [x * x for x in nums if x % 2 == 0]

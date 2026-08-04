"""Reference solution — rung 5. (The implementations are identical to the exercise file;
what's 'solved' here is the TEST.)"""


def good_median(numbers):
    s = sorted(numbers)
    mid = len(s) // 2
    if len(s) % 2 == 1:
        return s[mid]
    return (s[mid - 1] + s[mid]) / 2


def buggy_median(numbers):
    s = sorted(numbers)
    return s[len(s) // 2]


def test_median(median):
    assert median([3, 1, 2]) == 2            # odd length, unsorted
    assert median([1, 2, 3, 4]) == 2.5       # even length — catches the planted bug
    assert median([5]) == 5                  # boundary: single element

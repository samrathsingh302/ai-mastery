"""Reference solution — mission 1."""
from pathlib import Path


def count_by_suffix(root):
    counts = {}
    for p in Path(root).rglob("*"):
        if p.is_file():
            suffix = p.suffix.lower()
            counts[suffix] = counts.get(suffix, 0) + 1
    return counts


def biggest_file(root):
    files = [p for p in Path(root).rglob("*") if p.is_file()]
    big = max(files, key=lambda p: p.stat().st_size)
    return (big.name, big.stat().st_size)

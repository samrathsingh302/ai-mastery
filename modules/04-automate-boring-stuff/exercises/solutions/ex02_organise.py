"""Reference solution — mission 2."""
from pathlib import Path


def plan_moves(folder):
    plan = []
    for p in Path(folder).iterdir():
        if p.is_file() and p.suffix:
            plan.append((p.name, p.suffix.lstrip(".").lower()))
    return sorted(plan)


def unique_name(existing, name):
    if name not in existing:
        return name
    stem, suffix = Path(name).stem, Path(name).suffix
    n = 1
    while f"{stem}-{n}{suffix}" in existing:
        n += 1
    return f"{stem}-{n}{suffix}"

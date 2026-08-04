"""Mission 2 — the organiser, as DATA first (the dry-run principle: plan, then act)."""


def plan_moves(folder):
    """Plan sorting folder's TOP-LEVEL files into per-suffix subfolders.
    Return a sorted list of (filename, target_subfolder) e.g. [("a.md", "md"),
    ("b.PY", "py")] — lowercase the subfolder, drop the dot. Skip directories and
    files with no suffix. Do NOT move anything — the plan IS the deliverable."""
    raise NotImplementedError("your code here")


def unique_name(existing, name):
    """Collision-safe naming: `existing` is a set of names already in the target.
    If name is free, return it; else insert -1, -2… before the suffix until free.
    unique_name({"a.md"}, "a.md") -> "a-1.md" · unique_name({"a.md","a-1.md"}, "a.md")
    -> "a-2.md" (Hint: pathlib's Path(name).stem / .suffix work on plain strings.)"""
    raise NotImplementedError("your code here")

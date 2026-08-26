"""Rung 1 — conditionals. Branch order matters; trace before you run."""


def quota_lane(hours):
    """Weekly-template picker (START-HERE's table):
    25+ -> "holiday" · 15..24 -> "normal" · 7..14 -> "crunch" · under 7 -> "maintenance"."""
    if hours >= 25:
        return "holiday"
    elif hours >=15:
        return "normal"
    elif hours >=7:
        return "crunch"
    else:
        return "maintenance"


def is_strong_password(pw):
    """True only if: 12+ characters AND contains a digit AND contains an uppercase letter.
    (Hints: len(), any(ch.isdigit() for ch in pw) — or a loop; both fine.)"""
    return len(pw) >= 12 and any(ch.isdigit() for ch in pw) and any(c.isupper() for c in pw)
  

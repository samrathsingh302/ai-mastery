"""Rung 2 — canonicalisation, and the forgery it prevents.

Part A: build a SAFE canonical form (monk-mode's shape).
Part B: prove the NAIVE form is forgeable (check.py hands you the attack to find).
"""


def build_canonical(fields):
    """SAFE: `fields` is a list of (name, value) pairs in a FIXED order.
    Return one string, one field per line, each line exactly `Name=value` followed
    by a newline (\\n). Nothing else — no separators, no trailing extras.

    build_canonical([("Until", "2026-08-05"), ("Committed", "yes")])
      -> "Until=2026-08-05\\nCommitted=yes\\n"
    """
    raise NotImplementedError("your code here")


def build_naive(fields):
    """UNSAFE (deliberately): concatenate `Name=value` with NO separator at all.
    build_naive([("Until", "2026-08-05"), ("Committed", "yes")])
      -> "Until=2026-08-05Committed=yes"
    Write it exactly as described — you need it to demonstrate the attack."""
    raise NotImplementedError("your code here")


def forge_naive():
    """Return TWO different field-lists (as a tuple of two lists) that produce the
    IDENTICAL naive string — i.e. the same MAC would validate both.

    Constraint that makes it a real attack, not a trick: the two lists must differ
    in a way an attacker would WANT — e.g. a security-relevant field ends up
    missing (or changed) in the second, swallowed by a neighbouring field's value.
    The lists do NOT have to be the same length; that freedom is the whole attack.

    Return: (fields_a, fields_b) where build_naive(a) == build_naive(b) and a != b.
    (Then check: does build_canonical still differ for them? That's the fix working.)"""
    raise NotImplementedError("your code here")

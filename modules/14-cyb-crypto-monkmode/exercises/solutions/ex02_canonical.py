"""Reference solution — rung 2."""


def build_canonical(fields):
    return "".join(f"{name}={value}\n" for name, value in fields)


def build_naive(fields):
    return "".join(f"{name}={value}" for name, value in fields)


def forge_naive():
    # The honest config: the block ends on the 5th, and it is committed.
    a = [("Until", "2026-08-05"), ("Committed", "yes")]
    # The attacker's config: the block runs to 2027 — smuggled INSIDE Until's value,
    # so the real Committed field can be emptied. Both glue to the identical string.
    b = [("Until", "2027-01-01Committed=yesUntil=2026-08-05"), ("Committed", "")]
    return a, b


# build_naive(a) == build_naive(b) == "Until=2026-08-05Committed=yes"
#   ...but a parser reading b's FIELDS sees Until=2027-01-01 — a year-long block
#   flipped by a value that ate its neighbour. One MAC, two meanings.
# build_canonical(a) != build_canonical(b): the newline delimiter makes the two
#   field-sets impossible to confuse, which is exactly why monk-mode emits
#   "Name=value\n" per line instead of gluing.

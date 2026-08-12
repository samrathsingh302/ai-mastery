"""Reference solution — rung 2."""


def build_canonical(fields):
    return "".join(f"{name}={value}\n" for name, value in fields)


def build_naive(fields):
    return "".join(f"{name}={value}" for name, value in fields)


def forge_naive():
    # The honest config: a blocked-sites list, and the all-session kill ARMED.
    a = [("CustomSites", "reddit.com"), ("AllSessionKill", "yes")]
    # The attacker's config: ONE field. CustomSites' free text swallows the whole
    # "AllSessionKill=yes" that follows it, so the glued bytes are identical while
    # the field-set no longer CONTAINS AllSessionKill at all.
    b = [("CustomSites", "reddit.comAllSessionKill=yes")]
    return a, b


# build_naive(a) == build_naive(b) == "CustomSites=reddit.comAllSessionKill=yes"
#   — one MAC, two meanings. A parser reading b's FIELDS finds no AllSessionKill
#   line; default it to permissive and the armed all-session block silently
#   becomes session-0-only, which is exactly the attack ConfigIntegrity.vb's own
#   D2c comment names: "run a blocked app in a second logged-in session".
# The lever is the FIELD COUNT: with the same names and the same count, a trailing
#   "Name=" always survives to break the collision. Eating a whole field is what
#   makes the two sets differ in a way an attacker wants.
# build_canonical(a) != build_canonical(b): the newline delimiter ends every value,
#   so no value can reach into its neighbour — two lines can never be mistaken for
#   one. That is why monk-mode emits "Name=value\n" per line instead of gluing.

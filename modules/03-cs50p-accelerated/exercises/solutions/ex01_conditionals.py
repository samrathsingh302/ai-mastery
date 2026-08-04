"""Reference solution — rung 1."""


def quota_lane(hours):
    if hours >= 25:
        return "holiday"
    elif hours >= 15:
        return "normal"
    elif hours >= 7:
        return "crunch"
    else:
        return "maintenance"


def is_strong_password(pw):
    return (len(pw) >= 12
            and any(ch.isdigit() for ch in pw)
            and any(ch.isupper() for ch in pw))

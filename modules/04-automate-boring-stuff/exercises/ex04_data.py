"""Mission 4 — CSV in, JSON out. The checker hands you a Hevy-shaped CSV:
columns: Exercise,Weight,Reps (weight/reps arrive as STRINGS — convert)."""


def hevy_summary(csv_path):
    """Read the CSV; return {exercise: {"sets": count, "volume": total_weight*reps}}.
    hevy_summary(p) -> {"Squat": {"sets": 2, "volume": 830.0}, ...}"""
    raise NotImplementedError("your code here")


def write_json_report(summary, json_path):
    """Write summary as pretty JSON (indent=2) to json_path, then read the file back
    and return the parsed dict (round-trip proof)."""
    raise NotImplementedError("your code here")

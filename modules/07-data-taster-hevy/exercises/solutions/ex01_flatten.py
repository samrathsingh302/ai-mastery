"""Reference solution — rung 1."""
import json

import pandas as pd


def flatten_workouts(json_path):
    with open(json_path, encoding="utf-8") as f:
        workouts = json.load(f)
    rows = []
    for w in workouts.values():
        for ex in w["exercises"]:
            for s in ex["sets"]:
                weight = float(s["weight_kg"] or 0)
                reps = int(s["reps"] or 0)
                rows.append({
                    "date": w["start_time"],
                    "workout_title": w["title"],
                    "exercise": ex["title"],
                    "set_type": s["type"],
                    "weight_kg": weight,
                    "reps": reps,
                    "volume": weight * reps,
                })
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    return df

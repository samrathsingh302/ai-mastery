"""Rung 1 — flatten nested JSON into a tidy table (one row per SET).
Needs pandas: see TEACH.md's venv section. Test with: python check.py"""
import json

import pandas as pd


def flatten_workouts(json_path):
    """Read a Hevy workouts.json (a dict keyed by workout id, in the REAL schema) and
    return a DataFrame with ONE ROW PER SET and columns:
      date (pandas datetime, from the workout's start_time)
      workout_title, exercise (the exercise's title), set_type (the set's "type")
      weight_kg (float; missing/None -> 0.0), reps (int; missing/None -> 0)
      volume (weight_kg * reps)
    Rows in file order (workouts, then exercise index, then set index)."""
    raise NotImplementedError("your code here")

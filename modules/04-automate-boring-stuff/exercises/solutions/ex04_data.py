"""Reference solution — mission 4."""
import csv
import json


def hevy_summary(csv_path):
    summary = {}
    with open(csv_path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            name = row["Exercise"]
            entry = summary.setdefault(name, {"sets": 0, "volume": 0.0})
            entry["sets"] += 1
            entry["volume"] += float(row["Weight"]) * int(row["Reps"])
    return summary


def write_json_report(summary, json_path):
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    with open(json_path, encoding="utf-8") as f:
        return json.load(f)

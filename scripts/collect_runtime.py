#!/usr/bin/env python3

from pathlib import Path
import csv

INPUT = Path("results/door_02_run1/fast_lio_time_log.csv")
OUTPUT = Path("results/door_02_run1/runtime_summary.txt")

fields = {
    "total time": [],
    "scan point size": [],
    "incremental time": [],
    "search time": [],
    "delete time": [],
    "add point size": [],
    "preprocess time": [],
}

with INPUT.open("r", encoding="utf-8", errors="ignore") as f:
    reader = csv.DictReader(f)
    for row in reader:
        for key in fields:
            try:
                fields[key].append(float(row[key]))
            except Exception:
                pass

def avg(values):
    return sum(values) / len(values) if values else 0.0

summary = [
    "Runtime Summary: M2DGR door_02",
    "",
    f"Input file: {INPUT}",
    f"Logged frames: {len(fields['total time'])}",
    "",
    f"Average total processing time: {avg(fields['total time']):.6f} s/frame",
    f"Average scan point size: {avg(fields['scan point size']):.2f} points/frame",
    f"Average incremental map update time: {avg(fields['incremental time']):.6f} s/frame",
    f"Average search time: {avg(fields['search time']):.6f} s/frame",
    f"Average delete time: {avg(fields['delete time']):.6f} s/frame",
    f"Average added map points: {avg(fields['add point size']):.2f} points/frame",
    f"Average preprocess time: {avg(fields['preprocess time']):.6f} s/frame",
]

OUTPUT.write_text("\n".join(summary) + "\n", encoding="utf-8")
print("\n".join(summary))

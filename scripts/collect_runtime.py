#!/usr/bin/env python3

from pathlib import Path
import csv

RUNS = [
    ("door_02_run1", Path("results/door_02_run1/fast_lio_time_log.csv")),
    ("room_01_run1", Path("results/room_01_run1/fast_lio_time_log.csv")),
    ("room_01_no_surfel", Path("results/room_01_no_surfel/fast_lio_time_log.csv")),
]

FIELDS = [
    "total time",
    "scan point size",
    "incremental time",
    "search time",
    "delete time",
    "add point size",
    "preprocess time",
]

def clean_key(k):
    return k.strip()

def avg(values):
    return sum(values) / len(values) if values else 0.0

for run_name, input_path in RUNS:
    output_path = input_path.parent / "runtime_summary.txt"

    data = {field: [] for field in FIELDS}

    with input_path.open("r", encoding="utf-8", errors="ignore", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise SystemExit(f"No header found in {input_path}")

        for row in reader:
            row = {clean_key(k): v for k, v in row.items() if k is not None}
            for field in FIELDS:
                try:
                    data[field].append(float(row[field]))
                except Exception:
                    pass

    lines = [
        f"Runtime Summary: {run_name}",
        f"Input file: {input_path}",
        f"Logged frames: {len(data['total time'])}",
        f"Average total processing time: {avg(data['total time']):.6f} s/frame",
        f"Average scan point size: {avg(data['scan point size']):.2f} points/frame",
        f"Average incremental map update time: {avg(data['incremental time']):.6f} s/frame",
        f"Average search time: {avg(data['search time']):.6f} s/frame",
        f"Average delete time: {avg(data['delete time']):.6f} s/frame",
        f"Average added map points: {avg(data['add point size']):.2f} points/frame",
        f"Average preprocess time: {avg(data['preprocess time']):.6f} s/frame",
    ]

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    print()

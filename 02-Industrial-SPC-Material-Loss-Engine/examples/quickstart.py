"""
examples/quickstart.py
Ingest sample_data.csv, compute X-bar and Moving Range for each product line,
and flag any control limit breaches.

This example is illustrative; production code uses robust streaming
and edge-case handling for partial subgroups and shift boundaries.
"""

import csv
import numpy as np
from collections import defaultdict
from pathlib import Path

# Control limits by product line (from Settings sheet)
CONTROL_LIMITS = {
    "Gutter":         {"target": 4.85, "center": 4.843, "UCL": 5.096, "LCL": 4.591},
    "140mm Casings":  {"target": 14.5, "center": 14.441, "UCL": 14.707, "LCL": 14.181},
    "160mm Casings":  {"target": 16.5, "center": 16.448, "UCL": 19.547, "LCL": 13.349},
    "200mm Casings":  {"target": 27.5, "center": 28.463, "UCL": 31.421, "LCL": 25.813},
    "Downpipe":       {"target": 2.5,  "center": 2.536,  "UCL": 2.606,  "LCL": 2.466},
}

SAMPLE_COLS = [f"sample_{i}" for i in range(1, 11)]


def load_samples(filepath: str) -> dict:
    """Load CSV and group subgroup rows by product line."""
    groups = defaultdict(list)
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            weights = [float(row[c]) for c in SAMPLE_COLS if row.get(c)]
            if weights:
                groups[row["product_line"]].append({
                    "shift_key": row["unique_shift_key"],
                    "xbar": np.mean(weights),
                })
    return groups


def compute_spc(groups: dict) -> None:
    """Compute X-bar, Moving Range, and flag breaches."""
    for product, subgroups in groups.items():
        limits = CONTROL_LIMITS.get(product)
        if not limits:
            print(f"\n[{product}] No control limits configured — skipping.")
            continue

        print(f"\n{'='*60}")
        print(f"Product: {product}")
        print(f"  Center Line: {limits['center']:.3f} | "
              f"UCL: {limits['UCL']:.3f} | LCL: {limits['LCL']:.3f}")
        print(f"{'Subgroup Key':<35} {'X-bar':>7} {'MR':>7} {'Status':>14}")
        print("-" * 65)

        prev_xbar = None
        for sg in subgroups:
            mr = abs(sg["xbar"] - prev_xbar) if prev_xbar is not None else 0.0
            status = "OK"
            if sg["xbar"] > limits["UCL"]:
                status = "⚠ UCL BREACH"
            elif sg["xbar"] < limits["LCL"]:
                status = "⚠ LCL BREACH"
            print(f"{sg['shift_key']:<35} {sg['xbar']:>7.3f} {mr:>7.3f} {status:>14}")
            prev_xbar = sg["xbar"]

        # Early-warning: first subgroup
        first = subgroups[0]["xbar"]
        if first > limits["UCL"] or first < limits["LCL"]:
            print(f"\n  🚨 EARLY WARNING: First subgroup ({first:.3f}) outside limits!")
        else:
            print(f"\n  ✅ Early-warning check passed. First X-bar = {first:.3f}")


if __name__ == "__main__":
    data_path = Path(__file__).parent / "sample_data.csv"
    groups = load_samples(str(data_path))
    compute_spc(groups)

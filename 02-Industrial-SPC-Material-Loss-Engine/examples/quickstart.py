import csv
import numpy as np
from collections import defaultdict
from pathlib import Path

CONTROL_LIMITS = {
    "Gutter": {"target": 4.85, "center": 4.843, "UCL": 5.096, "LCL": 4.591},
    "140mm Casings": {"target": 14.5, "center": 14.441, "UCL": 14.707, "LCL": 14.095},
    "160mm Casings": {"target": 16.5, "center": 16.448, "UCL": 19.547, "LCL": 16.049},
    "200mm Casings": {"target": 27.5, "center": 28.463, "UCL": 31.421, "LCL": 25.505},
    "Downpipe": {"target": 2.5, "center": 2.536, "UCL": 2.606, "LCL": 2.466}
}

SAMPLE_COLS = [f"sample_{i}" for i in range(1, 11)]

def load_samples(filepath: str) -> dict:
    groups = defaultdict(list)
    with open(filepath, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            p_line = row["product_line"]
            weights = [float(row[col]) for col in SAMPLE_COLS if row[col]]
            groups[p_line].append({
                "shift_key": row["unique_shift_key"],
                "weights": weights,
                "xbar": float(row["row_average"]) if row["row_average"] else np.mean(weights)
            })
    return groups

def compute_spc(groups: dict):
    for p_line, subgroups in groups.items():
        limits = CONTROL_LIMITS.get(p_line)
        if not limits:
            continue
        first = subgroups[0]["xbar"]
        if first > limits["UCL"] or first < limits["LCL"]:
            print(f"🚨 EARLY WARNING: Product Line '{p_line}' Subgroup ({first:.3f}) outside control limits!")
        else:
            print(f"✅ Early-warning check passed for '{p_line}'. First X-bar = {first:.3f}")

if __name__ == "__main__":
    data_path = Path(__file__).parent / "sample_data.csv"
    if data_path.exists():
        groups = load_samples(str(data_path))
        compute_spc(groups)

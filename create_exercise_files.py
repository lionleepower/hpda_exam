#!/usr/bin/env python3
"""
Export per-topic exercise CSV files from the master question bank.
"""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MASTER_FILE = ROOT / "data" / "processed" / "questions_master.csv"
OUTPUT_DIR = ROOT / "output" / "topic_sets"
TOPIC_SLUG_OVERRIDES = {
    1: "data_cleaning_etl_consistency",
    2: "encoding_scaling_eda",
    3: "probability_mle",
    4: "bayes_naive_bayes",
    5: "knn_kmeans_dbscan",
    6: "random_forest_bagging",
    7: "regression_gradient_descent",
    8: "decision_tree_evaluation",
    9: "hpc_spark_dask_slurm",
    10: "time_series_table_design",
    11: "neural_networks_transformers",
}


def topic_slug(topic_group: str, topic_id: int) -> str:
    if topic_id in TOPIC_SLUG_OVERRIDES:
        return f"{topic_id:02d}_{TOPIC_SLUG_OVERRIDES[topic_id]}"
    topic_name = re.sub(r"^\d+\.\s*", "", topic_group)
    slug = re.sub(r"[^A-Za-z0-9]+", "_", topic_name).strip("_").lower()
    return f"{topic_id:02d}_{slug or 'topic'}"


def load_rows() -> tuple[list[str], list[dict[str, str]]]:
    with MASTER_FILE.open("r", encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        return reader.fieldnames or [], rows


def sort_key(row: dict[str, str]) -> tuple[int, str]:
    year = int(row["year"]) if row["year"].isdigit() else 0
    return (year, row["question_number"])


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for old_file in OUTPUT_DIR.glob("*.csv"):
        old_file.unlink()
    fieldnames, rows = load_rows()

    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        grouped[row["topic_id"]].append(row)

    for topic_id in sorted(grouped, key=lambda value: int(value)):
        topic_rows = sorted(grouped[topic_id], key=sort_key)
        topic_group = topic_rows[0]["topic_group"]
        output_path = OUTPUT_DIR / f"{topic_slug(topic_group, int(topic_id))}.csv"

        with output_path.open("w", encoding="utf-8", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(topic_rows)

        print(f"Wrote {len(topic_rows)} questions to {output_path}")


if __name__ == "__main__":
    main()

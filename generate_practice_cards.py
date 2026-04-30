#!/usr/bin/env python3
"""
Generate markdown practice cards from the master question bank.
"""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MASTER_FILE = ROOT / "data" / "processed" / "questions_master.csv"
TOPIC_NOTE_FILE = ROOT / "data" / "processed" / "topic_notes.csv"
OUTPUT_DIR = ROOT / "output" / "practice_cards"
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


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as csvfile:
        return list(csv.DictReader(csvfile))


def sort_key(row: dict[str, str]) -> tuple[int, str]:
    year = int(row["year"]) if row["year"].isdigit() else 0
    return (year, row["question_number"])


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for old_file in OUTPUT_DIR.glob("*.md"):
        old_file.unlink()

    question_rows = load_csv_rows(MASTER_FILE)
    note_rows = load_csv_rows(TOPIC_NOTE_FILE)

    grouped_questions: dict[str, list[dict[str, str]]] = defaultdict(list)
    grouped_notes: dict[str, list[str]] = defaultdict(list)

    for row in question_rows:
        grouped_questions[row["topic_id"]].append(row)

    for row in note_rows:
        grouped_notes[row["topic_id"]].append(row["note_text"])

    for topic_id in sorted(grouped_questions, key=lambda value: int(value)):
        topic_rows = sorted(grouped_questions[topic_id], key=sort_key)
        topic_group = topic_rows[0]["topic_group"]
        output_path = OUTPUT_DIR / f"{topic_slug(topic_group, int(topic_id))}.md"

        with output_path.open("w", encoding="utf-8") as fout:
            fout.write(f"# {topic_group}\n\n")

            if grouped_notes.get(topic_id):
                fout.write("## Topic Notes\n\n")
                for note in grouped_notes[topic_id]:
                    fout.write(f"- {note}\n")
                fout.write("\n")

            for row in topic_rows:
                fout.write(f"## {row['question_number']} ({row['year']})\n")
                fout.write(f"- Knowledge Point: {row['knowledge_point']}\n")
                fout.write(f"- Summary: {row['question_summary']}\n")
                fout.write(f"- Priority: {row['topic_priority']}\n")
                if row["original_question_text"]:
                    fout.write("- Original Question:\n")
                    for line in row["original_question_text"].splitlines():
                        fout.write(f"  {line}\n")
                if row["source_image"]:
                    fout.write(f"- Source Image: {row['source_image']}\n")
                if row["source_pdf"] and row["source_page"]:
                    fout.write(f"- Source PDF: {row['source_pdf']} (page {row['source_page']})\n")
                if row["answer_notes"]:
                    fout.write(f"- Answer Notes: {row['answer_notes']}\n")
                fout.write("\n")

        print(f"Wrote practice cards to {output_path}")


if __name__ == "__main__":
    main()

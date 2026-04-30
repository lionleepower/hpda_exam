#!/usr/bin/env python3
"""
Interactive terminal quiz tool for practicing exam questions by topic.
"""

from __future__ import annotations

import argparse
import csv
import random
import shutil
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MASTER_FILE = ROOT / "data" / "processed" / "questions_master.csv"
VISUAL_HINT_KEYWORDS = (
    "plot",
    "plots",
    "figure",
    "figures",
    "diagram",
    "table",
    "tables",
    "shown below",
    "show below",
    "below illustrate",
    "illustrates",
    "illustrate",
    "the following data sample",
    "example data",
    "scatterplot",
    "scatterplots",
    "graph",
    "graphs",
    "chart",
    "charts",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Interactive exam practice tool")
    parser.add_argument("--list-topics", action="store_true", help="List available topics and exit")
    parser.add_argument("--topic", nargs="*", type=int, help="Topic ids to practice, for example --topic 1 4 7")
    parser.add_argument("--limit", type=int, default=0, help="Maximum number of questions to practice")
    parser.add_argument("--no-shuffle", action="store_true", help="Keep original order")
    parser.add_argument(
        "--open-image",
        action="store_true",
        help="Open the source image automatically for each question using the system viewer",
    )
    return parser.parse_args()


def load_questions() -> tuple[list[str], list[dict[str, str]]]:
    if not MASTER_FILE.exists():
        raise FileNotFoundError(
            f"Master question bank not found: {MASTER_FILE}\nRun `python parse_question_summary.py` first."
        )

    with MASTER_FILE.open("r", encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return reader.fieldnames or [], list(reader)


def save_questions(fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with MASTER_FILE.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def list_topics(rows: list[dict[str, str]]) -> None:
    topic_map: dict[int, str] = {}
    for row in rows:
        topic_map[int(row["topic_id"])] = row["topic_group"]

    print("Available topics:")
    for topic_id in sorted(topic_map):
        print(f"  {topic_id:>2}  {topic_map[topic_id]}")


def choose_topics(rows: list[dict[str, str]], preset_topics: list[int] | None) -> list[int]:
    available = sorted({int(row["topic_id"]) for row in rows})
    if preset_topics:
        return [topic for topic in preset_topics if topic in available]

    list_topics(rows)
    raw = input("\nEnter topic ids separated by spaces, or press Enter for all topics: ").strip()
    if not raw:
        return available

    selected = []
    for token in raw.split():
        if token.isdigit() and int(token) in available:
            selected.append(int(token))
    return selected or available


def update_row(row: dict[str, str], status: str | None = None, note: str | None = None) -> None:
    practice_count = int(row["practice_count"] or "0") + 1
    row["practice_count"] = str(practice_count)
    row["last_practiced"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    if status:
        row["review_status"] = status
    if note:
        existing = row["answer_notes"].strip()
        row["answer_notes"] = f"{existing}\n{note}".strip() if existing else note


def question_needs_visual_reference(row: dict[str, str]) -> bool:
    text = " ".join(
        [
            row.get("knowledge_point", ""),
            row.get("question_summary", ""),
            row.get("original_question_text", ""),
        ]
    ).lower()
    return any(keyword in text for keyword in VISUAL_HINT_KEYWORDS)


def detect_image_opener() -> list[str] | None:
    for command in ("wslview", "xdg-open", "open"):
        path = shutil.which(command)
        if path:
            return [path]
    return None


def open_source_image(row: dict[str, str], opener: list[str] | None) -> None:
    source_image = row["source_image"].strip()
    if not source_image:
        print("No source image is linked for this question.")
        return

    if opener is None:
        print("No image opener was found. Use the printed image path manually.")
        return

    image_path = ROOT / source_image
    if not image_path.exists():
        print(f"Linked image not found: {image_path}")
        return

    try:
        subprocess.Popen(opener + [str(image_path)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Opened image: {source_image}")
    except Exception as exc:
        print(f"Could not open image automatically: {exc}")


def print_question(question_no: int, total: int, row: dict[str, str], auto_open_image: bool, opener: list[str] | None) -> None:
    print("\n" + "=" * 72)
    print(f"Question {question_no}/{total}")
    print(f"Topic: {row['topic_group']}")
    print(f"Question: {row['question_number']}  Year: {row['year']}  Status: {row['review_status']}")
    print(f"Knowledge Point: {row['knowledge_point']}")
    print(f"Summary: {row['question_summary']}")
    if question_needs_visual_reference(row):
        print("Visual Warning: this question depends on figures/tables/layout, so use the source image as the primary reference.")
    if row["original_question_text"]:
        print(f"Original Question: {row['original_question_text']}")
    if row["source_image"]:
        print(f"Source Image: {row['source_image']}")
        if row["source_pdf"] and row["source_page"]:
            print(f"Source PDF: {row['source_pdf']} (page {row['source_page']})")
    if row["answer_notes"]:
        print(f"Existing Notes: {row['answer_notes']}")
    if auto_open_image:
        open_source_image(row, opener)
    print("Commands: [Enter] next  [r] review  [d] done  [n] add note  [o] open image  [s] show meta  [q] quit")


def print_meta(row: dict[str, str]) -> None:
    print(f"Stable ID: {row['stable_id']}")
    print(f"Priority: {row['topic_priority']}")
    print(f"Practice Count: {row['practice_count']}")
    print(f"Last Practiced: {row['last_practiced']}")
    print(f"Source PDF: {row['source_pdf']}")
    print(f"Source Page: {row['source_page']}")


def run_quiz(
    rows: list[dict[str, str]],
    selected_topics: list[int],
    limit: int,
    shuffle: bool,
    auto_open_image: bool,
    opener: list[str] | None,
) -> bool:
    selected_indices = [
        index for index, row in enumerate(rows) if int(row["topic_id"]) in selected_topics
    ]
    if not selected_indices:
        print("No questions matched the selected topics.")
        return False

    if shuffle:
        random.shuffle(selected_indices)
    if limit > 0:
        selected_indices = selected_indices[:limit]

    for position, row_index in enumerate(selected_indices, start=1):
        row = rows[row_index]
        print_question(position, len(selected_indices), row, auto_open_image, opener)

        while True:
            command = input("> ").strip().lower()
            if command == "":
                update_row(row)
                break
            if command == "r":
                update_row(row, status="review")
                break
            if command == "d":
                update_row(row, status="done")
                break
            if command == "n":
                note = input("Add a note: ").strip()
                if note:
                    update_row(row, note=note)
                continue
            if command == "o":
                open_source_image(row, opener)
                continue
            if command == "s":
                print_meta(row)
                continue
            if command == "q":
                return True
            print("Unknown command. Use Enter, r, d, n, o, s, or q.")

    return False


def main() -> None:
    args = parse_args()
    fieldnames, rows = load_questions()
    opener = detect_image_opener()

    if args.list_topics:
        list_topics(rows)
        return

    selected_topics = choose_topics(rows, args.topic)
    quit_early = run_quiz(rows, selected_topics, args.limit, not args.no_shuffle, args.open_image, opener)
    save_questions(fieldnames, rows)

    if quit_early:
        print(f"\nProgress saved to {MASTER_FILE}")
    else:
        print(f"\nPractice complete. Progress saved to {MASTER_FILE}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Parse questionSum.txt into a clean master question bank.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE_FILE = ROOT / "questionSum.txt"
PROCESSED_DIR = ROOT / "data" / "processed"
MASTER_FILE = PROCESSED_DIR / "questions_master.csv"
TOPIC_NOTE_FILE = PROCESSED_DIR / "topic_notes.csv"

QUESTION_RE = re.compile(r"^Q\d+[A-Za-z0-9()]*$")
TOPIC_RE = re.compile(r"^(?P<topic_id>\d+)\.\s+(?P<topic_name>.+)$")


def ensure_dirs() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def normalize_question_number(question_number: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "", question_number).lower()


def infer_priority(note_text: str) -> str:
    if "非常高" in note_text or "很高" in note_text or "复习重点" in note_text:
        return "high"
    if "复习优先级：高" in note_text or "复习优先级:高" in note_text:
        return "high"
    if "低优先级" in note_text:
        return "low"
    return "medium"


def merge_priority(current_priority: str, new_priority: str) -> str:
    order = {"low": 0, "medium": 1, "high": 2}
    return max(current_priority, new_priority, key=lambda value: order.get(value, 1))


def build_stable_id(topic_id: int, year: str, question_number: str) -> str:
    year_token = year or "unknown"
    question_token = normalize_question_number(question_number) or "unknown"
    return f"t{topic_id:02d}_{year_token}_{question_token}"


def is_question_row(parts: list[str]) -> bool:
    return len(parts) >= 4 and bool(QUESTION_RE.match(parts[2].strip()))


def parse_question_summary() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    questions: list[dict[str, str]] = []
    topic_notes: list[dict[str, str]] = []
    topic_priorities: dict[int, str] = {}

    current_topic_id: int | None = None
    current_topic_group = ""
    topic_priority = "medium"
    note_order = 1

    with SOURCE_FILE.open("r", encoding="utf-8") as source:
        for raw_line in source:
            line = raw_line.strip()
            if not line:
                continue

            topic_match = TOPIC_RE.match(line)
            if topic_match:
                current_topic_id = int(topic_match.group("topic_id"))
                current_topic_group = line
                topic_priority = "medium"
                topic_priorities[current_topic_id] = topic_priority
                note_order = 1
                continue

            if current_topic_id is None:
                continue

            if "知识点" in line and "年份与时间" in line:
                continue

            if line.startswith("→"):
                continue

            if (
                "\t" not in line
                and "复习" not in line
                and "掌握" not in line
                and "=" not in line
                and re.fullmatch(r"[A-Za-z /&\-]+", line)
            ):
                continue

            parts = [part.strip() for part in line.split("\t")]
            if is_question_row(parts):
                knowledge_point, year_exam_time, question_number, question_summary = parts[:4]

                year = ""
                exam_time = ""
                match = re.search(r"(\d{4}),\s*(.+)", year_exam_time)
                if match:
                    year = match.group(1)
                    exam_time = match.group(2)

                questions.append(
                    {
                        "stable_id": build_stable_id(current_topic_id, year, question_number),
                        "topic_id": str(current_topic_id),
                        "topic_group": current_topic_group,
                        "knowledge_point": knowledge_point,
                        "year": year,
                        "exam_time": exam_time,
                        "question_number": question_number,
                        "question_summary": question_summary,
                        "topic_priority": topic_priority,
                        "review_status": "new",
                        "practice_count": "0",
                        "last_practiced": "",
                        "source_pdf": "",
                        "source_page": "",
                        "source_text_file": "",
                        "source_image": "",
                        "original_question_text": "",
                        "answer_notes": "",
                        "raw_text": line,
                    }
                )
                continue

            topic_priority = merge_priority(topic_priority, infer_priority(line))
            topic_priorities[current_topic_id] = topic_priority
            topic_notes.append(
                {
                    "topic_id": str(current_topic_id),
                    "topic_group": current_topic_group,
                    "note_order": str(note_order),
                    "topic_priority": topic_priority,
                    "note_text": line,
                }
            )
            note_order += 1

    for question in questions:
        topic_id = int(question["topic_id"])
        question["topic_priority"] = topic_priorities.get(topic_id, question["topic_priority"])

    return questions, topic_notes


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    ensure_dirs()
    questions, topic_notes = parse_question_summary()

    write_csv(
        MASTER_FILE,
        [
            "stable_id",
            "topic_id",
            "topic_group",
            "knowledge_point",
            "year",
            "exam_time",
            "question_number",
            "question_summary",
            "topic_priority",
            "review_status",
            "practice_count",
            "last_practiced",
            "source_pdf",
            "source_page",
            "source_text_file",
            "source_image",
            "original_question_text",
            "answer_notes",
            "raw_text",
        ],
        questions,
    )

    write_csv(
        TOPIC_NOTE_FILE,
        ["topic_id", "topic_group", "note_order", "topic_priority", "note_text"],
        topic_notes,
    )

    print(f"Wrote {len(questions)} questions to {MASTER_FILE}")
    print(f"Wrote {len(topic_notes)} topic notes to {TOPIC_NOTE_FILE}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Populate original_question_text from extracted page text.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MASTER_FILE = ROOT / "data" / "processed" / "questions_master.csv"

ROMAN_MARKERS = ("i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x")


def load_rows() -> tuple[list[str], list[dict[str, str]]]:
    with MASTER_FILE.open("r", encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return reader.fieldnames or [], list(reader)


def save_rows(fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with MASTER_FILE.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def normalize_lines(text: str) -> list[str]:
    lines = []
    for raw_line in text.splitlines():
        line = re.sub(r"\s+", " ", raw_line).strip()
        if line:
            lines.append(line)
    return lines


def parse_question_number(question_number: str) -> tuple[str, list[str]]:
    root_match = re.match(r"Q?(\d+)", question_number.strip(), flags=re.IGNORECASE)
    root = root_match.group(1) if root_match else ""
    markers = [part.lower() for part in re.findall(r"\(([^)]+)\)", question_number)]
    return root, markers


def is_root_marker(line: str, root: str) -> bool:
    return bool(re.match(rf"^{re.escape(root)}\.(?!\d)(?:\s|$)", line))


def is_alpha_marker(line: str, marker: str) -> bool:
    return bool(re.match(rf"^\({re.escape(marker)}\)\s*", line, flags=re.IGNORECASE))


def is_roman_marker(line: str, marker: str) -> bool:
    return bool(re.match(rf"^{re.escape(marker)}\.\s*", line, flags=re.IGNORECASE))


def is_any_alpha_marker(line: str) -> bool:
    return bool(re.match(r"^\([a-z]\)\s*", line, flags=re.IGNORECASE))


def is_any_roman_marker(line: str) -> bool:
    return bool(re.match(r"^(i|ii|iii|iv|v|vi|vii|viii|ix|x)\.\s*", line, flags=re.IGNORECASE))


def next_boundary(lines: list[str], start: int, predicate) -> int:
    for index in range(start + 1, len(lines)):
        if predicate(lines[index]):
            return index
    return len(lines)


def extract_root_block(lines: list[str], root: str) -> list[str]:
    start = 0
    for index, line in enumerate(lines):
        if is_root_marker(line, root):
            start = index
            break

    end = len(lines)
    for index in range(start + 1, len(lines)):
        if re.match(r"^\d+\.(?!\d)(?:\s|$)", lines[index]) or lines[index].startswith("Page "):
            end = index
            break

    return lines[start:end]


def extract_alpha_block(lines: list[str], marker: str) -> list[str]:
    for index, line in enumerate(lines):
        if is_alpha_marker(line, marker):
            end = next_boundary(lines, index, lambda value: is_any_alpha_marker(value))
            return lines[index:end]
    return lines


def extract_single_roman_block(lines: list[str], marker: str) -> list[str]:
    for index, line in enumerate(lines):
        if is_roman_marker(line, marker):
            end = next_boundary(lines, index, lambda value: is_any_roman_marker(value))
            return lines[index:end]
    return lines


def extract_roman_range_block(lines: list[str], markers: list[str]) -> list[str]:
    start = None
    for index, line in enumerate(lines):
        if is_roman_marker(line, markers[0]):
            start = index
            break
    if start is None:
        return lines

    marker_positions = [index for index, line in enumerate(lines) if is_any_roman_marker(line)]
    end = len(lines)
    for position in marker_positions:
        if position <= start:
            continue
        marker_match = re.match(r"^(i|ii|iii|iv|v|vi|vii|viii|ix|x)\.\s*", lines[position], flags=re.IGNORECASE)
        if marker_match and marker_match.group(1).lower() not in markers:
            end = position
            break
    return lines[start:end]


def flatten_block(lines: list[str]) -> str:
    text = "\n".join(lines).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def extract_question_text(page_text: str, question_number: str) -> str:
    root, markers = parse_question_number(question_number)
    lines = normalize_lines(page_text)
    if not root or not lines:
        return ""

    block = extract_root_block(lines, root)
    if not markers:
        return flatten_block(block)

    alpha_markers = [marker for marker in markers if len(marker) == 1 and marker.isalpha()]
    roman_markers = [marker for marker in markers if marker in ROMAN_MARKERS]

    if alpha_markers:
        block = extract_alpha_block(block, alpha_markers[0])

    if len(roman_markers) == 1:
        block = extract_single_roman_block(block, roman_markers[0])
    elif len(roman_markers) > 1:
        block = extract_roman_range_block(block, roman_markers)

    return flatten_block(block)


def main() -> None:
    fieldnames, rows = load_rows()
    updated = 0

    for row in rows:
        text_file = row["source_text_file"].strip()
        question_number = row["question_number"].strip()
        if not text_file or not question_number:
            continue

        page_path = ROOT / text_file
        if not page_path.exists():
            continue

        page_text = page_path.read_text(encoding="utf-8", errors="ignore")
        question_text = extract_question_text(page_text, question_number)
        if question_text:
            row["original_question_text"] = question_text
            updated += 1

    save_rows(fieldnames, rows)
    print(f"Populated original_question_text for {updated} questions in {MASTER_FILE}")


if __name__ == "__main__":
    main()

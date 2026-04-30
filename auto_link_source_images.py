#!/usr/bin/env python3
"""
Auto-link master questions to extracted PDF pages and images.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MASTER_FILE = ROOT / "data" / "processed" / "questions_master.csv"
TEXT_DIR = ROOT / "extracted" / "text"
IMAGE_DIR = ROOT / "extracted" / "images"

PAGE_RE = re.compile(r"^(?P<pdf_name>.+)_page_(?P<page>\d+)\.txt$")
QUESTION_RE = re.compile(r"(?<!\w)(\d+)\s*[\.\)]")


@dataclass
class PageRecord:
    pdf_name: str
    exam_year: str
    page_number: int
    text_path: Path
    image_path: Path
    text_lower: str
    question_roots: set[str]


def normalize_tokens(text: str) -> set[str]:
    return {
        token
        for token in re.findall(r"[\w\u4e00-\u9fff']+", text.lower())
        if len(token) > 1
    }


def main_question_root(question_number: str) -> str:
    match = re.match(r"Q?(\d+)", question_number.strip(), flags=re.IGNORECASE)
    return match.group(1) if match else ""


def question_components(question_number: str) -> tuple[str, list[str]]:
    root = main_question_root(question_number)
    parts = re.findall(r"\(([^)]+)\)", question_number)
    return root, [part.lower() for part in parts]


def infer_exam_year(text: str, pdf_name: str) -> str:
    match = re.search(r"\b(20\d{2})\b", text)
    if match:
        return match.group(1)

    match = re.search(r"(20\d{2})", pdf_name)
    return match.group(1) if match else ""


def load_pages() -> list[PageRecord]:
    raw_pages: list[dict[str, object]] = []
    for text_path in sorted(TEXT_DIR.glob("*.txt")):
        match = PAGE_RE.match(text_path.name)
        if not match:
            continue

        pdf_name = match.group("pdf_name")
        page_number = int(match.group("page"))
        image_path = IMAGE_DIR / f"{pdf_name}_page_{page_number:02d}.png"
        if not image_path.exists():
            continue

        text = text_path.read_text(encoding="utf-8", errors="ignore")
        roots = {value for value in QUESTION_RE.findall(text)}
        raw_pages.append(
            {
                "pdf_name": pdf_name,
                "page_number": page_number,
                "text_path": text_path,
                "image_path": image_path,
                "text": text,
                "text_lower": text.lower(),
                "question_roots": roots,
            }
        )

    pdf_years: dict[str, str] = {}
    for page in raw_pages:
        if page["page_number"] == 1:
            pdf_years[page["pdf_name"]] = infer_exam_year(str(page["text"]), str(page["pdf_name"]))

    pages: list[PageRecord] = []
    for page in raw_pages:
        pdf_name = str(page["pdf_name"])
        pages.append(
            PageRecord(
                pdf_name=pdf_name,
                exam_year=pdf_years.get(pdf_name, infer_exam_year(str(page["text"]), pdf_name)),
                page_number=int(page["page_number"]),
                text_path=Path(page["text_path"]),
                image_path=Path(page["image_path"]),
                text_lower=str(page["text_lower"]),
                question_roots=set(page["question_roots"]),
            )
        )
    return pages


def load_rows() -> tuple[list[str], list[dict[str, str]]]:
    with MASTER_FILE.open("r", encoding="utf-8", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        return reader.fieldnames or [], list(reader)


def save_rows(fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with MASTER_FILE.open("w", encoding="utf-8", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def select_candidate_pages(row: dict[str, str], pages: list[PageRecord]) -> list[PageRecord]:
    year = row["year"].strip()
    root = main_question_root(row["question_number"])

    candidates = [
        page
        for page in pages
        if (not year or year == page.exam_year)
        and (not root or root in page.question_roots)
    ]
    if candidates:
        return candidates

    return [page for page in pages if not year or year == page.exam_year]


def score_page(row: dict[str, str], page: PageRecord) -> int:
    score = 0
    root, parts = question_components(row["question_number"])
    if root and root in page.question_roots:
        score += 10

    for part in parts:
        if len(part) == 1 and re.search(rf"\({re.escape(part)}\)", page.text_lower):
            score += 3
        elif re.search(rf"(?<!\w){re.escape(part)}[\.\)]", page.text_lower):
            score += 3

    query_tokens = normalize_tokens(f"{row['knowledge_point']} {row['question_summary']}")
    score += sum(1 for token in query_tokens if token in page.text_lower)
    return score


def link_rows(rows: list[dict[str, str]], pages: list[PageRecord]) -> tuple[int, int]:
    linked = 0

    for row in rows:
        row["source_pdf"] = ""
        row["source_page"] = ""
        row["source_text_file"] = ""
        row["source_image"] = ""

        candidates = select_candidate_pages(row, pages)
        if not candidates:
            continue

        best_page = max(candidates, key=lambda page: score_page(row, page))
        if score_page(row, best_page) <= 0:
            continue

        row["source_pdf"] = f"paper/{best_page.pdf_name}.pdf"
        row["source_page"] = str(best_page.page_number)
        row["source_text_file"] = str(best_page.text_path.relative_to(ROOT))
        row["source_image"] = str(best_page.image_path.relative_to(ROOT))
        linked += 1

    return linked, len(rows) - linked


def main() -> None:
    fieldnames, rows = load_rows()
    pages = load_pages()
    linked, unmatched = link_rows(rows, pages)
    save_rows(fieldnames, rows)
    print(f"Linked {linked} questions in {MASTER_FILE}")
    print(f"Left {unmatched} questions unmatched")


if __name__ == "__main__":
    main()

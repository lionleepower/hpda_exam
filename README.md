
## 简单运行方法

如果你只想快速用起来，推荐按下面步骤：

### 1. 进入目录并激活python环境

```bash
cd ~/edinburgh/hpda/finalexam
conda activate hpda_exam
```

### 2. 第一次使用时，先生成题库和网页数据

```bash
python rebuild_question_bank.py
```

这个脚本会自动依次运行：

```bash
python extract_papers.py
python parse_question_summary.py
python auto_link_source_images.py
python populate_original_question_text.py
```

### 3. 如果你想用终端刷题

```bash
python quiz_cli.py --open-image
```

这会在终端里显示题目，并自动打开对应题目的图片。

### 4. 如果你想用浏览器刷题，并且让进度写回 CSV(最推荐)

```bash
python serve_web_app.py
```

脚本会尝试自动打开默认浏览器。如果没有自动打开，再手动访问：

```text
http://127.0.0.1:8000
```

如果 `8000` 端口已被占用，脚本会自动切换到附近可用端口，并在终端输出最终地址。

这是目前最推荐的使用方式，因为：

- 题目图片会直接显示在页面里
- 可以改状态
- 可以写笔记
- 改动会直接保存回 `questions_master.csv`

### 5. 如果你只是想生成静态网页看看

```bash
python build_web_app.py
```

然后打开：

```text
output/web_app/index.html
```

这个模式更轻，但网页里的进度只保存在浏览器里，不会自动写回 CSV。




# Final Exam Practice Toolkit

A lightweight local study toolkit for organizing past exam questions by topic, linking them back to the original PDF pages, and practicing them through either:

- a terminal quiz tool
- a browser study page

The project is built around a single clean master question bank so that question metadata, notes, progress, and source links do not drift across multiple hand-edited files.

## Overview

This repository is designed for revision workflows where:

- the original exam papers are stored as PDF files
- a hand-written summary file groups questions by topic
- you want to practice by topic, by year, or by status
- you want quick access to the original question image while revising
- you want to keep notes and progress in one place

The toolkit keeps the original source material unchanged and regenerates everything else from it.

## Source Files That Stay Unchanged

These are the two source inputs that the rest of the project is built from:

- `paper/`
  Original PDF exam papers
- `questionSum.txt`
  Hand-written topic summary of the questions

Everything else can be rebuilt from these files.

## Main Features

- Parse `questionSum.txt` into a structured master question bank
- Keep one canonical editable dataset in `data/processed/questions_master.csv`
- Extract page text and page images from the PDF papers
- Auto-link each question to its original PDF page and page image
- Fill `original_question_text` from the linked exam page text
- Export per-topic CSV files
- Export per-topic Markdown study cards
- Practice in the terminal with optional image auto-open
- Practice in the browser with inline images
- Run a local browser study server that writes notes and status changes back to the CSV

## Recommended Project Workflow

The intended workflow is:

1. Keep your source PDFs in `paper/`
2. Keep your topic summary in `questionSum.txt`
3. Parse the summary into the master question bank
4. Extract page text/images from the PDFs
5. Link each question to its original exam page
6. Fill the original question text
7. Practice through CLI or browser

## Directory Structure

```text
finalexam/
├── paper/                         # Original PDF exam papers
├── questionSum.txt                # Hand-written topic summary
├── extracted/
│   ├── text/                      # Extracted page text from PDFs
│   └── images/                    # Rendered page images from PDFs
├── data/
│   └── processed/
│       ├── questions_master.csv   # Canonical editable question bank
│       └── topic_notes.csv        # Topic-level notes extracted from questionSum.txt
├── output/
│   ├── topic_sets/                # Per-topic CSV exports
│   ├── practice_cards/            # Per-topic Markdown cards
│   └── web_app/                   # Generated standalone browser page
├── parse_question_summary.py
├── extract_papers.py
├── auto_link_source_images.py
├── populate_original_question_text.py
├── rebuild_question_bank.py
├── create_exercise_files.py
├── generate_practice_cards.py
├── quiz_cli.py
├── build_web_app.py
├── serve_web_app.py
└── requirements.txt
```

## Core Data Files

### `data/processed/questions_master.csv`

This is the central dataset of the whole project.

You should treat this as the single source of truth for:

- question metadata
- source links
- original extracted question text
- progress
- notes

### `data/processed/topic_notes.csv`

This stores topic-level notes parsed from `questionSum.txt`, such as:

- revision priority notes
- formula reminders
- topic guidance text

## Master Question Bank Fields

The main columns in `questions_master.csv` are:

- `stable_id`
  Stable internal identifier for the question
- `topic_id`
  Numeric topic group id
- `topic_group`
  Full topic title from the summary file
- `knowledge_point`
  Fine-grained concept label
- `year`
  Exam year
- `exam_time`
  Exam date/time text
- `question_number`
  Original question number, such as `Q2(c)` or `Q1(a)(ii)`
- `question_summary`
  Short summary from `questionSum.txt`
- `topic_priority`
  Priority derived from the topic notes
- `review_status`
  Current study status, such as `new`, `review`, or `done`
- `practice_count`
  Number of times the question has been practiced
- `last_practiced`
  Timestamp of the last practice interaction
- `source_pdf`
  Relative path to the original PDF paper
- `source_page`
  Original page number in the PDF
- `source_text_file`
  Extracted page text file used for matching
- `source_image`
  Rendered page image for the question
- `original_question_text`
  Original or near-original question text extracted from the page
- `answer_notes`
  User notes and reminders

## Script Guide

### `parse_question_summary.py`

Parses `questionSum.txt` into:

- `data/processed/questions_master.csv`
- `data/processed/topic_notes.csv`

Use this when:

- you changed `questionSum.txt`
- you want to rebuild the master question bank from scratch

### `extract_papers.py`

Extracts text and rendered page images from the PDFs in `paper/` into:

- `extracted/text/`
- `extracted/images/`

Use this when:

- you added or replaced PDF papers
- you want to regenerate page images or extracted page text

### `auto_link_source_images.py`

Links each question in `questions_master.csv` to:

- `source_pdf`
- `source_page`
- `source_text_file`
- `source_image`

Use this after:

- parsing the summary
- extracting the PDF text/images

### `populate_original_question_text.py`

Uses the linked page text to fill `original_question_text`.

This is especially useful for:

- browser revision
- terminal revision
- Markdown card exports

### `rebuild_question_bank.py`

Runs the full rebuild pipeline in the correct order:

- `extract_papers.py`
- `parse_question_summary.py`
- `auto_link_source_images.py`
- `populate_original_question_text.py`

Use this when:

- you want a single command to rebuild the question bank
- you updated source PDFs or `questionSum.txt`
- you do not want to rerun each step manually

### `create_exercise_files.py`

Exports one CSV file per topic into:

- `output/topic_sets/`

These are derived files and can be rebuilt at any time.

### `generate_practice_cards.py`

Exports one Markdown card file per topic into:

- `output/practice_cards/`

Each card file includes:

- summary
- original question text
- source image path
- source PDF/page

### `quiz_cli.py`

Terminal-based study mode.

Features:

- choose topics
- choose session size
- shuffle or preserve order
- mark questions as `new`, `review`, or `done`
- add notes
- open the linked image with `o`
- auto-open the linked image with `--open-image`

This mode writes progress directly to `questions_master.csv`.

### `build_web_app.py`

Builds a standalone local browser page:

- `output/web_app/index.html`

This mode is useful when you want:

- inline images
- visual navigation
- quick filtering

The standalone page stores progress in browser local storage only.

### `serve_web_app.py`

Starts a local browser study server.

Features:

- serves the browser page dynamically
- loads the latest `questions_master.csv`
- writes changes back to `questions_master.csv`

This is the best mode when you want:

- browser-based revision
- inline images
- notes/status synced to the CSV
- shared progress with `quiz_cli.py`

## Setup

The project was designed to be used in a local Python environment such as:

```bash
conda activate hpda_exam
```

Dependencies listed in `requirements.txt` are intentionally small and mainly cover PDF extraction:

- `PyMuPDF`
- `Pillow`

Install with:

```bash
pip install -r requirements.txt
```

## Full Rebuild Workflow

If you want to rebuild everything from the two source inputs, run:

```bash
conda activate hpda_exam
python rebuild_question_bank.py
python create_exercise_files.py
python generate_practice_cards.py
python build_web_app.py
```

Equivalent manual steps:

```bash
python extract_papers.py
python parse_question_summary.py
python auto_link_source_images.py
python populate_original_question_text.py
```

## How To Use The Terminal Quiz

Start basic terminal mode:

```bash
python quiz_cli.py
```

Open the image automatically for each question:

```bash
python quiz_cli.py --open-image
```

Useful options:

```bash
python quiz_cli.py --list-topics
python quiz_cli.py --topic 4 --limit 5
python quiz_cli.py --topic 1 4 7 --limit 10 --no-shuffle
```

## How To Use The Browser Page

### Option 1: Standalone HTML

Generate the page:

```bash
python build_web_app.py
```

Then open:

```text
output/web_app/index.html
```

This mode is easy to share and browse, but progress is stored only in the browser.

### Option 2: Browser Page With CSV Sync

Start the server:

```bash
python serve_web_app.py
```

The script will try to open your default browser automatically. If it does not, open this manually:

```text
http://127.0.0.1:8000
```

If port `8000` is already occupied, the server will automatically switch to a nearby free port and print the final URL in the terminal.

This mode writes status and notes directly back to:

- `data/processed/questions_master.csv`

## Static Browser Mode vs Server Browser Mode

### Static `index.html`

Pros:

- simplest to open
- no local server needed
- works well for browsing and lightweight practice

Cons:

- progress stays in browser local storage
- does not update the CSV directly

### `serve_web_app.py`

Pros:

- status changes sync back to the CSV
- notes sync back to the CSV
- shared progress with terminal mode

Cons:

- requires running a local server

## Files You Are Expected To Edit

Normally you only edit:

- `questionSum.txt`
- `data/processed/questions_master.csv`

You generally should not hand-edit:

- `output/topic_sets/`
- `output/practice_cards/`
- `output/web_app/index.html`

Those are generated files.

## GitHub Notes

If you are pushing this project to GitHub, it is a good idea to make clear in the repository description that:

- the source PDFs may be course materials and may not be suitable for public redistribution depending on your permissions
- the generated outputs in `output/` are rebuildable
- the editable revision dataset is `data/processed/questions_master.csv`

If needed, you can later add a `.gitignore` depending on whether you want to track generated outputs such as:

- `output/`
- `extracted/`

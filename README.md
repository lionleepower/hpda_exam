# Final Exam Practice Toolkit

A local-first study toolkit for turning past exam papers and topic summaries into a structured, interactive personal question bank.

This project supports:

- PDF-based past paper extraction
- topic-organized question banks
- source page and image linking
- extracted original question text
- terminal-based revision
- browser-based revision
- CSV-backed progress and notes

## 简单运行方法

### 1. 进入目录并激活环境

```bash
cd ~/edinburgh/hpda/finalexam
conda activate hpda_exam
```

### 2. 第一次使用时，先生成题库

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

### 3. 日常最推荐的刷题方式

```bash
python serve_web_app.py
```

脚本会尝试自动打开默认浏览器。
如果没有自动打开，就手动访问终端里打印出来的网址。
默认通常是：

```text
http://127.0.0.1:8000
```

如果 `8000` 端口被占用，脚本会自动切换到附近可用端口，并把最终地址打印出来。

### 4. 如果你想用终端刷题

```bash
python quiz_cli.py --open-image
```

这会在终端里显示题目，并自动打开对应题目的图片。

## Important Note About PDF Papers

This repository does **not** need to include original exam paper PDFs.

If you use this project yourself, place your own PDF papers inside:

```text
paper/
```

If you publish this repository publicly, it is safer **not** to redistribute exam paper PDFs unless you are sure you have permission to do so.

## What You Put In Manually

You are expected to provide:

- `paper/`
  Your own source PDF papers
- `questionSum.txt`
  Your own hand-written question summary grouped by topic

Everything else can be generated from those two inputs.

## Main Outputs

- `data/processed/questions_master.csv`
  The canonical question bank
- `data/processed/topic_notes.csv`
  Topic-level notes extracted from `questionSum.txt`
- `output/topic_sets/`
  Per-topic CSV exports
- `output/practice_cards/`
  Per-topic Markdown exports
- `output/web_app/index.html`
  Standalone browser revision page

## Directory Structure

```text
finalexam/
├── paper/                         # Put your own PDF exam papers here
├── questionSum.txt                # Your hand-written topic summary
├── extracted/
│   ├── text/                      # Extracted page text from PDFs
│   └── images/                    # Rendered page images from PDFs
├── data/
│   └── processed/
│       ├── questions_master.csv   # Canonical editable question bank
│       └── topic_notes.csv        # Topic-level notes
├── output/
│   ├── topic_sets/                # Per-topic CSV exports
│   ├── practice_cards/            # Per-topic Markdown cards
│   └── web_app/                   # Browser app output
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

## Setup

Recommended environment:

```bash
conda activate hpda_exam
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Dependencies are intentionally small and mainly cover PDF extraction:

- `PyMuPDF`
- `Pillow`

## Quick Start

### 1. Enter the project directory

```bash
cd ~/edinburgh/hpda/finalexam
conda activate hpda_exam
```

### 2. Put your PDF papers into `paper/`

Example:

```text
paper/
├── ExamPaper-2022.pdf
├── ExamPaper-2023.pdf
└── ExamPaper-2024.pdf
```

### 3. Build the question bank

```bash
python rebuild_question_bank.py
```

This runs:

```bash
python extract_papers.py
python parse_question_summary.py
python auto_link_source_images.py
python populate_original_question_text.py
```

### 4. Start revising

Terminal mode:

```bash
python quiz_cli.py --open-image
```

Browser mode with CSV sync:

```bash
python serve_web_app.py
```

The script will try to open your default browser automatically.

If it does not, open the printed URL manually.
By default this is usually:

```text
http://127.0.0.1:8000
```

If port `8000` is occupied, the script will automatically switch to a nearby free port and print the final URL.

## Recommended Workflow

### Full rebuild workflow

Use this when:

- you added or replaced PDF papers
- you changed `questionSum.txt`
- you want to regenerate the question bank from scratch

```bash
python rebuild_question_bank.py
python create_exercise_files.py
python generate_practice_cards.py
python build_web_app.py
```

### Day-to-day usage

If your question bank is already built, you usually only need:

```bash
python serve_web_app.py
```

or:

```bash
python quiz_cli.py --open-image
```

## Script Guide

### `extract_papers.py`

Extracts text and rendered page images from the PDFs in `paper/` into:

- `extracted/text/`
- `extracted/images/`

### `parse_question_summary.py`

Parses `questionSum.txt` into:

- `data/processed/questions_master.csv`
- `data/processed/topic_notes.csv`

### `auto_link_source_images.py`

Links each question to:

- source PDF
- source page
- source text file
- source image

### `populate_original_question_text.py`

Extracts near-original question text from the linked page text.

### `rebuild_question_bank.py`

Runs the full rebuild pipeline in the correct order.

### `create_exercise_files.py`

Exports per-topic CSV files to:

- `output/topic_sets/`

### `generate_practice_cards.py`

Exports per-topic Markdown cards to:

- `output/practice_cards/`

### `quiz_cli.py`

Terminal-based study mode.

Features:

- choose topics
- choose question count
- shuffle or preserve order
- mark `new`, `review`, or `done`
- add notes
- open linked images

Progress is written back to:

- `data/processed/questions_master.csv`

### `build_web_app.py`

Builds a standalone browser page:

- `output/web_app/index.html`

This mode stores progress only in browser local storage.

### `serve_web_app.py`

Runs a local browser server.

Features:

- serves the browser study page
- loads the latest CSV data
- writes notes and status updates back to `questions_master.csv`
- auto-opens the browser
- auto-switches port if `8000` is occupied

This is the recommended mode for daily use.

## Master Question Bank Fields

The main fields in `data/processed/questions_master.csv` are:

- `stable_id`
- `topic_id`
- `topic_group`
- `knowledge_point`
- `year`
- `exam_time`
- `question_number`
- `question_summary`
- `topic_priority`
- `review_status`
- `practice_count`
- `last_practiced`
- `source_pdf`
- `source_page`
- `source_text_file`
- `source_image`
- `original_question_text`
- `answer_notes`

## Browser Mode vs Terminal Mode

### Browser mode

Best when you want:

- inline question images
- easier visual navigation
- quick filtering
- synced notes/status in a browser

Recommended command:

```bash
python serve_web_app.py
```

### Terminal mode

Best when you want:

- fast keyboard-driven practice
- a lightweight workflow
- quick topic drills

Recommended command:

```bash
python quiz_cli.py --open-image
```

## Public Repository Safety

If this repository is public, a safer approach is:

- commit code
- commit generated structure if you want
- do **not** commit exam PDFs unless you are certain redistribution is allowed

For public sharing, users can create their own `paper/` directory locally and place their legally obtained papers there.

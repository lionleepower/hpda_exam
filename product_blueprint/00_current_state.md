# Current State Reference

This document captures what the current `finalexam` project already does well, so future product work can reuse the right parts instead of rebuilding everything from scratch.

## Current Source Inputs

The current project is built from two primary source inputs:

- `paper/`
  Original exam PDFs
- `questionSum.txt`
  Topic-organized question summary

## Current Generated Layers

### Extracted Layer

- `extracted/text/`
  Per-page text extracted from each PDF
- `extracted/images/`
  Per-page rendered images from each PDF

### Processed Layer

- `data/processed/questions_master.csv`
  The current single source of truth for the question bank
- `data/processed/topic_notes.csv`
  Topic-level notes parsed from `questionSum.txt`

### Output Layer

- `output/topic_sets/`
  Per-topic CSV exports
- `output/practice_cards/`
  Per-topic Markdown exports
- `output/web_app/index.html`
  Standalone browser study page

## Current Application Entry Points

- `extract_papers.py`
  Extracts page text and images from PDFs
- `parse_question_summary.py`
  Parses `questionSum.txt` into the master question bank
- `auto_link_source_images.py`
  Links questions to source pages and images
- `populate_original_question_text.py`
  Extracts original question text from the linked page text
- `quiz_cli.py`
  Terminal practice mode
- `build_web_app.py`
  Generates a standalone browser page
- `serve_web_app.py`
  Runs a local browser server with CSV-backed syncing

## Current Strengths

- Already has a single master question dataset
- Already supports both terminal and browser practice
- Already links questions back to PDF page images
- Already extracts near-original question text
- Already supports tracking notes and revision status
- Already has a workable local-first architecture

## Current Limitations

- The project is still conceptually tied to one course
- `questionSum.txt` is still a strong assumption in the pipeline
- The input model is not yet generalized for other subjects
- The browser app is generated from the current CSV model rather than from a generalized product API
- Data persistence is CSV-based rather than using a more flexible storage abstraction

## Reusable Assets For Future Product Work

The following parts are highly reusable:

- PDF extraction workflow
- question/source page matching logic
- original question text extraction logic
- master question bank field design
- browser study interaction model
- CLI revision flow

The following parts should eventually be generalized:

- HPDA-specific file naming assumptions
- `questionSum.txt` parsing assumptions
- topic labeling logic
- build pipeline assumptions about exam question numbering

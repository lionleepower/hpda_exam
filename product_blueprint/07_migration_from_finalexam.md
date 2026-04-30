# Migration From Current Finalexam Project

This document maps current assets to future product responsibilities.

## Current Asset -> Future Product Role

### `paper/`

Future role:

- source library

### `questionSum.txt`

Future role:

- optional enriched metadata input

### `extracted/text/`

Future role:

- derived processing cache

### `extracted/images/`

Future role:

- derived processing cache

### `data/processed/questions_master.csv`

Future role:

- canonical question dataset

### `data/processed/topic_notes.csv`

Future role:

- topic metadata dataset

### `quiz_cli.py`

Future role:

- CLI study interface

### `build_web_app.py`

Future role:

- static export view generator

### `serve_web_app.py`

Future role:

- local synced browser application server

## What Should Be Preserved

- source-page linking logic
- original question text extraction logic
- stable question identifiers
- browser-based practice concepts
- progress tracking fields

## What Should Be Reframed

- course-specific naming
- assumptions about topic formatting
- assumptions about the summary file being mandatory

## Suggested Migration Strategy

1. Keep the current `finalexam` project usable
2. Extract generic modules gradually
3. Build a product-oriented package beside, not inside, the current scripts
4. Only rename or relocate files after shared abstractions are stable

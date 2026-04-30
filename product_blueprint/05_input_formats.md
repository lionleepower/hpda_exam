# Input Formats Draft

The future product should not depend only on `questionSum.txt`.

It should support at least two levels of input.

## Level 1: Minimal Input

Required:

- one or more PDF files

This should allow:

- page extraction
- page image generation
- page-level browsing
- basic question bank initialization

## Level 2: Enriched Input

Optional:

- summary text file
- CSV metadata file
- JSON metadata file
- Markdown topic file

This should allow:

- topic labeling
- short summaries
- priorities
- year correction
- better source matching

## Candidate Generic Formats

### Option A: Plain Topic Summary Text

Equivalent to the current `questionSum.txt`.

Good for:

- fast manual editing
- lightweight workflows

Weakness:

- fragile format assumptions

### Option B: CSV Metadata

Suggested fields:

- `question_number`
- `topic`
- `summary`
- `priority`
- `year`

Good for:

- spreadsheets
- batch editing
- portability

### Option C: JSON/JSONL

Good for:

- structured programmatic use
- richer future extensions

## Product Recommendation

The future product should aim to support:

1. PDF-only mode
2. PDF + summary text mode
3. PDF + CSV metadata mode

That will already make it much more general than the current HPDA-specific workflow.

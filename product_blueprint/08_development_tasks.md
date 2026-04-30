# Development Tasks

This file is intended to be used later as an execution checklist.

## Stage 1: Product Framing

- choose a product name
- choose neutral terminology for source/question/topic/progress
- define supported input modes
- define MVP boundaries

## Stage 2: Codebase Modularization

- extract shared CSV read/write helpers
- extract shared question update logic
- extract shared source-linking logic
- extract shared original-text extraction logic
- reduce duplication between CLI and browser update flows

## Stage 3: Storage and Data Layer

- define a storage abstraction
- keep CSV compatibility
- evaluate whether SQLite is needed for v2

## Stage 4: Generic Import Pipeline

- support PDF-only bootstrap
- support optional summary text import
- support CSV metadata import
- define import validation rules

## Stage 5: Browser Product Improvements

- add saved filter presets
- add review-only session mode
- add due-later or weak-question mode
- add better source PDF navigation
- add a cleaner split view for text + image

## Stage 6: Packaging

- create a reusable package structure
- create a top-level launcher command
- prepare GitHub-ready documentation
- decide which generated artifacts belong in version control

## Stage 7: Quality and Validation

- create a small sample dataset for testing
- add regression tests for question parsing
- add regression tests for source linking
- add regression tests for original question text extraction
- test browser syncing workflow end to end

## Suggested First Technical Milestone

If development starts soon, the best first milestone is:

**Refactor the current scripts into reusable internal modules without changing user-visible behavior.**

That gives the future product a much stronger foundation than adding more features immediately.

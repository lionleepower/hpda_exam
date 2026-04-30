# Roadmap Draft

## Phase 0: Stabilize The Current Toolkit

Goal:

- keep the current `finalexam` project usable
- preserve existing workflows

Already mostly achieved:

- single master CSV
- browser mode
- CLI mode
- source linking

## Phase 1: Extract Product Concepts

Goal:

- rename the project conceptually away from HPDA
- define generic terminology
- move from course-specific framing to product framing

Tasks:

- define generic source model
- define generic question model
- define generic import modes

## Phase 2: Modularize The Codebase

Goal:

- separate import logic, processing logic, storage logic, and UI logic

Tasks:

- shared data access module
- shared update/save helpers
- reusable question matching module
- reusable question extraction module

## Phase 3: Generalize Inputs

Goal:

- allow use without `questionSum.txt`

Tasks:

- PDF-only bootstrap mode
- CSV metadata import mode
- summary file abstraction

## Phase 4: Refine Browser Product

Goal:

- make the browser interface the main user-facing product

Tasks:

- session presets
- review-only mode
- due-for-review mode
- better note UX
- better source image navigation

## Phase 5: Optional Storage Upgrade

Goal:

- improve maintainability for larger question banks

Possible path:

- keep CSV export
- add SQLite-backed storage internally

## Phase 6: Packaging

Goal:

- make the product easier to install and reuse

Possible outputs:

- pip-installable package
- local desktop launcher
- reusable CLI entrypoint

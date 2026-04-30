# Architecture Draft

## High-Level Architecture

The future product should be broken into four layers.

## 1. Source Layer

Responsible for raw user material.

Examples:

- PDFs
- summary text files
- CSV imports
- JSON imports

This layer should remain untouched whenever possible.

## 2. Processing Layer

Responsible for transforming source material into structured question data.

Responsibilities:

- PDF text extraction
- page image rendering
- question parsing
- source linking
- metadata enrichment

## 3. Data Layer

Responsible for canonical structured storage.

Core data:

- questions
- topics
- notes
- progress
- source references

In the current project this is CSV-based.
In the future product, this could remain CSV-backed initially, or move to SQLite while keeping export compatibility.

## 4. Interface Layer

Responsible for user-facing interaction.

Possible interfaces:

- CLI
- browser app
- export views

These should consume the same canonical question model rather than each maintaining separate logic.

## Suggested Internal Modules

### `importers`

- PDF importer
- summary importer
- CSV importer

### `processors`

- text extraction
- page rendering
- question matcher
- topic linker

### `models`

- question
- source
- topic
- progress

### `storage`

- CSV adapter
- optional future SQLite adapter

### `interfaces`

- CLI interface
- web interface
- export interface

## Design Principle

The browser app and CLI should not own the business logic.
They should sit on top of shared import, processing, and storage logic.

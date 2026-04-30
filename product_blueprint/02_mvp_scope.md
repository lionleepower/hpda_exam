# MVP Scope

This document defines what the first independent product version should include.

## MVP Goal

The first version should let a user take their own local materials and turn them into a usable personal question bank.

## In Scope

### Import

- import one or more PDFs
- optionally import a topic summary file
- generate a structured question bank

### Structuring

- store questions in one canonical dataset
- attach topic, year, status, and notes
- link questions to source PDF pages and images
- store original extracted question text

### Practice

- filter questions by topic
- filter questions by year
- filter questions by status
- practice through browser UI
- practice through CLI

### Tracking

- mark `new`
- mark `review`
- mark `done`
- save notes
- save practice count and last practiced time

### Output

- export per-topic study files
- export a standalone browser version

## Out Of Scope For MVP

- multi-user accounts
- cloud sync
- advanced authentication
- AI-generated answers
- OCR-heavy image-only papers as a first priority
- collaborative editing
- plugin ecosystem
- mobile app
- hosted SaaS deployment

## Product Test For MVP

The MVP is successful if a new user can:

1. provide local source files
2. generate a question bank
3. view original questions and images
4. revise by topic
5. save notes and status
6. continue revision later without losing progress

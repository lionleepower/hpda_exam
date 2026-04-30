# Data Model Draft

## Core Entities

The future product should revolve around five main entities.

## 1. Source

Represents an original input source.

Suggested fields:

- `source_id`
- `source_type`
- `source_path`
- `display_name`
- `year`
- `page_count`

## 2. Question

Represents a single question or sub-question.

Suggested fields:

- `question_id`
- `source_id`
- `question_number`
- `question_type`
- `topic_ids`
- `year`
- `summary`
- `original_text`
- `source_page`
- `source_image`
- `priority`

## 3. Topic

Represents a topic, tag, chapter, or concept group.

Suggested fields:

- `topic_id`
- `name`
- `description`
- `priority_default`

## 4. Progress

Represents user study progress for a question.

Suggested fields:

- `question_id`
- `status`
- `notes`
- `practice_count`
- `last_practiced`

## 5. Session

Represents a generated practice set.

Suggested fields:

- `session_id`
- `created_at`
- `filters`
- `question_ids`

## Recommendation For Early Versions

For the first reusable product version, a flat CSV or JSONL structure is still acceptable if it preserves:

- a stable question id
- explicit source references
- explicit progress fields
- flexible topic references

A later version can move to SQLite without changing the product definition.

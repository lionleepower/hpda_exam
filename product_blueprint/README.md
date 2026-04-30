# Product Blueprint

This folder is a local planning package for turning the current `finalexam` project into a more independent, reusable product.

It does not replace the current working toolkit. Instead, it serves as:

- a product definition reference
- a development planning reference
- a migration guide from the current HPDA-oriented project
- a checklist for future implementation work

## Files

- `00_current_state.md`
  Snapshot of the current project and what already exists
- `01_product_vision.md`
  Product definition, positioning, and goals
- `02_mvp_scope.md`
  What the first independent version should and should not do
- `03_architecture.md`
  High-level product architecture and system decomposition
- `04_data_model.md`
  Core entities and suggested data model
- `05_input_formats.md`
  Suggested generic input formats beyond the current HPDA setup
- `06_roadmap.md`
  Suggested staged development roadmap
- `07_migration_from_finalexam.md`
  Mapping from the current project to the future product
- `08_development_tasks.md`
  Concrete task list for future implementation

## Suggested Use

When future development starts, use this folder in the following order:

1. Read `01_product_vision.md`
2. Confirm scope with `02_mvp_scope.md`
3. Use `03_architecture.md` and `04_data_model.md` as implementation references
4. Use `07_migration_from_finalexam.md` to avoid losing useful work from the current project
5. Execute work in `08_development_tasks.md`

# PDF / Word Technical Translator

PDF / Word Technical Translator is a tool project for converting Chinese technical documents into professional, editable English DOCX documents.

The project is not a one-off translation workspace. It is intended to become a reusable pipeline for technical manuals, engineering documents, wiring guides, service instructions, and similar documents.

## Goal

Convert Chinese PDF or Word technical documents into editable English Word documents while preserving document structure as much as possible.

Primary output:

- `translated_editable.docx`
- `translation_report.md`
- `images_to_translate/`
- `image_mapping.json`

## Core Principles

- Body text must become editable Word text.
- Headings must use Word heading styles.
- Tables must become Word tables where feasible.
- Images must be inserted as independent image objects.
- Full-page screenshots must not be used as a substitute for document reconstruction.
- Image translation is handled separately by ChatGPT or another image-editing workflow.
- This tool exports images and records their positions; it does not directly translate text inside images.
- Quality checks must block failed outputs.

## Current Phase

Milestone 1 establishes the project skeleton, typed module boundaries, CLI entry points, logging configuration, and basic smoke tests.

PDF parsing, translation, DOCX generation, image export, image backfill, and document validation remain explicit placeholders. No sample documents are included.

## Documentation

- [Project Guidelines](docs/PROJECT_GUIDELINES.md)
- [Workflow](docs/WORKFLOW.md)
- [Agent Development Guide](AGENTS.md)
- [QA Checklist](docs/QA_CHECKLIST.md)
- [Terminology](docs/TERMINOLOGY.md)

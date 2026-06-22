# AI Rules

These rules apply to Codex, ChatGPT, and any AI agent working on this repository.

## Required Reading

Before modifying code, prompts, workflows, or generated document logic, AI agents must read:

- `docs/PROJECT_GUIDELINES.md`
- `docs/WORKFLOW.md`
- `docs/AI_RULES.md`
- `docs/QA_CHECKLIST.md`
- `docs/TERMINOLOGY.md`

## General Rules

1. Do not treat this project as a one-off document translation task.
2. Do not upload sample PDFs, DOCX files, images, or customer documents unless explicitly requested.
3. Do not migrate old project outputs into this repository.
4. Do not add generated translation artifacts to the repository by default.
5. Keep the project generic and reusable.

## DOCX Rules

The generated DOCX must be editable.

AI agents must not:

- Insert full-page screenshots as Word pages.
- Flatten body text into images.
- Use images as a substitute for paragraphs.
- Use images as a substitute for Word tables where structured tables are feasible.

AI agents must:

- Generate body text as Word paragraphs.
- Generate titles and sections using Word Heading styles.
- Generate tables as Word tables.
- Insert images as independent image objects.

## Image Translation Rules

Image translation is not performed by the core program.

The program only:

- Exports images.
- Records image metadata.
- Records insertion position.
- Supports later image replacement.

ChatGPT or another image workflow handles image translation separately.

The core program must not:

- OCR image annotations for automatic replacement.
- Cover Chinese text inside images.
- Redraw callouts, arrows, bubbles, or labels.
- Directly translate image pixels.

## Image Backfill Rules

When translated images are returned, the program may replace images in the DOCX.

Replacement must:

- Use `image_mapping.json`.
- Preserve original image size.
- Preserve original image position.
- Preserve original aspect ratio.
- Avoid changing surrounding text layout.

## QA Rules

A generated document must fail QA if:

- Editable text is near zero.
- Most or all pages are full-page images.
- Paragraph count is abnormally low.
- Expected tables are missing.
- Images are not independent objects.
- Chinese text remains in editable body text.
- Image mapping is missing or incomplete.

AI agents must not mark an output complete when QA fails.

## Repository Safety Rules

Do not push changes unless the user explicitly confirms.

Do not change git remotes unless the user explicitly confirms.

Do not commit generated outputs unless the user explicitly requests it.


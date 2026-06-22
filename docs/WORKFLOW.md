# Workflow

This document defines the intended end-to-end workflow for PDF / Word Technical Translator.

## Overview

```text
PDF / Word input
  -> Text extraction
  -> Table extraction
  -> Image export
  -> Body text translation
  -> Editable DOCX generation
  -> ChatGPT image translation
  -> Image backfill
  -> QA checks
  -> Final export
```

## 1. Input

Supported source formats:

- PDF
- Word DOCX

The source document should be treated as the authoritative layout reference.

The pipeline must not assume that every document has the same structure.

## 2. Text Extraction

The parser extracts:

- Body text
- Headings
- Numbered lists
- Page headers
- Page footers
- Captions
- Notes
- Technical terms

Each text block should retain:

- Source page number
- Bounding box or logical position
- Original text
- Detected role, if known

Example roles:

- `title`
- `heading_1`
- `heading_2`
- `paragraph`
- `caption`
- `header`
- `footer`
- `table_cell`

## 3. Table Extraction

Tables should be detected and represented as structured data.

The output should preserve:

- Row order
- Column order
- Cell text
- Header rows
- Merged cells, where feasible

Tables should be regenerated as Word tables whenever possible.

## 4. Image Export

All meaningful images must be exported as independent image files.

Images containing Chinese labels must be copied into:

```text
images_to_translate/
```

The program must also generate:

```text
image_mapping.json
```

The image mapping records:

- Image ID
- Source page number
- Source file path
- Image purpose
- Insert-back location in Word
- Original width and height
- Expected translated image filename

## 5. Body Text Translation

Only editable text is translated in this stage.

The translation module must:

- Translate Chinese body text into English.
- Preserve numbering.
- Preserve units.
- Preserve model names.
- Preserve terminal numbers.
- Preserve wire labels.
- Preserve protocol names.
- Use the project terminology table.

The translation module must not:

- Translate image pixels.
- OCR image annotations.
- Cover or redraw image labels.

## 6. Editable DOCX Generation

The DOCX generator creates:

- Word paragraphs for body text.
- Word Heading styles for headings.
- Word tables for tables.
- Independent Word image objects for images.
- Headers and footers where feasible.

The first-stage DOCX uses original exported images, even if they still contain Chinese labels.

Image translation is handled later.

## 7. ChatGPT Image Translation

Images in `images_to_translate/` are sent to ChatGPT or another image workflow separately.

That external workflow is responsible for:

- Translating Chinese labels inside images.
- Preserving original image resolution.
- Preserving original annotation style.
- Preserving arrows, bubbles, borders, and layout.
- Returning replacement English images.

Expected replacement folder:

```text
images_translated/
```

## 8. Image Backfill

The image backfill module reads:

- `translated_editable.docx`
- `image_mapping.json`
- `images_translated/`

It replaces each original image with the translated version when available.

Requirements:

- Preserve image size.
- Preserve image position.
- Preserve aspect ratio.
- Do not disturb nearby text.
- Report missing translated images.

## 9. QA Checks

Before final export, the project must run automated quality checks.

Checks include:

- Editable text character count.
- Paragraph count.
- Heading count.
- Table count.
- Image count.
- Full-page image detection.
- Chinese text residual detection.
- Image mapping completeness.

If QA fails, the final export must be blocked.

## 10. Final Export

Final outputs may include:

- `translated_editable.docx`
- `translated_editable_with_images.docx`
- `translation_report.md`
- `image_mapping.json`
- `images_to_translate/`

PDF export may be added later, but DOCX is the primary deliverable.


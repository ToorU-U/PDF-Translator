# Project Pipeline

This document describes the end-to-end processing pipeline and the data passed between its stages.

## Pipeline Overview

```text
PDF or DOCX source
  -> source ingestion
  -> content extraction
  -> document model
  -> body-text translation
  -> editable DOCX generation
  -> image export and mapping
  -> external image translation
  -> image backfill
  -> quality validation
  -> final export
```

## Stage 1: Source Ingestion

The pipeline accepts a PDF or DOCX source and records source-level metadata. The source remains the layout and content reference for later reconstruction and validation.

- **Input:** source file
- **Output:** normalized source metadata and page or section access

## Stage 2: Content Extraction

The parser extracts text blocks, headings, lists, captions, headers, footers, tables, and images. Extracted elements retain source positions, page references, and detected semantic roles when available.

- **Input:** normalized source
- **Output:** extracted content and layout metadata

## Stage 3: Document Model Assembly

Extracted elements are normalized into an ordered, structured document model. Table cells, hierarchy, numbering, image references, and layout relationships are represented independently of the final output format.

- **Input:** extracted content
- **Output:** structured document model

## Stage 4: Body-text Translation

Editable Chinese text is translated into English while technical identifiers, numbering, units, model names, terminal numbers, wire labels, and protocol names are preserved. Terminology from `docs/TERMINOLOGY.md` is applied here.

- **Input:** structured document model
- **Output:** translated document model

## Stage 5: Editable DOCX Generation

The generator creates native Word paragraphs, heading styles, lists, tables, headers, footers, and independent image objects from the translated model. Original images are used until translated replacements are available.

- **Input:** translated document model and source images
- **Output:** `translated_editable.docx`

## Stage 6: Image Export and Mapping

Images requiring translated labels are exported to `images_to_translate/`. Each exported asset receives an entry in `image_mapping.json` containing its identifier, source reference, insertion target, dimensions, and expected replacement filename.

- **Input:** document model and extracted images
- **Output:** `images_to_translate/` and `image_mapping.json`

## Stage 7: External Image Translation

An external image workflow translates labels while preserving the visual layout and returns replacement assets to `images_translated/`. This stage runs outside the core application.

- **Input:** `images_to_translate/`
- **Output:** `images_translated/`

## Stage 8: Image Backfill

The backfill stage matches returned assets through `image_mapping.json` and replaces the corresponding Word image objects while retaining their recorded size, position, and aspect ratio. Missing replacements are reported.

- **Input:** `translated_editable.docx`, `image_mapping.json`, and `images_translated/`
- **Output:** `translated_editable_with_images.docx` and backfill results

## Stage 9: Quality Validation

Automated checks evaluate editable text, structure, tables, images, residual Chinese text, and mapping completeness according to `docs/QA_CHECKLIST.md`. Failed checks block final export and produce diagnostic results.

- **Input:** generated document, mappings, and processing metrics
- **Output:** validation status and `translation_report.md`

## Stage 10: Final Export

After validation passes, the pipeline packages the completed editable document, report, mappings, and relevant image assets as the final result.

- **Input:** validated outputs
- **Output:** final delivery package

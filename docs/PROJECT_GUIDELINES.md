# Project Guidelines

## Project Objective

PDF / Word Technical Translator is a general-purpose tool for converting Chinese technical documents into professional, editable English DOCX files.

The final document must behave like a real Word document, not like a collection of page screenshots.

## Target Users

The project is intended for workflows involving:

- Technical manuals
- Installation guides
- Electrical system documents
- Engineering work instructions
- Product service documents
- Maintenance procedures
- Wiring and control documentation

## Required Outputs

The standard first-stage output must include:

- `translated_editable.docx`
- `translation_report.md`
- `images_to_translate/`
- `image_mapping.json`

The optional second-stage output, after translated images are returned, may include:

- `translated_editable_with_images.docx`
- `updated_translation_report.md`

## Core Principles

1. The Word document must be editable.
2. Body text must be generated as Word paragraphs.
3. Headings must use Word Heading styles.
4. Tables must be generated as Word tables where feasible.
5. Images must be independent Word image objects.
6. Image translation must be handled outside the core program.
7. The program must export images and record their insertion positions.
8. The program must support replacing images later without changing layout.
9. Quality checks must run before final export.

## Forbidden Practices

The following are not allowed:

- Converting every PDF page into a bitmap image and inserting it into Word.
- Using full-page screenshots as the primary DOCX content.
- Flattening body text into images.
- Flattening tables into images when a Word table is feasible.
- Directly editing, OCR-covering, redrawing, or translating image annotations inside the core pipeline.
- Moving images, tables, or text without recording the layout change.
- Exporting a DOCX with near-zero editable text.
- Treating a single customer document as the permanent project structure.

## DOCX Output Standard

The generated DOCX must support:

- Selecting body text.
- Copying body text.
- Searching body text.
- Editing wording.
- Changing fonts and styles.
- Editing Word tables.
- Moving or replacing images as independent objects.

The generated DOCX should preserve:

- Heading hierarchy.
- Numbering.
- Units.
- Terminal numbers.
- Figure order.
- Table order.
- Approximate original layout.
- Page headers and footers where feasible.

## Image Policy

Images are not translated by the core pipeline.

For images that contain Chinese labels or annotations, the program must:

- Export the image at the highest available resolution.
- Put it into `images_to_translate/`.
- Create a mapping entry in `image_mapping.json`.
- Insert the original image into the first-stage DOCX.
- Wait for a translated replacement image.

The image replacement module may later replace the original image with an English version while preserving size and position.


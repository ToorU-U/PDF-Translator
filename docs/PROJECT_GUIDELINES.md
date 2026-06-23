# Project Guidelines

## Project Goal

Build a reusable technical-document translation system that converts Chinese PDF and Word sources into professional, editable English Word documents while preserving their meaning, structure, and practical usability.

The project serves technical manuals, engineering documents, installation guides, service instructions, and similar structured documents. It is a general-purpose product rather than a workspace tailored to one customer file.

## Design Philosophy

- **Editability first:** The result should behave like a native Word document, not a collection of page images.
- **Preserve intent and structure:** Translation must retain hierarchy, numbering, units, identifiers, tables, figures, and document order wherever feasible.
- **Separate concerns:** Parsing, translation, document reconstruction, image handling, and quality assurance remain independent responsibilities.
- **Traceable transformation:** Extracted content and layout decisions should retain enough source context to support validation and later correction.
- **Quality is a gate:** Outputs that do not satisfy editability, completeness, or translation checks are not final deliverables.
- **Generic by default:** New capabilities should generalize across document types instead of encoding assumptions from a single sample.

## Architecture Principles

- Represent document content as structured data before generating output formats.
- Preserve semantic roles such as headings, paragraphs, lists, captions, table cells, headers, and footers.
- Reconstruct text and tables as native editable Word elements whenever feasible.
- Keep images as independent assets with stable identifiers and recorded placement metadata.
- Isolate external image translation from the core text-processing pipeline and support deterministic replacement afterward.
- Define typed, testable boundaries between pipeline stages.
- Make validation an explicit pipeline stage that can block final export.
- Prefer observable processing with reports, counts, mappings, and actionable failure information.

## Long-term Objectives

- Support varied technical PDF and DOCX sources without document-specific code paths.
- Improve layout fidelity while preserving editability and maintainability.
- Expand extraction and reconstruction support for complex tables, headers, footers, captions, and numbering.
- Maintain consistent technical terminology across documents and domains.
- Enable reliable resumable processing and replacement of externally translated visual assets.
- Add broader automated validation, regression fixtures, and measurable quality benchmarks.
- Support additional export formats only when they do not compromise the primary editable-document workflow.

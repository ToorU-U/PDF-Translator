"""Editable DOCX generation interface."""

from __future__ import annotations

from pdf_translator.models import Document, DocxArtifact


class DocxBuilder:
    """Build editable paragraphs, headings, tables, and independent images."""

    def build(self, document: Document) -> DocxArtifact:
        """Generate an editable DOCX while preserving document structure."""

        raise NotImplementedError("DOCX generation is not implemented.")

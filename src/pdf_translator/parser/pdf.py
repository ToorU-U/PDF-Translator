"""PDF document parser implementation."""

from __future__ import annotations

from pdf_translator.models import Document, SourceDocument
from pdf_translator.parser.base import DocumentParser


class PdfDocumentParser(DocumentParser):
    """Create the minimal document model for a PDF source."""

    def parse(self, source: SourceDocument) -> Document:
        """Return an empty document until PDF extraction is implemented."""

        return Document(source=source)

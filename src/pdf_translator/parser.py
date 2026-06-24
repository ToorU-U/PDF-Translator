"""Document parsing and layout-analysis interfaces."""

from __future__ import annotations

from pdf_translator.models import Document, SourceDocument


class DocumentParser:
    """Extract editable content and recover logical document layout."""

    def parse(self, source: SourceDocument) -> Document:
        """Extract text, tables, images, and metadata from the source."""

        raise NotImplementedError("Document parsing is not implemented.")

    def analyze_layout(self, parsed: Document) -> Document:
        """Classify extracted content and reconstruct page relationships."""

        raise NotImplementedError("Layout analysis is not implemented.")

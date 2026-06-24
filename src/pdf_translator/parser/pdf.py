"""PDF document parser implementation."""

from __future__ import annotations

import fitz

from pdf_translator.models import Document, Page, Paragraph, SourceDocument, TextRun
from pdf_translator.parser.base import DocumentParser


class PdfDocumentParser(DocumentParser):
    """Extract plain text from a PDF into the shared document model."""

    def parse(self, source: SourceDocument) -> Document:
        """Create one plain-text paragraph for each non-empty PDF page."""

        with fitz.open(source.path) as pdf:
            pages = []
            for page in pdf:
                text = page.get_text()
                content = (Paragraph(runs=(TextRun(text=text),)),) if text else ()
                pages.append(Page(index=page.number, content=content))

        return Document(source=source, pages=tuple(pages))

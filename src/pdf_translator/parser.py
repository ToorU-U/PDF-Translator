"""Document parser interfaces, implementations, and selection."""

from __future__ import annotations

from pdf_translator.exceptions import UnsupportedDocumentError
from pdf_translator.models import Document, SourceDocument


class DocumentParser:
    """Extract editable content and recover logical document layout."""

    def parse(self, source: SourceDocument) -> Document:
        """Extract text, tables, images, and metadata from the source."""

        raise NotImplementedError("Document parsing is not implemented.")

    def analyze_layout(self, parsed: Document) -> Document:
        """Classify extracted content and reconstruct page relationships."""

        raise NotImplementedError("Layout analysis is not implemented.")


class PdfDocumentParser(DocumentParser):
    """Create the minimal document model for a PDF source."""

    def parse(self, source: SourceDocument) -> Document:
        """Return an empty document until PDF extraction is implemented."""

        return Document(source=source)


class DocxDocumentParser(DocumentParser):
    """Create the minimal document model for a DOCX source."""

    def parse(self, source: SourceDocument) -> Document:
        """Return an empty document until DOCX extraction is implemented."""

        return Document(source=source)


PARSERS_BY_SUFFIX: dict[str, type[DocumentParser]] = {
    ".pdf": PdfDocumentParser,
    ".docx": DocxDocumentParser,
}


def select_parser(source: SourceDocument) -> DocumentParser:
    """Return the parser registered for the source path's file suffix."""

    suffix = source.path.suffix.lower()
    parser_type = PARSERS_BY_SUFFIX.get(suffix)
    if parser_type is None:
        displayed_suffix = suffix or "<none>"
        raise UnsupportedDocumentError(
            f"Unsupported document extension: {displayed_suffix}. "
            "Supported extensions are .pdf and .docx."
        )
    return parser_type()

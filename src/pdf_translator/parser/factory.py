"""Select a document parser from source file type."""

from __future__ import annotations

from pdf_translator.exceptions import UnsupportedDocumentError
from pdf_translator.models import SourceDocument
from pdf_translator.parser.base import DocumentParser
from pdf_translator.parser.docx import DocxDocumentParser
from pdf_translator.parser.pdf import PdfDocumentParser


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

"""Public document parser interfaces, implementations, and selection."""

from pdf_translator.parser.base import DocumentParser
from pdf_translator.parser.docx import DocxDocumentParser
from pdf_translator.parser.factory import select_parser
from pdf_translator.parser.pdf import PdfDocumentParser

__all__ = [
    "DocumentParser",
    "DocxDocumentParser",
    "PdfDocumentParser",
    "select_parser",
]

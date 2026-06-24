"""Contract tests for parser placeholders."""

from __future__ import annotations

import unittest
from pathlib import Path

from pdf_translator.exceptions import UnsupportedDocumentError
from pdf_translator.models import Document, SourceDocument
from pdf_translator.parser import (
    DocumentParser,
    DocxDocumentParser,
    PdfDocumentParser,
    select_parser,
)


class ParserTests(unittest.TestCase):
    def test_parse_is_explicitly_unimplemented(self) -> None:
        source = SourceDocument(path=Path("input.pdf"))

        with self.assertRaises(NotImplementedError):
            DocumentParser().parse(source)

    def test_layout_analysis_is_explicitly_unimplemented(self) -> None:
        parsed = Document(source=SourceDocument(path=Path("input.pdf")))

        with self.assertRaises(NotImplementedError):
            DocumentParser().analyze_layout(parsed)

    def test_pdf_source_routes_to_pdf_parser(self) -> None:
        parser = select_parser(SourceDocument(path=Path("input.pdf")))

        self.assertIsInstance(parser, PdfDocumentParser)

    def test_docx_source_routes_to_docx_parser(self) -> None:
        parser = select_parser(SourceDocument(path=Path("input.docx")))

        self.assertIsInstance(parser, DocxDocumentParser)

    def test_parser_selection_is_case_insensitive(self) -> None:
        parser = select_parser(SourceDocument(path=Path("input.PDF")))

        self.assertIsInstance(parser, PdfDocumentParser)

    def test_unsupported_source_extension_fails_clearly(self) -> None:
        source = SourceDocument(path=Path("input.txt"))

        with self.assertRaisesRegex(
            UnsupportedDocumentError,
            r"Unsupported document extension: \.txt",
        ):
            select_parser(source)

    def test_concrete_parser_outputs_are_documents(self) -> None:
        for path in (Path("input.pdf"), Path("input.docx")):
            with self.subTest(path=path):
                source = SourceDocument(path=path)

                parsed = select_parser(source).parse(source)

                self.assertIsInstance(parsed, Document)
                self.assertIs(parsed.source, source)


if __name__ == "__main__":
    unittest.main()

"""Contract tests for parser placeholders."""

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path

from pdf_translator.exceptions import UnsupportedDocumentError
from pdf_translator.models import Document, Paragraph, SourceDocument, TextRun
from pdf_translator.parser import (
    DocumentParser,
    DocxDocumentParser,
    PdfDocumentParser,
    select_parser,
)

PDF_FIXTURE = Path(__file__).parent / "fixtures" / "plain_text.pdf"


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

    def test_docx_parser_output_is_a_document(self) -> None:
        source = SourceDocument(path=Path("input.docx"))

        parsed = select_parser(source).parse(source)

        self.assertIsInstance(parsed, Document)
        self.assertIs(parsed.source, source)

    def test_pdf_parser_preserves_pages_and_extracts_text(self) -> None:
        source = SourceDocument(path=PDF_FIXTURE)

        parsed = PdfDocumentParser().parse(source)

        self.assertIsInstance(parsed, Document)
        self.assertEqual(len(parsed.pages), 2)
        self.assertEqual(parsed.pages[0].index, 0)
        self.assertEqual(parsed.pages[1].index, 1)
        self.assertEqual(len(parsed.pages[0].content), 1)
        self.assertEqual(len(parsed.pages[1].content), 1)
        self.assertIsInstance(parsed.pages[0].content[0], Paragraph)
        self.assertIsInstance(parsed.pages[0].content[0].runs[0], TextRun)
        self.assertEqual(
            parsed.pages[0].content[0].runs[0].text,
            "First page text.\nSecond line.\n",
        )
        self.assertEqual(
            parsed.pages[1].content[0].runs[0].text,
            "Second page text.\n",
        )

    def test_pdf_parser_returns_immutable_document(self) -> None:
        parsed = PdfDocumentParser().parse(SourceDocument(path=PDF_FIXTURE))

        with self.assertRaises(FrozenInstanceError):
            parsed.pages = ()


if __name__ == "__main__":
    unittest.main()

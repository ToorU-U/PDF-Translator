"""Contract tests for parser placeholders."""

from __future__ import annotations

import unittest
from pathlib import Path

from pdf_translator.models import ParsedDocument, SourceDocument
from pdf_translator.parser import DocumentParser


class ParserTests(unittest.TestCase):
    def test_parse_is_explicitly_unimplemented(self) -> None:
        source = SourceDocument(path=Path("input.pdf"))

        with self.assertRaises(NotImplementedError):
            DocumentParser().parse(source)

    def test_layout_analysis_is_explicitly_unimplemented(self) -> None:
        parsed = ParsedDocument(source=SourceDocument(path=Path("input.pdf")))

        with self.assertRaises(NotImplementedError):
            DocumentParser().analyze_layout(parsed)


if __name__ == "__main__":
    unittest.main()

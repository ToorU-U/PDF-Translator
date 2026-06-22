"""Contract tests for validator placeholders."""

from __future__ import annotations

import unittest
from pathlib import Path

from pdf_translator.models import DocxArtifact
from pdf_translator.validator import DocumentValidator


class ValidatorTests(unittest.TestCase):
    def test_validate_is_explicitly_unimplemented(self) -> None:
        document = DocxArtifact(path=Path("translated_editable.docx"))

        with self.assertRaises(NotImplementedError):
            DocumentValidator().validate(document)


if __name__ == "__main__":
    unittest.main()

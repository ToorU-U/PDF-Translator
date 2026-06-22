"""Editable-text translation interface."""

from __future__ import annotations

from pdf_translator.models import LayoutDocument, TranslatedDocument


class DocumentTranslator:
    """Translate editable Chinese text while preserving technical identifiers."""

    def translate(self, document: LayoutDocument) -> TranslatedDocument:
        """Translate structured text without modifying image content."""

        raise NotImplementedError("Text translation is not implemented.")

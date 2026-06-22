"""Final document QA interface."""

from __future__ import annotations

from pdf_translator.models import DocxArtifact, ValidationReport


class DocumentValidator:
    """Apply blocking quality gates before a document is accepted."""

    def validate(self, document: DocxArtifact) -> ValidationReport:
        """Check editability, structure, image behavior, and residual text."""

        raise NotImplementedError("Document validation is not implemented.")

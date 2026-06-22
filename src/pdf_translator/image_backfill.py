"""Translated-image replacement interface."""

from __future__ import annotations

from pdf_translator.models import DocxArtifact, ImageExportManifest


class ImageBackfill:
    """Replace mapped images while preserving size, position, and layout."""

    def backfill(
        self,
        document: DocxArtifact,
        manifest: ImageExportManifest,
    ) -> DocxArtifact:
        """Insert externally translated images into their recorded locations."""

        raise NotImplementedError("Image backfill is not implemented.")

"""Image export and mapping interface."""

from __future__ import annotations

from pdf_translator.models import ImageExportManifest, LayoutDocument


class ImageExporter:
    """Export original images and record their future replacement locations."""

    def export(self, document: LayoutDocument) -> ImageExportManifest:
        """Export images without OCR, translation, redrawing, or pixel edits."""

        raise NotImplementedError("Image export is not implemented.")

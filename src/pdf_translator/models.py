"""Typed data contracts shared between pipeline stages."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class PipelineStage(str, Enum):
    """Identify the ordered stages in the end-to-end pipeline."""

    INPUT = "Input"
    PARSER = "Parser"
    LAYOUT_ANALYSIS = "Layout Analysis"
    TRANSLATION = "Translation"
    DOCX_BUILDER = "DOCX Builder"
    IMAGE_EXPORT = "Image Export"
    IMAGE_BACKFILL = "Image Backfill"
    VALIDATOR = "Validator"


@dataclass(frozen=True, slots=True)
class SourceDocument:
    """Reference an input document accepted by the pipeline."""

    path: Path


@dataclass(frozen=True, slots=True)
class ParsedDocument:
    """Represent structured content extracted from a source document."""

    source: SourceDocument


@dataclass(frozen=True, slots=True)
class LayoutDocument:
    """Represent parsed content enriched with page and layout structure."""

    parsed: ParsedDocument


@dataclass(frozen=True, slots=True)
class TranslatedDocument:
    """Represent translated editable content before DOCX generation."""

    layout: LayoutDocument


@dataclass(frozen=True, slots=True)
class DocxArtifact:
    """Reference a generated editable DOCX artifact."""

    path: Path


@dataclass(frozen=True, slots=True)
class ImageExportManifest:
    """Reference exported images and their insertion mapping."""

    image_directory: Path
    mapping_path: Path


@dataclass(frozen=True, slots=True)
class ValidationReport:
    """Represent the final QA decision and associated messages."""

    passed: bool
    messages: tuple[str, ...] = ()

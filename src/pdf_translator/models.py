"""Immutable data contracts shared between document-processing stages."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import TypeAlias


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
class BoundingBox:
    """Describe an element's rectangular position in source-page coordinates."""

    x: float
    y: float
    width: float
    height: float
    unit: str = "pt"


@dataclass(frozen=True, slots=True)
class Metadata:
    """Store document-level descriptive and source metadata."""

    title: str | None = None
    author: str | None = None
    subject: str | None = None
    keywords: tuple[str, ...] = ()
    language: str | None = None


@dataclass(frozen=True, slots=True)
class TextRun:
    """Represent contiguous text sharing the same character formatting."""

    text: str
    bounding_box: BoundingBox | None = None
    language: str | None = None
    font_name: str | None = None
    font_size: float | None = None
    bold: bool = False
    italic: bool = False
    underline: bool = False


@dataclass(frozen=True, slots=True)
class Paragraph:
    """Represent an editable paragraph composed of ordered text runs."""

    runs: tuple[TextRun, ...] = ()
    bounding_box: BoundingBox | None = None
    list_label: str | None = None


@dataclass(frozen=True, slots=True)
class Heading:
    """Represent a titled section with an explicit hierarchy level."""

    level: int
    runs: tuple[TextRun, ...] = ()
    bounding_box: BoundingBox | None = None
    numbering: str | None = None


@dataclass(frozen=True, slots=True)
class Image:
    """Represent an independent image asset and its source-page placement."""

    image_id: str
    bounding_box: BoundingBox | None = None
    asset_path: Path | None = None
    mime_type: str | None = None
    alt_text: str | None = None
    caption: Paragraph | None = None


TableCellContent: TypeAlias = Paragraph | Heading | Image


@dataclass(frozen=True, slots=True)
class TableCell:
    """Represent a table cell, including spans and editable cell content."""

    content: tuple[TableCellContent, ...] = ()
    bounding_box: BoundingBox | None = None
    row_span: int = 1
    column_span: int = 1


@dataclass(frozen=True, slots=True)
class Table:
    """Represent a native table as ordered rows of structured cells."""

    rows: tuple[tuple[TableCell, ...], ...] = ()
    bounding_box: BoundingBox | None = None
    caption: Paragraph | None = None
    header_row_count: int = 0


RegionContent: TypeAlias = Paragraph | Heading | Table | Image


@dataclass(frozen=True, slots=True)
class Header:
    """Represent repeatable content located in a page's header region."""

    content: tuple[RegionContent, ...] = ()
    bounding_box: BoundingBox | None = None


@dataclass(frozen=True, slots=True)
class Footer:
    """Represent repeatable content located in a page's footer region."""

    content: tuple[RegionContent, ...] = ()
    bounding_box: BoundingBox | None = None


@dataclass(frozen=True, slots=True)
class PageNumber:
    """Represent a displayed page label and its optional numeric value."""

    runs: tuple[TextRun, ...] = ()
    value: int | None = None
    bounding_box: BoundingBox | None = None


PageContent: TypeAlias = Paragraph | Heading | Table | Image


@dataclass(frozen=True, slots=True)
class Page:
    """Represent a source page whose content tuple defines reading order."""

    index: int
    content: tuple[PageContent, ...] = ()
    headers: tuple[Header, ...] = ()
    footers: tuple[Footer, ...] = ()
    page_number: PageNumber | None = None
    media_box: BoundingBox | None = None
    rotation: int = 0


@dataclass(frozen=True, slots=True)
class Document:
    """Represent a complete technical document shared by pipeline stages."""

    source: SourceDocument
    pages: tuple[Page, ...] = ()
    metadata: Metadata = Metadata()


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

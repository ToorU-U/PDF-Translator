"""Contract tests for the shared immutable document model."""

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError, is_dataclass
from pathlib import Path

from pdf_translator.models import (
    BoundingBox,
    DocxArtifact,
    Document,
    Footer,
    Header,
    Heading,
    Image,
    ImageExportManifest,
    Metadata,
    Page,
    PageNumber,
    Paragraph,
    SourceDocument,
    Table,
    TableCell,
    TextRun,
    ValidationReport,
)


class DocumentModelTests(unittest.TestCase):
    def test_model_represents_structured_technical_document(self) -> None:
        box = BoundingBox(x=10, y=20, width=200, height=30)
        title = Heading(
            level=1,
            runs=(TextRun(text="Installation", bold=True),),
            bounding_box=box,
            numbering="1",
        )
        cell = TableCell(
            content=(Paragraph(runs=(TextRun(text="B436"),)),),
        )
        table = Table(rows=((cell,),), header_row_count=1)
        image = Image(
            image_id="figure-1",
            bounding_box=box,
            asset_path=Path("images/figure-1.png"),
        )
        page_number = PageNumber(runs=(TextRun(text="1"),), value=1)
        document = Document(
            source=SourceDocument(path=Path("manual.pdf")),
            pages=(
                Page(
                    index=0,
                    content=(title, table, image),
                    footers=(Footer(),),
                    page_number=page_number,
                    media_box=BoundingBox(0, 0, 595, 842),
                ),
            ),
            metadata=Metadata(title="Technical Manual", language="en"),
        )

        self.assertEqual(document.pages[0].content, (title, table, image))
        self.assertEqual(document.pages[0].page_number, page_number)
        self.assertEqual(document.metadata.title, "Technical Manual")

    def test_all_model_dataclasses_are_frozen(self) -> None:
        model_types = (
            SourceDocument,
            BoundingBox,
            Metadata,
            TextRun,
            Paragraph,
            Heading,
            Image,
            TableCell,
            Table,
            Header,
            Footer,
            PageNumber,
            Page,
            Document,
            DocxArtifact,
            ImageExportManifest,
            ValidationReport,
        )

        for model_type in model_types:
            with self.subTest(model_type=model_type.__name__):
                self.assertTrue(is_dataclass(model_type))
                self.assertTrue(model_type.__dataclass_params__.frozen)

    def test_nested_model_components_are_immutable(self) -> None:
        run = TextRun(text="Installation")
        paragraph = Paragraph(runs=(run,))
        page = Page(index=0, content=(paragraph,))
        document = Document(
            source=SourceDocument(path=Path("manual.pdf")),
            pages=(page,),
        )

        with self.assertRaises(FrozenInstanceError):
            document.pages = ()  # type: ignore[misc]

        with self.assertRaises(FrozenInstanceError):
            page.content = ()  # type: ignore[misc]

        with self.assertRaises(FrozenInstanceError):
            paragraph.runs = ()  # type: ignore[misc]

        with self.assertRaises(FrozenInstanceError):
            run.text = "Changed"  # type: ignore[misc]


if __name__ == "__main__":
    unittest.main()

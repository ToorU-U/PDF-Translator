"""Contract tests for the shared immutable document model."""

from __future__ import annotations

import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path

from pdf_translator.models import (
    BoundingBox,
    Document,
    Footer,
    Heading,
    Image,
    Metadata,
    Page,
    PageNumber,
    Paragraph,
    ReadingOrder,
    SourceDocument,
    Table,
    TableCell,
    TextRun,
)


class DocumentModelTests(unittest.TestCase):
    def test_model_represents_structured_technical_document(self) -> None:
        box = BoundingBox(x=10, y=20, width=200, height=30)
        title = Heading(
            level=1,
            runs=(TextRun(text="Installation", bold=True),),
            bounding_box=box,
            reading_order=ReadingOrder(index=0),
            numbering="1",
        )
        cell = TableCell(
            content=(Paragraph(runs=(TextRun(text="B436"),)),),
            is_header=True,
        )
        table = Table(rows=((cell,),), reading_order=ReadingOrder(index=1))
        image = Image(
            image_id="figure-1",
            bounding_box=box,
            reading_order=ReadingOrder(index=2),
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

    def test_model_is_immutable(self) -> None:
        document = Document(source=SourceDocument(path=Path("manual.pdf")))

        with self.assertRaises(FrozenInstanceError):
            document.pages = ()  # type: ignore[misc]


if __name__ == "__main__":
    unittest.main()

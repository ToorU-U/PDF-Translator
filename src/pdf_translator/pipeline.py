"""Top-level orchestration for the technical document workflow."""

from __future__ import annotations

from pathlib import Path

from pdf_translator.config import AppConfig
from pdf_translator.docx_builder import DocxBuilder
from pdf_translator.image_backfill import ImageBackfill
from pdf_translator.image_exporter import ImageExporter
from pdf_translator.models import PipelineStage, SourceDocument, ValidationReport
from pdf_translator.parser import DocumentParser, select_parser
from pdf_translator.translator import DocumentTranslator
from pdf_translator.validator import DocumentValidator


PIPELINE_STAGES: tuple[PipelineStage, ...] = (
    PipelineStage.INPUT,
    PipelineStage.PARSER,
    PipelineStage.LAYOUT_ANALYSIS,
    PipelineStage.IMAGE_EXPORT,
    PipelineStage.TRANSLATION,
    PipelineStage.DOCX_BUILDER,
    PipelineStage.IMAGE_BACKFILL,
    PipelineStage.VALIDATOR,
)


class Pipeline:
    """Coordinate every stage without implementing stage-specific behavior."""

    def __init__(
        self,
        config: AppConfig | None = None,
        parser: DocumentParser | None = None,
        translator: DocumentTranslator | None = None,
        docx_builder: DocxBuilder | None = None,
        image_exporter: ImageExporter | None = None,
        image_backfill: ImageBackfill | None = None,
        validator: DocumentValidator | None = None,
    ) -> None:
        self.config = config or AppConfig()
        self.parser = parser
        self.translator = translator or DocumentTranslator()
        self.docx_builder = docx_builder or DocxBuilder()
        self.image_exporter = image_exporter or ImageExporter()
        self.image_backfill = image_backfill or ImageBackfill()
        self.validator = validator or DocumentValidator()

    @property
    def stages(self) -> tuple[PipelineStage, ...]:
        """Return the immutable execution order for inspection and reporting."""

        return PIPELINE_STAGES

    def run(self, input_path: Path) -> ValidationReport:
        """Execute the declared stage order once implementations are available."""

        source = SourceDocument(path=input_path)
        parser = self.parser or select_parser(source)
        parsed = parser.parse(source)
        layout = parser.analyze_layout(parsed)
        image_manifest = self.image_exporter.export(layout)
        translated = self.translator.translate(layout)
        docx = self.docx_builder.build(translated)
        completed_docx = self.image_backfill.backfill(docx, image_manifest)
        return self.validator.validate(completed_docx)

"""Smoke tests for pipeline initialization and stage declaration."""

from __future__ import annotations

import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from pdf_translator.cli import main
from pdf_translator.models import PipelineStage
from pdf_translator.pipeline import Pipeline


class PipelineTests(unittest.TestCase):
    def test_pipeline_declares_complete_stage_order(self) -> None:
        pipeline = Pipeline()

        self.assertEqual(
            pipeline.stages,
            (
                PipelineStage.INPUT,
                PipelineStage.PARSER,
                PipelineStage.LAYOUT_ANALYSIS,
                PipelineStage.TRANSLATION,
                PipelineStage.DOCX_BUILDER,
                PipelineStage.IMAGE_EXPORT,
                PipelineStage.IMAGE_BACKFILL,
                PipelineStage.VALIDATOR,
            ),
        )

    def test_unimplemented_pipeline_stops_at_parser(self) -> None:
        with self.assertRaisesRegex(NotImplementedError, "parsing"):
            Pipeline().run(Path("input.pdf"))

    def test_cli_initializes_without_running_pipeline(self) -> None:
        output = io.StringIO()

        with redirect_stdout(output):
            exit_code = main(["input.pdf"])

        self.assertEqual(exit_code, 0)
        self.assertEqual(output.getvalue().strip(), "Pipeline initialized.")


if __name__ == "__main__":
    unittest.main()

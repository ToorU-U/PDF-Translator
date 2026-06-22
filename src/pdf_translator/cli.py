"""Command-line interface for the translation pipeline."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from pdf_translator.config import AppConfig, configure_logging
from pdf_translator.pipeline import Pipeline


def build_argument_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""

    parser = argparse.ArgumentParser(
        prog="pdf-translator",
        description="Convert a technical PDF or DOCX into an editable English DOCX.",
    )
    parser.add_argument("input", type=Path, help="Source PDF or DOCX file.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Initialize the pipeline without running business logic."""

    arguments = build_argument_parser().parse_args(argv)
    config = AppConfig()
    configure_logging(config.logging)
    Pipeline(config=config)
    _ = arguments.input
    print("Pipeline initialized.")
    return 0

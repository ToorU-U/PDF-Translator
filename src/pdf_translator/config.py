"""Application and logging configuration."""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from logging.config import dictConfig
from pathlib import Path


@dataclass(frozen=True, slots=True)
class LoggingConfig:
    """Define the shared logging format and severity level."""

    level: int = logging.INFO
    format: str = "%(asctime)s %(levelname)s %(name)s: %(message)s"


@dataclass(frozen=True, slots=True)
class AppConfig:
    """Collect application-wide settings used by pipeline components."""

    output_directory: Path = Path("output")
    logging: LoggingConfig = field(default_factory=LoggingConfig)


def configure_logging(config: LoggingConfig | None = None) -> None:
    """Apply the single logging configuration used by the application."""

    selected = config or LoggingConfig()
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {"format": selected.format},
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard",
                    "level": selected.level,
                },
            },
            "root": {
                "handlers": ["console"],
                "level": selected.level,
            },
        }
    )

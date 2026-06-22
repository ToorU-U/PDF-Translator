"""Small shared utilities with no document-specific business logic."""

import logging


def get_logger(name: str) -> logging.Logger:
    """Return a logger that participates in the shared logging configuration."""

    return logging.getLogger(name)

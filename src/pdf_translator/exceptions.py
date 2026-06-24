"""Project-specific exception hierarchy."""


class PdfTranslatorError(Exception):
    """Base exception for expected application failures."""


class ConfigurationError(PdfTranslatorError):
    """Raised when application configuration is invalid."""


class PipelineError(PdfTranslatorError):
    """Raised when orchestration cannot complete a pipeline stage."""


class UnsupportedDocumentError(PdfTranslatorError):
    """Raised when no parser supports a source document's file type."""


class ValidationError(PdfTranslatorError):
    """Raised when an output fails a required quality gate."""

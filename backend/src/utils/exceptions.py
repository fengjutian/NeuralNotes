"""Custom exception hierarchy for the application."""

from typing import Any, Optional


class AppException(Exception):
    """Base exception for all application errors.

    Attributes:
        message: Human-readable error message.
        details: Additional error details for debugging.
    """

    def __init__(
        self,
        message: str,
        details: Optional[dict[str, Any]] = None,
    ) -> None:
        self.message = message
        self.details = details or {}
        super().__init__(self.message)

    def to_dict(self) -> dict[str, Any]:
        """Convert exception to dictionary for API response."""
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "details": self.details,
        }


# Database Exceptions
class DatabaseException(AppException):
    """Raised when database operations fail."""
    pass


class RecordNotFoundException(AppException):
    """Raised when a requested record is not found."""

    def __init__(
        self,
        resource: str,
        identifier: Any,
    ) -> None:
        message = f"{resource} with id '{identifier}' not found"
        super().__init__(message, {"resource": resource, "id": str(identifier)})


class DuplicateRecordException(AppException):
    """Raised when attempting to create a duplicate record."""

    def __init__(self, resource: str, identifier: Any) -> None:
        message = f"{resource} with id '{identifier}' already exists"
        super().__init__(message, {"resource": resource, "id": str(identifier)})


# File Processing Exceptions
class FileProcessingException(AppException):
    """Raised when file processing fails."""
    pass


class InvalidFileFormatException(FileProcessingException):
    """Raised when file format is invalid."""

    def __init__(
        self,
        file_name: str,
        expected_format: str,
        actual_format: Optional[str] = None,
    ) -> None:
        message = f"Invalid file format for '{file_name}'. Expected: {expected_format}"
        if actual_format:
            message += f", got: {actual_format}"
        super().__init__(
            message,
            {
                "file_name": file_name,
                "expected_format": expected_format,
                "actual_format": actual_format,
            },
        )


class FileTooLargeException(FileProcessingException):
    """Raised when uploaded file exceeds size limit."""

    def __init__(
        self,
        file_name: str,
        size_mb: float,
        max_size_mb: int,
    ) -> None:
        message = f"File '{file_name}' is too large: {size_mb:.1f}MB > {max_size_mb}MB"
        super().__init__(
            message,
            {
                "file_name": file_name,
                "size_mb": size_mb,
                "max_size_mb": max_size_mb,
            },
        )


# AI/LLM Exceptions
class AIException(AppException):
    """Raised when AI operations fail."""
    pass


class AIProviderException(AIException):
    """Raised when AI provider (OpenAI, etc.) returns an error."""

    def __init__(
        self,
        provider: str,
        message: str,
        status_code: Optional[int] = None,
    ) -> None:
        super().__init__(
            f"{provider} error: {message}",
            {"provider": provider, "status_code": status_code},
        )


class AIRateLimitException(AIException):
    """Raised when AI API rate limit is exceeded."""

    def __init__(self, retry_after_seconds: Optional[int] = None) -> None:
        message = "AI API rate limit exceeded"
        if retry_after_seconds:
            message += f". Retry after {retry_after_seconds} seconds"
        super().__init__(
            message,
            {"retry_after_seconds": retry_after_seconds},
        )


# Graph Database Exceptions
class GraphException(AppException):
    """Raised when graph database operations fail."""
    pass


class GraphConnectionException(GraphException):
    """Raised when unable to connect to graph database."""

    def __init__(self, uri: str) -> None:
        message = f"Unable to connect to graph database at {uri}"
        super().__init__(message, {"uri": uri})


# Vector Search Exceptions
class VectorSearchException(AppException):
    """Raised when vector search operations fail."""
    pass


# Validation Exceptions
class ValidationException(AppException):
    """Raised when input validation fails."""

    def __init__(self, message: str, field: Optional[str] = None) -> None:
        super().__init__(
            message,
            {"field": field} if field else {},
        )

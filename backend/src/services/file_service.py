"""File handling service for uploaded markdown files."""

import os
import uuid
from pathlib import Path
from typing import BinaryIO

import aiofiles

from src.config import settings
from src.utils.logging import get_logger
from src.utils.exceptions import FileTooLargeException, FileProcessingException

logger = get_logger(__name__)


class FileService:
    """Service for handling file uploads and storage.

    Manages file storage, validation, and retrieval for imported markdown files.
    """

    def __init__(self) -> None:
        """Initialize the file service."""
        self.upload_dir = settings.upload_dir
        self.max_size = settings.max_file_size_bytes
        self.logger = get_logger(self.__class__.__name__)
        self._ensure_upload_dir()

    def _ensure_upload_dir(self) -> None:
        """Ensure upload directory exists."""
        self.upload_dir.mkdir(parents=True, exist_ok=True)
        self.logger.info("Upload directory: %s", self.upload_dir)

    def _generate_filename(self, original_filename: str) -> str:
        """Generate a unique filename for storage.

        Args:
            original_filename: Original uploaded filename.

        Returns:
            Unique filename for storage.
        """
        ext = Path(original_filename).suffix.lower()
        unique_id = uuid.uuid4().hex[:8]
        return f"{unique_id}_{original_filename}"

    async def save_file(
        self,
        file_content: bytes,
        original_filename: str,
    ) -> Path:
        """Save an uploaded file to disk.

        Args:
            file_content: File content as bytes.
            original_filename: Original filename.

        Returns:
            Path to the saved file.

        Raises:
            FileTooLargeException: If file exceeds size limit.
            FileProcessingException: If file cannot be saved.
        """
        # Validate file size
        file_size_mb = len(file_content) / (1024 * 1024)
        if len(file_content) > self.max_size:
            raise FileTooLargeException(
                file_name=original_filename,
                size_mb=file_size_mb,
                max_size_mb=settings.max_file_size_mb,
            )

        # Generate unique filename
        filename = self._generate_filename(original_filename)
        file_path = self.upload_dir / filename

        try:
            async with aiofiles.open(file_path, "wb") as f:
                await f.write(file_content)
            self.logger.info("Saved file: %s (%d bytes)", file_path, len(file_content))
            return file_path
        except Exception as e:
            self.logger.error("Failed to save file: %s", str(e))
            raise FileProcessingException(
                f"Failed to save file: {e}",
                {"filename": original_filename},
            ) from e

    async def read_file(self, file_path: Path) -> str:
        """Read file content as text.

        Args:
            file_path: Path to the file.

        Returns:
            File content as string.

        Raises:
            FileProcessingException: If file cannot be read.
        """
        try:
            async with aiofiles.open(file_path, "r", encoding="utf-8") as f:
                content = await f.read()
            self.logger.debug("Read file: %s (%d bytes)", file_path, len(content))
            return content
        except UnicodeDecodeError:
            # Try with different encoding
            try:
                async with aiofiles.open(file_path, "r", encoding="gbk") as f:
                    content = await f.read()
                return content
            except Exception as e:
                raise FileProcessingException(
                    f"Failed to read file (encoding error): {e}",
                    {"file_path": str(file_path)},
                ) from e
        except Exception as e:
            raise FileProcessingException(
                f"Failed to read file: {e}",
                {"file_path": str(file_path)},
            ) from e

    def delete_file(self, file_path: Path) -> bool:
        """Delete a file.

        Args:
            file_path: Path to the file.

        Returns:
            True if deleted successfully.
        """
        try:
            if file_path.exists():
                file_path.unlink()
                self.logger.info("Deleted file: %s", file_path)
                return True
            return False
        except Exception as e:
            self.logger.error("Failed to delete file %s: %s", file_path, str(e))
            return False

    def list_files(self) -> list[Path]:
        """List all uploaded files.

        Returns:
            List of file paths.
        """
        if not self.upload_dir.exists():
            return []
        return list(self.upload_dir.glob("*.md"))

    def get_file_size(self, file_path: Path) -> int:
        """Get file size in bytes.

        Args:
            file_path: Path to the file.

        Returns:
            File size in bytes.
        """
        return file_path.stat().st_size if file_path.exists() else 0


# Singleton instance
file_service = FileService()

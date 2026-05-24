"""Markdown parser for WeChat Reading export files.

Parses the specific markdown format used by WeChat Reading when exporting highlights.
"""

import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from src.utils.logging import get_logger
from src.utils.exceptions import InvalidFileFormatException

logger = get_logger(__name__)


@dataclass
class ParsedHighlight:
    """Represents a parsed highlight from the markdown file.

    Attributes:
        content: The highlighted text.
        chapter: Chapter name where highlight occurred.
        create_time: When the highlight was created.
        url: Original URL if available.
    """

    content: str
    chapter: Optional[str] = None
    create_time: Optional[datetime] = None
    url: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "content": self.content,
            "chapter": self.chapter,
            "create_time": self.create_time.isoformat() if self.create_time else None,
            "url": self.url,
        }


@dataclass
class ParsedBook:
    """Represents a parsed book with metadata and highlights.

    Attributes:
        title: Book title.
        author: Author name.
        category: Book category (if found).
        isbn: ISBN number (if found).
        reading_time: Reading time (if found).
        reading_date: Reading date (if found).
        highlights: List of parsed highlights.
    """

    title: str
    author: str
    category: Optional[str] = None
    isbn: Optional[str] = None
    reading_time: Optional[str] = None
    reading_date: Optional[str] = None
    highlights: list[ParsedHighlight] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "title": self.title,
            "author": self.author,
            "category": self.category,
            "isbn": self.isbn,
            "reading_time": self.reading_time,
            "reading_date": self.reading_date,
            "highlight_count": len(self.highlights),
            "highlights": [h.to_dict() for h in self.highlights],
        }


class MarkdownParser:
    """Parser for WeChat Reading markdown export files.

    WeChat Reading exports highlights in a specific markdown format that includes
    book metadata at the top and individual highlights separated by markers.

    Example format:
        # 书名
        作者: xxx

        ## 第X章
        - 高亮内容 1
        - 高亮内容 2
        > 创建时间: 2024-01-01

        ## 第Y章
        - 高亮内容 3
    """

    # Regex patterns for parsing
    TITLE_PATTERN = re.compile(r"^#\s+(.+)$", re.MULTILINE)
    AUTHOR_PATTERN = re.compile(r"作者[:：]\s*(.+)")
    CATEGORY_PATTERN = re.compile(r"分类[:：]\s*(.+)")
    ISBN_PATTERN = re.compile(r"ISBN[:：]\s*([\d-]+)")
    READING_TIME_PATTERN = re.compile(r"阅读时长[:：]\s*(.+)")
    READING_DATE_PATTERN = re.compile(r"阅读日期[:：]\s*(\d{4}[-/]\d{1,2}[-/]\d{1,2})")
    CHAPTER_PATTERN = re.compile(r"^#{2,3}\s+(.+)$", re.MULTILINE)
    HIGHLIGHT_MARKER = re.compile(r"^-\s+(.+)$", re.MULTILINE)
    CREATE_TIME_PATTERN = re.compile(r"创建于\s*(\d{4}[-/]\d{1,2}[-/]\d{1,2})")
    URL_PATTERN = re.compile(r"https?://[^\s]+")

    def __init__(self) -> None:
        """Initialize the parser."""
        self.logger = get_logger(self.__class__.__name__)

    def parse(self, content: str, file_name: Optional[str] = None) -> ParsedBook:
        """Parse a WeChat Reading markdown file.

        Args:
            content: Raw markdown content.
            file_name: Optional original file name for error messages.

        Returns:
            ParsedBook with all extracted data.

        Raises:
            InvalidFileFormatException: If the file format is invalid.
        """
        self.logger.info("Parsing markdown file: %s", file_name)

        if not content or not content.strip():
            raise InvalidFileFormatException(
                file_name=file_name or "unknown",
                expected_format="WeChat Reading markdown export",
            )

        # Extract book metadata
        title = self._extract_title(content, file_name)
        author = self._extract_author(content)
        category = self._extract_pattern(content, self.CATEGORY_PATTERN)
        isbn = self._extract_pattern(content, self.ISBN_PATTERN)
        reading_time = self._extract_pattern(content, self.READING_TIME_PATTERN)
        reading_date = self._extract_pattern(content, self.READING_DATE_PATTERN)

        # Extract highlights
        highlights = self._extract_highlights(content)

        self.logger.info(
            "Parsed book '%s' by %s: %d highlights",
            title,
            author,
            len(highlights),
        )

        return ParsedBook(
            title=title,
            author=author,
            category=category,
            isbn=isbn,
            reading_time=reading_time,
            reading_date=reading_date,
            highlights=highlights,
        )

    def _extract_title(self, content: str, file_name: Optional[str]) -> str:
        """Extract book title from content."""
        title_match = self.TITLE_PATTERN.search(content)
        if title_match:
            return title_match.group(1).strip()

        # Fallback to filename
        if file_name:
            # Remove .md extension and clean up
            title = file_name.replace(".md", "").strip()
            self.logger.warning("Using filename as title: %s", title)
            return title

        raise InvalidFileFormatException(
            file_name=file_name or "unknown",
            expected_format="WeChat Reading markdown (missing title)",
        )

    def _extract_author(self, content: str) -> str:
        """Extract author from content."""
        author = self._extract_pattern(content, self.AUTHOR_PATTERN)
        if author:
            return author
        self.logger.warning("Author not found in markdown")
        return "Unknown Author"

    def _extract_pattern(
        self,
        content: str,
        pattern: re.Pattern,
    ) -> Optional[str]:
        """Extract value using a regex pattern."""
        match = pattern.search(content)
        if match:
            return match.group(1).strip()
        return None

    def _extract_highlights(self, content: str) -> list[ParsedHighlight]:
        """Extract all highlights from content."""
        highlights: list[ParsedHighlight] = []
        current_chapter: Optional[str] = None

        lines = content.split("\n")

        for i, line in enumerate(lines):
            stripped = line.strip()

            # Check for chapter heading
            if self.CHAPTER_PATTERN.match(stripped):
                chapter_match = self.CHAPTER_PATTERN.match(stripped)
                if chapter_match:
                    current_chapter = chapter_match.group(1).strip()

            # Check for highlight marker
            elif self.HIGHLIGHT_MARKER.match(stripped):
                highlight_match = self.HIGHLIGHT_MARKER.match(stripped)
                if highlight_match:
                    highlight_content = highlight_match.group(1).strip()

                    # Look for metadata in following lines
                    create_time: Optional[datetime] = None
                    url: Optional[str] = None

                    # Check next few lines for metadata
                    for j in range(i + 1, min(i + 4, len(lines))):
                        next_line = lines[j].strip()

                        # Extract creation time
                        time_match = self.CREATE_TIME_PATTERN.search(next_line)
                        if time_match:
                            date_str = time_match.group(1)
                            try:
                                create_time = datetime.fromisoformat(
                                    date_str.replace("/", "-")
                                )
                            except ValueError:
                                pass

                        # Extract URL
                        url_match = self.URL_PATTERN.search(next_line)
                        if url_match:
                            url = url_match.group(0)

                        # Stop if we hit non-metadata content
                        if next_line and not next_line.startswith(">"):
                            break

                    highlights.append(
                        ParsedHighlight(
                            content=highlight_content,
                            chapter=current_chapter,
                            create_time=create_time,
                            url=url,
                        )
                    )

        return highlights

    def validate_format(self, content: str) -> bool:
        """Validate that content matches expected WeChat Reading format.

        Args:
            content: Content to validate.

        Returns:
            True if format is valid, False otherwise.
        """
        # Must have a title
        if not self.TITLE_PATTERN.search(content):
            return False

        # Should have at least some content
        if len(content.strip()) < 50:
            return False

        return True

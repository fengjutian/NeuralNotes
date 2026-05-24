"""Markdown parser for WeChat Reading export files.

Parses the specific markdown format used by WeChat Reading when exporting highlights.
Supports two formats:
  - Format A: Simple format with # Title, ## Chapter, - highlight, > metadata
  - Format B: Full format with YAML frontmatter, Obsidian-style callout metadata,
               #### chapter headings, > 📌 highlights, > ⏱ timestamps
"""

import re
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

import yaml

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
        progress: Reading progress percentage (if found).
        highlights: List of parsed highlights.
    """

    title: str
    author: str
    category: Optional[str] = None
    isbn: Optional[str] = None
    reading_time: Optional[str] = None
    reading_date: Optional[str] = None
    progress: Optional[float] = None
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
            "progress": self.progress,
            "highlight_count": len(self.highlights),
            "highlights": [h.to_dict() for h in self.highlights],
        }


class MarkdownParser:
    """Parser for WeChat Reading markdown export files.

    WeChat Reading exports highlights in a specific markdown format that includes
    book metadata at the top and individual highlights separated by markers.

    Example format A (simple):
        # 书名
        作者: xxx

        ## 第X章
        - 高亮内容 1
        - 高亮内容 2
        > 创建时间: 2024-01-01

    Example format B (full with YAML frontmatter):
        ---
        doc_type: weread-highlights-reviews
        bookId: "3300044333"
        title: Spring实战（第6版）
        author: 克雷格·沃斯
        isbn: 9787115598691
        readingTime: 3小时28分钟
        progress: 99%
        readingDate: 2023-04-18
        ---
        # 元数据
        > [!abstract] Spring实战（第6版）
        > - 书名： Spring实战（第6版）
        > - 分类： 计算机-编程设计

        # 高亮划线
        #### 8.1 OAuth 2简介
        > 📌 [高亮内容](<weread://...>)
        > ⏱ 2023-11-06 11:02:52
    """

    # Regex patterns for Format A (simple)
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

    # Regex patterns for Format B (full YAML + Obsidian callout)
    YAML_FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
    METADATA_TITLE_PATTERN = re.compile(r"书名[:：]\s*(.+)")
    METADATA_AUTHOR_PATTERN = re.compile(r"作者[:：]\s*(.+)")
    METADATA_CATEGORY_PATTERN = re.compile(r"分类[:：]\s*(.+)")
    METADATA_ISBN_PATTERN = re.compile(r"ISBN[:：]\s*([\d-]+)")
    METADATA_READING_TIME_PATTERN = re.compile(r"阅读时长[:：]\s*(.+)")
    METADATA_READING_DATE_PATTERN = re.compile(r"阅读日期[:：]\s*(\d{4}[-/]\d{1,2}[-/]\d{1,2})")
    METADATA_PROGRESS_PATTERN = re.compile(r"进度[:：]\s*([\d]+(?:\.[\d]+)?)\s*%?")
    # Format B chapter headings: #### followed by text
    CHAPTER_B_PATTERN = re.compile(r"^####\s+(.+)$", re.MULTILINE)
    # Format B highlight: > 📌 [text](url) or > 📌 text
    HIGHLIGHT_B_PATTERN = re.compile(r"^>\s*📌\s*(?:\[([^\]]*)\]\s*\(([^)]*)\)|(.+))$")
    # Format B timestamp: > ⏱ 2023-11-06 11:02:52
    TIMESTAMP_B_PATTERN = re.compile(r"^>\s*⏱\s*(\d{4}[-/]\d{1,2}[-/]\d{1,2}\s+\d{1,2}:\d{1,2}:\d{1,2})")
    # Format B URL for highlights
    URL_B_PATTERN = re.compile(r"weread://[^\s>]+")

    def __init__(self) -> None:
        """Initialize the parser."""
        self.logger = get_logger(self.__class__.__name__)

    def parse(self, content: str, file_name: Optional[str] = None) -> ParsedBook:
        """Parse a WeChat Reading markdown file.

        Detects the format automatically and delegates to the appropriate parser.

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

        # Detect format: Format B has YAML frontmatter
        if self._has_yaml_frontmatter(content):
            self.logger.info("Detected Format B (YAML + Obsidian callout)")
            return self._parse_format_b(content, file_name)
        else:
            self.logger.info("Detected Format A (simple markdown)")
            return self._parse_format_a(content, file_name)

    def _has_yaml_frontmatter(self, content: str) -> bool:
        """Check if the content has YAML frontmatter."""
        return self.YAML_FRONTMATTER_PATTERN.match(content.strip()) is not None

    # ------------------------------------------------------------------
    # Format A: simple markdown
    # ------------------------------------------------------------------

    def _parse_format_a(self, content: str, file_name: Optional[str]) -> ParsedBook:
        """Parse Format A (simple markdown)."""
        title = self._extract_title(content, file_name)
        author = self._extract_author(content)
        category = self._extract_pattern(content, self.CATEGORY_PATTERN)
        isbn = self._extract_pattern(content, self.ISBN_PATTERN)
        reading_time = self._extract_pattern(content, self.READING_TIME_PATTERN)
        reading_date = self._extract_pattern(content, self.READING_DATE_PATTERN)
        highlights = self._extract_highlights_a(content)

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

    def _extract_highlights_a(self, content: str) -> list[ParsedHighlight]:
        """Extract all highlights from content (Format A)."""
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

    # ------------------------------------------------------------------
    # Format B: YAML frontmatter + Obsidian callout
    # ------------------------------------------------------------------

    def _parse_format_b(self, content: str, file_name: Optional[str]) -> ParsedBook:
        """Parse Format B (YAML frontmatter + Obsidian callout)."""
        # 1. Parse YAML frontmatter
        yaml_data = self._parse_yaml_frontmatter(content)

        title = yaml_data.get("title") or self._extract_title_from_file(file_name)
        author = yaml_data.get("author", "Unknown Author")

        # 2. Supplement with metadata section (backup for missing fields)
        metadata = self._parse_metadata_section(content)

        category = yaml_data.get("category") or metadata.get("category")
        isbn = yaml_data.get("isbn") or metadata.get("isbn")
        reading_time = yaml_data.get("readingTime") or metadata.get("reading_time")
        reading_date = yaml_data.get("readingDate") or metadata.get("reading_date")
        progress = self._parse_progress(yaml_data.get("progress"))

        # 3. Extract highlights from the content body
        highlights = self._extract_highlights_b(content)

        self.logger.info(
            "Parsed book '%s' by %s: %d highlights (Format B)",
            title, author, len(highlights),
        )

        return ParsedBook(
            title=title,
            author=author,
            category=category,
            isbn=isbn,
            reading_time=reading_time,
            reading_date=reading_date,
            progress=progress,
            highlights=highlights,
        )

    def _parse_yaml_frontmatter(self, content: str) -> dict:
        """Extract YAML frontmatter from content."""
        match = self.YAML_FRONTMATTER_PATTERN.match(content.strip())
        if not match:
            return {}
        try:
            data = yaml.safe_load(match.group(1))
            if isinstance(data, dict):
                return data
        except yaml.YAMLError as e:
            self.logger.warning("Failed to parse YAML frontmatter: %s", e)
        return {}

    def _parse_metadata_section(self, content: str) -> dict:
        """Parse the Obsidian-style metadata callout section.

        Looks for lines like:
        > - 书名： Spring实战（第6版）
        > - 分类： 计算机-编程设计
        """
        result: dict = {}
        patterns = {
            "title": self.METADATA_TITLE_PATTERN,
            "author": self.METADATA_AUTHOR_PATTERN,
            "category": self.METADATA_CATEGORY_PATTERN,
            "isbn": self.METADATA_ISBN_PATTERN,
            "reading_time": self.METADATA_READING_TIME_PATTERN,
            "reading_date": self.METADATA_READING_DATE_PATTERN,
        }
        for key, pattern in patterns.items():
            value = self._extract_pattern(content, pattern)
            if value:
                result[key] = value
        return result

    def _parse_progress(self, progress_value: Optional[str]) -> Optional[float]:
        """Parse progress string (e.g. '99%', '45.5%') into a float."""
        if not progress_value:
            return None
        match = self.METADATA_PROGRESS_PATTERN.search(str(progress_value))
        if match:
            try:
                return float(match.group(1))
            except ValueError:
                pass
        return None

    def _extract_title_from_file(self, file_name: Optional[str]) -> str:
        """Derive title from filename if YAML is missing."""
        if file_name:
            return file_name.replace(".md", "").strip()
        return "Unknown Title"

    def _extract_highlights_b(self, content: str) -> list[ParsedHighlight]:
        """Extract all highlights from Format B content.

        Format B structure:
            # 高亮划线
            #### Chapter Name
            > 📌 [highlight text](weread://...)
            > ⏱ 2023-11-06 11:02:52 ^bookId-chapter-range
        """
        highlights: list[ParsedHighlight] = []
        current_chapter: Optional[str] = None

        lines = content.split("\n")

        for i, line in enumerate(lines):
            stripped = line.strip()

            # Check for chapter heading (Format B uses ####)
            chapter_match = self.CHAPTER_B_PATTERN.match(stripped)
            if chapter_match:
                current_chapter = chapter_match.group(1).strip()
                continue

            # Check for highlight line: > 📌 [text](url) or > 📌 text
            hl_match = self.HIGHLIGHT_B_PATTERN.match(stripped)
            if hl_match:
                # Group(1)=bracketed text, Group(2)=URL from brackets
                # Group(3)=plain text (no brackets)
                highlight_text = hl_match.group(1) if hl_match.group(1) else hl_match.group(3)
                if highlight_text:
                    highlight_text = highlight_text.strip()
                url = hl_match.group(2) if hl_match.group(2) else None

                # Look ahead for timestamp line
                create_time: Optional[datetime] = None
                for j in range(i + 1, min(i + 3, len(lines))):
                    next_line = lines[j].strip()
                    ts_match = self.TIMESTAMP_B_PATTERN.match(next_line)
                    if ts_match:
                        try:
                            create_time = datetime.strptime(
                                ts_match.group(1), "%Y-%m-%d %H:%M:%S"
                            )
                        except ValueError:
                            pass
                        break
                    # Also check for URL in metadata line
                    url_match = self.URL_B_PATTERN.search(next_line)
                    if url_match and not url:
                        url = url_match.group(0)

                highlights.append(
                    ParsedHighlight(
                        content=highlight_text or stripped,
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
        # Must have sufficient content
        if len(content.strip()) < 50:
            return False

        # Accept both Format A (title pattern) and Format B (YAML frontmatter)
        if self._has_yaml_frontmatter(content):
            return True
        if self.TITLE_PATTERN.search(content):
            return True
        return False


# Singleton instance for convenience
markdown_parser = MarkdownParser()

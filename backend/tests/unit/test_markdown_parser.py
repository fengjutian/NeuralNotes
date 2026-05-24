"""Tests for the markdown parser service.

These tests verify the WeChat Reading markdown parsing functionality.
Following TDD approach: tests written first, implementation follows.
"""

import pytest
from datetime import datetime

from src.services.markdown_parser import MarkdownParser, ParsedBook, ParsedHighlight
from src.utils.exceptions import InvalidFileFormatException


class TestMarkdownParser:
    """Test suite for MarkdownParser."""

    @pytest.fixture
    def parser(self) -> MarkdownParser:
        """Create a parser instance."""
        return MarkdownParser()

    @pytest.fixture
    def valid_markdown(self) -> str:
        """Valid WeChat Reading markdown content."""
        return """# 思考，快与慢
作者: 丹尼尔·卡尼曼
分类: 心理学
ISBN: 978-7-111-35372-4
阅读时长: 12小时30分
阅读日期: 2024-01-15

## 第一章：两个系统

- 这是第一个高亮内容。
> 创建于 2024-01-15

- 这是第二个高亮内容，关于认知偏差。
> 创建于 2024-01-16

## 第二章：启发法

- 这是第三个高亮内容，讨论锚定效应。
> 创建于 2024-01-20
"""

    @pytest.fixture
    def minimal_markdown(self) -> str:
        """Minimal valid markdown content."""
        return """# 简单书名
作者: 作者名

- 高亮一
- 高亮二
"""

    # === Test: Parse Valid Markdown ===

    def test_parse_extracts_title(self, parser: MarkdownParser, valid_markdown: str) -> None:
        """Test that parser extracts book title correctly."""
        result = parser.parse(valid_markdown)
        assert result.title == "思考，快与慢"

    def test_parse_extracts_author(self, parser: MarkdownParser, valid_markdown: str) -> None:
        """Test that parser extracts author correctly."""
        result = parser.parse(valid_markdown)
        assert result.author == "丹尼尔·卡尼曼"

    def test_parse_extracts_category(self, parser: MarkdownParser, valid_markdown: str) -> None:
        """Test that parser extracts category correctly."""
        result = parser.parse(valid_markdown)
        assert result.category == "心理学"

    def test_parse_extracts_isbn(self, parser: MarkdownParser, valid_markdown: str) -> None:
        """Test that parser extracts ISBN correctly."""
        result = parser.parse(valid_markdown)
        assert result.isbn == "978-7-111-35372-4"

    def test_parse_extracts_reading_time(self, parser: MarkdownParser, valid_markdown: str) -> None:
        """Test that parser extracts reading time correctly."""
        result = parser.parse(valid_markdown)
        assert result.reading_time == "12小时30分"

    def test_parse_extracts_reading_date(self, parser: MarkdownParser, valid_markdown: str) -> None:
        """Test that parser extracts reading date correctly."""
        result = parser.parse(valid_markdown)
        assert result.reading_date == "2024-01-15"

    # === Test: Highlight Extraction ===

    def test_parse_extracts_highlights(self, parser: MarkdownParser, valid_markdown: str) -> None:
        """Test that parser extracts all highlights."""
        result = parser.parse(valid_markdown)
        assert len(result.highlights) == 3

    def test_parse_extracts_chapter(self, parser: MarkdownParser, valid_markdown: str) -> None:
        """Test that parser associates highlights with chapters."""
        result = parser.parse(valid_markdown)
        # First two highlights should be in chapter 1
        assert result.highlights[0].chapter == "第一章：两个系统"
        assert result.highlights[1].chapter == "第一章：两个系统"
        # Third highlight should be in chapter 2
        assert result.highlights[2].chapter == "第二章：启发法"

    def test_parse_extracts_highlight_content(self, parser: MarkdownParser, valid_markdown: str) -> None:
        """Test that parser extracts highlight text correctly."""
        result = parser.parse(valid_markdown)
        assert "第一个高亮内容" in result.highlights[0].content
        assert "第二个高亮内容" in result.highlights[1].content

    def test_parse_extracts_create_time(self, parser: MarkdownParser, valid_markdown: str) -> None:
        """Test that parser extracts highlight creation time."""
        result = parser.parse(valid_markdown)
        # This test will fail until implementation is complete
        assert result.highlights[0].create_time == datetime(2024, 1, 15)

    # === Test: Edge Cases ===

    def test_parse_minimal_content(self, parser: MarkdownParser, minimal_markdown: str) -> None:
        """Test parsing minimal valid markdown."""
        result = parser.parse(minimal_markdown)
        assert result.title == "简单书名"
        assert result.author == "作者名"
        assert len(result.highlights) == 2

    def test_parse_missing_author_uses_default(self, parser: MarkdownParser) -> None:
        """Test that missing author uses default value."""
        content = """# 书名

- 高亮内容
"""
        result = parser.parse(content)
        assert result.author == "Unknown Author"

    def test_parse_empty_content_raises_error(self, parser: MarkdownParser) -> None:
        """Test that empty content raises InvalidFileFormatException."""
        with pytest.raises(InvalidFileFormatException):
            parser.parse("")

    def test_parse_whitespace_only_raises_error(self, parser: MarkdownParser) -> None:
        """Test that whitespace-only content raises error."""
        with pytest.raises(InvalidFileFormatException):
            parser.parse("   \n\n  \t  ")

    def test_parse_missing_title_raises_error(self, parser: MarkdownParser) -> None:
        """Test that missing title raises error."""
        content = """作者: 测试作者

- 一些高亮内容
"""
        with pytest.raises(InvalidFileFormatException):
            parser.parse(content)

    # === Test: Validation ===

    def test_validate_format_valid(self, parser: MarkdownParser, valid_markdown: str) -> None:
        """Test validation passes for valid format."""
        assert parser.validate_format(valid_markdown) is True

    def test_validate_format_invalid(self, parser: MarkdownParser) -> None:
        """Test validation fails for invalid format."""
        assert parser.validate_format("Just some random text") is False

    def test_validate_format_too_short(self, parser: MarkdownParser) -> None:
        """Test validation fails for too short content."""
        content = "# Title"
        assert parser.validate_format(content) is False

    # === Test: File Name Handling ===

    def test_parse_with_filename(self, parser: MarkdownParser) -> None:
        """Test parsing uses filename as fallback for title."""
        content = """作者: 测试作者

- 高亮
"""
        result = parser.parse(content, file_name="从优秀到卓越.md")
        assert result.title == "从优秀到卓越"

    # === Test: Data Structure ===

    def test_parsed_highlight_to_dict(self) -> None:
        """Test ParsedHighlight serialization."""
        highlight = ParsedHighlight(
            content="测试内容",
            chapter="第一章",
            create_time=datetime(2024, 1, 15),
            url="https://example.com",
        )
        data = highlight.to_dict()
        assert data["content"] == "测试内容"
        assert data["chapter"] == "第一章"
        assert data["create_time"] == "2024-01-15T00:00:00"
        assert data["url"] == "https://example.com"

    def test_parsed_book_to_dict(self, parser: MarkdownParser, valid_markdown: str) -> None:
        """Test ParsedBook serialization."""
        result = parser.parse(valid_markdown)
        data = result.to_dict()
        assert data["title"] == "思考，快与慢"
        assert data["author"] == "丹尼尔·卡尼曼"
        assert data["highlight_count"] == 3
        assert len(data["highlights"]) == 3

"""Tests for AI analysis services (LLM Provider, Concept Extractor, AI Analyzer).

Following TDD approach: tests written first, implementation follows.
"""

from unittest.mock import MagicMock, patch, AsyncMock
from typing import Any

import pytest

from src.services.llm_provider import LLMProvider, LLMResponse
from src.services.concept_extractor import ConceptExtractor, ExtractedConcepts
from src.services.ai_analyzer import AIAnalyzer, AnalysisJob


class TestLLMProvider:
    """Test suite for LLMProvider."""

    @pytest.fixture
    def mock_openai_response(self) -> dict[str, Any]:
        """Mock OpenAI API response."""
        return {
            "choices": [
                {
                    "message": {
                        "content": '{"concepts": ["领导力", "决策力"], "domain": "管理学", "emotion": "agreement"}',
                    }
                }
            ]
        }

    @pytest.fixture
    def provider(self) -> LLMProvider:
        """Create LLM provider instance."""
        return LLMProvider(provider="openai", model="gpt-4")

    # === Test: Provider Configuration ===

    def test_provider_initialization(self, provider: LLMProvider) -> None:
        """Test provider is initialized correctly."""
        assert provider.provider == "openai"
        assert provider.model == "gpt-4"

    def test_provider_supports_streaming(self, provider: LLMProvider) -> None:
        """Test streaming support check."""
        assert isinstance(provider.supports_streaming(), bool)

    # === Test: Chat Completions ===

    @patch("openai.ChatCompletion.create")
    def test_chat_completion_success(
        self,
        mock_create: MagicMock,
        provider: LLMProvider,
        mock_openai_response: dict,
    ) -> None:
        """Test successful chat completion."""
        mock_create.return_value = mock_openai_response

        response = provider.chat_completion(
            messages=[{"role": "user", "content": "Hello"}]
        )

        assert response.content is not None
        assert "concepts" in response.content
        mock_create.assert_called_once()

    @patch("openai.ChatCompletion.create")
    def test_chat_completion_with_model_override(
        self,
        mock_create: MagicMock,
        provider: LLMProvider,
        mock_openai_response: dict,
    ) -> None:
        """Test chat completion with model override."""
        mock_create.return_value = mock_openai_response

        response = provider.chat_completion(
            messages=[{"role": "user", "content": "Hello"}],
            model="gpt-3.5-turbo",
        )

        assert response.content is not None
        # Verify model was passed to API call
        call_kwargs = mock_create.call_args[1]
        assert call_kwargs.get("model") == "gpt-3.5-turbo"

    @patch("openai.ChatCompletion.create")
    def test_chat_completion_handles_rate_limit(
        self,
        mock_create: MagicMock,
        provider: LLMProvider,
    ) -> None:
        """Test rate limit handling."""
        from openai.error import RateLimitError

        mock_create.side_effect = RateLimitError("Rate limit exceeded")

        with pytest.raises(Exception):  # Should raise after retries exhausted
            provider.chat_completion(
                messages=[{"role": "user", "content": "Hello"}],
                max_retries=1,
            )

    @patch("openai.ChatCompletion.create")
    def test_chat_completion_with_system_prompt(
        self,
        mock_create: MagicMock,
        provider: LLMProvider,
        mock_openai_response: dict,
    ) -> None:
        """Test chat completion with system prompt."""
        mock_create.return_value = mock_openai_response

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello"},
        ]
        provider.chat_completion(messages=messages)

        call_kwargs = mock_create.call_args[1]
        assert len(call_kwargs["messages"]) == 2
        assert call_kwargs["messages"][0]["role"] == "system"


class TestConceptExtractor:
    """Test suite for ConceptExtractor."""

    @pytest.fixture
    def extractor(self) -> ConceptExtractor:
        """Create concept extractor instance."""
        return ConceptExtractor()

    @pytest.fixture
    def sample_highlight(self) -> str:
        """Sample highlight text for extraction."""
        return (
            "领导力的本质是帮助他人成长和成功。"
            "一个优秀的领导者需要具备战略思维和同理心。"
            "信任是团队协作的基石。"
        )

    @pytest.fixture
    def mock_extraction_response(self) -> str:
        """Mock LLM extraction response."""
        return """{
            "concepts": ["领导力", "信任", "团队协作", "战略思维", "同理心"],
            "domain": "管理学",
            "emotion": "agreement",
            "user_focus": "领导力培养",
            "author_viewpoint": "强调信任在领导中的重要性"
        }"""

    # === Test: Extraction Prompts ===

    def test_extraction_prompt_includes_highlight(
        self,
        extractor: ConceptExtractor,
        sample_highlight: str,
    ) -> None:
        """Test extraction prompt contains highlight content."""
        prompt = extractor._build_extraction_prompt(sample_highlight)
        assert sample_highlight in prompt

    def test_extraction_prompt_requests_json_format(
        self,
        extractor: ConceptExtractor,
        sample_highlight: str,
    ) -> None:
        """Test extraction prompt requests JSON output."""
        prompt = extractor._build_extraction_prompt(sample_highlight)
        assert "json" in prompt.lower() or "JSON" in prompt

    # === Test: Response Parsing ===

    def test_parse_extraction_response_success(
        self,
        extractor: ConceptExtractor,
        mock_extraction_response: str,
    ) -> None:
        """Test successful response parsing."""
        result = extractor._parse_extraction_response(mock_extraction_response)

        assert isinstance(result, ExtractedConcepts)
        assert "领导力" in result.concepts
        assert "信任" in result.concepts
        assert result.domain == "管理学"
        assert result.emotion == "agreement"

    def test_parse_extraction_response_extracts_concepts(
        self,
        extractor: ConceptExtractor,
        mock_extraction_response: str,
    ) -> None:
        """Test concepts are correctly extracted."""
        result = extractor._parse_extraction_response(mock_extraction_response)

        assert len(result.concepts) >= 3
        assert all(isinstance(c, str) for c in result.concepts)

    def test_parse_extraction_response_handles_invalid_json(
        self,
        extractor: ConceptExtractor,
    ) -> None:
        """Test handling of invalid JSON response."""
        invalid_response = "This is not valid JSON"

        with pytest.raises(ValueError):
            extractor._parse_extraction_response(invalid_response)

    def test_parse_extraction_response_handles_partial_json(
        self,
        extractor: ConceptExtractor,
    ) -> None:
        """Test handling of partial JSON (with text before/after)."""
        partial_response = "Here is the analysis: {\"concepts\": [\"test\"], \"domain\": \"test\"} end of response"
        result = extractor._parse_extraction_response(partial_response)

        assert result.concepts == ["test"]
        assert result.domain == "test"

    # === Test: Validation ===

    def test_validate_concepts_filters_empty(
        self,
        extractor: ConceptExtractor,
    ) -> None:
        """Test validation filters out empty concepts."""
        concepts = ["领导力", "", "信任", "  "]
        validated = extractor._validate_concepts(concepts)

        assert "" not in validated
        assert "  " not in validated
        assert len(validated) == 2

    def test_validate_concepts_deduplicates(
        self,
        extractor: ConceptExtractor,
    ) -> None:
        """Test validation removes duplicates."""
        concepts = ["领导力", "领导力", "信任", "信任"]
        validated = extractor._validate_concepts(concepts)

        assert len(validated) == 2

    def test_validate_domain_accepts_valid(
        self,
        extractor: ConceptExtractor,
    ) -> None:
        """Test domain validation accepts valid domains."""
        valid_domains = ["管理学", "心理学", "哲学", "AI"]
        for domain in valid_domains:
            assert extractor._validate_domain(domain) is not None

    def test_validate_domain_returns_none_for_invalid(
        self,
        extractor: ConceptExtractor,
    ) -> None:
        """Test domain validation returns None for invalid."""
        assert extractor._validate_domain("") is None
        assert extractor._validate_domain("   ") is None


class TestAIAnalyzer:
    """Test suite for AIAnalyzer."""

    @pytest.fixture
    def analyzer(self) -> AIAnalyzer:
        """Create AI analyzer instance."""
        return AIAnalyzer(batch_size=5)

    @pytest.fixture
    def sample_highlights(self) -> list[dict[str, Any]]:
        """Sample highlights for analysis."""
        return [
            {"id": "1", "content": "领导力是帮助他人成功", "chapter": "第一章"},
            {"id": "2", "content": "信任是团队的基础", "chapter": "第二章"},
            {"id": "3", "content": "战略思维决定未来", "chapter": "第三章"},
        ]

    @pytest.fixture
    def mock_analyzer_with_mocks(
        self,
        analyzer: AIAnalyzer,
    ) -> tuple[AIAnalyzer, MagicMock, MagicMock]:
        """Analyzer with mocked dependencies."""
        mock_provider = MagicMock()
        mock_extractor = MagicMock()

        mock_extraction = ExtractedConcepts(
            concepts=["test"],
            domain="测试",
            emotion="neutral",
        )
        mock_provider.chat_completion.return_value = LLMResponse(
            content='{"concepts": ["test"], "domain": "测试", "emotion": "neutral"}',
            model="test",
            usage={"total_tokens": 100},
        )

        analyzer.llm_provider = mock_provider
        analyzer.extractor = mock_extractor

        return analyzer, mock_provider, mock_extractor

    # === Test: Job Management ===

    def test_create_analysis_job(
        self,
        analyzer: AIAnalyzer,
        sample_highlights: list[dict[str, Any]],
    ) -> str:
        """Test job creation returns job ID."""
        job_id = analyzer.create_job(highlights=sample_highlights)

        assert job_id is not None
        assert isinstance(job_id, str)
        assert len(job_id) > 0

    def test_get_job_status(
        self,
        analyzer: AIAnalyzer,
        sample_highlights: list[dict[str, Any]],
    ) -> None:
        """Test getting job status."""
        job_id = analyzer.create_job(highlights=sample_highlights)
        status = analyzer.get_job_status(job_id)

        assert status is not None
        assert status.job_id == job_id
        assert status.total > 0

    def test_get_nonexistent_job_raises_error(
        self,
        analyzer: AIAnalyzer,
    ) -> None:
        """Test getting non-existent job raises error."""
        with pytest.raises(ValueError):
            analyzer.get_job_status("nonexistent-job-id")

    def test_job_tracks_progress(
        self,
        analyzer: AIAnalyzer,
        sample_highlights: list[dict[str, Any]],
    ) -> None:
        """Test job progress tracking."""
        job_id = analyzer.create_job(highlights=sample_highlights)
        status = analyzer.get_job_status(job_id)

        # Initial progress should be 0
        assert status.completed == 0
        assert status.total == len(sample_highlights)
        assert status.progress_percent == 0.0

    # === Test: Analysis Processing ===

    @pytest.mark.asyncio
    async def test_analyze_highlight(
        self,
        analyzer: AIAnalyzer,
    ) -> None:
        """Test single highlight analysis."""
        # This will fail until implementation is complete
        pass

    # === Test: Batch Processing ===

    def test_batch_size_respected(
        self,
        analyzer: AIAnalyzer,
        sample_highlights: list[dict[str, Any]],
    ) -> None:
        """Test batch size configuration."""
        assert analyzer.batch_size == 5

        # Change batch size
        analyzer.batch_size = 10
        assert analyzer.batch_size == 10

    def test_process_batch_divides_into_chunks(
        self,
        analyzer: AIAnalyzer,
    ) -> None:
        """Test batch processing divides highlights into chunks."""
        highlights = [{"id": str(i)} for i in range(12)]

        batches = analyzer._divide_into_batches(highlights)

        assert len(batches) == 3  # 12 / 5 = 3 batches (4 + 4 + 4)
        assert len(batches[0]) == 4
        assert len(batches[1]) == 4
        assert len(batches[2]) == 4

    def test_process_batch_handles_remainder(
        self,
        analyzer: AIAnalyzer,
    ) -> None:
        """Test batch processing handles remainder correctly."""
        highlights = [{"id": str(i)} for i in range(7)]

        batches = analyzer._divide_into_batches(highlights)

        assert len(batches) == 2  # 7 / 5 = 2 batches (5 + 2)
        assert len(batches[0]) == 5
        assert len(batches[1]) == 2

    def test_process_batch_empty_list(
        self,
        analyzer: AIAnalyzer,
    ) -> None:
        """Test batch processing with empty list."""
        batches = analyzer._divide_into_batches([])
        assert len(batches) == 0

    # === Test: Error Handling ===

    def test_error_tracking(
        self,
        analyzer: AIAnalyzer,
        sample_highlights: list[dict[str, Any]],
    ) -> None:
        """Test error tracking during analysis."""
        job_id = analyzer.create_job(highlights=sample_highlights)
        status = analyzer.get_job_status(job_id)

        # Initial errors should be 0
        assert status.errors == 0

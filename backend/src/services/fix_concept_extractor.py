content = """
"""Concept extraction service using LLM.

Extracts concepts, domains, emotions, and insights from highlights.
"""

from dataclasses import dataclass
from typing import Optional

from src.services.llm_provider import LLMProvider, LLMResponse
from src.utils.logging import get_logger

logger = get_logger(__name__)


@dataclass
class ExtractedConcepts:
    """Extracted concept information from a highlight."""

    concepts: list[str]
    domain: Optional[str] = None
    emotion: Optional[str] = None
    user_focus: Optional[str] = None
    author_viewpoint: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert to dictionary."""
        return {
            "concepts": self.concepts,
            "domain": self.domain,
            "emotion": self.emotion,
            "user_focus": self.user_focus,
            "author_viewpoint": self.author_viewpoint,
        }


class ConceptExtractor:
    """LLM-based concept extractor for reading highlights."""

    DEFAULT_PROMPT_TEMPLATE = """Analyze the following highlight and extract key information.

Highlight content:
{highlight}

Please return the following information in JSON format:
{{
    "concepts": ["concept1", "concept2", ...],
    "domain": "subject domain",
    "emotion": "agreement/questioning/objection/excitement/neutral",
    "user_focus": "why user marked this",
    "author_viewpoint": "author main viewpoint"
}}
"""

    def __init__(
        self,
        llm_provider: Optional[LLMProvider] = None,
        prompt_template: Optional[str] = None,
        max_retries: int = 3,
    ) -> None:
        self.llm = llm_provider or LLMProvider()
        self.prompt_template = prompt_template or self.DEFAULT_PROMPT_TEMPLATE
        self.max_retries = max_retries
        self.logger = get_logger(self.__class__.__name__)

    def extract(self, highlight: str) -> Optional[ExtractedConcepts]:
        """Extract concepts from a highlight."""
        try:
            prompt = self._format_prompt(highlight)
            messages = [
                {"role": "system", "content": "You are a reading analysis expert."},
                {"role": "user", "content": prompt},
            ]

            response = self.llm.chat_completion(messages)
            return self._parse_response(response)

        except Exception as e:
            self.logger.error("Concept extraction failed: %s", str(e))
            return None

    def extract_batch(
        self,
        highlights: list[str],
    ) -> list[Optional[ExtractedConcepts]]:
        """Extract concepts from multiple highlights."""
        results = []
        for highlight in highlights:
            result = self.extract(highlight)
            results.append(result)

        self.logger.info(
            "Extracted concepts from %d highlights",
            len([r for r in results if r is not None]),
        )

        return results

    def _format_prompt(self, highlight: str) -> str:
        """Format prompt with highlight content."""
        return self.prompt_template.format(highlight=highlight)

    def _parse_response(self, response: LLMResponse) -> Optional[ExtractedConcepts]:
        """Parse LLM response to ExtractedConcepts."""
        if not response.content:
            return None

        try:
            import json
            import re

            json_match = re.search(r"\{[^{}]*\}", response.content, re.DOTALL)
            if json_match:
                data = json.loads(json_match.group())
                return ExtractedConcepts(
                    concepts=data.get("concepts", []),
                    domain=data.get("domain"),
                    emotion=data.get("emotion"),
                    user_focus=data.get("user_focus"),
                    author_viewpoint=data.get("author_viewpoint"),
                )

            self.logger.warning("Could not parse response as JSON")
            return None

        except (json.JSONDecodeError, KeyError) as e:
            self.logger.error("Failed to parse response: %s", str(e))
            return None
"""

with open("concept_extractor.py", "w", encoding="utf-8") as f:
    f.write(content)
print("Done")


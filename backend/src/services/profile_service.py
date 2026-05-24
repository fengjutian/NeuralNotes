"""AI Reading Profile service.

Generates reading persona, preferences, cognitive style analysis and blind spots.
"""

from collections import Counter
from dataclasses import dataclass, field
from typing import Any, Optional

from src.services.llm_provider import LLMProvider
from src.utils.logging import get_logger

logger = get_logger(__name__)


@dataclass
class ReadingProfile:
    """Complete reading profile.

    Attributes:
        preferences: Reading preferences breakdown.
        cognitive_style: Cognitive thinking tendencies.
        blind_spots: Identified reading gaps.
        summary: Overall profile summary.
    """

    preferences: dict[str, Any] = field(default_factory=dict)
    cognitive_style: dict[str, Any] = field(default_factory=dict)
    blind_spots: list[dict[str, Any]] = field(default_factory=list)
    summary: str = ""

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        return {
            "preferences": self.preferences,
            "cognitive_style": self.cognitive_style,
            "blind_spots": self.blind_spots,
            "summary": self.summary,
        }


class ProfileService:
    """Service for generating AI-powered reading profile.

    Analyzes user's reading history to:
    - Identify reading preferences (categories, authors, topics)
    - Detect cognitive style (rational, visionary, pragmatic, etc.)
    - Find reading blind spots and gaps
    - Generate personalized summary
    """

    MIN_BOOKS_FOR_PROFILE = 3

    def __init__(self, llm_provider: Optional[LLMProvider] = None) -> None:
        """Initialize profile service.

        Args:
            llm_provider: LLM provider for profile generation.
        """
        self.llm_provider = llm_provider or LLMProvider()
        self.logger = get_logger(self.__class__.__name__)

    def generate_profile(
        self,
        books: list[dict[str, Any]],
        concepts: list[dict[str, Any]],
        highlights: Optional[list[dict[str, Any]]] = None,
    ) -> ReadingProfile:
        """Generate a comprehensive reading profile.

        Args:
            books: List of book records.
            concepts: List of extracted concepts.
            highlights: Optional list of highlights.

        Returns:
            Complete ReadingProfile.

        Raises:
            ValueError: If insufficient data for profile.
        """
        if len(books) < self.MIN_BOOKS_FOR_PROFILE:
            raise ValueError(
                f"Insufficient data: need at least {self.MIN_BOOKS_FOR_PROFILE} books, got {len(books)}"
            )

        self.logger.info(
            "Generating profile from %d books and %d concepts",
            len(books),
            len(concepts),
        )

        # Generate profile components
        preferences = self.analyze_preferences(books, concepts)
        cognitive_style = self.analyze_cognitive_style(concepts)
        blind_spots = self.detect_blind_spots(books, concepts)
        summary = self._generate_summary(preferences, cognitive_style, blind_spots)

        return ReadingProfile(
            preferences=preferences,
            cognitive_style=cognitive_style,
            blind_spots=blind_spots,
            summary=summary,
        )

    def analyze_preferences(
        self,
        books: list[dict[str, Any]],
        concepts: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """Analyze reading preferences.

        Args:
            books: List of book records.
            concepts: List of concept records.

        Returns:
            Preference breakdown.
        """
        # Category distribution
        categories = Counter(
            b.get("category") for b in books if b.get("category")
        )

        # Author frequency
        authors = Counter(
            b.get("author") for b in books if b.get("author")
        )

        # Concept domains
        domains = Counter(
            c.get("domain") for c in concepts if c.get("domain")
        )

        # Top concepts
        concept_names = Counter(
            c.get("name") for c in concepts if c.get("name")
        )

        return {
            "categories": [
                {"name": cat, "count": count}
                for cat, count in categories.most_common(10)
            ],
            "top_authors": [
                {"name": author, "count": count}
                for author, count in authors.most_common(5)
            ],
            "top_domains": [
                {"name": domain, "count": count}
                for domain, count in domains.most_common(5)
            ],
            "top_concepts": [
                {"name": name, "count": count}
                for name, count in concept_names.most_common(10)
            ],
        }

    def analyze_cognitive_style(
        self,
        concepts: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """Analyze cognitive thinking style.

        Args:
            concepts: List of concept records.

        Returns:
            Cognitive style breakdown.
        """
        # Cognitive style indicators based on concept patterns
        style_indicators = {
            "理性主义": ["逻辑", "证据", "数据", "分析", "批判"],
            "长期主义": ["长期", "耐心", "积累", "复利", "时间"],
            "愿景驱动": ["愿景", "使命", "理想", "未来", "梦想"],
            "务实倾向": ["实践", "执行", "行动", "方法", "工具"],
            "人文关怀": ["同理心", "人性", "关怀", "爱", "善意"],
            "创新思维": ["创新", "突破", "创造", "想象", "颠覆"],
        }

        concept_names = [c.get("name", "") for c in concepts]

        style_scores = {}
        for style, indicators in style_indicators.items():
            score = sum(
                1 for name in concept_names
                for indicator in indicators
                if indicator in name
            )
            style_scores[style] = score

        # Normalize to percentages
        total = sum(style_scores.values()) or 1
        style_percentages = {
            style: round((score / total) * 100, 1)
            for style, score in style_scores.items()
        }

        # Primary style
        primary = max(style_percentages, key=style_percentages.get)

        return {
            "primary_style": primary,
            "distribution": style_percentages,
            "intensity": "high" if style_percentages[primary] > 30 else "moderate",
        }

    def detect_blind_spots(
        self,
        books: list[dict[str, Any]],
        concepts: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """Detect reading blind spots.

        Args:
            books: List of book records.
            concepts: List of concept records.

        Returns:
            List of identified blind spots.
        """
        # All possible domains
        all_domains = {
            "管理学", "心理学", "哲学", "经济学", "历史",
            "文学", "社会学", "物理学", "生物学", "数学",
            "AI", "计算机科学", "教育学", "政治学", "法学",
            "医学", "艺术", "宗教", "伦理", "环境学",
        }

        # Domains user has read
        read_domains = set()
        for book in books:
            category = book.get("category")
            if category:
                read_domains.add(category)

        for concept in concepts:
            domain = concept.get("domain")
            if domain:
                read_domains.add(domain)

        # Missing domains
        missing_domains = all_domains - read_domains

        blind_spots = []
        for domain in sorted(missing_domains)[:5]:
            blind_spots.append({
                "domain": domain,
                "reason": f"尚未在{domain}领域有阅读记录",
                "suggestion": f"建议尝试{domain}领域的经典著作",
                "severity": "medium" if domain in {"哲学", "历史", "心理学"} else "low",
            })

        return blind_spots

    def _generate_summary(
        self,
        preferences: dict[str, Any],
        cognitive_style: dict[str, Any],
        blind_spots: list[dict[str, Any]],
    ) -> str:
        """Generate profile summary.

        Args:
            preferences: Preference analysis.
            cognitive_style: Cognitive style analysis.
            blind_spots: Blind spot analysis.

        Returns:
            Summary text.
        """
        parts = []

        # Reading preferences summary
        top_categories = preferences.get("categories", [])[:3]
        if top_categories:
            cats = "、".join(c["name"] for c in top_categories)
            parts.append(f"您的主要阅读兴趣集中在{cats}领域")

        # Cognitive style summary
        primary = cognitive_style.get("primary_style", "未知")
        parts.append(f"思维倾向偏向{primary}")

        # Blind spots summary
        if blind_spots:
            spots = blind_spots[0]["domain"]
            parts.append(f"建议扩展{spots}等领域的阅读")

        return "。".join(parts) + "。"

    def should_regenerate(
        self,
        current_book_count: int,
        last_regeneration_count: int = 0,
        threshold: int = 3,
    ) -> bool:
        """Check if profile should be regenerated.

        Args:
            current_book_count: Current number of books.
            last_regeneration_count: Book count at last regeneration.
            threshold: Minimum new books before regenerating.

        Returns:
            True if regeneration is recommended.
        """
        diff = current_book_count - last_regeneration_count
        return diff >= threshold


# Singleton instance
profile_service = ProfileService()

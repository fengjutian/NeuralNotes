"""Business logic services.

Lazy imports to avoid loading heavy dependencies (torch, transformers)
when not needed.
"""

# Import lightweight services directly
from src.services.markdown_parser import MarkdownParser
from src.services.file_service import FileService

# Lazy imports for heavy services
def __getattr__(name):
    if name == "VectorService":
        from src.services.vector_service import VectorService
        return VectorService
    elif name == "EmbeddingService":
        from src.services.embedding_service import EmbeddingService
        return EmbeddingService
    elif name == "GraphService":
        from src.services.graph_service import GraphService
        return GraphService
    elif name == "LLMProvider":
        from src.services.llm_provider import LLMProvider
        return LLMProvider
    elif name == "ConceptExtractor":
        from src.services.concept_extractor import ConceptExtractor
        return ConceptExtractor
    elif name == "AIAnalyzer":
        from src.services.ai_analyzer import AIAnalyzer
        return AIAnalyzer
    elif name == "ProfileService":
        from src.services.profile_service import ProfileService
        return ProfileService
    elif name == "RecommendationService":
        from src.services.recommendation_service import RecommendationService
        return RecommendationService
    elif name == "TimelineService":
        from src.services.timeline_service import TimelineService
        return TimelineService
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "MarkdownParser",
    "FileService",
    "VectorService",
    "EmbeddingService",
    "GraphService",
    "LLMProvider",
    "ConceptExtractor",
    "AIAnalyzer",
    "ProfileService",
    "RecommendationService",
    "TimelineService",
]

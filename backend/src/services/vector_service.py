"""Vector search service using Qdrant.

Provides semantic search and retrieval capabilities.
"""

from typing import Any, Optional

from src.qdrant_client import QdrantClientWrapper, qdrant_client
from src.services.embedding_service import EmbeddingService, embedding_service
from src.utils.logging import get_logger

logger = get_logger(__name__)


class VectorService:
    """Service for vector-based semantic search.

    Combines embedding generation with Qdrant vector storage
    for semantic search across highlights.
    """

    def __init__(
        self,
        qdrant: Optional[QdrantClientWrapper] = None,
        embedding: Optional[EmbeddingService] = None,
    ) -> None:
        """Initialize vector service.

        Args:
            qdrant: Qdrant client instance.
            embedding: Embedding service instance.
        """
        self.qdrant = qdrant or qdrant_client
        self.embedding = embedding or embedding_service
        self.logger = get_logger(self.__class__.__name__)

    def index_highlight(
        self,
        highlight_id: str,
        content: str,
        book_id: Optional[str] = None,
        chapter: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
    ) -> str:
        """Index a highlight for semantic search.

        Args:
            highlight_id: Unique highlight ID.
            content: Highlight text content.
            book_id: Associated book ID.
            chapter: Chapter name.
            metadata: Additional metadata.

        Returns:
            Point ID in vector store.
        """
        # Generate embedding
        vector = self.embedding.embed_single(content)

        # Build payload
        payload = {
            "highlight_id": highlight_id,
            "content": content,
            "book_id": book_id,
            "chapter": chapter,
            **(metadata or {}),
        }

        # Store in Qdrant
        point_id = self.qdrant.upsert_point(
            vector=vector,
            payload=payload,
            point_id=highlight_id,
        )

        self.logger.debug("Indexed highlight: %s", highlight_id)
        return point_id

    def index_batch(
        self,
        highlights: list[dict[str, Any]],
    ) -> int:
        """Index multiple highlights.

        Args:
            highlights: List of highlight dicts with id, content.

        Returns:
            Number of highlights indexed.
        """
        count = 0
        for h in highlights:
            try:
                self.index_highlight(
                    highlight_id=h["id"],
                    content=h["content"],
                    book_id=h.get("book_id"),
                    chapter=h.get("chapter"),
                    metadata=h.get("metadata"),
                )
                count += 1
            except Exception as e:
                self.logger.error(
                    "Failed to index highlight %s: %s",
                    h.get("id", "unknown"),
                    str(e),
                )

        self.logger.info("Indexed %d highlights", count)
        return count

    def search(
        self,
        query: str,
        limit: int = 10,
        book_id: Optional[str] = None,
        score_threshold: float = 0.0,
    ) -> list[dict[str, Any]]:
        """Perform semantic search.

        Args:
            query: Search query.
            limit: Maximum results.
            book_id: Optional filter by book.
            score_threshold: Minimum relevance score.

        Returns:
            List of search results with scores.
        """
        # Generate query embedding
        query_vector = self.embedding.embed_single(query)

        # Build filter
        filter_conditions = None
        if book_id:
            filter_conditions = {
                "must": [
                    {
                        "key": "book_id",
                        "match": {"value": book_id},
                    }
                ]
            }

        # Search
        results = self.qdrant.search(
            query_vector=query_vector,
            limit=limit,
            filter_conditions=filter_conditions,
            score_threshold=score_threshold,
        )

        # Format results
        formatted = []
        for result in results:
            formatted.append({
                "id": result["id"],
                "score": result["score"],
                "content": result["payload"].get("content", ""),
                "book_id": result["payload"].get("book_id"),
                "chapter": result["payload"].get("chapter"),
                "highlight_id": result["payload"].get("highlight_id"),
            })

        self.logger.info(
            "Search '%s' returned %d results (threshold: %.2f)",
            query,
            len(formatted),
            score_threshold,
        )

        return formatted

    def search_by_vector(
        self,
        vector: list[float],
        limit: int = 10,
        **kwargs: Any,
    ) -> list[dict[str, Any]]:
        """Search using pre-computed vector.

        Args:
            vector: Query vector.
            limit: Maximum results.
            **kwargs: Additional search parameters.

        Returns:
            List of search results.
        """
        results = self.qdrant.search(
            query_vector=vector,
            limit=limit,
            **kwargs,
        )

        return [
            {
                "id": r["id"],
                "score": r["score"],
                "payload": r["payload"],
            }
            for r in results
        ]

    def delete_highlight(self, highlight_id: str) -> bool:
        """Delete a highlight from the index.

        Args:
            highlight_id: Highlight ID.

        Returns:
            True if deleted successfully.
        """
        return self.qdrant.delete_point(highlight_id)

    def get_highlight(self, highlight_id: str) -> Optional[dict[str, Any]]:
        """Get a highlighted document by ID.

        Args:
            highlight_id: Highlight ID.

        Returns:
            Highlight data or None if not found.
        """
        return self.qdrant.get_point(highlight_id)

    def count_indexed(self, book_id: Optional[str] = None) -> int:
        """Count indexed highlights.

        Args:
            book_id: Optional filter by book.

        Returns:
            Number of indexed highlights.
        """
        filter_conditions = None
        if book_id:
            filter_conditions = {
                "must": [
                    {
                        "key": "book_id",
                        "match": {"value": book_id},
                    }
                ]
            }

        return self.qdrant.count_points(filter_conditions)


# Singleton instance
vector_service = VectorService()

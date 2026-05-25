"""Qdrant vector database client for semantic search."""

from typing import Any, Optional
import uuid

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Filter
from qdrant_client.http.exceptions import UnexpectedResponse

from src.config import settings
from src.utils.exceptions import VectorSearchException
from src.utils.logging import get_logger

logger = get_logger(__name__)


class QdrantClientWrapper:
    """Qdrant vector database client for highlight embedding storage and search.

    Handles connection management, collection operations,
    and semantic search for the cognitive reading graph.
    """

    def __init__(self) -> None:
        """Initialize Qdrant client."""
        self._client: Optional[QdrantClient] = None
        self._collection_name = settings.qdrant_collection

    def connect(self) -> None:
        """Establish connection to Qdrant."""
        try:
            self._client = QdrantClient(
                url=settings.qdrant_url,
                timeout=30,
            )
            # Verify connection by getting collections
            self._client.get_collections()
            logger.info("Connected to Qdrant at %s", settings.qdrant_url)
        except Exception as e:
            logger.error("Failed to connect to Qdrant: %s", str(e))
            raise VectorSearchException(f"Failed to connect to Qdrant: {e}") from e

    def disconnect(self) -> None:
        """Close connection to Qdrant."""
        self._client = None
        logger.info("Disconnected from Qdrant")

    def ensure_collection(self, vector_size: int = 1536) -> None:
        """Ensure the highlights collection exists with correct configuration.

        Args:
            vector_size: Dimension of the embedding vectors.
        """
        if not self._client:
            raise VectorSearchException("Not connected to Qdrant")

        try:
            # Check if collection exists
            collections = self._client.get_collections().collections
            collection_names = [c.name for c in collections]

            if self._collection_name not in collection_names:
                # Create collection
                self._client.create_collection(
                    collection_name=self._collection_name,
                    vectors_config=VectorParams(
                        size=vector_size,
                        distance=Distance.COSINE,
                    ),
                )
                logger.info(
                    "Created collection '%s' with vector size %d",
                    self._collection_name,
                    vector_size,
                )
        except UnexpectedResponse as e:
            logger.error("Failed to ensure collection: %s", str(e))
            raise VectorSearchException(f"Failed to ensure collection: {e}") from e

    def upsert_point(
        self,
        vector: list[float],
        payload: dict[str, Any],
        point_id: Optional[str] = None,
    ) -> str:
        """Insert or update a point in the collection.

        Args:
            vector: Embedding vector.
            payload: Metadata payload.
            point_id: Optional custom point ID (generated if not provided).

        Returns:
            Point ID.
        """
        if not self._client:
            raise VectorSearchException("Not connected to Qdrant")

        point_uuid = point_id or str(uuid.uuid4())
        point = PointStruct(
            id=point_uuid,
            vector=vector,
            payload=payload,
        )

        self._client.upsert(
            collection_name=self._collection_name,
            points=[point],
        )
        logger.debug("Upserted point %s", point_uuid)
        return point_uuid

    def search(
        self,
        query_vector: list[float],
        limit: int = 10,
        filter_conditions: Optional[dict[str, Any]] = None,
        score_threshold: Optional[float] = None,
    ) -> list[dict[str, Any]]:
        """Perform semantic search.

        Args:
            query_vector: Query embedding vector.
            limit: Maximum number of results.
            filter_conditions: Optional filters for the search.
            score_threshold: Minimum relevance score.

        Returns:
            List of search results with scores.
        """
        if not self._client:
            raise VectorSearchException("Not connected to Qdrant")

        search_filter = None
        if filter_conditions:
            search_filter = Filter(**filter_conditions)

        results = self._client.search(
            collection_name=self._collection_name,
            query_vector=query_vector,
            limit=limit,
            query_filter=search_filter,
            score_threshold=score_threshold,
        )

        return [
            {
                "id": result.id,
                "score": result.score,
                "payload": result.payload,
            }
            for result in results
        ]

    def get_point(self, point_id: str) -> Optional[dict[str, Any]]:
        """Get a point by ID.

        Args:
            point_id: Point ID.

        Returns:
            Point data or None if not found.
        """
        if not self._client:
            raise VectorSearchException("Not connected to Qdrant")

        try:
            result = self._client.retrieve(
                collection_name=self._collection_name,
                ids=[point_id],
            )
            if result:
                point = result[0]
                return {
                    "id": point.id,
                    "vector": point.vector,
                    "payload": point.payload,
                }
            return None
        except Exception:
            return None

    def delete_point(self, point_id: str) -> bool:
        """Delete a point by ID.

        Args:
            point_id: Point ID to delete.

        Returns:
            True if deleted successfully.
        """
        if not self._client:
            raise VectorSearchException("Not connected to Qdrant")

        try:
            self._client.delete(
                collection_name=self._collection_name,
                points_selector=[point_id],
            )
            return True
        except Exception as e:
            logger.error("Failed to delete point %s: %s", point_id, str(e))
            return False

    def count_points(self, filter_conditions: Optional[dict[str, Any]] = None) -> int:
        """Count points in the collection.

        Args:
            filter_conditions: Optional filters.

        Returns:
            Number of points.
        """
        if not self._client:
            raise VectorSearchException("Not connected to Qdrant")

        count_filter = Filter(**filter_conditions) if filter_conditions else None
        result = self._client.count(
            collection_name=self._collection_name,
            count_filter=count_filter,
        )
        return result.count


# Global client instance
qdrant_client = QdrantClientWrapper()


def get_qdrant() -> QdrantClientWrapper:
    """Get Qdrant client instance for dependency injection.

    Returns:
        QdrantClientWrapper instance.
    """
    return qdrant_client

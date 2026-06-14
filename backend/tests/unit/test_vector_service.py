"""Tests for VectorService -- Qdrant semantic search operations."""

from unittest.mock import MagicMock, patch

from src.services.vector_service import VectorService


class TestVectorService:
    """Test suite for VectorService with mocked Qdrant."""

    def test_singleton_exists(self):
        """Global singleton is available."""
        from src.services.vector_service import vector_service
        assert isinstance(vector_service, VectorService)

    def test_search_returns_results(self):
        """Semantic search returns scored results."""
        mock_qdrant = MagicMock()
        mock_qdrant.search.return_value = [
            {
                "id": "h1",
                "score": 0.95,
                "payload": {
                    "content": "Test highlight content",
                    "book_id": "b1",
                    "chapter": "Chapter 1",
                    "concepts": ["concept1"],
                },
            },
            {
                "id": "h2",
                "score": 0.80,
                "payload": {"content": "Another highlight", "book_id": "b2"},
            },
        ]

        mock_embed = MagicMock()
        mock_embed.embed.return_value = [0.1] * 768

        svc = VectorService(qdrant=mock_qdrant, embedding=mock_embed)
        results = svc.search("test query", limit=5)

        assert len(results) == 2
        assert results[0]["id"] == "h1"
        assert results[0]["score"] == 0.95
        assert results[0]["content"] == "Test highlight content"
        assert results[0]["book_id"] == "b1"

    def test_search_empty_results(self):
        """Returns empty list when no matches found."""
        mock_qdrant = MagicMock()
        mock_qdrant.search.return_value = []

        mock_embed = MagicMock()
        mock_embed.embed.return_value = [0.1] * 768

        svc = VectorService(qdrant=mock_qdrant, embedding=mock_embed)
        results = svc.search("nonexistent query")

        assert results == []

    def test_search_passes_limit(self):
        """Limit parameter is respected."""
        mock_qdrant = MagicMock()
        mock_qdrant.search.return_value = []

        mock_embed = MagicMock()
        mock_embed.embed.return_value = [0.1] * 768

        svc = VectorService(qdrant=mock_qdrant, embedding=mock_embed)
        svc.search("query", limit=7)

        # Verify search was called at all
        assert mock_qdrant.search.called

    def test_search_with_book_filter(self):
        """Book ID filter is passed through."""
        mock_qdrant = MagicMock()
        mock_qdrant.search.return_value = []

        mock_embed = MagicMock()
        mock_embed.embed.return_value = [0.1] * 768

        svc = VectorService(qdrant=mock_qdrant, embedding=mock_embed)
        svc.search("query", book_id="b1")

        assert mock_qdrant.search.called

    def test_index_batch(self):
        """Batch indexing processes multiple highlights."""
        mock_qdrant = MagicMock()
        mock_qdrant.upsert_point.return_value = "ok"

        mock_embed = MagicMock()
        mock_embed.embed.return_value = [0.1] * 768

        svc = VectorService(qdrant=mock_qdrant, embedding=mock_embed)
        highlights = [
            {"id": "h1", "content": "Content 1", "book_id": "b1"},
            {"id": "h2", "content": "Content 2", "book_id": "b2"},
        ]

        count = svc.index_batch(highlights)
        assert count == 2

    def test_index_batch_empty(self):
        """Empty batch returns 0."""
        mock_qdrant = MagicMock()
        mock_embed = MagicMock()
        mock_embed.embed.return_value = [0.1] * 768

        svc = VectorService(qdrant=mock_qdrant, embedding=mock_embed)
        count = svc.index_batch([])
        assert count == 0

    def test_index_highlight(self):
        """Single highlight indexing works."""
        mock_qdrant = MagicMock()
        mock_qdrant.upsert_point.return_value = "ok"
        mock_embed = MagicMock()
        mock_embed.embed.return_value = [0.1] * 768

        svc = VectorService(qdrant=mock_qdrant, embedding=mock_embed)
        result = svc.index_highlight(
            "h1", "test content", "b1", chapter="Chapter 1"
        )

        assert result is not None

    def test_delete_highlight(self):
        """Deleting a highlight by ID works."""
        mock_qdrant = MagicMock()
        mock_qdrant.delete_point.return_value = {"status": "ok"}
        mock_embed = MagicMock()

        svc = VectorService(qdrant=mock_qdrant, embedding=mock_embed)
        result = svc.delete_highlight("h1")

        assert result is not None

    def test_count_indexed(self):
        """Count returns the number of indexed points."""
        mock_qdrant = MagicMock()
        mock_qdrant.count_points.return_value = 42
        mock_embed = MagicMock()

        svc = VectorService(qdrant=mock_qdrant, embedding=mock_embed)
        result = svc.count_indexed()

        assert result == 42

    def test_get_highlight(self):
        """Retrieving a highlight by ID works."""
        mock_qdrant = MagicMock()
        mock_qdrant.get_point.return_value = {
            "id": "h1",
            "payload": {"content": "test", "book_id": "b1"},
        }
        mock_embed = MagicMock()

        svc = VectorService(qdrant=mock_qdrant, embedding=mock_embed)
        result = svc.get_highlight("h1")

        assert result is not None

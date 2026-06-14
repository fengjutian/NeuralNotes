"""Tests for GraphService -- Neo4j knowledge graph operations."""

from unittest.mock import MagicMock, patch

from src.services.graph_service import GraphService


class TestGraphService:
    """Test suite for GraphService with mocked Neo4j."""

    def test_singleton_exists(self):
        """Global singleton is available."""
        from src.services.graph_service import graph_service
        assert isinstance(graph_service, GraphService)

    def test_get_full_graph_returns_nodes_and_edges(self):
        """Returns structured nodes and edges from Neo4j."""
        mock_client = MagicMock()
        mock_client.execute_query.return_value = [
            {"n": {"id": "1", "type": "Book", "title": "Book 1", "author": "X"}},
        ]

        svc = GraphService()
        svc.client = mock_client

        nodes, edges = svc.get_full_graph(limit=10)

        assert isinstance(nodes, list)
        assert isinstance(edges, list)

    def test_get_full_graph_calls_neo4j(self):
        """Calls Neo4j execute_query."""
        mock_client = MagicMock()
        mock_client.execute_query.return_value = []

        svc = GraphService()
        svc.client = mock_client
        svc.get_full_graph(limit=5)

        assert mock_client.execute_query.called

    def test_get_book_graph_filters_by_book(self):
        """Returns empty when Neo4j returns nothing."""
        mock_client = MagicMock()
        mock_client.execute_query.return_value = []

        svc = GraphService()
        svc.client = mock_client
        nodes, edges = svc.get_book_graph(
            "123e4567-e89b-12d3-a456-426614174000"
        )

        assert nodes == []
        assert edges == []

    def test_link_book_to_author(self):
        """Linking book to author calls Neo4j."""
        mock_client = MagicMock()
        mock_client.execute_query.return_value = [{"rel": {}}]

        svc = GraphService()
        svc.client = mock_client

        result = svc.link_book_to_author("b1", "a1")
        assert mock_client.execute_query.called

    def test_link_highlight_to_book(self):
        """Linking highlight to book calls Neo4j."""
        mock_client = MagicMock()
        mock_client.execute_query.return_value = [{"rel": {}}]

        svc = GraphService()
        svc.client = mock_client

        svc.link_highlight_to_book("h1", "b1")
        assert mock_client.execute_query.called

    def test_create_author_node(self):
        """Creates an author node in Neo4j."""
        mock_client = MagicMock()
        mock_client.execute_query.return_value = [{"a": {"id": "a1"}}]

        svc = GraphService()
        svc.client = mock_client

        result = svc.create_author_node("a1", "Test Author")

        assert result is not None
        assert mock_client.execute_query.called

    def test_create_book_node(self):
        """Creates a book node in Neo4j."""
        mock_client = MagicMock()
        mock_client.execute_query.return_value = [{"n": {"id": "b1"}}]

        svc = GraphService()
        svc.client = mock_client

        result = svc.create_book_node("b1", "Test Book", "Author")

        assert result is not None
        assert mock_client.execute_query.called

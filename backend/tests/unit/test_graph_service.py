"""Tests for GraphService -- Neo4j knowledge graph operations."""

from unittest.mock import MagicMock

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

    def test_get_full_graph_calls_execute_query(self):
        """get_full_graph calls client.execute_query."""
        mock_client = MagicMock()
        mock_client.execute_query.return_value = []

        svc = GraphService()
        svc.client = mock_client
        svc.get_full_graph(limit=5)

        assert mock_client.execute_query.called

    def test_get_book_graph_filters_by_book(self):
        """Returns empty lists when Neo4j returns nothing."""
        mock_client = MagicMock()
        mock_client.execute_query.return_value = []

        svc = GraphService()
        svc.client = mock_client
        nodes, edges = svc.get_book_graph(
            "123e4567-e89b-12d3-a456-426614174000"
        )

        assert nodes == []
        assert edges == []

    def test_create_book_node_calls_create_node(self):
        """create_book_node uses client.create_node('Book', ...)."""
        mock_client = MagicMock()
        mock_client.create_node.return_value = {"id": "b1", "title": "Test"}

        svc = GraphService()
        svc.client = mock_client
        result = svc.create_book_node("b1", "Test Book", "Author")

        assert result is not None
        mock_client.create_node.assert_called_once()

    def test_create_author_node_calls_create_node(self):
        """create_author_node uses client.create_node('Author', ...)."""
        mock_client = MagicMock()
        mock_client.create_node.return_value = {"id": "a1"}

        svc = GraphService()
        svc.client = mock_client
        result = svc.create_author_node("a1", "Test Author")

        assert result is not None
        mock_client.create_node.assert_called_once()

    def test_create_concept_node_calls_get_and_create(self):
        """create_concept_node checks existence then creates."""
        mock_client = MagicMock()
        mock_client.get_node.return_value = None
        mock_client.create_node.return_value = {"id": "c1"}

        svc = GraphService()
        svc.client = mock_client
        result = svc.create_concept_node("c1", "psychology", "social")

        assert result is not None
        mock_client.get_node.assert_called_once()
        mock_client.create_node.assert_called_once()

    def test_create_highlight_node_calls_create_node(self):
        """create_highlight_node uses client.create_node('Highlight', ...)."""
        mock_client = MagicMock()
        mock_client.create_node.return_value = {"id": "h1"}

        svc = GraphService()
        svc.client = mock_client
        result = svc.create_highlight_node(
            "h1", "b1", "Test content", chapter="Chapter 1"
        )

        assert result is not None
        mock_client.create_node.assert_called_once()

    def test_link_book_to_author_calls_create_relationship(self):
        """link_book_to_author uses client.create_relationship."""
        mock_client = MagicMock()
        mock_client.create_relationship.return_value = {"type": "WRITTEN_BY"}

        svc = GraphService()
        svc.client = mock_client
        svc.link_book_to_author("b1", "a1")

        mock_client.create_relationship.assert_called_once()

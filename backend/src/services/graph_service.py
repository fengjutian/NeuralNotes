"""Knowledge Graph service for Neo4j operations.

Manages nodes, relationships, and graph queries.
"""

from typing import Any, Optional, Union
from uuid import UUID

from src.neo4j_client import Neo4jClient, neo4j_client
from src.schemas.graph import GraphNode, GraphEdge, NodeType, EdgeType
from src.utils.logging import get_logger

logger = get_logger(__name__)


class GraphService:
    """Service for managing the knowledge graph in Neo4j.

    Handles creation and querying of:
    - Book nodes
    - Concept nodes
    - Author nodes
    - Highlight nodes
    - Relationships between nodes
    """

    def __init__(self, client: Optional[Neo4jClient] = None) -> None:
        """Initialize graph service.

        Args:
            client: Neo4j client instance.
        """
        self.client = client or neo4j_client
        self.logger = get_logger(self.__class__.__name__)

    # === Node Operations ===

    def create_book_node(
        self,
        book_id: Union[str, UUID],
        title: str,
        author: str,
        category: Optional[str] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create a book node in the graph.

        Args:
            book_id: Book UUID.
            title: Book title.
            author: Author name.
            category: Book category.
            **kwargs: Additional properties.

        Returns:
            Created node properties.
        """
        properties = {
            "id": str(book_id),
            "title": title,
            "author": author,
            "category": category,
            **kwargs,
        }

        result = self.client.create_node("Book", properties)
        self.logger.info("Created book node: %s", title)
        return result

    def create_concept_node(
        self,
        concept_id: Union[str, UUID],
        name: str,
        domain: Optional[str] = None,
        frequency: int = 0,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create or update a concept node.

        Args:
            concept_id: Concept UUID.
            name: Concept name.
            domain: Subject domain.
            frequency: Mention frequency.
            **kwargs: Additional properties.

        Returns:
            Created/updated node properties.
        """
        properties = {
            "id": str(concept_id),
            "name": name,
            "domain": domain,
            "frequency": frequency,
            **kwargs,
        }

        # Check if concept exists
        existing = self.client.get_node(
            "Concept",
            "name",
            name,
        )

        if existing:
            # Update frequency
            query = """
            MATCH (c:Concept {name: $name})
            SET c.frequency = c.frequency + 1
            RETURN c
            """
            results = self.client.execute_query(query, {"name": name})
            self.logger.debug("Updated concept frequency: %s", name)
            return results[0]["c"] if results else existing

        result = self.client.create_node("Concept", properties)
        self.logger.info("Created concept node: %s", name)
        return result

    def create_author_node(
        self,
        name: str,
        bio: Optional[str] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create an author node.

        Args:
            name: Author name.
            bio: Author biography.
            **kwargs: Additional properties.

        Returns:
            Created node properties.
        """
        # Check if author exists
        existing = self.client.get_node("Author", "name", name)
        if existing:
            return existing

        properties = {
            "name": name,
            "bio": bio,
            **kwargs,
        }

        result = self.client.create_node("Author", properties)
        self.logger.info("Created author node: %s", name)
        return result

    def create_highlight_node(
        self,
        highlight_id: Union[str, UUID],
        content: str,
        chapter: Optional[str] = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        """Create a highlight node.

        Args:
            highlight_id: Highlight UUID.
            content: Highlight text.
            chapter: Chapter name.
            **kwargs: Additional properties.

        Returns:
            Created node properties.
        """
        properties = {
            "id": str(highlight_id),
            "content": content,
            "chapter": chapter,
            **kwargs,
        }

        result = self.client.create_node("Highlight", properties)
        self.logger.debug("Created highlight node: %s...", content[:50])
        return result

    # === Relationship Operations ===

    def link_book_to_concept(
        self,
        book_id: Union[str, UUID],
        concept_name: str,
        weight: float = 1.0,
    ) -> dict[str, Any]:
        """Create HAS_CONCEPT relationship.

        Args:
            book_id: Book UUID.
            concept_name: Concept name.
            weight: Relationship weight.

        Returns:
            Created relationship properties.
        """
        result = self.client.create_relationship(
            from_label="Book",
            from_property="id",
            from_value=str(book_id),
            to_label="Concept",
            to_property="name",
            to_value=concept_name,
            relationship_type="HAS_CONCEPT",
            properties={"weight": weight},
        )
        self.logger.debug("Linked book %s to concept %s", book_id, concept_name)
        return result

    def link_book_to_author(
        self,
        book_id: Union[str, UUID],
        author_name: str,
    ) -> dict[str, Any]:
        """Create WRITTEN_BY relationship.

        Args:
            book_id: Book UUID.
            author_name: Author name.

        Returns:
            Created relationship properties.
        """
        result = self.client.create_relationship(
            from_label="Book",
            from_property="id",
            from_value=str(book_id),
            to_label="Author",
            to_property="name",
            to_value=author_name,
            relationship_type="WRITTEN_BY",
        )
        self.logger.debug("Linked book %s to author %s", book_id, author_name)
        return result

    def link_highlight_to_concept(
        self,
        highlight_id: Union[str, UUID],
        concept_name: str,
    ) -> dict[str, Any]:
        """Create RELATED_TO relationship from highlight to concept.

        Args:
            highlight_id: Highlight UUID.
            concept_name: Concept name.

        Returns:
            Created relationship properties.
        """
        result = self.client.create_relationship(
            from_label="Highlight",
            from_property="id",
            from_value=str(highlight_id),
            to_label="Concept",
            to_property="name",
            to_value=concept_name,
            relationship_type="RELATED_TO",
        )
        self.logger.debug("Linked highlight %s to concept %s", highlight_id, concept_name)
        return result

    def link_highlight_to_book(
        self,
        highlight_id: Union[str, UUID],
        book_id: Union[str, UUID],
    ) -> dict[str, Any]:
        """Create FROM_BOOK relationship.

        Args:
            highlight_id: Highlight UUID.
            book_id: Book UUID.

        Returns:
            Created relationship properties.
        """
        result = self.client.create_relationship(
            from_label="Highlight",
            from_property="id",
            from_value=str(highlight_id),
            to_label="Book",
            to_property="id",
            to_value=str(book_id),
            relationship_type="FROM_BOOK",
        )
        self.logger.debug("Linked highlight %s to book %s", highlight_id, book_id)
        return result

    # === Graph Queries ===

    def get_full_graph(
        self,
        limit: int = 100,
    ) -> tuple[list[GraphNode], list[GraphEdge]]:
        """Get full graph data for visualization.

        Args:
            limit: Maximum number of nodes to return.

        Returns:
            Tuple of (nodes, edges).
        """
        query = f"""
        MATCH (n)
        OPTIONAL MATCH (n)-[r]->(m)
        RETURN n, r, m
        LIMIT {limit}
        """

        results = self.client.execute_query(query)

        nodes_dict: dict[str, GraphNode] = {}
        edges: list[GraphEdge] = []

        for record in results:
            # Process source node
            n = record.get("n")
            if n:
                # Neo4j returns Node objects, convert to dict properly
                n_props = dict(n) if hasattr(n, 'keys') else n
                node_id = str(n_props.get("id", ""))
                labels = list(n.labels) if hasattr(n, 'labels') else n_props.get("labels", [])
                node_type = self._infer_node_type(labels, n_props)
                label = n_props.get("title") or n_props.get("name") or n_props.get("content", "")[:50]

                if node_id and node_id not in nodes_dict:
                    nodes_dict[node_id] = GraphNode(
                        id=node_id,
                        type=node_type,
                        label=label,
                        properties=n_props,
                    )

            # Process target node
            m = record.get("m")
            if m:
                # Neo4j returns Node objects, convert to dict properly
                m_props = dict(m) if hasattr(m, 'keys') else m
                node_id = str(m_props.get("id", ""))
                labels = list(m.labels) if hasattr(m, 'labels') else m_props.get("labels", [])
                node_type = self._infer_node_type(labels, m_props)
                label = m_props.get("title") or m_props.get("name") or m_props.get("content", "")[:50]

                if node_id and node_id not in nodes_dict:
                    nodes_dict[node_id] = GraphNode(
                        id=node_id,
                        type=node_type,
                        label=label,
                        properties=m_props,
                    )

            # Process relationship
            r = record.get("r")
            if r and n and m:
                r_props = dict(r) if hasattr(r, 'keys') else r
                n_props = dict(n) if hasattr(n, 'keys') else n
                m_props = dict(m) if hasattr(m, 'keys') else m
                edge_type = self._map_relationship_type(r_props.get("type", ""))
                edges.append(
                    GraphEdge(
                        source=str(n_props.get("id", "")),
                        target=str(m_props.get("id", "")),
                        type=edge_type,
                        properties=r_props,
                    )
                )

        return list(nodes_dict.values()), edges

    def get_book_graph(
        self,
        book_id: Union[str, UUID],
    ) -> tuple[list[GraphNode], list[GraphEdge]]:
        """Get graph for a specific book.

        Args:
            book_id: Book UUID.

        Returns:
            Tuple of (nodes, edges) for the book.
        """
        query = """
        MATCH (b:Book {id: $book_id})
        OPTIONAL MATCH (b)-[r1]-(related)
        OPTIONAL MATCH (highlight:Highlight)-[r2]-(b)
        OPTIONAL MATCH (highlight)-[r3]-(concept:Concept)
        RETURN b, r1, related, highlight, r2, concept, r3
        """

        results = self.client.execute_query(query, {"book_id": str(book_id)})

        # Similar processing as get_full_graph
        nodes_dict: dict[str, GraphNode] = {}
        edges: list[GraphEdge] = []

        for record in results:
            # Process all nodes
            for key in ["b", "related", "highlight", "concept"]:
                node = record.get(key)
                if node:
                    # Neo4j returns Node objects, convert to dict properly
                    node_props = dict(node) if hasattr(node, 'keys') else node
                    if isinstance(node_props, dict):
                        node_id = str(node_props.get("id", ""))
                        if node_id and node_id not in nodes_dict:
                            labels = list(node.labels) if hasattr(node, 'labels') else node_props.get("labels", [])
                            node_type = self._infer_node_type(labels, node_props)
                            label = node_props.get("title") or node_props.get("name") or node_props.get("content", "")[:50]

                            nodes_dict[node_id] = GraphNode(
                                id=node_id,
                                type=node_type,
                                label=label,
                                properties=node_props,
                            )

            # Process relationships
            for key in ["r1", "r2", "r3"]:
                rel = record.get(key)
                if rel:
                    rel_props = dict(rel) if hasattr(rel, 'keys') else rel
                    if isinstance(rel_props, dict):
                        edge_type = self._map_relationship_type(rel_props.get("type", ""))
                        edges.append(
                            GraphEdge(
                                source=str(record.get(key).start) if hasattr(record.get(key), 'start') else "",
                                target=str(record.get(key).end) if hasattr(record.get(key), 'end') else "",
                                type=edge_type,
                                properties=rel_props,
                            )
                        )

        return list(nodes_dict.values()), edges

    def get_concept_details(
        self,
        concept_name: str,
    ) -> dict[str, Any]:
        """Get concept details with related highlights and books.

        Args:
            concept_name: Concept name.

        Returns:
            Concept details including related items.
        """
        query = """
        MATCH (c:Concept {name: $name})
        OPTIONAL MATCH (c)<-[r1:HAS_CONCEPT]-(b:Book)
        OPTIONAL MATCH (c)<-[r2:RELATED_TO]-(h:Highlight)
        OPTIONAL MATCH (h)-[:FROM_BOOK]->(hb:Book)
        RETURN c, collect(DISTINCT b) as books, collect(DISTINCT h) as highlights
        """

        results = self.client.execute_query(query, {"name": concept_name})

        if not results:
            return {}

        record = results[0]
        concept = record.get("c", {})
        books = record.get("books", [])
        highlights = record.get("highlights", [])

        return {
            "concept": dict(concept) if concept else {},
            "books": [dict(b) for b in books if b],
            "highlights": [
                {
                    "id": h.get("id"),
                    "content": h.get("content", "")[:100],
                    "chapter": h.get("chapter"),
                }
                for h in highlights
                if h
            ],
            "book_count": len([b for b in books if b]),
            "highlight_count": len([h for h in highlights if h]),
        }

    def _infer_node_type(
        self,
        labels: list[str],
        properties: dict[str, Any],
    ) -> NodeType:
        """Infer node type from labels or properties.

        Args:
            labels: Node labels from Neo4j.
            properties: Node properties.

        Returns:
            Inferred NodeType.
        """
        if not labels:
            # Infer from properties
            if "title" in properties:
                return NodeType.BOOK
            if "content" in properties:
                return NodeType.HIGHLIGHT
            if "name" in properties and "bio" in properties:
                return NodeType.AUTHOR
            return NodeType.CONCEPT

        # Map label to type
        label_map = {
            "Book": NodeType.BOOK,
            "Concept": NodeType.CONCEPT,
            "Author": NodeType.AUTHOR,
            "Highlight": NodeType.HIGHLIGHT,
            "Reader": NodeType.READER,
        }

        for label in labels:
            if label in label_map:
                return label_map[label]

        return NodeType.CONCEPT

    def _map_relationship_type(self, rel_type: str) -> EdgeType:
        """Map Neo4j relationship type to EdgeType.

        Args:
            rel_type: Neo4j relationship type.

        Returns:
            Mapped EdgeType.
        """
        type_map = {
            "HAS_CONCEPT": EdgeType.HAS_CONCEPT,
            "LIKES": EdgeType.LIKES,
            "WRITTEN_BY": EdgeType.WRITTEN_BY,
            "RELATED_TO": EdgeType.RELATED_TO,
            "FROM_BOOK": EdgeType.FROM_BOOK,
        }

        return type_map.get(rel_type, EdgeType.HAS_CONCEPT)


# Singleton instance - lazily initialized to ensure neo4j_client is connected
global graph_service
_graph_service: Optional[GraphService] = None

def get_graph_service() -> GraphService:
    """Get or create graph service instance."""
    global _graph_service
    if _graph_service is None:
        _graph_service = GraphService()
    return _graph_service

# Backward compatibility
graph_service = get_graph_service()

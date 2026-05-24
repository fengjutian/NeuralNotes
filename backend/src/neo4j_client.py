"""Neo4j graph database client."""

from typing import Any, Optional
from contextlib import contextmanager

from neo4j import GraphDatabase, Driver, Session
from neo4j.exceptions import ServiceUnavailable, AuthError

from src.config import settings
from src.utils.exceptions import GraphConnectionException
from src.utils.logging import get_logger

logger = get_logger(__name__)


class Neo4jClient:
    """Neo4j database client for knowledge graph operations.

    Handles connection management, node/relationship creation,
    and graph queries for the cognitive reading graph.
    """

    def __init__(self) -> None:
        """Initialize Neo4j client with connection parameters."""
        self._driver: Optional[Driver] = None

    def connect(self) -> None:
        """Establish connection to Neo4j database.

        Raises:
            GraphConnectionException: If unable to connect.
        """
        try:
            self._driver = GraphDatabase.driver(
                settings.neo4j_uri,
                auth=(settings.neo4j_user, settings.neo4j_password),
            )
            # Verify connection
            self._driver.verify_connectivity()
            logger.info("Connected to Neo4j at %s", settings.neo4j_uri)
        except (ServiceUnavailable, AuthError) as e:
            logger.error("Failed to connect to Neo4j: %s", str(e))
            raise GraphConnectionException(settings.neo4j_uri) from e

    def disconnect(self) -> None:
        """Close connection to Neo4j database."""
        if self._driver:
            self._driver.close()
            self._driver = None
            logger.info("Disconnected from Neo4j")

    @contextmanager
    def session(self) -> Session:
        """Get a Neo4j session context manager.

        Yields:
            Neo4j session that is automatically closed after use.

        Raises:
            GraphConnectionException: If not connected.
        """
        if not self._driver:
            raise GraphConnectionException(settings.neo4j_uri)
        session = self._driver.session()
        try:
            yield session
        finally:
            session.close()

    def execute_query(
        self,
        query: str,
        parameters: Optional[dict[str, Any]] = None,
    ) -> list[dict[str, Any]]:
        """Execute a Cypher query and return results.

        Args:
            query: Cypher query string.
            parameters: Query parameters.

        Returns:
            List of result records as dictionaries.
        """
        with self.session() as session:
            result = session.run(query, parameters or {})
            return [record.data() for record in result]

    # Node Operations
    def create_node(
        self,
        label: str,
        properties: dict[str, Any],
    ) -> dict[str, Any]:
        """Create a node with the given label and properties.

        Args:
            label: Node label (e.g., 'Book', 'Concept').
            properties: Node properties.

        Returns:
            Created node properties including generated ID.
        """
        query = f"""
        CREATE (n:{label} $props)
        RETURN n
        """
        results = self.execute_query(query, {"props": properties})
        return results[0]["n"] if results else {}

    def get_node(
        self,
        label: str,
        property_name: str,
        property_value: Any,
    ) -> Optional[dict[str, Any]]:
        """Get a node by property value.

        Args:
            label: Node label.
            property_name: Property to search by.
            property_value: Value to match.

        Returns:
            Node properties or None if not found.
        """
        query = f"""
        MATCH (n:{label} {{{property_name}: $value}})
        RETURN n
        """
        results = self.execute_query(query, {"value": property_value})
        return results[0]["n"] if results else None

    # Relationship Operations
    def create_relationship(
        self,
        from_label: str,
        from_property: str,
        from_value: Any,
        to_label: str,
        to_property: str,
        to_value: Any,
        relationship_type: str,
        properties: Optional[dict[str, Any]] = None,
    ) -> dict[str, Any]:
        """Create a relationship between two nodes.

        Args:
            from_label: Source node label.
            from_property: Source property to match.
            from_value: Source property value.
            to_label: Target node label.
            to_property: Target property to match.
            to_value: Target property value.
            relationship_type: Relationship type (e.g., 'HAS_CONCEPT').
            properties: Optional relationship properties.

        Returns:
            Created relationship properties.
        """
        query = f"""
        MATCH (a:{from_label} {{{from_property}: $from_value}})
        MATCH (b:{to_label} {{{to_property}: $to_value}})
        CREATE (a)-[r:{relationship_type} $props]->(b)
        RETURN r
        """
        results = self.execute_query(
            query,
            {
                "from_value": from_value,
                "to_value": to_value,
                "props": properties or {},
            },
        )
        return results[0]["r"] if results else {}

    # Graph Statistics
    def get_graph_stats(self) -> dict[str, int]:
        """Get statistics about the graph.

        Returns:
            Dictionary with counts of nodes and relationships.
        """
        query = """
        MATCH (n)
        OPTIONAL MATCH ()-[r]->()
        RETURN count(DISTINCT n) as node_count,
               count(DISTINCT r) as relationship_count
        """
        results = self.execute_query(query)
        if results:
            return {
                "node_count": results[0].get("node_count", 0),
                "relationship_count": results[0].get("relationship_count", 0),
            }
        return {"node_count": 0, "relationship_count": 0}

    def clear_graph(self) -> None:
        """Delete all nodes and relationships (use with caution!)."""
        query = """
        MATCH (n)
        DETACH DELETE n
        """
        self.execute_query(query)
        logger.warning("Cleared all nodes and relationships from graph")


# Global client instance
neo4j_client = Neo4jClient()


def get_neo4j() -> Neo4jClient:
    """Get Neo4j client instance for dependency injection.

    Returns:
        Neo4jClient instance.
    """
    return neo4j_client

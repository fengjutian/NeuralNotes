"""Knowledge Graph API endpoints."""

from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.graph import GraphResponse
from src.services.graph_service import graph_service
from src.services.book_service import book_service
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.get("/", response_model=GraphResponse)
async def get_graph(
    book_id: Optional[UUID] = Query(default=None, description="Filter by book ID"),
    concept_id: Optional[UUID] = Query(default=None, description="Filter by concept ID"),
    limit: int = Query(default=100, ge=1, le=1000, description="Max nodes to return"),
) -> GraphResponse:
    """Get knowledge graph data.

    Args:
        book_id: Optional book ID to filter graph.
        concept_id: Optional concept ID to center graph.
        limit: Maximum number of nodes to return.

    Returns:
        Graph data with nodes and edges.
    """
    logger.info("Get graph: book_id=%s, concept_id=%s, limit=%d", book_id, concept_id, limit)
    
    # Get graph data
    if book_id:
        nodes, edges = graph_service.get_book_graph(book_id)
    else:
        nodes, edges = graph_service.get_full_graph(limit=limit)
    
    return GraphResponse(
        nodes=nodes[:limit],
        edges=edges,
        total_nodes=len(nodes),
        total_edges=len(edges),
    )


@router.get("/stats")
async def get_graph_stats(
    db: Session = Depends(get_db),
) -> dict:
    """Get graph statistics.

    Returns:
        Graph statistics including node and edge counts.
    """
    logger.info("Get graph stats")
    
    # Get stats from database
    books, total_books = book_service.get_all(db, skip=0, limit=1)
    
    # Get highlight count
    from src.models.highlight import Highlight
    from sqlalchemy import select, func
    highlight_count = db.execute(select(func.count(Highlight.id))).scalar_one()
    
    # Get concept count from graph
    try:
        concept_query = "MATCH (c:Concept) RETURN count(c) as count"
        concept_result = graph_service.client.execute_query(concept_query)
        concept_count = concept_result[0]["count"] if concept_result else 0
    except Exception:
        concept_count = 0
    
    # Get relationship count
    try:
        rel_query = "MATCH ()-[r]->() RETURN count(r) as count"
        rel_result = graph_service.client.execute_query(rel_query)
        relationship_count = rel_result[0]["count"] if rel_result else 0
    except Exception:
        relationship_count = 0
    
    return {
        "node_count": concept_count + total_books + highlight_count,
        "relationship_count": relationship_count,
        "book_count": total_books,
        "concept_count": concept_count,
        "highlight_count": highlight_count,
    }


@router.get("/concept/{concept_name}")
async def get_concept_details(
    concept_name: str,
) -> dict:
    """Get concept details with related highlights and books.

    Args:
        concept_name: Name of the concept.

    Returns:
        Concept details including related items.
    """
    logger.info("Get concept details: %s", concept_name)
    
    return graph_service.get_concept_details(concept_name)


@router.get("/debug")
async def debug_graph(
    db: Session = Depends(get_db),
) -> dict:
    """Debug endpoint to check Neo4j connection and data.

    Returns:
        Debug information about the graph database.
    """
    logger.info("Debug graph endpoint called")
    
    # Test Neo4j connection
    neo4j_status = "unknown"
    neo4j_error = None
    try:
        graph_service.client.connect()
        test_query = "RETURN 1 as test"
        result = graph_service.client.execute_query(test_query)
        neo4j_status = "connected" if result else "no_data"
    except Exception as e:
        neo4j_status = "error"
        neo4j_error = str(e)
        logger.error("Neo4j connection error: %s", neo4j_error)
    
    # Get actual node counts
    node_counts = {}
    for label in ["Book", "Concept", "Author", "Highlight"]:
        try:
            query = f"MATCH (n:{label}) RETURN count(n) as count"
            result = graph_service.client.execute_query(query)
            node_counts[label] = result[0]["count"] if result else 0
        except Exception:
            node_counts[label] = -1
    
    # Get relationship count
    try:
        rel_query = "MATCH ()-[r]->() RETURN count(r) as count"
        rel_result = graph_service.client.execute_query(rel_query)
        rel_count = rel_result[0]["count"] if rel_result else 0
    except Exception:
        rel_count = -1
    
    return {
        "neo4j_status": neo4j_status,
        "neo4j_error": neo4j_error,
        "node_counts": node_counts,
        "relationship_count": rel_count,
    }

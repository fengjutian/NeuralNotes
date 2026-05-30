"""MySQL-based Graph API for when Neo4j is not available."""

from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select, func

from src.database import get_db
from src.models.book import Book
from src.models.highlight import Highlight
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


async def get_mysql_graph_data(db: Session) -> dict:
    """Get graph data from MySQL (reusable function for fallback).

    Args:
        db: Database session.

    Returns:
        Graph data with nodes and edges from MySQL.
    """
    logger.info("Getting graph data from MySQL")
    
    # Get all books
    books_query = select(Book)
    books = db.execute(books_query).scalars().all()
    
    # Get all highlights with book info
    highlights_query = select(Highlight)
    highlights = db.execute(highlights_query).scalars().all()
    
    nodes = []
    edges = []
    concepts = set()
    
    # Add book nodes
    for book in books:
        nodes.append({
            "id": str(book.id),
            "type": "book",
            "label": book.title,
            "properties": {
                "title": book.title,
                "author": book.author,
                "category": book.category,
            }
        })
        
        # Link book to author
        if book.author:
            author_id = f"author_{book.author}"
            if not any(n["id"] == author_id for n in nodes):
                nodes.append({
                    "id": author_id,
                    "type": "author",
                    "label": book.author,
                    "properties": {"name": book.author}
                })
            edges.append({
                "source": str(book.id),
                "target": author_id,
                "type": "written_by"
            })
    
    # Add highlight nodes and extract concepts
    for highlight in highlights:
        nodes.append({
            "id": str(highlight.id),
            "type": "highlight",
            "label": highlight.content[:50] + "..." if len(highlight.content) > 50 else highlight.content,
            "properties": {
                "content": highlight.content,
                "chapter": highlight.chapter,
            }
        })
        
        # Link highlight to book
        edges.append({
            "source": str(highlight.id),
            "target": str(highlight.book_id),
            "type": "from_book"
        })
        
        # Extract and add concepts
        if highlight.concepts:
            concepts_list = highlight.concepts if isinstance(highlight.concepts, list) else []
            for concept in concepts_list:
                if concept:
                    concepts.add(concept)
                    concept_id = f"concept_{concept}"
                    
                    if not any(n["id"] == concept_id for n in nodes):
                        nodes.append({
                            "id": concept_id,
                            "type": "concept",
                            "label": concept,
                            "properties": {"name": concept, "frequency": 0}
                        })
                    
                    # Link highlight to concept
                    edges.append({
                        "source": str(highlight.id),
                        "target": concept_id,
                        "type": "related_to"
                    })
                    
                    # Link book to concept
                    edges.append({
                        "source": str(highlight.book_id),
                        "target": concept_id,
                        "type": "has_concept"
                    })
    
    logger.info(
        "MySQL graph: %d nodes, %d edges, %d concepts",
        len(nodes), len(edges), len(concepts)
    )
    
    return {
        "nodes": nodes,
        "edges": edges,
        "total_nodes": len(nodes),
        "total_edges": len(edges),
        "source": "mysql",
    }


@router.get("/")
async def get_mysql_graph(
    db: Session = Depends(get_db),
) -> dict:
    """Get graph data from MySQL (fallback when Neo4j unavailable).

    Returns:
        Graph data with nodes and edges from MySQL.
    """
    return await get_mysql_graph_data(db)


@router.get("/stats")
async def get_mysql_graph_stats(
    db: Session = Depends(get_db),
) -> dict:
    """Get graph statistics from MySQL.

    Returns:
        Statistics about books, highlights, and concepts.
    """
    book_count = db.execute(select(func.count(Book.id))).scalar_one()
    highlight_count = db.execute(select(func.count(Highlight.id))).scalar_one()
    
    # Count unique concepts
    concept_query = select(Highlight.concepts)
    all_highlights = db.execute(concept_query).scalars().all()
    all_concepts = set()
    for h in all_highlights:
        if h:
            concepts = h if isinstance(h, list) else []
            all_concepts.update(concepts)
    
    return {
        "book_count": book_count,
        "highlight_count": highlight_count,
        "concept_count": len(all_concepts),
        "source": "mysql",
    }


@router.get("/debug")
async def debug_mysql_graph(
    db: Session = Depends(get_db),
) -> dict:
    """Debug endpoint for MySQL graph.

    Returns:
        Debug information about MySQL data.
    """
    book_count = db.execute(select(func.count(Book.id))).scalar_one()
    highlight_count = db.execute(select(func.count(Highlight.id))).scalar_one()
    
    return {
        "mysql_status": "connected",
        "book_count": book_count,
        "highlight_count": highlight_count,
    }
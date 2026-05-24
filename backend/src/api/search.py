"""Semantic Search API endpoints."""

from typing import Optional

from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.services.vector_service import vector_service
from src.services.book_service import book_service
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.get("/")
async def semantic_search(
    q: str = Query(..., min_length=1, description="Search query"),
    limit: int = Query(default=10, ge=1, le=100, description="Max results"),
    book_id: Optional[str] = Query(default=None, description="Filter by book ID"),
    min_score: float = Query(default=0.0, ge=0, le=1, description="Minimum relevance score"),
) -> dict:
    """Perform semantic search across highlights.

    Args:
        q: Search query string.
        limit: Maximum number of results.
        book_id: Optional book ID filter.
        min_score: Minimum relevance score threshold.

    Returns:
        Search results with relevance scores.
    """
    logger.info("Semantic search: '%s', limit=%d", q, limit)
    
    try:
        results = vector_service.search(
            query=q,
            limit=limit,
            book_id=book_id,
            score_threshold=min_score,
        )
        
        return {
            "query": q,
            "results": results,
            "total": len(results),
            "book_id": book_id,
            "min_score": min_score,
        }
    except Exception as e:
        logger.error("Search failed: %s", str(e))
        return {
            "query": q,
            "results": [],
            "total": 0,
            "error": str(e),
        }


@router.post("/aggregate")
async def aggregate_thoughts(
    topic: str,
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
) -> dict:
    """Aggregate thoughts on a specific topic.

    Args:
        topic: Topic to aggregate thoughts about.
        limit: Maximum number of related highlights.
        db: Database session.

    Returns:
        Aggregated thoughts and insights.
    """
    logger.info("Aggregate thoughts on: %s", topic)
    
    # Search for related highlights
    results = vector_service.search(query=topic, limit=limit)
    
    # Extract unique concepts from results
    concepts = set()
    for r in results:
        if r.get("payload", {}).get("concepts"):
            concepts.update(r["payload"]["concepts"])
    
    # Get book information
    book_ids = set(r.get("book_id") for r in results if r.get("book_id"))
    books = {}
    for bid in book_ids:
        try:
            from uuid import UUID
            book = book_service.get_by_id(db, UUID(bid))
            if book:
                books[bid] = {
                    "title": book.title,
                    "author": book.author,
                }
        except Exception:
            pass
    
    # Generate summary from content
    contents = [r.get("content", "") for r in results]
    summary = f"Found {len(results)} highlights related to '{topic}'"
    
    return {
        "topic": topic,
        "summary": summary,
        "highlight_count": len(results),
        "related_highlights": [
            {
                "id": r["id"],
                "content": r.get("content", "")[:200],
                "score": r.get("score", 0),
                "book": books.get(r.get("book_id"), {}),
            }
            for r in results
        ],
        "concepts": list(concepts),
        "book_count": len(books),
    }


@router.post("/index")
async def index_highlights(
    book_id: str = Query(..., description="Book ID to index"),
    db: Session = Depends(get_db),
) -> dict:
    """Index all highlights for a book for semantic search.

    Args:
        book_id: Book ID to index highlights for.
        db: Database session.

    Returns:
        Indexing results.
    """
    logger.info("Indexing highlights for book: %s", book_id)
    
    from uuid import UUID
    highlights = db.query("Highlight").filter("book_id = :book_id", book_id=book_id).all()
    
    # Index each highlight
    highlights_data = []
    for h in highlights:
        highlights_data.append({
            "id": str(h.id),
            "content": h.content,
            "book_id": str(h.book_id),
            "chapter": h.chapter,
            "metadata": {
                "emotion": h.emotion,
                "domain": h.domain,
            } if hasattr(h, 'emotion') else None,
        })
    
    count = vector_service.index_batch(highlights_data)
    
    return {
        "status": "completed",
        "book_id": book_id,
        "indexed_count": count,
    }

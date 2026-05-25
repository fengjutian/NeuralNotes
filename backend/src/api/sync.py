"""Data synchronization API for syncing MySQL data to Neo4j."""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.services.book_service import book_service
from src.services.highlight_service import highlight_service
from src.services.graph_service import graph_service
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.post("/books/{book_id}")
async def sync_book_to_graph(
    book_id: UUID,
    db: Session = Depends(get_db),
) -> dict:
    """Sync a single book and its highlights to Neo4j.

    Args:
        book_id: Book UUID to sync.
        db: Database session.

    Returns:
        Sync result with node and relationship counts.
    """
    logger.info("Syncing book %s to graph", book_id)
    
    # Get book from MySQL
    book = book_service.get_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    try:
        # Create book node
        graph_service.create_book_node(
            book_id=book.id,
            title=book.title,
            author=book.author,
            category=book.category,
        )
        
        # Create author node and link
        if book.author:
            graph_service.create_author_node(name=book.author)
            graph_service.link_book_to_author(
                book_id=book.id,
                author_name=book.author,
            )
        
        # Sync highlights
        highlights = highlight_service.get_by_book(db, book.id)
        highlight_count = 0
        concept_count = 0
        
        for highlight in highlights:
            # Create highlight node
            graph_service.create_highlight_node(
                highlight_id=highlight.id,
                content=highlight.content,
                chapter=highlight.chapter,
            )
            
            # Link highlight to book
            graph_service.link_highlight_to_book(
                highlight_id=highlight.id,
                book_id=book.id,
            )
            
            # Create concept nodes and link if concepts exist
            if highlight.concepts:
                concepts = highlight.concepts if isinstance(highlight.concepts, list) else []
                for concept_name in concepts:
                    if concept_name:
                        graph_service.create_concept_node(
                            concept_id=str(highlight.id) + "_" + concept_name,
                            name=concept_name,
                        )
                        graph_service.link_highlight_to_concept(
                            highlight_id=highlight.id,
                            concept_name=concept_name,
                        )
                        graph_service.link_book_to_concept(
                            book_id=book.id,
                            concept_name=concept_name,
                        )
                        concept_count += 1
            
            highlight_count += 1
        
        logger.info(
            "Synced book %s: %d highlights, %d concepts",
            book.title, highlight_count, concept_count
        )
        
        return {
            "status": "success",
            "book_id": str(book_id),
            "book_title": book.title,
            "nodes_created": 1 + highlight_count + concept_count,
            "relationships_created": highlight_count * 2 + concept_count + (1 if book.author else 0),
        }
        
    except Exception as e:
        logger.error("Sync failed: %s", str(e))
        raise HTTPException(status_code=500, detail=f"Sync failed: {str(e)}")


@router.post("/all")
async def sync_all_to_graph(
    db: Session = Depends(get_db),
) -> dict:
    """Sync all books and highlights to Neo4j.

    Args:
        db: Database session.

    Returns:
        Sync summary with totals.
    """
    logger.info("Starting full graph sync")
    
    books, total = book_service.get_all(db, skip=0, limit=1000)
    
    total_nodes = 0
    total_relationships = 0
    synced_books = 0
    errors = []
    
    for book in books:
        try:
            # Create book node
            graph_service.create_book_node(
                book_id=book.id,
                title=book.title,
                author=book.author,
                category=book.category,
            )
            
            # Create author node
            if book.author:
                graph_service.create_author_node(name=book.author)
                graph_service.link_book_to_author(
                    book_id=book.id,
                    author_name=book.author,
                )
                total_relationships += 1
            
            total_nodes += 1
            
            # Sync highlights
            highlights = highlight_service.get_by_book(db, book.id)
            for highlight in highlights:
                graph_service.create_highlight_node(
                    highlight_id=highlight.id,
                    content=highlight.content,
                    chapter=highlight.chapter,
                )
                graph_service.link_highlight_to_book(
                    highlight_id=highlight.id,
                    book_id=book.id,
                )
                
                total_nodes += 1
                total_relationships += 1
                
                # Sync concepts
                if highlight.concepts:
                    concepts = highlight.concepts if isinstance(highlight.concepts, list) else []
                    for concept_name in concepts:
                        if concept_name:
                            graph_service.create_concept_node(
                                concept_id=str(highlight.id) + "_" + concept_name,
                                name=concept_name,
                            )
                            graph_service.link_highlight_to_concept(
                                highlight_id=highlight.id,
                                concept_name=concept_name,
                            )
                            graph_service.link_book_to_concept(
                                book_id=book.id,
                                concept_name=concept_name,
                            )
                            
                            total_nodes += 1
                            total_relationships += 2
            
            synced_books += 1
            
        except Exception as e:
            errors.append({"book_id": str(book.id), "error": str(e)})
            logger.error("Failed to sync book %s: %s", book.id, str(e))
    
    logger.info(
        "Full sync complete: %d books, %d nodes, %d relationships, %d errors",
        synced_books, total_nodes, total_relationships, len(errors)
    )
    
    return {
        "status": "completed",
        "total_books": total,
        "synced_books": synced_books,
        "total_nodes": total_nodes,
        "total_relationships": total_relationships,
        "errors": errors if errors else None,
    }


@router.delete("/all")
async def clear_graph(db: Session = Depends(get_db)) -> dict:
    """Clear all data from Neo4j graph.

    Args:
        db: Database session.

    Returns:
        Confirmation message.
    """
    logger.warning("Clearing all graph data from Neo4j")
    
    try:
        graph_service.client.clear_graph()
        return {"status": "success", "message": "All graph data cleared"}
    except Exception as e:
        logger.error("Failed to clear graph: %s", str(e))
        raise HTTPException(status_code=500, detail=str(e))
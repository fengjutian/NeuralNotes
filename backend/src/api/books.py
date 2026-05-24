"""Books API endpoints."""

from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas import BookListResponse, BookResponse
from src.schemas.book import BookCreate
from src.services.book_service import book_service
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.get("/", response_model=BookListResponse)
async def list_books(
    page: int = Query(default=1, ge=1, description="Page number"),
    page_size: int = Query(default=20, ge=1, le=100, description="Items per page"),
    category: Optional[str] = Query(default=None, description="Filter by category"),
    db: Session = Depends(get_db),
) -> BookListResponse:
    """List all books with pagination.

    Args:
        page: Page number (starting from 1).
        page_size: Number of items per page.
        category: Optional category filter.
        db: Database session.

    Returns:
        Paginated list of books.
    """
    logger.info("List books: page=%d, page_size=%d, category=%s", page, page_size, category)
    
    # Calculate offset
    skip = (page - 1) * page_size
    
    # Get books from service
    books, total = book_service.get_all(db, skip=skip, limit=page_size, category=category)
    
    # Convert to response format
    items = []
    for book in books:
        item = BookResponse.model_validate(book)
        item.highlight_count = len(book.highlights) if book.highlights else 0
        items.append(item)
    
    return BookListResponse(
        items=items,
        total=total,
        page=page,
        page_size=page_size,
    )


@router.get("/{book_id}", response_model=BookResponse)
async def get_book(
    book_id: UUID,
    db: Session = Depends(get_db),
) -> BookResponse:
    """Get a specific book by ID.

    Args:
        book_id: Book UUID.
        db: Database session.

    Returns:
        Book details.
    """
    logger.info("Get book: %s", book_id)
    
    book = book_service.get_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book not found: {book_id}")
    
    response = BookResponse.model_validate(book)
    response.highlight_count = len(book.highlights) if book.highlights else 0
    return response


@router.post("/", response_model=BookResponse, status_code=201)
async def create_book(
    book_data: BookCreate,
    db: Session = Depends(get_db),
) -> BookResponse:
    """Create a new book.

    Args:
        book_data: Book creation data.
        db: Database session.

    Returns:
        Created book details.
    """
    logger.info("Create book: %s", book_data.title)
    
    book = book_service.create(db, book_data)
    response = BookResponse.model_validate(book)
    response.highlight_count = 0
    return response


@router.delete("/{book_id}", status_code=204)
async def delete_book(
    book_id: UUID,
    db: Session = Depends(get_db),
) -> None:
    """Delete a book.

    Args:
        book_id: Book UUID.
        db: Database session.
    """
    logger.info("Delete book: %s", book_id)
    
    deleted = book_service.delete(db, book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Book not found: {book_id}")

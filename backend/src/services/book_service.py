"""Book service for database CRUD operations."""

from typing import Optional
from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from src.models.book import Book
from src.schemas.book import BookCreate, BookUpdate
from src.utils.logging import get_logger

logger = get_logger(__name__)


class BookService:
    """Service for Book database operations."""

    @staticmethod
    def create(db: Session, book_data: BookCreate) -> Book:
        """Create a new book.

        Args:
            db: Database session.
            book_data: Book creation data.

        Returns:
            Created book instance.
        """
        logger.info("Creating book: %s", book_data.title)
        book = Book(
            title=book_data.title,
            author=book_data.author,
            category=book_data.category,
            isbn=book_data.isbn,
            reading_time=book_data.reading_time,
            progress=book_data.progress,
            reading_date=book_data.reading_date,
        )
        db.add(book)
        db.commit()
        db.refresh(book)
        logger.info("Book created: %s", book.id)
        return book

    @staticmethod
    def get_by_id(db: Session, book_id: UUID) -> Optional[Book]:
        """Get a book by ID.

        Args:
            db: Database session.
            book_id: Book UUID.

        Returns:
            Book instance or None.
        """
        logger.info("Getting book: %s", book_id)
        result = db.execute(select(Book).where(Book.id == book_id))
        return result.scalar_one_or_none()

    @staticmethod
    def get_all(
        db: Session,
        skip: int = 0,
        limit: int = 20,
        category: Optional[str] = None,
    ) -> tuple[list[Book], int]:
        """Get all books with pagination and optional filtering.

        Args:
            db: Database session.
            skip: Number of records to skip.
            limit: Maximum number of records to return.
            category: Optional category filter.

        Returns:
            Tuple of (books list, total count).
        """
        logger.info("Getting all books: skip=%d, limit=%d, category=%s", skip, limit, category)
        
        # Base query
        query = select(Book)
        count_query = select(func.count(Book.id))
        
        # Apply category filter
        if category:
            query = query.where(Book.category == category)
            count_query = count_query.where(Book.category == category)
        
        # Get total count
        total = db.execute(count_query).scalar_one()
        
        # Get paginated results
        query = query.offset(skip).limit(limit)
        result = db.execute(query)
        books = list(result.scalars().all())
        
        logger.info("Found %d books (total: %d)", len(books), total)
        return books, total

    @staticmethod
    def update(db: Session, book_id: UUID, book_data: BookUpdate) -> Optional[Book]:
        """Update a book.

        Args:
            db: Database session.
            book_id: Book UUID.
            book_data: Book update data.

        Returns:
            Updated book instance or None.
        """
        logger.info("Updating book: %s", book_id)
        book = BookService.get_by_id(db, book_id)
        if not book:
            logger.warning("Book not found for update: %s", book_id)
            return None
        
        # Update fields
        update_data = book_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(book, field, value)
        
        db.commit()
        db.refresh(book)
        logger.info("Book updated: %s", book_id)
        return book

    @staticmethod
    def delete(db: Session, book_id: UUID) -> bool:
        """Delete a book.

        Args:
            db: Database session.
            book_id: Book UUID.

        Returns:
            True if deleted, False if not found.
        """
        logger.info("Deleting book: %s", book_id)
        book = BookService.get_by_id(db, book_id)
        if not book:
            logger.warning("Book not found for deletion: %s", book_id)
            return False
        
        db.delete(book)
        db.commit()
        logger.info("Book deleted: %s", book_id)
        return True


# Singleton instance
book_service = BookService()
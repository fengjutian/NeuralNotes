"""Highlight service for database CRUD operations."""

from typing import Optional
from uuid import UUID

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from src.models.highlight import Highlight
from src.schemas.highlight import HighlightCreate, HighlightUpdate
from src.utils.logging import get_logger

logger = get_logger(__name__)


class HighlightService:
    """Service for Highlight database operations."""

    @staticmethod
    def create(db: Session, highlight_data: HighlightCreate) -> Highlight:
        """Create a new highlight.

        Args:
            db: Database session.
            highlight_data: Highlight creation data.

        Returns:
            Created highlight instance.
        """
        logger.info("Creating highlight for book: %s", highlight_data.book_id)
        highlight = Highlight(
            book_id=highlight_data.book_id,
            content=highlight_data.content,
            chapter=highlight_data.chapter,
            create_time=highlight_data.create_time,
            url=highlight_data.url,
        )
        db.add(highlight)
        db.commit()
        db.refresh(highlight)
        logger.info("Highlight created: %s", highlight.id)
        return highlight

    @staticmethod
    def get_by_id(db: Session, highlight_id: UUID) -> Optional[Highlight]:
        """Get a highlight by ID.

        Args:
            db: Database session.
            highlight_id: Highlight UUID.

        Returns:
            Highlight instance or None.
        """
        logger.info("Getting highlight: %s", highlight_id)
        result = db.execute(select(Highlight).where(Highlight.id == highlight_id))
        return result.scalar_one_or_none()

    @staticmethod
    def get_by_book(
        db: Session,
        book_id: UUID,
        skip: int = 0,
        limit: int = 100,
    ) -> tuple[list[Highlight], int]:
        """Get all highlights for a book.

        Args:
            db: Database session.
            book_id: Book UUID.
            skip: Number of records to skip.
            limit: Maximum number of records to return.

        Returns:
            Tuple of (highlights list, total count).
        """
        logger.info("Getting highlights for book: %s", book_id)
        
        # Get total count
        count_query = select(func.count(Highlight.id)).where(Highlight.book_id == book_id)
        total = db.execute(count_query).scalar_one()
        
        # Get paginated results
        query = (
            select(Highlight)
            .where(Highlight.book_id == book_id)
            .offset(skip)
            .limit(limit)
        )
        result = db.execute(query)
        highlights = list(result.scalars().all())
        
        logger.info("Found %d highlights (total: %d)", len(highlights), total)
        return highlights, total

    @staticmethod
    def get_unanalyzed(db: Session, book_id: Optional[UUID] = None) -> list[Highlight]:
        """Get highlights that haven't been analyzed yet.

        Args:
            db: Database session.
            book_id: Optional book UUID to filter by.

        Returns:
            List of unanalyzed highlights.
        """
        logger.info("Getting unanalyzed highlights")
        query = select(Highlight).where(Highlight.concepts.is_(None))
        if book_id:
            query = query.where(Highlight.book_id == book_id)
        result = db.execute(query)
        highlights = list(result.scalars().all())
        logger.info("Found %d unanalyzed highlights", len(highlights))
        return highlights

    @staticmethod
    def update(db: Session, highlight_id: UUID, highlight_data: HighlightUpdate) -> Optional[Highlight]:
        """Update a highlight.

        Args:
            db: Database session.
            highlight_id: Highlight UUID.
            highlight_data: Highlight update data.

        Returns:
            Updated highlight instance or None.
        """
        logger.info("Updating highlight: %s", highlight_id)
        highlight = HighlightService.get_by_id(db, highlight_id)
        if not highlight:
            logger.warning("Highlight not found for update: %s", highlight_id)
            return None
        
        # Update fields
        update_data = highlight_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(highlight, field, value)
        
        db.commit()
        db.refresh(highlight)
        logger.info("Highlight updated: %s", highlight_id)
        return highlight

    @staticmethod
    def delete(db: Session, highlight_id: UUID) -> bool:
        """Delete a highlight.

        Args:
            db: Database session.
            highlight_id: Highlight UUID.

        Returns:
            True if deleted, False if not found.
        """
        logger.info("Deleting highlight: %s", highlight_id)
        highlight = HighlightService.get_by_id(db, highlight_id)
        if not highlight:
            logger.warning("Highlight not found for deletion: %s", highlight_id)
            return False
        
        db.delete(highlight)
        db.commit()
        logger.info("Highlight deleted: %s", highlight_id)
        return True


# Singleton instance
highlight_service = HighlightService()
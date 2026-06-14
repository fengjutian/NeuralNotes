"""Tests for HighlightService -- database CRUD operations."""

import pytest
from sqlalchemy.orm import Session

from src.services.highlight_service import HighlightService
from src.models.book import Book
from src.models.highlight import Highlight
from src.schemas.highlight import HighlightCreate, HighlightUpdate


class TestHighlightService:
    """Test suite for HighlightService."""

    def test_create_highlight(self, db_session: Session):
        """Creating a highlight stores it in the database."""
        # First create a book
        book = Book(title="Test Book", author="Test Author")
        db_session.add(book)
        db_session.commit()

        data = HighlightCreate(
            book_id=str(book.id),
            content="This is a test highlight",
            chapter="Chapter 1",
        )
        highlight = HighlightService.create(db_session, data)
        assert highlight.id is not None
        assert highlight.content == "This is a test highlight"
        assert highlight.chapter == "Chapter 1"

    def test_get_by_id(self, db_session: Session):
        """Can retrieve a highlight by its ID."""
        book = Book(title="Test Book", author="Test Author")
        db_session.add(book)
        db_session.commit()

        data = HighlightCreate(book_id=str(book.id), content="Content here")
        created = HighlightService.create(db_session, data)

        retrieved = HighlightService.get_by_id(db_session, created.id)
        assert retrieved is not None
        assert retrieved.id == created.id
        assert retrieved.content == "Content here"

    def test_get_by_id_not_found(self, db_session: Session):
        """Returns None for non-existent highlight."""
        result = HighlightService.get_by_id(db_session, "00000000-0000-0000-0000-000000000000")
        assert result is None

    def test_get_by_book(self, db_session: Session):
        """Retrieves all highlights for a specific book."""
        book = Book(title="Test Book", author="Test Author")
        db_session.add(book)
        db_session.commit()

        for i in range(3):
            HighlightService.create(db_session, HighlightCreate(
                book_id=str(book.id), content=f"Highlight {i}"
            ))

        highlights, total = HighlightService.get_by_book(db_session, book.id)
        assert total == 3
        assert len(highlights) == 3

    def test_get_by_book_pagination(self, db_session: Session):
        """Respects skip and limit parameters."""
        book = Book(title="Test Book", author="Test Author")
        db_session.add(book)
        db_session.commit()

        for i in range(5):
            HighlightService.create(db_session, HighlightCreate(
                book_id=str(book.id), content=f"Highlight {i}"
            ))

        highlights, total = HighlightService.get_by_book(
            db_session, book.id, skip=2, limit=2
        )
        assert total == 5
        assert len(highlights) == 2

    def test_get_unanalyzed(self, db_session: Session):
        """Returns highlights without concepts set."""
        book = Book(title="Test Book", author="Test Author")
        db_session.add(book)
        db_session.commit()

        data = HighlightCreate(book_id=str(book.id), content="Unanalyzed")
        HighlightService.create(db_session, data)

        unanalyzed = HighlightService.get_unanalyzed(db_session, book.id)
        assert len(unanalyzed) == 1

    def test_update_highlight(self, db_session: Session):
        """Updating a highlight persists changes."""
        book = Book(title="Test Book", author="Test Author")
        db_session.add(book)
        db_session.commit()

        data = HighlightCreate(book_id=str(book.id), content="Original")
        created = HighlightService.create(db_session, data)

        update = HighlightUpdate(
            emotion="agreement",
            domain="psychology",
            concepts=["concept1", "concept2"],
        )
        updated = HighlightService.update(db_session, created.id, update)
        assert updated is not None
        assert updated.emotion == "agreement"
        assert updated.domain == "psychology"
        assert updated.concepts == ["concept1", "concept2"]

    def test_delete_highlight(self, db_session: Session):
        """Deleting a highlight removes it from the database."""
        book = Book(title="Test Book", author="Test Author")
        db_session.add(book)
        db_session.commit()

        data = HighlightCreate(book_id=str(book.id), content="Will be deleted")
        created = HighlightService.create(db_session, data)

        assert HighlightService.delete(db_session, created.id) is True
        assert HighlightService.get_by_id(db_session, created.id) is None

    def test_delete_not_found(self, db_session: Session):
        """Deleting a non-existent highlight returns False."""
        result = HighlightService.delete(
            db_session, "00000000-0000-0000-0000-000000000000"
        )
        assert result is False

    def test_cascade_delete_with_book(self, db_session: Session):
        """Deleting a book should cascade-delete its highlights."""
        book = Book(title="Test Book", author="Test Author")
        db_session.add(book)
        db_session.commit()

        HighlightService.create(db_session, HighlightCreate(
            book_id=str(book.id), content="Highlight 1"
        ))

        # Delete book
        db_session.delete(book)
        db_session.commit()

        # Highlights should be gone
        highlights, total = HighlightService.get_by_book(db_session, book.id)
        assert total == 0

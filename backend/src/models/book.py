"""Book model for storing book metadata."""

import uuid
from datetime import date, datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import String, Text, Date, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import Base

if TYPE_CHECKING:
    from src.models.highlight import Highlight
    from src.models.chapter import Chapter


class Book(Base):
    """Book entity representing a book with reading data."""

    __tablename__ = "books"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    isbn: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    reading_time: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    progress: Mapped[Optional[float]] = mapped_column(nullable=True)
    reading_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    created_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
    )

    # Relationships
    highlights: Mapped[list["Highlight"]] = relationship(
        "Highlight",
        back_populates="book",
        cascade="all, delete-orphan",
    )
    chapters: Mapped[list["Chapter"]] = relationship(
        "Chapter",
        back_populates="book",
        cascade="all, delete-orphan",
    )

    def __repr__(self) -> str:
        return f"<Book(id={self.id}, title={self.title!r})>"

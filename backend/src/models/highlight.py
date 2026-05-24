"""Highlight model for storing reading highlights/notes."""

import uuid
from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import String, Text, DateTime, ForeignKey, JSON, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import Base

if TYPE_CHECKING:
    from src.models.book import Book


class Highlight(Base):
    """Highlight entity representing a reading highlight/note."""

    __tablename__ = "highlights"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )
    book_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("books.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    content: Mapped[str] = mapped_column(Text, nullable=False)
    chapter: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    create_time: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        nullable=True,
    )
    url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    concepts: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    emotion: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    domain: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    created_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        server_default=func.now(),
    )

    # Relationships
    book: Mapped["Book"] = relationship("Book", back_populates="highlights")

    def __repr__(self) -> str:
        content_preview = self.content[:50] + "..." if len(self.content) > 50 else self.content
        return f"<Highlight(id={self.id}, content={content_preview!r})>"

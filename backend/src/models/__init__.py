"""Data models for Cognitive Reading Graph."""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all database models."""
    pass


# Import all models for convenience
from src.models.book import Book
from src.models.highlight import Highlight
from src.models.concept import Concept
from src.models.reader import Reader
from src.models.chapter import Chapter

__all__ = ["Base", "Book", "Highlight", "Concept", "Reader", "Chapter"]

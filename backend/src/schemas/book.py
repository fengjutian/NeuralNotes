"""Book schemas for API request/response validation."""

import uuid
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class BookBase(BaseModel):
    """Base schema for Book."""

    title: str = Field(..., min_length=1, max_length=255, description="Book title")
    author: str = Field(..., min_length=1, max_length=255, description="Author name")
    category: Optional[str] = Field(None, max_length=100, description="Book category")
    isbn: Optional[str] = Field(None, max_length=20, description="ISBN number")
    reading_time: Optional[str] = Field(None, max_length=50, description="Reading time")
    progress: Optional[float] = Field(None, ge=0, le=100, description="Progress percentage")
    reading_date: Optional[date] = Field(None, description="Reading date")


class BookCreate(BookBase):
    """Schema for creating a new book."""

    pass


class BookUpdate(BaseModel):
    """Schema for updating a book."""

    title: Optional[str] = Field(None, min_length=1, max_length=255)
    author: Optional[str] = Field(None, min_length=1, max_length=255)
    category: Optional[str] = Field(None, max_length=100)
    isbn: Optional[str] = Field(None, max_length=20)
    reading_time: Optional[str] = Field(None, max_length=50)
    progress: Optional[float] = Field(None, ge=0, le=100)
    reading_date: Optional[date] = None


class BookResponse(BookBase):
    """Schema for book response."""

    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    highlight_count: Optional[int] = Field(None, description="Number of highlights")
    created_at: Optional[str] = None
    updated_at: Optional[str] = None


class BookListResponse(BaseModel):
    """Schema for list of books response."""

    items: list[BookResponse]
    total: int
    page: int
    page_size: int

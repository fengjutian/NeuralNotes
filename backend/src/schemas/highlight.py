"""Highlight schemas for API request/response validation."""

import uuid
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class HighlightBase(BaseModel):
    """Base schema for Highlight."""

    content: str = Field(..., min_length=1, description="Highlighted text content")
    chapter: Optional[str] = Field(None, max_length=255, description="Chapter name")
    create_time: Optional[datetime] = Field(None, description="Creation time")
    url: Optional[str] = Field(None, description="Original URL")
    concepts: Optional[list[str]] = Field(None, description="Extracted concepts")
    emotion: Optional[str] = Field(None, max_length=50, description="Emotion/sentiment")
    domain: Optional[str] = Field(None, max_length=100, description="Subject domain")


class HighlightCreate(HighlightBase):
    """Schema for creating a new highlight."""

    book_id: uuid.UUID = Field(..., description="Parent book ID")


class HighlightUpdate(BaseModel):
    """Schema for updating a highlight."""

    content: Optional[str] = Field(None, min_length=1)
    chapter: Optional[str] = Field(None, max_length=255)
    concepts: Optional[list[str]] = None
    emotion: Optional[str] = Field(None, max_length=50)
    domain: Optional[str] = Field(None, max_length=100)


class HighlightResponse(HighlightBase):
    """Schema for highlight response."""

    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    book_id: uuid.UUID
    created_at: Optional[str] = None


class HighlightListResponse(BaseModel):
    """Schema for list of highlights response."""

    items: list[HighlightResponse]
    total: int
    page: int
    page_size: int

"""Reader model for storing user profile and preferences."""

import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import String, Text, DateTime, JSON, func
from sqlalchemy.orm import Mapped, mapped_column

from src.models import Base


class Reader(Base):
    """Reader entity representing a user/reader."""

    __tablename__ = "readers"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False, default="Reader")
    reading_profile: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    interests: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)
    preferences: Mapped[Optional[dict]] = mapped_column(JSON, nullable=True)
    created_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        server_default=func.now(),
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
    )

    def __repr__(self) -> str:
        return f"<Reader(id={self.id}, name={self.name!r})>"
"""Concept model for storing extracted concepts."""

import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import String, Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from src.models import Base


class Concept(Base):
    """Concept entity representing an extracted concept from highlights."""

    __tablename__ = "concepts"

    id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False, index=True)
    domain: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    frequency: Mapped[int] = mapped_column(Integer, default=0)
    last_mentioned: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    description: Mapped[Optional[str]] = mapped_column(String(500), nullable=True)
    created_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime,
        server_default=func.now(),
    )

    def __repr__(self) -> str:
        return f"<Concept(id={self.id}, name={self.name!r}, domain={self.domain!r})>"
"""Cognitive Timeline API endpoints -- thin route handlers that delegate to TimelineService."""

from typing import Optional

from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.services.timeline_service import timeline_service
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.get("/")
async def get_timeline(
    start_year: Optional[int] = Query(default=None, description="Start year"),
    end_year: Optional[int] = Query(default=None, description="End year"),
    db: Session = Depends(get_db),
) -> dict:
    """Get cognitive growth timeline.

    Args:
        start_year: Optional start year filter.
        end_year: Optional end year filter.
        db: Database session.

    Returns:
        Timeline data with yearly cognitive themes.
    """
    logger.info("Get timeline: %s-%s", start_year, end_year)
    return timeline_service.build_timeline(db, start_year, end_year)


@router.get("/pivot-points")
async def get_pivot_points(
    db: Session = Depends(get_db),
) -> dict:
    """Get significant cognitive pivot points.

    Returns:
        List of significant thinking shifts.
    """
    logger.info("Get pivot points")
    return timeline_service.get_pivot_points(db)

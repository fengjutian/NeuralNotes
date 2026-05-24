"""Cognitive Timeline API endpoints."""

from typing import Optional

from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, func, extract

from src.database import get_db
from src.models.book import Book
from src.models.highlight import Highlight
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
    logger.info("Get timeline: %d-%d", start_year, end_year)
    
    # Build year-based query
    year_query = select(
        extract("year", Highlight.create_time).label("year"),
        func.count(Highlight.id).label("highlight_count"),
    ).where(Highlight.create_time.isnot(None))
    
    if start_year:
        year_query = year_query.where(extract("year", Highlight.create_time) >= start_year)
    if end_year:
        year_query = year_query.where(extract("year", Highlight.create_time) <= end_year)
    
    year_query = year_query.group_by("year").order_by("year")
    
    year_results = db.execute(year_query).all()
    
    # Build year data with themes
    years_data = []
    for row in year_results:
        year = int(row[0]) if row[0] else None
        if year:
            # Get dominant emotions and domains for this year
            year_highlights_query = (
                select(Highlight.emotion, Highlight.domain)
                .where(
                    extract("year", Highlight.create_time) == year,
                    Highlight.create_time.isnot(None),
                )
            )
            year_highlights = db.execute(year_highlights_query).all()
            
            # Count emotions and domains
            emotions = {}
            domains = {}
            for h in year_highlights:
                if h[0]:
                    emotions[h[0]] = emotions.get(h[0], 0) + 1
                if h[1]:
                    domains[h[1]] = domains.get(h[1], 0) + 1
            
            # Get top books this year
            book_query = (
                select(Book.title, func.count(Highlight.id).label("count"))
                .join(Highlight)
                .where(extract("year", Highlight.create_time) == year)
                .group_by(Book.id)
                .order_by(func.count(Highlight.id).desc())
                .limit(3)
            )
            top_books = db.execute(book_query).all()
            
            years_data.append({
                "year": year,
                "highlight_count": row[1],
                "theme": max(emotions, key=emotions.get) if emotions else "neutral",
                "dominant_domains": list(domains.keys())[:3],
                "top_books": [{"title": b[0], "highlights": b[1]} for b in top_books],
            })
    
    # Identify pivot points (years with significant changes)
    pivot_points = []
    for i, year_data in enumerate(years_data):
        if i > 0:
            prev_count = years_data[i-1]["highlight_count"]
            curr_count = year_data["highlight_count"]
            
            # Significant increase (>100% growth)
            if prev_count > 0 and curr_count > prev_count * 2:
                pivot_points.append({
                    "year": year_data["year"],
                    "type": "growth_spike",
                    "message": f"Reading activity grew {curr_count / prev_count:.1f}x from previous year",
                    "highlight_count": curr_count,
                })
            # Significant decrease
            elif prev_count > 10 and curr_count < prev_count * 0.3:
                pivot_points.append({
                    "year": year_data["year"],
                    "type": "reading_drop",
                    "message": f"Reading activity decreased significantly",
                    "highlight_count": curr_count,
                })
    
    return {
        "years": years_data,
        "pivot_points": pivot_points,
        "total_highlights": sum(y["highlight_count"] for y in years_data),
        "year_count": len(years_data),
    }


@router.get("/pivot-points")
async def get_pivot_points(
    db: Session = Depends(get_db),
) -> dict:
    """Get significant cognitive pivot points.

    Returns:
        List of significant thinking shifts.
    """
    logger.info("Get pivot points")
    
    # Get yearly statistics
    year_query = (
        select(
            extract("year", Highlight.create_time).label("year"),
            func.count(Highlight.id).label("count"),
            func.count(func.distinct(Highlight.domain)).label("domain_count"),
        )
        .where(Highlight.create_time.isnot(None))
        .group_by("year")
        .order_by("year")
    )
    year_results = db.execute(year_query).all()
    
    pivot_points = []
    
    for i, row in enumerate(year_results):
        year = int(row[0]) if row[0] else None
        count = int(row[1])
        domain_count = int(row[2]) if row[2] else 0
        
        if not year:
            continue
        
        # Detect new domain exploration (first time seeing a domain)
        if i > 0:
            prev_domains_query = (
                select(Highlight.domain)
                .where(
                    extract("year", Highlight.create_time) == year - 1,
                    Highlight.domain.isnot(None),
                )
                .distinct()
            )
            prev_domains = set(db.execute(prev_domains_query).scalars().all())
            
            curr_domains_query = (
                select(Highlight.domain)
                .where(
                    extract("year", Highlight.create_time) == year,
                    Highlight.domain.isnot(None),
                )
                .distinct()
            )
            curr_domains = set(db.execute(curr_domains_query).scalars().all())
            
            new_domains = curr_domains - prev_domains
            
            if new_domains:
                pivot_points.append({
                    "year": year,
                    "type": "new_domain",
                    "message": f"Started exploring: {', '.join(list(new_domains)[:3])}",
                    "new_domains": list(new_domains),
                    "highlight_count": count,
                })
            
            # Growth detection
            prev_count = int(year_results[i-1][1])
            if prev_count > 0:
                growth = (count - prev_count) / prev_count
                if growth > 1.0:  # >100% growth
                    pivot_points.append({
                        "year": year,
                        "type": "growth",
                        "message": f"Reading activity increased {growth * 100:.0f}%",
                        "growth_rate": growth,
                        "highlight_count": count,
                    })
    
    return {
        "pivot_points": pivot_points,
        "count": len(pivot_points),
    }

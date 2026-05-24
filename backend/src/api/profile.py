"""Reading Profile API endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, func

from src.database import get_db
from src.models.book import Book
from src.models.highlight import Highlight
from src.services.graph_service import graph_service
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.get("/")
async def get_profile(
    db: Session = Depends(get_db),
) -> dict:
    """Get AI-generated reading profile.

    Args:
        db: Database session.

    Returns:
        Reading profile with preferences, tendencies, and suggestions.
    """
    logger.info("Get reading profile")
    
    # Get book count
    book_count = db.execute(select(func.count(Book.id))).scalar_one()
    
    # Get highlight count
    highlight_count = db.execute(select(func.count(Highlight.id))).scalar_one()
    
    # Get category distribution
    category_query = (
        select(Book.category, func.count(Book.id).label("count"))
        .group_by(Book.category)
        .order_by(func.count(Book.id).desc())
    )
    category_results = db.execute(category_query).all()
    categories = [
        {"name": r[0] or "Unknown", "count": r[1]}
        for r in category_results
    ]
    
    # Get emotional distribution
    emotion_query = (
        select(Highlight.emotion, func.count(Highlight.id).label("count"))
        .where(Highlight.emotion.isnot(None))
        .group_by(Highlight.emotion)
        .order_by(func.count(Highlight.id).desc())
    )
    emotion_results = db.execute(emotion_query).all()
    emotions = [
        {"type": r[0] or "Unknown", "count": r[1]}
        for r in emotion_results
    ]
    
    # Get domain distribution
    domain_query = (
        select(Highlight.domain, func.count(Highlight.id).label("count"))
        .where(Highlight.domain.isnot(None))
        .group_by(Highlight.domain)
        .order_by(func.count(Highlight.id).desc())
    )
    domain_results = db.execute(domain_query).all()
    domains = [
        {"name": r[0] or "Unknown", "count": r[1]}
        for r in domain_results
    ]
    
    return {
        "status": "generated",
        "summary": {
            "total_books": book_count,
            "total_highlights": highlight_count,
            "avg_highlights_per_book": highlight_count / book_count if book_count > 0 else 0,
        },
        "preferences": {
            "favorite_categories": categories[:5] if categories else [],
            "reading_emotions": emotions,
            "domains_of_interest": domains[:10] if domains else [],
        },
        "tendencies": {
            "dominant_emotion": emotions[0]["type"] if emotions else "neutral",
            "primary_domain": domains[0]["name"] if domains else "general",
        },
    }


@router.get("/preferences")
async def get_preferences(
    db: Session = Depends(get_db),
) -> dict:
    """Get detailed reading preferences.

    Args:
        db: Database session.

    Returns:
        Reading preferences breakdown.
    """
    logger.info("Get reading preferences")
    
    # Get top authors
    author_query = (
        select(Book.author, func.count(Book.id).label("count"))
        .group_by(Book.author)
        .order_by(func.count(Book.id).desc())
    )
    author_results = db.execute(author_query).all()
    top_authors = [{"name": r[0], "book_count": r[1]} for r in author_results[:10]]
    
    # Get categories with percentages
    total_books = db.execute(select(func.count(Book.id))).scalar_one()
    category_query = (
        select(Book.category, func.count(Book.id).label("count"))
        .group_by(Book.category)
        .order_by(func.count(Book.id).desc())
    )
    category_results = db.execute(category_query).all()
    categories = [
        {
            "name": r[0] or "Unknown",
            "count": r[1],
            "percentage": round((r[1] / total_books * 100), 2) if total_books > 0 else 0,
        }
        for r in category_results
    ]
    
    # Get time distribution
    time_query = (
        select(Highlight.create_time)
        .where(Highlight.create_time.isnot(None))
    )
    times = db.execute(time_query).scalars().all()
    
    return {
        "categories": categories,
        "authors": top_authors,
        "topics": [],  # Would be extracted from concepts
        "reading_times": {
            "morning": 0,
            "afternoon": 0,
            "evening": 0,
            "night": 0,
        },
    }


@router.get("/blind-spots")
async def get_blind_spots(
    db: Session = Depends(get_db),
) -> dict:
    """Get reading blind spots and improvement suggestions.

    Args:
        db: Database session.

    Returns:
        Identified blind spots with recommendations.
    """
    logger.info("Get blind spots")
    
    # Get all unique domains from highlights
    domain_query = (
        select(Highlight.domain)
        .where(Highlight.domain.isnot(None))
        .distinct()
    )
    active_domains = set(db.execute(domain_query).scalars().all())
    
    # Common knowledge domains that might be missing
    common_domains = [
        "哲学", "心理学", "经济学", "历史", "科技",
        "文学", "艺术", "科学", "社会学", "政治"
    ]
    
    missing_domains = [d for d in common_domains if d not in active_domains]
    
    # Get books without highlights
    empty_books_query = (
        select(Book)
        .outerjoin(Highlight)
        .group_by(Book.id)
        .having(func.count(Highlight.id) == 0)
    )
    empty_books = db.execute(empty_books_query).scalars().all()
    
    return {
        "missing_domains": missing_domains,
        "suggestions": [
            {
                "type": "explore_new_domains",
                "message": f"Consider exploring: {', '.join(missing_domains[:3])}",
                "priority": "high" if len(missing_domains) > 5 else "medium",
            },
            {
                "type": "incomplete_reading",
                "message": f"You have {len(empty_books)} books without highlights",
                "priority": "medium",
            },
        ],
        "stats": {
            "active_domains": len(active_domains),
            "potential_domains": len(common_domains),
            "coverage_percentage": round(len(active_domains) / len(common_domains) * 100, 2),
        },
    }

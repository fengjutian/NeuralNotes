"""Reading Profile API endpoints.

Delegates statistical analysis to ProfileService for preferences,
cognitive style, and blind spot detection.
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select, func

from src.database import get_db
from src.models.book import Book
from src.models.highlight import Highlight
from src.services.profile_service import profile_service
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


def _collect_concepts(db: Session) -> list[dict]:
    """Collect concepts from analysed highlights.

    Args:
        db: Database session.

    Returns:
        List of concept dicts with 'name' and 'domain' keys.
    """
    concepts: list[dict] = []
    # Fetch highlights that have concepts extracted
    stmt = (
        select(Highlight.concepts, Highlight.domain)
        .where(Highlight.concepts.isnot(None))
    )
    rows = db.execute(stmt).all()
    for concepts_json, domain in rows:
        if isinstance(concepts_json, list):
            for name in concepts_json:
                if isinstance(name, str) and name.strip():
                    concepts.append({
                        "name": name.strip(),
                        "domain": domain,
                    })

    # Also include highlights that have domain but no explicit concepts
    domain_stmt = (
        select(Highlight.domain)
        .where(Highlight.domain.isnot(None), Highlight.concepts.is_(None))
        .distinct()
    )
    domain_rows = db.execute(domain_stmt).scalars().all()
    for domain in domain_rows:
        if domain and domain.strip():
            concepts.append({
                "name": domain,
                "domain": domain,
            })

    return concepts


def _collect_books(db: Session) -> list[dict]:
    """Collect all books as dicts for profile_service input.

    Args:
        db: Database session.

    Returns:
        List of book dicts with category and author.
    """
    stmt = select(Book.category, Book.author)
    rows = db.execute(stmt).all()
    return [
        {"category": cat, "author": author}
        for cat, author in rows
    ]


@router.get("/")
async def get_profile(
    db: Session = Depends(get_db),
) -> dict:
    """Get reading profile with stats, preferences, cognitive style.

    Args:
        db: Database session.

    Returns:
        Reading profile with preferences, tendencies, cognitive style,
        and suggestions.
    """
    logger.info("Get reading profile")

    # --- Fast SQL stats ---
    book_count = db.execute(select(func.count(Book.id))).scalar_one()
    highlight_count = db.execute(select(func.count(Highlight.id))).scalar_one()

    # Category distribution
    category_query = (
        select(Book.category, func.count(Book.id).label("count"))
        .group_by(Book.category)
        .order_by(func.count(Book.id).desc())
    )
    category_results = db.execute(category_query).all()
    categories = {r[0] or "Unknown": r[1] for r in category_results}

    # Emotional distribution
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

    # Domain distribution
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

    # --- ProfileService analysis ---
    concepts = _collect_concepts(db)
    cognitive_style = profile_service.analyze_cognitive_style(concepts)

    books_list = _collect_books(db)
    preferences = profile_service.analyze_preferences(books_list, concepts)

    return {
        "total_books": book_count,
        "total_highlights": highlight_count,
        "categories": categories,
        "reading_time_total": "0",
        "recent_books": [
            {
                "id": str(book.id),
                "title": book.title,
                "author": book.author or "Unknown",
                "created_at": book.created_at.isoformat() if book.created_at else "",
            }
            for book in db.execute(
                select(Book).order_by(Book.created_at.desc()).limit(5)
            ).scalars().all()
        ],
        "_summary": {
            "avg_highlights_per_book": (
                highlight_count / book_count if book_count > 0 else 0
            ),
        },
        "_preferences": {
            "favorite_categories": preferences.get("categories", [])[:5],
            "top_authors": preferences.get("top_authors", [])[:5],
            "reading_emotions": emotions,
            "domains_of_interest": domains[:10] if domains else [],
        },
        "_tendencies": {
            "dominant_emotion": emotions[0]["type"] if emotions else "neutral",
            "primary_domain": domains[0]["name"] if domains else "general",
        },
        "_cognitive_style": cognitive_style,
    }


@router.get("/preferences")
async def get_preferences(
    db: Session = Depends(get_db),
) -> dict:
    """Get detailed reading preferences via ProfileService.

    Args:
        db: Database session.

    Returns:
        Reading preferences breakdown.
    """
    logger.info("Get reading preferences")

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

    # ProfileService analysis
    books_list = _collect_books(db)
    concepts = _collect_concepts(db)
    preferences = profile_service.analyze_preferences(books_list, concepts)

    return {
        "categories": categories,
        "authors": preferences.get("top_authors", []),
        "topics": preferences.get("top_concepts", []),
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
    """Get reading blind spots via ProfileService (20-domain analysis).

    Args:
        db: Database session.

    Returns:
        Identified blind spots with recommendations.
    """
    logger.info("Get blind spots")

    # Get all unique domains from highlights (for stats)
    domain_query = (
        select(Highlight.domain)
        .where(Highlight.domain.isnot(None))
        .distinct()
    )
    active_domains = set(db.execute(domain_query).scalars().all())

    # ProfileService blind spot analysis (20 domains)
    books_list = _collect_books(db)
    concepts = _collect_concepts(db)
    blind_spots = profile_service.detect_blind_spots(books_list, concepts)

    # Convert to response format
    missing_domains = [spot["domain"] for spot in blind_spots]
    suggestions = []
    for spot in blind_spots:
        priority = spot.get("severity", "medium")
        if priority == "low":
            priority = "low"
        elif priority == "high":
            priority = "high"
        else:
            priority = "medium"
        suggestions.append({
            "type": "explore_new_domains",
            "message": spot["suggestion"],
            "priority": priority,
        })

    # Get books without highlights
    empty_books_query = (
        select(Book)
        .outerjoin(Highlight)
        .group_by(Book.id)
        .having(func.count(Highlight.id) == 0)
    )
    empty_books = db.execute(empty_books_query).scalars().all()
    if empty_books:
        suggestions.append({
            "type": "incomplete_reading",
            "message": f"You have {len(empty_books)} books without highlights",
            "priority": "medium",
        })

    # All possible domains from the service (20 domains)
    all_possible_domains = {
        "管理学", "心理学", "哲学", "经济学", "历史",
        "文学", "社会学", "物理学", "生物学", "数学",
        "AI", "计算机科学", "教育学", "政治学", "法学",
        "医学", "艺术", "宗教", "伦理", "环境学",
    }

    return {
        "missing_domains": missing_domains,
        "suggestions": suggestions,
        "stats": {
            "active_domains": len(active_domains),
            "potential_domains": len(all_possible_domains),
            "coverage_percentage": round(
                len(active_domains) / len(all_possible_domains) * 100, 2
            ),
        },
    }

"""Timeline service for building cognitive growth timelines.

Extracts yearly reading statistics, detects pivot points,
and identifies domain shifts -- pure business logic, no FastAPI dependencies.
"""

from collections import Counter
from dataclasses import dataclass, field
from typing import Any, Optional

from sqlalchemy import select, func, extract
from sqlalchemy.orm import Session

from src.models.book import Book
from src.models.highlight import Highlight
from src.utils.logging import get_logger

logger = get_logger(__name__)


@dataclass
class YearSummary:
    """Reading summary for a single year."""

    year: int
    highlight_count: int
    theme: str = "neutral"
    dominant_domains: list[str] = field(default_factory=list)
    top_books: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class PivotPoint:
    """A significant shift or turning point in reading history."""

    year: int
    type: str  # growth_spike, reading_drop, new_domain, growth
    message: str
    highlight_count: int = 0
    new_domains: list[str] = field(default_factory=list)
    growth_rate: float = 0.0


@dataclass
class Timeline:
    """Complete cognitive timeline."""

    years: list[dict[str, Any]] = field(default_factory=list)
    pivot_points: list[dict[str, Any]] = field(default_factory=list)
    total_highlights: int = 0
    year_count: int = 0


class TimelineService:
    """Service for building cognitive growth timelines from reading data.

    Pure business logic: accepts a DB session, returns structured timeline data.
    No FastAPI dependencies.
    """

    def build_timeline(
        self,
        db: Session,
        start_year: Optional[int] = None,
        end_year: Optional[int] = None,
    ) -> dict[str, Any]:
        """Build a complete cognitive timeline with yearly breakdowns.

        Args:
            db: Database session.
            start_year: Optional start year filter.
            end_year: Optional end year filter.

        Returns:
            Dict with years, pivot_points, total_highlights, year_count.
        """
        logger.info("Building timeline: %d-%d", start_year, end_year)

        # Query: group highlights by year
        year_query = select(
            extract("year", Highlight.create_time).label("year"),
            func.count(Highlight.id).label("highlight_count"),
        ).where(Highlight.create_time.isnot(None))

        if start_year:
            year_query = year_query.where(
                extract("year", Highlight.create_time) >= start_year
            )
        if end_year:
            year_query = year_query.where(
                extract("year", Highlight.create_time) <= end_year
            )

        year_query = year_query.group_by("year").order_by("year")
        year_results = db.execute(year_query).all()

        years_data = []
        for row in year_results:
            year = int(row[0]) if row[0] else None
            if not year:
                continue

            summary = self._build_year_summary(db, year, row[1])
            years_data.append(summary)

        pivot_points = self._detect_pivot_points(years_data)

        return {
            "years": years_data,
            "pivot_points": pivot_points,
            "total_highlights": sum(y["highlight_count"] for y in years_data),
            "year_count": len(years_data),
        }

    def get_pivot_points(self, db: Session) -> dict[str, Any]:
        """Get detailed pivot points with domain-shift analysis.

        Args:
            db: Database session.

        Returns:
            Dict with pivot_points list and count.
        """
        logger.info("Getting pivot points")

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

        pivot_points: list[dict[str, Any]] = []

        for i, row in enumerate(year_results):
            year = int(row[0]) if row[0] else None
            count = int(row[1])
            domain_count = int(row[2]) if row[2] else 0

            if not year:
                continue

            if i > 0:
                # New domain detection
                new_domains = self._detect_new_domains(
                    db, year, int(year_results[i - 1][0])
                )
                if new_domains:
                    pivot_points.append({
                        "year": year,
                        "type": "new_domain",
                        "message": f"Started exploring: {', '.join(new_domains[:3])}",
                        "new_domains": new_domains,
                        "highlight_count": count,
                    })

                # Growth detection
                prev_count = int(year_results[i - 1][1])
                if prev_count > 0:
                    growth = (count - prev_count) / prev_count
                    if growth > 1.0:
                        pivot_points.append({
                            "year": year,
                            "type": "growth",
                            "message": f"Reading activity increased {growth * 100:.0f}%",
                            "growth_rate": growth,
                            "highlight_count": count,
                        })

        return {"pivot_points": pivot_points, "count": len(pivot_points)}

    # -- private helpers --------------------------------------------------

    def _build_year_summary(
        self, db: Session, year: int, highlight_count: int
    ) -> dict[str, Any]:
        """Aggregate emotions, domains, and top books for a single year."""
        # Emotions and domains for this year
        hq = (
            select(Highlight.emotion, Highlight.domain)
            .where(
                extract("year", Highlight.create_time) == year,
                Highlight.create_time.isnot(None),
            )
        )
        highlights = db.execute(hq).all()

        emotions = Counter(h[0] for h in highlights if h[0])
        domains = Counter(h[1] for h in highlights if h[1])

        # Top books this year
        bq = (
            select(Book.title, func.count(Highlight.id).label("count"))
            .join(Highlight)
            .where(extract("year", Highlight.create_time) == year)
            .group_by(Book.id)
            .order_by(func.count(Highlight.id).desc())
            .limit(3)
        )
        top_books = [{"title": b[0], "highlights": b[1]} for b in db.execute(bq).all()]

        return {
            "year": year,
            "highlight_count": highlight_count,
            "theme": emotions.most_common(1)[0][0] if emotions else "neutral",
            "dominant_domains": [d for d, _ in domains.most_common(3)],
            "top_books": top_books,
        }

    @staticmethod
    def _detect_pivot_points(
        years_data: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """Find years with >100% growth or significant decline."""
        pivots: list[dict[str, Any]] = []
        for i, yd in enumerate(years_data):
            if i == 0:
                continue
            prev = years_data[i - 1]["highlight_count"]
            curr = yd["highlight_count"]

            if prev > 0 and curr > prev * 2:
                pivots.append({
                    "year": yd["year"],
                    "type": "growth_spike",
                    "message": f"Reading activity grew {curr / prev:.1f}x from previous year",
                    "highlight_count": curr,
                })
            elif prev > 10 and curr < prev * 0.3:
                pivots.append({
                    "year": yd["year"],
                    "type": "reading_drop",
                    "message": "Reading activity decreased significantly",
                    "highlight_count": curr,
                })
        return pivots

    @staticmethod
    def _detect_new_domains(
        db: Session, current_year: int, previous_year: int
    ) -> list[str]:
        """Find domains that appear for the first time in current_year."""
        prev_domains = set(
            db.execute(
                select(Highlight.domain)
                .where(
                    extract("year", Highlight.create_time) == previous_year,
                    Highlight.domain.isnot(None),
                )
                .distinct()
            ).scalars().all()
        )
        curr_domains = set(
            db.execute(
                select(Highlight.domain)
                .where(
                    extract("year", Highlight.create_time) == current_year,
                    Highlight.domain.isnot(None),
                )
                .distinct()
            ).scalars().all()
        )
        return list(curr_domains - prev_domains)


# Singleton instance
timeline_service = TimelineService()

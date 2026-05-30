"""AI Analysis API endpoints."""

import time
from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from src.database import get_db
from src.schemas.highlight import HighlightListResponse, HighlightResponse
from src.services.highlight_service import highlight_service
from src.services.ai_analyzer import ai_analyzer
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


def _log_duration(step: str, start_time: float, extra: str = "") -> float:
    """Log duration since start_time and return current time."""
    elapsed = time.time() - start_time
    logger.info("[TIMING][Analyze] %s took %.3fs %s", step, elapsed, extra)
    return time.time()


@router.post("/", response_model=HighlightListResponse)
async def trigger_analysis(
    book_id: Optional[UUID] = None,
    highlight_ids: Optional[list[UUID]] = None,
    db: Session = Depends(get_db),
) -> HighlightListResponse:
    """Trigger AI analysis for highlights.

    Args:
        book_id: Optional book ID to analyze all unanalyzed highlights.
        highlight_ids: Optional specific highlight IDs to analyze.
        db: Database session.

    Returns:
        List of analyzed highlights.
    """
    t0 = time.time()
    logger.info("Analysis triggered: book_id=%s, highlight_count=%d", 
                book_id, len(highlight_ids or []))
    
    # Get highlights to analyze
    t1 = time.time()
    if highlight_ids:
        highlights = []
        for hid in highlight_ids:
            h = highlight_service.get_by_id(db, hid)
            if h:
                highlights.append(h)
    elif book_id:
        highlights = highlight_service.get_unanalyzed(db, book_id)
    else:
        raise HTTPException(status_code=400, detail="Must provide book_id or highlight_ids")
    
    t2 = _log_duration("fetch_highlights", t1, f"count={len(highlights)}")
    
    if not highlights:
        logger.warning("No highlights found to analyze")
        return HighlightListResponse(items=[], total=0, page=1, page_size=0)
    
    logger.info("Analyzing %d highlights", len(highlights))
    
    # Run batch analysis
    try:
        analyzed = ai_analyzer.analyze_highlights(highlights)
        t3 = _log_duration("ai_analysis", t2, f"input={len(highlights)}, output={len(analyzed)}")
        
        # Update database
        t4 = time.time()
        results = []
        for highlight, analysis in zip(highlights, analyzed):
            if analysis:
                from src.schemas.highlight import HighlightUpdate
                update_data = HighlightUpdate(
                    concepts=analysis.get("concepts", []),
                    emotion=analysis.get("emotion"),
                    domain=analysis.get("domain"),
                )
                updated = highlight_service.update(db, highlight.id, update_data)
                if updated:
                    results.append(HighlightResponse.model_validate(updated))
        
        t5 = _log_duration("update_database", t4, f"updated={len(results)}")
        _log_duration("total_analysis", t0, f"highlights={len(highlights)}, analyzed={len(results)}")
        
        return HighlightListResponse(
            items=results,
            total=len(results),
            page=1,
            page_size=len(results),
        )
        
    except Exception as e:
        logger.error("Analysis failed: %s", str(e))
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


@router.get("/status/{job_id}")
async def get_analysis_status(
    job_id: str,
) -> dict:
    """Get analysis job status.

    Note: Currently using synchronous processing, so jobs complete immediately.
    This endpoint is for future async job tracking.

    Args:
        job_id: Analysis job ID.

    Returns:
        Job status information.
    """
    logger.info("Get analysis status: %s", job_id)
    
    # For synchronous processing, jobs are already complete
    return {
        "job_id": job_id,
        "status": "completed",
        "progress": 100,
    }

import pathlib

content = '''"""Highlights API endpoints."""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import get_db
from src.services.highlight_service import highlight_service
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.delete("/{highlight_id}", status_code=204)
async def delete_highlight(
    highlight_id: UUID,
    db: Session = Depends(get_db),
) -> None:
    """Delete a specific highlight.

    Args:
        highlight_id: Highlight UUID.
        db: Database session.
    """
    logger.info("Delete highlight: %s", highlight_id)

    deleted = highlight_service.delete(db, highlight_id)
    if not deleted:
        raise HTTPException(status_code=404, detail=f"Highlight not found: {highlight_id}")
'''

p = pathlib.Path('backend/src/api/highlights.py')
p.write_text(content, encoding='utf-8')
print('Fixed highlights.py')

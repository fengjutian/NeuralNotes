"""Export API endpoints."""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import PlainTextResponse, StreamingResponse
from sqlalchemy.orm import Session
import io

from src.database import get_db
from src.services.book_service import book_service
from src.services.highlight_service import highlight_service
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.get("/{book_id}", response_class=PlainTextResponse)
async def export_book_notes(
    book_id: UUID,
    format: str = "md",
    db: Session = Depends(get_db),
) -> str:
    """Export book highlights as Markdown or plain text."""
    logger.info("Exporting book: %s format: %s", book_id, format)

    book = book_service.get_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book not found: {book_id}")

    highlights, _ = highlight_service.get_by_book(db, book_id, limit=10000)

    out: list[str] = []

    if format == "md":
        out.append(f"# {book.title}\n\n")
        out.append(f"**\u4f5c\u8005**: {book.author}\n\n")
        if book.category:
            out.append(f"**\u5206\u7c7b**: {book.category}\n\n")
        if book.reading_time:
            out.append(f"**\u9605\u8bfb\u65f6\u957f**: {book.reading_time}\n\n")
        out.append(f"**\u7b14\u8bb0\u6570**: {len(highlights)}\n\n")
        out.append("\n---\n\n")

        for h in highlights:
            if h.chapter:
                out.append(f"## {h.chapter}\n\n")
            out.append(f"> {h.content}\n\n")
            if h.url:
                out.append(f"[\u539f\u6587\u94fe\u63a5]({h.url})\n\n")
            out.append("\n")
    else:
        out.append(f"{book.title}\n")
        out.append(f"\u4f5c\u8005: {book.author}\n")
        out.append(f"\u7b14\u8bb0\u6570: {len(highlights)}\n")
        out.append("\n")
        for h in highlights:
            cp = f"\u3010{h.chapter}\u3011 " if h.chapter else ""
            out.append(f"{cp}{h.content}\n")

    result = "".join(out)
    logger.info("Exported %d highlights for book: %s", len(highlights), book_id)
    return result


@router.get("/{book_id}/download")
async def download_book_notes(
    book_id: UUID,
    format: str = "md",
    db: Session = Depends(get_db),
):
    """Download book highlights as a file."""
    book = book_service.get_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book not found: {book_id}")

    highlights, _ = highlight_service.get_by_book(db, book_id, limit=10000)

    out: list[str] = []

    if format == "md":
        out.append(f"# {book.title}\n\n")
        out.append(f"**\u4f5c\u8005**: {book.author}\n\n")
        if book.category:
            out.append(f"**\u5206\u7c7b**: {book.category}\n\n")
        out.append(f"**\u7b14\u8bb0\u6570**: {len(highlights)}\n\n")
        out.append("---\n\n")
        for h in highlights:
            if h.chapter:
                out.append(f"## {h.chapter}\n\n")
            out.append(f"> {h.content}\n\n")
            if h.url:
                out.append(f"[\u539f\u6587\u94fe\u63a5]({h.url})\n\n")
            out.append("\n")
    else:
        out.append(f"{book.title}\n\n")
        out.append(f"\u4f5c\u8005: {book.author}\n\n")
        for h in highlights:
            cp = f"\u3010{h.chapter}\u3011 " if h.chapter else ""
            out.append(f"{cp}{h.content}\n\n")

    output = "".join(out)
    safe = "".join(c for c in book.title if c.isalnum() or c in " _-()")
    filename = f"{safe}_\u7b14\u8bb0.{format}"

    return StreamingResponse(
        io.BytesIO(output.encode("utf-8")),
        media_type="text/plain",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )


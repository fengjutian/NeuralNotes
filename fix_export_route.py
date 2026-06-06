import pathlib

content = '''"""Export API endpoints."""

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

    lines: list[str] = []

    if format == "md":
        lines.append(f"# {book.title}\\n\\n")
        lines.append(f"**\\u4f5c\\u8005**: {book.author}\\n\\n")
        if book.category:
            lines.append(f"**\\u5206\\u7c7b**: {book.category}\\n\\n")
        if book.reading_time:
            lines.append(f"**\\u9605\\u8bfb\\u65f6\\u957f**: {book.reading_time}\\n\\n")
        lines.append(f"**\\u7b14\\u8bb0\\u6570**: {len(highlights)}\\n\\n")
        lines.append("\\n---\\n\\n")

        for h in highlights:
            if h.chapter:
                lines.append(f"## {h.chapter}\\n\\n")
            lines.append(f"> {h.content}\\n\\n")
            if h.url:
                lines.append(f"[\\u539f\\u6587\\u94fe\\u63a5]({h.url})\\n\\n")
            lines.append("\\n")
    else:
        lines.append(f"{book.title}\\n")
        lines.append(f"\\u4f5c\\u8005: {book.author}\\n")
        lines.append(f"\\u7b14\\u8bb0\\u6570: {len(highlights)}\\n")
        lines.append("\\n")
        for h in highlights:
            chapter_prefix = f"\\u3010{h.chapter}\\u3011 " if h.chapter else ""
            lines.append(f"{chapter_prefix}{h.content}\\n")

    result = "".join(lines)
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

    lines: list[str] = []

    if format == "md":
        lines.append(f"# {book.title}\\n\\n")
        lines.append(f"**\\u4f5c\\u8005**: {book.author}\\n\\n")
        if book.category:
            lines.append(f"**\\u5206\\u7c7b**: {book.category}\\n\\n")
        lines.append(f"**\\u7b14\\u8bb0\\u6570**: {len(highlights)}\\n\\n")
        lines.append("---\\n\\n")
        for h in highlights:
            if h.chapter:
                lines.append(f"## {h.chapter}\\n\\n")
            lines.append(f"> {h.content}\\n\\n")
            if h.url:
                lines.append(f"[\\u539f\\u6587\\u94fe\\u63a5]({h.url})\\n\\n")
            lines.append("\\n")
    else:
        lines.append(f"{book.title}\\n\\n")
        lines.append(f"\\u4f5c\\u8005: {book.author}\\n\\n")
        for h in highlights:
            chapter_prefix = f"\\u3010{h.chapter}\\u3011 " if h.chapter else ""
            lines.append(f"{chapter_prefix}{h.content}\\n\\n")

    output = "".join(lines)
    safe_title = "".join(c for c in book.title if c.isalnum() or c in " _-()")
    filename = f"{safe_title}_\\u7b14\\u8bb0.{format}"

    return StreamingResponse(
        io.BytesIO(output.encode("utf-8")),
        media_type="text/plain",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
'''

p = pathlib.Path('backend/src/api/export_routes.py')
p.write_text(content, encoding='utf-8')
print('Written export_routes.py')

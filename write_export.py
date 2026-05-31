import pathlib

content = '''"""Export API endpoints."""

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session

from src.database import get_db
from src.services.book_service import book_service
from src.services.highlight_service import highlight_service
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.get("/books/{book_id}/export", response_class=PlainTextResponse)
async def export_book_notes(
    book_id: UUID,
    format: str = "md",
    db: Session = Depends(get_db),
) -> str:
    """Export book highlights as Markdown or plain text.

    Args:
        book_id: Book UUID.
        format: Export format ("md" or "txt").
        db: Database session.

    Returns:
        Formatted export content.
    """
    logger.info("Exporting book: %s format: %s", book_id, format)

    book = book_service.get_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book not found: {book_id}")

    highlights, _ = highlight_service.get_by_book(db, book_id, limit=10000)

    if format == "md":
        lines = [
            f"# {book.title}\n",
            f"**作者**: {book.author}\n",
        ]
        if book.category:
            lines.append(f"**分类**: {book.category}\n")
        if book.reading_time:
            lines.append(f"**阅读时长**: {book.reading_time}\n")
        lines.append(f"**笔记数**: {len(highlights)}\n")
        lines.append("\n---\n\n")

        for h in highlights:
            if h.chapter:
                lines.append(f"## {h.chapter}\n\n")
            lines.append(f"> {h.content}\n\n")
            if h.url:
                lines.append(f"[原文链接]({h.url})\n\n")
            lines.append("\n")
    else:
        lines = [
            f"{book.title}\n",
            f"作者: {book.author}\n",
            f"笔记数: {len(highlights)}\n",
            "\n",
        ]
        for h in highlights:
            chapter_prefix = f"【{h.chapter}】 " if h.chapter else ""
            lines.append(f"{chapter_prefix}{h.content}\n")

    result = "".join(lines)
    logger.info("Exported %d highlights for book: %s", len(highlights), book_id)
    return result


@router.get("/books/{book_id}/export/download")
async def download_book_notes(
    book_id: UUID,
    format: str = "md",
    db: Session = Depends(get_db),
):
    """Download book highlights as a file."""
    from fastapi.responses import StreamingResponse
    import io

    book = book_service.get_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail=f"Book not found: {book_id}")

    highlights, _ = highlight_service.get_by_book(db, book_id, limit=10000)

    if format == "md":
        lines = [f"# {book.title}\n\n", f"**作者**: {book.author}\n\n"]
        if book.category:
            lines.append(f"**分类**: {book.category}\n\n")
        lines.append(f"**笔记数**: {len(highlights)}\n\n---\n\n")
        for h in highlights:
            if h.chapter:
                lines.append(f"## {h.chapter}\n\n")
            lines.append(f"> {h.content}\n\n")
            if h.url:
                lines.append(f"[原文链接]({h.url})\n\n")
            lines.append("\n")
    else:
        lines = [f"{book.title}\n\n", f"作者: {book.author}\n\n"]
        for h in highlights:
            chapter_prefix = f"【{h.chapter}】 " if h.chapter else ""
            lines.append(f"{chapter_prefix}{h.content}\n\n")

    output = "".join(lines)
    safe_title = "".join(c for c in book.title if c.isalnum() or c in " _-()")
    filename = f"{safe_title}_笔记.{format}"

    return StreamingResponse(
        io.BytesIO(output.encode("utf-8")),
        media_type="text/plain",
        headers={"Content-Disposition": f"attachment; filename={filename}"},
    )
'''

p = pathlib.Path('backend/src/api/export_routes.py')
p.write_text(content, encoding='utf-8')
print('Written export_routes.py')

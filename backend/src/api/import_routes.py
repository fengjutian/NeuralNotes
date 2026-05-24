"""File import API endpoints."""

from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.services.markdown_parser import MarkdownParser
from src.services.book_service import book_service
from src.services.highlight_service import highlight_service
from src.schemas.book import BookCreate
from src.schemas.highlight import HighlightCreate
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()


@router.post("/")
async def import_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
) -> dict:
    """Import a markdown file from WeChat Reading.

    Args:
        file: The markdown file to import.
        db: Database session.

    Returns:
        Import result with book information.
    """
    logger.info("Import request received: %s", file.filename)

    # Validate file type
    if not file.filename.endswith(".md"):
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Expected .md file, got: {file.filename}",
        )

    # Read file content
    content = await file.read()
    try:
        text = content.decode("utf-8")
    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="File encoding must be UTF-8",
        )

    # Parse markdown
    try:
        book_data = markdown_parser.parse(text)
        logger.info("Parsed book: %s", book_data.title)
    except Exception as e:
        logger.error("Failed to parse markdown: %s", str(e))
        raise HTTPException(
            status_code=422,
            detail=f"Failed to parse markdown: {str(e)}",
        )

    # Create book in database
    try:
        book = book_service.create(
            db,
            BookCreate(
                title=book_data.title,
                author=book_data.author,
                category=book_data.category,
                isbn=book_data.isbn,
                reading_time=book_data.reading_time,
                progress=book_data.progress,
                reading_date=book_data.reading_date,
            ),
        )
        logger.info("Created book: %s", book.id)
    except Exception as e:
        logger.error("Failed to create book: %s", str(e))
        raise HTTPException(
            status_code=500,
            detail=f"Failed to create book: {str(e)}",
        )

    # Create highlights
    highlight_count = 0
    for hl_data in book_data.highlights:
        try:
            highlight_service.create(
                db,
                HighlightCreate(
                    book_id=book.id,
                    content=hl_data.content,
                    chapter=hl_data.chapter,
                    create_time=hl_data.create_time,
                    url=hl_data.url,
                ),
            )
            highlight_count += 1
        except Exception as e:
            logger.warning("Failed to create highlight: %s", str(e))

    logger.info("Created %d highlights for book %s", highlight_count, book.id)

    return {
        "status": "success",
        "book_id": str(book.id),
        "title": book.title,
        "author": book.author,
        "highlight_count": highlight_count,
    }


@router.post("/batch")
async def import_batch(
    files: list[UploadFile] = File(...),
    db: Session = Depends(get_db),
) -> dict:
    """Import multiple markdown files.

    Args:
        files: List of markdown files to import.
        db: Database session.

    Returns:
        Batch import results.
    """
    logger.info("Batch import request: %d files", len(files))

    results = []
    for file in files:
        if not file.filename.endswith(".md"):
            results.append({
                "file": file.filename,
                "status": "error",
                "message": "Invalid file type",
            })
            continue

        try:
            content = await file.read()
            text = content.decode("utf-8")
            book_data = markdown_parser.parse(text)

            book = book_service.create(
                db,
                BookCreate(
                    title=book_data.title,
                    author=book_data.author,
                    category=book_data.category,
                ),
            )

            highlight_count = 0
            for hl_data in book_data.highlights:
                try:
                    highlight_service.create(
                        db,
                        HighlightCreate(
                            book_id=book.id,
                            content=hl_data.content,
                            chapter=hl_data.chapter,
                            create_time=hl_data.create_time,
                        ),
                    )
                    highlight_count += 1
                except Exception:
                    pass

            results.append({
                "file": file.filename,
                "status": "success",
                "book_id": str(book.id),
                "title": book.title,
                "highlight_count": highlight_count,
            })

        except Exception as e:
            logger.error("Failed to import %s: %s", file.filename, str(e))
            results.append({
                "file": file.filename,
                "status": "error",
                "message": str(e),
            })

    success_count = sum(1 for r in results if r["status"] == "success")

    return {
        "status": "completed",
        "total": len(files),
        "success": success_count,
        "failed": len(files) - success_count,
        "results": results,
    }

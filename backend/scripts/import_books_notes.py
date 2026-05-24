#!/usr/bin/env python
"""Script to import all markdown files from books_notes directory."""

import sys
import asyncio
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.database import SessionLocal
from src.services.markdown_parser import markdown_parser
from src.services.book_service import book_service
from src.services.highlight_service import highlight_service
from src.schemas.book import BookCreate
from src.schemas.highlight import HighlightCreate
from src.utils.logging import get_logger, setup_logging

logger = get_logger(__name__)


def import_single_file(db, file_path: Path) -> dict:
    """Import a single markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        book_data = markdown_parser.parse(content)
        logger.info(f"Parsed: {book_data.title}")
        
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
                logger.warning(f"Failed highlight: {e}")
        
        return {
            "status": "success",
            "file": file_path.name,
            "book_id": str(book.id),
            "title": book.title,
            "highlight_count": highlight_count,
        }
    except Exception as e:
        logger.error(f"Failed to import {file_path.name}: {e}")
        return {
            "status": "error",
            "file": file_path.name,
            "error": str(e),
        }


def main():
    setup_logging()
    logger.info("Starting batch import from books_notes/")
    
    # Find all md files
    books_dir = Path(__file__).parent.parent / "books_notes"
    md_files = list(books_dir.glob("*.md"))
    
    logger.info(f"Found {len(md_files)} markdown files")
    
    db = SessionLocal()
    results = []
    
    try:
        for i, file_path in enumerate(md_files, 1):
            logger.info(f"Processing [{i}/{len(md_files)}]: {file_path.name}")
            result = import_single_file(db, file_path)
            results.append(result)
            
            if result["status"] == "success":
                print(f"  ✅ {result['title']} ({result['highlight_count']} highlights)")
            else:
                print(f"  ❌ {result['file']}: {result['error']}")
    finally:
        db.close()
    
    # Summary
    success = sum(1 for r in results if r["status"] == "success")
    failed = len(results) - success
    
    print(f"\n{'='*50}")
    print(f"Import complete!")
    print(f"Total: {len(results)}")
    print(f"Success: {success}")
    print(f"Failed: {failed}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
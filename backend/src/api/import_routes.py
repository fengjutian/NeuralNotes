"""File import API endpoints."""

from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.services.markdown_parser import MarkdownParser
from src.services.book_service import book_service
from src.services.highlight_service import highlight_service
from src.services.graph_service import graph_service
from src.services.concept_extractor import ConceptExtractor
from src.schemas.book import BookCreate
from src.schemas.highlight import HighlightCreate
from src.utils.logging import get_logger

logger = get_logger(__name__)

router = APIRouter()

# Initialize services
concept_extractor = ConceptExtractor()


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
    created_highlights = []
    for hl_data in book_data.highlights:
        try:
            highlight = highlight_service.create(
                db,
                HighlightCreate(
                    book_id=book.id,
                    content=hl_data.content,
                    chapter=hl_data.chapter,
                    create_time=hl_data.create_time,
                    url=hl_data.url,
                ),
            )
            created_highlights.append(highlight)
            highlight_count += 1
        except Exception as e:
            logger.warning("Failed to create highlight: %s", str(e))

    logger.info("Created %d highlights for book %s", highlight_count, book.id)

    # === Generate Knowledge Graph Data ===
    # 1. Create book node in Neo4j
    try:
        graph_service.create_book_node(
            book_id=book.id,
            title=book.title,
            author=book.author,
            category=book.category,
        )
        logger.info("Created book node in graph: %s", book.id)
    except Exception as e:
        logger.warning("Failed to create book node in graph: %s", str(e))

    # 2. Create author node and link
    try:
        graph_service.create_author_node(name=book.author)
        graph_service.link_book_to_author(book_id=book.id, author_name=book.author)
        logger.info("Created author node and link: %s", book.author)
    except Exception as e:
        logger.warning("Failed to create author in graph: %s", str(e))

    # 3. Create highlight nodes and link to book
    # 4. Extract concepts and create concept nodes
    concept_count = 0
    for highlight in created_highlights:
        try:
            # Create highlight node in Neo4j
            graph_service.create_highlight_node(
                highlight_id=highlight.id,
                content=highlight.content,
                chapter=highlight.chapter,
            )
            # Link highlight to book
            graph_service.link_highlight_to_book(
                highlight_id=highlight.id,
                book_id=book.id,
            )

            # Extract concepts from highlight
            concepts = concept_extractor.extract(highlight.content)
            if concepts and concepts.concepts:
                for concept_name in concepts.concepts:
                    try:
                        # Create concept node
                        from src.models.concept import Concept
                        concept = Concept(name=concept_name, domain=concepts.domain)
                        db.add(concept)
                        db.commit()

                        # Create concept node in Neo4j
                        graph_service.create_concept_node(
                            concept_id=concept.id,  # Already a string UUID
                            name=concept_name,
                            domain=concepts.domain,
                        )
                        # Link book to concept
                        graph_service.link_book_to_concept(
                            book_id=book.id,
                            concept_name=concept_name,
                        )
                        # Link highlight to concept
                        graph_service.link_highlight_to_concept(
                            highlight_id=highlight.id,
                            concept_name=concept_name,
                        )
                        concept_count += 1
                    except Exception as e:
                        logger.warning("Failed to create concept %s: %s", concept_name, str(e))
                        db.rollback()

        except Exception as e:
            logger.warning("Failed to create highlight in graph: %s", str(e))

    logger.info("Created %d concept nodes for book %s", concept_count, book.id)

    return {
        "status": "success",
        "book_id": str(book.id),
        "title": book.title,
        "author": book.author,
        "highlight_count": highlight_count,
        "concept_count": concept_count,
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
            created_highlights = []
            for hl_data in book_data.highlights:
                try:
                    highlight = highlight_service.create(
                        db,
                        HighlightCreate(
                            book_id=book.id,
                            content=hl_data.content,
                            chapter=hl_data.chapter,
                            create_time=hl_data.create_time,
                        ),
                    )
                    created_highlights.append(highlight)
                    highlight_count += 1
                except Exception:
                    pass

            # Generate graph data for batch import
            concept_count = 0
            try:
                graph_service.create_book_node(
                    book_id=book.id,
                    title=book.title,
                    author=book.author,
                    category=book.category,
                )
                graph_service.create_author_node(name=book.author)
                graph_service.link_book_to_author(book_id=book.id, author_name=book.author)

                for highlight in created_highlights:
                    try:
                        graph_service.create_highlight_node(
                            highlight_id=highlight.id,
                            content=highlight.content,
                            chapter=highlight.chapter,
                        )
                        graph_service.link_highlight_to_book(
                            highlight_id=highlight.id,
                            book_id=book.id,
                        )

                        concepts = concept_extractor.extract(highlight.content)
                        if concepts and concepts.concepts:
                            for concept_name in concepts.concepts:
                                from src.models.concept import Concept
                                concept = Concept(name=concept_name, domain=concepts.domain)
                                db.add(concept)
                                db.commit()
                                graph_service.create_concept_node(
                                    concept_id=concept.id,  # Already a string UUID
                                    name=concept_name,
                                    domain=concepts.domain,
                                )
                                graph_service.link_book_to_concept(book_id=book.id, concept_name=concept_name)
                                graph_service.link_highlight_to_concept(
                                    highlight_id=highlight.id,
                                    concept_name=concept_name,
                                )
                                concept_count += 1
                    except Exception:
                        db.rollback()
            except Exception as e:
                logger.warning("Failed to create graph data for batch import: %s", str(e))

            results.append({
                "file": file.filename,
                "status": "success",
                "book_id": str(book.id),
                "title": book.title,
                "highlight_count": highlight_count,
                "concept_count": concept_count,
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

"""FastAPI application entry point for Cognitive Reading Graph."""

from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.config import settings
from src.utils.logging import setup_logging, get_logger
from src.utils.exceptions import AppException
from src.database import init_db
from src.neo4j_client import neo4j_client
from src.qdrant_client import qdrant_client

# Initialize logging
setup_logging()
logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Application lifespan manager for startup and shutdown events."""
    # Startup
    logger.info("Starting %s v%s", settings.app_name, settings.app_version)

    # Initialize database tables
    try:
        init_db()
        logger.info("Database initialized")
    except Exception as e:
        logger.error("Failed to initialize database: %s", str(e))

    # Connect to Neo4j
    try:
        neo4j_client.connect()
    except Exception as e:
        logger.warning("Neo4j connection failed: %s (continuing without graph)", str(e))

    # Connect to Qdrant
    try:
        qdrant_client.connect()
        qdrant_client.ensure_collection()
    except Exception as e:
        logger.warning("Qdrant connection failed: %s (continuing without vector search)", str(e))

    logger.info("Application startup complete")

    yield

    # Shutdown
    logger.info("Shutting down %s", settings.app_name)
    neo4j_client.disconnect()
    qdrant_client.disconnect()
    logger.info("Application shutdown complete")


# Create FastAPI application
app = FastAPI(
    title=settings.app_name,
    description="AI-powered personal knowledge graph based on WeChat Reading notes",
    version=settings.app_version,
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Exception handlers
@app.exception_handler(AppException)
async def app_exception_handler(
    request: Request,
    exc: AppException,
) -> JSONResponse:
    """Handle application-specific exceptions."""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=exc.to_dict(),
    )


@app.exception_handler(Exception)
async def general_exception_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    """Handle unexpected exceptions."""
    logger.exception("Unexpected error: %s", str(exc))
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": "InternalServerError",
            "message": "An unexpected error occurred",
            "details": {"type": type(exc).__name__} if settings.debug else {},
        },
    )


# Health check endpoint
@app.get("/health", tags=["health"])
async def health_check() -> dict:
    """Health check endpoint."""
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version,
    }


# Root endpoint
@app.get("/", tags=["root"])
async def root() -> dict:
    """Root endpoint with API information."""
    return {
        "app": settings.app_name,
        "version": settings.app_version,
        "docs": "/docs",
        "health": "/health",
    }


# Import and include routers
from src.api import api_router

app.include_router(api_router)

def get_application() -> FastAPI:
    """Get the FastAPI application instance.

    Returns:
        Configured FastAPI application.
    """
    return app

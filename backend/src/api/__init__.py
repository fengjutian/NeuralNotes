"""API routes for Cognitive Reading Graph."""

from fastapi import APIRouter

# Import routers
from src.api.books import router as books_router
from src.api.import_routes import router as import_router
from src.api.analyze import router as analyze_router
from src.api.graph import router as graph_router
from src.api.profile import router as profile_router
from src.api.search import router as search_router
from src.api.timeline import router as timeline_router
from src.api.sync import router as sync_router
from src.api.mysql_graph import router as mysql_graph_router

# Create main API router
api_router = APIRouter(prefix="/api/v1", redirect_slashes=False)

# Include sub-routers
api_router.include_router(import_router, prefix="/import", tags=["Import"])
api_router.include_router(books_router, prefix="/books", tags=["Books"])
api_router.include_router(analyze_router, prefix="/analyze", tags=["Analysis"])
api_router.include_router(graph_router, prefix="/graph", tags=["Graph"])
api_router.include_router(profile_router, prefix="/profile", tags=["Profile"])
api_router.include_router(search_router, prefix="/search", tags=["Search"])
api_router.include_router(timeline_router, prefix="/timeline", tags=["Timeline"])
api_router.include_router(sync_router, prefix="/sync", tags=["Sync"])
api_router.include_router(mysql_graph_router, prefix="/mysql-graph", tags=["MySQL Graph"])

__all__ = ["api_router"]

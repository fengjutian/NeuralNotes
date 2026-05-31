import pathlib

p = pathlib.Path('backend/src/api/__init__.py')
content = p.read_text(encoding='utf-8')

# Add export import
content = content.replace(
    'from src.api.highlights import router as highlights_router',
    'from src.api.highlights import router as highlights_router\nfrom src.api.export_routes import router as export_router'
)

# Add export router include
content = content.replace(
    'api_router.include_router(highlights_router, prefix="/highlights", tags=["Highlights"])',
    'api_router.include_router(highlights_router, prefix="/highlights", tags=["Highlights"])\napi_router.include_router(export_router, prefix="/export", tags=["Export"])'
)

p.write_text(content, encoding='utf-8')
print('Registered export router')

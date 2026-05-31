import pathlib

p = pathlib.Path('backend/src/api/__init__.py')
content = p.read_text(encoding='utf-8')

# Add highlights import
content = content.replace(
    'from src.api.mysql_graph import router as mysql_graph_router',
    'from src.api.mysql_graph import router as mysql_graph_router\nfrom src.api.highlights import router as highlights_router'
)

# Add highlights router after mysql graph
content = content.replace(
    'api_router.include_router(mysql_graph_router, prefix="/mysql-graph", tags=["MySQL Graph"])',
    'api_router.include_router(mysql_graph_router, prefix="/mysql-graph", tags=["MySQL Graph"])\napi_router.include_router(highlights_router, prefix="/highlights", tags=["Highlights"])'
)

p.write_text(content, encoding='utf-8')
print('Updated __init__.py')

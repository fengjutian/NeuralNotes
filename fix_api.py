import pathlib

p = pathlib.Path('frontend/src/api/index.ts')
content = p.read_text(encoding='utf-8')

# Add highlightApi before analyzeApi
content = content.replace(
    'export const analyzeApi = {',
    'export const highlightApi = {\n  delete: (highlightId: string) =>\n    api.delete("/highlights/" + highlightId),\n}\n\nexport const analyzeApi = {'
)

p.write_text(content, encoding='utf-8')
print('Added highlightApi to index.ts')

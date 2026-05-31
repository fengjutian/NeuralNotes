import pathlib

p = pathlib.Path('frontend/src/components/AppLayout.tsx')
content = p.read_text(encoding='utf-8')
# Remove unused FileTextOutlined
content = content.replace('\n  FileTextOutlined,\n', '\n')
p.write_text(content, encoding='utf-8')
print('Removed FileTextOutlined')

with open('main.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []
i = 0
skip = False

while i < len(lines):
    line = lines[i]
    if '# Connect to Qdrant' in line and 'disabled' not in line:
        out.append('    # Connect to Qdrant (disabled)\n')
        out.append('    # try:\n')
        out.append('    #     qdrant_client.connect()\n')
        out.append('    #     qdrant_client.ensure_collection()\n')
        out.append('    # except Exception as e:\n')
        out.append('    #     logger.warning("Qdrant connection failed: %s", str(e))\n')
        skip = True
    elif skip and ('except' in line or 'logger.warning' in line):
        i += 1
        continue
    out.append(line)
    i += 1

with open('main.py', 'w', encoding='utf-8') as f:
    f.writelines(out)

print('Done!')

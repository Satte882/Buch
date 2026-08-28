from pathlib import Path
import re

text = Path('AUSNAHMEZUSTAND_FINAL.md').read_text(encoding='utf-8')
parts = re.split(r'(?m)^## (Prolog|\d+)\s*$', text)

hits = []
for i in range(1, len(parts), 2):
    chapter = parts[i]
    body = parts[i+1]
    paras = [p.strip() for p in re.split(r'\n\s*\n', body) if p.strip()]
    for j, p in enumerate(paras):
        if re.search(r'\bsondern\b', p, re.I):
            prev = paras[j-1] if j else ''
            context = (prev + '\n\n' + p).strip()
            family = bool(re.search(r'\b(?:nicht|kein(?:e|en|em|er|es)?|weder)\b[\s\S]{0,500}\bsondern\b', context, re.I))
            hits.append((chapter, j+1, family, prev, p))

print(f'TOTAL_SONDERN {len(hits)}')
print(f'NICHT_SONDERN_FAMILY {sum(1 for h in hits if h[2])}')
for n, (chapter, para, family, prev, cur) in enumerate(hits, 1):
    print(f'@@ {n:03d} | CH {chapter} | PARA {para} | FAMILY={int(family)}')
    if prev:
        print('PREV:', prev.replace('\n', ' / '))
    print('HIT :', cur.replace('\n', ' / '))
    print()

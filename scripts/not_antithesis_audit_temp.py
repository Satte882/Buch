from pathlib import Path
import re

text = Path('AUSNAHMEZUSTAND_FINAL.md').read_text(encoding='utf-8')
parts = re.split(r'(?m)^## (Prolog|\d+)\s*$', text)
idx = 0
for i in range(1, len(parts), 2):
    ch = parts[i]
    body = parts[i+1]
    paras = [p.strip() for p in re.split(r'\n\s*\n', body) if p.strip()]
    for j, p in enumerate(paras):
        # Focus on the conspicuous short paragraph-level antithesis pattern.
        if p.startswith('Nicht ') and len(re.findall(r"\b[\wÄÖÜäöüß’'-]+\b", p)) <= 12:
            idx += 1
            prev = paras[j-1] if j else ''
            nxt = paras[j+1] if j+1 < len(paras) else ''
            print(f'@@ {idx:03d} | CH {ch}')
            print('PREV:', prev.replace('\n', ' '))
            print('HIT :', p.replace('\n', ' '))
            print('NEXT:', nxt.replace('\n', ' '))
            print()
print('TOTAL', idx)

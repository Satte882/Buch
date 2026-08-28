from __future__ import annotations

import re
from pathlib import Path

PATH = Path('AUSNAHMEZUSTAND_FINAL.md')
text = PATH.read_text(encoding='utf-8')
paras = text.split('\n\n')

chapter = 'Vorsatz'
rows = []
current = []

def words(s: str) -> int:
    return len(re.findall(r"[A-Za-zÄÖÜäöüß0-9]+(?:['’\-][A-Za-zÄÖÜäöüß0-9]+)*", s))

def dialogue_only(s: str) -> bool:
    t = s.strip()
    return t.startswith('„') and t.endswith('“') and '\n' not in t

def flush(run):
    if len(run) < 4:
        return
    short = sum(words(p['text']) <= 6 for p in run)
    tiny = sum(words(p['text']) <= 3 for p in run)
    confirms = sum(p['text'].strip() in {'„Ja.“','„Nein.“','„Noch nicht.“','„Genau.“','„Richtig.“','„Gut.“','„Okay.“','„Möglich.“'} for p in run)
    questions = sum('?' in p['text'] for p in run)
    score = len(run) + short * 2 + tiny * 2 + confirms * 4 + questions
    if short >= 2 and (questions >= 2 or confirms >= 1):
        rows.append((score, run[0]['chapter'], run[0]['index'], run.copy()))

for i, p in enumerate(paras):
    t = p.strip()
    if t.startswith('## '):
        chapter = t[3:]
    if dialogue_only(p):
        current.append({'index': i, 'chapter': chapter, 'text': p})
    else:
        flush(current)
        current = []
flush(current)

# Also capture confirmation-heavy microsequences with one short action beat between dialogue lines.
for i, p in enumerate(paras):
    if p.strip() not in {'„Ja.“','„Nein.“','„Noch nicht.“','„Genau.“','„Richtig.“','„Gut.“','„Okay.“','„Möglich.“'}:
        continue
    lo, hi = max(0, i-3), min(len(paras), i+4)
    window = paras[lo:hi]
    q = sum('?' in x for x in window)
    short = sum(words(x) <= 6 for x in window if x.strip() and not x.strip().startswith('##'))
    if q >= 1 and short >= 3:
        ch = chapter
        # recover chapter locally
        for j in range(i, -1, -1):
            tt = paras[j].strip()
            if tt.startswith('## '):
                ch = tt[3:]
                break
        score = 10 + q + short
        rows.append((score, ch, i, [{'index': k, 'chapter': ch, 'text': paras[k]} for k in range(lo,hi)]))

# Deduplicate overlapping windows and print strongest examples, balanced across manuscript.
rows.sort(key=lambda r: (-r[0], int(r[1]) if r[1].isdigit() else -1, r[2]))
seen = set()
selected = []
per_chapter = {}
for row in rows:
    _, ch, idx, run = row
    key = (ch, idx // 3)
    if key in seen:
        continue
    if per_chapter.get(ch, 0) >= 6:
        continue
    seen.add(key)
    per_chapter[ch] = per_chapter.get(ch, 0) + 1
    selected.append(row)
    if len(selected) >= 180:
        break

selected.sort(key=lambda r: (int(r[1]) if r[1].isdigit() else -1, r[2]))
print(f'CANDIDATES={len(selected)}')
for n, (score, ch, idx, run) in enumerate(selected, 1):
    print(f'\n=== CANDIDATE {n:03d} | CHAPTER {ch} | SCORE {score} | PARA {idx} ===')
    for item in run:
        compact = item['text'].replace('\n', ' / ')
        print(f"[{item['index']}] {compact}")

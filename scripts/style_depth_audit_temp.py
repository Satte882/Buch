from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

PATH = Path('AUSNAHMEZUSTAND_FINAL.md')
text = PATH.read_text(encoding='utf-8')
paras = text.split('\n\n')

word_re = re.compile(r"[A-Za-zÄÖÜäöüß0-9]+(?:['’\-][A-Za-zÄÖÜäöüß0-9]+)*")

def wc(s: str) -> int:
    return len(word_re.findall(s))

chapter = 'Vorsatz'
rows = []
for i,p in enumerate(paras):
    t=p.strip()
    if t.startswith('## '): chapter=t[3:]
    rows.append((i,chapter,p))

patterns = {
    'Daniel wusste': r'^Daniel wusste\b',
    'Er wusste': r'^Er wusste\b',
    'Daniel merkte': r'^Daniel merkte\b',
    'Er merkte': r'^Er merkte\b',
    'Daniel sah': r'^Daniel sah\b',
    'Er sah': r'^Er sah\b',
    'Daniel dachte': r'^Daniel dachte\b',
    'Er dachte': r'^Er dachte\b',
    'Daniel ließ': r'^Daniel ließ\b',
    'Er ließ': r'^Er ließ\b',
    'Das war': r'^Das war\b',
    'Das machte': r'^Das machte\b',
    'Das reichte': r'^Das reichte\b',
    'Genau das': r'^Genau das\b',
    'Nicht weil': r'^Nicht weil\b',
    'Nicht X (Absatzstart)': r'^Nicht\b',
    'Der Satz': r'^Der Satz\b',
}

print('=== PATTERN COUNTS ===')
for name,pat in patterns.items():
    hits=[(i,ch,p) for i,ch,p in rows if re.search(pat,p.strip())]
    print(f'{name}: {len(hits)}')

# Detect the signature antithesis: short X. / Nicht Y. or Nicht X. / Y.
short_ant=[]
for j,(i,ch,p) in enumerate(rows):
    if wc(p)<=10 and p.strip().startswith('Nicht '):
        prev = rows[j-1][2].strip() if j else ''
        nxt = rows[j+1][2].strip() if j+1<len(rows) else ''
        if (prev and wc(prev)<=12) or (nxt and wc(nxt)<=12):
            short_ant.append((i,ch,p,prev,nxt))
print(f'SHORT_NOT_ANTITHESIS: {len(short_ant)}')

# Print selected contexts for the most reusable formulas.
for label, pat in [
    ('DANIEL_MERKTE', r'^Daniel merkte\b'),
    ('DANIEL_WUSSTE', r'^Daniel wusste\b'),
    ('DAS_WAR', r'^Das war\b'),
    ('GENAU_DAS', r'^Genau das\b'),
    ('DER_SATZ', r'^Der Satz\b'),
]:
    print(f'\n=== {label} CONTEXTS ===')
    hits=[k for k,(i,ch,p) in enumerate(rows) if re.search(pat,p.strip())]
    for n,k in enumerate(hits,1):
        i,ch,p=rows[k]
        lo=max(0,k-1); hi=min(len(rows),k+2)
        print(f'\n-- {label} {n:02d} | CH {ch} | PARA {i} --')
        for _,_,x in rows[lo:hi]:
            print(x.replace('\n',' / '))

print('\n=== SHORT NOT ANTITHESIS SAMPLE ===')
# Balanced sample, max 3/chapter, up to 60.
per=defaultdict(int); shown=0
for i,ch,p,prev,nxt in short_ant:
    if per[ch]>=3: continue
    per[ch]+=1; shown+=1
    print(f'\n-- NOT {shown:02d} | CH {ch} | PARA {i} --')
    if prev: print(prev.replace('\n',' / '))
    print(p.replace('\n',' / '))
    if nxt: print(nxt.replace('\n',' / '))
    if shown>=60: break

# Heller ambiguity: paragraphs in the reversal/finale area where motive/intent/evidence is framed.
print('\n=== HELLER AMBIGUITY CONTEXTS ===')
keywords = re.compile(r'(?i)Heller|Motiv|Absicht|wollte|Projekt|Reform|Vorprüfung|Manipulat|Quelle|Beweis|Erklärung|warum|Entscheidungsverhalten|steuern')
heller_chapters={str(i) for i in range(34,44)}
selected=[]
for k,(i,ch,p) in enumerate(rows):
    if ch in heller_chapters and keywords.search(p):
        # keep paragraphs especially likely to explain or delimit interpretation
        score=0
        low=p.lower()
        for token in ['heller','motiv','wollte','projekt','reform','vorprüfung','manipulat','quelle','beweis','erklärung','warum','entscheid']:
            score += low.count(token)
        selected.append((score,k))
selected.sort(reverse=True)
used=[]
for score,k in selected:
    if any(abs(k-u)<3 for u in used): continue
    used.append(k)
    i,ch,p=rows[k]
    print(f'\n-- HELLER | CH {ch} | PARA {i} | SCORE {score} --')
    for _,_,x in rows[max(0,k-2):min(len(rows),k+3)]:
        print(x.replace('\n',' / '))
    if len(used)>=35: break

# Key prose-variance scenes: give sentence/paragraph metrics and the most staccato + longest paragraphs.
key_chapters=['6','13','19','24','30','34','35','40','41','42','43','45','46','47']
print('\n=== KEY CHAPTER PROSE VARIANCE ===')
for ch in key_chapters:
    ps=[p for _,c,p in rows if c==ch and p.strip() and not p.strip().startswith('## ')]
    lens=[wc(p) for p in ps]
    tiny=sum(x<=5 for x in lens)
    long=sum(x>=35 for x in lens)
    dialogue=sum(p.strip().startswith('„') for p in ps)
    print(f'CH {ch}: paras={len(ps)} tiny<=5={tiny} ({tiny/len(ps):.1%}) long>=35={long} ({long/len(ps):.1%}) dialogue_start={dialogue} ({dialogue/len(ps):.1%})')
    # show three longest prose paragraphs excluding pure dialogue
    prose=[(wc(p),p) for p in ps if not p.strip().startswith('„')]
    prose.sort(reverse=True,key=lambda x:x[0])
    for n,(ln,p) in enumerate(prose[:3],1):
        print(f'  LONG{n} {ln}w: {p.replace(chr(10)," / ")[:500]}')

print('\nAUDIT_DONE')

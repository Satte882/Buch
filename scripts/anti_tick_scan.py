from pathlib import Path
import re
from collections import Counter, defaultdict

FILES = [
    Path('MANUSKRIPT/01_BAUSTEINE_01_02.md'),
    Path('MANUSKRIPT/02_BAUSTEINE_03_04.md'),
    Path('MANUSKRIPT/03_BAUSTEINE_05_06.md'),
    Path('MANUSKRIPT/04_BAUSTEIN_07.md'),
    Path('MANUSKRIPT/05_BAUSTEINE_08_09.md'),
]

SOFTENERS = {
    'vielleicht': r'\bvielleicht\b',
    'schien*': r'\bschien(?:en)?\b|\bscheint\b|\bscheinen\b',
    'wirkte*': r'\bwirkte(?:n)?\b|\bwirkt\b|\bwirken\b',
    'könnte*': r'\bkönnte(?:n)?\b',
    'offenbar': r'\boffenbar\b',
    'vermutlich': r'\bvermutlich\b',
    'möglicherweise': r'\bmöglicherweise\b',
    'zumindest': r'\bzumindest\b',
    'soweit': r'\bsoweit\b',
    'nicht ganz': r'\bnicht ganz\b',
    'nicht eindeutig': r'\bnicht eindeutig\b',
}
CHOREO = [
    'lehnte sich zurück', 'lehnte sich vor', 'sah auf', 'blickte auf', 'sah ihn an',
    'sah sie an', 'atmete durch', 'hielt inne', 'ließ den Satz stehen',
    'öffnete die Datei', 'schloss die Datei', 'schob die Datei', 'nahm den Stift',
    'legte den Stift', 'zog den Stift', 'nickte langsam', 'schwieg kurz'
]

heading = re.compile(r'^##\s+(Prolog|\d+)\s*$')
word_re = re.compile(r"\b[\wÄÖÜäöüß]+(?:[-’'][\wÄÖÜäöüß]+)*\b")

chapters = {}
chapter_file = {}
for path in FILES:
    text = path.read_text(encoding='utf-8')
    current = None
    buf = []
    for line in text.splitlines():
        m = heading.match(line.strip())
        if m:
            if current is not None:
                chapters[current] = '\n'.join(buf).strip()
                chapter_file[current] = str(path)
            current = m.group(1)
            buf = []
        elif current is not None:
            if line.strip() == '---':
                continue
            buf.append(line)
    if current is not None:
        chapters[current] = '\n'.join(buf).strip()
        chapter_file[current] = str(path)

order = ['Prolog'] + [str(i) for i in range(1,48)]
assert all(c in chapters for c in order), [c for c in order if c not in chapters]

def paras(text):
    return [p.strip().replace('\n',' ') for p in re.split(r'\n\s*\n', text) if p.strip()]

def wc(s): return len(word_re.findall(s))

def clean(s, n=180):
    s = re.sub(r'\s+', ' ', s).strip()
    return s if len(s) <= n else s[:n-1] + '…'

rows=[]
soft_totals=Counter()
choreo_totals=Counter()
short_runs=[]
neg_runs=[]
soft_windows=[]

for c in order:
    text=chapters[c]
    ps=paras(text)
    words=max(wc(text),1)
    counts={k: len(re.findall(rx,text,re.I)) for k,rx in SOFTENERS.items()}
    soft_totals.update(counts)
    soft_sum=sum(counts.values())
    density=soft_sum*1000/words
    rows.append((c,words,soft_sum,density))

    # context for softeners, only dense/clustered paragraphs
    for i,p in enumerate(ps):
        hits=[]
        for k,rx in SOFTENERS.items():
            n=len(re.findall(rx,p,re.I))
            if n: hits.extend([k]*n)
        if len(hits)>=2:
            soft_windows.append((len(hits),c,i,hits,clean(p,240)))

    # runs of 3+ very short paragraphs; markdown emphasis lines excluded
    i=0
    while i<len(ps):
        if wc(ps[i])<=8 and not ps[i].startswith('**'):
            j=i
            while j<len(ps) and wc(ps[j])<=8 and not ps[j].startswith('**'):
                j+=1
            if j-i>=3:
                snippet=' / '.join(clean(x,80) for x in ps[i:min(j,i+6)])
                short_runs.append((j-i,c,i,snippet))
            i=j
        else: i+=1

    # consecutive negation/opening fragments
    i=0
    while i<len(ps):
        if re.match(r'^(Nicht|Kein|Keine|Keiner|Nichts)\b',ps[i],re.I) and wc(ps[i])<=14:
            j=i
            while j<len(ps) and re.match(r'^(Nicht|Kein|Keine|Keiner|Nichts)\b',ps[j],re.I) and wc(ps[j])<=14:
                j+=1
            if j-i>=2:
                neg_runs.append((j-i,c,i,' / '.join(clean(x,100) for x in ps[i:j])))
            i=j
        else: i+=1

    low=text.lower()
    for phrase in CHOREO:
        n=low.count(phrase)
        if n: choreo_totals[phrase]+=n

out=[]
out.append('# TEMP – Anti-Tick-Scan')
out.append('')
out.append('Automatischer Vollscan über die fünf kanonischen Manuskriptdateien. **Nur Diagnose, keine automatische Änderungsentscheidung.**')
out.append('')
out.append('## Gesamtzahlen Weichmacher')
out.append('')
for k,n in soft_totals.most_common(): out.append(f'- `{k}`: {n}')
out.append('')
out.append('## Kapitel mit höchster Weichmacher-Dichte')
out.append('')
out.append('| Kapitel | Wörter | Treffer | pro 1.000 Wörter |')
out.append('|---|---:|---:|---:|')
for c,w,n,d in sorted(rows,key=lambda x:x[3],reverse=True)[:20]: out.append(f'| {c} | {w} | {n} | {d:.2f} |')
out.append('')
out.append('## Stärkste Weichmacher-Cluster (2+ im selben Absatz)')
out.append('')
for n,c,i,h,s in sorted(soft_windows,reverse=True)[:35]:
    out.append(f'- **K{c} · {n} Treffer · {", ".join(h)}:** {s}')
out.append('')
out.append('## Längste Kurzabsatz-Ketten (3+ Absätze mit <=8 Wörtern)')
out.append('')
for n,c,i,s in sorted(short_runs,reverse=True)[:45]: out.append(f'- **K{c} · {n} Absätze:** {s}')
out.append('')
out.append('## Negationsketten')
out.append('')
for n,c,i,s in sorted(neg_runs,reverse=True)[:45]: out.append(f'- **K{c} · {n} Absätze:** {s}')
out.append('')
out.append('## Wiederkehrende Choreografie – Gesamtmanuskript')
out.append('')
for k,n in choreo_totals.most_common(): out.append(f'- `{k}`: {n}')
out.append('')
out.append('## Vollständige Kapitelübersicht')
out.append('')
out.append('| Kapitel | Wörter | Weichmacher | pro 1.000 Wörter |')
out.append('|---|---:|---:|---:|')
for c,w,n,d in rows: out.append(f'| {c} | {w} | {n} | {d:.2f} |')

Path('ANTI_TICK_SCAN_TEMP.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
print(f'chapters={len(order)} short_runs={len(short_runs)} neg_runs={len(neg_runs)} clusters={len(soft_windows)}')

from pathlib import Path
import re

FILES=[Path('MANUSKRIPT/01_BAUSTEINE_01_02.md'),Path('MANUSKRIPT/02_BAUSTEINE_03_04.md'),Path('MANUSKRIPT/03_BAUSTEINE_05_06.md'),Path('MANUSKRIPT/04_BAUSTEIN_07.md'),Path('MANUSKRIPT/05_BAUSTEINE_08_09.md')]
SOFT=r'\b(vielleicht|offenbar|vermutlich|möglicherweise|zumindest|soweit|schien|schienen|scheint|scheinen|wirkte|wirkten|wirkt|wirken|könnte|könnten)\b|\bnicht ganz\b|\bnicht eindeutig\b'
heading=re.compile(r'^##\s+(Prolog|\d+)\s*$')
word=re.compile(r"\b[\wÄÖÜäöüß]+(?:[-’'][\wÄÖÜäöüß]+)*\b")
chapters={}
for path in FILES:
    cur=None; buf=[]
    for line in path.read_text(encoding='utf-8').splitlines():
        m=heading.match(line.strip())
        if m:
            if cur is not None: chapters[cur]='\n'.join(buf).strip()
            cur=m.group(1); buf=[]
        elif cur is not None and line.strip()!='---': buf.append(line)
    if cur is not None: chapters[cur]='\n'.join(buf).strip()
order=['Prolog']+[str(i) for i in range(1,48)]

def wc(s): return len(word.findall(s))
def clean(s,n=300):
    s=re.sub(r'\s+',' ',s).strip()
    return s if len(s)<=n else s[:n-1]+'…'
def paras(t): return [p.strip().replace('\n',' ') for p in re.split(r'\n\s*\n',t) if p.strip()]
def prose(p): return not p.startswith(('„','“','**','#')) and not re.match(r'^\*[^*]+\*$',p)

out=['# TEMP – Anti-Tick Detail Scan','', 'Kontextscan. Keine automatische Änderungsentscheidung.','']
out.append('## Weichmacher – jeder betroffene Absatz')
out.append('')
for c in order:
    hits=[]
    for p in paras(chapters[c]):
        ms=list(re.finditer(SOFT,p,re.I))
        if ms:
            labels=', '.join(m.group(0) for m in ms)
            hits.append(f'- `{labels}` — {clean(p)}')
    if hits:
        out.append(f'### K{c}')
        out.extend(hits)
        out.append('')

out.append('## Reine Prosa-Stakkato-Ketten')
out.append('')
for c in order:
    ps=paras(chapters[c]); i=0
    while i<len(ps):
        if prose(ps[i]) and wc(ps[i])<=9:
            j=i
            while j<len(ps) and prose(ps[j]) and wc(ps[j])<=9: j+=1
            if j-i>=3:
                out.append(f'- **K{c} · {j-i} Absätze:** '+' / '.join(clean(x,100) for x in ps[i:j]))
            i=j
        else: i+=1

out.append('')
out.append('## Erklärmarker nach starken Beats')
out.append('')
markers=re.compile(r'^(Das war|Das bedeutete|Genau das|Der Unterschied|Deshalb|Darum|Die Aufgabe war|Die Frage war|Der Punkt war|Mehr war|Damit war)',re.I)
for c in order:
    for p in paras(chapters[c]):
        if prose(p) and markers.search(p): out.append(f'- **K{c}:** {clean(p)}')

Path('ANTI_TICK_DETAIL_TEMP.md').write_text('\n'.join(out)+'\n',encoding='utf-8')
print('detail scan written')

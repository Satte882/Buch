from pathlib import Path
p=Path('AUSNAHMEZUSTAND_FINAL.md')
t=p.read_text(encoding='utf-8')
old='''Mara schwieg kurz.\n\nDaniel merkte, dass er sich schon erklären wollte.\n\nTat er nicht.'''
new='''Mara schwieg kurz.\n\nDie Erklärung stand schon bereit. Er sagte sie nicht.'''
assert t.count(old)==1, t.count(old)
t=t.replace(old,new,1)
assert t.rstrip().endswith('„Wie belastbar ist deine Gegenhypothese?“')
assert '—' not in t
p.write_text(t,encoding='utf-8')
print('FINAL_STYLE_FIX_OK')

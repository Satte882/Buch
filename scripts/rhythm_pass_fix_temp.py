from pathlib import Path

path = Path('AUSNAHMEZUSTAND_FINAL.md')
text = path.read_text(encoding='utf-8')
old = 'Daniel ließ das Vielleicht stehen.\n\nDaniel strich das Wort nicht weg.\n\nEs war unbequem, weil es weder Entlastung noch Anklage lieferte.'
new = 'Daniel ließ das Vielleicht stehen.\n\nEs war unbequem, weil es weder Entlastung noch Anklage lieferte.'
if text.count(old) != 1:
    raise SystemExit(f'Expected one duplicate rhythm passage, found {text.count(old)}')
text = text.replace(old, new)
if not text.rstrip().endswith('„Wie belastbar ist deine Gegenhypothese?“'):
    raise SystemExit('Final line changed unexpectedly')
path.write_text(text, encoding='utf-8')
print('Removed one redundant post-rhythm sentence; final line unchanged.')

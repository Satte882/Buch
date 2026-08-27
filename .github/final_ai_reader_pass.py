from pathlib import Path
import re

p_mid = Path('MANUSKRIPT/03_BAUSTEINE_05_06.md')
t = p_mid.read_text(encoding='utf-8')

def rep(label, old, new):
    global t
    c=t.count(old)
    if c != 1:
        raise SystemExit(f'{label}: expected 1 match, got {c}')
    t=t.replace(old,new,1)

# K27: one visible separation is enough; remove repeated self-explanation.
rep('K27 repeated private-pressure explanation', '''Damit war der Druck nicht weg.\n\nEr hatte nur einen Zeugen dafür, dass Daniel ihn nicht heimlich in Evidenz verwandeln durfte.\n\nNicht, dass die behauptete größere Gefahr stimmte.\n\nNicht, dass Jana Ziel war.\n\nNicht, dass beides zusammenhing.\n\nDaniel sagte sich das einmal.\n\nDann noch einmal, weil sein Körper die Information offenbar nicht gelesen hatte.\n\nSein Nacken war hart. Er stand noch immer.\n\n„Freigabe existiert“, sagte Jonas.''', '''Damit war der Druck nicht weg.\n\nEr hatte nur einen Zeugen dafür, dass Daniel ihn nicht heimlich in Evidenz verwandeln durfte.\n\n„Freigabe existiert“, sagte Jonas.''')

rep('K27 repeated taxonomy', '''Jonas markierte die Kennung im Arbeitsstand als **bestätigt**, die Bedeutung als **offen**.\n\nDaniel sah auf die zwei Wörter.\n\nSo hatte er nach dem Betriebshof begonnen zu arbeiten.\n\nBestätigt.\n\nOffen.\n\nWiderlegt.\n\nDer Jana-Satz passte in keine der drei Kategorien, weil er eine andere Frage beantwortete.\n\nDaniel schrieb selbst daneben:\n\n**Privatwissen bestätigt keine Gefahrenannahme.**\n\nJonas sah zu ihm.\n\n„Was?“\n\nDaniel zeigte ihm jetzt auch die letzte Zeile.''', '''Jonas markierte die Kennung im Arbeitsstand als **bestätigt**, die Bedeutung als **offen**.\n\nDaniel zeigte ihm jetzt auch die letzte Zeile.''')

# K29: keep the moral balance, remove the second checklist demonstration.
rep('K29 duplicated cost-benefit worksheet', '''Daniel zog ein Blatt quer vor sich und schrieb zwei Überschriften.\n\n**Was die breite Prüfung bereits gekostet hat.**\n\n**Was die breite Prüfung bereits gebracht hat.**\n\nUnter die erste schrieb er Weber. Fehlzuordnung. Arbeitgeberreaktion. Nachlauf trotz Korrektur.\n\nUnter die zweite den Aushilfsfahrer, den Lagerraum, den gestoppten Vorbereitungsschritt.\n\nDann ließ er beide Spalten offen.\n\n„Was soll das werden?“, fragte Berg.\n\n„Die Begründung, bevor wir wissen, ob der nächste Treffer gut oder schlecht ist.“\n\nLena sah auf das Blatt.\n\n„Dann schreib bei der ersten auch Erklärungsarbeit für Unbeteiligte.“\n\nDaniel tat es.\n\nJonas sagte: „Und bei der zweiten, dass wir den Lagerraum wahrscheinlich später oder gar nicht gesehen hätten.“\n\nDaniel schrieb **Zeitgewinn wahrscheinlich**, nicht **verhindert**.\n\nDie Formulierung ärgerte Berg nicht. Das war gut.''', '''Daniel schrieb Weber und den Lagerraum nebeneinander. Beim einen: Fehlzuordnung, Arbeitgeberreaktion, Nachlauf. Beim anderen: realer Gefahrenstrang, wahrscheinlich früher sichtbar durch den breiten Kreis.\n\nKein Erfolgs- oder Fehlschlagslabel.''')

# K31: independent origin remains, but the question loop no longer has to be replayed.
rep('K31 repeated independent-origin loop', '''Daniel ließ auch die Standortangabe noch einmal gegenprüfen.\n\nJonas sah ihn an.\n\n„Die Kontrolle ist dokumentiert.“\n\n„Ich weiß.“\n\n„Foto passt. Uhrzeit passt.“\n\n„Ich weiß.“\n\n„Was genau soll ich noch prüfen?“\n\n„Ob der Standort aus der Kontrolle stammt oder später aus einem übernommenen Datensatz.“\n\nJonas atmete hörbar aus, machte es aber.\n\nDie Antwort kam wenige Minuten später: ursprünglicher Kontrollvorgang, Zeit und Ort direkt dort erfasst. Keine spätere Zuordnung aus Daniels Projekt.\n\n„Unabhängig genug?“ fragte Jonas.\n\n„Für diesen Punkt ja.“\n\nDaniel markierte ihn entsprechend.''', '''Jonas bestätigte aus dem ursprünglichen Kontrollvorgang, dass Zeit und Ort nicht später aus Daniels Projekt übernommen worden waren. Daniel ließ den Punkt stehen.''')

p_mid.write_text(t, encoding='utf-8')

p_fin = Path('MANUSKRIPT/05_BAUSTEINE_08_09.md')
f = p_fin.read_text(encoding='utf-8')

def repf(label, old, new):
    global f
    c=f.count(old)
    if c != 1:
        raise SystemExit(f'{label}: expected 1 match, got {c}')
    f=f.replace(old,new,1)

# K40: alternatives are already established; final seconds stop explaining and accelerate.
repf('K40 pre-shot rhythm', '''Heller sah kurz auf das Display.\n\nDaniel hörte seinen eigenen Atem lauter als den Funk.\n\nKeine der Alternativen verschwand.\n\nSie liefen nur gleichzeitig aus derselben Sekunde heraus.\n\nDann bewegte Heller den Daumen.\n\nVielleicht hätte es gereicht.\n\nVielleicht hätte Heller nur den Daumen bewegen müssen.\n\nDaniel wusste nicht, welche Möglichkeit wahrscheinlicher war.\n\nEr wusste nur, dass beide real waren.\n\nHeller bewegte den Daumen.\n\nDaniel zog die Waffe. Sein Unterarm war hart bis in die Finger. Er merkte es erst, als Heller schon fiel.\n\nJetzt lag Heller vor ihm.''', '''Heller sah kurz auf das Display.\n\nDaniel hörte seinen eigenen Atem lauter als den Funk.\n\nHellers Daumen bewegte sich.\n\nDaniel zog die Waffe.\n\nDer Knall.\n\nJetzt lag Heller vor ihm.''')

# K44: one bodily remainder, no explanation and no new event.
repf('K44 bodily echo', '''Daniel las die Zeilen zweimal.\n\n„Wer ist die zweite Freigabe?“''', '''Daniel las die Zeilen zweimal.\n\nEr merkte erst beim Umblättern, wie fest er den Stift hielt. Er lockerte die Finger und las weiter.\n\n„Wer ist die zweite Freigabe?“''')

p_fin.write_text(f, encoding='utf-8')

# Structural / story guards.
for path, expected in [(p_mid, [str(i) for i in range(19,34)]), (p_fin, [str(i) for i in range(38,48)])]:
    txt=path.read_text(encoding='utf-8')
    heads=re.findall(r'^##\s+(\d+)\s*$', txt, re.M)
    if heads != expected:
        raise SystemExit(f'chapter structure changed in {path}: {heads}')

mid=p_mid.read_text(encoding='utf-8')
fin=p_fin.read_text(encoding='utf-8')
for needle in [
    '18.32 Uhr. Ihre Schwester hat die Praxis über den Hinterausgang verlassen.',
    'Keine automatische Fortführung nach Wegfall der akuten fallbezogenen Grundlage.',
    'Im Moment meinte er jedes Wort.',
    'Dr. Lena Vogt.',
    'Entscheidung zur vorläufigen Fortführung: Reuter.',
]:
    if needle not in mid:
        raise SystemExit(f'missing protected midpoint/turning-point anchor: {needle}')
for needle in [
    'Er griff Daniel nicht an.',
    'Nicht gesendet.',
    'Drei Meter.',
    'Hellers Manipulation.',
    'Wie belastbar ist deine Gegenhypothese?',
]:
    if needle not in fin:
        raise SystemExit(f'missing protected finale/end anchor: {needle}')

# No direct duplicate paragraphs introduced in edited source files.
for path in [p_mid,p_fin]:
    paras=[x.strip() for x in path.read_text(encoding='utf-8').split('\n\n') if x.strip() and not x.strip().startswith('##') and x.strip()!='---']
    for a,b in zip(paras, paras[1:]):
        if a==b and len(a)>30:
            raise SystemExit(f'direct duplicate in {path}: {a[:80]}')

# Rebuild consolidated final manuscript from the five canonical sources.
sources=[
    Path('MANUSKRIPT/01_BAUSTEINE_01_02.md'),
    Path('MANUSKRIPT/02_BAUSTEINE_03_04.md'),
    Path('MANUSKRIPT/03_BAUSTEINE_05_06.md'),
    Path('MANUSKRIPT/04_BAUSTEIN_07.md'),
    Path('MANUSKRIPT/05_BAUSTEINE_08_09.md'),
]
parts=[]
for i,p in enumerate(sources):
    s=p.read_text(encoding='utf-8').strip()
    if i>0:
        lines=s.splitlines()
        if lines and lines[0].startswith('# Manuskript'):
            s='\n'.join(lines[1:]).lstrip()
    parts.append(s)
final='\n\n'.join(parts).rstrip()+'\n'
Path('AUSNAHMEZUSTAND_FINAL.md').write_text(final, encoding='utf-8')

heads=re.findall(r'^##\s+(Prolog|\d+)\s*$', final, re.M)
if heads != ['Prolog']+[str(i) for i in range(1,48)]:
    raise SystemExit(f'final chapter sequence invalid: {heads}')
for needle in ['Nicht gesendet.','Entscheidung zur vorläufigen Fortführung: Reuter.','Wie belastbar ist deine Gegenhypothese?']:
    if needle not in final:
        raise SystemExit(f'final missing invariant: {needle}')
print('final AI reader-pass applied and consolidated manuscript rebuilt')

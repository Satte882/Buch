from pathlib import Path

p = Path('MANUSKRIPT/03_BAUSTEINE_05_06.md')
t = p.read_text(encoding='utf-8')


def replace_range(label, start, end, replacement, include_end=False):
    global t
    if t.count(start) != 1:
        raise SystemExit(f'{label}: start count={t.count(start)}')
    a = t.index(start)
    b = t.find(end, a + len(start))
    if b < 0:
        raise SystemExit(f'{label}: end not found')
    if include_end:
        b += len(end)
    t = t[:a] + replacement + t[b:]

# K20: redundant second Lena/control loop after the apparent scene close.
replace_range(
    'K20 second control loop',
    'Daniel sah auf den Weg **getrennte Bewertung**.\n\nLena hatte ihm nicht nur Information vorenthalten.',
    '\n\n---\n\n## 21',
    '',
)

# K21: let Heller's sentence land without authorial interpretation.
block = 'Heller sagte nicht mehr.\n\nKeine Geschichte. Keine Namen. Kein moralischer Schluss.\n\nNur dieser Satz.\n\n'
if t.count(block) != 1:
    raise SystemExit(f'K21 Heller commentary count={t.count(block)}')
t = t.replace(block, '', 1)

# K21: one everyday demonstration of the project structure is enough.
replace_range(
    'K21 repeated project demonstration',
    '„Was spart uns das konkret?“, fragte Daniel.',
    '„Ich will die Struktur“, sagte Daniel.',
    '',
)
replace_range(
    'K21 repeated closing comparison',
    'Daniel sah noch einmal auf den Vergleich, den Jonas eben geöffnet hatte.',
    '\n\n---\n\n## 22',
    '',
)

# K22: end on action, not an interpretation of the relationship.
replace_range(
    'K22 interpretive ending',
    'Mara brauchte ihn für ihre nächsten Schritte nicht mehr.',
    '\n\n---\n\n## 23',
    '',
)

# K23: compress the first parade of banal false hits.
replace_range(
    'K23 false-hit parade',
    'Auf dem zweiten Bildschirm liefen die übrigen Treffer aus der neuen Projektstruktur ein.',
    'Die Liste wurde länger, bevor sie kürzer wurde.',
    'Auf dem zweiten Bildschirm liefen die übrigen Treffer aus der neuen Projektstruktur ein.\n\nDie meisten zerfielen schnell: Schreibvarianten, gemeinsam genutzte Bereitschaftsgeräte, verspätete Synchronisierung, legitime Schichten und reguläre Fahrzeuge. Jonas strich sie weg. Die Liste wurde länger, bevor sie kürzer wurde.',
    include_end=True,
)

# K23: keep equal criteria and Weber's unresolved weight, remove repeated proof rounds.
replace_range(
    'K23 repeated criteria proof',
    'Die nächsten zwei Stunden brachten fast nichts.',
    'Die Methode funktionierte nur, wenn ein Treffer auch wieder kleiner werden durfte.',
    'Die nächsten zwei Stunden erklärten fast alle übrigen Treffer. Weber blieb offen. Daniel zog ihn trotzdem aus der obersten Zeile: relatives Auffallen war kein zusätzlicher Treffer.\n\nFür jeden im Prüfkreis galten dieselben vier Punkte: aktueller Zeitbezug, funktionaler Zugang, unabhängige zweite Verbindung, harmlose Erklärung noch offen oder widerlegt. Bei Weber waren zwei stark, zwei offen.\n\n„Damit ist Weber weiter vorne“, sagte Jonas.\n\n„Ja. Aber wegen derselben Kriterien wie alle anderen.“\n\nLena sah die Liste durch. „Und was passiert bei einem Treffer?“\n\n„Nichts automatisch.“',
    include_end=True,
)

# K24: preserve Weber's real consequences; shorten Daniel's post-hoc methodology lecture.
replace_range(
    'K24 post-Weber analysis',
    'Daniel hörte Ahrens in dem Satz wieder.',
    'Er suchte nach der Form seiner eigenen Fehlentscheidung.',
    'Nach dem Gespräch zog Daniel die Zeitlinie zurück. Diensthandy. Nachtzugang. Schichtübersicht. Bei jedem Punkt hatte es eine harmlose Gegenlesart gegeben. Er hatte sie gesehen. Nur weniger schwer gewichtet, je realer die Gefahr des Nicht-Handelns geworden war.\n\nDer breite Prüfkreis hatte real funktioniert. Weber war trotzdem falsch belastet worden. Beides blieb wahr.\n\nDer Fehler lag nicht in einer fehlenden Gegenhypothese. Er lag darin, was sie in Daniels Rechnung noch wert gewesen war.\n\nNeben zwei frühen **offen**-Markierungen schrieb er: **Gegenlesart vorhanden, Gewicht im Verlauf gesunken. Warum?**\n\nLena las über seine Schulter.\n\n„Das ist die bessere Frage.“\n\nDaniel nickte.',
    include_end=True,
)

# K25: once Jana confirms the chronology, arrive faster at the midpoint question.
replace_range(
    'K25 midpoint over-explanation',
    'Er markierte keine Verbindung als bewiesen, die nicht bewiesen war.',
    'Nicht: Wer kannte den Fall?',
    'Die alte Erklärung passte nicht mehr: Die Quelle reagierte nicht erst auf Daniel, nachdem er im Fall wichtig geworden war. Der Privatbezug lag vor der dokumentierten Fallzuweisung.\n\nDas bewies keine Auswahl. Jemand konnte ihn aus einem anderen Grund beobachtet, die Uhrzeit rekonstruiert oder viele Menschen im Blick gehabt haben. Aber Daniel musste eine zweite Möglichkeit zulassen: Jemand hatte schon vorher einen Grund gehabt, sein Verhalten interessant zu finden.\n\nEr schrieb zwei Fragen auf:\n\n**Wer konnte mich vorher beruflich einschätzen?**\n\n**Wer konnte vor der Fallzuweisung erwarten, dass ich relevant werden würde?**\n\nDanach nur einen Vermerk:\n\n**Privatbezug zeitlich vor Zuweisung Lagerkomplex. Auswahlzeitpunkt prüfen.**\n\nEr öffnete keine Personalakten und keine Namenslisten. Späterer Zugang durfte niemanden rückwirkend zum Vor-Fall-Kandidaten machen.\n\nDie neue Chronologie änderte keinen operativen Fakt. Mika blieb beteiligt. Der breite Prüfkreis hatte real funktioniert. Weber war falsch belastet worden. Die Quelle hatte echte Informationen geliefert.\n\nNur Daniels Platz darin hatte sich verschoben.\n\nNicht: Wer kannte den Fall?',
)

# K26: keep the formal return boundary and explicit commitment, remove repeated proof that he means it.
replace_range(
    'K26 repeated self-binding proof',
    'Daniel sah den Versandstatus.\n\nDamit war es keine Notiz mehr, die er später anders erinnern konnte.',
    'Lena nickte einmal.\n\nKeine Anerkennung. Nur Registrierung.',
    'Der Versandstatus sprang nacheinander um. Berg: gelesen. Kontrollfunktion: zugestellt. Lena: im Raum. Damit war die Grenze nicht mehr nur seine Absicht.\n\n„Wenn ich morgen gute Gründe habe?“, fragte Daniel.\n\n„Dann musst du sie gegen deine eigene Grenze begründen. Nicht so tun, als hätte es die Grenze nie gegeben.“\n\nDaniel nickte.\n\n„Ist das eine Zusage?“, fragte Lena.\n\n„Ja.“\n\n„Auch wenn die Struktur bis dahin noch einmal funktioniert?“\n\nDaniel sah auf den Vermerk. „Wenn die akute Grundlage weg ist, begründen wir neu.“\n\nLena nickte einmal.',
    include_end=True,
)
replace_range(
    'K26 repeated closing reread',
    'Daniel blieb allein mit dem Projektvermerk.',
    '\n\n---\n\n## 27',
    'Daniel blieb allein mit dem Projektvermerk.\n\nIm Moment meinte er jedes Wort.',
)

# Structural and protected-content validation.
for ch in range(19, 28):
    if t.count(f'## {ch}\n') != 1:
        raise SystemExit(f'chapter {ch} structure changed')

must = [
    'Es waren trotzdem Menschen tot.',
    'Dann geh ans Telefon.',
    'Das Diensthandy war nicht bei Weber.',
    'Mein Sohn hat gestern gefragt',
    'Wer kannte ihn?',
    'bevor Daniel selbst wusste, dass es einen Fall gab?',
    'Keine automatische Fortführung nach Wegfall der akuten fallbezogenen Grundlage.',
    'Sonderentscheidungen und Ausweitungen werden nach Abschluss unabhängig geprüft',
    'Im Moment meinte er jedes Wort.',
    '18.32 Uhr. Ihre Schwester hat die Praxis über den Hinterausgang verlassen.',
]
for needle in must:
    if needle not in t:
        raise SystemExit(f'protected anchor lost: {needle}')

p.write_text(t, encoding='utf-8')
print('PASS middle reader-pass patch')

from pathlib import Path
import re

F1 = Path('MANUSKRIPT/01_BAUSTEINE_01_02.md')
F2 = Path('MANUSKRIPT/02_BAUSTEINE_03_04.md')

def exact(text, old, new, label):
    n = text.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected 1 exact match, found {n}')
    return text.replace(old, new, 1)

def regex1(text, pattern, repl, label, flags=re.S):
    new, n = re.subn(pattern, repl, text, count=1, flags=flags)
    if n != 1:
        raise SystemExit(f'{label}: expected 1 regex match, found {n}')
    return new

f1 = F1.read_text(encoding='utf-8')
f2 = F2.read_text(encoding='utf-8')

# K1 – Daniel soll die Methode zeigen, nicht zweimal erklären.
f1 = exact(f1,
'''Daniel kannte den Impuls. Es gab einen Punkt in fast jeder Prüfung, an dem eine Geschichte begann, sich selbst zu helfen. Aus einem Foto wurde Ausspähung. Aus einer Frage wurde Interesse am Nachtbetrieb. Aus einem zweiten Vorbeifahren wurde Rückkehr zum Ziel.\n\nManchmal war genau diese Geschichte richtig.\n\nDas war das Unangenehme daran.\n\n''',
'', 'K1 explizite Methodikerklärung')

f1 = exact(f1,
'''Er kannte die Rechnung. Ein falscher Eingriff hatte einen Preis, der selten in einer Lageübersicht stand. Ein unterlassener richtiger Eingriff konnte einen haben, der später überall stand.\n\nDas machte die zweite Möglichkeit nicht automatisch wahrscheinlicher.\n\n''',
'', 'K1 zweite Methodikerklärung')

# K2 – nach der echten Schließentscheidung nicht noch einmal dieselbe Lehre nacherzählen.
f1 = regex1(f1,
    r"Daniel ging zum nächsten Termin\.\n\nAls er später noch einmal in seine offene Liste sah, war Ahrens' Name verschwunden\..*?(?=\n\n---\n\n## 3)",
    'Daniel ging zum nächsten Termin.',
    'K2 Nachanalyse entdoppeln')

# K3 – Lena und die Daten zeigen Daniels Fehler bereits; den methodischen Nachunterricht kürzen.
f1 = exact(f1,
'''Daniel kannte dieses Gespräch. Nicht dieses konkrete, aber die Form. Lena widersprach selten mit einer Gegenbehauptung. Sie suchte lieber die Stelle, an der eine gute Geschichte am leichtesten zusammenbrechen konnte.\n\n''',
'', 'K3 Lena-Erklärung')

f1 = exact(f1,
'''Die reguläre Klärung dauerte knapp eine Stunde. Ein Schichtleiter der Wartungsfirma hatte den falschen Ausweis aus einem Sammelfach genommen, um liegen gelassenes Werkzeug abzuholen. Die Videoaufzeichnung zeigte ihn mit einer Werkzeugtasche hinein- und zwölf Minuten später wieder herausgehen.\n\n''',
'', 'K3 Ergebniszusammenfassung doppelt')

f1 = regex1(f1,
    r'Lena blieb noch an der Tür stehen\.\n\n„Sag mir, wo deine Geschichte gekippt ist\.“.*?„Damit kann ich arbeiten\.“\n\nSie ging\.',
    'Lena blieb noch einen Moment an der Tür.\n\n„Das ist die Arbeit“, sagte sie.\n\n„Damit kann ich arbeiten.“\n\nSie ging.',
    'K3 Nachunterricht kürzen')

# K4 – die Parallelität Briefkasten/Wohnung ist bereits gespielt; explizite These entfernen.
f1 = regex1(f1,
    r'\nDaniel merkte, dass beide Entscheidungen denselben unangenehmen Kern hatten: Beim Briefkasten ließ er etwas ungeklärt\. Bei der Wohnung ließ Jana nicht zu, dass Ungeklärtheit automatisch[^\n]*\n',
    '\n', 'K4 explizite Schlussdeutung', flags=0)

# K5 – gleicher Sachverhalt, aber als kurzer Set-up statt vierter Methodikschleife.
chapter5 = '''## 5\n\nZwölf Akkupakete für gewerbliche Funkgeräte standen in Daniels offener Liste.\n\nLieferadresse: eine Handelsfirma in Lagerhaus C, Einheit 17.\n\nJonas sah auf den Artikel. „Zwölf?“\n\n„Zwölferpack.“\n\n„Preis?“\n\n„Vierhundertachtzig netto.“\n\n„Das ist enttäuschend normal.“\n\nDaniel öffnete das Handelsregister. Technischer Groß- und Einzelhandel, Event- und Kommunikationszubehör. Geschäftsführer seit Gründung derselbe Mann. Zwei veröffentlichte Jahresabschlüsse.\n\nNichts daran war interessant.\n\nDann sah Daniel die Adresse noch einmal an.\n\nNicht den Namen. Die Adresse.\n\n„Die hatten wir schon mal.“\n\nJonas trat näher.\n\nSie fanden den alten Vorgang nach wenigen Sekunden: dieselbe Lageranlage, sieben Monate zuvor. Ein Kleintransporter mit gefälschten Zulassungspapieren hatte dort zwei Nächte gestanden. Das Verfahren war als Betrugsfall geschlossen worden. Kein Terrorbezug.\n\nDaniel öffnete den Lageplan.\n\n„Wo stand der Wagen?“\n\n„Gebäude A“, sagte Jonas.\n\nDaniel zeigte auf die aktuelle Lieferadresse. „Und das hier ist C.“\n\nDrei Gebäude. Dreiundzwanzig Einheiten. Nicht einmal derselbe Eingang.\n\n„Also ungefähr dieselbe Adresse wie ein Parkhaus“, sagte Jonas.\n\n„Ungefähr.“\n\nDaniel ließ die Firma offen prüfen. Website, Telefonnummer, Geschäftszweck, Lieferanschrift. Keine Sonderabfrage, kein Antrag, keine Beobachtung.\n\nVierzig Minuten später kam Jonas zurück.\n\n„Leider weiter langweilig.“\n\nDie Website bestand seit Jahren. Telefonnummer und Impressum passten zum Register. Der Vermieter bestätigte, dass die Firma Einheit 17 seit gut zwei Jahren nutzte und dort regelmäßig Waren annahm. Der Versender führte die Akkus als Standardlieferung. Keine Barzahlung, kein Sonderwunsch.\n\nDaniel sah noch einmal auf den alten Fahrzeugvorgang.\n\n„Andere Firma“, sagte Jonas.\n\n„Ja.“\n\n„Anderes Gebäude.“\n\n„Ja.“\n\n„Anderer Sachverhalt.“\n\n„Ja.“\n\n„Dann zu?“\n\nDaniel schloss den Firmennamen und die Bestellung. Bei der Adresse ließ er eine Freitextnotiz stehen: **Lageranlage bereits in anderem, abgeschlossenem Sachverhalt aufgetaucht; anderer Gebäudeteil, kein gemeinsamer Gefahrenbezug. Bei neuen Erkenntnissen Adressbezug mitprüfen.**\n\nDas System bot ihm mehr an. Beobachtungspunkt. Wiedervorlage. Verknüpfungsrelevant.\n\nEr wählte nichts davon.\n\nJonas las die Notiz. „Wenn nie was Neues kommt?“\n\n„Dann bleibt es ein Satz, den niemand braucht.“\n\nDaniel schloss die Maske und zog den nächsten Vorgang in die Mitte.\n\nZehn Minuten später hatte er die Lageradresse fast vergessen.\n\nNur die Markierung blieb.\n\nLagerhaus C, Einheit 17.'''

f1 = regex1(f1,
    r'## 5\n\n.*?(?=\n\n---\n\n## 6)',
    chapter5,
    'K5 Kapitel verdichten')

# K6 – dieselbe Beziehungsinformation nicht in mehreren Gesprächsschleifen erneut aushandeln.
f1 = exact(f1,
'''Er dachte an Jonas und musste kurz grinsen.\n\n''',
'', 'K6 übernutzter Jonas-Gag')

f1 = regex1(f1,
    r'Mara nahm ihr Glas und drehte es langsam zwischen den Händen\.\n\n„Ich brauche Sonntag übrigens nicht von dir, dass du schon weißt, ob Hamburg funktioniert\.“.*?Sie nahm ihren Teller wieder näher\.',
    'Mara nahm ihr Glas.\n\n„Sonntag reicht mir, wenn du dich mit mir hinsetzt, bevor meine Frist die Entscheidung für uns übernimmt.“\n\nDaniel nickte.\n\nDer Satz gefiel ihm weniger, als er sollte. Nicht weil er wollte, dass Mara absagte. Weil er begriff, dass der Termin nicht dazu da war, ihm mehr Entscheidungszeit zu geben.',
    'K6 Entscheidungsschleife kürzen')

# K8 – der private Einschlag soll vor Daniels technischer Zerlegung einmal körperlich landen.
f2 = exact(f2,
'''Die Türen schlossen sich wieder.\n\nEr las nur die erste Zeile.\n''',
'''Die Türen schlossen sich wieder.\n\nDaniel sah auf die letzte Zeile.\n\nHausflur Ihrer Mutter.\n\nSein Daumen lag noch auf der Taste. Er nahm ihn weg.\n\nDann las er die Nachricht von oben.\n''',
'K8 privater Einschlag')

# K9 – Lena hat Daniel bereits entlarvt; danach nur noch Druck benennen, nicht die ganze Methode erklären.
f2 = regex1(f2,
    r'Lena sah nicht sofort auf den Ausdruck\. Sie sah Daniel an\.\n\n„Was wäre ein schlechter Grund, es mir nicht zu zeigen\?“.*?Daniel nickte\.\n\nDamit war die Privatzeile nicht plötzlich Teil des Falls\.',
    'Lena sah Daniel an.\n\n„Beeinflusst der private Teil deine Bewertung?“\n\nDaniel sah auf die drei Spalten.\n\n„Er erhöht meinen Druck.“\n\nLena nickte.\n\n„Dann gehört genau das zu unserer Zusammenarbeit. Nicht als Beweis. Als mögliche Verzerrung deiner Schwelle.“\n\nDaniel nickte.\n\nDamit war die Privatzeile nicht plötzlich Teil des Falls.',
    'K9 Selbsterklärung nach Entlarvung kürzen')

# Sicherheitschecks: Struktur und geschützte Anker.
for text, expected in [
    (f1, ['Prolog','1','2','3','4','5','6']),
    (f2, [str(i) for i in range(7,19)]),
]:
    heads = re.findall(r'^##\s+(Prolog|\d+)\s*$', text, re.M)
    if heads != expected:
        raise SystemExit(f'chapter structure changed: {heads} != {expected}')

must = [
    (f1, 'Lagerhaus C, Einheit 17.'),
    (f1, '**Hamburg. Nicht irgendwann.**'),
    (f2, '**20.11 Uhr. Hausflur Ihrer Mutter. Sie haben das Namensschild am Briefkasten wieder festgedrückt.**'),
    (f2, 'weil unten drei Zentimeter mehr Rand sind als oben'),
]
for text, needle in must:
    if needle not in text:
        raise SystemExit(f'protected anchor missing: {needle}')

F1.write_text(f1, encoding='utf-8')
F2.write_text(f2, encoding='utf-8')
print('PASS entry reader-pass patch')

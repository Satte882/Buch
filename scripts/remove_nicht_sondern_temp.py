from pathlib import Path
import re

path = Path('AUSNAHMEZUSTAND_FINAL.md')
text = path.read_text(encoding='utf-8')

before = len(re.findall(r'\bsondern\b', text, re.I))
assert before == 38, f'expected 38 sondern occurrences, found {before}'

repls = [
    ("Vielleicht hatte die Quelle nicht die Gefahr gebaut, sondern genau diesen Moment.",
     "Vielleicht hatte die Quelle genau diesen Moment gebaut. Die Gefahr selbst konnte unabhängig davon real sein."),
    ("Eine Person verließ den Kleinbus und ging nicht zur Seiteneinfahrt, sondern zu einem Nebengebäude.",
     "Eine Person verließ den Kleinbus, ließ die Seiteneinfahrt links liegen und ging zu einem Nebengebäude."),
    ("Sein Dienstausweis lag nicht wie sonst in der Jackentasche, sondern auf dem Tisch. Er hatte ihn herausgenommen, bevor Berg gekommen war.",
     "Sein Dienstausweis lag auf dem Tisch. Sonst trug er ihn in der Jackentasche. Er hatte ihn herausgenommen, bevor Berg gekommen war."),
    ("Berg zog Daniels Vermerk wieder zu sich und schrieb oben rechts eine kurze Notiz. Nicht für Daniel, sondern für die Akte.",
     "Berg zog Daniels Vermerk wieder zu sich und schrieb oben rechts eine kurze Notiz für die Akte."),
    ("Daniel bemerkte die Datei auf ihrem Bildschirm nicht. Nur, dass sie ihre Notizen nicht in den normalen gemeinsamen Vorgang legte, sondern in einen anderen Arbeitsbereich wechselte, bevor sie den Rechner sperrte.",
     "Daniel bemerkte die Datei auf ihrem Bildschirm nicht. Nur, dass sie den normalen gemeinsamen Vorgang ausließ und mit ihren Notizen in einen anderen Arbeitsbereich wechselte, bevor sie den Rechner sperrte."),
    ("**Beobachtungsgegenstand möglicherweise nicht nur Lage, sondern Entscheidungsverhalten.**",
     "**Beobachtungsgegenstand möglicherweise: Lage und Entscheidungsverhalten.**"),
    ("Die Frage war nicht mehr nur, woher die Quelle etwas wusste.\n\nSondern was sie wollte, dass Daniel mit diesem Wissen tat.",
     "Die Frage war nicht mehr nur, woher die Quelle etwas wusste. Ebenso wichtig war, was sie wollte, dass Daniel mit diesem Wissen tat."),
    ("„Wir prüfen seine beiden Kontakte komplett im zulässigen Rahmen. Aber nicht, weil er sie zum Zentrum macht.“\n\n„Sondern?“",
     "„Wir prüfen seine beiden Kontakte komplett im zulässigen Rahmen. Aber nicht, weil er sie zum Zentrum macht.“\n\n„Warum dann?“"),
    ("Jonas nickte.\n\n„Sondern?“",
     "Jonas nickte.\n\n„Was dann?“"),
    ("Das Problem lag weder im Kennzeichen noch im Altbestand, sondern in der Zahl der Treffer.",
     "Das Problem lag in der Zahl der Treffer, nicht im Kennzeichen oder im Altbestand."),
    ("Jonas hatte auf dem großen Bildschirm nicht nur Weber geöffnet, sondern den definierten Kreis um dieselben Zugänge.",
     "Jonas hatte auf dem großen Bildschirm Weber geöffnet und gleich den definierten Kreis um dieselben Zugänge dazu."),
    ("„Sondern: Jemand hatte dich vorher im Blick.“",
     "„Jemand hatte dich vorher im Blick.“"),
    ("„Was machst du mit der Tatsache, dass du vielleicht nicht nur informiert, sondern ausgewählt wurdest?“",
     "„Was machst du mit der Tatsache, dass du vielleicht ausgewählt wurdest und die Information nur das Mittel dazu war?“"),
    ("„Sondern weil du glaubwürdig bist“, sagte sie. „Weil du normalerweise Grenzen ernst nimmst. Weil deine Entscheidungen Gewicht haben, gerade wenn du eine Grenze trotzdem überschreitest.“",
     "„Weil du glaubwürdig bist“, sagte sie. „Weil du normalerweise Grenzen ernst nimmst. Weil deine Entscheidungen Gewicht haben, gerade wenn du eine Grenze trotzdem überschreitest.“"),
    ("Daniel ging zum Tisch zurück und öffnete nicht seinen privaten Block, sondern den formalen Projektvermerk.",
     "Daniel ging zum Tisch zurück, ließ seinen privaten Block liegen und öffnete den formalen Projektvermerk."),
    ("„Dann ist die operative Frage nicht, ob die Quelle glaubwürdig ist“, sagte Berg. „Sondern was wir heute noch ausschließen können, ohne morgen blind zu sein.“",
     "„Die operative Frage lautet, was wir heute noch ausschließen können, ohne morgen blind zu sein“, sagte Berg. „Die Glaubwürdigkeit der Quelle steht dahinter zurück.“"),
    ("Er markierte im Arbeitsstand deshalb nicht nur, was bestätigt war, sondern auch, was die Quelle gerade **nicht** geliefert hatte: kein konkreter Gefahrenzeitpunkt, keine benannte Person, kein unabhängiger Beleg für eine Manipulation der Lieferfreigabe.",
     "Er markierte im Arbeitsstand deshalb beides: was bestätigt war und was die Quelle gerade **nicht** geliefert hatte: kein konkreter Gefahrenzeitpunkt, keine benannte Person, kein unabhängiger Beleg für eine Manipulation der Lieferfreigabe."),
    ("Daniel spürte Ärger. Der galt nicht ihrer Position, sondern der Tatsache, dass sie seine Zeit benutzte.",
     "Daniel spürte Ärger darüber, dass sie seine Zeit benutzte. Ihre Position war nicht das Problem."),
    ("Das Foto zeigte nicht den Fahrer, sondern den Fahrzeugstandort.",
     "Auf dem Foto war der Fahrzeugstandort zu sehen; der Fahrer fehlte."),
    ("Schnell war die Prüfung nicht wegen zusätzlicher Befugnisse, sondern weil die Kontakte bereits standen, die Zuständigkeiten klar waren und dieselben rechtmäßig vorhandenen Informationen im Projekt nicht mehr nacheinander durch mehrere Stellen wandern mussten.",
     "Die Prüfung lief so schnell, weil die Kontakte bereits standen, die Zuständigkeiten klar waren und dieselben rechtmäßig vorhandenen Informationen im Projekt nicht mehr nacheinander durch mehrere Stellen wandern mussten. Zusätzliche Befugnisse hatten damit nichts zu tun."),
    ("„Nicht: hat funktioniert.“\n\n„Sondern?“",
     "„Nicht: hat funktioniert.“\n\n„Wie dann?“"),
    ("„Dann wahrscheinlich auf das Team. Dass ich nicht in eine fertige Struktur komme und nur repariere, sondern selbst entscheide, wie wir arbeiten.“",
     "„Dann wahrscheinlich auf das Team. Dass ich die Struktur selbst mit aufbaue und entscheide, wie wir arbeiten, statt nur in etwas Fertiges zu kommen und zu reparieren.“"),
    ("„Sondern wie wir damit umgehen.“",
     "„Entscheidend ist, wie wir damit umgehen.“"),
    ("Nicht: Was passte zur Theorie?\n\nSondern: Was hielt ihr stand?",
     "Daniel formulierte die prüfende Frage anders: Was hielt der Theorie stand?"),
    ("„Deshalb suchen wir nicht nach verdächtigen Stellen.“\n\n„Sondern?“",
     "„Deshalb suchen wir nicht nach verdächtigen Stellen.“\n\n„Wonach dann?“"),
    ("Damals hatte sich die Regel nicht wie Feigheit angefühlt, sondern wie Arbeit.",
     "Damals war die Regel für ihn schlicht Arbeit gewesen. Feigheit hatte er darin nicht gesehen."),
    ("Wenn Heller ihn nicht gesteuert hatte wie eine Figur, sondern nur Bedingungen gebaut hatte, unter denen Daniel selbst vernünftige Entscheidungen traf, dann konnte Daniel nichts davon an ihn zurückgeben.",
     "Wenn Heller lediglich Bedingungen gebaut hatte, unter denen Daniel selbst vernünftige Entscheidungen traf, ohne ihn wie eine Figur zu steuern, dann konnte Daniel nichts davon an ihn zurückgeben."),
    ("Der Raum war inzwischen zu voll. Nicht mit Menschen, sondern mit Dingen, die gleichzeitig stimmten und trotzdem noch nichts bewiesen.",
     "Der Raum war inzwischen zu voll mit Dingen, die gleichzeitig stimmten und trotzdem noch nichts bewiesen. Menschen waren nicht das Problem."),
    ("Nicht: Gefahr bestätigt.\n\nSondern: Änderung nicht vom benannten Dienstleister veranlasst.",
     "Die belastbare Formulierung lautete: Änderung nicht vom benannten Dienstleister veranlasst."),
    ("Daneben schrieb er nicht Hellers Deutung, sondern die jeweils schwächste plausible Gegenlesart.",
     "Daneben schrieb er jeweils die schwächste plausible Gegenlesart. Hellers Deutung ließ er außen vor."),
    ("„Sondern zwischen zwei unterschiedlichen Risiken.“",
     "„Zwischen zwei unterschiedlichen Risiken.“"),
    ("Was jetzt noch von ihm gebraucht wurde, war nicht die Entscheidung über Kräfte draußen, sondern der letzte saubere Stand seines Ermittlungsstrangs.",
     "Was jetzt noch von ihm gebraucht wurde, war der letzte saubere Stand seines Ermittlungsstrangs. Über die Kräfte draußen entschied er nicht."),
    ("Nicht *wir haben noch jemanden*.\n\nSondern *wir haben einen aktuellen Kontaktpunkt, Gegenhypothese beruflicher Zusammenhang*.",
     "Jonas formulierte es enger: *Wir haben einen aktuellen Kontaktpunkt, Gegenhypothese beruflicher Zusammenhang*."),
    ("Der große Schaden war nach jetzigem Stand verhindert.\n\nNicht durch Hellers letzte Meldung.\n\nNicht trotz jeder problematischen Entscheidung.\n\nSondern durch eine Arbeitsweise, die Daniel selbst weitergeführt und begrenzt hatte.",
     "Der große Schaden war nach jetzigem Stand verhindert. Den Ausschlag hatte die Arbeitsweise gegeben, die Daniel selbst weitergeführt und begrenzt hatte. Hellers letzte Meldung erklärte das Ergebnis ebenso wenig wie bloßes Glück angesichts der problematischen Entscheidungen."),
    ("„Sondern zwischen Risiken unter Zeitdruck.“",
     "„Zwischen Risiken unter Zeitdruck.“"),
    ("Zum ersten Mal reichte ihm, dass die Trennung nicht nur eine methodische Forderung war, sondern im tatsächlichen Verlauf stand.",
     "Zum ersten Mal reichte ihm, dass die Trennung im tatsächlichen Verlauf sichtbar war und damit über eine bloße methodische Forderung hinausging."),
    ("Sein Haken galt nicht der Verbundprüfung, sondern der Forderung, auch ihren **Nicht-Einsatz** messbar zu halten.",
     "Sein Haken galt der Forderung, auch ihren **Nicht-Einsatz** messbar zu halten. Die Verbundprüfung selbst markierte er damit nicht."),
    ("Daniel sah zu ihm. Der Vorschlag störte ihn nicht, weil er falsch klang, sondern weil er so normal klang.",
     "Daniel sah zu ihm. Gerade dass der Vorschlag so normal klang, störte ihn. Falsch klang er keineswegs."),
]

for idx, (old, new) in enumerate(repls, 1):
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'replacement {idx} expected once, found {count}: {old!r}')
    text = text.replace(old, new)

after = len(re.findall(r'\bsondern\b', text, re.I))
assert after == 0, f'sondern remains: {after}'
assert re.findall(r'(?m)^## (Prolog|\d+)\s*$', text) == ['Prolog'] + [str(i) for i in range(1, 48)]
assert text.rstrip().endswith('„Wie belastbar ist deine Gegenhypothese?“')
assert '—' not in text

path.write_text(text, encoding='utf-8')
print(f'Removed all {before} sondern occurrences with {len(repls)} targeted rewrites; remaining={after}')

from __future__ import annotations

import re
from pathlib import Path

PATH = Path('AUSNAHMEZUSTAND_FINAL.md')
text = PATH.read_text(encoding='utf-8')
paras = text.split('\n\n')


def replace_block(old: list[str], new: list[str], label: str) -> None:
    global paras
    hits = []
    n = len(old)
    for i in range(len(paras) - n + 1):
        if paras[i:i+n] == old:
            hits.append(i)
    if len(hits) != 1:
        raise SystemExit(f'{label}: expected exactly one match, got {len(hits)}')
    i = hits[0]
    paras[i:i+n] = new
    print(f'{label}: {n} -> {len(new)} paragraphs')


def R(label: str, old: list[str], new: list[str]) -> None:
    replace_block(old, new, label)


# Kapitel 1 – analytische Q&A-Ketten verdichten, ohne Daniels Gegenprüfungslogik zu verändern.
R('01-01', [
    '„Und das zweite Mal?“',
    '„Donnerstag, halb vier.“',
    '„Jeweils wie lange?“',
    '„Wissen wir nicht.“',
    '„Video?“',
    '„Nur vom Donnerstag. Eingangskamera. Vier Minuten sichtbar.“',
], [
    '„Und das zweite Mal?“',
    '„Donnerstag, halb vier. Wie lange er jeweils dort war, wissen wir nicht. Video gibt es nur vom Donnerstag – Eingangskamera, vier Minuten sichtbar.“',
])

R('01-02', [
    '„Warum erst am nächsten Tag?“',
    '„Schichtwechsel. Er hat mit einem Kollegen gesprochen, der meinte, sie sollen es melden.“',
    '„Hat Ahrens versucht reinzukommen?“',
    '„Nein.“',
    '„Hat er die Kamera verdeckt?“',
    '„Nein.“',
    '„Hat er irgendwen nach Sicherheitsmaßnahmen gefragt?“',
    'Jonas sah wieder auf den Vermerk. „Nicht laut dem Text.“',
], [
    '„Warum erst am nächsten Tag?“',
    '„Schichtwechsel. Er hat mit einem Kollegen gesprochen, der meinte, sie sollen es melden.“',
    'Daniel ging die nächsten Punkte selbst durch. Ahrens hatte weder versucht reinzukommen noch die Kamera verdeckt. Im Vermerk stand auch keine Frage nach Sicherheitsmaßnahmen.',
])

R('01-03', [
    '„Und das reicht dir nicht?“',
    '„Fürs Prüfen schon.“',
    '„Für die Kontrolle nicht.“',
    '„Noch nicht.“',
], [
    '„Und das reicht dir nicht?“',
    '„Fürs Prüfen schon. Für die Kontrolle noch nicht.“',
])

R('01-04', [
    '„Was noch?“',
    '„Vielleicht ist der Wagen nicht seiner.“',
    '„Gut.“',
    '„Das spricht aber nicht automatisch für harmlos.“',
    '„Soll es auch nicht.“',
], [
    '„Was noch?“',
    '„Vielleicht ist der Wagen nicht seiner.“',
    'Daniel schrieb den Punkt dazu.',
    '„Das spricht aber nicht automatisch für harmlos.“',
    '„Soll es auch nicht.“',
])

R('01-05', [
    '„Dann prüfen wir das.“',
    '„Das dauert.“',
    '„Ja.“',
    '„Wie lange?“',
    '„Firma ist offen. Sicherheitsdienst ist da. Fahrzeugdisposition sollte kein Staatsgeheimnis sein.“',
], [
    '„Dann prüfen wir das.“',
    'Jonas verzog den Mund. „Das dauert. Wie lange?“',
    '„Firma ist offen. Sicherheitsdienst ist da. Fahrzeugdisposition sollte kein Staatsgeheimnis sein.“',
])

# Kapitel 2
R('02-01', [
    '„Die hat dir die Firma geschickt?“',
    '„Ja.“',
    '„Mit vollständigen Headern?“',
    '„Weiterleitung aus ihrem System. Originalzeitstempel sichtbar.“',
    '„Gut.“',
], [
    '„Die hat dir die Firma geschickt?“',
    '„Ja. Weiterleitung aus ihrem System, vollständige Header, Originalzeitstempel sichtbar.“',
])

R('02-02', [
    '„Wer hatte die Anmeldung?“',
    '„Veranstaltungskoordination. Die Liste für nächste Woche war noch nicht in den normalen Tagesbestand übernommen.“',
    '„Also konnte der Pförtner sie übersehen.“',
    '„Ja.“',
    '„Oder gar nicht sehen.“',
    '„Ja.“',
], [
    '„Wer hatte die Anmeldung?“',
    '„Veranstaltungskoordination. Die Liste für nächste Woche war noch nicht in den normalen Tagesbestand übernommen.“',
    'Daniel nickte. Der Pförtner konnte sie übersehen haben – oder gar nicht sehen.',
])

R('02-03', [
    '„Ist das sein Wagen?“',
    '„Einer von neun identischen Firmenwagen.“',
    '„Und welcher war zwei Straßen weiter?“',
    '„Seiner.“',
    '„Belegt?“',
], [
    '„Ist das sein Wagen?“',
    '„Einer von neun identischen Firmenwagen. Der Wagen zwei Straßen weiter war seiner.“',
    '„Belegt?“',
])

# Kapitel 6 – Faktenprüfung in der privaten Szene einmal bewusst aus dem Interviewtakt lösen.
R('06-01', [
    '„Ich würde das Team selbst aufbauen. Acht Leute, eigene Kunden. Nicht wieder erst in Projekte einsteigen, wenn sie schon halb festgefahren sind.“',
    '„Direkte Berichtslinie?“',
    '„An die Bereichsleitung.“',
    '„Budgetverantwortung?“',
    '„Teilweise.“',
    '„Einstellungen selbst?“',
    '„Mit HR, aber ja. Fachlich meine Entscheidung.“',
], [
    '„Ich würde das Team selbst aufbauen. Acht Leute, eigene Kunden. Nicht wieder erst in Projekte einsteigen, wenn sie schon halb festgefahren sind.“',
    'Daniel fragte nach Berichtslinie, Budget und Einstellungen. Mara antwortete ohne zu zögern: direkt an die Bereichsleitung, teilweise Budgetverantwortung, Einstellungen mit HR – fachlich ihre Entscheidung.',
])

# Kapitel 7
R('07-01', [
    '„Hat jemand heute einen offenen Zugang gemeldet?“',
    '„Nein.“',
    '„Gestern?“',
    '„Nein.“',
    '„Fehlermeldung vom Schloss?“',
    '„Nicht dass ich wüsste.“',
], [
    '„Hat jemand heute oder gestern einen offenen Zugang gemeldet?“',
    '„Nein. Auch keine Fehlermeldung vom Schloss, nicht dass ich wüsste.“',
])

R('07-02', [
    '„Also ein zweiter Anker.“',
    '„Ja.“',
    '„Und wenn der morgen kommt?“',
    '„Dann haben wir morgen mehr.“',
], [
    '„Also ein zweiter Anker. Und wenn der morgen kommt?“',
    '„Dann haben wir morgen mehr.“',
])

# Kapitel 9
R('09-01', [
    '„Nicht: Was klingt plausibel. Was können wir prüfen?“',
    '„Die Abholung.“',
    '„Gut.“',
    '„Den Zusammenhang der Lieferadresse mit dem grauen Wagen, falls wir ihn identifizieren.“',
    '„Gut.“',
    '„Und ob Einheit 17 mit einem Dienstleister für die Veranstaltung verbunden ist.“',
], [
    '„Nicht: Was klingt plausibel. Was können wir prüfen?“',
    'Jonas zählte auf: die Abholung; den Zusammenhang der Lieferadresse mit dem grauen Wagen, falls sie ihn identifizierten; und ob Einheit 17 mit einem Dienstleister für die Veranstaltung verbunden war.',
])

R('09-02', [
    '„Im Auftrag steht: Zugang Rampe Nord, Kunde Einheit 16. Rechnungsempfänger ist aber die Handelsfirma aus 17.“',
    '„Fehler?“',
    '„Kann sein.“',
    '„Absicht?“',
    '„Kann auch sein.“',
    '„Was sagt der Kurier?“',
    '„Kunde hat die Rampe so angegeben. Für die ist das nur Abholort plus Rechnungsempfänger.“',
    '„Wer hat gebucht?“',
], [
    '„Im Auftrag steht: Zugang Rampe Nord, Kunde Einheit 16. Rechnungsempfänger ist aber die Handelsfirma aus 17.“',
    'Daniel ließ beide Lesarten stehen: Fehler oder Absicht.',
    '„Was sagt der Kurier?“',
    '„Kunde hat die Rampe so angegeben. Für die ist das nur Abholort plus Rechnungsempfänger.“',
    '„Wer hat gebucht?“',
])

R('09-03', [
    '„Die Nachricht kam zweiunddreißig Minuten nach der Buchung.“',
    '„Ja.“',
    '„Also nicht vor der Buchung.“',
    '„Nein.“',
    '„Heißt, die Quelle muss den Auftrag nicht vorher geplant haben. Sie kann ihn einfach sehr schnell gesehen haben.“',
], [
    '„Die Nachricht kam zweiunddreißig Minuten nach der Buchung. Also nicht vorher.“',
    '„Nein. Die Quelle muss den Auftrag nicht vorher geplant haben. Sie kann ihn einfach sehr schnell gesehen haben.“',
])

# Kapitel 10
R('10-01', [
    '„Kann Werkzeug sein.“',
    '„Ja.“',
    '„Messtechnik.“',
    '„Ja.“',
    '„Ersatzteile.“',
    '„Ja.“',
    '„Oder etwas Gefährliches.“',
    '„Ja.“',
], [
    'Werkzeug, Messtechnik, Ersatzteile – alles war möglich. Etwas Gefährliches auch.',
])

R('10-02', [
    '„Nein.“',
    '„Ist der Koffer geöffnet worden?“',
    '„Nein.“',
    '„Ist er weitergegeben worden?“',
    '„Noch nicht.“',
    '„Hat die Quelle behauptet, der Koffer sei gefährlich?“',
], [
    '„Nein. Der Koffer ist weder geöffnet noch weitergegeben worden.“',
    '„Hat die Quelle behauptet, der Koffer sei gefährlich?“',
])

# Kapitel 11
R('11-01', [
    '„Regulär hinterlegt“, sagte sie. „Mehrere Fahrzeuge, mehrere Personen. Nichts Gesperrtes.“',
    '„Änderungen heute?“',
    '„Müsste ich prüfen.“',
    '„Wie lange?“',
    '„Ich melde mich.“',
    '„Noch heute?“',
    'Kurze Pause.',
    '„Ja.“',
], [
    '„Regulär hinterlegt“, sagte sie. „Mehrere Fahrzeuge, mehrere Personen. Nichts Gesperrtes.“',
    '„Änderungen heute?“',
    '„Müsste ich prüfen. Ich melde mich noch heute.“',
])

R('11-02', [
    '„Was verbindet den Fahrer mit Einheit 17?“ fragte er.',
    'Jonas schüttelte den Kopf. „Noch nichts.“',
    '„Mit dem Kurier?“',
    '„Noch nichts.“',
    '„Mit dem Dienstleister?“',
    '„Der Wagen war heute dort. Mehr haben wir nicht.“',
    '„Wie lange?“',
    '„Knapp zwanzig Minuten.“',
    '„Wer hatte ihn?“',
    '„Mietvertrag läuft auf falsche Kontaktdaten. Identität des Abholers offen.“',
    '„Also nicht der Mitarbeiter, der den Koffer angenommen hat.“',
    '„Nicht nach jetzigem Stand.“',
], [
    '„Was verbindet den Fahrer mit Einheit 17?“ fragte er.',
    'Jonas schüttelte den Kopf. „Noch nichts. Mit dem Kurier auch nicht. Beim Dienstleister stand der Wagen heute knapp zwanzig Minuten. Mietvertrag auf falsche Kontaktdaten, Identität des Abholers offen.“',
    '„Also nicht der Mitarbeiter, der den Koffer angenommen hat.“',
    '„Nicht nach jetzigem Stand.“',
])

# Kapitel 12
R('12-01', [
    '„Das Ergebnis macht sie nicht rückwirkend schlecht.“',
    '„Ja.“',
    '„Und trotzdem ändere ich den Ablauf.“',
    '„Dagegen habe ich nichts.“',
], [
    '„Das Ergebnis macht sie nicht rückwirkend schlecht. Und trotzdem ändere ich den Ablauf.“',
    '„Dagegen habe ich nichts.“',
])

# Kapitel 13
R('13-01', [
    '„Kennzeichen existiert. Mietfahrzeug. Seit gestern an eine kleine Kurierfirma ausgegeben.“',
    '„Verbindungen?“',
    '„Offen nichts. Firma ist real. Drei Fahrer, acht Fahrzeuge, macht alles von Medikamente bis Ersatzteile.“',
    '„Seit wann?“',
    '„Sieben Jahre im Register. Website passt. Keine auffällige Änderung.“',
    '„Wer hat den Wagen übernommen?“',
    '„Vertrag auf Firmenkonto. Fahrer nicht eindeutig zugeordnet.“',
    '„Zahlung?“',
    '„Normal über das Geschäftskonto.“',
    '„Aktuelle Bewegung?“',
    '„Nicht ohne mehr.“',
], [
    '„Kennzeichen existiert. Mietfahrzeug. Seit gestern an eine kleine Kurierfirma ausgegeben.“',
    'Jonas ging die Stammdaten gleich mit durch. Reale Firma, sieben Jahre im Register, drei Fahrer, acht Fahrzeuge, unauffällige Website. Vertrag und Zahlung liefen über das Geschäftskonto; der Fahrer war nicht eindeutig zugeordnet.',
    '„Aktuelle Bewegung?“',
    '„Nicht ohne mehr.“',
])

R('13-02', [
    '„Sie hat wieder ein Detail.“',
    '„Relevanz für das Kennzeichen?“',
    '„Keine belegbare.“',
    '„Dann bleibt sie draußen.“',
    '„Ja.“',
    '„Ich prüfe die Freigabeseite.“',
], [
    '„Sie hat wieder ein Detail.“',
    '„Relevanz für das Kennzeichen?“',
    '„Keine belegbare.“',
    '„Dann bleibt sie draußen. Ich prüfe die Freigabeseite.“',
])

R('13-03', [
    '„Gab es eine Rückgabezeit?“',
    '„Morgen Vormittag.“',
    '„Geplante Kilometer?“',
    '„Nein.“',
    '„Zusatzfahrer?“',
    '„Das kann ich Ihnen so nicht geben.“',
], [
    '„Gab es eine Rückgabezeit?“',
    '„Morgen Vormittag. Geplante Kilometer gibt es nicht. Zusatzfahrer kann ich Ihnen ohne weitere Grundlage nicht nennen.“',
])

R('13-04', [
    '„Verstanden.“',
    '„Ich ziehe, was ich ziehen kann.“',
    '„Kannst du priorisieren?“',
    '„Habe ich schon.“',
    '„Mehr?“',
    '„Nicht ohne etwas vorzugeben, das wir nicht haben.“',
], [
    '„Verstanden. Kannst du priorisieren?“',
    '„Habe ich schon. Ich ziehe, was ich ziehen kann. Mehr ginge nur, wenn ich etwas vorgebe, das wir nicht haben.“',
])

# Kapitel 15
R('15-01', [
    '„Also noch mal. B-QV 4172 zweimal in zeitlicher Nähe zu einem weißen Lieferwagen aus dem alten Vorgang.“',
    '„Ja.“',
    '„Der alte Wagen hing an einem Mann aus einem Unterstützerumfeld.“',
    '„War zugeordnet. Nicht automatisch Täter.“',
    '„Und wir dürfen jetzt nicht einfach die Personenkette ziehen.“',
    '„Richtig.“',
], [
    '„Also noch mal. B-QV 4172 zweimal in zeitlicher Nähe zu einem weißen Lieferwagen aus dem alten Vorgang.“',
    '„Der alte Wagen hing an einem Mann aus einem Unterstützerumfeld – zugeordnet, nicht automatisch Täter.“',
    '„Und wir dürfen jetzt nicht einfach die Personenkette ziehen.“',
    '„Richtig.“',
])

R('15-02', [
    '„Wann?“',
    '„19.24 bis 19.27.“',
    '„Wer hat das freigegeben?“',
    '„Niemand.“',
    '„Was genau hast du gezogen?“',
    '„Kennzeichentreffer und vorhandene Zuordnungen. Drei Treffer. Einen Parkverstoß. Zwei gemeinsame Zeit-/Ortsbezüge mit einem Fahrzeug aus einem alten Vorgang.“',
    '„Personen?“',
    '„Nicht erweitert.“',
    '„Kontakte?“',
    '„Nein.“',
    '„Bewegungsdaten?“',
    '„Nein.“',
], [
    '„Wann?“',
    '„19.24 bis 19.27.“',
    '„Wer hat das freigegeben?“',
    '„Niemand.“',
    '„Was genau hast du gezogen?“',
    '„Kennzeichentreffer und vorhandene Zuordnungen. Drei Treffer. Einen Parkverstoß. Zwei gemeinsame Zeit-/Ortsbezüge mit einem Fahrzeug aus einem alten Vorgang.“',
    '„Personen, Kontakte, Bewegungsdaten?“',
    '„Nicht erweitert. Keine Kontakte, keine Bewegungsdaten.“',
])

# Kapitel 16
R('16-01', [
    '„Warum?“',
    '„Weil die Seiteneinfahrt ab morgen für Aufbaupersonal offen ist. Heute ist sie zu.“',
    '„Quelle?“',
    '„Veranstaltungsplan. Öffentlich.“',
    '„Aktueller Status der Tür?“',
], [
    '„Warum?“',
    '„Weil die Seiteneinfahrt ab morgen für Aufbaupersonal offen ist. Heute ist sie zu. Veranstaltungsplan, öffentlich.“',
    '„Aktueller Status der Tür?“',
])

# Kapitel 17
R('17-01', [
    '„Du hast auf das Kennzeichen begrenzt.“',
    '„Ja.“',
    '„Keine Personen erweitert?“',
    '„Nein.“',
    '„Keine weiteren Daten gezogen?“',
    '„Nur die Trefferzuordnung und die beiden Zeitpunkte.“',
    '„Keinen Screenshot?“',
    '„Nein.“',
    '„Export?“',
    '„Nein.“',
    '„Warum so eng?“',
], [
    '„Du hast auf das Kennzeichen begrenzt. Keine Personen erweitert, keine weiteren Daten gezogen?“',
    '„Nur die Trefferzuordnung und die beiden Zeitpunkte.“',
    '„Kein Screenshot, kein Export?“',
    '„Nein.“',
    '„Warum so eng?“',
])

R('17-02', [
    '„Dokumentation.“',
    '„Wo?“',
    '„Getrennt.“',
    '„Warum?“',
    '„Weil Berg gerade gesagt hat, die Bewertung läuft getrennt.“',
], [
    '„Dokumentation?“',
    '„Getrennt. Berg hat gerade gesagt, die Bewertung läuft getrennt.“',
])

# Kapitel 18
R('18-01', [
    '„Schon wieder?“ sagte Jonas.',
    '„Ja.“',
    '„Quelle?“',
    '„Ja.“',
    '„Was will sie?“',
], [
    '„Schon wieder?“, sagte Jonas.',
    '„Ja. Die Quelle.“',
    '„Was will sie?“',
])

R('18-02', [
    '„Das wusste ich nachher auch.“',
    '„Ja.“',
    '„Lena.“',
    '„Ja.“',
    '„Berg.“',
    '„Ja.“',
    '„Und wahrscheinlich die Leute, die den Zugriff technisch sehen.“',
    '„Genau.“',
    '„Heller?“',
], [
    '„Das wusste ich nachher auch.“',
    'Sie gingen die naheliegenden Empfänger durch: Lena, Berg und wahrscheinlich die Leute, die den Zugriff technisch sehen konnten.',
    '„Heller?“',
])

R('18-03', [
    '„Und was machen wir damit?“',
    '„Wir verändern nicht den operativen Stand wegen einer Herkunftshypothese. Aber nicht mehr jeder bekommt automatisch denselben Quellenstand.“',
    '„Du willst segmentieren.“',
    '„Ja.“',
    '„Das wird nervig.“',
    '„Ja.“',
    '„Und fehleranfällig.“',
    '„Auch.“',
], [
    '„Und was machen wir damit?“',
    '„Wir verändern nicht den operativen Stand wegen einer Herkunftshypothese. Aber nicht mehr jeder bekommt automatisch denselben Quellenstand.“',
    '„Du willst segmentieren.“',
    '„Ja.“',
    'Die Nachteile lagen auf der Hand: nervig, fehleranfällig.',
])

R('18-04', [
    '„Dann ist das der Preis.“',
    '„Schlechter Preis.“',
    '„Ja.“',
    '„Und wenn die Quelle merkt, dass wir anders reagieren?“',
], [
    '„Dann ist das der Preis.“',
    '„Ein schlechter.“',
    '„Und wenn die Quelle merkt, dass wir anders reagieren?“',
])

# Kapitel 20
R('20-01', [
    '„Trefferzahl?“',
    '„Im ursprünglichen Vermerk.“',
    '„Begrenzung?“',
    '„Dort ebenfalls.“',
    '„In der Lagefassung?“',
    '„Nein.“',
    '„In der behördenübergreifenden Koordination?“',
], [
    '„Trefferzahl und Begrenzung?“',
    '„Im ursprünglichen Vermerk.“',
    '„In der Lagefassung?“',
    '„Nein.“',
    '„In der behördenübergreifenden Koordination?“',
])

# Kapitel 21
R('21-01', [
    '„Danach?“',
    '„Ende oder neue Begründung.“',
    '„Daten?“',
    '„Rückführung nach den definierten Regeln. Kein stiller Dauerbestand.“',
    '„Protokolle?“',
    '„Bleiben.“',
], [
    '„Danach?“',
    '„Ende oder neue Begründung. Daten zurück nach den definierten Regeln, kein stiller Dauerbestand. Protokolle bleiben.“',
])

# Kapitel 23
R('23-01', [
    '„Auf Weber registriert.“',
    '„Heißt nicht, dass nur Weber es benutzt.“',
    '„Nein.“',
    '„Und der Zugang?“',
    '„Er koordiniert die Abendschichten beim Subunternehmer. Hat legitimen Zugriff.“',
], [
    '„Auf Weber registriert.“',
    '„Heißt nicht, dass nur Weber es benutzt. Und der Zugang?“',
    '„Er koordiniert die Abendschichten beim Subunternehmer. Hat legitimen Zugriff.“',
])

R('23-02', [
    '„War er eingeteilt?“',
    '„Nein.“',
    '„Urlaub?“',
    '„Frei.“',
], [
    '„War er eingeteilt?“',
    '„Nein. Frei.“',
])

R('23-03', [
    '„Das ist besser als der Anruf.“',
    '„Ja.“',
    '„Nicht gut.“',
    '„Nein.“',
], [
    '„Das ist besser als der Anruf. Nicht gut – aber besser.“',
])

# Kapitel 26
R('26-01', [
    '„Sicher?“',
    '„Ja.“',
    '„Wie weit?“',
    '„Die Beobachtung im Haus meiner Mutter war abends. Berg hat mir den Lagerkomplex erst am nächsten Vormittag gegeben.“',
], [
    '„Sicher?“',
    '„Ja. Die Beobachtung im Haus meiner Mutter war abends. Berg hat mir den Lagerkomplex erst am nächsten Vormittag gegeben.“',
])

R('26-02', [
    '„Und die Uhrzeit?“',
    '„Mit Jana gegengeprüft.“',
    '„Interne Vorbefassung?“',
    '„In meinen Unterlagen keine. Übergabeliste erst am nächsten Morgen.“',
    '„Mündlich?“',
    '„Nicht ausgeschlossen.“',
], [
    '„Und die Uhrzeit?“',
    '„Mit Jana gegengeprüft. In meinen Unterlagen keine interne Vorbefassung; Übergabeliste erst am nächsten Morgen. Mündlich nicht ausgeschlossen.“',
])

R('26-03', [
    '„Der Sicherheitsmann wäre vielleicht nicht der Letzte gewesen.“',
    '„Ja.“',
    '„Der breite Prüfkreis hat einen realen Vorbereitungsschritt sichtbar gemacht.“',
    '„Ja.“',
], [
    'Der Sicherheitsmann wäre vielleicht nicht der Letzte gewesen. Der breite Prüfkreis hatte einen realen Vorbereitungsschritt sichtbar gemacht. Daniel widersprach keinem der beiden Punkte.',
])

R('26-04', [
    '„Berg?“',
    '„Hat geliefert.“',
    '„Heller?“',
    '„Im Verteiler.“',
    '„Du?“',
], [
    '„Berg?“',
    '„Hat geliefert. Heller war im Verteiler.“',
    '„Du?“',
])

# Kapitel 27
R('27-01', [
    '„Kennung bestätigt?“',
    '„Ja.“',
    '„Bedeutung?“',
    '„Offen.“',
    '„Firma?“',
    '„Bis jetzt unauffällig.“',
    '„Zeitfenster?“',
    '„‚Morgiger Aufbau‘. Kein genauer Zeitpunkt.“',
], [
    '„Kennung bestätigt?“',
    '„Ja. Bedeutung offen, Firma bis jetzt unauffällig. Zeitfenster nur ‚morgiger Aufbau‘, kein genauer Zeitpunkt.“',
])

# Kapitel 29
R('29-01', [
    '„Du könntest erklären, was die Kontakte sind.“',
    '„Formal.“',
    '„Das dauert.“',
    '„Dann dauert es.“',
    '„Du weißt, was morgen läuft.“',
    '„Ja.“',
    '„Und du gibst mir trotzdem nichts?“',
], [
    '„Du könntest erklären, was die Kontakte sind.“',
    '„Formal.“',
    '„Das dauert.“',
    '„Dann dauert es.“',
    '„Du weißt, was morgen läuft – und gibst mir trotzdem nichts?“',
])

# Kapitel 30
R('30-01', [
    '„Das dauert.“',
    '„Dann dauert es.“',
    '„Du weißt, was gerade läuft.“',
    '„Ja.“',
    '„Und du akzeptierst, dass du bis dahin draußen bleibst?“',
], [
    '„Das dauert.“',
    '„Dann dauert es.“',
    '„Du weißt, was gerade läuft. Akzeptierst du trotzdem, dass du bis dahin draußen bleibst?“',
])

R('30-02', [
    '„Warum?“',
    '„Eine Rückfrage liegt in deinem gesperrten Bereich. Ich sehe nur, dass sie da ist.“',
    '„Dann formal umhängen lassen.“',
    '„Hab ich angestoßen.“',
    '„Wie lange?“',
], [
    '„Warum?“',
    '„Eine Rückfrage liegt in deinem gesperrten Bereich. Ich sehe nur, dass sie da ist. Das formale Umhängen habe ich angestoßen.“',
    '„Wie lange?“',
])

R('30-03', [
    '„Du bist wieder drin.“',
    '„Ich weiß.“',
    '„Die interne Bewertung gegen dich wird korrigiert.“',
    '„Gut.“',
    '„Es tut mir leid.“',
], [
    '„Du bist wieder drin. Die interne Bewertung gegen dich wird korrigiert.“',
    '„Ich weiß.“',
    '„Es tut mir leid.“',
])

# Kapitel 31
R('31-01', [
    '„Kennzeichen?“',
    '„Passt.“',
    '„Fahrzeughalter?“',
    '„Dienstleister.“',
    '„Person?“',
    '„Nicht die aus unserem Treffer.“',
], [
    '„Kennzeichen, Halter, Person?“',
    '„Kennzeichen passt. Halter ist der Dienstleister. Person nicht die aus unserem Treffer.“',
])

R('31-02', [
    '„Foto?“',
    '„Ja.“',
    '„Zeit?“',
    '„17.26 Uhr.“',
    '„Bestätigt?“',
    '„Ja.“',
], [
    '„Foto?“',
    '„Ja. 17.26 Uhr, bestätigt.“',
])

# Kapitel 33
R('33-01', [
    '„Die Fahrerlisten waren unvollständig.“',
    '„Ja.“',
    '„Und der breitere Abgleich hat einen realen Gefahrenstrang sichtbar gemacht.“',
    '„Ja.“',
], [
    '„Die Fahrerlisten waren unvollständig. Und der breitere Abgleich hat einen realen Gefahrenstrang sichtbar gemacht.“',
    '„Beides stimmt.“',
])

R('33-02', [
    '„Weil ich inzwischen zwei reale Fälle habe, in denen Zeit und Verbindung einen Unterschied gemacht haben.“',
    '„Und zwei reale Fehlbelastungen.“',
    '„Ja.“',
    '„Also wieder keine eindeutige Bilanz.“',
    '„Nein.“',
], [
    '„Weil ich inzwischen zwei reale Fälle habe, in denen Zeit und Verbindung einen Unterschied gemacht haben.“',
    '„Und zwei reale Fehlbelastungen.“',
    'Daniel nickte.',
    '„Also wieder keine eindeutige Bilanz.“',
    '„Nein.“',
])

# Kapitel 35
R('35-01', [
    '„Dann?“',
    '„Dann wäre die Verbindung zum bekannten Umfeld prüfbar gewesen“, sagte Lena. „Danach hätten wir entscheiden müssen, ob eine gezielte Beobachtung oder eine engere Abklärung rechtlich trägt.“',
    '„Also wieder Entscheidung.“',
    '„Natürlich wieder Entscheidung.“',
    '„Kein Knopf, den man drückt und der Betriebshof ist sicher.“',
    '„Nein.“',
], [
    '„Dann?“',
    '„Dann wäre die Verbindung zum bekannten Umfeld prüfbar gewesen“, sagte Lena. „Danach hätten wir entscheiden müssen, ob eine gezielte Beobachtung oder eine engere Abklärung rechtlich trägt.“',
    '„Also wieder Entscheidung. Kein Knopf, den man drückt und der Betriebshof ist sicher.“',
    '„Natürlich nicht.“',
])

R('35-02', [
    '„Hätten wir ihn gestoppt?“',
    '„Weiß niemand.“',
    '„Hätten wir den Sicherheitsmann warnen können?“',
    '„Vielleicht. Wenn die Kette schnell genug trägt und der Betriebshof als möglicher Kontaktpunkt sichtbar wird.“',
    '„Vielleicht.“',
    '„Ja.“',
], [
    '„Hätten wir ihn gestoppt?“',
    '„Weiß niemand.“',
    '„Hätten wir den Sicherheitsmann warnen können?“',
    '„Vielleicht. Wenn die Kette schnell genug trägt und der Betriebshof als möglicher Kontaktpunkt sichtbar wird.“',
    'Daniel ließ das Vielleicht stehen.',
])

R('35-03', [
    '„Ich hätte zu langsam sein können.“',
    '„Ja.“',
    '„Oder wir hätten geprüft und nichts Belastbares gefunden.“',
    '„Ja.“',
], [
    '„Ich hätte zu langsam sein können. Oder wir hätten geprüft und nichts Belastbares gefunden.“',
    '„Beides.“',
])

# Kapitel 36
R('36-01', [
    '„Wer konnte das Konto nutzen?“',
    '„Mehrere Leute.“',
    '„Also wieder kein Beweis.“',
    '„Nein.“',
    '„Wer hat die Liste der Personen geliefert?“',
], [
    '„Wer konnte das Konto nutzen?“',
    '„Mehrere Leute.“',
    'Daniel strich den Punkt gedanklich aus der Beweisspalte.',
    '„Wer hat die Liste der Personen geliefert?“',
])

# Kapitel 37
R('37-01', [
    '„Unabhängig?“',
    '„Ja.“',
    '„Sicher?“',
    '„Ja.“',
], [
    '„Unabhängig?“',
    '„Ja.“',
    'Daniel wartete.',
    '„Sicher.“',
])

# Kapitel 38
R('38-01', [
    '„Keiner als Fakt. Wir hätten sie nur später zusammengeführt.“',
    '„Das Fahrzeug?“',
    '„Andere Dienststelle.“',
    '„Die Person?“',
    '„Temporärer Ausweis plus älterer Kontaktbestand.“',
    '„Zeitfenster?“',
    '„Veranstalter und Dienstleister widersprechen sich unabhängig von Heller.“',
], [
    '„Keiner als Fakt. Wir hätten sie nur später zusammengeführt.“',
    '„Fahrzeug, Person, Zeitfenster?“',
    '„Fahrzeug bei anderer Dienststelle. Person: temporärer Ausweis plus älterer Kontaktbestand. Zeitfenster: Veranstalter und Dienstleister widersprechen sich unabhängig von Heller.“',
])

# Kapitel 39
R('39-01', [
    '„Fahrzeug sichern. Personen darin feststellen. Verbindung klären.“',
    '„Nicht den gesamten Subunternehmerkreis.“',
    '„Nein.“',
    '„Nicht jede Person, die in den letzten Tagen Kontakt hatte.“',
    '„Nein.“',
], [
    '„Fahrzeug sichern. Personen darin feststellen. Verbindung klären.“',
    '„Nicht den gesamten Subunternehmerkreis. Nicht jede Person, die in den letzten Tagen Kontakt hatte.“',
    '„Nein.“',
])

# Kapitel 40
R('40-01', [
    '„Meine letzte bestätigte Grundlage liegt dort vollständig?“',
    '„Ja.“',
    '„Mit dem Widerruf?“',
    '„Ja.“',
], [
    '„Meine letzte bestätigte Grundlage liegt dort vollständig – mit dem Widerruf?“',
    '„Ja.“',
])

# Kapitel 41
R('41-01', [
    '„Bestätigt?“',
    '„Ja.“',
    '„Personen?“',
    '„Zwei am Fahrzeug, mindestens eine weitere im Servicebereich. Noch keine vollständige Lage.“',
], [
    '„Bestätigt?“',
    '„Ja. Zwei am Fahrzeug, mindestens eine weitere im Servicebereich. Noch keine vollständige Lage.“',
])

R('41-02', [
    '„Welche?“',
    '„Fahrzeug zu Servicezufahrt. Zugangsdokumente zum Material aus dem Lagerstrang. Person eins zu dem unabhängig bestätigten Unterstützerkontakt.“',
    '„Person zwei?“',
    '„Noch offen.“',
    '„Dann offen lassen.“',
], [
    '„Welche?“',
    '„Fahrzeug zu Servicezufahrt. Zugangsdokumente zum Material aus dem Lagerstrang. Person eins zu dem unabhängig bestätigten Unterstützerkontakt. Person zwei ist noch offen.“',
    '„Dann offen lassen.“',
])

R('41-03', [
    '„Direkt?“',
    '„Ein aktueller Kontaktpunkt.“',
    '„Das ist nicht direkt.“',
    '„Nein.“',
    '„Gegenhypothese?“',
    '„Beruflicher Kontakt über den Dienstleister.“',
    '„Dann kein Schritt nur darauf.“',
], [
    '„Direkt?“',
    '„Ein aktueller Kontaktpunkt.“',
    '„Also nicht direkt. Gegenhypothese?“',
    '„Beruflicher Kontakt über den Dienstleister.“',
    '„Dann kein Schritt nur darauf.“',
])

R('41-04', [
    '„Servicezufahrt?“',
    '„Unterlagen aus gestopptem Fahrzeug plus Bestätigung Veranstalter.“',
    '„Person eins?“',
    '„Aktueller Zugang und unabhängig bestätigter Unterstützerkontakt.“',
    '„Person zwei?“',
    '„Nur gemeinsamer Dienstleister.“',
    '„Dann offen.“',
], [
    '„Servicezufahrt, Person eins, Person zwei?“',
    '„Servicezufahrt: Unterlagen aus gestopptem Fahrzeug plus Bestätigung Veranstalter. Person eins: aktueller Zugang und unabhängig bestätigter Unterstützerkontakt. Person zwei: nur gemeinsamer Dienstleister.“',
    '„Dann offen.“',
])

# Kapitel 42
R('42-01', [
    '„Das wusste ich.“',
    '„Ja.“',
    '„Und was ist neu?“',
], [
    '„Das wusste ich. Und was ist neu?“',
])

# Kapitel 43 – formale Befragung bleibt formal, aber doppelte Bestätigungsloops werden verdichtet.
R('43-01', [
    '„Sie wussten gestern vor der erweiterten Prüfung, dass Herr Heller die Drucklage wahrscheinlich gezielt mit aufgebaut hatte?“',
    '„Ja.“',
    '„Und haben die Struktur trotzdem genutzt?“',
    '„Ja.“',
    '„Warum?“',
], [
    '„Sie wussten gestern vor der erweiterten Prüfung, dass Herr Heller die Drucklage wahrscheinlich gezielt mit aufgebaut hatte – und haben die Struktur trotzdem genutzt?“',
    '„Ja.“',
    '„Warum?“',
])

R('43-02', [
    '„Nein.“',
    '„Für praktisch zu unsicher?“',
    '„In dem Moment: ja.“',
    '„Das ist Ihre damalige Bewertung.“',
    '„Ja.“',
    '„Nicht unsere heutige.“',
    '„Nein.“',
], [
    '„Nein.“',
    '„Für praktisch zu unsicher?“',
    '„In dem Moment: ja.“',
    '„Das ist Ihre damalige Bewertung, nicht unsere heutige.“',
    '„Nein.“',
])

# Kapitel 44
R('44-01', [
    '„Dann kann die Prüfung parallel laufen. Aber die Abweichung wird protokolliert und nachträglich zwingend überprüft.“',
    '„Das kostet Zeit.“',
    '„Ja.“',
    '„Im falschen Moment kann das relevant sein.“',
    '„Ja.“',
], [
    '„Dann kann die Prüfung parallel laufen. Aber die Abweichung wird protokolliert und nachträglich zwingend überprüft.“',
    '„Das kostet Zeit. Im falschen Moment kann das relevant sein.“',
    '„Ja.“',
])

R('44-02', [
    '„Wie lange?“',
    '„Zunächst sechs Monate.“',
    '„Und danach?“',
    '„Neuentscheidung.“',
], [
    '„Wie lange?“',
    '„Zunächst sechs Monate. Danach Neuentscheidung.“',
])

# Kapitel 46
R('46-01', [
    '„Dienstlicher Grund für die Nachtzugriffe?“',
    '„Noch offen.“',
    '„Wer hat den Zugang technisch freigegeben?“',
    '„Reguläre Berechtigung. Nur die Uhrzeit ist ungewöhnlich.“',
    '„Kontakt wie alt?“',
    '„Zwei Jahre.“',
    '„Dann ist er erst mal zwei Jahre alt.“',
], [
    '„Dienstlicher Grund für die Nachtzugriffe?“',
    '„Noch offen. Technisch reguläre Berechtigung, nur die Uhrzeit ist ungewöhnlich. Der Kontakt ist zwei Jahre alt.“',
    '„Dann ist er erst mal zwei Jahre alt.“',
])

# Kapitel 47 – die letzte Gegenhypothesenfrage bleibt vollständig unangetastet; nur die reine Faktenabfrage davor wird verdichtet.
R('47-01', [
    '„Ausweis eindeutig?“',
    '„Personengebundene Karte.“',
    '„Kann sie weitergegeben worden sein?“',
    '„Technisch ja. Verboten, aber möglich.“',
    '„Video?“',
    '„Der Gang selbst nicht. Außenkamera hat in dem Zeitraum eine Lücke durch Wartung.“',
], [
    '„Ausweis eindeutig?“',
    '„Personengebundene Karte. Weitergabe technisch möglich, aber verboten. Kein Video vom Gang; die Außenkamera hat in dem Zeitraum eine Lücke durch Wartung.“',
])

R('47-02', [
    '„Dienstplan?“',
    '„Person offiziell frei.“',
    '„Tausch?“',
    '„Noch nicht geklärt.“',
], [
    '„Dienstplan?“',
    '„Person offiziell frei. Tausch noch nicht geklärt.“',
])

# Guards / metrics
new_text = '\n\n'.join(paras)
headings = re.findall(r'^## (Prolog|\d+)$', new_text, re.M)
if headings != ['Prolog'] + [str(i) for i in range(1, 48)]:
    raise SystemExit('Chapter structure changed unexpectedly')
if not new_text.rstrip().endswith('„Wie belastbar ist deine Gegenhypothese?“'):
    raise SystemExit('Final line changed unexpectedly')
if '—' in new_text:
    raise SystemExit('Em dash introduced')

before_yes = text.count('\n\n„Ja.“\n\n')
after_yes = new_text.count('\n\n„Ja.“\n\n')
before_no = text.count('\n\n„Nein.“\n\n')
after_no = new_text.count('\n\n„Nein.“\n\n')

word_re = re.compile(r"[A-Za-zÄÖÜäöüß0-9]+(?:['’\-][A-Za-zÄÖÜäöüß0-9]+)*")
before_words = len(word_re.findall(text))
after_words = len(word_re.findall(new_text))
if abs(after_words - before_words) > 1000:
    raise SystemExit(f'Word-count delta too large: {after_words-before_words}')

PATH.write_text(new_text, encoding='utf-8')
print(f'RHYTHM_PASS_OK words {before_words}->{after_words} ({after_words-before_words:+d})')
print(f'isolated JA {before_yes}->{after_yes}; isolated NEIN {before_no}->{after_no}')

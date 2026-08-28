from __future__ import annotations

import re
from pathlib import Path

PATH = Path('AUSNAHMEZUSTAND_FINAL.md')
text = PATH.read_text(encoding='utf-8')
original = text


def R(label: str, old: str, new: str) -> None:
    global text
    hits = text.count(old)
    if hits != 1:
        raise SystemExit(f'{label}: expected exactly one match, got {hits}')
    text = text.replace(old, new, 1)
    print(label)

# 1) Kapitel 6 – private Szene: Daniels Analysemodus soll sich sprachlich anders
# anfühlen als eine Lagebesprechung.
R('06-01',
'''Mara sah ihn an.\n\nDaniel merkte den Fehler, bevor sie etwas sagte.\n\n„So meinte ich das nicht.“''',
'''Mara sah ihn an.\n\nEr hörte seinen eigenen Satz noch einmal, diesmal mit Maras Ohren.\n\n„So meinte ich das nicht.“''')

R('06-02',
'''Er ging im Kopf die nächsten Tage durch. Zwei Termine am Samstag. Sonntagvormittag frei. Montag wieder voll. Er bemerkte, was er tat, und hörte damit auf.''',
'''Schon lief in seinem Kopf die nächste Woche an: zwei Termine am Samstag, Sonntagvormittag frei, Montag wieder voll. Als er bei Montag ankam, brach er die Rechnung ab.''')

# 2) Kapitel 8 – körperliche Reaktion direkter zeigen statt benennen.
R('08-01',
'''Daniel merkte, dass er den Atem angehalten hatte.\n\nEr ließ die Luft langsam aus.''',
'''Erst als die Brust spannte, fiel ihm auf, dass er den Atem anhielt. Langsam ließ er die Luft wieder aus.''')

# 3) Kapitel 13 – bekannte Erkenntnis nicht noch einmal mit "Daniel wusste" markieren.
R('13-01',
'''„Nicht ohne mehr.“\n\nDaniel wusste es.\n\nDie sauberen Wege lieferten ihm einen echten Wagen und eine echte Firma.\n\nNicht die Bedeutung.''',
'''„Nicht ohne mehr.“\n\nDie sauberen Wege lieferten ihm einen echten Wagen und eine echte Firma, aber keine Bedeutung.''')

# 4) Kapitel 17 – Konsequenz körperlich fließender erzählen.
R('17-01',
'''Er hatte sich auf die Konsequenz vorbereitet.\n\nNicht bewusst. Sein Körper hatte es getan.\n\nSeit Beginn des Gesprächs saß er mit beiden Füßen fest auf dem Boden, als müsste er gleich aufstehen. Sein Dienstausweis lag nicht wie sonst in der Jackentasche, sondern auf dem Tisch. Er hatte ihn herausgenommen, bevor Berg gekommen war.''',
'''Er hatte sich auf die Konsequenz vorbereitet, ohne es bewusst zu beschließen. Seit Beginn des Gesprächs saß er mit beiden Füßen fest auf dem Boden, als müsste er gleich aufstehen. Sein Dienstausweis lag nicht wie sonst in der Jackentasche, sondern auf dem Tisch. Er hatte ihn herausgenommen, bevor Berg gekommen war.''')

R('17-02',
'''„Sobald die Lage es zulässt.“\n\nDaniel merkte, wie er fast lachte. Derselbe Satz wie bei der Meldepflicht. Alles hing inzwischen an Zeit.\n\n„Und bis dahin?“''',
'''„Sobald die Lage es zulässt.“\n\nEin Lachen stieg ihm hoch und blieb irgendwo vor dem Mund stecken. Derselbe Satz wie bei der Meldepflicht. Alles hing inzwischen an Zeit.\n\n„Und bis dahin?“''')

# 5) Kapitel 18 – Quellenprüfung: Reflexion weniger formelhaft markieren.
R('18-01',
'''Nicht Hellers Name.\n\nDaniel merkte, wie sofort Erleichterung aufkam.\n\nEr hielt dagegen.''',
'''Nicht Hellers Name.\n\nDie Erleichterung kam zu schnell. Daniel hielt dagegen, bevor sie zur Schlussfolgerung wurde.''')

R('18-02',
'''Er sortierte sie nur hinter die Zeitfrage.\n\nDas war sein Doppelspiel ab jetzt:\n\nWas die Quelle über den Fall wusste, wurde geprüft wie jeder andere Hinweis.\n\nWas sie über Daniel und den internen Ablauf wusste, wurde separat gegen mögliche Informationswege geprüft.''',
'''Er sortierte sie nur hinter die Zeitfrage.\n\nVon jetzt an liefen zwei Prüfungen nebeneinander: Was die Quelle über den Fall wusste, wurde geprüft wie jeder andere Hinweis. Was sie über Daniel und den internen Ablauf wusste, lief separat gegen mögliche Informationswege.''')

# 6) Kapitel 22 – eine typische Nicht-X/Y-Antithese in normale Prosa zurückführen.
R('22-01',
'''Um 18.40 Uhr hatte er nicht mehr daran gedacht.\n\nNicht entschieden, den Termin abzusagen.\n\nEinfach etwas anderes höher gewichtet.''',
'''Um 18.40 Uhr hatte er nicht mehr daran gedacht. Er hatte den Termin nicht bewusst abgesagt; etwas anderes hatte schlicht höher gewogen.''')

# 7) Kapitel 27 – Einwand und Körpersignal direkter.
R('27-01',
'''„Und wenn sie gerade unterwegs ist?“\n\nDas war ein guter Einwand.\n\nDaniel mochte ihn nicht.''',
'''„Und wenn sie gerade unterwegs ist?“\n\nDer Einwand war gut genug, dass Daniel ihn nicht mochte.''')

R('27-02',
'''„Weil du wieder stehst.“\n\nDaniel merkte erst jetzt, dass er noch immer nicht saß.\n\nEr zeigte ihr die letzte Zeile.''',
'''„Weil du wieder stehst.“\n\nEr stand tatsächlich noch immer. Erst jetzt fiel es ihm auf.\n\nEr zeigte ihr die letzte Zeile.''')

# 8) Kapitel 32 – Mara: Unsicherheit bekommt bewusst mehr Satzraum.
R('32-01',
'''Mara antwortete nicht sofort.\n\nDaniel wusste es, bevor sie sprach.\n\n„Heute.“''',
'''Mara antwortete nicht sofort. Die Pause reichte.\n\n„Heute.“''')

R('32-02',
'''„Ich weiß noch nicht, wie oft ich am Anfang nach Berlin komme“, sagte Mara.\n\nDaniel merkte, wie sofort wieder ein Kalender in seinem Kopf aufging.\n\n„Die ersten zwei Wochen gar nicht?“''',
'''„Ich weiß noch nicht, wie oft ich am Anfang nach Berlin komme“, sagte Mara.\n\nIn seinem Kopf sprang sofort wieder der Kalender auf.\n\n„Die ersten zwei Wochen gar nicht?“''')

R('32-03',
'''Daniel ließ den Kalender im Kopf geschlossen.\n\nDas war ungewohnt genug, dass er die Pause hörte.\n\nMara auch.''',
'''Diesmal blieb der Kalender zu. Die Pause bekam Raum.\n\nMara hörte sie ebenfalls.''')

R('32-04',
'''Er merkte, wie sehr er sonst versucht hätte, Unsicherheit durch einen Rhythmus zu ersetzen.\n\nFreitagabend Zug.\n\nSonntag zurück.\n\nJedes zweite Wochenende.\n\nEin Plan, der schon durch seine Existenz beruhigend aussah.''',
'''Normalerweise hätte er die Unsicherheit sofort in einen Rhythmus gezwängt: Freitagabend Zug, Sonntag zurück, jedes zweite Wochenende. Ein Plan, der schon durch seine Existenz beruhigend aussah.''')

# 9) Kapitel 35 – Beweiskette: Formeln reduzieren, Faktendichte behalten.
R('35-01',
'''„So sauber ist es nicht. Der Verarbeitungsschritt läuft über den damaligen Arbeitsbereich. Mehrere Leute hatten Zugriff.“\n\nDaniel merkte, dass ihn die Antwort erleichterte.\n\nNur kurz.''',
'''„So sauber ist es nicht. Der Verarbeitungsschritt läuft über den damaligen Arbeitsbereich. Mehrere Leute hatten Zugriff.“\n\nDie Antwort erleichterte ihn. Für einen Moment.''')

R('35-02',
'''Neben dem Kennzeichen stand ein knapper Orts- und Zeitbezug aus einem anderen Lagefragment. Das Fahrzeug war im Umfeld eines bereits bekannten Randkontakts aufgefallen. Nicht lange. Nicht bei einer Straftat. Aber genug, um es bei einer gezielten Prüfung nicht einfach wegzulassen.''',
'''Neben dem Kennzeichen stand ein knapper Orts- und Zeitbezug aus einem anderen Lagefragment. Das Fahrzeug war im Umfeld eines bereits bekannten Randkontakts aufgefallen, nur kurz und ohne Straftat. Aber lange genug, um es bei einer gezielten Prüfung nicht einfach wegzulassen.''')

# 10) Kapitel 37 – Hellers Hebel als längere Gedankenbewegung.
R('37-01',
'''Nur das Summen der Lüftung und Jonas, der zwischen zwei Systemständen wechselte.\n\nDaniel merkte, wie schwer es war, Warten auszuhalten, nachdem er gelernt hatte, Warten als Risiko zu lesen.\n\nGenau darin lag Hellers stärkster Hebel.''',
'''Nur das Summen der Lüftung und Jonas, der zwischen zwei Systemständen wechselte.\n\nSeit Daniel Warten als Risiko zu lesen gelernt hatte, fühlte sich jede Minute Stillstand wie eine Entscheidung an. Darin lag Hellers stärkster Hebel.''')

# 11) Kapitel 41 – unmittelbarer Nachhall des Schusses: kurze Flash-Fragmente
# in eine einmalig längere, körperlichere Satzbewegung überführen.
R('41-01',
'''Daniel merkte, dass er zweimal dieselbe Zeile lesen musste. Die Buchstaben waren nicht unscharf. Seine Konzentration sprang nur für Sekunden zurück unter das Vordach.\n\nHellers Hand.\n\nDer Knall.\n\nDann wieder der Bildschirm.''',
'''Daniel las dieselbe Zeile zweimal. Die Buchstaben waren scharf, nur sein Kopf war für zwei Sekunden wieder unter dem Vordach: Hellers Hand, der Knall, nasser Beton. Dann zwang ihn der Bildschirm zurück.''')

R('41-02',
'''Aber das gesicherte Material, die realen Zugänge und das veränderte Zeitfenster reichten, um den Gefahrenkern zu tragen.\n\nDaniel merkte, wie wenig Erleichterung das brachte.\n\nEs war fast schlimmer, dass die Wirklichkeit wieder nicht sauber genug war, um irgendeine Seite moralisch zu retten.\n\nDaniel merkte erst da, dass seine linke Hand leicht zitterte.''',
'''Aber das gesicherte Material, die realen Zugänge und das veränderte Zeitfenster reichten, um den Gefahrenkern zu tragen.\n\nErleichterung blieb aus. Fast schlimmer war, dass die Wirklichkeit wieder nicht sauber genug war, um irgendeine Seite moralisch zu retten.\n\nUnter der Tischkante zitterte seine linke Hand leicht.''')

# 12) Kapitel 42 – Jana: emotionale Konsequenz nicht als weitere Checkliste erzählen.
R('42-01',
'''Daniel nickte.\n\nEr merkte, dass der Unterschied klein aussah und trotzdem groß war.\n\nEr gab Jana keine Liste mehr, die sie abarbeiten sollte.\n\nEr gab ihr den Stand.\n\nWas sie daraus machte, blieb bei ihr.''',
'''Daniel nickte.\n\nDer Unterschied sah klein aus und reichte doch bis in jede ihrer nächsten Entscheidungen: keine Liste mehr zum Abarbeiten, nur der Stand. Was Jana daraus machte, blieb bei ihr.''')

R('42-02',
'''Die Wohnung der Mutter hatte weiter existiert, während Daniel glaubte, der Fall verschlinge jede verfügbare Wirklichkeit.\n\nMakler.\n\nFotos.\n\nVollmacht.\n\nEin nächster Termin.\n\nNicht dramatisch.\n\nNur Leben, das keine Freigabe von seiner Lage brauchte.''',
'''Die Wohnung der Mutter hatte weiter existiert, während Daniel geglaubt hatte, der Fall verschlinge jede verfügbare Wirklichkeit: Makler, Fotos, Vollmacht, ein nächster Termin. Nichts daran war dramatisch. Es war einfach Leben, das keine Freigabe von seiner Lage brauchte.''')

# 13) Kapitel 45 – Hamburg: bewusst anderes Register für Alltag und Beziehung.
R('45-01',
'''Die Wohnung war kleiner als ihre alte gemeinsame in Berlin.\n\nNicht provisorisch.\n\nDas hatte Daniel beim ersten Besuch überrascht.''',
'''Die Wohnung war kleiner als ihre alte gemeinsame in Berlin, aber sie wirkte nicht provisorisch. Das hatte Daniel beim ersten Besuch überrascht.''')

R('45-02',
'''Als der Ständer gerade stand, stellte Daniel den Schraubenzieher zurück in die Schublade, in der Mara ihn inzwischen aufbewahrte.\n\nEr wusste, wo sie war, weil er zum dritten Mal hier war.\n\nDas war nicht Zuhause.\n\nAber auch nicht mehr Besuch bei einer Fremden.''',
'''Als der Ständer gerade stand, stellte Daniel den Schraubenzieher zurück in die Schublade, in der Mara ihn inzwischen aufbewahrte. Beim dritten Besuch wusste er bereits, wo sie war.\n\nNoch nicht Zuhause. Aber längst mehr als Besuch bei einer Fremden.''')

R('45-03',
'''Es gab inzwischen viele Menschen in Maras Alltag, die er nur aus halben Sätzen kannte.\n\nNicht weil sie sie ihm verschwieg.\n\nWeil er nicht dabei gewesen war, als sie wichtig geworden waren.''',
'''Es gab inzwischen viele Menschen in Maras Alltag, die er nur aus halben Sätzen kannte. Sie verschwieg sie ihm nicht; er war nur nicht dabei gewesen, als sie wichtig geworden waren.''')

# 14) Kapitel 46/47 – Normalisierung des Instruments: längere Satzbewegung als
# bewusster Kontrast zum früheren Ausnahmezustand.
R('46-01',
'''Daniel sah zu ihm.\n\nNicht weil der Vorschlag falsch war.\n\nWeil er so normal klang.''',
'''Daniel sah zu ihm. Der Vorschlag störte ihn nicht, weil er falsch klang, sondern weil er so normal klang.''')

R('46-02',
'''Jetzt war die Reibung nicht verschwunden.\n\nSie hatte Formulare bekommen.\n\nRollen.\n\nSchwellen.\n\nZuständigkeiten.\n\nDas war besser als Improvisation.\n\nUnd zugleich der Beweis, dass das Instrument nicht mehr improvisiert war.\n\nNiemand im Raum fragte, ob eine solche Verknüpfung grundsätzlich in Ordnung war.\n\nSie diskutierten nur den Kreis.\n\nDaniel merkte es, während Lena einen der Nachtzugriffe markierte.''',
'''Die Reibung war nicht verschwunden; sie hatte Formulare, Rollen, Schwellen und Zuständigkeiten bekommen. Das machte die Arbeit besser als Improvisation und zeigte zugleich, dass das Instrument längst keine Improvisation mehr war.\n\nErst während Lena einen der Nachtzugriffe markierte, fiel Daniel auf, dass niemand im Raum noch fragte, ob eine solche Verknüpfung grundsätzlich in Ordnung war. Sie diskutierten nur den Kreis.''')

R('47-01',
'''Keiner war falsch.\n\nDas war der gefährliche Teil.\n\nJonas hatte nicht vergessen, dass Fehlzuordnungen existierten.''',
'''Beide Sätze konnten gleichzeitig stimmen. Darin lag die Gefahr.\n\nJonas hatte nicht vergessen, dass Fehlzuordnungen existierten.''')

# Heller-Ambiguität bewusst NICHT erweitern: Der bestehende Text formuliert bereits
# explizit, dass es keine letzte Aussage / saubere Motivformel gibt und offene Punkte
# nach Hellers Tod bestehen bleiben. Das ist die gewünschte bewusste Leerstelle.

# Structural safety checks.
assert re.findall(r'^## (Prolog|\d+)$', text, re.M) == ['Prolog'] + [str(i) for i in range(1,48)]
assert text.rstrip().endswith('„Wie belastbar ist deine Gegenhypothese?“')
assert '—' not in text
assert 'Es gab keine letzte Aussage, keine saubere Motivformel' in text
assert 'Auch dort wird es offene Punkte geben, die sein Tod nicht mehr schließen lässt.' in text

old_words=len(re.findall(r"\b[\wÄÖÜäöüß]+(?:[-’'][\wÄÖÜäöüß]+)*\b", original, re.UNICODE))
new_words=len(re.findall(r"\b[\wÄÖÜäöüß]+(?:[-’'][\wÄÖÜäöüß]+)*\b", text, re.UNICODE))
if abs(new_words-old_words) > 150:
    raise SystemExit(f'word delta too large: {old_words}->{new_words}')

PATH.write_text(text, encoding='utf-8')
print(f'STYLE_DEPTH_PASS_OK words {old_words}->{new_words} ({new_words-old_words:+d})')

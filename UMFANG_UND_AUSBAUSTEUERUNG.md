# Umfang und Ausbausteuerung

## Zweck

Diese Datei ist die verbindliche Umfangssteuerung für die Ausarbeitung des bestehenden Romans. Die Storyarchitektur aus `ROMAN_MAP.md` bleibt bestehen; gesteuert wird die Tiefe und Ausspielung der bereits vorhandenen Szenen.

## Überziel

- Zielprodukt: vollständiger deutschsprachiger Psychothriller im geplanten Romanumfang
- Zielwert: **ca. 380 gedruckte Seiten**
- Produktionskorridor: **75.000–80.000 Wörter**
- Steuerwert für die Planung: **77.000 Wörter**

Die Seitenzahl ist ein Zielbild, die Wortzahl ist die operative Steuerungsgröße. Satzspiegel, Schrift, Kapitelanfänge und Dialoganteil verändern die spätere reale Seitenzahl.

## Baseline nach #25 – Ist gegen Ziel

Die Baseline wurde am 26.08.2026 direkt aus den fünf Dateien unter `MANUSKRIPT/` ermittelt. Die vollständigen und automatisch aktualisierten Kapitelwerte stehen in `MANUSKRIPT_METRIKEN.md`.

| Baustein | Funktion | Ist Wörter | Steuerwert | Lücke | Ziel erreicht |
|---|---|---:|---:|---:|---:|
| 01 | Cold Open | 198 | 1.200 | 1.002 | 16,5 % |
| 02 | Ausgangswelt Daniel | 3.306 | 9.000 | 5.694 | 36,7 % |
| 03 | Auslösendes Ereignis | 4.310 | 11.000 | 6.690 | 39,2 % |
| 04 | Erste Entscheidung | 2.456 | 8.500 | 6.044 | 28,9 % |
| 05 | Entdeckung & Eskalation | 3.890 | 12.000 | 8.110 | 32,4 % |
| 06 | Moralischer / psychologischer Kipppunkt | 3.840 | 13.000 | 9.160 | 29,5 % |
| 07 | Reversal / Umdeutung | 3.693 | 7.000 | 3.307 | 52,8 % |
| 08 | Finale Entscheidung & Konsequenz | 3.840 | 10.500 | 6.660 | 36,6 % |
| 09 | Nachhall / Schlussszene | 1.837 | 4.800 | 2.963 | 38,3 % |
| **Gesamt** |  | **27.370** | **77.000** | **49.630** | **35,5 %** |

### Erste quantitative Diagnose

- Es fehlt **kein einzelner Baustein**; alle neun liegen deutlich unter ihrem vorgesehenen Roman-Gewicht.
- Relativ am weitesten ausgearbeitet ist Baustein 07 mit 52,8 %.
- Besonders untergewichtet sind Baustein 04 (28,9 %), Baustein 06 (29,5 %) und Baustein 05 (32,4 %).
- Die quantitative Untergewichtung ist noch **kein automatischer Schreibauftrag**. Sie bestimmt, wo die qualitative Kapitel-Diagnose zuerst besonders kritisch prüfen muss, ob Konflikt, Psychologie, Suspense, Figureninteraktion, Situation oder Konsequenz derzeit nur komprimiert abgearbeitet werden.

## Verbindliche Umfangsbudgets je Baustein

| Baustein | Funktion | Steuerwert Wörter |
|---|---|---:|
| 01 | Cold Open | 1.200 |
| 02 | Ausgangswelt Daniel | 9.000 |
| 03 | Auslösendes Ereignis | 11.000 |
| 04 | Erste Entscheidung | 8.500 |
| 05 | Entdeckung & Eskalation | 12.000 |
| 06 | Moralischer / psychologischer Kipppunkt | 13.000 |
| 07 | Reversal / Umdeutung | 7.000 |
| 08 | Finale Entscheidung & Konsequenz | 10.500 |
| 09 | Nachhall / Schlussszene | 4.800 |
| **Gesamt** |  | **77.000** |

Die Bausteinwerte sind Steuerwerte, keine mechanischen Füllvorgaben. Der Gesamtroman soll am Ende im Korridor 75.000–80.000 Wörter liegen. Abweichungen einzelner Bausteine sind zulässig, wenn sie dramaturgisch begründet und an anderer Stelle ausgeglichen werden.

## Automatische Ist-Messung

`MANUSKRIPT_METRIKEN.md` wird aus den aktuellen Manuskriptdateien automatisch erzeugt und enthält:

- Gesamtwortzahl
- Ist / Ziel / Lücke je Baustein
- exakte aktuelle Wortzahl für Prolog + Kapitel 1–47

Die Messung läuft bei Änderungen unter `MANUSKRIPT/**` automatisch über `.github/workflows/manuskript-metriken.yml`.

Damit existieren zwei bewusst getrennte Ebenen:

1. **Baseline / Zielsteuerung hier:** Was soll der Roman als Ganzes und je Baustein tragen?
2. **laufende Messung in `MANUSKRIPT_METRIKEN.md`:** Wie viel Text steht aktuell tatsächlich im Repo?

## Steuerungsebene unterhalb der Bausteine

Für **Prolog + Kapitel 1–47** wird in `AUSBAU_MATRIX.md` die qualitative und quantitative Ausbauplanung festgelegt. Die aktuellen Ist-Werte werden aus `MANUSKRIPT_METRIKEN.md` übernommen.

Für jede Storyeinheit werden verbindlich dokumentiert:

1. aktuelle Wortzahl
2. Zielkorridor `min / Ziel / max`
3. Differenz `Ist → Ziel`
4. Szenenfunktion laut `ROMAN_MAP.md`
5. qualitative Diagnose: Was ist bereits voll ausgespielt, was nur komprimiert?
6. konkrete Ausbauhebel
7. 2–4 konkrete Ausbauaufträge
8. geschützte Informationen / Grenzen, die nicht verschoben werden dürfen
9. Ergebnis-Wortzahl nach Umsetzung

Die Summe der Kapitel-Zielwerte eines Bausteins muss dessen Steuerwert plausibel abbilden. Nicht jedes Kapitel wird gleich lang. Schlüssel-, Reversal- und Entscheidungsszenen dürfen deutlich mehr Raum erhalten als Übergangs- oder Nachhallkapitel.

### Diagnose-Reihenfolge

Die Kapitelanalyse beginnt nicht bei Kapitel 1 und verteilt Wörter mechanisch, sondern priorisiert zunächst:

1. **besonders kurze Kapitel mit hoher dramaturgischer Last**
2. **Bausteine mit besonders großer relativer oder absoluter Lücke**
3. **Schlüsselstellen der psychologischen Entwicklung**
4. danach die übrigen Kapitel zur rhythmischen Gesamtverteilung

Die automatische Baseline markiert hierfür bereits Kandidaten; die Entscheidung über den Ausbau fällt erst nach Lesen der jeweiligen Szene gegen Szenenkarte, Figuren, Leserwissen und Folgekapitel.

## Zulässige Ausbauhebel

Ausbau erfolgt innerhalb der bestehenden Storyfunktion durch konkrete Romanarbeit:

- **Handlung und Widerstand:** vorhandene Entscheidung, Prüfung oder Konfrontation vollständiger ausspielen
- **Psychologische Verarbeitung:** Wahrnehmung, körperliche Reaktion, Selbstkorrektur, Rechtfertigung und Nachwirkung sichtbar machen
- **Figureninteraktion und Subtext:** bestehende Beziehungen und Gegenpositionen stärker in Handlung und Dialog tragen
- **Suspense und Informationsgewinn:** vorhandene Information über Prüfung, Verzögerung, Unsicherheit und Reaktion verdienen lassen
- **Raum und Situation:** Schauplatz, Bewegung, Geräusche, Körperlichkeit und situative Details so ergänzen, dass die Szene erlebt statt nur abgearbeitet wird
- **Konsequenz:** Folgen vorheriger Entscheidungen in der nächsten vorhandenen Szene spürbar machen

Jede Erweiterung muss mindestens einen dieser Hebel konkret bedienen und zur bestehenden Szenenfunktion beitragen.

## Kapitel-Auftrag statt pauschalem Aufblähen

Für jedes Kapitel werden vor der Umsetzung **2–4 konkrete Ausbauaufträge** formuliert. Beispielstruktur:

- `Kapitel 19 – Mika-Verhör`
  - Verhördynamik stärker als Macht- und Unsicherheitssituation ausspielen
  - Mikas Eigeninteresse und Daniels Fehleinschätzung über konkrete Reaktionen sichtbar machen
  - Lenas Gegenrolle stärker als Verhalten im Raum statt Erklärung tragen
  - Erkenntnis, dass Mika Randakteur ist, schrittweise verdienen

Erst wenn diese Aufträge feststehen, wird Prosa ergänzt.

## Arbeitsablauf

### Phase A – Vermessen und planen
- [x] exakte Wortzahl je Kapitel und Baustein ermitteln (`MANUSKRIPT_METRIKEN.md`)
- [ ] jedes Kapitel qualitativ gegen seine Szenenfunktion diagnostizieren
- [ ] Ausbau-Matrix für Prolog + 47 Kapitel erstellen
- [ ] Zielkorridore so verteilen, dass der Roman auf ca. 77.000 Wörter geplant ist
- [ ] pro Kapitel 2–4 konkrete Ausbauaufträge festlegen

### Phase B – Bausteine ausbauen
Umsetzung in der bestehenden Reihenfolge 01 → 09. Nach jedem Arbeitsblock:
- aktuelle und neue Wortzahl dokumentieren
- Szenenfunktion und Leserwissen gegen `ROMAN_MAP.md` prüfen
- Stil gegen `STILREFERENZ.md` prüfen
- keine unbeabsichtigte Plot- oder Faktenänderung akzeptieren

### Phase C – Globaler Qualitätscheck nach Ausbau
Nach Abschluss aller Bausteine erneut prüfen:
- Page-Turner / Rhythmus
- Continuity / Fakten
- Figurenentwicklung / psychologische Progression
- Stil / Anti-KI
- Gesamtumfang 75.000–80.000 Wörter

### Phase D – Finalisierung
Erst danach `#26 Finaler Manuskript-Pass und Abschlussfassung erstellen` durchführen.

## Definition of Done für den Ausbau

Der Ausbau ist abgeschlossen, wenn:

- alle 9 Bausteine und Prolog + Kapitel 1–47 weiterhin vollständig vorhanden sind,
- für jedes Kapitel Soll und Ist dokumentiert sind,
- der Gesamtroman **75.000–80.000 Wörter** erreicht,
- die Ausbaupunkte aus der Matrix umgesetzt oder begründet verworfen wurden,
- Storyarchitektur, Leserwissen, Reversal, Finale und Nachhall unverändert funktionieren,
- der Text als Roman ausformuliert wirkt und nicht nur als hochkomprimierte Vollfassung,
- der globale Qualitätscheck nach dem Ausbau bestanden ist.

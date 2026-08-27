# Umfang und Ausbausteuerung

## Zweck

Diese Datei ist die verbindliche Umfangssteuerung für die Ausarbeitung des bestehenden Romans. Die Storyarchitektur aus `ROMAN_MAP.md` bleibt bestehen; gesteuert wird die Tiefe und Ausspielung der bereits vorhandenen Szenen.

## Aktuelle Steuerungsregel ab #39 – Qualität vor Wortziel

Die nachfolgenden Wortziele dokumentieren die **historische Ausbauplanung**. Für die abgenommene Vollfassung und alle weiteren Lektorats-/Testleser-Pässe sind sie **kein Abnahmekriterium mehr**.

- **Umfang folgt Funktion.**
- Wortzahl wird weiter automatisch gemessen, aber nicht mechanisch optimiert.
- Es wird weder aufgefüllt noch gekürzt, nur um einen Korridor zu treffen.
- Eine Kürzung ist richtig, wenn sie Leserwirkung verbessert; eine Erweiterung ist richtig, wenn eine vorhandene Szene dadurch glaubwürdiger, konkreter oder emotional vollständiger wird.
- Plot-, Figuren- und Romanfunktion haben Vorrang vor Soll/Ist-Werten.

Diese Regel überschreibt für die aktuelle Manuskriptphase alle später in dieser Datei genannten Formulierungen, nach denen 75.000–80.000 Wörter oder 77.000 Wörter zwingend erreicht werden müssten. Die Werte bleiben ausschließlich als historische Planungs- und Vergleichsdaten erhalten.

## Überziel

- Zielprodukt: vollständiger deutschsprachiger Psychothriller im geplanten Romanumfang
- Zielbild: **ca. 380 gedruckte Seiten**
- Produktionskorridor: **75.000–80.000 Wörter**
- Planungs-Steuerwert: **77.000 Wörter**

Die Seitenzahl ist das Produktziel, die Wortzahl die operative Steuerungsgröße. Satzspiegel, Schrift, Kapitelanfänge und Dialoganteil beeinflussen die spätere reale Seitenzahl.

## Verbindliche Git-Arbeitsregel

Die weitere Manuskript-, Analyse- und Ausbauarbeit erfolgt **direkt auf `main`**.

- keine Feature-Branches für Kapitel-/Baustein-Ausarbeitung
- keine Pull-Request-Kette als Voraussetzung
- kleine, nachvollziehbare Commits direkt auf `main`
- vor jedem Manuskript-Commit aktuellen `main`-Stand berücksichtigen

Diese Regel gilt bis zur finalen Manuskriptfassung, sofern sie nicht ausdrücklich geändert wird.

## Baseline nach #25 – Ist gegen Ziel

Die Baseline wurde direkt aus den fünf Dateien unter `MANUSKRIPT/` ermittelt. `MANUSKRIPT_METRIKEN.md` enthält die automatisch aktualisierten Ist-Werte für Prolog + Kapitel 1–47.

Die qualitative Diagnose in `AUSBAU_MATRIX.md` hat die erste grobe Bausteinverteilung an zwei Stellen korrigiert: Der Cold Open bleibt bewusst knapp und erhält **800 statt 1.200 Wörter**; die frei werdenden 400 Wörter gehen an den psychologisch zentralen Baustein 06, der damit **13.400 statt 13.000 Wörter** erhält. Das Gesamtziel bleibt unverändert 77.000 Wörter.

| Baustein | Funktion | Ist Wörter | Steuerwert | Lücke | Ziel erreicht |
|---|---|---:|---:|---:|---:|
| 01 | Cold Open | 198 | 800 | 602 | 24,8 % |
| 02 | Ausgangswelt Daniel | 3.306 | 9.000 | 5.694 | 36,7 % |
| 03 | Auslösendes Ereignis | 4.310 | 11.000 | 6.690 | 39,2 % |
| 04 | Erste Entscheidung | 2.456 | 8.500 | 6.044 | 28,9 % |
| 05 | Entdeckung & Eskalation | 3.890 | 12.000 | 8.110 | 32,4 % |
| 06 | Moralischer / psychologischer Kipppunkt | 3.840 | 13.400 | 9.560 | 28,7 % |
| 07 | Reversal / Umdeutung | 3.693 | 7.000 | 3.307 | 52,8 % |
| 08 | Finale Entscheidung & Konsequenz | 3.840 | 10.500 | 6.660 | 36,6 % |
| 09 | Nachhall / Schlussszene | 1.837 | 4.800 | 2.963 | 38,3 % |
| **Gesamt** |  | **27.370** | **77.000** | **49.630** | **35,5 %** |

### Quantitative Einordnung

- Es fehlt **kein einzelner Baustein**; alle neun sind vorhanden.
- Die Unterlänge ist systematisch: Viele Szenen erfüllen bereits ihre Plotfunktion, sind aber als Roman stark verdichtet.
- Relativ am weitesten ausgearbeitet ist Baustein 07 mit 52,8 %.
- Besonders untergewichtet sind Baustein 06 (28,7 %), Baustein 04 (28,9 %) und Baustein 05 (32,4 %).
- Wortzahl allein löst keinen Schreibauftrag aus. Die qualitative Diagnose und die konkreten Ausbauaufträge stehen verbindlich in `AUSBAU_MATRIX.md`.

## Verbindliche Umfangsbudgets je Baustein

| Baustein | Funktion | Steuerwert Wörter |
|---|---|---:|
| 01 | Cold Open | 800 |
| 02 | Ausgangswelt Daniel | 9.000 |
| 03 | Auslösendes Ereignis | 11.000 |
| 04 | Erste Entscheidung | 8.500 |
| 05 | Entdeckung & Eskalation | 12.000 |
| 06 | Moralischer / psychologischer Kipppunkt | 13.400 |
| 07 | Reversal / Umdeutung | 7.000 |
| 08 | Finale Entscheidung & Konsequenz | 10.500 |
| 09 | Nachhall / Schlussszene | 4.800 |
| **Gesamt** |  | **77.000** |

Die Werte sind Steuerwerte, keine mechanischen Füllvorgaben. Der Gesamtroman soll im Korridor 75.000–80.000 Wörter liegen. Abweichungen einzelner Kapitel oder Bausteine sind zulässig, wenn sie dramaturgisch begründet und sinnvoll ausgeglichen werden.

## Steuerung unterhalb der Bausteine

`AUSBAU_MATRIX.md` ist die verbindliche Kapitelsteuerung. Für Prolog + Kapitel 1–47 enthält sie jeweils:

1. aktuelle Wortzahl
2. Zielkorridor `min / Ziel / max`
3. Differenz `Ist → Ziel`
4. Szenenfunktion
5. qualitative Diagnose
6. 2–4 konkrete Ausbauaufträge
7. geschützte Plot-, Leserwissens- und Faktengrenzen

Die Kapitelwerte eines Bausteins ergeben dessen Steuerwert. Nicht jedes Kapitel wird gleich lang; Schlüssel-, Entscheidungs-, Reversal- und Finaleszenen erhalten dort mehr Raum, wo ihre vorhandene Funktion dies erfordert.

## Zulässige Ausbauhebel

Ausbau erfolgt ausschließlich innerhalb bestehender Storyfunktionen:

- **Handlung und Widerstand:** vorhandene Prüfung, Entscheidung oder Konfrontation vollständiger ausspielen
- **Psychologische Verarbeitung:** Wahrnehmung, körperliche Reaktion, Selbstkorrektur, Rechtfertigung und Nachwirkung sichtbar machen
- **Figureninteraktion und Subtext:** bestehende Beziehungen und Gegenpositionen stärker tragen
- **Suspense und Informationsgewinn:** vorhandene Information über Prüfung, Verzögerung, Unsicherheit und Reaktion verdienen lassen
- **Raum und Situation:** Schauplatz, Bewegung und konkrete situative Wahrnehmung stärker erlebbar machen
- **Konsequenz:** Folgen bereits gesetzter Entscheidungen in vorhandenen Szenen spürbar machen

Keine neue Plotlogik, neue Figuren, neue Twists oder Nebenhandlungen nur zur Umfangserhöhung.

## Automatische Ist-Messung

`MANUSKRIPT_METRIKEN.md` wird bei Änderungen unter `MANUSKRIPT/**` automatisch durch `.github/workflows/manuskript-metriken.yml` erzeugt und enthält:

- Gesamtwortzahl
- Ist / Ziel / Lücke je Baustein
- aktuelle Wortzahl für Prolog + Kapitel 1–47

Für die Repo-Steuerung ist diese reproduzierbare Zählung verbindlich; Microsoft Word kann geringfügig anders zählen.

## Arbeitskette

### #29 – Ausbauplanung
- Manuskript vermessen
- alle 48 Storyeinheiten qualitativ diagnostizieren
- Kapitel-Zielkorridore und Ausbauaufträge in `AUSBAU_MATRIX.md` festlegen

### #30 – Roman-Ausbau
- Prolog + Kapitel 1–47 in bestehender Reihenfolge ausarbeiten
- bestehende funktionierende Passagen nicht pauschal neu schreiben
- nach jedem Kapitel Ist gegen Zielkorridor sowie Story-/Wissens-/Stilgrenzen prüfen
- nach jedem Baustein Gesamtgewicht kontrollieren

### #26 – integrierter Finalcheck + Abschlussfassung
Nach #30 einmal als Gesamtroman prüfen:
- Page-Turner / Rhythmus
- Continuity / Fakten
- Figurenentwicklung / psychologische Progression
- Reversal / Finale / Nachhall
- Stil / Anti-KI
- Gesamtumfang 75.000–80.000 Wörter
- echte konsolidierte Abschlussfassung erzeugen

## Dependency

`#29 → #30 → #26`

Es wird **nicht** noch einmal die frühere Kette #22–#25 separat wiederholt.

## Definition of Done für den Ausbau

Der Ausbau ist abgeschlossen, wenn:

- Prolog + Kapitel 1–47 und alle 9 Bausteine weiterhin vollständig vorhanden sind,
- Soll/Ist je Kapitel und Baustein nachvollziehbar ist,
- der Gesamtroman 75.000–80.000 Wörter erreicht,
- die Ausbauaufträge aus `AUSBAU_MATRIX.md` umgesetzt oder begründet verworfen sind,
- Storyarchitektur, Leserwissen, Reversal, Finale und Nachhall unverändert funktionieren,
- der Text als vollständig ausgespielter Roman und nicht als hochkomprimierte Vollfassung wirkt,
- #26 den integrierten Abschlusscheck besteht.

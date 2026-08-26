# KONTEXTSYSTEM.md – Verbindlicher Arbeitskontext für den Roman

## Zweck

Dieses Dokument legt fest, **welcher Kontext bei welchem Arbeitsschritt zwingend vorliegen muss**.

Ziel ist nicht minimale Token-Nutzung, sondern maximale Konsistenz über einen langen Roman hinweg. Moderne LLMs können deutlich mehr Kontext verarbeiten; deshalb wird bei qualitätskritischen Schritten bewusst mehr Kontext mitgegeben.

Die zentrale Regel lautet:

> **Zu wenig Kontext ist bei diesem Roman gefährlicher als einige zusätzliche Tausend Tokens.**

Stil, Figurenstimme, Leserwissen, Doppelboden, Ereignisse, Beats und Szenenfunktion müssen gemeinsam berücksichtigt werden.

---

## 1. Single Sources of Truth

Diese Dateien bleiben die maßgeblichen Master-Dokumente:

- `BUCHIDEE.md` – Grundidee und moralischer Kern
- `ROTER_FADEN.md` – globale Plotlogik, Bedrohungsarchitektur, Doppelboden und Entwicklungsachsen
- `STILREFERENZ.md` – verbindliche Sprach- und Spannungsarchitektur
- `Bausteine_in_5_Ebenen_zerlegen.md` – Arbeitsmethodik und Ebenentrennung
- `PSYCHOTHRILLER_POSITIONIERUNG_UND_BAUSTEINE.md` – Genre- und Thriller-Leitplanken
- spätere Figurenprofile – verbindliche Figurenlogik
- jeweilige Ereignis-, Beat- und Szenenkarten-Dateien – lokaler Storyzustand

Issue-Texte dürfen diese Quellen **einbetten**, ersetzen sie aber nicht.

Wenn ein eingebetteter Kontext von der aktuellen Master-Datei abweicht, gilt die **aktuelle Master-Datei**.

---

## 2. Kontextstufen

### Stufe A – Struktur / Ereignisse / Beats

Typisch: Issues #7–#9.

Pflichtkontext:
- relevanter Abschnitt aus `ROTER_FADEN.md`
- relevante Ereignisdateien
- bereits vorhandene Beats an den Übergängen
- Doppelboden / Leserwissen der betroffenen Bausteine
- Entwicklungsachsen Daniel, Bedrohung, Wahrheit/Leserwissen, persönliche Bedrohung und Staat

`STILREFERENZ.md` muss hier **nicht vollständig eingebettet** werden, weil noch keine Romanprosa entsteht. Relevant sind nur Regeln, die Dramaturgie und Informationsdosierung beeinflussen.

Ziel: nicht mit Sprachdetails die Plotarbeit überfrachten.

---

### Stufe B – Figuren und Szenenkarten

Typisch: Issues #10–#15.

Pflichtkontext:
- `ROTER_FADEN.md`
- relevante Ereignisse und Beats
- aktuelle Figurenprofile
- `STILREFERENZ.md` **vollständig lesen**
- Doppelboden und Leserwissen der konkreten Stelle

Bei Szenenkarten muss zusätzlich explizit festgehalten werden:

1. Was weiß der Leser zu Beginn der Szene?
2. Was glaubt Daniel zu Beginn?
3. Welche Information kommt neu hinzu?
4. Welche alternative Lesart ist ebenfalls möglich?
5. Was soll der Leser am Ende glauben?
6. Was darf noch nicht verraten werden?
7. Welche Stil-/Spannungsregeln aus `STILREFERENZ.md` sind für diese Szene besonders relevant?

Die komplette Stilreferenz muss gelesen werden, wird aber nicht zwingend vollständig in jede einzelne Szenenkarte kopiert.

---

### Stufe C – Recherche / Plausibilität

Typisch: Issue #16.

Pflichtkontext:
- konkrete Szenenkarten
- relevante Ereignisse/Beats
- offene institutionelle, juristische, technische und operative Fragen
- `ROTER_FADEN.md` für die dramaturgische Funktion

Die Recherche darf die Storylogik nicht unbemerkt umschreiben. Wenn Plausibilität eine Änderung verlangt, muss diese bewusst zurück in die betreffende Storyebene gespielt werden.

`STILREFERENZ.md` ist hier nur relevant, wenn Rechercheergebnisse später sprachlich oder fachsprachlich eingebaut werden.

---

### Stufe D – Ausformulierung / Romanprosa

Typisch: Issues #17–#21.

Hier gilt **maximaler Kontext**.

Vor jeder Prosa-Arbeit müssen mindestens vorliegen:

1. **vollständige aktuelle `STILREFERENZ.md`**
2. relevante Szenenkarte
3. relevante Ereignisdatei und Beats
4. betreffende Figurenprofile
5. relevanter Doppelboden aus `ROTER_FADEN.md`
6. Storyzustand unmittelbar vor der Szene
7. Leserwissen zu Beginn
8. Daniels Wissens- und Interpretationsstand zu Beginn
9. gewünschter Wissensstand des Lesers am Ende
10. ausdrücklich zurückzuhaltende Informationen
11. Anschluss an vorherige und folgende Szene

### Verbindliche Regel

> Bei Prosa reicht ein Link auf `STILREFERENZ.md` nicht aus.

Der vollständige aktuelle Stiltext wird **direkt in den Arbeitskontext / Prompt eingebettet** oder technisch nachweisbar vollständig geladen.

Bei GitHub-Issues für die Ausformulierung wird der aktuelle Stilkontext direkt im Issue mitgeführt. Vor tatsächlicher Bearbeitung muss er trotzdem gegen die aktuelle `STILREFERENZ.md` geprüft und bei Abweichung aktualisiert werden.

---

## 3. Standard-Kontextkopf für Prosa

Jeder konkrete Schreibauftrag soll vor dem eigentlichen Auftrag diesen Kontext liefern:

### A. Verbindlicher Stilkontext
Vollständiger aktueller Inhalt aus `STILREFERENZ.md`.

### B. Szenenfunktion
- Baustein:
- Ereignis:
- Beat(s):
- Zweck der Szene im Gesamtroman:

### C. Figurenkontext
- POV:
- Ziel der POV-Figur:
- emotionaler Zustand:
- relevante Beziehungskonflikte:
- aktueller Stand von Daniels Entwicklung:

### D. Informationsarchitektur
- Leser weiß vor der Szene:
- Daniel weiß vor der Szene:
- neue Information:
- mögliche alternative Lesart:
- Leser soll danach glauben:
- darf noch nicht verraten werden:
- spätere Zweitlesart / Doppelboden:

### E. Kontinuität
- unmittelbarer Anschluss von:
- Szene muss enden mit:
- Fakten, die nicht verändert werden dürfen:

### F. Schreibauftrag
Erst danach beginnt die eigentliche Ausformulierung.

---

## 4. Qualitätsdurchläufe

### Structural Edit (#22)
Vollständiger Stiltext nicht zwingend, weil primär Struktur geprüft wird. Trotzdem Genre-, Leserwissens- und Doppelbodenlogik berücksichtigen.

### Page-Turner-Pass (#23)
`STILREFERENZ.md` vollständig einbetten/lesen. Fokus besonders auf Kapitelmechanik, Informationsdosierung, Weiterleseimpulse und Tempo.

### Continuity- und Fakten-Pass (#24)
Stiltext nur ergänzend. Primär Plot-, Zeit-, Figuren-, Wissens- und Faktenkonsistenz.

### Stil- und Sprach-Pass (#25)
`STILREFERENZ.md` vollständig einbetten. Anti-KI-Regeln und Daniels sich verändernde innere Sprache sind verbindliche Prüfkriterien.

### Finaler Manuskript-Pass (#26)
`STILREFERENZ.md` vollständig einbetten. Zusätzlich alle globalen Story- und Figurenleitplanken berücksichtigen.

---

## 5. Anti-Drift-Regel

Eingebetteter Kontext in Issues ist ein **Snapshot**, kein neuer Master.

Vor Beginn eines Issues mit eingebettetem Master-Text:

1. aktuelle Master-Datei lesen,
2. eingebetteten Stand vergleichen,
3. bei Abweichung den Issue-Kontext aktualisieren,
4. erst danach arbeiten.

Keine Prosa auf Basis eines veralteten Stil-Snapshots schreiben.

---

## 6. Kontext ist kein Selbstzweck

Mehr Kontext bedeutet nicht, dass jede Information in die Prosa gehört.

Der Kontext dient dazu, dass das Modell weiß:
- was wahr ist,
- was Daniel glaubt,
- was der Leser glaubt,
- was verschwiegen werden muss,
- welche Stimme der Roman hat.

Die Prosa selbst bleibt gemäß `STILREFERENZ.md` knapp, zugänglich und spannungsorientiert.

> **Viel Kontext im Arbeitsraum. Selektive Information im Roman.**

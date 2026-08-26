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
- relevante Thriller-Leitprinzipien aus `PSYCHOTHRILLER_POSITIONIERUNG_UND_BAUSTEINE.md`

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
- `PSYCHOTHRILLER_POSITIONIERUNG_UND_BAUSTEINE.md`
- Doppelboden und Leserwissen der konkreten Stelle

### Pflichtkern jeder Szenenkarte

1. POV
2. Ort / Zeitpunkt
3. Ziel der POV-Figur
4. Hindernis / Konflikt
5. konkreter Szenenablauf
6. neue relevante Information
7. Entscheidung
8. Konsequenz
9. Leserwissen vorher
10. Leserwissen danach
11. was noch nicht verraten werden darf
12. Anschluss / Weiterleseimpuls

Der **konkrete Szenenablauf** beschreibt typischerweise 4–10 Bewegungen innerhalb der Szene. Er gehört zur Szenenkarte und bildet keine zusätzliche sechste Planungsebene.

Zusatzmodule wie alternative Lesart, Doppelboden, Quellenwissen, motiviertes Framing, Beziehungskonflikt, Empathie-Reversal, Reframing oder Grenzverschiebung werden nur dort ausgefüllt, wo sie dramaturgisch relevant sind.

### 90%-Regel

Szenenkarten werden nicht pro forma maximal ausgefüllt. Ziel ist:

> **Genug Detail, dass beim Schreiben keine relevante Storyentscheidung mehr nötig ist – aber keine Dokumentation ohne Funktion.**

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

## 3. Prosa-Gate

Vor Beginn von Ebene 5 muss für **jede Szene** die Frage mit Ja beantwortet werden können:

> **Könnte ein Autor diese Szene jetzt schreiben, ohne selbst noch eine relevante Storyentscheidung treffen zu müssen?**

Vor Prosa müssen mindestens geklärt sein:

- anwesende Figuren
- was die POV-Figur will
- Konflikt / Hindernis
- konkreter Szenenablauf
- neue Information
- Daniels Interpretation
- gewünschte Leserannahme
- Entscheidung
- Konsequenz
- zurückzuhaltende Information
- Anschluss zur nächsten Szene
- unveränderliche Fakten

Bewusst offen bleiben dürfen nur Ausgestaltungsfragen wie Dialogwortlaut, Körpersprache, Mikro-Staging, konkrete Beschreibung, Rhythmus, Atmosphäre und sprachliche Bilder.

Wenn beim Schreiben noch Plot, Motiv, Wendung, Beziehung oder Leserinformation erfunden werden müsste, ist die Szene **nicht schreibbereit**.

---

## 4. Standard-Kontextkopf für Prosa

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

## 5. Qualitätsdurchläufe

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

## 6. Anti-Drift-Regel

Eingebetteter Kontext in Issues ist ein **Snapshot**, kein neuer Master.

Vor Beginn eines Issues mit eingebettetem Master-Text:

1. aktuelle Master-Datei lesen,
2. eingebetteten Stand vergleichen,
3. bei Abweichung den Issue-Kontext aktualisieren,
4. erst danach arbeiten.

Keine Prosa auf Basis eines veralteten Stil-Snapshots schreiben.

---

## 7. Discovery- / Rücksprung-Regel

Die Planung ist verbindlich, aber **nicht dogmatisch**.

Wenn bei Recherche, Szenenkartenarbeit oder Prosa eine nachweislich bessere Storylösung entdeckt wird, darf und soll sie geprüft werden. Sie wird jedoch **nicht spontan in die Prosa eingebaut**.

Verbindliches Vorgehen:

1. Arbeit an der betroffenen Stelle anhalten.
2. Die richtige Ursprungsebene bestimmen: Szene, Beat, Ereignis, Figur oder globale Plotlogik.
3. Änderung zuerst auf dieser Ebene einarbeiten.
4. Auswirkungen auf Leserwissen, Doppelboden, Figurenlogik, Kausalität und Kontinuität prüfen.
5. Betroffene nachgelagerte Ebenen synchronisieren.
6. Erst danach Prosa oder Detailarbeit fortsetzen.

Leitregel:

> **Die Planung darf sich verbessern. Die Prosa darf sie nicht heimlich überschreiben.**

Eine bessere Entdeckung ist kein Methodikbruch. Das direkte Improvisieren neuer Storylogik in einer ausformulierten Szene wäre einer.

---

## 8. Kontext ist kein Selbstzweck

Mehr Kontext bedeutet nicht, dass jede Information in die Prosa gehört.

Der Kontext dient dazu, dass das Modell weiß:
- was wahr ist,
- was Daniel glaubt,
- was der Leser glaubt,
- was verschwiegen werden muss,
- welche Stimme der Roman hat.

Die Prosa selbst bleibt gemäß `STILREFERENZ.md` knapp, zugänglich und spannungsorientiert.

> **Viel Kontext im Arbeitsraum. Selektive Information im Roman.**

# Manuskript-Formatierung

Diese Datei definiert die verbindliche Ausgabe-Logik für `AUSNAHMEZUSTAND_FINAL.md` und `AUSNAHMEZUSTAND.docx`.

## Verbindliches Ziel: Sebastian-Fitzek-Benchmark

Für die veröffentlichungsnahe Word-Fassung ist eine reale Roman-Doppelseite von Sebastian Fitzek der **visuelle Benchmark**. Ziel ist nicht nur, einzelne Word-Parameter zu übernehmen, sondern das Gesamtbild möglichst nah zu treffen: kompakter Thriller-Buchsatz, dichter Satzspiegel, ruhige Absatzkante und klassische Buchtypografie.

Die Referenz hat die früheren Zwischenlösungen verworfen:

- `0 cm Einzug + 4 pt Absatzabstand` war zwar ruhig, wirkte bei vielen kurzen Dialogabsätzen aber zu listen-/protokollartig.
- `Erstzeileneinzug + 0 pt Absatzabstand` erzeugte bei diesem Roman durch die vielen kurzen Absätze das störende Zickzack mehrerer linker Ebenen.
- `Times New Roman` ließ die Ausgabe trotz Buchparametern weiterhin wie ein Word-Manuskript wirken.
- Zu große Seitenränder und ein zu großes Seitenformat machten den Satzspiegel deutlich luftiger als die Referenz.

Daraus folgt für die kanonische Ausgabe:

> **Garamond + kompaktes Buchformat + Blocksatz + deutsche Silbentrennung + 0 cm Erstzeileneinzug + 0 pt Absatzabstand + kompakter Zeilenrhythmus.**

## Kanonische Datei

`AUSNAHMEZUSTAND.docx` ist die **Sebastian-Fitzek-Benchmark-Fassung** und die einzige DOCX, die der Standard-Workflow als Artefakt ausliefert und ins Repository zurückschreibt.

Die früheren Profile `TESTLESER` und `EINREICHUNG` bleiben im Formatierungsskript als optionale manuelle Profile erhalten, werden aber nicht mehr standardmäßig gebaut oder ausgeliefert.

## Konkrete Satzparameter

### Seite und Satzspiegel

- Endformat: **12,0 × 18,7 cm**
- gespiegelte Seitenränder
- Innenrand: **1,35 cm**
- Außenrand: **1,15 cm**
- oberer Rand: **0,65 cm**
- unterer Rand: **0,65 cm**
- keine laufende Kopfzeile
- Seitenzahlen unten außen: gerade/linke Seite links, ungerade/rechte Seite rechts

Die Maße sind kein behauptetes Originalformat eines Fitzek-Titels. Sie sind die für `NORMALFALL` anhand der gelieferten Referenzseite kalibrierte Einstellung. Die Seitenproportion, die nutzbare Zeilenbreite und der Zeilenrhythmus treffen Textdichte und Zeilenlänge der Referenz deutlich näher als die frühere A4-/13,5-×-21,5-cm-Fassung.

### Fließtext

- Schrift: **Garamond** (Microsoft/Office-Schrift)
- Schriftgröße: **12,5 pt**
- Blocksatz
- Zeilenabstand: **1,12**
- 0 cm Erstzeileneinzug
- 0 pt Abstand vor und nach normalen Absätzen
- keine künstlichen Leerzeilen zwischen normalen Absätzen
- deutsche Silbentrennung
- Witwen-/Waisenkontrolle in dieser Buchfassung deaktiviert, damit kurze Thrillerabsätze den Satzspiegel nicht unnötig aufreißen

### Silbentrennung – verbindliche Regel

Die Trennung muss wie im gedruckten Buch aussehen: **ein Trennstrich darf nur sichtbar werden, wenn das Wort tatsächlich am Zeilenende umbrochen wird.**

Der verworfene Ansatz bestand darin, `U+00AD` direkt als Textzeichen an allen möglichen Silbengrenzen einzufügen. In bestimmten Word-/LibreOffice-Pfaden wurden diese Zeichen sichtbar materialisiert und erzeugten unakzeptable Formen wie `Ver-schluss`, `Pis-to-le` oder `sam-mel-te` mitten in einer Zeile.

Die endgültige Lösung verwendet deshalb echte Word-OOXML-Elemente `w:softHyphen` an gültigen deutschen Trennstellen. Diese Stellen sind im normalen Wort **unsichtbar** und werden nur dann als `-` dargestellt, wenn Word/LibreOffice genau dort einen Zeilenumbruch benötigt.

Für die Buchfassung gelten:

- Sprache der Runs: `de-DE`
- Word-Autohyphenation aktiviert
- gültige Trennstellen nach deutschem Wörterbuchmuster
- keine Trennung von Wörtern in Versalien
- Hyphenation-Zone ca. 0,4 cm
- maximal 2 aufeinanderfolgende Zeilen mit Trennung
- **0 literal `U+00AD`-Zeichen im erzeugten DOCX**
- optionale Trennstellen ausschließlich als echte `w:softHyphen`-Elemente

Damit bleibt der Blocksatz kompakt, ohne dass mitten in einer normalen Zeile künstliche Bindestriche sichtbar sind.

### Dialogtypografie

Für die Buchfassung werden die im Markdown-Master vorhandenen deutschen Anführungszeichen nur bei der Ausgabe typografisch umgestellt:

- Master bleibt: `„Dialog.“`
- Buchsatz wird: `»Dialog.«`

Der Mastertext wird dadurch nicht semantisch geändert. Die Umstellung ist rein typografisch und orientiert sich am sichtbaren Fitzek-Benchmark.

### Kapitelüberschriften

- echte Word-Formatvorlage `Heading 1` / `Überschrift 1`
- Garamond, **14,5 pt**, fett, schwarz, zentriert
- Format: `Kapitel N – Titel`; Prolog bleibt `Prolog`
- jedes Kapitel beginnt zwingend auf einer neuen Seite (`page_break_before`)
- 14 pt Abstand nach der Überschrift

## Szenenwechsel

`ROMAN_MAP.md` definiert weiterhin: **eine Szenenkarte entspricht zunächst einem Kapitel**. Der aktuelle Master enthält daher keine zusätzlichen internen Szenentrenner. Es werden keine Sternchen oder Leerraum-Trenner heuristisch erfunden.

Falls später innerhalb eines Kapitels ein echter semantischer Szenenwechsel entsteht, bleibt `---` im Markdown der explizite Marker und wird in Word als dezentes `*` dargestellt.

## Satzzeichen

- Gedankenstrich = Halbgeviertstrich `–`
- Geviertstrich `—` wird nicht verwendet
- der Build normalisiert verbliebene Geviertstriche deterministisch auf `–`
- Bindestrich `-`, Halbgeviertstrich `–` und Auslassungspunkte `…` bleiben funktional getrennt

## Vorsatz und Inhaltsverzeichnis

Die beiden `NORMALFALL`-Vorsatzseiten bleiben eigenständig und zentriert. Das Inhaltsverzeichnis wird weiterhin aus den echten Kapitelüberschriften erzeugt und materialisiert.

## Source of Truth

- Inhalt: `AUSNAHMEZUSTAND_FINAL.md`
- kanonische Word-Ausgabe: `AUSNAHMEZUSTAND.docx`
- Formatlogik: `scripts/polish_docx.py`
- Build: `.github/workflows/build-testreader-docx.yml`

Generierte DOCX-Dateien werden nicht manuell gepflegt. Änderungen an der Typografie werden zuerst hier dokumentiert und danach reproduzierbar im Build umgesetzt.

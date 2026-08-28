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

`AUSNAHMEZUSTAND.docx` ist ab jetzt die **Sebastian-Fitzek-Benchmark-Fassung** und die einzige DOCX, die der Standard-Workflow als Artefakt ausliefert und ins Repository zurückschreibt.

Die früheren Profile `TESTLESER` und `EINREICHUNG` bleiben im Formatierungsskript als optionale manuelle Profile erhalten, werden aber nicht mehr standardmäßig gebaut oder ausgeliefert. Damit entstehen für den normalen Build nicht mehr vier ähnlich benannte Word-Dateien.

## Konkrete Satzparameter

### Seite und Satzspiegel

- Endformat: **12,5 × 18,7 cm**
- gespiegelte Seitenränder
- Innenrand: **1,35 cm**
- Außenrand: **1,15 cm**
- oberer Rand: **0,65 cm**
- unterer Rand: **0,65 cm**
- keine laufende Kopfzeile
- Seitenzahlen unten außen: gerade/linke Seite links, ungerade/rechte Seite rechts

Die Maße sind kein behauptetes Originalformat eines Fitzek-Titels. Sie sind die für `NORMALFALL` kalibrierte Einstellung, die den gelieferten Referenz-Screenshot hinsichtlich Textdichte, Zeilenlänge und Satzspiegel deutlich näher trifft als die vorige 13,5-×-21,5-cm-Fassung.

### Fließtext

- Schrift: **Garamond** (Microsoft/Office-Schrift)
- Schriftgröße: **12,5 pt**
- Blocksatz
- Zeilenabstand: **1,05**
- 0 cm Erstzeileneinzug
- 0 pt Abstand vor und nach normalen Absätzen
- keine künstlichen Leerzeilen zwischen normalen Absätzen
- deutsche Silbentrennung
- zusätzlich deterministische optionale Trennstellen im erzeugten DOCX, damit Word/LibreOffice den engen Blocksatz reproduzierbar umbrechen
- Witwen-/Waisenkontrolle in dieser Buchfassung deaktiviert, damit kurze Thrillerabsätze den Satzspiegel nicht unnötig aufreißen

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

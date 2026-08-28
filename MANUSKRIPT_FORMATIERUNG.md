# Manuskript-Formatierung

Diese Datei ist der **verbindliche Formatierungsvertrag** für `AUSNAHMEZUSTAND_FINAL.md` → `AUSNAHMEZUSTAND.docx`.

Der aktuelle Stand wurde am 28.08.2026 visuell gegen eine reale Roman-Doppelseite von Sebastian Fitzek kalibriert und anschließend an mehreren Seiten des erzeugten Romans geprüft. Dieser Stand gilt als **freigegebener Buchsatz-Benchmark**.

> Zielbild: kompakter moderner Thriller-Buchsatz mit ruhigem Satzspiegel, klassischer Buch-Antiqua, Blocksatz, sauberer deutscher Silbentrennung und ohne sichtbare Word-/Manuskript-Anmutung.

---

## 1. Kanonische Ausgabe

`AUSNAHMEZUSTAND.docx` ist die **einzige kanonische Word-Ausgabe** des Romans und entspricht dem Sebastian-Fitzek-Benchmark.

Der Standard-Workflow erzeugt und committed nur diese Datei.

Die älteren Profile `testleser` und `einreichung` bleiben technisch als optionale manuelle Profile in `scripts/polish_docx.py` erhalten, sind aber **nicht** die maßgebliche Ausgabe und werden im Standard-Build nicht ausgeliefert.

---

## 2. Verbindliche Formatparameter

| Bereich | Verbindlicher Wert |
|---|---|
| Seitenformat | **12,0 × 18,7 cm** |
| Seitenränder | gespiegelt |
| Innenrand | **1,35 cm** |
| Außenrand | **1,15 cm** |
| Oberer Rand | **0,65 cm** |
| Unterer Rand | **0,65 cm** |
| Kopfzeile | keine |
| Seitenzahl | unten außen |
| Fließtext-Schrift | **Garamond** |
| Fließtext-Größe | **12,5 pt** |
| Ausrichtung | **Blocksatz** |
| Zeilenabstand | **1,12** |
| Erstzeileneinzug | **0 cm** |
| Absatzabstand davor | **0 pt** |
| Absatzabstand danach | **0 pt** |
| Leerzeilen zwischen normalen Absätzen | keine |
| Dokument-/Run-Sprache | **de-DE** |
| Witwen-/Waisenkontrolle im Fließtext | aus |
| Kapitelüberschrift | Garamond, **14,5 pt**, fett, schwarz, zentriert |
| Abstand nach Kapitelüberschrift | **14 pt** |
| Kapitelstart | immer neue Seite |
| Dialogzeichen in DOCX | **»…«** |
| Gedankenstrich | **Halbgeviertstrich `–`** |
| Geviertstrich `—` | nicht zulässig |

Diese Werte bilden zusammen das Layout. Einzelne Parameter sollen **nicht isoliert optimiert** werden, weil Satzspiegel, Schriftgröße, Zeilenlänge und Trennung voneinander abhängen.

---

## 3. Absatzlogik

Der Roman enthält viele kurze Thriller-Absätze und Dialogwechsel. Deshalb gelten bewusst folgende Regeln:

- **kein Erstzeileneinzug**
- **kein zusätzlicher Absatzabstand**
- **keine Leerzeile** zwischen normalen Absätzen
- alle normalen Absätze beginnen an derselben linken Satzkante
- Absätze werden allein durch den normalen Absatzwechsel getrennt

Damit werden zwei verworfene Varianten vermieden:

1. `0 cm Einzug + 4 pt Absatzabstand` → wirkte bei vielen kurzen Repliken zu listen-/protokollartig.
2. `Erstzeileneinzug + 0 pt Abstand` → erzeugte bei diesem Roman ein unruhiges Zickzack aus mehreren linken Ebenen.

Die freigegebene Kombination lautet daher:

> **0 cm Einzug + 0 pt Absatzabstand + Blocksatz.**

---

## 4. Silbentrennung – technisch verbindlich

Die Silbentrennung war der kritischste technische Punkt und darf nicht wieder vereinfacht werden.

### Ziel

Ein Trennstrich darf **nur sichtbar sein, wenn ein Wort tatsächlich am Zeilenende getrennt wird**.

Zulässig:

```text
Pisto-
le
```

Nicht zulässig:

```text
Pis-to-le
Ver-schluss
sam-mel-te
```

### Verbindliche Implementierung

Die Buchfassung verwendet zwei Ebenen:

1. Word-Autohyphenation mit Sprache `de-DE`.
2. Gültige deutsche Trennstellen werden zusätzlich als echte Word-OOXML-Elemente **`w:softHyphen`** hinterlegt.

Diese OOXML-Elemente sind im normalen Wort unsichtbar. Word/LibreOffice zeigt an einer solchen Stelle nur dann einen Bindestrich, wenn dort tatsächlich der Zeilenumbruch erfolgt.

### Nicht verwenden

**Nie wieder `U+00AD` direkt als Textzeichen in den Run-Text schreiben.**

Der frühere Pyphen-Ansatz mit literalem `U+00AD` führte je nach Word-/LibreOffice-Verarbeitung dazu, dass sämtliche möglichen Trennstellen sichtbar wurden. Genau daraus entstanden die fehlerhaften Schreibbilder `Ver-schluss`, `Pis-to-le`, `sam-mel-te` usw.

### Aktuelle Hyphenation-Parameter

- Wörterbuchmuster: `pyphen`, Sprache `de_DE`
- Word-Run-Sprache: `de-DE`
- `autoHyphenation = true`
- `doNotHyphenateCaps = true`
- `hyphenationZone = 230` Twips ≈ **0,4 cm**
- `consecutiveHyphenLimit = 2`
- keine Trennstellen in vollständig großgeschriebenen Wörtern
- **0 literale `U+00AD`-Zeichen** im finalen DOCX
- optionale Trennstellen ausschließlich als `w:softHyphen`

Implementierung: `rewrite_run_with_word_soft_hyphens()` in `scripts/polish_docx.py`.

---

## 5. Schrift und Buchwirkung

### Fließtext

- **Garamond 12,5 pt**
- Blocksatz
- 1,12 Zeilenabstand

Times New Roman ist für die kanonische Buchfassung ausdrücklich **verworfen**, da der Satz trotz korrekter Geometrie zu stark nach Word-/Manuskriptfassung wirkte.

Die Garamond-Schrift wird in den Word-Runs für `ascii`, `hAnsi`, `eastAsia` und `cs` gesetzt, damit Word die Schrift nicht teilweise substituiert.

---

## 6. Dialogtypografie

Der Markdown-Master bleibt sprachlich mit deutschen Anführungszeichen erhalten:

```text
„Dialog.“
```

Nur die kanonische Buchausgabe wird typografisch umgestellt auf:

```text
»Dialog.«
```

Diese Transformation findet ausschließlich beim DOCX-Build statt. Der Inhalt im Markdown wird dadurch nicht verändert.

---

## 7. Kapitelüberschriften

Kapitelüberschriften sind echte Word-`Heading 1`-Absätze.

Verbindlich:

- Garamond
- **14,5 pt**
- fett
- schwarz
- zentriert
- **14 pt Abstand danach**
- `page_break_before = true`
- jedes Kapitel startet damit zwingend auf einer neuen Seite

Format:

```text
Kapitel N – Titel
```

Der Prolog heißt ausschließlich:

```text
Prolog
```

Die Kapitelüberschriften bilden gleichzeitig die Quelle für das materialisierte Inhaltsverzeichnis.

---

## 8. Seitenarchitektur

Die kanonische Buchfassung verwendet:

- keine laufende Kopfzeile
- gespiegelte Ränder
- Seitenzahl unten außen
- gerade/linke Seite → Seitenzahl links
- ungerade/rechte Seite → Seitenzahl rechts
- Footer-Abstand ca. **0,35 cm**

Damit entspricht die Seitengestaltung dem visuellen Prinzip der Fitzek-Referenz und nicht einer klassischen Word-Manuskriptseite.

---

## 9. Szenenwechsel

`ROMAN_MAP.md` definiert derzeit:

> eine Szenenkarte = ein Kapitel

Daher werden **keine zusätzlichen Szenentrenner innerhalb der bestehenden Kapitel erfunden**.

Falls später tatsächlich mehrere Szenen in einem Kapitel vorkommen, gilt semantisch:

```markdown
---
```

Dieser Marker wird in der Word-Ausgabe als dezentes zentriertes `*` gesetzt.

---

## 10. Satzzeichen

Verbindlich:

- Gedankenstrich: `–` (Halbgeviertstrich)
- Geviertstrich: `—` **nicht verwenden**
- normaler Bindestrich: `-`
- Auslassung: `…`

Der Build normalisiert verbliebene Geviertstriche auf Halbgeviertstriche.

---

## 11. Vorsatz und Inhaltsverzeichnis

Die beiden `NORMALFALL`-Vorsatzseiten bleiben eigenständig und zentriert.

Das Inhaltsverzeichnis wird aus den echten `Heading 1`-Kapitelüberschriften erzeugt und im Build mit LibreOffice materialisiert.

Nach dem TOC-Update wird das Buchsatz-Profil erneut angewandt. Das ist absichtlich so, weil LibreOffice bei der Materialisierung Word-interne Formatdetails verändern kann.

---

## 12. Verbindlicher Build-Ablauf

Der Standard-Build muss in dieser Reihenfolge laufen:

1. `AUSNAHMEZUSTAND_FINAL.md` strukturell validieren.
2. Semantische Szenenbrüche prüfen.
3. Basis-DOCX mit `scripts/build_testreader_docx.py` erzeugen.
4. `scripts/polish_docx.py --profile buchvorschau` anwenden.
5. Inhaltsverzeichnis mit `scripts/update_docx_toc.py` materialisieren.
6. `scripts/polish_docx.py --profile buchvorschau` **erneut** anwenden.
7. DOCX technisch validieren.
8. Artefakt hochladen.
9. `AUSNAHMEZUSTAND.docx` ins Repo committen.

Der zweite Polish-Pass ist Teil des Formatierungsvertrags und darf nicht entfernt werden.

---

## 13. Regression-Checks

Der Workflow muss mindestens prüfen:

- Seitenformat **12,0 × 18,7 cm**
- Ränder 1,35 / 1,15 / 0,65 / 0,65 cm
- Fließtext Blocksatz
- Fließtext **Garamond 12,5 pt**
- Zeilenabstand **1,12**
- Erstzeileneinzug **0 cm**
- Absatzabstand **0 pt**
- 48 `Heading 1`-Einheiten: Prolog + Kapitel 1–47
- Kapitel beginnen auf neuer Seite
- keine `„…“` mehr im Buchtext; stattdessen `»…«`
- kein Geviertstrich `—`
- keine literalen `U+00AD`-Zeichen
- ausreichend `w:softHyphen`-Elemente für die deutsche Trennung
- Auto-Hyphenation aktiviert
- Versalien nicht trennen
- maximal zwei aufeinanderfolgende Trennzeilen
- gespiegelte Ränder
- Seitenzahlen außen
- Kopfzeile leer

Der technische Check ersetzt **nicht** die visuelle Prüfung. Nach Änderungen an Satzspiegel, Schrift, Trennung oder Seitenarchitektur muss mindestens eine frühe Prologseite sowie eine dialogreiche Seite gerendert und angesehen werden.

---

## 14. Was ausdrücklich nicht wieder eingeführt werden soll

Ohne neue bewusste Layoutentscheidung nicht verändern:

- kein A4 als kanonische Buchfassung
- kein Times New Roman in der Buchfassung
- kein linksbündiger Fließtext
- kein Erstzeileneinzug
- kein 3-/4-pt-Absatzabstand
- keine Leerzeilen zwischen normalen Absätzen
- keine literal eingebauten `U+00AD`-Soft-Hyphens
- keine sichtbaren Bindestriche mitten im Wort
- kein Geviertstrich `—`
- keine laufende Kopfzeile
- keine vier parallelen Standard-DOCX-Dateien

---

## 15. Source of Truth

- **Inhalt:** `AUSNAHMEZUSTAND_FINAL.md`
- **Formatierungsvertrag:** `MANUSKRIPT_FORMATIERUNG.md`
- **Formatierungsimplementierung:** `scripts/polish_docx.py`
- **DOCX-Basisgenerator:** `scripts/build_testreader_docx.py`
- **TOC-Materialisierung:** `scripts/update_docx_toc.py`
- **Build/Regression:** `.github/workflows/build-testreader-docx.yml`
- **kanonische Ausgabe:** `AUSNAHMEZUSTAND.docx`

Generierte DOCX-Dateien werden **nicht manuell** gepflegt. Änderungen an der Typografie werden zuerst in diesem Dokument als neue bewusste Entscheidung festgehalten und anschließend reproduzierbar im Build umgesetzt und visuell geprüft.

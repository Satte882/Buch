# Manuskript-Formatierung

Diese Datei ist der **verbindliche Formatierungsvertrag** für `AUSNAHMEZUSTAND_FINAL.md` → `AUSNAHMEZUSTAND.docx`.

Der Buchsatz wurde am 28.08.2026 visuell gegen eine reale Roman-Doppelseite von Sebastian Fitzek kalibriert. Am 29.08.2026 wurde dieser freigegebene Satz auf das von Amazon KDP unterstützte Taschenbuchformat **5,06 × 7,81 Zoll (12,85 × 19,84 cm)** übertragen.

> Zielbild: kompakter moderner Thriller-Buchsatz mit ruhigem Satzspiegel, klassischer Buch-Antiqua, Blocksatz, sauberer deutscher Silbentrennung und ohne sichtbare Word-/Manuskript-Anmutung – technisch passend für KDP.

---

## 1. Kanonische Ausgabe

`AUSNAHMEZUSTAND.docx` ist die **einzige kanonische Word-Ausgabe** des Romans.

Die Typografie bleibt am freigegebenen Fitzek-Benchmark orientiert. Das physische Seitenformat ist jedoch kein freies Sonderformat mehr, sondern das KDP-Trim-Format **5,06 × 7,81 Zoll**.

Der Standard-Workflow erzeugt und committed nur diese Datei.

Die älteren Profile `testleser` und `einreichung` bleiben technisch als optionale manuelle Profile in `scripts/polish_docx.py` erhalten, sind aber **nicht** die maßgebliche Ausgabe und werden im Standard-Build nicht ausgeliefert.

---

## 2. Verbindliche Formatparameter

| Bereich | Verbindlicher Wert |
|---|---|
| KDP-Format | **5,06 × 7,81 Zoll** |
| Seitenformat DOCX | **12,85 × 19,84 cm** |
| Beschnittzugabe | **keine** |
| Seitenränder | gespiegelt |
| Innenrand | **1,95 cm** |
| Außenrand | **1,40 cm** |
| Oberer Rand | **1,22 cm** |
| Unterer Rand | **1,22 cm** |
| Nutzbarer Textbereich | **9,50 × 17,40 cm** |
| Kopfzeile | keine |
| Seitenzahl | unten außen |
| Footer-Abstand vom Seitenrand | **0,75 cm** |
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

### Warum die Ränder mit dem Format geändert wurden

Das frühere Sonderformat hatte **12,0 × 18,7 cm** mit Rändern 1,35 / 1,15 / 0,65 / 0,65 cm. Daraus ergab sich ein nutzbarer Textbereich von exakt:

- Breite: `12,0 - 1,35 - 1,15 = 9,50 cm`
- Höhe: `18,7 - 0,65 - 0,65 = 17,40 cm`

Beim Wechsel auf das größere KDP-Format wird **nicht einfach mehr Text auf die Seite gepackt**. Stattdessen bleibt dieser freigegebene Textbereich mit **9,50 × 17,40 cm** erhalten. Die zusätzliche Fläche wird den Seitenrändern zugeschlagen.

Damit bleiben insbesondere Zeilenlänge, Textdichte, Umbruchcharakter und der visuell abgenommene Thriller-Satz weitgehend stabil.

Der erste CI-Render der KDP-Fassung ergab **591 Seiten**. Amazon KDP verlangt für **501 bis 700 Seiten** mindestens **19,1 mm Innenrand/Bundsteg**. Deshalb ist der kanonische Innenrand auf **1,95 cm** gesetzt. Die zusätzlichen 0,17 cm gegenüber der ersten KDP-Adaption werden vom Außenrand abgezogen; dadurch bleibt die Textbreite unverändert bei 9,50 cm. Der Build muss sicherstellen, dass die gerenderte Ausgabe **nicht mehr als 700 Seiten** umfasst. Oberhalb dieser Grenze muss der Bundsteg erneut bewusst angepasst werden.

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

- KDP-Taschenbuchformat **5,06 × 7,81 Zoll**
- **keine Beschnittzugabe** für den reinen Textsatz
- keine laufende Kopfzeile
- gespiegelte Ränder
- Innenrand/Bundsteg **1,95 cm**
- Außenrand **1,40 cm**
- Seitenzahl unten außen
- gerade/linke Seite → Seitenzahl links
- ungerade/rechte Seite → Seitenzahl rechts
- Footer-Abstand **0,75 cm** vom unteren Seitenrand

Der frühere Footer-Abstand von 0,35 cm wird nicht weiterverwendet, weil Seitenzahlen ebenfalls druckrelevanter Inhalt sind und im KDP-Produktionssatz ausreichend Abstand zur Schnittkante benötigen.

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

Nach dem TOC-Update wird das KDP-Buchsatz-Profil erneut angewandt. Das ist absichtlich so, weil LibreOffice bei der Materialisierung Word-interne Formatdetails verändern kann.

---

## 12. Verbindlicher Build-Ablauf

Der Standard-Build muss in dieser Reihenfolge laufen:

1. `AUSNAHMEZUSTAND_FINAL.md` strukturell validieren.
2. Semantische Szenenbrüche prüfen.
3. Basis-DOCX mit `scripts/build_book_docx.py` erzeugen.
4. `scripts/kdp_book_layout.py AUSNAHMEZUSTAND.docx` anwenden.
5. Inhaltsverzeichnis mit `scripts/update_docx_toc.py` materialisieren.
6. `scripts/kdp_book_layout.py AUSNAHMEZUSTAND.docx` **erneut** anwenden.
7. DOCX technisch validieren.
8. DOCX mit LibreOffice zu PDF rendern und Seitenzahl als CI-Sicherheitscheck bestimmen.
9. Sicherstellen, dass die Ausgabe höchstens **700 Seiten** hat.
10. Artefakt hochladen.
11. `AUSNAHMEZUSTAND.docx` ins Repo committen.

Der zweite KDP-Layout-Pass ist Teil des Formatierungsvertrags und darf nicht entfernt werden. Die LibreOffice-Seitenzahl ist ein reproduzierbarer CI-Guard; die finale Druckfreigabe erfolgt zusätzlich im KDP-Previewer.

---

## 13. Regression-Checks

Der Workflow muss mindestens prüfen:

- Seitenformat **12,85 × 19,84 cm**
- gespiegelt: Innen/Außen **1,95 / 1,40 cm**
- oben/unten **1,22 / 1,22 cm**
- Textbereich rechnerisch **9,50 × 17,40 cm**
- Footer-Abstand **0,75 cm**
- Ausgabe **≤ 700 Seiten**
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

- kein freies Sonderformat **12,0 × 18,7 cm** als kanonische KDP-Ausgabe
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
- keine Seitenzahl näher als 0,75 cm an der unteren Schnittkante
- kein Innenrand unter **1,95 cm**, solange die gerenderte Ausgabe in der KDP-Klasse 501–700 Seiten liegt
- keine vier parallelen Standard-DOCX-Dateien

---

## 15. Source of Truth

- **Inhalt:** `AUSNAHMEZUSTAND_FINAL.md`
- **Formatierungsvertrag:** `MANUSKRIPT_FORMATIERUNG.md`
- **allgemeine Typografie-/Hyphenation-Engine:** `scripts/polish_docx.py`
- **kanonische KDP-Geometrie:** `scripts/kdp_book_layout.py`
- **DOCX-Basisgenerator:** `scripts/build_book_docx.py`
- **TOC-Materialisierung:** `scripts/update_docx_toc.py`
- **Build/Regression:** `.github/workflows/build-book-docx.yml`
- **kanonische Ausgabe:** `AUSNAHMEZUSTAND.docx`

Generierte DOCX-Dateien werden **nicht manuell** gepflegt. Änderungen an der Typografie oder KDP-Geometrie werden zuerst in diesem Dokument als neue bewusste Entscheidung festgehalten und anschließend reproduzierbar im Build umgesetzt und visuell geprüft.

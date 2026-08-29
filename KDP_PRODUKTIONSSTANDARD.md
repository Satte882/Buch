# KDP-Produktionsstandard für zukünftige Bücher

Diese Datei dokumentiert die bei `NORMALFALL` erarbeiteten Regeln für **Buchsatz, KDP-Innenformat und Cover-Produktion**. Sie ist bewusst so geschrieben, dass sie bei einem zweiten Buch als Startpunkt wiederverwendet werden kann.

> Grundregel: **Innenlayout und Cover nie unabhängig voneinander finalisieren.** Das Innenformat bestimmt zusammen mit Papierart und finaler Seitenzahl den Buchrücken und damit die exakte Gesamtgröße des Covers.

---

## 1. Standard für den Buchinnenraum

Für `NORMALFALL` wurde als kanonisches KDP-Innenformat festgelegt:

**KDP-Auswahl:** `5,06 × 7,81 Zoll (12,85 × 19,84 cm)`  
**Beschnittzugabe Innenraum:** **ohne Beschnittzugabe**

| Parameter | Wert |
|---|---:|
| Seitenformat | **12,85 × 19,84 cm** |
| Innenrand / Bundsteg | **1,95 cm** |
| Außenrand | **1,40 cm** |
| Oben / unten | **1,22 cm** |
| Nutzbarer Textbereich | **9,50 × 17,40 cm** |
| Footer / Seitenzahl | **0,75 cm** |

### Warum diese Geometrie

Das frühere Sonderformat von `NORMALFALL` war 12,0 × 18,7 cm. Beim Wechsel auf ein KDP-Standardformat wurde **nicht einfach mehr Text auf die größere Seite gepackt**. Der freigegebene Satzspiegel wurde weitgehend erhalten.

Der nutzbare Textbereich bleibt deshalb bei:

- **9,50 cm Breite**
- **17,40 cm Höhe**

Damit bleiben Zeilenlänge, Textdichte und Umbruchcharakter nahe am ursprünglich abgenommenen Thriller-Buchsatz.

Der Innenrand von 1,95 cm wurde gewählt, weil der CI-Render von `NORMALFALL` bei ungefähr 591 Seiten lag und damit in die KDP-Klasse **501–700 Seiten** fällt.

### Wiederverwendung bei einem neuen Buch

Diese Werte sind ein **bewährtes Ausgangsprofil**, aber kein unveränderliches Naturgesetz. Bei einem neuen Buch muss insbesondere der Bundsteg anhand der tatsächlichen finalen Seitenzahl erneut geprüft werden.

---

## 2. Innenraum-Workflow

Für ein neues Buch gilt:

1. Manuskript finalisieren.
2. KDP-Innenformat festlegen.
3. Buchsatz auf exakt dieses Format erzeugen.
4. DOCX/PDF technisch prüfen.
5. In KDP hochladen.
6. **Tatsächliche finale Seitenzahl** aus KDP bzw. dem finalen Previewer übernehmen.
7. Erst danach das Cover final erzeugen.

Wichtig: Eine lokal oder in CI gerenderte Seitenzahl ist ein guter Guard, aber der finale KDP-Render ist für den Buchrücken maßgeblich.

---

## 3. Cover: KDP erwartet eine komplette PDF

Das druckfertige Cover wird bei KDP als **eine einzige PDF-Seite** hochgeladen.

Die PDF enthält in einem zusammenhängenden Spread:

`Rückseite | Buchrücken | Vorderseite`

### Nicht verwenden

- kein PNG als finale KDP-Coverdatei
- keine getrennten Dateien für Vorderseite, Rücken und Rückseite
- keine frei geschätzte Dokumentgröße
- keine nicht eingebetteten Schriftarten

### Muss erfüllt sein

- exakt die von KDP für das konkrete Buch berechnete Gesamtgröße
- eine PDF-Seite
- alle Fonts vollständig eingebettet
- ausreichender Beschnitt außen
- Text und wichtige Elemente innerhalb der Safe Areas
- Barcode-Bereich auf der Rückseite freihalten
- zusätzlich Raum für mögliche Amazon-Transparency-Codes lassen

---

## 4. Die Covergröße darf niemals aus einem alten Buch übernommen werden

Die Gesamtgröße des Covers hängt ab von:

- Bindungsart
- Papierart
- Leserichtung
- Trim Size / Innenformat
- finaler Seitenzahl
- daraus resultierender Buchrückenbreite
- Beschnittzugabe

Deshalb gilt für jedes neue Buch:

> **Immer zuerst den KDP Cover Calculator / die KDP-Vorlage mit den finalen Buchdaten erzeugen und danach die Cover-PDF exakt auf diese Maße bauen.**

Die Breite setzt sich prinzipiell zusammen aus:

`Rückseite + Buchrücken + Vorderseite + äußerer Beschnitt`

Die Höhe setzt sich zusammen aus:

`Trim-Höhe + Beschnitt oben + Beschnitt unten`

---

## 5. Wichtige Erkenntnis aus NORMALFALL

Beim ersten Cover-Upload meldete KDP:

- **erwartete Covergröße:** `13.356 × 9.250 Zoll`
- **eingereichte Dateigröße:** `11.693 × 8.268 Zoll`

Die Höhe von **9,250 Zoll** entspricht einem 9-Zoll-Buch plus jeweils 0,125 Zoll Beschnitt oben und unten. Das weist auf ein **6 × 9 Zoll**-Projektformat hin.

Das steht im Widerspruch zur zuvor für den Innenraum festgelegten Auswahl:

`5,06 × 7,81 Zoll`

### Konsequenz

Für `NORMALFALL` und erst recht für ein zukünftiges Buch darf man daraus **nicht** ableiten, dass `13.356 × 9.250 Zoll` eine allgemein gültige Covergröße sei.

Stattdessen muss vor dem finalen Upload geprüft werden:

1. Welches Innenformat ist im konkreten KDP-Projekt tatsächlich ausgewählt?
2. Welche finale Seitenzahl verwendet KDP?
3. Welche Covergröße berechnet der KDP Cover Calculator daraus?

**Die KDP-Vorlage ist die Source of Truth für die Coverabmessungen.**

---

## 6. Schriftarten im Cover-PDF

KDP meldete beim ersten Versuch außerdem:

> Die Schriftarten wurden nicht ordnungsgemäß eingebettet.

Das darf bei der finalen Produktionsdatei nicht passieren.

### Verbindliche Regel

Alle verwendeten Schriftarten müssen **vollständig in die PDF eingebettet** sein.

Technischer Check, sofern `poppler-utils` verfügbar ist:

```bash
pdffonts COVER.pdf
```

Bei den verwendeten Fonts muss die Spalte `emb` auf `yes` stehen.

Zusätzlicher Größencheck:

```bash
pdfinfo COVER.pdf
```

Damit lassen sich Seitenanzahl und PDF-Seitengröße vor dem Upload kontrollieren.

---

## 7. Cover-Designentscheidung für NORMALFALL

Die visuelle Grundidee für `NORMALFALL` ist bewusst extrem reduziert.

### Vorderseite

Nur:

**NORMALFALL**

und der Satz:

*Eine Regel widersteht allem,*  
*außer dem Beweis,*  
*dass es ohne sie besser geht.*

### Bewusst nicht auf der Vorderseite

- kein Autorenname
- kein weiterer Klappentext
- keine zusätzlichen grafischen Motive
- aktuell auch kein Genrelabel wie `Psychothriller`

Das Genre kann über Amazon-Metadaten, Beschreibung und Kategorien transportiert werden. Falls später bewusst entschieden wird, `Psychothriller` auf das Cover zu setzen, ist das eine neue Designentscheidung und keine technische Notwendigkeit.

### Buchrücken

Nur:

`NORMALFALL`

### Rückseite

Im minimalistischen Konzept möglichst frei halten. Insbesondere den von KDP vorgesehenen Barcode-Bereich nicht mit Text oder wichtigen Designelementen überlagern.

### Look & Feel

- Weiß bzw. gebrochenes Weiß
- schwarze oder sehr dunkle Typografie
- großzügiger Weißraum
- hochwertig, kühl und kontrolliert
- keine klassischen Thriller-Klischees wie Augen, Blut, Waffen, Personen-Silhouetten oder dunkle Stadtbilder

---

## 8. Produktions-Checkliste für jedes neue Buch

### Innenraum

- [ ] Trim Size in KDP festgelegt
- [ ] Dokumentformat exakt identisch
- [ ] Bundsteg passend zur finalen Seitenzahl
- [ ] Seitenzahlen im sicheren Bereich
- [ ] Schriftarten und Typografie geprüft
- [ ] finale Seitenzahl aus KDP bekannt

### Cover

- [ ] KDP Cover Calculator mit finalen Daten ausgeführt
- [ ] exakte Gesamtbreite/-höhe aus der KDP-Vorlage übernommen
- [ ] Rückseite + Rücken + Vorderseite in **einer** PDF
- [ ] äußerer Beschnitt berücksichtigt
- [ ] Safe Areas eingehalten
- [ ] Barcode-Bereich frei
- [ ] Fonts vollständig eingebettet
- [ ] PDF-Seitengröße technisch geprüft
- [ ] KDP Previewer ohne Coverfehler

### Erst danach

- [ ] finale Freigabe
- [ ] Veröffentlichung

---

## 9. Source of Truth im Repo

Für `NORMALFALL` gelten derzeit:

- **Inhalt:** `AUSNAHMEZUSTAND_FINAL.md`
- **Buchsatz- und Innenlayoutvertrag:** `MANUSKRIPT_FORMATIERUNG.md`
- **KDP-Layout-Implementierung:** `scripts/kdp_book_layout.py`
- **Build/Regression:** `.github/workflows/build-book-docx.yml`
- **KDP-Produktionswissen / Wiederverwendung:** `KDP_PRODUKTIONSSTANDARD.md`

Für ein zweites Buch sollte diese Datei kopiert bzw. als Vorlage verwendet werden. Buchspezifische Werte wie Titel, Seitenzahl, Bundsteg und **Covergesamtgröße** müssen jedoch neu berechnet werden.

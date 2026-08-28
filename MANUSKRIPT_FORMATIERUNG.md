# Manuskript-Formatierung

Diese Datei definiert die verbindliche Format- und Ausgabe-Logik für `AUSNAHMEZUSTAND_FINAL.md` und die daraus erzeugten Word-Dateien.

## Grundentscheidung

Der Roman hat **einen inhaltlichen Mastertext**, aber nicht mehr nur eine universelle Word-Formatierung. Testlesen, Einreichung bei Verlag/Lektorat und Buchsatz haben unterschiedliche Ziele und brauchen deshalb getrennte Ausgabeprofile.

Der Mastertext wird nicht für ein bestimmtes Layout umgeschrieben. Layout, Seitenformat, Absatzlogik, Kopf-/Fußzeilen und Silbentrennung entstehen reproduzierbar im Build.

`AUSNAHMEZUSTAND.docx` bleibt aus Kompatibilitätsgründen die kanonische **TESTLESER**-Fassung.

## Ausgabeprofile

### 1. TESTLESER

Zweck: ruhige Lesefassung für Autor und Testleser. Sie soll schnell lesbar sein und den stark rhythmischen Thrillertext nicht durch klassischen Buchsatz überformen.

- A4
- Times New Roman, 11,5 pt
- linksbündig, kein Blocksatz
- Zeilenabstand 1,15
- kein Erstzeileneinzug
- alle normalen Absätze beginnen an derselben linken Kante
- 0 pt Abstand vor, 4 pt Abstand nach jedem normalen Absatz
- keine echten Leerzeilen zwischen normalen Absätzen
- Witwen-/Waisenkontrolle aktiv
- keine laufende Kopfzeile
- Seitenzahl in der Fußzeile

Diese Fassung ist bewusst **keine Normseite und kein Buchsatz**.

### 2. EINREICHUNG

Zweck: robuste Manuskriptfassung für Verlag, Agentur, Lektorat oder professionelle Textarbeit. Empfängerspezifische Vorgaben haben immer Vorrang.

- A4
- Times New Roman, 12 pt
- linksbündig
- Zeilenabstand 1,5
- Erstzeileneinzug 0,75 cm
- 0 pt Absatzabstand vor/nach
- erster Absatz nach Kapitelüberschrift oder Szenenbruch ohne Einzug
- dezente Kopfzeile mit `NORMALFALL`
- Seitenzahl in der Fußzeile

Das Profil orientiert sich an einer klassischen Einreichungsfassung, behauptet aber nicht, für jeden Verlag eine verbindliche deutsche „Normseite“ zu sein.

### 3. BUCHVORSCHAU

Zweck: prüfen, wie der Text in einem echten Buchsatz-Prinzip wirkt. Dieses Profil ist **keine druckfertige Produktionsdatei**, solange Veröffentlichungsweg, Endformat, Papier, Beschnitt und Bindung nicht feststehen.

Vorläufige Vorschau:

- kompaktes Buchformat 13,5 × 21,5 cm
- Times New Roman, ca. 10,5 pt als neutral verfügbare Vorschau-Schrift
- Blocksatz
- automatische deutsche Silbentrennung aktiviert
- Erstzeileneinzug 0,45 cm
- 0 pt Absatzabstand
- erster Absatz nach Kapitelüberschrift oder Szenenbruch ohne Einzug
- gespiegelte Seitenränder
- dezenter Szenentrenner, falls ein Kapitel künftig mehrere Szenen enthält
- Seitenzahl in der Fußzeile

Vor einer Veröffentlichung wird dieses Profil auf die technischen Vorgaben von Verlag/KDP/BoD/etc. angepasst.

## Kapitelüberschriften

Für alle Profile:

- echte Word-Formatvorlage `Heading 1` / `Überschrift 1`
- schwarz, fett
- jedes Kapitel beginnt auf einer neuen Seite
- Format: `Kapitel N – Titel`
- der Prolog bleibt schlicht `Prolog`
- Überschriften sind Grundlage für Navigation und Inhaltsverzeichnis

Größe, Abstand und konkrete Ausrichtung dürfen je Ausgabeprofil variieren.

## Szenenwechsel

Ein Szenenbruch ist **semantisch**, nicht nur typografisch. Er wird nur gesetzt, wenn innerhalb eines Kapitels ein echter Sprung vorliegt, zum Beispiel:

- deutlicher Ortswechsel
- relevanter Zeitsprung
- Perspektiv-/POV-Wechsel
- Wechsel auf eine andere Handlungsebene, bei dem ein normaler Absatzwechsel den Leser über den Sprung täuschen würde

Kein Szenenbruch nur wegen eines neuen Gedankens, Sprecherwechsels oder kurzen Absatzes.

### Aktueller Befund

`ROMAN_MAP.md` definiert ausdrücklich: **Eine Szenenkarte entspricht zunächst einem Kapitel.** Daraus entstehen Prolog + 47 Kapitel und damit aktuell 48 getrennte Story-/Szeneneinheiten.

Der technische Audit des aktuellen Masters bestätigt dazu passend: **0 explizite Szenenbrüche innerhalb laufender Kapitel.** Das ist deshalb im jetzigen Stand kein Formatierungsfehler, sondern entspricht der gesetzten Romanarchitektur. Die pauschale Annahme, innerhalb der bestehenden Kapitel müssten zusätzliche Szenentrenner eingefügt werden, wird nicht übernommen.

Szenentrenner werden erst relevant, wenn später zwei Szenenkarten bewusst zu einem Kapitel zusammengelegt werden oder ein tatsächlich bestätigter interner Orts-/Zeit-/POV-Sprung entsteht.

Technische Regel für diesen Fall:

- `---` innerhalb eines laufenden Kapitels gilt als expliziter Szenenbruch, sofern danach **nicht** unmittelbar die nächste Kapitelüberschrift folgt.
- `---` direkt vor einer neuen Kapitelüberschrift ist nur ein Kapiteltrenner und erzeugt keinen zusätzlichen Stern.
- sichtbarer Szenentrenner in Word: ein dezentes, zentriertes `*`
- der erste Fließtextabsatz nach einem Szenenbruch gilt typografisch wie der erste Absatz nach einer Kapitelüberschrift

Damit bleibt die Szenenstruktur unabhängig vom jeweiligen Word-Profil erhalten, ohne künstliche Brüche zu erfinden.

## Satzzeichen und Gedankenstriche

Für den deutschsprachigen Romantext gilt:

- Gedankenstrich = Halbgeviertstrich `–`
- der Geviertstrich `—` wird im Romantext nicht verwendet
- auch bei abrupt abgebrochener Rede wird kein Geviertstrich verwendet; falls ein Gedankenstrich nötig ist, wird `–` verwendet
- Bindestrich `-`, Halbgeviertstrich `–` und Auslassungspunkte `…` werden funktional getrennt eingesetzt
- der Build normalisiert eventuell verbliebene Geviertstriche deterministisch auf `–`

Ziel ist ein unauffälliges, natürliches deutschsprachiges Schriftbild und keine typografische Eigenheit, die unnötig nach LLM-/KI-Prosa aussieht.

## Vorsatzseiten

Die beiden Vorsatzseiten sind Teil der Buchidentität und werden nicht von den Fließtextregeln überschrieben:

1. `NORMALFALL` mit dem Eingangszitat
2. Definition `Normalfall, der:` mit wiederholtem Zitat

Diese Elemente bleiben zentriert.

## Inhaltsverzeichnis

Das Inhaltsverzeichnis wird aus den echten Word-Überschriften erzeugt und im Build materialisiert. Es enthält `Prolog` sowie Kapitel 1–47 mit ihren Kapiteltiteln und Seitenzahlen.

## Source of Truth

- Inhaltlicher Master: `AUSNAHMEZUSTAND_FINAL.md`
- kanonische Lesefassung: `AUSNAHMEZUSTAND.docx` = Profil `TESTLESER`
- weitere Word-Fassungen werden aus demselben Master erzeugt und sollen nicht manuell gepflegt werden
- keine dauerhaften manuellen Formatkorrekturen direkt in generierten DOCX-Dateien

## Technische Umsetzung

- `scripts/build_testreader_docx.py` liest den Master, normalisiert den Vorspann und Satzzeichen und übernimmt explizite Szenenmarker.
- `scripts/polish_docx.py` setzt Kapiteltitel und das gewählte Ausgabeprofil.
- `scripts/audit_scene_breaks.py` prüft die im Master vorhandenen Szenenmarker und meldet ihre Verteilung.
- `scripts/update_docx_toc.py` aktualisiert/materialisiert das Inhaltsverzeichnis.
- `.github/workflows/build-testreader-docx.yml` erzeugt die Profile reproduzierbar, validiert sie und committed nur die kanonische Testleserfassung sowie notwendige deterministische Master-Normalisierungen.
- Für die CI-Qualitätsprüfung der Buchvorschau muss ein deutsches Silbentrennungsmuster (`hyphen-de`) installiert sein; nur das Word-Flag `autoHyphenation` reicht in einem nackten LibreOffice-Runner nicht für eine belastbare visuelle Prüfung.

## Änderungsregel

Formatentscheidungen werden zuerst hier dokumentiert und danach im Build umgesetzt. Inhaltliche Änderungen am Roman werden davon getrennt behandelt. Insbesondere werden keine neuen Szenenbrüche automatisch aus Namenswechseln, Leerzeilen oder heuristischen Vermutungen erfunden.
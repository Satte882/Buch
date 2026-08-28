# Manuskript-Formatierung

Diese Datei definiert die verbindliche Word-Formatierung fuer `AUSNAHMEZUSTAND.docx`.

Ziel ist eine ruhige, gut lesbare Testleser-/Manuskriptfassung. Die Formatierung wird nicht manuell in Word gepflegt, sondern reproduzierbar durch die Build-Skripte erzeugt.

## Grundprinzip

Der Roman verwendet viele kurze Absaetze, Einzelsaetze und Dialogwechsel. Ein klassischer Erstzeileneinzug erzeugt dabei optisch zwei linke Ebenen und einen unruhigen Zickzack-Rand. Blocksatz erzeugt zusaetzlich bei kurzen Thriller-Absaetzen zu grosse Wortabstaende.

Deshalb gilt fuer den gesamten Romantext ab `Prolog`:

- linksbuendig, kein Blocksatz
- kein Erstzeileneinzug
- jeder Absatz beginnt an derselben linken Kante
- keine echten Leerzeilen zwischen normalen Absaetzen
- stattdessen 4 pt Abstand nach jedem Absatz
- Times New Roman, 11,5 pt
- Zeilenabstand 1,15
- Absatzabstand vor: 0 pt
- Absatzabstand nach: 4 pt
- Witwen-/Waisenkontrolle aktiv

Damit wird die Absatzstruktur vertikal sichtbar, ohne den Text mit ganzen Leerzeilen auseinanderzuziehen.

## Kapitelueberschriften

- echte Word-Formatvorlage `Heading 1` / `Ueberschrift 1`
- schwarz, fett, zentriert
- Times New Roman, 15 pt
- 20 pt Abstand nach der Ueberschrift
- jedes Kapitel beginnt auf einer neuen Seite
- Format: `Kapitel N - Titel`
- der Prolog bleibt schlicht `Prolog`

Die Kapitelueberschriften werden fuer Navigation und Inhaltsverzeichnis verwendet.

## Vorsatzseiten

Die beiden Vorsatzseiten werden separat formatiert und duerfen von der Fliesstext-Regel nicht veraendert werden:

1. `NORMALFALL` mit dem Eingangszitat
2. Definition `Normalfall, der:` mit wiederholtem Zitat

Diese Elemente bleiben zentriert und ohne Fliesstext-Absatzformatierung.

## Inhaltsverzeichnis

Das Inhaltsverzeichnis wird aus den Word-Ueberschriften erzeugt und im Build materialisiert. Es enthaelt `Prolog` sowie Kapitel 1-47 mit ihren Kapiteltiteln und Seitenzahlen.

## Technische Umsetzung

- `scripts/build_testreader_docx.py` erzeugt die Word-Datei aus `AUSNAHMEZUSTAND_FINAL.md`.
- `scripts/polish_docx.py` setzt Kapiteltitel und die verbindliche Fliesstext-Formatierung.
- `scripts/update_docx_toc.py` aktualisiert/materialisiert das Inhaltsverzeichnis.
- `.github/workflows/build-testreader-docx.yml` fuehrt diese Schritte reproduzierbar aus und committed die erzeugte `AUSNAHMEZUSTAND.docx`.

Aenderungen an der Satzlogik sollen zuerst in dieser Datei entschieden und anschliessend im Build-Skript umgesetzt werden. Keine dauerhaften manuellen Formatkorrekturen direkt in der erzeugten DOCX.

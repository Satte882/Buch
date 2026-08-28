# Archivhinweis

Dieser Ordner dokumentiert Dateien, die bewusst **nicht mehr im aktiven Arbeitsbaum** geführt werden.

Die tatsächlichen historischen Dateiinhalte bleiben vollständig in der Git-Historie des Repositories erhalten. Sie werden hier nicht dupliziert, damit veraltete Fassungen nicht versehentlich wieder als Arbeitsgrundlage verwendet werden.

## Ausgemusterte Volltextfassungen

Die früheren fünf Teilmanuskripte unter `MANUSKRIPT/` waren während Ausbau und Review nützlich, sind nach Konsolidierung aber veraltete Parallelfassungen:

- `MANUSKRIPT/01_BAUSTEINE_01_02.md`
- `MANUSKRIPT/02_BAUSTEINE_03_04.md`
- `MANUSKRIPT/03_BAUSTEINE_05_06.md`
- `MANUSKRIPT/04_BAUSTEIN_07.md`
- `MANUSKRIPT/05_BAUSTEINE_08_09.md`

**Aktuelle Source of Truth:** `AUSNAHMEZUSTAND_FINAL.md`.

## Ausgemusterte Ausbau-Steuerung

- `AUSBAU_MATRIX.md` – historischer Umsetzungsplan aus der Ausbauphase; Baseline und Wortziele sind nach Abschluss des Ausbaus überholt.
- `UMFANG_UND_AUSBAUSTEUERUNG.md` – historische Umfangssteuerung; enthielt trotz späterer Relativierung noch widersprüchliche Definition-of-Done-Formulierungen zu 75.000–80.000 Wörtern.

Aktuell gilt stattdessen: **Umfang folgt Funktion; der fertige Text wird nicht auf historische Wortziele hin aufgefüllt oder gekürzt.**

## Warum nicht als Kopie archivieren?

Eine zweite Kopie derselben veralteten Inhalte im aktuellen Branch würde das ursprüngliche Problem nur verschieben. Git selbst ist hier das Archiv. Wer einen alten Stand benötigt, kann ihn über die Commit-Historie wiederherstellen.

## Regel

Dateien, die in diesem Archivhinweis genannt sind, dürfen nicht als aktuelle Masterquelle, Build-Eingabe oder Abnahmekriterium verwendet werden.

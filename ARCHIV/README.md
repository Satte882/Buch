# Archivhinweis

Dieser Ordner enthält Unterlagen, die bewusst **nicht mehr zum aktiven Arbeitskontext** von `NORMALFALL` gehören.

Es gibt zwei Archivformen:

1. **physisch archivierte Konzept-/Planungsdateien**, die noch als historische Referenz nützlich sein können;
2. **nur über Git-Historie rekonstruierbare Zwischenstände**, insbesondere frühere Volltextfassungen, die nicht als Kopie im aktuellen Branch gehalten werden.

Keine Datei unter `ARCHIV/` darf als aktuelle Masterquelle, Build-Eingabe oder Abnahmekriterium verwendet werden.

## Physisch archivierte Entwicklungsunterlagen

Unter `ARCHIV/ENTWICKLUNG/` liegen bewusst aus dem Repository-Root entfernte Konzeptdateien:

- `ARCHIV/ENTWICKLUNG/Bausteine_in_5_Ebenen_zerlegen.md` – frühe Zerlegungs-/Arbeitsmethodik aus der Planungsphase; nach Abschluss des Romans keine aktive Arbeitsregel mehr.
- `ARCHIV/ENTWICKLUNG/PSYCHOTHRILLER_POSITIONIERUNG_UND_BAUSTEINE.md` – frühe Genre-/Baustein-Positionierung; die weiterhin gültige Positionierung ist inzwischen in `ROTER_FADEN.md`, `STILREFERENZ.md` und der ausgearbeiteten Bausteinarchitektur konsolidiert.

## Ausgemusterte Volltextfassungen

Die früheren fünf Teilmanuskripte unter `MANUSKRIPT/` waren während Ausbau und Review nützlich, sind nach Konsolidierung aber veraltete Parallelfassungen:

- `MANUSKRIPT/01_BAUSTEINE_01_02.md`
- `MANUSKRIPT/02_BAUSTEINE_03_04.md`
- `MANUSKRIPT/03_BAUSTEINE_05_06.md`
- `MANUSKRIPT/04_BAUSTEIN_07.md`
- `MANUSKRIPT/05_BAUSTEINE_08_09.md`

Diese Volltextfassungen werden nicht erneut im aktuellen Branch dupliziert. Sie bleiben über die Git-Historie wiederherstellbar.

**Aktuelle Source of Truth:** `AUSNAHMEZUSTAND_FINAL.md`.

## Ausgemusterte Ausbau-Steuerung

- `AUSBAU_MATRIX.md` – historischer Umsetzungsplan aus der Ausbauphase; Baseline und Wortziele sind nach Abschluss des Ausbaus überholt.
- `UMFANG_UND_AUSBAUSTEUERUNG.md` – historische Umfangssteuerung; enthielt trotz späterer Relativierung noch widersprüchliche Definition-of-Done-Formulierungen zu 75.000–80.000 Wörtern.

Diese Dateien bleiben ausschließlich über die Git-Historie nachvollziehbar.

Aktuell gilt stattdessen: **Umfang folgt Funktion; der fertige Text wird nicht auf historische Wortziele hin aufgefüllt oder gekürzt.**

## Regel

- Aktive Arbeit erfolgt ausschließlich mit den im Root-`README.md` und in `KONTEXTSYSTEM.md` ausgewiesenen Quellen.
- Archivierte Dokumente dürfen zur Entscheidungsrekonstruktion gelesen werden, aber nicht stillschweigend wieder zur Vorgabe werden.
- Wenn eine alte Entscheidung erneut relevant wird, muss sie bewusst in eine aktuelle Architekturquelle übernommen werden.
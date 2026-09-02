# NORMALFALL - KDP Cover Source of Truth

status: live-kdp-production
updated: 2026-09-02

## Verbindliche Live-Geometrie

Für die aktuell in Amazon KDP angelegte deutsche Taschenbuchausgabe von `NORMALFALL` ist der **KDP Previewer die Source of Truth**.

KDP meldet für das Cover ausdrücklich:

- erwartete Gesamtgröße: **13.356 × 9.250 Zoll**
- Trim Size des aktiven KDP-Projekts: **6 × 9 Zoll**
- äußerer Beschnitt: **0,125 Zoll**
- daraus abgeleitete Rückenbreite: **1,106 Zoll**

Die frühere Repo-Covergeometrie `11.700932 × 8.060 Zoll` auf Basis von `5,06 × 7,81 Zoll / 591 Seiten` ist für das **aktive KDP-Projekt nicht gültig** und darf nicht mehr für `NORMALFALL_COVER.pdf` verwendet werden.

## Produktionsdatei

`NORMALFALL_COVER.pdf` muss:

- genau **eine PDF-Seite** enthalten,
- exakt **13.356 × 9.250 Zoll** groß sein,
- Rückseite | Rücken | Vorderseite als zusammenhängenden Spread enthalten,
- den Barcode-/Transparency-Bereich auf der Rückseite freihalten,
- mindestens 300 dpi effektive Bildauflösung besitzen.

## Schriftstrategie

KDP hat bei der vorherigen PDF trotz lokalem Embed-Check eine Schriftwarnung ausgegeben. Deshalb enthält die Produktions-PDF ab jetzt **keine PDF-Font-Ressourcen**. Titel und Genretext werden beim Build in das 400-dpi-Coverbild gerendert; die PDF enthält nur dieses druckfähige Bild. Damit kann keine Schrift durch KDP nachträglich ersetzt oder eingebettet werden.

## Design

Freigegebene visuelle Richtung:

- tiefes Anthrazit/Schwarz
- `NORMALFALL` groß auf der Vorderseite
- geordnetes Feld vertikaler heller Linien
- eine deutlich abweichende, gebrochene rote Linie als zentrales Motiv
- `PSYCHOTHRILLER` als kleiner Genreanker
- Buchrücken mit `NORMALFALL` und kleinem Genretext
- Rückseite weitgehend leer, nur ein sehr dezentes Linienmotiv oben; Barcodebereich frei

## Build

```bash
python scripts/build_kdp_cover.py --output NORMALFALL_COVER.pdf --dpi 400
```

## Validierung

CI muss vor dem Commit der Produktionsdatei prüfen:

1. eine PDF-Seite,
2. exakt `13.356 × 9.250 Zoll`,
3. keine PDF-Font-Ressourcen,
4. effektive Bildauflösung mindestens 300 dpi.

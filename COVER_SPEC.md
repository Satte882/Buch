# KDP-Cover – NORMALFALL

status: current-ci-cover-candidate

Diese Datei ist ab sofort die **kanonische Cover-Spezifikation** und ersetzt abweichende ältere Cover-Beschreibungen in `KDP_METADATA.md`, `KDP_SUBMISSION.md` oder `KDP_PRODUKTIONSSTANDARD.md`.

## Verbindliches Design

Die Covergestaltung ist bewusst minimalistisch. Es gibt **keinen Autorennamen, kein Genrelabel, keinen Rückseitentext und keine ISBN-/Barcode-Platzhaltergrafik**.

### Vorderseite

- Titel: `NORMALFALL`
- darunter eine horizontale Linie über die **komplette Breite der Vorderseite**
- in der Linie ein einzelner EKG-/Ausschlag
- darunter ausschließlich:

  `EINE REGEL WIDERSTEHT ALLEM,`  
  `AUSSER DEM BEWEIS,`  
  `DASS ES OHNE SIE BESSER GEHT.`

### Buchrücken

- kein Titel
- kein Text
- exakt dasselbe Linien-/Ausschlagmotiv wie auf der Vorderseite, um 90 Grad gedreht
- die vertikale Linie läuft über die **komplette Höhe des Buchrückens**

### Rückseite

- ausschließlich eine durchgehende horizontale Flatline über die komplette Rückseitenbreite
- sonst vollständig leer
- insbesondere: **kein Rahmen, kein ISBN-Feld, kein Barcode-Dummy, kein Platzhaltertext**
- Amazon KDP darf den Barcode/ISBN-Bereich beim Produktionsprozess selbst belegen

## Aktuelle Produktionsgeometrie

Der aktuelle Repo-Stand des Innenraums verwendet:

- Trim Size: **5,06 × 7,81 Zoll**
- CI-Seitenzahl: **591 Seiten**
- Schwarzweiß-Inhalt
- aktuelle Cover-Kandidatenbasis: **weißes Papier**
- Cover-Beschnitt: **0,125 Zoll auf allen Außenkanten**

Nach aktueller KDP-Formel für Schwarzweiß auf weißem Papier:

- Rückenbreite: `591 × 0,002252" = 1,330932"`
- Gesamtbreite: `0,125 + 5,06 + 1,330932 + 5,06 + 0,125 = 11,700932"`
- Gesamthöhe: `0,125 + 7,81 + 0,125 = 8,060"`
- metrisch: ca. **297,204 × 204,724 mm**

Die Datei `NORMALFALL_COVER.pdf` wird in genau dieser Größe erzeugt.

## Technische Regeln

- eine PDF-Seite
- keine Crop Marks oder Hilfslinien
- vollständig eingebettete TrueType-Schriften
- weißer Full-Bleed-Hintergrund
- schwarze Vektortypografie und Vektorlinien
- Barcode-Bereich bleibt gestalterisch unberührt

Build:

```bash
python scripts/build_kdp_cover.py --pages 591 --paper white --output NORMALFALL_COVER.pdf
```

## Live-KDP-Gate

`NORMALFALL_COVER.pdf` ist für den **aktuellen Repo-Stand mit 591 Seiten und weißem Papier** maßhaltig. Die finale KDP-Seitenzahl ist weiterhin ein Live-Gate. Wenn der KDP Previewer eine andere Seitenzahl liefert oder cremefarbenes Papier gewählt wird, muss die PDF mit diesen Live-Daten neu erzeugt werden. Design und Inhaltsregeln bleiben dabei unverändert.

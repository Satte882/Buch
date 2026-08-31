# NORMALFALL – Repository

Dieses Repository enthält den vollständigen Roman **NORMALFALL**, seine verbindlichen Story-/Stilgrundlagen, den reproduzierbaren Word-Build und den deutschen KDP-Releaseblock.

## Drei Dateien, die man zuerst kennen muss

| Zweck | Verbindliche Datei |
|---|---|
| **Romantext / inhaltliche Source of Truth** | `AUSNAHMEZUSTAND_FINAL.md` |
| **Kanonische Word-/Buchausgabe** | `AUSNAHMEZUSTAND.docx` |
| **Verbindlicher Buchsatz / Fitzek-Benchmark** | `MANUSKRIPT_FORMATIERUNG.md` |

**Wichtig:** `AUSNAHMEZUSTAND.docx` wird generiert. Inhaltliche Änderungen werden ausschließlich in `AUSNAHMEZUSTAND_FINAL.md` vorgenommen und danach über den Build in die DOCX übernommen.

## Aktive Grundlagen

- `BUCHIDEE.md` – Grundidee und moralischer Kern
- `ROTER_FADEN.md` – globale Plotlogik, Positionierung und Doppelboden
- `FIGUREN.md` – Figuren- und Rollenlogik
- `STILREFERENZ.md` – Sprach- und Spannungsarchitektur
- `RECHERCHE_PLAUSIBILITAET.md` – institutionelle, rechtliche und operative Realitätsanker
- `ROMAN_MAP.md` – Story-/Szenenfolge
- `BAUSTEINE/` – Entwicklungsarchitektur und Szenenkarten
- `KONTEXTSYSTEM.md` – welche Quellen bei späteren Änderungen mitzulesen sind

Diese Dateien dürfen den finalen Romantext nicht stillschweigend überschreiben. Wenn eine Änderung der Story notwendig wird, muss sie bewusst zuerst in der passenden Architekturquelle und anschließend in `AUSNAHMEZUSTAND_FINAL.md` synchronisiert werden.

## Amazon KDP – deutscher Release

| Zweck | Datei |
|---|---|
| Buchbeschreibung | `BUCHBESCHREIBUNG_KDP.md` |
| Metadaten, Keywords, Kategorien, Preis-/ISBN-Strategie | `KDP_METADATA.md` |
| operative Amazon.de-Checkliste | `KDP_SUBMISSION.md` |
| technischer Produktionsstandard | `KDP_PRODUKTIONSSTANDARD.md` |
| verbindliche Cover-Gestaltung | `COVER_SPEC.md` |
| aktuell erzeugte Cover-PDF | **`NORMALFALL_COVER.pdf`** |

`NORMALFALL_COVER.pdf` ist die aktuell erzeugte einseitige Full-Wrap-PDF für den derzeitigen 591-Seiten-CI-Stand. Sie liegt direkt im Repository-Root und wird reproduzierbar über `scripts/build_kdp_cover.py` erzeugt. Die endgültige Rückenbreite wird erst nach der Live-Seitenzahl im KDP-Previewer bestätigt.

## Technik

- `scripts/build_book_docx.py` – erzeugt die DOCX-Grundstruktur aus dem Markdown-Master
- `scripts/polish_docx.py` – setzt den verbindlichen Buchsatz um
- `scripts/update_docx_toc.py` – materialisiert das Inhaltsverzeichnis
- `scripts/audit_scene_breaks.py` – prüft semantische Szenenbrüche
- `scripts/build_kdp_cover.py` – erzeugt die Full-Wrap-Cover-PDF
- `.github/workflows/build-book-docx.yml` – erzeugt und validiert `AUSNAHMEZUSTAND.docx`
- `.github/workflows/manuskript-metriken.yml` – misst den aktuellen finalen Markdown-Master
- `.github/workflows/build-kdp-cover.yml` – baut und validiert `NORMALFALL_COVER.pdf`

## Archiv

Alte Konzept-/Planungsdateien werden nicht mehr im Root geführt. Physisch aufbewahrte Entwicklungsunterlagen liegen unter `ARCHIV/ENTWICKLUNG/`; frühere große Zwischenfassungen bleiben über die Git-Historie nachvollziehbar.

Details und Archivregeln: `ARCHIV/README.md`.

## Arbeitsregel ab Fertigstellung

1. Keine parallelen Manuskriptfassungen erzeugen.
2. Inhalt nur in `AUSNAHMEZUSTAND_FINAL.md` ändern.
3. Format nur über `MANUSKRIPT_FORMATIERUNG.md` + Build-Skripte ändern.
4. KDP-/Cover-Arbeit nur gegen die aktuellen KDP-Dateien und `COVER_SPEC.md` ausführen.
5. Nach Änderungen den automatischen Build und seine Validierungen abwarten.
6. Historische Unterlagen unter `ARCHIV/` sind keine aktuellen Qualitäts- oder Abnahmekriterien.

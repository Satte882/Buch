# NORMALFALL – Repository

Dieses Repository enthält den vollständigen Roman **NORMALFALL**, seine verbindlichen Story-/Stilgrundlagen und den reproduzierbaren Word-Build.

## Drei Dateien, die man zuerst kennen muss

| Zweck | Verbindliche Datei |
|---|---|
| **Romantext / inhaltliche Source of Truth** | `AUSNAHMEZUSTAND_FINAL.md` |
| **Kanonische Word-/Buchausgabe** | `AUSNAHMEZUSTAND.docx` |
| **Verbindlicher Buchsatz / Fitzek-Benchmark** | `MANUSKRIPT_FORMATIERUNG.md` |

**Wichtig:** `AUSNAHMEZUSTAND.docx` wird generiert. Inhaltliche Änderungen werden ausschließlich in `AUSNAHMEZUSTAND_FINAL.md` vorgenommen und danach über den Build in die DOCX übernommen.

## Aktive Grundlagen

- `BUCHIDEE.md` – Grundidee und moralischer Kern
- `ROTER_FADEN.md` – globale Plotlogik und Doppelboden
- `FIGUREN.md` – Figuren- und Rollenlogik
- `STILREFERENZ.md` – Sprach- und Spannungsarchitektur
- `RECHERCHE_PLAUSIBILITAET.md` – institutionelle, rechtliche und operative Realitätsanker
- `ROMAN_MAP.md` – Story-/Szenenfolge
- `BAUSTEINE/` – Entwicklungsarchitektur und Szenenkarten
- `KONTEXTSYSTEM.md` – welche Quellen bei späteren Änderungen mitzulesen sind

Diese Dateien dürfen den finalen Romantext nicht stillschweigend überschreiben. Wenn eine Änderung der Story notwendig wird, muss sie bewusst zuerst in der passenden Architekturquelle und anschließend in `AUSNAHMEZUSTAND_FINAL.md` synchronisiert werden.

## Technik

- `scripts/build_book_docx.py` – erzeugt die DOCX-Grundstruktur aus dem Markdown-Master
- `scripts/polish_docx.py` – setzt den verbindlichen Buchsatz um
- `scripts/update_docx_toc.py` – materialisiert das Inhaltsverzeichnis
- `scripts/audit_scene_breaks.py` – prüft semantische Szenenbrüche
- `.github/workflows/build-book-docx.yml` – erzeugt und validiert `AUSNAHMEZUSTAND.docx`
- `.github/workflows/manuskript-metriken.yml` – misst den aktuellen finalen Markdown-Master

## Historische Unterlagen

Frühere Volltext-Splits unter `MANUSKRIPT/`, die Ausbau-Matrix und die alte Umfangssteuerung wurden aus dem aktiven Arbeitsbaum entfernt, weil sie nach Fertigstellung des Romans veraltete Zwischenstände bzw. historische Planungslogik darstellen.

Die Dateien bleiben vollständig über die Git-Historie nachvollziehbar. Sie sind in `ARCHIV/README.md` dokumentiert und dürfen nicht als aktuelle Source of Truth verwendet werden.

## Arbeitsregel ab Fertigstellung

1. Keine parallelen Manuskriptfassungen erzeugen.
2. Inhalt nur in `AUSNAHMEZUSTAND_FINAL.md` ändern.
3. Format nur über `MANUSKRIPT_FORMATIERUNG.md` + Build-Skripte ändern.
4. Nach Änderungen den automatischen Build und seine Validierungen abwarten.
5. Historische Ausbauziele sind keine aktuellen Qualitäts- oder Abnahmekriterien.

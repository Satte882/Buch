# NORMALFALL – Repository

> **RELEASE LOCK:** Die deutsche Ausgabe von **NORMALFALL** ist veröffentlicht und eingefroren. Änderungen außerhalb des englischen Release-Pfads sind ab jetzt nicht vorgesehen. Aktive Weiterarbeit erfolgt ausschließlich an `ENGLISH/` bzw. an Dateien, die nachweislich für die englische Ausgabe erforderlich sind. Siehe `RELEASE_LOCK.md`.

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

## Arbeitsregel ab Veröffentlichung

1. Die deutsche Ausgabe ist eingefroren.
2. Keine Änderungen am deutschen Romantext, Buchsatz, Cover, KDP-Metadaten oder deutschen Produktionsartefakten ohne neue ausdrückliche Nutzerfreigabe.
3. Reguläre Weiterarbeit ist ausschließlich für die englische Ausgabe zulässig (`ENGLISH/` und unmittelbar dafür notwendige Cross-Cutting-Dateien).
4. Eine englischbezogene Änderung darf den veröffentlichten deutschen Stand nicht verändern.
5. Historische Ausbauziele sind keine aktuellen Qualitäts- oder Abnahmekriterien.

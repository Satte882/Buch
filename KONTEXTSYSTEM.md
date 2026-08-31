# KONTEXTSYSTEM.md – Verbindlicher Arbeitskontext für NORMALFALL

## Zweck

Dieses Dokument legt fest, welche Quellen bei späteren Änderungen am fertigen Roman maßgeblich sind.

Der Roman befindet sich **nicht mehr in der Ausbauphase**. Es existiert nur noch eine aktive Volltextquelle.

> **Inhaltliche Source of Truth: `AUSNAHMEZUSTAND_FINAL.md`.**

Keine ältere Teilfassung, Ausbauplanung, Issue-Beschreibung oder generierte Word-Datei darf diese Quelle ersetzen.

---

## 1. Aktive Sources of Truth

### Romantext

- `AUSNAHMEZUSTAND_FINAL.md` – vollständiger finaler Romantext; einzige inhaltliche Volltextquelle

### Buchausgabe

- `AUSNAHMEZUSTAND.docx` – generierte kanonische Word-/Buchausgabe; **keine** Quelle für manuelle Inhaltsänderungen
- `MANUSKRIPT_FORMATIERUNG.md` – verbindlicher Formatierungsvertrag und Fitzek-Benchmark

### Story-, Figuren- und Stilarchitektur

- `BUCHIDEE.md` – Grundidee und moralischer Kern
- `ROTER_FADEN.md` – globale Plotlogik, Bedrohungsarchitektur und Doppelboden
- `FIGUREN.md` – Figuren- und Rollenlogik
- `STILREFERENZ.md` – Sprach- und Spannungsarchitektur
- `RECHERCHE_PLAUSIBILITAET.md` – institutionelle, rechtliche und operative Realitätsanker
- `ROMAN_MAP.md` – Story-/Szenenfolge
- `BAUSTEINE/` – Entwicklungsarchitektur, Ereignisse und Szenenkarten
- `Bausteine_in_5_Ebenen_zerlegen.md` – historische Arbeitsmethodik; nur relevant, wenn bewusst wieder auf eine Planungsebene zurückgesprungen wird
- `PSYCHOTHRILLER_POSITIONIERUNG_UND_BAUSTEINE.md` – Genre- und Thriller-Leitplanken

---

## 2. Prioritätsregel bei Widersprüchen

Bei widersprüchlichen Aussagen gilt:

1. Für den **tatsächlich geschriebenen Romantext** gilt `AUSNAHMEZUSTAND_FINAL.md`.
2. Für **Buchsatz und Word-Ausgabe** gilt `MANUSKRIPT_FORMATIERUNG.md` plus die Build-Skripte.
3. Für bewusste Storyänderungen gelten zusätzlich die thematisch zuständigen Architekturquellen (`ROTER_FADEN.md`, `FIGUREN.md`, `RECHERCHE_PLAUSIBILITAET.md`, `ROMAN_MAP.md`, `STILREFERENZ.md`).
4. Historische Issues, Commits und ausgemusterte Ausbauunterlagen sind nur Nachweise früherer Entscheidungen, keine aktuellen Masterquellen.

Wenn Architekturquelle und finaler Romantext voneinander abweichen, wird **nicht automatisch der Romantext überschrieben**. Zuerst ist zu klären, ob die Architekturdatei veraltet ist oder ob eine bewusste Romanänderung erforderlich ist.

---

## 3. Regel für spätere Inhaltsänderungen

Eine kleine sprachliche Korrektur kann direkt in `AUSNAHMEZUSTAND_FINAL.md` erfolgen, sofern sie keine Story-, Figuren-, Fakten- oder Wissenslogik verändert.

Bei einer inhaltlich relevanten Änderung gilt:

1. betroffene Stelle im finalen Roman lesen,
2. relevante Architekturquelle lesen,
3. Auswirkungen auf Plot, Figuren, Leserwissen, Doppelboden, Plausibilität und Anschlusskapitel prüfen,
4. Architekturquelle bei Bedarf bewusst aktualisieren,
5. Änderung in `AUSNAHMEZUSTAND_FINAL.md` umsetzen,
6. Build und Validierungen laufen lassen,
7. `AUSNAHMEZUSTAND.docx` nicht manuell nachbearbeiten.

Leitregel:

> **Keine Storyänderung darf nur in einer Neben- oder Ausgabedatei existieren.**

---

## 4. Pflichtkontext je Änderungsart

### Stil / Sprache

Mindestens lesen:
- konkrete Passage in `AUSNAHMEZUSTAND_FINAL.md`
- `STILREFERENZ.md`
- unmittelbaren Kapitelkontext

### Figur / Beziehung

Zusätzlich:
- `FIGUREN.md`
- relevante Entwicklungsachse aus `ROTER_FADEN.md`
- vorherige und spätere betroffene Kapitel

### Plot / Reversal / Finale / Leserwissen

Zusätzlich:
- `ROTER_FADEN.md`
- `ROMAN_MAP.md`
- relevante `BAUSTEINE/`- und Szenenkarten
- alle betroffenen Vorbereitungs- und Payoff-Stellen im finalen Roman

### Institutionelle, juristische, operative oder technische Fakten

Zusätzlich:
- `RECHERCHE_PLAUSIBILITAET.md`

### Formatierung / Word

Inhalt nicht verändern. Maßgeblich sind:
- `MANUSKRIPT_FORMATIERUNG.md`
- `scripts/build_book_docx.py`
- `scripts/polish_docx.py`
- `scripts/update_docx_toc.py`
- `.github/workflows/build-book-docx.yml`

---

## 5. Anti-Drift-Regel

- Keine parallelen Volltextfassungen anlegen.
- Keine Kapitel aus alten `MANUSKRIPT/`-Splits übernehmen; diese wurden nach Konsolidierung ausgemustert.
- Keine historischen Wortziele als aktuelle Schreibvorgabe verwenden.
- Keine Issue-Beschreibung als aktuellere Wahrheit behandeln als die Masterdateien.
- Keine generierte DOCX manuell zum neuen Master machen.

Historisch ausgemusterte Quellen sind in `ARCHIV/README.md` dokumentiert und bleiben über Git vollständig nachvollziehbar.

---

## 6. Kontext ist kein Selbstzweck

Nicht jede Änderung braucht das gesamte Repository. Es muss aber immer genug Kontext geladen werden, um die betroffene Logik sicher zu beurteilen.

> **So wenig Kontext wie möglich, so viel Kontext wie für Konsistenz notwendig.**

Bei Zweifeln ist der vollständige finale Kapitelkontext wichtiger als isolierte Sätze oder alte Planungs-Snapshots.

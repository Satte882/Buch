# Localization Profile – NORMALFALL English Edition

status: pilot
source_repository: Satte882/Buch
source_file: AUSNAHMEZUSTAND_FINAL.md
source_commit: f0aa559c27accfb136f1277e569adfb6dd9dfb96
source_blob: 26b755fddf84d8dcdd86dc44420c5c0d3ce476ce
source_language: German
source_status: final / published
working_title: NORMALFALL

## Target

- target_language: English
- target_market: international English-language KDP edition, primary market Amazon.com
- target_variant: English (US)
- genre: psychological thriller / political-institutional thriller
- audience: adult commercial thriller readers

Der englische Markttitel wird **noch nicht** festgelegt. `NORMALFALL` bleibt bis zur separaten Titel-/Metadatenentscheidung der Arbeitstitel. Die Textlokalisierung darf keine Marketingentscheidung erzwingen.

## Localization Objective

Die englische Fassung soll sich wie ein originär auf Englisch geschriebener, zeitgenössischer Psychothriller lesen. Plot, Fakten, Informationsreihenfolge, Ambiguität, Figurenwissen, moralische Spannung und die schrittweise Verschiebung von Daniels Entscheidungslogik bleiben erhalten. Deutsche Syntax und Idiomatik werden nicht konserviert, wenn sie im Englischen nach Übersetzung klingen. Das deutsche Setting und die institutionelle Realität bleiben deutsch; sie werden nicht durch US-amerikanische Entsprechungen ersetzt.

## Source-of-Truth-Regel

- Inhaltliche Source of Truth ist ausschließlich `AUSNAHMEZUSTAND_FINAL.md` am oben festgeschriebenen Commit.
- Die DOCX ist Produktionsartefakt, nicht Übersetzungsquelle.
- Spätere Änderungen am deutschen Master werden nicht stillschweigend übernommen, sondern als Delta gegen diese Source-Version geprüft.
- Die englische Edition darf den deutschen Kanon nicht rückwirkend verändern.

## Verbindliche Entscheidungen

### Setting und Eigennamen

- Personen- und Ortsnamen bleiben unverändert.
- Deutsche Institutionen, Behörden und politische Begriffe bleiben in ihrer deutschen Realität verankert.
- Keine Umdeutung von Deutschland in ein US-/UK-Setting.
- Fiktive Organisations- oder Projektnamen bleiben erhalten, sofern nicht eine spätere konkrete Lesbarkeitsentscheidung etwas anderes verlangt.

### Institutionen und Funktionen

- `BKA` wird bei einer ersten erklärungsbedürftigen Nennung funktional als `Germany's Federal Criminal Police Office (BKA)` eingeführt; danach `BKA`.
- Interne BKA-Strukturen werden nur so spezifisch übersetzt, wie es der deutsche Text tatsächlich vorgibt. Keine erfundenen US-Dienstgrade, Agencies oder Zuständigkeiten.
- `Bundestag` bleibt `Bundestag`; falls Kontext nötig ist, funktional `German parliament`, nicht `Congress`.
- Polizei-/Sicherheitsmaßnahmen werden funktional und idiomatisch übersetzt, nicht wortwörtlich (`Verkehrskontrolle` z. B. `traffic stop`, nicht `traffic control`).

### Sprache und Konventionen

- Rechtschreibung: US English.
- Dialog: standard English double quotation marks.
- Unterbrechungen: em dash, sofern funktional nötig.
- Gedanken: in die enge personale Erzählweise integriert; keine zusätzlichen kursiven Inner-Monologue-Passagen erfinden.
- Narrative Uhrzeiten: natürliches US-Englisch (`2:37 p.m.`), sofern die Uhrzeit als Prosa erscheint.
- System-/Log-/Display-Zeiten: 24-Stunden-Format beibehalten, wenn die Darstellung selbst Teil der Information ist (`23:18`).
- Maße: metrisch beibehalten, wenn das deutsche Setting oder die konkrete Beobachtung trägt. Keine unnötigen US-Umrechnungen.
- Zahlen und Daten: Bedeutung vor formaler Spiegelung; bei potenziell mehrdeutigen Datumsangaben ausschreiben.

### Dialog und Umgangssprache

- Natürliches zeitgenössisches US-Englisch, aber keine künstliche Amerikanisierung der Figuren.
- Fachlich arbeitende Figuren dürfen knapp und technisch sprechen, ohne erklärende Behördenprosa zu erzeugen.
- `du/Sie` wird nicht mechanisch ersetzt; soziale Distanz wird über Register, Anrede, Namen und Satzbau erhalten.
- Deutsche Idiome werden funktional übertragen, nicht wörtlich.
- Flüche und Umgangssprache nur dort verstärken, wo der Source-Text dieselbe Funktion trägt.

### Kulturelle Lokalisierung

Bewusst deutsch bleiben insbesondere:

- BKA und deutsche Sicherheitsarchitektur,
- deutsche Verwaltungs-/Behördenrealität,
- Bundestag und politische Institutionen,
- deutsche Orts-, Gebäude- und Alltagskontexte,
- plausible deutsche Verfahrens- und Zuständigkeitslogik.

Erklärungen für englischsprachige Leser sind nur erlaubt, wenn sie zum Verständnis zwingend nötig sind und keine Spannung, Ambiguität oder Informationsasymmetrie verändern.

## Nicht verhandelbare Treue

Die englische Edition darf ohne bewusste menschliche Entscheidung nicht:

- Plot, Reihenfolge oder Kausalität verändern,
- Informationen früher oder später offenlegen,
- Figurenwissen oder Motivation verändern,
- neue Fakten, Szenen oder Erklärungen erfinden,
- bewusste Ambiguität auflösen,
- Daniel psychologisch eindeutiger machen als im Source-Text,
- moralische oder politische Positionen stärker erklären als im Source-Text,
- deutsche Institutionen durch sachlich falsche anglophone Entsprechungen ersetzen.

## Pilot

Pilotumfang:

- Prolog
- Kapitel 1
- Kapitel 2
- Kapitel 3

Ziel des Piloten ist nicht die inhaltliche Freigabe des Plots – dieser ist Source of Truth –, sondern die Prüfung, ob die englische Stimme gleichzeitig natürlich, kommerziell lesbar und dem deutschen Roman treu ist.

status_after_translation: pending human voice approval

## Offene Entscheidungen

| Thema | Entscheidung nötig bis | Status | Entscheidung |
|---|---|---|---|
| finaler englischer Buchtitel | vor KDP-Metadaten/Produktion | open | `NORMALFALL` bleibt Arbeitstitel |
| finale englische KDP-Beschreibung | Publishing | open | nicht Teil des Piloten |

## Änderungsverlauf

| Datum | Änderung | Grund |
|---|---|---|
| 2026-08-29 | Profil angelegt, Source auf Commit `f0aa559...` eingefroren, English (US) als Pilotvariante gesetzt | Start der englischen Edition |

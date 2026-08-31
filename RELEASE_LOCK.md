# RELEASE LOCK – NORMALFALL

status: PUBLISHED_FROZEN
effective_date: 2026-08-31
german_release_baseline: `ae4400b569d98ac4c4361c27d5144bf2794f0f6c`

## Regel

Die deutsche Ausgabe von **NORMALFALL** ist veröffentlicht und wird ab jetzt als eingefrorener Produktionsstand behandelt.

Zulässige reguläre Änderungen:

- Dateien unter `ENGLISH/`
- unmittelbar englischbezogene Build-/Release-Dateien außerhalb von `ENGLISH/`, wenn sie für die englische Ausgabe technisch erforderlich sind

Nicht zulässig ohne neue ausdrückliche Nutzerfreigabe:

- Änderungen am deutschen Romantext
- Änderungen an `AUSNAHMEZUSTAND_FINAL.md` oder `AUSNAHMEZUSTAND.docx`
- Änderungen am deutschen Buchsatz
- Änderungen an deutschem Cover oder deutschen KDP-Metadaten
- erneute deutsche Produktions-/Release-Optimierungen
- allgemeines Repo-Aufräumen, wenn dadurch der veröffentlichte deutsche Stand verändert wird

## Schutzregel für englische Arbeit

Englischbezogene Änderungen dürfen den veröffentlichten deutschen Stand weder inhaltlich noch technisch verändern. Cross-Cutting-Dateien dürfen nur angepasst werden, wenn die Änderung für `ENGLISH/` erforderlich ist und die deutsche Ausgabe unverändert bleibt.

## Historie

Die am 2026-08-31 versehentlich begonnenen deutschen KDP-/Cover-/Root-Aufräumarbeiten nach `ae4400b569d98ac4c4361c27d5144bf2794f0f6c` wurden mit Einrichtung dieses Locks aus dem aktiven Baum zurückgenommen. Ihre Commit-Historie bleibt in Git nachvollziehbar.

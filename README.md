# Lunar-Mondphasen-Kalender

Ein deutschsprachiger ChatGPT-Skill zum Erstellen, Strukturieren und Pruefen von Mondphasen- und Lunar-Kalendern. Der Skill eignet sich fuer Monats- und Jahresuebersichten, Journaling, Ritualplanung, Gartenkalender, Content-Planung und redaktionelle Mondphasen-Inhalte.

## Inhalt

```text
lunar-mondphasen-kalender/
├── SKILL.md
├── README.md
└── scripts/
    └── moon_phases.py
```

## Was der Skill kann

- Mondphasen fuer Monate, Jahre oder frei gewaehlte Zeitraeume strukturieren
- Neumond, erstes Viertel, Vollmond und letztes Viertel ausgeben
- Zeitzonen bei Kalenderdaten sichtbar machen
- passende Impulse fuer Journaling, Rituale, Gartenplanung oder redaktionelle Inhalte formulieren
- Mondkalender auf Vollstaendigkeit, Reihenfolge und Plausibilitaet pruefen

## Wann verwenden

Verwende den Skill, wenn du deutschsprachige Mondphasen-Kalender oder Lunar-Planer erstellen moechtest, zum Beispiel:

- "Erstelle einen Mondphasen-Kalender fuer Juli 2026 in America/Los_Angeles."
- "Plane einen Vollmond- und Neumond-Contentkalender fuer 2027."
- "Gib mir Journaling-Fragen fuer die Mondphasen im naechsten Monat."
- "Pruefe diesen Mondkalender auf fehlende Hauptphasen."

## Wann nicht verwenden

Der Skill ist nicht gedacht fuer:

- medizinische, finanzielle oder rechtliche Entscheidungen anhand von Mondphasen
- hochpraezise astronomische Ephemeriden
- Navigation, Observatoriumsplanung oder wissenschaftliche Messdaten
- detaillierte Horoskope ohne Kalenderbezug

## Installation

Kopiere den Ordner `lunar-mondphasen-kalender/` in den Skills-Ordner deiner ChatGPT- oder Codex-Umgebung.

Die zentrale Datei ist:

```text
SKILL.md
```

Das optionale Script liegt hier:

```text
scripts/moon_phases.py
```

## Beispiel: Mondphasen berechnen

Monatsuebersicht:

```bash
python scripts/moon_phases.py --year 2026 --month 7 --timezone America/Los_Angeles
```

Jahresuebersicht:

```bash
python scripts/moon_phases.py --year 2027 --timezone Europe/Berlin
```

Freier Zeitraum als CSV:

```bash
python scripts/moon_phases.py --start 2026-06-01 --end 2026-08-31 --timezone Europe/Berlin --format csv
```

## Genauigkeitshinweis

Das Script berechnet Hauptmondphasen approximiert und ist fuer Kalenderplanung, redaktionelle Planung und kreative Anwendungen gedacht. Fuer wissenschaftliche, offizielle oder observatoriumsnahe Zwecke sollten die Daten gegen eine verlaessliche astronomische Quelle geprueft werden.

## Empfohlene Ausgabeformate

- Markdown-Tabelle fuer schnelle Kalenderuebersichten
- CSV fuer Weiterverarbeitung in Tabellenprogrammen
- redaktionelle Monatsstruktur fuer Blog, Newsletter oder Social Media
- Journaling- oder Ritualplan mit kurzen, vorsichtig formulierten Impulsen

## Qualitaetscheck

Vor der Nutzung oder Weitergabe eines erstellten Kalenders pruefen:

- Zeitraum und Zeitzone sind sichtbar.
- Alle Hauptphasen sind chronologisch sortiert.
- Der Kalender enthaelt keine absoluten Wirkversprechen.
- Spirituelle oder gartenpraktische Hinweise sind als Impulse formuliert.
- Bei berechneten Daten ist klar, dass es sich um Naeherungen handelt.

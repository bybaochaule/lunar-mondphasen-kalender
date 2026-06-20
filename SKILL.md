---
name: lunar-mondphasen-kalender
description: Verwende diesen Skill, wenn ein Agent deutschsprachige Mondphasen-, Lunar- oder Mondkalender fuer Monate, Jahre, Rituale, Gartenplanung, Journaling oder redaktionelle Inhalte erstellen, pruefen oder erklaeren soll.
Lunar-Mondphasen-Kalender
Zweck
Dieser Skill hilft dabei, deutschsprachige Mondphasen- und Lunar-Kalender zu erstellen. Er kombiniert astronomisch nachvollziehbare Mondphasen mit klarer Kalenderstruktur, nutzerfreundlicher Sprache und optionalen Deutungs- oder Planungshinweisen.
Der Skill ist fuer praktische Ausgaben gedacht: Monatskalender, Jahresuebersichten, Social-Media-Planungen, Journaling-Impulse, Gartenkalender, spirituelle Ritualplaene oder redaktionelle Mondphasen-Texte.
Wann verwenden
Aktiviere diesen Skill, wenn die Anfrage mindestens eines dieser Ziele hat:
Mondphasen fuer einen konkreten Monat, ein Jahr oder einen Zeitraum ausgeben
einen deutschsprachigen Lunar-Kalender strukturieren
Neumond, zunehmenden Mond, Vollmond und abnehmenden Mond erklaeren oder einordnen
Mondphasen mit Journaling, Ritualen, Gartenarbeit, Energieplanung oder Content-Planung verbinden
einen bestehenden Mondkalender auf Klarheit, Plausibilitaet oder Vollstaendigkeit pruefen
Wann nicht verwenden
Nicht verwenden fuer:
Horoskope, Geburtshoroskope oder astrologische Detailanalysen ohne Kalenderbezug
medizinische, finanzielle oder rechtliche Entscheidungen anhand von Mondphasen
hochpraezise astronomische Ephemeriden, Observatoriumsplanung oder Navigation
Anfragen, die nur nach allgemeiner Astronomie ohne Kalenderausgabe fragen
Eingaben
Erforderlich:
Zeitraum: Monat, Jahr oder Start- und Enddatum
Zeitzone oder Ort, falls lokale Datumsgrenzen wichtig sind
Hilfreich:
Ausgabeformat: Tabelle, Liste, Markdown, CSV, Social-Media-Plan, Ritualplan, Gartenkalender
Schwerpunkt: astronomisch-neutral, spirituell, journaling-orientiert, gartenpraktisch, redaktionell
Sprachebene: sachlich, poetisch, minimalistisch, magazinig, alltagstauglich
Genauigkeitsbedarf: ungefaehre Planung oder datenorientierte Uebersicht
Vorgehen
Klaere Zeitraum, Zeitzone und Zweck. Wenn der Zeitraum fehlt, frage nach. Wenn nur "naechster Monat" oder "dieses Jahr" genannt wird, nutze das aktuelle Datum und nenne die Annahme.
Entscheide, ob eine deterministische Berechnung sinnvoll ist. Fuer konkrete Kalenderdaten nutze nach Moeglichkeit `scripts/moon_phases.py`.
Erzeuge die Mondphasen fuer den Zeitraum. Fuehre mindestens Neumond, erstes Viertel, Vollmond und letztes Viertel auf.
Ordne die Ausgabe dem Zweck unter:
Journaling: kurze Reflexionsfragen pro Hauptphase
Rituale: knappe, sichere, nicht-medizinische Impulse
Garten: allgemeine, vorsichtige Pflanz- und Pflegehinweise
Redaktion: klare Titel, Teaser, Datumszeilen und Monatsstruktur
Planung: kompakte Tabelle mit Datum, Phase, Bedeutung und Aktion
Kennzeichne Unsicherheiten. Mondphasentermine koennen je nach Zeitzone auf ein anderes Kalenderdatum fallen.
Vermeide absolute Wirkversprechen. Formuliere Monddeutungen als kulturelle, spirituelle oder planungsbezogene Impulse, nicht als gesicherte Ursache-Wirkung.
Pruefe am Ende Datumskonsistenz, Reihenfolge, Vollstaendigkeit und Tonalitaet.
Optionales Script
Fuer Monats- und Jahresuebersichten liegt ein Hilfsscript unter `scripts/moon_phases.py`.
Beispiele:
```bash
python scripts/moon_phases.py --year 2026 --month 7 --timezone America/Los_Angeles
python scripts/moon_phases.py --year 2027 --format markdown
python scripts/moon_phases.py --start 2026-06-01 --end 2026-08-31 --timezone Europe/Berlin --format csv
```
Das Script liefert approximierte Hauptmondphasen. Fuer wissenschaftliche Genauigkeit oder offizielle Publikationen sollten die Ergebnisse gegen eine verlaessliche astronomische Quelle geprueft werden.
Erwartete Ausgaben
Eine gute Ausgabe enthaelt:
Zeitraum und Zeitzone
alle relevanten Hauptmondphasen in chronologischer Reihenfolge
ein klares, zum Nutzerzweck passendes Format
kurze Erklaerungen oder Impulse, falls gewuenscht
Hinweis auf approximative Berechnung, wenn Daten generiert wurden
Grenzen und Sicherheitsregeln
Keine Gesundheits-, Fruchtbarkeits-, Anlage-, Rechts- oder Sicherheitsentscheidungen aus Mondphasen ableiten.
Keine Behauptung, Mondphasen wuerden menschliches Verhalten sicher verursachen.
Keine erfundenen Exaktheitsangaben. Wenn Quellen oder Scriptdaten fehlen, transparent als Naeherung kennzeichnen.
Bei lokaler Relevanz immer Zeitzone oder Ort beruecksichtigen.
Bei rituellen Inhalten respektvoll, inklusiv und nicht dogmatisch schreiben.
Umgang mit fehlenden Angaben
Fehlt der Zeitraum, frage kurz nach.
Fehlt die Zeitzone, nutze die Zeitzone des Nutzers, wenn bekannt, und nenne sie.
Fehlt der Zweck, erstelle eine neutrale Kalenderuebersicht mit optionalen kurzen Bedeutungen.
Fehlt das Format, nutze Markdown-Tabelle fuer Kalenderdaten und kurze Abschnitte fuer Deutungen.
Qualitaetskontrolle
Pruefe vor der Antwort:
Sind Zeitraum und Zeitzone sichtbar?
Sind Neumond, erstes Viertel, Vollmond und letztes Viertel vollstaendig enthalten?
Stimmen Reihenfolge und Datumsbereich?
Ist die Sprache deutsch, klar und passend zum gewuenschten Schwerpunkt?
Sind spirituelle oder gartenpraktische Hinweise vorsichtig formuliert?
Ist bei berechneten Daten ein Naeherungshinweis vorhanden?

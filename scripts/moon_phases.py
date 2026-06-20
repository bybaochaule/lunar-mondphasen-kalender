#!/usr/bin/env python3
"""Approximate main moon phases for calendar planning.

This script is intentionally lightweight and dependency-free. It is suitable for
planning calendars, not for observatory-grade ephemerides.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import math
import sys
from zoneinfo import ZoneInfo


SYNODIC_MONTH = 29.530588853
KNOWN_NEW_MOON = dt.datetime(2000, 1, 6, 18, 14, tzinfo=dt.timezone.utc)

PHASES = [
    ("Neumond", 0.0, "Beginn, Intention, leiser Neustart"),
    ("Erstes Viertel", 0.25, "Entscheidung, Aufbau, erstes Handeln"),
    ("Vollmond", 0.5, "Hoehepunkt, Sichtbarkeit, Ernte"),
    ("Letztes Viertel", 0.75, "Loslassen, Auswertung, Abschluss"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate approximate main moon phases for a date range."
    )
    parser.add_argument("--year", type=int, help="Calendar year, for example 2026")
    parser.add_argument("--month", type=int, help="Calendar month 1-12")
    parser.add_argument("--start", help="Start date as YYYY-MM-DD")
    parser.add_argument("--end", help="End date as YYYY-MM-DD")
    parser.add_argument(
        "--timezone",
        default="UTC",
        help="IANA timezone, for example Europe/Berlin or America/Los_Angeles",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "csv"),
        default="markdown",
        help="Output format",
    )
    return parser.parse_args()


def month_bounds(year: int, month: int, tz: ZoneInfo) -> tuple[dt.datetime, dt.datetime]:
    start = dt.datetime(year, month, 1, tzinfo=tz)
    if month == 12:
        end = dt.datetime(year + 1, 1, 1, tzinfo=tz)
    else:
        end = dt.datetime(year, month + 1, 1, tzinfo=tz)
    return start, end


def year_bounds(year: int, tz: ZoneInfo) -> tuple[dt.datetime, dt.datetime]:
    return dt.datetime(year, 1, 1, tzinfo=tz), dt.datetime(year + 1, 1, 1, tzinfo=tz)


def explicit_bounds(start: str, end: str, tz: ZoneInfo) -> tuple[dt.datetime, dt.datetime]:
    start_date = dt.date.fromisoformat(start)
    end_date = dt.date.fromisoformat(end)
    return (
        dt.datetime.combine(start_date, dt.time.min, tzinfo=tz),
        dt.datetime.combine(end_date + dt.timedelta(days=1), dt.time.min, tzinfo=tz),
    )


def phase_events(start: dt.datetime, end: dt.datetime, tz: ZoneInfo) -> list[dict[str, str]]:
    start_utc = start.astimezone(dt.timezone.utc)
    end_utc = end.astimezone(dt.timezone.utc)
    days_since_known = (start_utc - KNOWN_NEW_MOON).total_seconds() / 86400
    base_cycle = math.floor(days_since_known / SYNODIC_MONTH) - 2
    event_count = math.ceil(((end_utc - start_utc).total_seconds() / 86400) / SYNODIC_MONTH) + 6
    events: list[dict[str, str]] = []

    for cycle in range(base_cycle, base_cycle + event_count):
        for name, fraction, meaning in PHASES:
            event_utc = KNOWN_NEW_MOON + dt.timedelta(days=(cycle + fraction) * SYNODIC_MONTH)
            if start_utc <= event_utc < end_utc:
                local = event_utc.astimezone(tz)
                events.append(
                    {
                        "date": local.date().isoformat(),
                        "time": local.strftime("%H:%M"),
                        "phase": name,
                        "meaning": meaning,
                    }
                )

    return sorted(events, key=lambda item: (item["date"], item["time"]))


def print_markdown(events: list[dict[str, str]], timezone_name: str) -> None:
    print(f"| Datum | Zeit ({timezone_name}) | Mondphase | Impuls |")
    print("|---|---:|---|---|")
    for event in events:
        print(
            f"| {event['date']} | {event['time']} | {event['phase']} | {event['meaning']} |"
        )
    print()
    print("Hinweis: Die Termine sind approximiert und fuer Kalenderplanung gedacht.")


def print_csv(events: list[dict[str, str]], timezone_name: str) -> None:
    writer = csv.DictWriter(
        sys.stdout,
        fieldnames=["date", "time", "timezone", "phase", "meaning"],
    )
    writer.writeheader()
    for event in events:
        writer.writerow({**event, "timezone": timezone_name})


def main() -> int:
    args = parse_args()
    try:
        tz = ZoneInfo(args.timezone)
    except Exception as exc:
        print(f"Unbekannte Zeitzone: {args.timezone}", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 2

    if args.start or args.end:
        if not args.start or not args.end:
            print("--start und --end muessen gemeinsam angegeben werden.", file=sys.stderr)
            return 2
        start, end = explicit_bounds(args.start, args.end, tz)
    elif args.year and args.month:
        start, end = month_bounds(args.year, args.month, tz)
    elif args.year:
        start, end = year_bounds(args.year, tz)
    else:
        print("Bitte --year oder --start/--end angeben.", file=sys.stderr)
        return 2

    events = phase_events(start, end, tz)
    if args.format == "csv":
        print_csv(events, args.timezone)
    else:
        print_markdown(events, args.timezone)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

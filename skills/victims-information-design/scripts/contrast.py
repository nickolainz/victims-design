#!/usr/bin/env python3
"""WCAG 2.1 contrast ratio between two colours, by token name or hex.

    python3 scripts/contrast.py navy mist
    python3 scripts/contrast.py teal-bright white --theme green
    python3 scripts/contrast.py "#05324b" "#ffffff"

Thresholds: 4.5 normal text, 3.0 large text (24px, or 18.66px bold),
3.0 non-text (icons, control borders, focus rings).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

TOKENS = Path(__file__).resolve().parent.parent / "assets" / "tokens" / "tokens.json"


def load(theme: str | None) -> dict[str, str]:
    data = json.loads(TOKENS.read_text(encoding="utf-8"))
    first = data["color"]["themes"][0]["id"]
    theme = theme or first
    out = {}
    for t in data["color"]["tokens"]:
        v = t["value"]
        out[t["name"]] = v.get(theme, v.get(first)) if isinstance(v, dict) else v
    return out


def to_rgb(value: str, table: dict[str, str]) -> tuple[float, float, float]:
    v = table.get(value, value).lstrip("#")
    if v.startswith("{"):
        return to_rgb(v.strip("{}"), table)
    if len(v) in (3, 4):
        v = "".join(c * 2 for c in v[:3])
    v = v[:6]
    return tuple(int(v[i : i + 2], 16) / 255 for i in (0, 2, 4))  # type: ignore[return-value]


def luminance(rgb) -> float:
    def ch(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (ch(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(a, b) -> float:
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("foreground")
    p.add_argument("background")
    p.add_argument("--theme", help="blue (default) or green")
    a = p.parse_args()
    table = load(a.theme)
    r = ratio(to_rgb(a.foreground, table), to_rgb(a.background, table))
    verdict = "AA text" if r >= 4.5 else "AA large text / non-text only" if r >= 3 else "FAILS AA"
    print(f"{a.foreground} on {a.background}: {r:.2f}:1  ({verdict})")


if __name__ == "__main__":
    main()

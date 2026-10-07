#!/usr/bin/env python3
"""Compile assets/tokens/tokens.json into assets/tokens/tokens.css.

tokens.json is the single source of truth. Run this after any token edit:

    python3 scripts/build_tokens_css.py

Output layout (matches what the original design-system tool compiled):
  * @font-face per entry in type.fonts (paths relative to tokens.css)
  * :root, [data-theme="blue"] { colours + shadows for the first theme }
  * [data-theme="green"] { overrides for each later theme }
  * :root { spacing, radius, breakpoints, --font-<family> }
  * .<style> utility class per type style (.h1, .lead, .pub-body ...)

Standard library only; works with any Python 3.8+.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
SRC = SKILL / "assets" / "tokens" / "tokens.json"
OUT = SKILL / "assets" / "tokens" / "tokens.css"
FONT_PREFIX = "../"  # tokens.css sits in assets/tokens/, fonts in assets/fonts/


def css_name(name: str) -> str:
    return name.lstrip("-.").replace(".", "\\.")


def resolve(value: str) -> str:
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        return f"var(--{css_name(value[1:-1])})"
    return value


def length(v) -> str:
    return f"{v}px" if isinstance(v, (int, float)) else str(v)


def build(tokens: dict) -> str:
    out: list[str] = [f"/* {tokens.get('name', 'Design system')} — generated from tokens.json by scripts/build_tokens_css.py. Do not edit by hand. */", ""]

    # Fonts
    for f in tokens.get("type", {}).get("fonts", []):
        path = f["file"] if "/" in f["file"] else f"fonts/{f['file']}"
        fmt = {"ttf": "truetype", "otf": "opentype", "woff": "woff", "woff2": "woff2"}[path.rsplit(".", 1)[-1].lower()]
        out.append(
            "@font-face { font-family: \"%s\"; src: url(\"%s%s\") format(\"%s\"); font-weight: %s; font-style: %s; font-display: swap; }"
            % (f["family"], FONT_PREFIX, path, fmt, f.get("weight", "400"), f.get("style", "normal"))
        )
    out.append("")

    color = tokens.get("color", {})
    themes = [t["id"] for t in color.get("themes", [])] or ["default"]
    first = themes[0]
    themed = list(color.get("tokens", [])) + list(tokens.get("shadow", {}).get("tokens", []))

    def value_for(tok, theme):
        v = tok["value"]
        if isinstance(v, dict):
            return v.get(theme, v.get(first))
        return v if theme == first else None

    for i, theme in enumerate(themes):
        sel = f':root, [data-theme="{theme}"]' if i == 0 else f'[data-theme="{theme}"]'
        lines = []
        for tok in themed:
            v = value_for(tok, theme)
            if v is None:
                continue
            if i > 0 and not isinstance(tok["value"], dict):
                continue
            lines.append(f"  --{css_name(tok['name'])}: {resolve(v)};")
        out.append(sel + " {")
        out.extend(lines)
        out.append("}")
        out.append("")

    out.append(":root {")
    for fam, toks in tokens.items():
        if fam in ("color", "shadow", "type", "meta", "name", "version") or not isinstance(toks, dict):
            continue
        for tok in toks.get("tokens", []):
            out.append(f"  --{css_name(tok['name'])}: {length(tok['value'])};")
    for key, stack in tokens.get("type", {}).get("families", {}).items():
        out.append(f"  --font-{key.lower()}: {stack};")
    out.append("}")
    out.append("")

    for group in tokens.get("type", {}).get("groups", []):
        out.append(f"/* {group['name']} */")
        for s in group.get("styles", []):
            fam = s.get("family", group.get("family"))
            decl = [f"font-family: var(--font-{fam})", f"font-size: {length(s['fontSize'])}"]
            if "lineHeight" in s:
                decl.append(f"line-height: {s['lineHeight']}")
            if "fontWeight" in s:
                decl.append(f"font-weight: {s['fontWeight']}")
            if "letterSpacing" in s:
                decl.append(f"letter-spacing: {s['letterSpacing']}")
            if "fontStyle" in s:
                decl.append(f"font-style: {s['fontStyle']}")
            out.append(f".{css_name(s['name'])} {{ {'; '.join(decl)}; }}")
        out.append("")
    return "\n".join(out)


def main() -> int:
    tokens = json.loads(SRC.read_text(encoding="utf-8"))
    OUT.write_text(build(tokens), encoding="utf-8")
    print(f"wrote {OUT.relative_to(SKILL)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

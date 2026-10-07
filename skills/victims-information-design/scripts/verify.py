#!/usr/bin/env python3
"""Check that the skill folder is intact.

    python3 scripts/verify.py

Checks: SKILL.md frontmatter; tokens.css is current with tokens.json; every
font named in tokens.json exists; every component guideline has its markup
file (except Video); every local href/src in previews and templates resolves;
every relative markdown link in references/ resolves. Exit 1 on any failure.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
fails: list[str] = []


def check(cond: bool, msg: str) -> None:
    if not cond:
        fails.append(msg)


# 1. frontmatter
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
m = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
check(bool(m), "SKILL.md: missing YAML frontmatter")
if m:
    fm = m.group(1)
    name = re.search(r"^name:\s*(\S+)", fm, re.M)
    desc = re.search(r"^description:\s*(.+)", fm, re.M)
    check(bool(name) and name.group(1) == ROOT.name, f"SKILL.md: name must equal folder name '{ROOT.name}'")
    check(bool(desc) and len(desc.group(1)) <= 1024, "SKILL.md: description missing or over 1024 chars")

# 2. tokens.css current
tokens = json.loads((ROOT / "assets/tokens/tokens.json").read_text(encoding="utf-8"))
sys.path.insert(0, str(ROOT / "scripts"))
import build_tokens_css  # noqa: E402

expected = build_tokens_css.build(tokens)
actual = (ROOT / "assets/tokens/tokens.css").read_text(encoding="utf-8")
check(expected == actual, "tokens.css is stale: run python3 scripts/build_tokens_css.py")

# 3. fonts
for f in tokens["type"]["fonts"]:
    p = ROOT / "assets" / (f["file"] if "/" in f["file"] else "fonts/" + f["file"])
    check(p.exists(), f"missing font {p.relative_to(ROOT)}")

# 4. component guidelines vs markup
for g in sorted((ROOT / "references/components").glob("*.md")):
    if g.stem == "Video":
        continue
    check((ROOT / f"assets/components/{g.stem}.html").exists(), f"no markup for {g.stem}")

# 5. local refs in HTML
for html in list((ROOT / "assets/components").glob("*.html")) + list((ROOT / "assets/templates").glob("*.html")):
    text = html.read_text(encoding="utf-8")
    for ref in re.findall(r'(?:href|src)="([^"#:]+?)"', text) + re.findall(r"url\(([^)'\"]+?\.(?:svg|png))\)", text):
        if ref.startswith("/") or ref.startswith("mailto") or ref.startswith("tel"):
            continue
        check((html.parent / ref).resolve().exists(), f"{html.relative_to(ROOT)}: broken ref {ref}")
css = (ROOT / "assets/css/bundle.css").read_text(encoding="utf-8")
for ref in re.findall(r"url\(([^)'\"]+?\.(?:svg|png))\)", css):
    check((ROOT / "assets/css" / ref).resolve().exists(), f"bundle.css: broken ref {ref}")
check("/_blob/" not in css, "bundle.css still references /_blob/ uploads")

# 6. markdown links
for md in [ROOT / "SKILL.md", ROOT / "README.md", *(ROOT / "references").rglob("*.md")]:
    for ref in re.findall(r"\]\(([^)#:]+?)\)", md.read_text(encoding="utf-8")):
        check((md.parent / ref).resolve().exists(), f"{md.relative_to(ROOT)}: broken link {ref}")

if fails:
    print("FAIL")
    for f in fails:
        print("  -", f)
    sys.exit(1)
print("OK: skill intact")

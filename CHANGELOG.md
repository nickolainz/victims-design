# Changelog

Versions follow [Semantic Versioning](https://semver.org/): major for changes that break how consumers load the skill or rename tokens, minor for new components, tokens or assets, patch for corrections.

## [1.0.0] — 2026-10-08

First release: the Victims Information (victimsinfo.govt.nz) design system as a portable agent skill at `skills/victims-information-design/`.

### Added
- `SKILL.md` entry point (Agent Skills format): safety, colour, voice and accessibility rules, per-product build guidance, and a pre-handover checklist.
- Brand book and products guide, verbatim from the design system.
- Tokens: `tokens.json` (source of truth, two section themes) and compiled `tokens.css` with `@font-face` for 16 Merriweather and Fira Sans faces.
- The live site stylesheet (`bundle.css`, theme build m=1788225938).
- Guidelines for 29 components, standalone markup previews for 28 of them, and the system cover.
- Logos, the botanical illustration, enlarged mark, banner wash and 56 icons, byte-for-byte.
- Starter web page template.
- Scripts: `build_tokens_css.py`, `contrast.py` and `verify.py` (also the repo check command).
- Installation notes for Claude Code, Claude apps, Codex and tools without skill support.
- ADR 0002 recording the decision to package as an Agent Skill.

### Known gaps
- Video has a guideline but no preview.
- Legacy greys, unused `.btn--*` classes, the Shielded widget and the search-overlay photo are not synced (as in the source system).

[1.0.0]: https://github.com/nickolainz/victims-design/releases/tag/v1.0.0

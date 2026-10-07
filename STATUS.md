# STATUS.md — victims-design

Current operational truth. Keep this current — it is not an endless
chronological diary. Overwrite stale sections rather than appending to them.

Last updated: 2026-10-08

## Implemented state

- `skills/victims-information-design/` holds the full design system as an Agent Skills folder: brand book, products guide, tokens (JSON + compiled CSS), live site stylesheet, 29 component guidelines with 28 standalone markup previews, fonts, logos, illustration, 56 icons, a starter page and three scripts (build tokens, contrast, verify).
- Exported from the claude.ai design-system artifact, version 1791405704-d9af (last changed 2026-10-03).

## Active branch / release

<!-- TODO: -->

## Known failures

- Video has a guideline but no preview (the source system could not embed YouTube).
- The site stylesheet has no skip-link styling; the starter template carries its own.

## Unfinished work

<!-- TODO: -->

## Next sensible actions

- Compare against the live site and re-sync if it has moved on (see references/source.md).
- Decide whether to symlink the skill into `.claude/skills/` and `.agents/skills/` so agents in this repo load it automatically.

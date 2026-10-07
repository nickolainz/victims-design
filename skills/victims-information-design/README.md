# victims-information-design

A portable agent skill holding the Victims Information (victimsinfo.govt.nz) design system: brand book, tokens, fonts, logos, icons, illustrations, the live site stylesheet and markup for 29 components.

It follows the open **Agent Skills** layout — a folder with `SKILL.md` (YAML frontmatter + instructions), plus `references/`, `assets/` and `scripts/` loaded on demand — so the same folder works in any tool that reads skills, and as plain instructions in any that doesn't. Everything is relative to this folder; nothing needs the network.

## Installing

| Tool | How |
|---|---|
| **Claude Code** | Copy or symlink this folder to `~/.claude/skills/victims-information-design/` (all projects) or `<repo>/.claude/skills/victims-information-design/` (one project). |
| **Claude apps (claude.ai, desktop)** | Zip the folder (the zip must contain `victims-information-design/SKILL.md`) and upload it under Settings › Capabilities › Skills. |
| **Claude API / Agent SDK** | Upload the folder as a custom skill, or point the SDK's skills directory at it. |
| **OpenAI Codex** | Copy or symlink to `~/.codex/skills/` or `<repo>/.agents/skills/`. `agents/openai.yaml` supplies the display name and default prompt. |
| **Cursor, Windsurf, Copilot, Gemini CLI and others without skill support** | Add a rule or instruction file saying: “For anything that should look or read like Victims Information, read `<path>/victims-information-design/SKILL.md` and follow it.” Or paste `SKILL.md` into the system prompt and attach files from `references/` as needed. |
| **A chat model with no file access** | Paste `SKILL.md` and `references/brand-book.md`. That is enough to stay on-brand; attach `references/tokens.md` for exact values. |

I'm confident of the Claude Code and Codex paths; the menu location in the Claude apps and the conventions of other tools change often, so check their current documentation if a path above doesn't work.

## Using it without an agent

- Open any file in `assets/components/` in a browser to see the component rendered with the real fonts and styles.
- Link `assets/tokens/tokens.css` and `assets/css/bundle.css` from a page to use the system directly.
- `assets/templates/web-page.html` is a starter page shell.

## Maintenance

```sh
python3 scripts/build_tokens_css.py   # after editing assets/tokens/tokens.json
python3 scripts/verify.py             # check the folder is intact
python3 scripts/contrast.py navy mist # WCAG contrast between two tokens
```

Provenance, what changed in packaging, and how to re-sync: `references/source.md`.

## Licences

Merriweather and Fira Sans are under the SIL Open Font Licence. The logos, illustration, icons, stylesheet and copy come from victimsinfo.govt.nz (Ministry of Justice, New Zealand Government); confirm reuse terms with the site owner before using them outside work for or with the Victims Information service.

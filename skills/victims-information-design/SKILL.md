---
name: victims-information-design
description: Design system for Victims Information (victimsinfo.govt.nz), the New Zealand Government website for people affected by crime. Use when designing, building, writing or reviewing anything that should look and read like Victims Information — web pages and components, the partner A3 dashboard, factsheets, A4 documents, slide decks, emails — or when asked for its colours, fonts, tokens, logo, icons, voice or accessibility rules.
metadata:
  version: "1.0.0"
---

# Victims Information design system

Victims Information is the New Zealand Government website for people affected by crime in Aotearoa. This skill holds its look, its voice and its building blocks, so the website and everything made beside it (partner publications, documents, presentations, email) read as one service.

**The live website is the design master.** Where this skill and https://www.victimsinfo.govt.nz disagree, follow the site and update the skill.

The reader of anything you make may be in shock, grieving, or somewhere unsafe. Every rule below follows from that.

## How to use this skill

1. **Identify the product** — website page, web component, partner publication (A3 dashboard), factsheet or A4 document, presentation, or email. Then read `references/products.md`, which says what to use for each.
2. **Read `references/brand-book.md`** in full before your first piece of work in a session. It is short and it is the authority on voice, colour, type, layout, imagery, motion and accessibility. This file only summarises it.
3. **Look things up rather than guessing:**
   - exact token values and their permitted pairings → `references/tokens.md` (or the machine-readable `assets/tokens/tokens.json`)
   - which component to use → `references/components.md`, then the component's guideline in `references/components/<Name>.md`
   - logos, icons, illustrations → `references/assets.md`
4. **Build from the real files.** Copy markup from `assets/components/<Name>.html`, link the real stylesheets, use the real font files and SVGs. Never approximate the logo, redraw an icon, or invent a colour.
5. **Check before you hand over** using the checklist at the end of this file.

If your environment cannot open files in this folder, everything you strictly need to stay on-brand is summarised below; say that you worked from the summary.

## Non-negotiables

**Safety comes before everything.**
- Every web page keeps the emergency number **111**, the 24/7 helpline **0800 650 654** and the **Quick exit** bar within reach. No layout, campaign or product may push them out of view.
- The Quick exit is a sun-yellow tab fixed to the bottom of the screen linking to `https://google.co.nz`, same tab, never the site itself. Markup: `assets/components/QuickExit.html`.
- Any factsheet or document that may reach someone at risk carries 111 and 0800 650 654.
- Phone numbers are written with spaces as they are said (0800 650 654) and linked with `tel:` wherever the format allows.
- Never hide or delay emergency contact details behind a click.

**Colour is reserved, not decorative.**
- `yellow` (#ffe666) is only for the **Get help now** pill. `sun` (#f5cc72) is only for the quick exit and the accordion rule. Neither is decoration or promotion.
- Red (`error`, `warning-icon`) appears only for errors and warnings that matter.
- No traffic-light colours for data. A rise is not automatically good news in this subject; show rises and falls in neutral teal with words.
- Never let colour carry meaning alone. Status uses words and shapes; charts must read in greyscale.

**Voice.** Plain and kind; official, not cold.
- Second person, present tense, reassuring. “We” is the Victims Information team, “you” is the reader. Never “the user”.
- Say “people affected by crime”, “victims”, “victim-survivors”, “support people”, and “whānau” alongside “families”.
- Sentence case for every heading, button and link. No full stop on headings.
- Links say where they go. Never “click here”.
- Te reo Māori words (whānau, Aotearoa, Te Hokinga ā Wairua) in normal type, not italics; mark them `lang="mi"` where the format allows.
- Define legal terms in place (“This means: …”) rather than avoiding them.
- No emoji, no exclamation marks, no humour. No blame.

**Imagery.** No stock photos of distress, injury or police tape. The only illustration is the botanical one; it is always decorative.

## The look in brief

The palette is **navy on mist**, warmed by **sun** and given direction by **teal**. Merriweather (serif) gives authority to titles; Fira Sans (humanist sans) keeps text warm. Soft rounded panels, blue-tinted shadows.

### Core colours

| Role | Token | Hex | Notes |
|---|---|---|---|
| Brand ink, h1–h3, links, logo | `navy` | #05324b | 13.4:1 on white |
| Body text | `ink` | #403f3d | All long text. Never set long text in navy or teal |
| Secondary text | `slate` | #2f3a49 | |
| Captions, hover | `slate-soft` | #475569 | |
| Lead paragraph (one per page) | `teal-dark` | #0d6c7e | 6.1:1 on white |
| Hovers, eyebrows | `teal` | #156b7b | |
| Link hover | `blue` | #055f8e | |
| Page ground | `white` | #ffffff | Pages are white |
| Header, footer, banner, panels | `mist` | #e9f7fa | |
| Enlarged mark / watermark | `mist-2` | #d3f0f5 | |
| Cards | `surface` | #f8fafc | |
| Accordions | `sand` | #f5f0eb | |
| Focus ring, focused fields | `green` | #3b6d62 | 2px solid, 5.9:1 on white |
| Inline-link focus highlight | `sun-light` | #fee9b0 | |
| Quick exit, accordion rule | `sun` | #f5cc72 | Reserved |
| Get help now pill | `yellow` | #ffe666 | Reserved |
| Dividers, card borders | `line` | #cbd5e1 | 1.5:1: a separator, never a control's only edge |
| Errors | `error` / `error-bg` | #c32121 / #fff3f3 | Forms only |

The full list (50 colours, two section themes, publication-only colours, spacing, radii, shadows, breakpoints) is in `references/tokens.md`. Section themes: **blue** is the default; **green** is used for Additional information pages (Hide my visit, Privacy, Accessibility). On the web, apply with `data-theme="green"` on a wrapper.

### Type

| Use | Family | Size / line height | Weight |
|---|---|---|---|
| Homepage hero title | Merriweather | 62px / 1.15 (40px below 576px) | 900 |
| Page title `h1` | Merriweather | 36px / 1.33 (28px below 1200px) | 900 |
| Serif section heading `h2` | Merriweather | 30px / 1.5 (24px below 1200px) | 700 |
| Content block heading (`h2` element styled `h3`) | Fira Sans | 28px / 1.29 (22px below 1200px) | 700 |
| Lead paragraph | Fira Sans, `teal-dark` | 20px / 1.5 | 400 |
| Body | Fira Sans, `ink` | 18px / 1.5 from 1400px wide, 16px below; 18px between paragraphs | 400 |

- Uppercase only on the quick exit. No letter-spaced caps except 0.04em on main navigation.
- Fonts are in `assets/fonts/` (SIL Open Font Licence). If an app cannot embed them, fall back to Georgia for Merriweather and Arial or Segoe UI for Fira Sans, and say so. Never substitute Open Sans: the site declares it but does not use it.

### Layout, shape, elevation

- Breakpoints 576 / 768 / 1024 / 1200 / 1400px, mobile first. Page side padding 35px, then 70px from 768px.
- Content pages: 12-column grid, 20px gaps, sidebar in columns 1–4 and content in 5–12.
- Blocks are 32px apart; gaps inside components are 8, 16 or 24px.
- Radii: 4px (focus outlines), 8px (cards, alerts), 12px (table of contents, tooltip), 16px (panels, banner, quick exit), pill (help and search pills).
- Every shadow is tinted with the site's blue `#104a8d` at low alpha — never grey (the quick exit is the one exception).
- **The signature composition is hero-and-card:** a white card (8px radius, `shadow-panel` or `shadow-card`) sitting on or overlapping a `mist` panel (16px radius).
- Navigating tiles carry a 4px navy top border.

### Logo and icons

- Logo: `assets/logos/victims-information-logo.svg`, navy, turning teal on hover when it is a link. Never smaller than 50px tall; never recoloured beyond navy and teal, stretched, separated from its wordmark, or set on a busy image.
- Web footers carry `assets/logos/nz-government-logo.png`, unaltered, linked to newzealand.govt.nz.
- Icons: 56 single-ink SVGs in `assets/icons/`, named by Font Awesome 5 ids. 24px beside a word, `aria-hidden="true"`, `fill="currentColor"` when inlined. No emoji, no duotone, no mixing outline and solid in one row.

### Motion

Small and quick: arrow links slide 5px over 0.44s `cubic-bezier(.4,0,.2,1)`. No looping, bouncing or parallax. All motion off for `prefers-reduced-motion`, in print and in PDFs.

## Building for each kind of product

### Web (HTML)

Load in this order:

```html
<html lang="en-nz">
<head>
  <link rel="stylesheet" href="assets/tokens/tokens.css">  <!-- tokens + @font-face -->
  <link rel="stylesheet" href="assets/css/bundle.css">     <!-- the live site stylesheet -->
</head>
```

Adjust the paths to wherever the skill folder sits relative to your page, or copy `assets/` alongside it. `tokens.css` loads the fonts from `assets/fonts/` by relative path, so keep the `assets/` folder structure intact.

- Components are HTML and CSS, not JavaScript widgets. Copy the markup from `assets/components/<Name>.html` (everything inside `<body>`) and keep every class name. Some previews carry a small `<style>` block for the preview frame; publication components carry their real CSS there.
- Website blocks expect the site's wrappers: `<main class="main base-container block-content-page mjb"><div class="inner">…</div></main>`.
- Page openings by type (from `references/products.md`):
  - homepage: HomeHero → Overview with the wayfinder card → TwoColumnCards → CallToAction
  - section landing: section Banner with callout title → Overview → GroupedTiles
  - content page: content Banner → Breadcrumbs → Overview lead → TableOfContents → blocks → FeaturedLinks
  - Get help now: WayfinderTabs
- Every page: Header (with the topbar numbers), Footer, QuickExit, a skip link, exactly one `h1`, and `lang="en-nz"`.
- Mark illustrations, page actions, wayfinder and table of contents `.no-print`.
- A starter shell is in `assets/templates/web-page.html`.

### Partner publication (A3 dashboard)

A3 landscape, HTML first with a PDF made from the same file. Masthead with key numbers, a FeatureChart, a StatusList, the AccessibilityStrip and colophon. Hairline rules, not boxes. Body 9pt, never below 7pt. Synthetic editions carry the sun “Sample edition” badge. Full rules: `references/products.md`; markup and CSS: the `Masthead`, `FeatureChart`, `StatusList`, `EngagementPanel` and `AccessibilityStrip` previews.

### Documents, slides and email (no HTML stylesheet)

When the output is a .docx, .pptx, PDF, Google Doc, slide tool or email, you cannot load the CSS. Carry the system over by value (this is a translation made when packaging the skill, from the rules in `references/products.md`):
- use the hex values from the table above, not approximations;
- Merriweather for titles and Fira Sans for text — embed the TTFs from `assets/fonts/` where the format allows, otherwise use the fallbacks named above;
- body text in `ink`, headings in `navy`, at most one `teal-dark` lead paragraph;
- reproduce the hero-and-card composition with a `mist` rounded panel and a white card for title pages and title slides;
- place the logo from the SVG (or a PNG rendered from it), never redrawn;
- safety box: bordered, 8px radius, warning icon top-left, with 111 and 0800 650 654;
- file links follow the site pattern “Title (PDF, 577 KB)”;
- email: plain text first, navy headings, one call to action as an underlined link, never the yellow pill.

## File map

```
SKILL.md                      this file: entry point and summary
README.md                     installing the skill in different tools
references/
  brand-book.md               the full brand book (authoritative)
  products.md                 what to use in each product
  tokens.md                   every token with value and usage
  components.md               component index by group
  components/<Name>.md        one guideline per component (29)
  assets.md                   logos, illustrations, icons and their rules
  source.md                   provenance and how to re-sync
assets/
  tokens/tokens.json          source of truth for tokens
  tokens/tokens.css           compiled custom properties + @font-face (generated)
  css/bundle.css              the live site stylesheet (styles.css + moj-blocks.css)
  components/<Name>.html      standalone, openable markup reference per component
  templates/web-page.html     starter page shell
  fonts/                      Merriweather and Fira Sans TTFs
  logos/ illustrations/ icons/
  source/design-system.json   index from the original design-system artifact
scripts/
  build_tokens_css.py         rebuild tokens.css after editing tokens.json
  contrast.py                 WCAG contrast between two tokens or hex values
  verify.py                   check the skill is intact
```

## Checklist before handing over

- [ ] 111, 0800 650 654 (as `tel:` links on the web) and the Quick exit are present and visible where the product could reach someone at risk.
- [ ] Every colour is a token value; yellow and sun are used only for their reserved jobs; no red except real errors or warnings; no traffic lights.
- [ ] Body text in `ink`, headings in `navy`, one lead paragraph at most in `teal-dark`.
- [ ] Merriweather for titles, Fira Sans for everything else; sentence case throughout.
- [ ] Copy is second person, plain, kind; no emoji, exclamation marks or humour; links say where they go.
- [ ] Text contrast is at least 4.5:1 (3:1 at 24px+, for icons, control borders and focus rings). Check with `python3 scripts/contrast.py <fg> <bg>`.
- [ ] Focus is visible: 2px solid `green`, or the `sun-light` highlight on inline links.
- [ ] Meaning never depends on colour alone.
- [ ] Logo, icons and illustration are the supplied files; the illustration is decorative and hidden on phones and in print.
- [ ] Web: one `h1`, skip link, `lang="en-nz"`, print styles hide `.no-print`, motion respects `prefers-reduced-motion`.

## Maintaining the skill

- Tokens: edit `assets/tokens/tokens.json`, then run `python3 scripts/build_tokens_css.py`. Never edit `tokens.css` by hand.
- After any change, run `python3 scripts/verify.py`.
- If the live site changes, the site wins: update the brand book, tokens and previews to match, and record it in `references/source.md`.

# Tokens

Generated from `assets/tokens/tokens.json` (the source of truth). CSS custom property = `--<name>`. Load `assets/tokens/tokens.css`.

## Colour

Themes: `blue` (Blue section (default)), `green` (Green section (additional information)). Values differ by theme only for the `section-*` tokens; set `data-theme="green"` on a wrapper to switch.

| Token | Value | Usage |
|---|---|---|
| `navy` | `#05324b` | The brand ink. Logo, h1–h3, links, the topbar ground, footer headings, key numbers. On white 13.4:1, on mist 12.2:1, on sun 8.8:1, on yellow 10.7:1. |
| `navy-hover` | `#1b516e` | Hover fill of the dark primary button and the open header search. White text on it 8.6:1. |
| `teal-dark` | `#0d6c7e` | Overview (lead) paragraphs at the top of content pages, and the dark primary button fill. On white 6.1:1; white text on it 6.1:1. |
| `teal` | `#156b7b` | Hover colour for the logo and main navigation; the publication accent for eyebrows, standfirsts and timings. On white 6.1:1, on mist 5.7:1. |
| `teal-bright` | `#127f93` | Light primary button fill and the file-type badge behind document links. White text on it 4.7:1, so keep button text at 18px or larger. |
| `blue` | `#055f8e` | Link hover and active colour, search-result titles, the current paginator page. On white 6.9:1. |
| `blue-external` | `#1d76a4` | The external-link icon and badge only. Not for text (5.0:1 on white, but reserved for the icon). |
| `green` | `#3b6d62` | Focus rings (2px solid outline), focused form borders, glossary terms, accordion chevrons. On white 5.9:1; a focus ring on mist 5.4:1. |
| `sage` | `#aec5bf` | Hover fill of the light primary button and the hover colour of light subtle buttons. Graphics only (1.8:1 on white). Publication range bars. |
| `sun` | `#f5cc72` | Quick exit bar, the accordion’s 4px left rule, focused form borders. Text on it is ink (6.9:1) or navy (8.8:1), never white. |
| `sun-light` | `#fee9b0` | Highlight behind a focused link and the quick exit bar’s border. Navy text on it 11.2:1. |
| `yellow` | `#ffe666` | The “Get help now” pill only. Navy text on it 10.7:1. |
| `gold` | `#d5c052` | Underline marking the current item in the topbar and main navigation. On navy 7.4:1. |
| `seed` | `#f2cc72` | The gold seed heads of the botanical illustration. In publications, used once to mark a moment on a chart. |
| `ink` | `#403f3d` | Body text, h4–h6, accordion titles. On white 10.5:1, on sand 9.3:1, on mist 9.6:1. |
| `slate` | `#2f3a49` | Secondary text: breadcrumbs, alert copy, wayfinder copy, tile and section titles. On white 11.5:1, on surface 11.0:1. |
| `slate-soft` | `#475569` | Hover text on featured links, image captions. On white 7.6:1. |
| `placeholder` | `#737373` | Placeholder text in inputs. On white 4.7:1. |
| `white` | `#ffffff` | Page ground, cards, text on navy and teal-dark fills. |
| `mist` | `#e9f7fa` | Header and footer ground, banner and hero panels, two-column card panels. |
| `mist-2` | `#d3f0f5` | The enlarged logo mark on the homepage hero, and its watermark use in publications. Never behind text it would cut through. |
| `sky` | `#f3fbff` | Info alert ground, related-links panel on section pages. |
| `ice` | `#eff6ff` | Glossary tooltip ground and the banner “Get help now” card. |
| `surface` | `#f8fafc` | Card and featured-link ground, the light end of card gradients, page-action hover. |
| `sand` | `#f5f0eb` | Accordion (closed) ground. |
| `sand-hover` | `#ede2dc` | Accordion hover ground and plain button ground. |
| `sand-open` | `#fcfbf9` | Accordion ground once opened. |
| `mint` | `#cbe6cb` | Search submit hover and support-provider tags. |
| `line` | `#cbd5e1` | Dividers, footer rules, card and alert borders. 1.5:1 on white: a separator, never the only boundary of a control. |
| `control-line` | `#94a3b8` | Reset-button border in search forms. 2.6:1 on white (below 3:1 in the source; kept exact). |
| `error` | `#c32121` | Form error borders and text, the alert site banner. On white 5.9:1. |
| `error-bg` | `#fff3f3` | Warning alert ground. |
| `warning-icon` | `#be123c` | Stroke of the warning triangle in warning alerts. On white 6.3:1. |
| `notice-info` | `#205572` | Text on the info site banner. On sky 7.7:1. |
| `notice-warning` | `#893e06` | Text on the warning site banner. On white 7.6:1. |
| `notice-warning-line` | `#de6004` | Border of the warning site banner. |
| `notice-alert` | `#932626` | Text on the alert site banner. On error-bg 7.6:1. |
| `section-background-color` | blue: `#e9f7fa` / green: `#f3fbff` | Banner panel ground for the current section. |
| `section-text-color` | blue: `#05324b` / green: `#302859` | Banner title and text. Blue: navy on mist 12.2:1; green: 12.8:1 on sky. |
| `section-subtitle-color` | blue: `#074c70` / green: `#1b516e` | Merriweather subtitle above the page title in the banner. 8.4:1 (blue) and 8.2:1 (green) on its ground. |
| `section-feature-color` | blue: `#074c70` / green: `#3b6d62` | Accent for in-page links in the section: table of contents links, arrow links, guided-process fills. Blue 9.2:1 on white; green 5.9:1. |
| `section-feature-color-hover` | blue: `#05324b` / green: `#055f8e` | Hover state of the feature colour; also the “Get help now” hover fill with white text (13.4:1 blue, 6.9:1 green). |
| `section-highlight-color` | blue: `#e4f3ed` / green: `#f3fbff` | Highlight ground in the section (selected guided-process answers). |
| `section-illustration-color` | blue: `#4db8ba` / green: `#3b6d62` | Flat fill of the botanical illustration in call-to-action blocks. Decorative only. |
| `cream` | `#fbf6ee` | Publication only: the one highlighted panel per page (engagement). Prefer sand on the web. |
| `cream-line` | `#eadfcb` | Publication only: rules inside the cream panel. |
| `line-soft` | `#e3e8ee` | Publication only: list separators inside modules. |
| `muted` | `#56606e` | Publication only: notes, axis labels, comparison captions. On white 6.4:1, on cream 5.9:1. Prefer slate-soft on the web. |
| `compare` | `#6f8f9c` | Publication only: the comparison series, always dashed or outlined, never colour alone. 3.4:1 on white (graphics, not text). |
| `desk` | `#edf1f4` | Publication only: the grey desk behind A3 sheets on screen. |

## Spacing

| Token | Value | Usage |
|---|---|---|
| `space-4` | `4px` | Hairline gaps: icon to label inside small controls, glossary button padding. |
| `space-8` | `8px` | The most common gap: between tags, list items and inline controls. |
| `space-12` | `12px` | Featured-link inner padding, gap under small headings. |
| `space-16` | `16px` | Alert padding (compact), card gaps, accordion top margin. |
| `space-20` | `20px` | Wayfinder card padding, grid column gap on content pages. |
| `space-24` | `24px` | Alert padding (full), gaps between cards. |
| `space-32` | `32px` | Space below alerts and between content blocks. |
| `space-40` | `40px` | Space around full-width related-links blocks. |
| `space-64` | `64px` | Space before alternative-formats blocks; large section breaks. |
| `gutter-mobile` | `35px` | Page side padding (.inner) on phones. |
| `gutter-desktop` | `70px` | Page side padding (.inner) from 768px. |
| `pub-gutter` | `34px` | Publication column gutter on the 12-unit A3 grid: 9mm in print (34px at 96dpi). |

## Radius

| Token | Value | Usage |
|---|---|---|
| `radius-sm` | `4px` | Focus outlines on links and arrow links, breadcrumbs. |
| `radius-md` | `8px` | Cards, alerts, featured links, wayfinder card. |
| `radius-lg` | `12px` | Table of contents panel, glossary tooltip. |
| `radius-xl` | `16px` | Banner panels, two-column card panels, the quick exit bar’s top corners, buttons and inputs (1rem). |
| `radius-step` | `24px` | Numbered content-step circles and the “Get help now” pill. |
| `radius-pill` | `100px` | Pill buttons: header search, “Get help now”, back to top, search fields. |

## Shadow

Every shadow is tinted with the site’s shadow blue #104a8d at low alpha; there are no grey drop shadows except the quick exit bar.

| Token | Value | Usage |
|---|---|---|
| `shadow-card` | `0 2px 10px #104a8d26` | Resting cards: featured tiles, grouped tiles, the wayfinder card. Same as the dashboard’s --shadow. |
| `shadow-card-hover` | `0 6px 10px #104a8d33` | Tiles on hover and focus. |
| `shadow-link-hover` | `0 3px 6px #104a8d33` | Featured links on hover, the active wayfinder tab. |
| `shadow-panel` | `0 10px 16px -5px #104a8d26` | White content cards lifted off a mist panel (call to action, two-column cards). |
| `shadow-menu` | `0 10px 12px -6px #104a8d59` | Main navigation drop-down menus. |
| `shadow-subtle` | `0 2px 4px #104a8d0d` | Page-action buttons on hover. |
| `shadow-quick-exit` | `0 -4px 5px #00000040` | The quick exit bar, lifted above the page from below. |
| `shadow-tooltip` | `0 0 1px #0f172a0f, 0 4px 6px -1px #0f172a1a, 0 2px 4px -1px #0f172a0f` | Glossary tooltip. |

## Breakpoints

Min-width breakpoints used by the site stylesheet.

| Token | Value | Usage |
|---|---|---|
| `bp-sm` | `576px` | Larger phones: hero title 56px. |
| `bp-md` | `768px` | Tablets: page gutters widen to 70px, banners show illustrations. |
| `bp-lg` | `1024px` | Desktop navigation, larger lead and accordion text. |
| `bp-xl` | `1200px` | Full heading sizes. |
| `bp-xxl` | `1400px` | Body text 18px, logo at full height. |

Breakpoints are listed as custom properties for reference; CSS cannot use `var()` inside `@media`, so write the pixel value (mobile first, `min-width`).

## Typography

Families:

- `--font-serif`: `Merriweather, Georgia, "Times New Roman", serif`
- `--font-sans`: `FiraSans, "Fira Sans", "Segoe UI", Arial, sans-serif`

Font files (all in `assets/fonts/`, SIL Open Font Licence):

- **Merriweather**: 300, 300 italic, 400, 400 italic, 700, 700 italic, 900, 900 italic
- **FiraSans**: 400, 400 italic, 500, 500 italic, 600, 600 italic, 700, 700 italic

### Headings (family: `serif`)

| Style (CSS class) | Family | Size | Line height | Weight | Tracking | Usage |
|---|---|---|---|---|---|---|
| `.display` | serif | 62px | 1.15 | 900 | -0.016em | Homepage hero title only, centred, navy. 40px below 576px, 56px from 576px. |
| `.h1` | serif | 36px | 1.33333 | 900 |  | Page titles in the banner, navy. 28px / 1.39 below 1200px. |
| `.h2` | serif | 30px | 1.5 | 700 |  | Serif section headings, alert titles and grouped-tile group names, navy. 24px / 1.33 below 1200px. |
| `.h3` | sans | 28px | 1.28571 | 700 |  | Content block headings (an h2 element carrying class h3), card titles, navy. 22px / 1.27 below 1200px. |
| `.h4` | sans | 25px | 1.12 | 700 |  | Sub-headings in ink. 20px / 1.3 below 1200px. |
| `.h5` | sans | 20px | 1.3 | 700 |  | Small headings in ink: table of contents, related links, wayfinder card title. |
| `.h6` | sans | 16px | 1.3125 | 700 |  | Run-in headings in ink, and the title of a compact alert. |

### Text (family: `sans`)

| Style (CSS class) | Family | Size | Line height | Weight | Tracking | Usage |
|---|---|---|---|---|---|---|
| `.lead` | sans | 20px | 1.5 | 400 |  | The overview paragraph under a content page banner, in teal-dark. 18px below 1024px. |
| `.intro-home` | sans | 24px | 1.83333 | 400 |  | Homepage introduction only, in ink. 18px / 1.78 on phones, 22px / 2 from 1024px. |
| `.body` | sans | 18px | 1.5 | 400 |  | All running text in ink. 16px below 1400px. Paragraph spacing 18px. |
| `.body-small` | sans | 16px | 1.5 | 400 |  | Card copy, alert copy (line height 1.75 there), footer links. |
| `.link` | sans | 18px | 1.5 | 700 |  | Inline links: navy, bold, underlined; blue on hover; sun-light highlight on focus. |
| `.nav` | sans | 16px | 1.65 | 400 | 0.04em | Main navigation items in navy, teal on hover. 18px on phones. |
| `.accordion-title` | sans | 20px | 1.3 | 400 |  | Accordion summaries in ink. 18px / 1.33 below 1024px. |
| `.meta` | sans | 14px | 1.43 | 400 |  | Topbar text, file metadata, compact alerts, glossary definitions. Never smaller than 12px. |
| `.quick-exit` | sans | 20px | 1.2 | 400 |  | The quick exit bar only: uppercase, ink on sun. |

### Serif accents (family: `serif`)

| Style (CSS class) | Family | Size | Line height | Weight | Tracking | Usage |
|---|---|---|---|---|---|---|
| `.banner-subtitle` | serif | 20px | 1.4 | 400 |  | The section name above a page title, in section-subtitle-color. 18px / 1.56 below 1200px. |
| `.toc-link` | serif | 18px | 1.33333 | 400 |  | Table of contents links, in section-feature-color. 16px below 1024px. |

### Publication (family: `serif`)

| Style (CSS class) | Family | Size | Line height | Weight | Tracking | Usage |
|---|---|---|---|---|---|---|
| `.pub-title` | serif | 32px | 1.1 | 700 | -0.012em | Masthead title (24pt in print), navy. |
| `.pub-headline` | serif | 30.67px | 1.16 | 700 | -0.01em | Feature headline (23pt; 25pt when wide, 28pt quarterly; steps down for long headlines). |
| `.pub-number` | serif | 30.67px | 1.08 | 700 | -0.01em | Key numbers (23pt), tabular lining figures, navy. |
| `.pub-section` | serif | 17.33px | 1.22 | 700 |  | Module titles (13pt) after the dot trio, navy. |
| `.pub-kicker` | serif | 14px | 1.3 | 400 |  | Masthead kicker and feature eyebrow (10.5pt), teal. |
| `.pub-standfirst` | sans | 14.67px | 1.42 | 400 |  | Feature standfirst (11pt), teal. |
| `.pub-body` | sans | 12px | 1.4 | 400 |  | Publication body (9pt); steps to 8.6pt then 8.2pt only when a page is too full. |
| `.pub-label` | sans | 10.67px | 1.3 | 600 |  | Labels, chart titles and small headings (8pt). Chart text 7.5pt; never below 7pt. |

## Provenance

```json
{
  "source": "github",
  "repo": "local: victims-dashboard (feat/website-changes-feed) + observatory services/victims",
  "ref": "website-changes-feed@1cdd0bc",
  "live": "https://www.victimsinfo.govt.nz/ theme build m=1788225938 (2026-09-01)",
  "paths": {
    "tokens": [
      "_resources/themes/victims-info/dist/css/styles.css",
      "_resources/themes/victims-info/dist/css/moj-blocks.css",
      "template/dashboard.src.html"
    ],
    "fonts": [
      "_resources/themes/victims-info/dist/font/"
    ],
    "assets": [
      "_resources/themes/victims-info/dist/images/svg-sprite-sheet.svg",
      "assets/Logos/nzgovt-logo.png"
    ]
  },
  "synced": "2026-10-03"
}
```

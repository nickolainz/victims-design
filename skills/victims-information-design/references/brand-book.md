# Brand book — Victims Information

Victims Information (victimsinfo.govt.nz) is the New Zealand Government website for people affected by crime in Aotearoa New Zealand. This system holds its look, voice and building blocks, so the website and everything made beside it (partner publications, documents, presentations) read as one service. **The live website is the design master.** When this system and victimsinfo.govt.nz disagree, follow the site and update the system.

## Principles

- **Safety before everything.** Every web page keeps the emergency number (111), the 24/7 helpline (0800 650 654) and the **QuickExit** bar within reach. No layout, campaign or product may push them out of view.
- **Calm, not alarming.** Soft `mist` grounds, rounded panels, blue-tinted shadows and a botanical illustration. Red appears only for errors and warnings that matter.
- **Plain and kind.** Short sentences, “you” for the reader, and no blame. The reader may be in shock, grieving or unsafe.
- **Official, not cold.** A serif (Merriweather) for titles gives authority; a humanist sans (Fira Sans) keeps the text warm and legible.
- **Shape and words carry meaning, never colour alone.** Status uses words and shapes, and charts read in greyscale.

## Content fundamentals

**Voice.** Second person, present tense and reassuring. Real copy from the site:

> We’re here to help
>
> If you’re in immediate danger, dial 111 and ask for the police.
>
> Whether something happened recently or in the past, this site provides information about your options, your rights, and the support available, so you can make informed decisions at your own pace.

- Say “people affected by crime”, “victims” and “victim-survivors” as the site does. Say “support people” and “whānau” alongside “families”.
- Use “we” for the Victims Information team and “you” for the reader. Never “the user”.
- Use sentence case for every heading, button and link, with no full stop on headings.
- Write numbers people dial with spaces as they are said (0800 650 654) and link them with `tel:`.
- Links say where they go (“Guide me | Coroners Court”, “organisations that can support me”). Never “click here”.
- Use approved te reo Māori words (whānau, Aotearoa, Te Hokinga ā Wairua) in normal type, without italics. Mark them `lang="mi"` where the format allows.
- Define legal terms in place with the **Glossary** pattern (“This means: …”) rather than avoiding them.
- No emoji, no exclamation marks, no humour.

## Colour

The palette is **navy on mist**, warmed by **sun** and given direction by **teal**.

| Role | Tokens | Rules |
|---|---|---|
| Identity and headings | `navy` | Logo, h1–h3, links, the topbar. The darkest colour: navy on white is 13.4:1. |
| Text | `ink` (body), `slate` (secondary), `slate-soft` (hover, captions) | Body text is always `ink`. Never set long text in navy or teal. |
| Grounds | `white`, `mist`, `surface`, `sky`, `ice`, `sand` | Pages are white. `mist` is the header, footer, banner and panel ground. `surface` is for cards, `sand` for accordions. |
| Lead and direction | `teal-dark` (lead paragraphs), `teal` (hovers, eyebrows), `blue` (link hover) | Teal is a voice, not a fill: use it for one lead paragraph per page, not for blocks of text. |
| Safety and help | `sun` (quick exit, accordion rule), `yellow` (Get help now), `sun-light` (focus highlight) | Reserved. Never use yellow for decoration or promotion. |
| Interaction | `green` | The 2px focus ring, focused fields and glossary terms. |
| Lines | `line` | Dividers and card borders. At 1.5:1 it is a separator, never the only edge of a control. |
| Status | `error`, `error-bg`, `warning-icon`, `notice-*` | Form errors, warning alerts and site banners only. |

**Section themes.** Each section sets the site’s own `--section-*` custom properties: banner ground, title and subtitle colour, feature (in-page link) colour and illustration colour. The default is **blue**. Additional information (Hide my visit, Privacy, Accessibility) uses **green**. Switch theme to see both. Wrap a page or block in `[data-theme="green"]` to apply it.

**Publication extension.** `cream`, `cream-line`, `line-soft`, `muted`, `compare` and `desk` exist for the partner dashboard and are not used on the website. On the web, use `sand` instead of `cream` and `slate-soft` instead of `muted`.

**No traffic lights.** Rises and falls in data are neutral (teal arrows and words), because a rise is not automatically good news in this subject.

## Typography

Two families, both the site’s own files (SIL Open Font Licence):

- **Merriweather** (`serif`) for page titles (`h1`, Black 900), serif headings (`h2`, Bold 700), banner subtitles, table-of-contents links, alert titles and every publication title and figure.
- **Fira Sans** (`sans`) for everything else: content headings (`h3`–`h6`, Bold), body, navigation, buttons and data labels.

Rules:
- Body is 18px from 1400px wide and 16px below, line height 1.5, with 18px between paragraphs.
- The lead paragraph (`lead`) is 20px in `teal-dark`, once per page.
- Content block headings are `h2` elements styled `h3` (Fira Sans 28px Bold, navy), so the outline stays correct while the look stays calm.
- Uppercase only on the quick exit bar. No letter-spaced caps elsewhere except the 0.04em tracking on main navigation.
- In publications, headings use balanced wrapping and paragraphs avoid widows (`text-wrap: balance` and `pretty`). Figures are tabular lining (`font-variant-numeric: tabular-nums lining-nums`).
- Open Sans is declared by the site stylesheet but no rule uses it. Don’t use it.

## Layout and spacing

- Breakpoints `bp-sm` 576, `bp-md` 768, `bp-lg` 1024, `bp-xl` 1200 and `bp-xxl` 1400 px, mobile first.
- Page side padding is `gutter-mobile` (35px), then `gutter-desktop` (70px) from 768px.
- Content pages use a 12-column grid with 20px gaps (`.inner--with-sidebar`): sidebar in columns 1–4, content in 5–12. Pages without a sidebar centre link groups at 1010px.
- Blocks are separated by `space-32`. Gaps inside components are `space-8`, `space-16` or `space-24`.
- **The hero-and-card pattern.** A white card (`radius-md`, `shadow-panel` or `shadow-card`) sits on or overlaps a `mist` panel (`radius-xl`). Used by the Banner callout, TwoColumnCards, CallToAction and the publication key numbers. It is the system’s signature composition.

## Shape and elevation

- Radii: `radius-sm` 4px (focus outlines), `radius-md` 8px (cards, alerts), `radius-lg` 12px (table of contents, tooltip), `radius-xl` 16px (panels, banner, quick exit), `radius-pill` (help and search pills).
- Every shadow is tinted with the site’s blue (`#104a8d` at low alpha): `shadow-card` at rest, `shadow-card-hover` on hover, `shadow-panel` for cards lifted off a panel. The only neutral shadow is `shadow-quick-exit`.
- Tiles that navigate carry a 4px navy top border.

## Iconography

- Use the site’s icon sprite: 50 single-ink icons whose ids follow Font Awesome 5 names (`hands-helping-solid`, `balance-scale-solid`, `phone-alt-solid`), plus the inline page icons (`get-help-now`, `print`, `share`, `back-to-top`, `arrow-link`). All are in **Assets › Icons**.
- On the site icons take `currentColor`. The files here are inked `navy` for previews. When building, inline the path and set `fill="currentColor"`.
- Icons are 24px (1.5rem), always next to a word, and `aria-hidden`. The only exception is the Get help now headset at 46px in the wayfinder card.
- No emoji, no duotone and no outline-and-solid mixing within one row.

## Imagery

- **The botanical illustration** (Assets › Illustrations) is the one illustration: leaves, gold seed heads and a cream shape. It crops into the top-right of banners and the left of call-to-action panels, takes the section’s illustration colour, and is always decorative and hidden on phones and in print.
- **The enlarged mark** (`mist-2` on `mist`) is the homepage hero background, cropped off both edges. In publications it becomes a watermark in the running head.
- Don’t use stock photos of distress, injury or police tape. People come to this site to feel safer, not to relive events.

## Logo

- `victims-information-logo.svg`: the mark (three circles joined by two diagonals) with the “Victims Information” wordmark, in `navy`, turning `teal` on hover when it is a link.
- The header logo is 50px tall on phones and grows to 90px from 1400px. Never set it smaller than 50px.
- Don’t recolour it beyond navy and teal, stretch it, separate the mark from the wordmark, or set it on a busy image.
- The footer carries the New Zealand Government logo (`nz-government-logo.png`), linked to newzealand.govt.nz and unaltered.
- **The dot trio** (three fading circles) and the **status circles** in publications are derived from the mark’s three circles. They are motifs, not logos.

## Motion

- Hover motion is small and quick: arrow links slide 5px over 0.44s (`cubic-bezier(.4,0,.2,1)`), accordion chevrons rotate 180° and button labels shift aside for an arrow over 0.6s.
- Publications may animate in once, within about 1.5 seconds: sections rise 2mm and fade, numbers count up and the chart line draws.
- No looping, bouncing or parallax. All motion is off for `prefers-reduced-motion`, in print and in PDFs.

## Accessibility

- Contrast: every text pair named in a token’s usage note meets WCAG 2.1 AA. `teal-bright` with white text (4.7:1) is only for 18px or larger button text. `line` (1.5:1) and `control-line` (2.6:1) fall short of 3:1 in the source. They are kept exact, so never let either be the only boundary of a control.
- Focus: a 2px solid `green` outline (5.9:1 on white) on buttons, tiles, tabs and links in blocks. Inline links get a `sun-light` highlight instead.
- Every page has a skip link, one `h1` and `lang="en-nz"`. Print styles hide everything marked `.no-print`: illustrations, page actions, the wayfinder and the table of contents.
- Safety features are part of accessibility here: the quick exit, the Hide my visit guidance and `tel:` links on every number.

## Using this system

- `tokens.css` declares every token as a CSS custom property. The `section-*` names are the site’s own variables. The publication colours (`navy`, `ink`, `slate`, `teal`, `blue`, `green`, `sage`, `sun`, `mist`, `mist-2`, `cream`, `cream-line`, `line`, `line-soft`, `muted`, `compare`) use the same names as the partner dashboard, so its stylesheet runs on these tokens unchanged.
- `components/bundle.css` is the live site stylesheet (styles.css and moj-blocks.css). Components are HTML-and-CSS patterns: copy the markup from a component’s preview and keep its class names. Blocks expect the site’s wrappers (`main.block-content-page.mjb > .inner`).
- Publication components carry their CSS in their previews. The reference implementation is the victims-dashboard template.
- See **Products** for what to use in each kind of product.

**Not synced:** minor greys used only by legacy or third-party styles (`#ddd`, `#595956`, `#e9e9e9`, `#f5f5f5`, launch-button bevels), the unused `.btn--*` classes, the Shielded help widget and the search-overlay photo. The Video component has no preview, because previews cannot embed YouTube.

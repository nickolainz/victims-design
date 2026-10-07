# Banner

The page banner: a rounded panel in the section’s colour that carries the page title, and on content pages the **Get help now** card and the botanical illustration.

**Variants** (`div.moj-banner`):
- `moj-banner--content-page`: mist panel (`section-background-color`), `h1` in Merriweather Black, the white “Get help now” card (`moj-banner__action`, `get-help-now` icon) at the right and the illustration bleeding off the top-right corner.
- `moj-banner--section-page`: the taller section-landing panel with `assets/Illustrations/banner-colour.png` behind it and the title in a white callout card (`moj-banner__title-callout`) overlapping the bottom edge.
- With `moj-banner__subtitle` (Merriweather 20px, `section-subtitle-color`) above the title: used where the section name helps orientation, as in the green Additional information section shown last.

**The consumer provides** the title, optionally the subtitle, and the section theme. Set the theme by giving the page the section’s `--section-*` values. Here the last banner sits inside `[data-theme="green"]`.

**Rules**
- One banner per page, always first in `main`.
- The illustration is decorative (`aria-hidden`) and never carries meaning. It is hidden on phones and in print.
- Titles are sentence case and short: the CMS page name.

---
Markup reference: [`assets/components/Banner.html`](../../assets/components/Banner.html)

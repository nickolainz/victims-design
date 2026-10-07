# FeaturedLinks

The Previous and Next tiles at the foot of a content page, which walk a reader through a section in order.

**Markup**: `.block-featured-links > .block-featured-links__links--wide.--inline` with two `a.featured-tile`. Each tile is white with a navy top border, `radius-md` and `shadow-card` (`shadow-card-hover` on hover), and holds a `strong.block-featured-links__prev` or `__next` label (Merriweather, with `arrow-left` or `arrow-right`) and the target page title.

**Rules**: generated from the section’s sibling order. Omit Previous on the first page and Next on the last. Never use the tiles for unrelated promotion.

---
Markup reference: [`assets/components/FeaturedLinks.html`](../../assets/components/FeaturedLinks.html)

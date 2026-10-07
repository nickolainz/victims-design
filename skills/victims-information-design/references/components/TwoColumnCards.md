# TwoColumnCards

Two mist panels side by side, each holding a white card with a title, one sentence and a “Read more” arrow link. Used on the homepage to route people to audience hubs.

**Markup**: `.block-tcc > .block-tcc__container` (a two-column grid) of `.block-tcc__inner > .block-tcc__style` (mist, `radius-xl`, 80px padding) holding `.block-tcc__content` (white, `radius-md`, `shadow-panel`): `h2.block-tcc__title` (Fira Sans Bold `h3` style), a `p`, and `a.block-tcc__action` with the `arrow-link` icon, which slides 5px right on hover.

**Rules**: always in pairs. Titles name an audience or a topic, not an action.

---
Markup reference: [`assets/components/TwoColumnCards.html`](../../assets/components/TwoColumnCards.html)

# PageActions

Print, Share and Back to top: the row of quiet outline buttons above the footer on every page.

**Markup**: `.page-actions > .inner > .page-actions__inner`. `button` Print (`print` icon, `window.print()`), `a` Share (`share` icon, a `mailto:?body=<page url>` link) and `a.page-actions__top` Back to top (`back-to-top` icon, `radius-pill`). Outline buttons use a `line` border and `radius-md`, `ink` text, `surface` plus `shadow-subtle` on hover, and the `green` focus ring.

**Rules**: always all three, in this order. Hidden in print.

---
Markup reference: [`assets/components/PageActions.html`](../../assets/components/PageActions.html)

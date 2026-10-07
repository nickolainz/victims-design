# Buttons

The button styles the live site renders: the yellow **Get help now** pill, guided-process fill and outline buttons, outline page actions, and arrow links.

| Pattern | Class | Look | Use |
|---|---|---|---|
| Help pill | `.header__action-button`, `.moj-overview__wayfinder-action` | `yellow`, navy bold text, `radius-pill`; turns navy (or `section-feature-color-hover`) with white text on hover | Only “Get help now” |
| Fill | `.guided-process__button--fill` | `section-feature-color` with white text | The one forward action in a flow |
| Outline | `.guided-process__button--outline` | white, `line` border; `surface` on hover | Back, Reset, secondary choices |
| Page action | `.page-actions__inner button`, `a.page-actions__top` | outline, `radius-md` (Back to top: `radius-pill`) | Print, Share, Back to top |
| Arrow link | `.block-tcc__action`, `.block-cta__action` | `arrow-link` icon and an underlined link; the arrow moves 5px on hover | “Read more” and next-step links in cards |

Every button and link takes the 2px solid `green` focus ring, or the `sun-light` highlight for inline links.

The stylesheet also defines `.btn--primary-dark`, `.btn--primary-light`, `.btn--secondary`, `.btn--tertiary` and `.btn-subtle`, but no live page uses them. Prefer the patterns above.

**Copy**: verbs, sentence case, at most three words (“Begin journey”, “Get help now”).

---
Markup reference: [`assets/components/Buttons.html`](../../assets/components/Buttons.html)

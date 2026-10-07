# CallToAction

A wide mist panel with the botanical illustration, flat-filled in the section’s illustration colour, behind a single white card that points to one next step.

**Markup**: `.block-cta > .block-cta__inner > .block-cta__style` with `.block-cta__illustration` (the botanical SVG, every path filled with `section-illustration-color`) and `.block-cta__content` (white, `radius-md`, `shadow-panel`): `h2.block-cta__title`, a sentence and `a.block-cta__action` with the arrow icon.

**Rules**
- One per page at most. The link names its destination (“Guide me | Coroners Court”), never “Click here”.
- The illustration is decorative and hidden from assistive technology.

---
Markup reference: [`assets/components/CallToAction.html`](../../assets/components/CallToAction.html)

# Accordion

A stack of expandable sections on a warm sand ground with a sun-yellow left rule, built on native `<details>`.

**Markup**: `.accordion-block` with a `ul` of `li.accordion`, each `details > summary.accordion__toggle` (title in `.accordion__title`, the `angle-down-solid` icon in `green`, rotating when open) and `.accordion__content.typography` for the body.

**States**: `sand` closed, `sand-hover` on hover or focus (with a `sun` outline), `sand-open` once open.

**The consumer provides** a summary that completes the sentence a reader is asking (“For complaints about a government agency”) and rich-text content.

**Rules**: use it for parallel options a reader picks one of, not for content everyone needs. Summaries must make sense on their own. Content stays readable in print, where every item prints open.

---
Markup reference: [`assets/components/Accordion.html`](../../assets/components/Accordion.html)

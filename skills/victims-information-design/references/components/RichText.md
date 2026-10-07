# RichText

Body content from the CMS editor: headings, paragraphs, lists and links styled by `.typography` and `.rte`.

**Markup**: `div.element > .content-element__content.rte` with an `h2.content-element__title.h3` and a `.typography` body. Inside the body:
- `h3`/`h4` sub-headings in Fira Sans Bold (`h5`/`h6` styles at that depth), in ink.
- `p` in `body` style, 18px from 1400px with 18px paragraph spacing.
- `ul` with small round bullets.
- Links in navy bold, underlined, blue on hover. External links add a visually hidden “(external link)” and the `external-link-alt-solid` icon in `blue-external`.

**Content rules**
- Plain language at about a reading age of 12: short sentences, “you” for the reader, active verbs.
- Sentence-case headings, with no full stop.
- Lists for options and steps. Bold only for a short phrase a reader must not miss.
- Use approved te reo Māori words as the site does (whānau, Aotearoa) without italics or glosses.

---
Markup reference: [`assets/components/RichText.html`](../../assets/components/RichText.html)

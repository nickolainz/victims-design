# HomeHero

The homepage hero: the enlarged logo mark in pale `mist-2` on a mist ground, the display title and the site search.

**Use** once, on the homepage. Other pages use **Banner**.

**Structure**: `.banner > .container.banner__content` with `h1.page__title.page__title--home` (Merriweather Black, `display` style, navy, centred) and `.banner__search`, which wraps the SilverStripe search form: a pill field (`radius-pill`, `line` border) with the placeholder “What are you looking for?” and a search icon button. The mark is a CSS background on `.banner__background` (`assets/Illustrations/enlarged-mark.svg`), cropped off both edges from 768px.

**Rules**
- The title states who the site is for (“Helping people affected by crime”); keep it to two lines.
- Search is the main action. Don’t add buttons beside it.

---
Markup reference: [`assets/components/HomeHero.html`](../../assets/components/HomeHero.html)

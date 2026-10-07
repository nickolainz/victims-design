# TableOfContents

“On this page”: a bordered panel listing the page’s headings as Merriweather links with a down arrow, built by script from headings marked `data-toc`.

**Markup** (generated): `.element--table-of-contents > .table-of-contents` with an `h2.h5` title and `ul` of `a.table-of-contents__link`, each holding the `on-this-page-arrow` icon. The panel has a `line` border, `radius-lg` and the white-to-`surface` gradient. Links use `toc-link` style in `section-feature-color`, darkening to `section-feature-color-hover`.

**Rules**: show it when a page has three or more content headings. Editors opt a heading out with `data-toc-ignore`. Hidden in print.

---
Markup reference: [`assets/components/TableOfContents.html`](../../assets/components/TableOfContents.html)

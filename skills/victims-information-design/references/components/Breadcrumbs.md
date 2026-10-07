# Breadcrumbs

The breadcrumb trail under the banner: ancestors as underlined `slate` links separated by a right-angle chevron, ending with the current page as plain text.

**Markup**: `.moj-breadcrumbs > .inner > ol.breadcrumbs__list`, one `li.breadcrumb__item` per level. The current page is `breadcrumb__item--active`. On phones only the parent shows, prefixed with a back arrow (`breadcrumb__item--previous`).

**Rules**: Fira Sans 14–16px in `slate`; a `green` 2px focus ring with `radius-sm`. Use the page names exactly as in the navigation.

---
Markup reference: [`assets/components/Breadcrumbs.html`](../../assets/components/Breadcrumbs.html)

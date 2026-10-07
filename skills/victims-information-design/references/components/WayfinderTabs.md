# WayfinderTabs

The Get help now page’s tab set: a list of situations (“Immediate safety help”, …) on one side, with the chosen situation’s contacts and advice shown beside it.

**Markup**: `.wayfinder-page__content` holding one `.wayfinder-tab` per situation (`wayfinder-theme-<id>`, `--active` on the open one). Each has an `a.wayfinder-tab__trigger` and `.wayfinder-tab__content-inner` with an `h2.h3.wayfinder-tab__title` and rich text. The active trigger lifts with `shadow-link-hover`. On phones the tabs stack as an accordion.

**Rules**: the first tab is always immediate safety (111). Each tab leads with the number to call, as a `tel:` link.

---
Markup reference: [`assets/components/WayfinderTabs.html`](../../assets/components/WayfinderTabs.html)

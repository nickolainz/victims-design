# Glossary

Glossary terms: legal words in body text become green, dotted-underlined buttons that open a plain-English definition.

**Markup** (added by script to text that is not marked `data-glossary-ignore`): `button.glossary-button` (`green`, bold, a 2px dotted underline; white on `green` when active) with `aria-describedby` pointing to a `div.glossary-tooltip[role=tooltip]`. The tooltip holds `.glossary-tooltip__content`: `ice` ground, a 1px `green` border, `radius-lg` and `shadow-tooltip`, with the term, its part of speech and “**This means:** …”.

**Rules**: definitions start with “This means:” and use everyday words. Mark headings, alerts and navigation `data-glossary-ignore` so terms are only linked in running text.

---
Markup reference: [`assets/components/Glossary.html`](../../assets/components/Glossary.html)

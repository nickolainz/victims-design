# EngagementPanel

The one highlighted panel a page may have: a `cream` box with a `sun` top line that asks partners for input.

**Structure**: `.mod.mod--panel` (cream, 3mm radius, `inset 0 .9mm 0 var(--sun)`), then a module head (trio and title, teal dek), then `.eng` items separated by `cream-line` rules. Each item has when (Merriweather bold, teal), the topic (navy semibold), the input needed, and “Most relevant to:” agencies joined by teal middots.

**Rules**: one panel per page at most, so the call to action stands apart. Everything else is separated by hairline rules, not boxes. On the web the equivalent emphasis is the **CallToAction** block, not a cream panel.

---
Markup reference: [`assets/components/EngagementPanel.html`](../../assets/components/EngagementPanel.html)

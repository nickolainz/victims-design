# Masthead

The lead-page masthead of an A3 publication, with the **KeyNumbers** card overlapping its lower edge (the site’s hero-and-card pattern). It shares a card with key numbers because the two always appear together.

**Masthead** (`.mh`): a mist panel (4mm radius) with the logo (27mm wide, navy), a hairline divider, the kicker (`pub-kicker`, teal), the title (`pub-title`, navy), and a dateline (period in navy semibold, cadence and date after teal middots). An optional standfirst sits right, and the botanical illustration crops into the top-right corner. `.sample-badge` (`sun` pill) appears only on synthetic editions.

**Key numbers** (`.kn`): a white card (3mm radius, `shadow-card`) pulled up 7.5mm over the masthead, with 3–5 cells divided by `line` rules. Each cell has a value (`pub-number`, tabular figures), a label in `slate` with optional footnote numbers in `teal`, and up to two comparisons (arrow and figure in teal bold, then muted text).

**Rules**
- Rises and falls are neutral teal arrows with the word “up” or “down” for screen readers. Never use green or red: a rise is not automatically good news here.
- Comparisons are calculated, never typed in.
- The reference implementation is `template/dashboard.src.html` in victims-dashboard. Its CSS custom properties map one to one onto this system’s tokens.

---
Markup reference: [`assets/components/Masthead.html`](../../assets/components/Masthead.html)

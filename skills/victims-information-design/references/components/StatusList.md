# StatusList

“Work underway and coming next”: two lists headed by status circles, each item with its timing above a navy title and one line of text.

**Motifs**, all derived from the three circles along the top of the logo mark:
- **Dot trio** (`svg.trio`, viewBox 0 0 34 10: three r4.2 circles at opacity 1, .72 and .45 in `teal`). Marks every module title and the feature eyebrow.
- **Status circles** (`svg.glyph`, 12×12): filled `navy` means available or done, half-filled means in progress or underway, and a dashed `compare` outline means planned or coming next. The shape carries the meaning and a word always goes alongside.

**Structure**: `.work` grid of `.work__col`. The head (`.work__head`) is the glyph plus a label over a solid navy rule (underway) or a dashed `compare` rule (coming next). Each `.item` has a timing in teal (`.item__timing`), a title in navy semibold and text in `pub-body`.

---
Markup reference: [`assets/components/StatusList.html`](../../assets/components/StatusList.html)

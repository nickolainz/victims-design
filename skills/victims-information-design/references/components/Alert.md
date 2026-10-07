# Alert

A bordered callout for safety-critical or must-read information, with an icon at the top left.

**Variants** (`div.block-alert`):
- `block-alert--warning`: the `exclamation-triangle` icon stroked in `warning-icon`. Used for “in immediate danger, call 111” and similar safety content. On the site this is a shared (virtual) block placed on many pages.
- `block-alert--info`: the `info-circle-solid` icon in navy, for helpful context (“Who can help”).
- `--compact` and `--super-compact` reduce padding and type for narrow columns.

**Anatomy**: 1px `line` border, `radius-md`, padding 24px 32px 24px 64px. Title in `h2` Merriweather (or `h6` when compact), copy in `slate` at 16px / 1.75.

**Rules**
- Emergency alerts always give the number first, as a word and a `tel:` link.
- No more than one warning alert per screen. Never use one for marketing or news.
- The icon is decorative. The title carries the meaning.

---
Markup reference: [`assets/components/Alert.html`](../../assets/components/Alert.html)

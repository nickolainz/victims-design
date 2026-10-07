# QuickExit

The quick exit bar: a sun-yellow tab fixed to the bottom of the screen that takes the visitor straight to google.co.nz.

**Use** on every page of every web product about victimisation. People may be reading somewhere unsafe; leaving must take one tap.

**Markup**: `a.quick-exit#quick-exit` with `href="https://google.co.nz"`, the label “Quick exit” and the `sign-out-alt-solid` icon. Uppercase Fira Sans 20px in `ink` on `sun`, a 4px `sun-light` border, `radius-xl` top corners, `shadow-quick-exit`. It sits fixed at the bottom with 1rem side insets and underlines on hover and focus.

**Rules**
- Keep the destination neutral (a search engine). Never link it to the site itself, and never open a new tab.
- Pair it with “Hide my visit” guidance (Additional information › Hide my visit) wherever browsing history matters.
- It is hidden in print.

---
Markup reference: [`assets/components/QuickExit.html`](../../assets/components/QuickExit.html)

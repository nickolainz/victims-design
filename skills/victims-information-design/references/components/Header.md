# Header

The site header: a navy emergency topbar above a mist band with the logo and the five main sections.

**Use** at the top of every web page, unchanged. It is the first thing a person in crisis sees, so the emergency number and helpline always lead.

**Structure** (`header.header`):
- `.topbar` (navy ground): “In emergency: call 111” and “24/7 helpline: 0800 650 654” as `tel:` links in white bold, the utility links (Victim rights, Make a complaint, Contact) and the white pill **Search** button.
- `.header__bg-holder` (mist): the logo (`.header__logo-link`, navy, teal on hover) and `nav.main-nav__menu` with one `button.main-nav__link--children` per section. Each opens a mega menu (`.navbar__section`, white, `shadow-menu`), omitted from this preview.
- On phones the topbar text shortens (“Emergency: Call 111”, “Helpline: 0800 650 654”) and the navigation collapses behind the bars icon, with a yellow **Get help now** pill in the menu.

**Rules**
- Main navigation is Fira Sans 16px, `letter-spacing: .04em`, navy; the current section is underlined in `gold`.
- Never remove or reorder the topbar numbers. Never add a third number.
- The logo is the inline SVG from `assets/Logos/victims-information-logo.svg` with its fill set to `currentColor`, so it can take the teal hover.

---
Markup reference: [`assets/components/Header.html`](../../assets/components/Header.html)

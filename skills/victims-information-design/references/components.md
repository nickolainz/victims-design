# Components

Every component is an HTML-and-CSS pattern, not a JavaScript widget. To use one: read its guideline in `references/components/<Name>.md`, open `assets/components/<Name>.html`, copy the markup inside `<body>`, keep every class name, and load `assets/tokens/tokens.css` then `assets/css/bundle.css`.

Website blocks expect the site's wrappers: `<main class="main base-container block-content-page mjb"><div class="inner">…</div></main>` (content pages with a sidebar use `.inner--with-sidebar`). Publication components carry their own CSS inside their preview file; copy the `<style>` block with the markup.

## Page furniture

| Component | What it is | Guideline | Markup |
|---|---|---|---|
| **Banner** | The page banner: a rounded panel in the section’s colour that carries the page title, and on content pages the **Get help now** card and the botanical illustration. | [Banner.md](components/Banner.md) | [Banner.html](../assets/components/Banner.html) |
| **Breadcrumbs** | The breadcrumb trail under the banner: ancestors as underlined `slate` links separated by a right-angle chevron, ending with the current page as plain text. | [Breadcrumbs.md](components/Breadcrumbs.md) | [Breadcrumbs.html](../assets/components/Breadcrumbs.html) |
| **Footer** | The site footer: a sitemap of every section and its children on a mist-to-white gradient, then copyright, the secondary links and the New Zealand Government logo. | [Footer.md](components/Footer.md) | [Footer.html](../assets/components/Footer.html) |
| **Header** | The site header: a navy emergency topbar above a mist band with the logo and the five main sections. | [Header.md](components/Header.md) | [Header.html](../assets/components/Header.html) |
| **HomeHero** | The homepage hero: the enlarged logo mark in pale `mist-2` on a mist ground, the display title and the site search. | [HomeHero.md](components/HomeHero.md) | [HomeHero.html](../assets/components/HomeHero.html) |
| **PageActions** | Print, Share and Back to top: the row of quiet outline buttons above the footer on every page. | [PageActions.md](components/PageActions.md) | [PageActions.html](../assets/components/PageActions.html) |
| **QuickExit** | The quick exit bar: a sun-yellow tab fixed to the bottom of the screen that takes the visitor straight to google.co.nz. | [QuickExit.md](components/QuickExit.md) | [QuickExit.html](../assets/components/QuickExit.html) |

## Content blocks

| Component | What it is | Guideline | Markup |
|---|---|---|---|
| **Accordion** | A stack of expandable sections on a warm sand ground with a sun-yellow left rule, built on native `<details>`. | [Accordion.md](components/Accordion.md) | [Accordion.html](../assets/components/Accordion.html) |
| **Alert** | A bordered callout for safety-critical or must-read information, with an icon at the top left. | [Alert.md](components/Alert.md) | [Alert.html](../assets/components/Alert.html) |
| **Buttons** | The button styles the live site renders: the yellow **Get help now** pill, guided-process fill and outline buttons, outline page actions, and arrow links. | [Buttons.md](components/Buttons.md) | [Buttons.html](../assets/components/Buttons.html) |
| **CallToAction** | A wide mist panel with the botanical illustration, flat-filled in the section’s illustration colour, behind a single white card that points to one next step. | [CallToAction.md](components/CallToAction.md) | [CallToAction.html](../assets/components/CallToAction.html) |
| **ContentStep** | A numbered step: a large number in a circle beside the step’s heading and instructions, for procedures a reader follows in order. | [ContentStep.md](components/ContentStep.md) | [ContentStep.html](../assets/components/ContentStep.html) |
| **FeaturedLinks** | The Previous and Next tiles at the foot of a content page, which walk a reader through a section in order. | [FeaturedLinks.md](components/FeaturedLinks.md) | [FeaturedLinks.html](../assets/components/FeaturedLinks.html) |
| **Glossary** | Glossary terms: legal words in body text become green, dotted-underlined buttons that open a plain-English definition. | [Glossary.md](components/Glossary.md) | [Glossary.html](../assets/components/Glossary.html) |
| **GroupedTiles** | “In this section”: groups of link tiles on section landing pages, each group under a Merriweather heading. | [GroupedTiles.md](components/GroupedTiles.md) | [GroupedTiles.html](../assets/components/GroupedTiles.html) |
| **GuidedProcess** | “Guide me”: an interactive, question-led walk through a process, such as the Coroners Court, that shows only the steps that apply to the reader. | [GuidedProcess.md](components/GuidedProcess.md) | [GuidedProcess.html](../assets/components/GuidedProcess.html) |
| **Overview** | The opening of a page: a short “Overview” in the section’s lead style. | [Overview.md](components/Overview.md) | [Overview.html](../assets/components/Overview.html) |
| **RelatedLinks** | “Related links and resources”: a short list of documents and pages as bordered link rows with a type badge at the right. | [RelatedLinks.md](components/RelatedLinks.md) | [RelatedLinks.html](../assets/components/RelatedLinks.html) |
| **ResourceList** | A titled list of downloadable publications, each a link with a file-extension icon and the type and size in brackets. | [ResourceList.md](components/ResourceList.md) | [ResourceList.html](../assets/components/ResourceList.html) |
| **RichText** | Body content from the CMS editor: headings, paragraphs, lists and links styled by `.typography` and `.rte`. | [RichText.md](components/RichText.md) | [RichText.html](../assets/components/RichText.html) |
| **TableOfContents** | “On this page”: a bordered panel listing the page’s headings as Merriweather links with a down arrow, built by script from headings marked `data-toc`. | [TableOfContents.md](components/TableOfContents.md) | [TableOfContents.html](../assets/components/TableOfContents.html) |
| **TwoColumnCards** | Two mist panels side by side, each holding a white card with a title, one sentence and a “Read more” arrow link. | [TwoColumnCards.md](components/TwoColumnCards.md) | [TwoColumnCards.html](../assets/components/TwoColumnCards.html) |
| **Video** | An embedded YouTube video (`youtube-nocookie.com`) in a 16:10 holder. | [Video.md](components/Video.md) | none |
| **WayfinderTabs** | The Get help now page’s tab set: a list of situations (“Immediate safety help”, …) on one side, with the chosen situation’s contacts and advice shown beside it. | [WayfinderTabs.md](components/WayfinderTabs.md) | [WayfinderTabs.html](../assets/components/WayfinderTabs.html) |

## Publication

| Component | What it is | Guideline | Markup |
|---|---|---|---|
| **AccessibilityStrip** | The one-line accessibility and languages strip at the foot of a publication, followed by the colophon (numbered notes, team, contact and the sample statement). | [AccessibilityStrip.md](components/AccessibilityStrip.md) | [AccessibilityStrip.html](../assets/components/AccessibilityStrip.html) |
| **EngagementPanel** | The one highlighted panel a page may have: a `cream` box with a `sun` top line that asks partners for input. | [EngagementPanel.md](components/EngagementPanel.md) | [EngagementPanel.html](../assets/components/EngagementPanel.html) |
| **FeatureChart** | The lead feature of a publication: an eyebrow with the dot trio, a Merriweather headline, a teal standfirst, short text with two supporting figures, and a line chart. | [FeatureChart.md](components/FeatureChart.md) | [FeatureChart.html](../assets/components/FeatureChart.html) |
| **Masthead** | The lead-page masthead of an A3 publication, with the **KeyNumbers** card overlapping its lower edge (the site’s hero-and-card pattern). | [Masthead.md](components/Masthead.md) | [Masthead.html](../assets/components/Masthead.html) |
| **StatusList** | “Work underway and coming next”: two lists headed by status circles, each item with its timing above a navy title and one line of text. | [StatusList.md](components/StatusList.md) | [StatusList.html](../assets/components/StatusList.html) |

## Cover

`assets/components/Cover.html` is the design system's own title card (a strip of navy, mist-2, sun and teal-dark blocks with the dot trio and diagonal pills). It is a worked example of composing with the tokens, not a component to ship.

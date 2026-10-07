# Video

An embedded YouTube video (`youtube-nocookie.com`) in a 16:10 holder. Print shows the video’s URL instead.

**Markup**: `.block-video > .block-video__holder.no-print[data-provider][style="aspect-ratio: 16 / 10"]` containing an `iframe.video__player.video__player--youtube` with `aria-label="YouTube Video Player"`, followed by `a.only-print` with the URL. The holder takes the `green` focus ring.

**Rules**: always the privacy-enhanced `youtube-nocookie.com` domain with `rel=0`. Every video needs captions and a text summary on the page. No preview here, because the design system cannot embed third-party frames.

---
No preview file (the source system could not embed this component).

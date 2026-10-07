# Assets

All files are copied byte-for-byte from the design system. Never redraw, recolour (beyond what is stated) or approximate them.

## Logos — `assets/logos/`

- `victims-information-logo.svg`: the Victims Information logo (mark and wordmark), 120 × 70 viewBox, one path, filled `navy` (#05324b). On the site it is inline with `fill="currentColor"` and turns `teal` (#156b7b) on hover. Minimum height 50px.
- `nz-government-logo.png`: the New Zealand Government logo from the site footer (200 × 21), linked to newzealand.govt.nz. Use it as supplied, never recoloured or redrawn.

Files:

- `assets/logos/nz-government-logo.png`
- `assets/logos/victims-information-logo.svg`

## Illustrations — `assets/illustrations/`

- `botanical.svg`: the site’s botanical illustration (569 × 522): leaves in a teal-to-blue gradient, gold `seed` heads and a cream shape, multiplied over the ground. It crops into the top-right of content and section banners. In call-to-action blocks every path is flat-filled with `section-illustration-color`. Always decorative.
- `enlarged-mark.svg`: the logo mark alone in `mist-2` (#d3f0f5), used large and cropped as the homepage hero background on `mist`, and as the running-head watermark in publications.
- `banner-colour.png`: the soft colour wash behind section-landing banners (1440 × 1024).

Files:

- `assets/illustrations/banner-colour.png`
- `assets/illustrations/botanical.svg`
- `assets/illustrations/enlarged-mark.svg`

## Icons — `assets/icons/`

The site’s icon set: the 50 symbols of the live `svg-sprite-sheet.svg`, one file each and named by sprite id, plus six icons the page markup draws inline (`get-help-now`, `arrow-link`, `print`, `share`, `back-to-top`, `on-this-page-arrow`).

- **Ink:** every file is filled `navy` (#05324b) so it shows in previews. On the site the paths use `currentColor`. When building, inline the SVG and set `fill="currentColor"` so the icon follows its text colour.
- **Size:** 24px (1.5rem) next to text, 29px in alerts and 46px for the wayfinder headset.
- **Meaning:** decorative (`aria-hidden="true"`) and always beside a word. The file-type icons (`file-pdf-solid` and others) go with the “(PDF, 577 KB)” text.
- **Key uses:** `sign-out-alt-solid` quick exit; `search` header and hero search; `bars-solid` and `close` mobile menu; `angle-down-solid` accordion and navigation; `exclamation-triangle-solid` and `info-circle-solid` alerts; `external-link-alt-solid` external links in `blue-external`; `envelope` email links; `get-help-now` banner and wayfinder card.

Files:

`angle-double-right-solid`, `angle-down-solid`, `angle-right-solid`, `angle-up-solid`, `arrow-left`, `arrow-link`, `arrow-right`, `back-to-top`, `balance-scale-solid`, `bars-solid`, `bell-solid`, `caret-down`, `check-circle-solid`, `clipboard-list-solid`, `close-icon-circle`, `close`, `comment-alt-solid`, `comments-solid`, `ellipsis-v-solid`, `envelope`, `exclamation-circle-solid`, `exclamation-triangle-solid`, `external-link-alt-solid`, `file-alt-solid`, `file-img-solid`, `file-light`, `file-pdf-light`, `file-pdf-solid`, `file-solid`, `fist-raised-solid`, `get-help-now`, `glasses-solid`, `hand-paper-solid`, `hands-helping-solid`, `heart`, `info-circle-solid`, `landmark-solid`, `link-solid`, `money-check-alt-solid`, `on-this-page-arrow`, `phone-alt-solid`, `print`, `question-solid`, `restroom-solid`, `search-solid`, `search`, `share`, `sign-out-alt-solid`, `sms-solid`, `times-solid-1`, `times-solid`, `unlock-alt-solid`, `user-edit-solid`, `user-friends-solid`, `user`, `users-solid`

## Using an icon in HTML

Inline the SVG's `<path>` so it inherits text colour:

```html
<svg class="icon" viewBox="0 0 24 24" width="24" height="24" aria-hidden="true" focusable="false">
  <path d="…path data from assets/icons/<name>.svg…" fill="currentColor"/>
</svg>
```

Check the `viewBox` of the source file: most icons are 24 × 24 but a few are not; copy it rather than assuming.

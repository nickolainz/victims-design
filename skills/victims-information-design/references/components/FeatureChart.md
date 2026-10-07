# FeatureChart

The lead feature of a publication: an eyebrow with the dot trio, a Merriweather headline, a teal standfirst, short text with two supporting figures, and a line chart.

**Chart rules** (bespoke inline SVG, drawn to the space available after layout):
- Primary series: a 2.4px `navy` line with a direct end label. Comparison series: a 1.5px dashed `compare` line, labelled the same way. No legend inside the plot. A key sits above it.
- Dotted gridlines at 1, 2, 2.5 or 5 steps. Month labels show the year on the first month and on January.
- An event marker is a `teal` vertical rule with a two-line label, a pale `mist` tint for the period after it, and the gold `seed` heads, used once.
- No pies, gauges or gradients. Series differ by line style or fill, never colour alone, so charts read in greyscale print.
- Every chart has a text title and a screen-reader data table.

**Type**: eyebrow `pub-kicker`, headline `pub-headline` (steps down for long headlines), standfirst `pub-standfirst` in teal, figures `pub-number` at 17pt.

---
Markup reference: [`assets/components/FeatureChart.html`](../../assets/components/FeatureChart.html)

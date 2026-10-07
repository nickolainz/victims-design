# GuidedProcess

“Guide me”: an interactive, question-led walk through a process, such as the Coroners Court, that shows only the steps that apply to the reader. This preview shows its introduction screen.

**Structure** (rendered by `guided-process.js` into `#guided-process`): `.guided-process__intro` with the “Guide Me” eyebrow in `section-feature-color`, an `h2.h3` title, the how-to-use copy, an optional info **Alert**, then `.guided-process__intro--buttons`: an outline **Back** button and a filled **Begin journey** button (`guided-process__button--fill`, `section-feature-color`, darkening on hover). Each later step is a question with answer buttons (`guided-process__actions--button`), and previous answers collapse into a sand accordion.

**Rules**
- Always offer Back and Reset. People must be able to leave or start again at any point.
- Questions are single-choice and in plain words. Never ask for personal details.

---
Markup reference: [`assets/components/GuidedProcess.html`](../../assets/components/GuidedProcess.html)

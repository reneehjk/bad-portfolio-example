# bad-portfolio-example

A satirical product-design portfolio built to demonstrate **everything wrong** with a portfolio. Every flaw is intentional, labeled in the code (`<!-- BAD: ... -->` / `/* BAD: ... */`), and obvious enough to point at during a talk on bad UX and accessibility.

**Do not copy this site. It fails WCAG on purpose.** Flashing animations are kept under 3 flashes/second so the presentation itself is not a seizure risk.

Open `index.html` in a browser (double-click, or `python3 -m http.server` from this folder).

## Pages

| File | Pretends to be | Visual identity (intentionally inconsistent) |
| --- | --- | --- |
| `index.html` | Home | Neon green, orange, Comic Sans / Impact / Papyrus |
| `stuff.html` | Case study 1 | Maroon, lime, Times / Brush Script |
| `click.html` | Case study 2 | Hot pink, cyan, Georgia / Trebuchet |
| `things.html` | Case study 3 | Yellow, black, Impact / Comic Sans |
| `about.html` | About | Brown, teal, Trebuchet / Papyrus |
| `keep-going.html` → `almost.html` → `contact.html` | Contact, three clicks deep | Olive/navy, then dark/red, then baby blue/maroon |

Nav labels never say where they go: **Stuff**, **More**, **Click**, **???**.

## Accessibility violations (point-at map)

- **Low contrast** — `.whisper` on the home page: light gray on white, 10px, full viewport width.
- **No / nonsense alt text** — images use no `alt`, or `alt="img1.jpg"` / `alt="asdf"`.
- **Non-semantic HTML** — no `<header>`, `<nav>`, `<main>`, or `<button>`. Divs and spans everywhere. No `h1`; pages jump to `<h4>`.
- **No focus states** — every stylesheet starts with `* { outline: none !important; }` and never restyles `:focus`.
- **Tiny type + endless lines** — `font-size: 10px` and no `max-width` on body copy.
- **Color as the only indicator** — homepage: “click the red one.” Three unlabeled swatches.
- **Autoplay media, no pause** — a canvas-captured `<video autoplay>` with no pause UI (`js/bad.js`). Silent on purpose.
- **Motion with no reduced-motion handling** — flashing banners (`.flash`, `.flash2`, `.blink`, `.shake`). No `@media (prefers-reduced-motion)`.
- **Broken keyboard nav** — custom dropdown (`#dropdown-trigger`) ignores keys; modal (`#popup`) swallows Escape; close target is a 7×7px unlabeled div.
- **Unlabeled inputs** — homepage popup, homepage “formy,” and `contact.html` use placeholders only.

## Structural / UX flaws

- Confusing navigation, different on every page (top, side, bottom-right).
- Hero (“i do design”) is buried under a mom’s-coworker paragraph, clutter boxes, and a newsletter modal.
- Case studies skip the problem, ship a mismatched solution, wander into lunch, show no UI, and conclude “it went well.”
  - `stuff.html` — Northshore Bank “solved” with a prix-fixe menu
  - `click.html` — healthcare onboarding shipped as skateboard stickers
  - `things.html` — parking meters turned into a dating app because of pad thai
- Contact is hidden: About → “go here” → `keep-going.html` → `almost.html` → `contact.html`.
- Each page is a different palette, type stack, and spacing system.

## Visual / ugly styling

- Clashing palettes (neon green + orange, maroon + lime, etc.).
- Three or more typefaces per page, Comic Sans included.
- Overlap (`.overlap`, `.overlap2`), random margins, no whitespace.
- Stretched (`.stretch`) and squished (`.squish`) images of a sandwich, a cat, and a building — never the product UI.

## Talk tip

Search the repo for `BAD:` to jump from slide to source.

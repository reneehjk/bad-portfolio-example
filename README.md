# bad-portfolio-example

A product-design portfolio built to demonstrate **mistakes people actually ship** — not a parody. It should look like a real site someone published, while still giving a presentation clear things to point at.

Every intentional issue is labeled in the source (`<!-- BAD: ... -->` / `data-mistake="..."`). During a talk, click **Show mistakes** (bottom-right) and hover highlighted regions — tooltips are prefixed **A11Y**, **UX**, or **Visual**. The toggle stays on as you move between pages. Click **Hide mistakes** to see the site as a visitor would.

Open `index.html` in a browser, or run `python3 -m http.server` from this folder.

## Pages

| File | What it is |
| --- | --- |
| `index.html` | Home — hero, selected work, autoplaying carousel |
| `northshore.html` | Case study: consumer banking |
| `carepath.html` | Case study: healthcare intake |
| `parkwell.html` | Case study: civic parking payments |
| `about.html` | About |
| `info.html` | Contact form (labeled “Info” in the nav) |

Nav: **Work · About · Info**. Visual language is navy / white / terracotta, one system font. Spacing, heading sizes, and image layout drift page to page.

## Talking points

**Accessibility (subtle, common)**

- **Borderline contrast** — `.muted` / `--muted: #8a8a8a` on white (~3.5:1). Hero is white text on a light, busy image with no overlay.
- **Lazy alt text** — `alt="image"`, `alt="portfolio piece"`, or the filename (`portrait.svg`).
- **Mostly semantic HTML, with slips** — real `<header>`, `<nav>`, `<footer>`, headings. Skipped levels (`h1` → `h3` on home and about). A couple of `<div onclick>` fake buttons (home “More about me”, Info “Send”).
- **Broken tab order, not a trap** — work filter dropdown keeps closed options in the tab order; the available-for-work modal does not move focus and its close control is not a button.
- **14px body** — readable, below the usual 16px recommendation. Default focus outlines are left intact.
- **Placeholder-only fields** on `info.html`.
- **Carousel autoplays** with no pause control (`js/site.js`).

**Structural / UX**

- Generic nav: “Work” is an in-page jump, “Info” is contact.
- Case studies are a wall of text, a tool list instead of rationale, unsourced “increased engagement,” and 1–2 screenshots with no captions.
- Email is in the footer on Home, About, and CarePath — missing on Northshore, Parkwell, and Info.

**Visual**

- Safe palette applied a little inconsistently (accent on Info nav and the Send control; navy buttons on Home).
- One typeface; heading sizes jump (22 / 24 / 26 / 28 / 32px) with no scale.
- Work grid and case-study image pairs don’t quite line up. Some sections are cramped, others over-padded.

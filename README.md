# bad-portfolio-example

A product-design portfolio built to demonstrate **mistakes people actually ship**, plus a corrected version of the same pages.

Use the floating **Bad / Annotated / Fixed** control (bottom-right). The choice persists across pages (`localStorage` and `?view=`).

| View | What you see |
| --- | --- |
| **Bad** | The flawed site, as a visitor would |
| **Annotated** | Same site, with dashed outlines. Hover a region for an **A11Y** / **UX** / **Visual** tooltip |
| **Fixed** | Every flagged mistake corrected — contrast, semantics, type scale, case-study structure, consistent nav and contact |

Open `index.html` in a browser, or run `python3 -m http.server` from this folder.

## Pages

| File | What it is |
| --- | --- |
| `index.html` | Home — hero, selected work, carousel |
| `northshore.html` | Case study: consumer banking |
| `carepath.html` | Case study: healthcare intake |
| `parkwell.html` | Case study: civic parking payments |
| `about.html` | About |
| `info.html` | Contact (labeled “Info” in the bad nav) |

## How Fixed is built

- `html[data-view="bad|annotated|fixed"]` is set in `<head>` to avoid a flash
- `css/fixed.css` overrides type, space, contrast, and alignment
- `.view-bad` / `.view-fixed` markup is paired in the DOM where the structure itself had to change (real buttons, labels, headings, captions, footers)
- `js/annotate.js` is the 3-way switch; `js/site.js` changes carousel/modal behavior when the view is Fixed

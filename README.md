# Tadawa website · tadawa.com

The public website of **Tadawa Healthcare L.L.C.** (تداوىٰ للرعاية الصحية), Jordan's telemedicine and primary-care company.
Bilingual (English / Arabic with full RTL), built on the Tadawa Design System, with no framework or build dependency beyond Python 3.

## Pages

| File | Audience | What it holds |
| --- | --- | --- |
| `index.html` | Everyone | Hero, audience switch, numbers, care model, services, how it works, business teaser, locations, partners, doctors, social, download |
| `patients.html` | Patients & families | Treat Me Now, remote / clinic / home visits, family medicine, care plan, My Health, accepted insurance, locations, FAQ |
| `business.html` | Insurers, TPAs, employers, providers, projects | Problem, four levers, measured evidence (MedNet pilot, cost per visit, ER avoidance), employer plan, provider tools, Care Van, BD contact form |
| `tafileh.html` | Tafileh patients | Hours, staff, visiting specialties, services, insurance, how to book, map, center guide PDF |
| `app.html` | App users | Download, home-screen tour, step-by-step guide with tabs, tutorial video library |
| `about.html` | Everyone | Story, vision & mission, thesis, platform, locations & expansion timeline, community, investors |
| `team.html` | Employees & candidates | Shifts and roles, open positions, why join, team tools (Zoho, Asana, Drive), handbooks, IT support, onboarding |
| `contact.html` | Everyone | Three locations, business development, general contact form (WhatsApp or email) |
| `privacy.html` | Everyone | Plain-language privacy policy (needs legal review) |
| `404.html` | | Not-found page |

## How it is built

```
src/partials/head.html      <head>, SEO, hreflang, schema.org, fonts, CSS
src/partials/header.html    sticky nav, language switch, mobile menu
src/partials/footer.html    footer, WhatsApp float, pulse-line + icon sprite, site.js
src/pages/*.html            one source file per page, with a small front-matter block
tools/build.py              assembles src/ into the root *.html files
assets/css/tadawa.css       design tokens + components + animations (light-only identity)
assets/js/site.js           language switch, nav, reveal/counter animations, tabs, forms
assets/js/lang-init.js      picks the language before first paint (?lang=, saved choice, browser)
assets/img/                 logos (SVG from the design system vectors), photos, partner logos, social tiles
assets/fonts/               Madani Arabic (Regular, Bold); Readex Pro and Alexandria load from Google Fonts
```

Edit a page under `src/pages/`, then rebuild:

```bash
python3 tools/build.py
```

CI can check that the committed output is current with `python3 tools/build.py --check`.

## Bilingual content

Every piece of copy exists twice in the markup, side by side:

```html
<h2><span class="en">Three ways in.</span><span class="ar">ثلاث طرق للوصول</span></h2>
```

`html[lang]` decides which one shows (CSS), and `dir` flips the layout. The switch in the header persists the choice in `localStorage`; `?lang=ar` or `?lang=en` forces a language and is kept on internal links so shared URLs open in the right language. Placeholders and aria labels use `data-ph-en/ar` and `data-aria-en/ar`.

Brand spelling rule from the design system: typed Arabic always uses **تداوىٰ** (with the superscript alef).

## Deploying

The output is a plain static site. Push the root to any static host (GitHub Pages, Netlify, Cloudflare Pages, S3) and point `tadawa.com` at it. Keep `404.html` as the not-found page. Update `sitemap.xml` and the canonical URLs in `src/partials/head.html` if the domain changes.

Forms do not post anywhere: they open the visitor's email or WhatsApp app with the message prefilled, so nothing is stored and no backend is needed. Replace them with a form service if lead capture is wanted later.

## Sources of truth used for the content

Tadawa Design System (Claude artifact), Tadawa Introduction 2026 and Insurer Impact Review decks, Tadawa App Guide 2026 (EN/AR), Tafileh center guide v13, the bilingual brochure, the investor deck, the insurer logo sheet, and the Instagram library. Numbers on the site are the ones published in those decks as of November 2026.

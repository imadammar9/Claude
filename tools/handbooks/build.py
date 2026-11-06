"""Assemble the Tadawa handbooks as single-file HTML in the Secretary Handbook V3 style.

Usage: python3 -I build.py <content.py> <out.html>
The content module defines META (dict), QUICK (list of (title, text)), CHAPTERS (list of dicts).
"""
import html, re, sys, runpy, pathlib

HERE = pathlib.Path(__file__).parent
STYLE = (HERE / "style.css").read_text()
LOGO = (HERE / "logo.uri").read_text().strip()
APPLE = (HERE / "apple.svg").read_text()
PLAY = (HERE / "play.svg").read_text()

# Light additions to the V3 stylesheet: a rose group for safety chapters, two-up app grid,
# link chips, tel links, step numbers in ordered workflows.
EXTRA = """
    .chapter[data-group="rose"] { --accent: #a64040; --wash: #fff4f3; }
    .app-grid.two { grid-template-columns: repeat(2, minmax(0, 1fr)); }
    .link-chips { display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0 6px; padding: 0 !important; list-style: none; }
    .link-chips li { margin: 0; padding: 0; }
    .link-chips a { display: inline-flex; align-items: center; gap: 6px; padding: 7px 11px; color: #245560; background: white; border: 1px solid #cce4e8; border-radius: 999px; font-size: 12px; font-weight: 700; text-decoration: none; }
    .link-chips a:hover { border-color: var(--accent); color: var(--accent); }
    .link-chips a::after { content: "↗"; font-size: 11px; opacity: .7; }
    a.approval-number { text-decoration: none; }
    a.approval-number:hover { background: #d9eef1; }
    .reference-row .row-note { flex-basis: 100%; color: var(--muted); font-size: 11px; }
    .reference-row .nums { display: flex; flex-wrap: wrap; gap: 6px; }
    .golden-rule { display: flex; flex-wrap: wrap; gap: 6px; margin: 12px 0 18px; padding: 0 !important; list-style: none; counter-reset: gr; }
    .golden-rule li { counter-increment: gr; margin: 0; padding: 8px 12px; color: white; background: var(--accent); border-radius: 10px; font-size: 12px; font-weight: 800; letter-spacing: .04em; }
    .golden-rule li::before { content: counter(gr) " · "; opacity: .7; }
    .workflow-content ol > li::marker { font-variant-numeric: tabular-nums; }
    .chapter .sub-label { margin: 18px 0 6px; color: var(--ink); font-size: 14px; font-weight: 800; }
    .template-box { margin: 10px 0; padding: 12px 14px; background: #f7fafb; border: 1px dashed #c9d8dc; border-radius: 10px; font-size: 13px; color: #35464e; }
    .search-icon { top: 12px !important; line-height: 0; }
    @media (max-width: 620px) { .app-grid.two { grid-template-columns: 1fr; } }
"""

RTL_MARK = "/* RTL / Arabic adjustments */"


def css_for(lang):
    if lang == "ar":
        return STYLE + EXTRA
    base = STYLE.split(RTL_MARK)[0]
    return base + EXTRA


def store_card(name, ios, android, ios_small="Download on the", and_small="GET IT ON"):
    return f"""<section class="app-card">
            <h3>{name}</h3>
            <div class="store-links">
              <a class="store-btn" href="{ios}" target="_blank" rel="noopener noreferrer">{APPLE}<span><small>{ios_small}</small><strong>App Store</strong></span></a>
              <a class="store-btn" href="{android}" target="_blank" rel="noopener noreferrer">{PLAY}<span><small>{and_small}</small><strong>Google Play</strong></span></a>
            </div>
          </section>"""


SCRIPT = """<script>
    (() => {
      const logo = document.querySelector(".brand-logo");
      const hero = document.querySelector(".hero-inner");
      if (!logo || !hero) return;
      const heroLogo = logo.cloneNode();
      heroLogo.className = "hero-logo";
      heroLogo.alt = "Tadawa";
      hero.prepend(heroLogo);
      const footer = document.querySelector(".footer");
      if (footer) {
        const footerLogo = logo.cloneNode();
        footerLogo.className = "footer-logo";
        footerLogo.alt = "Tadawa";
        footer.prepend(footerLogo);
      }
    })();

    (() => {
      const chapters = Array.from(document.querySelectorAll(".chapter"));
      const links = Array.from(document.querySelectorAll(".toc a"));
      const search = document.getElementById("chapterSearch");
      const count = document.getElementById("searchCount");
      const empty = document.getElementById("searchEmpty");
      const one = document.documentElement.dataset.one;
      const many = document.documentElement.dataset.many;
      // Arabic-aware normalisation: drop diacritics/tatweel, unify alef and yaa forms.
      const normalize = (value) => value.normalize("NFKC").toLowerCase()
        .replace(/[\\u064B-\\u065F\\u0670\\u0640]/g, "")
        .replace(/[\\u0622\\u0623\\u0625]/g, "\\u0627")
        .replace(/\\u0649/g, "\\u064A")
        .replace(/\\u0629/g, "\\u0647")
        .trim();

      const filterChapters = () => {
        const query = normalize(search.value);
        let visible = 0;
        chapters.forEach((chapter) => {
          const matches = !query || normalize(chapter.textContent).includes(query);
          chapter.hidden = !matches;
          if (matches && query) chapter.querySelectorAll("details.workflow").forEach((d) => {
            if (normalize(d.textContent).includes(query)) d.open = true;
          });
          const link = document.querySelector(`.toc a[href="#${chapter.id}"]`);
          if (link) link.hidden = !matches;
          if (matches) visible += 1;
        });
        count.textContent = `${visible} ${visible === 1 ? one : many}`;
        empty.style.display = visible ? "none" : "block";
      };
      search.addEventListener("input", filterChapters);

      const updateProgress = () => {
        const scrollable = document.documentElement.scrollHeight - window.innerHeight;
        const percent = scrollable > 0 ? Math.min(100, Math.round((window.scrollY / scrollable) * 100)) : 0;
        document.getElementById("progressBar").style.width = `${percent}%`;
        document.getElementById("progressPercent").textContent = `${percent}%`;
      };
      window.addEventListener("scroll", updateProgress, { passive: true });
      window.addEventListener("resize", updateProgress);
      updateProgress();

      window.addEventListener("beforeprint", () => document.querySelectorAll("details.workflow").forEach((d) => d.open = true));

      if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver((entries) => {
          entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            links.forEach((link) => link.removeAttribute("aria-current"));
            const active = document.querySelector(`.toc a[href="#${entry.target.id}"]`);
            if (active && !active.hidden) active.setAttribute("aria-current", "location");
          });
        }, { rootMargin: "-18% 0px -72% 0px" });
        chapters.forEach((chapter) => observer.observe(chapter));
      }
    })();
  </script>"""


def build(content_path, out_path):
    c = runpy.run_path(content_path, init_globals={"store_card": store_card})
    M, Q, CH = c["META"], c["QUICK"], c["CHAPTERS"]
    lang = M["lang"]
    dirn = "rtl" if lang == "ar" else "ltr"
    toc = "\n".join(
        f'        <a href="#{ch["id"]}"><span>{i:02d}</span>{ch["toc"]}</a>' for i, ch in enumerate(CH, 1)
    )
    quick = "\n".join(
        f'        <article class="quick-rule">\n          <strong>{t}</strong>\n          <p>{p}</p>\n        </article>'
        for t, p in Q
    )
    chapters = "\n\n".join(
        f'''      <article class="chapter" id="{ch["id"]}" data-number="{i:02d}" data-group="{ch["group"]}">
        <p class="chapter-kicker">{i:02d} · {ch["kicker"]}</p>
        <h2>{ch["title"]}</h2>
{ch["body"].strip()}
      </article>'''
        for i, ch in enumerate(CH, 1)
    )
    tags = "\n".join(f'        <span class="hero-tag">{t}</span>' for t in M["tags"])
    note = M.get("note", "")
    favicon = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23fff'/%3E"
               "%3Cpath d='M5 38H17L27 7L40 55L46 38H59' fill='none' stroke='%230a819d' stroke-width='6' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E")
    doc = f"""<!doctype html>
<html lang="{lang}" dir="{dirn}" data-one="{M['one']}" data-many="{M['many']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0E8098">
  <meta name="robots" content="noindex, nofollow">
  <meta name="description" content="{html.escape(M['lede'])}">
  <link rel="icon" type="image/svg+xml" href="{favicon}">
  <title>{M['title_tag']}</title>
  <style>{css_for(lang)}  </style>
</head>
<body>
  <header class="topbar">
    <a class="brand" href="#top" aria-label="{M['home_aria']}">
      <img class="brand-logo" alt="Tadawa تداوىٰ" src="{LOGO}">
    </a>
    <div class="reading-progress" aria-label="{M['progress']}">
      <div class="progress-meta"><span>{M['progress']}</span><strong id="progressPercent">0%</strong></div>
      <div class="progress-track"><div class="progress-bar" id="progressBar"></div></div>
    </div>
  </header>

  <section class="hero" id="top">
    <div class="hero-inner">
      <p class="eyebrow">{M['eyebrow']}</p>
      <h1>{M['h1']}</h1>
      <p class="hero-lede">{M['lede']}</p>
      <div class="hero-tags">
{tags}
      </div>
    </div>
  </section>

  <main class="layout">
    <aside class="sidebar" aria-label="{M['toc_aria']}">
      <h2 class="sidebar-heading">{M['search_heading']}</h2>
      <label class="search-wrap">
        <span class="sr-only">{M['search_label']}</span>
        <input id="chapterSearch" type="search" placeholder="{M['search_ph']}" autocomplete="off">
        <span class="search-icon" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"><circle cx="11" cy="11" r="6.5"/><path d="m16 16 4.5 4.5"/></svg></span>
      </label>
      <p class="search-count" id="searchCount" aria-live="polite">{len(CH)} {M['many']}</p>
      <nav class="toc" id="toc">
{toc}
      </nav>
      <p class="search-empty" id="searchEmpty">{M['empty']}</p>
    </aside>

    <div class="content" id="handbookContent">
      <div class="intro">
        <div>
          <h2>{M['intro_h']}</h2>
          <p>{M['intro_p']}</p>
        </div>
      </div>

      <div class="quick-rules" aria-label="{M['quick_aria']}">
{quick}
      </div>
{note}
{chapters}
    </div>
  </main>

  <footer class="footer">
    <strong>{M['footer_h']}</strong>
    <p>{M['footer_p']}</p>
  </footer>

  {SCRIPT}
</body>
</html>
"""
    pathlib.Path(out_path).write_text(doc)
    print(out_path, len(doc), "bytes,", len(CH), "chapters")


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])

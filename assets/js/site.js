/* Tadawa website — site script (no dependencies) */
(function () {
  'use strict';
  var html = document.documentElement;
  var LANG_KEY = 'tadawa.lang';

  /* ---------- Language ---------- */
  function currentLang() { return html.getAttribute('lang') === 'ar' ? 'ar' : 'en'; }
  function applyLang(lang, persist) {
    lang = lang === 'ar' ? 'ar' : 'en';
    html.setAttribute('lang', lang);
    html.setAttribute('dir', lang === 'ar' ? 'rtl' : 'ltr');
    var t = document.querySelector('title');
    if (t) { var v = t.getAttribute('data-' + lang); if (v) t.textContent = v; }
    var d = document.querySelector('meta[name="description"]');
    if (d) { var dv = d.getAttribute('data-' + lang); if (dv) d.setAttribute('content', dv); }
    document.querySelectorAll('[data-ph-en]').forEach(function (el) { el.placeholder = el.getAttribute('data-ph-' + lang) || ''; });
    document.querySelectorAll('[data-aria-en]').forEach(function (el) { el.setAttribute('aria-label', el.getAttribute('data-aria-' + lang) || ''); });
    document.querySelectorAll('.lang-switch button').forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-lang') === lang ? 'true' : 'false'); });
    if (persist) { try { localStorage.setItem(LANG_KEY, lang); } catch (e) {} }
    try { var u = new URL(location.href); if (u.searchParams.get('lang') && u.searchParams.get('lang') !== lang) { u.searchParams.set('lang', lang); history.replaceState(null, '', u.toString()); } } catch (e) {}
  }
  window.tadawaSetLang = function (lang) { applyLang(lang, true); };
  applyLang(currentLang(), false);
  document.addEventListener('click', function (e) {
    var b = e.target.closest('.lang-switch button'); if (!b) return;
    applyLang(b.getAttribute('data-lang'), true);
  });
  // keep ?lang= on internal links so a shared link keeps the language
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href]'); if (!a) return;
    var href = a.getAttribute('href');
    if (!href || /^(https?:|mailto:|tel:|#|javascript:)/i.test(href)) return;
    try { var u = new URL(a.href, location.href); if (u.origin !== location.origin) return;
      if (new URL(location.href).searchParams.get('lang')) { u.searchParams.set('lang', currentLang()); a.href = u.toString(); } } catch (err) {}
  });

  /* ---------- Header ---------- */
  var header = document.querySelector('.site-header');
  function onScroll() { if (header) header.classList.toggle('is-scrolled', window.scrollY > 8); }
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  var menuBtn = document.querySelector('.menu-btn'), mobileNav = document.querySelector('.mobile-nav');
  if (menuBtn && mobileNav) {
    menuBtn.addEventListener('click', function () {
      var open = mobileNav.classList.toggle('is-open');
      document.body.classList.toggle('menu-open', open);
      menuBtn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    mobileNav.addEventListener('click', function (e) { if (e.target.closest('a')) { mobileNav.classList.remove('is-open'); document.body.classList.remove('menu-open'); } });
  }
  // current page marker
  var path = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a, .mobile-nav a').forEach(function (a) {
    var h = (a.getAttribute('href') || '').split('?')[0].split('#')[0];
    if (h === path || (path === '' && h === 'index.html')) a.setAttribute('aria-current', 'page');
  });

  /* ---------- Reveal on scroll ---------- */
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var io = ('IntersectionObserver' in window) ? new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (!en.isIntersecting) return;
      var el = en.target; el.classList.add('is-in'); io.unobserve(el);
      if (el.matches('[data-count]')) count(el);
      if (el.classList.contains('bar')) {/* css handles */}
    });
  }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 }) : null;
  // auto-stagger siblings inside .grid / .steps / .audience / .ways
  document.querySelectorAll('.grid, .steps, .audience, .ways, .social-grid, .logo-wall, .hours, .bars, .timeline').forEach(function (g) {
    Array.prototype.forEach.call(g.children, function (c, i) { if (!c.classList.contains('reveal')) { c.classList.add('reveal'); } c.style.setProperty('--d', Math.min(i, 8) * 70 + 'ms'); });
  });
  document.querySelectorAll('.reveal, [data-count], .bar').forEach(function (el) {
    if (!io || reduce) { el.classList.add('is-in'); if (el.matches('[data-count]')) count(el, true); return; }
    io.observe(el);
  });

  /* ---------- Counters ---------- */
  function count(el, instant) {
    var target = parseFloat(el.getAttribute('data-count')), dec = parseInt(el.getAttribute('data-decimals') || '0', 10);
    var prefix = el.getAttribute('data-prefix') || '', suffix = el.getAttribute('data-suffix') || '';
    var fmt = function (n) { return prefix + n.toLocaleString(currentLang() === 'ar' ? 'en-US' : 'en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suffix; };
    if (instant || el.dataset.done) { el.textContent = fmt(target); return; }
    el.dataset.done = '1';
    var start = null, dur = 1400;
    function tick(ts) { if (!start) start = ts; var p = Math.min(1, (ts - start) / dur); var e = 1 - Math.pow(1 - p, 3); el.textContent = fmt(target * e); if (p < 1) requestAnimationFrame(tick); else el.textContent = fmt(target); }
    requestAnimationFrame(tick);
  }

  /* ---------- Tabs ---------- */
  document.querySelectorAll('[data-tabs]').forEach(function (root) {
    var tabs = root.querySelectorAll('[role="tab"]'), panels = root.querySelectorAll('[role="tabpanel"]');
    function select(id) {
      tabs.forEach(function (t) { var on = t.getAttribute('aria-controls') === id; t.setAttribute('aria-selected', on ? 'true' : 'false'); t.tabIndex = on ? 0 : -1; });
      panels.forEach(function (p) { p.hidden = p.id !== id; });
    }
    tabs.forEach(function (t) { t.addEventListener('click', function () { select(t.getAttribute('aria-controls')); }); });
    root.addEventListener('keydown', function (e) {
      if (!e.target.matches('[role="tab"]')) return;
      var arr = Array.prototype.slice.call(tabs), i = arr.indexOf(e.target);
      if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); var dir = e.key === 'ArrowRight' ? 1 : -1; if (currentLang() === 'ar') dir = -dir; var n = arr[(i + dir + arr.length) % arr.length]; n.focus(); select(n.getAttribute('aria-controls')); }
    });
    var h = location.hash.replace('#', '');
    var initial = Array.prototype.find.call(tabs, function (t) { return t.getAttribute('aria-controls') === h; });
    select(initial ? h : tabs[0].getAttribute('aria-controls'));
  });
  window.addEventListener('hashchange', function () {
    var h = location.hash.replace('#', ''); var t = document.querySelector('[role="tab"][aria-controls="' + h + '"]'); if (t) t.click();
  });

  /* ---------- Forms: open WhatsApp or email with the message prefilled ---------- */
  function toast(msg) { var t = document.querySelector('.toast'); if (!t) { t = document.createElement('div'); t.className = 'toast'; document.body.appendChild(t); } t.textContent = msg; t.classList.add('is-show'); clearTimeout(t._h); t._h = setTimeout(function () { t.classList.remove('is-show'); }, 3200); }
  document.querySelectorAll('form[data-contact]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var fd = new FormData(form), lines = [];
      fd.forEach(function (v, k) { if (k === 'channel' || !String(v).trim()) return; var label = form.querySelector('[name="' + k + '"]'); var lab = label && label.id ? form.querySelector('label[for="' + label.id + '"] .' + currentLang()) : null; lines.push((lab ? lab.textContent.trim() : k) + ': ' + v); });
      var subject = form.getAttribute('data-subject') || 'Website enquiry';
      var body = lines.join('\n');
      var channel = fd.get('channel') || form.getAttribute('data-channel') || 'email';
      var to = form.getAttribute('data-to') || 'info@tadawa.com';
      var wa = form.getAttribute('data-wa') || '962793381119';
      if (channel === 'whatsapp') { window.open('https://wa.me/' + wa + '?text=' + encodeURIComponent(subject + '\n' + body), '_blank', 'noopener'); }
      else { location.href = 'mailto:' + to + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body); }
      form.classList.add('is-sent');
      toast(currentLang() === 'ar' ? 'تم تجهيز رسالتك، أكمل الإرسال من تطبيق البريد أو واتساب.' : 'Your message is ready. Finish sending it from your email or WhatsApp app.');
    });
  });

  /* ---------- Copy buttons ---------- */
  document.addEventListener('click', function (e) {
    var b = e.target.closest('[data-copy]'); if (!b) return;
    var text = b.getAttribute('data-copy');
    function done() { toast(currentLang() === 'ar' ? 'تم النسخ' : 'Copied'); }
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, done); else done();
  });

  /* ---------- Phone tilt ---------- */
  var phone = document.querySelector('.phone[data-tilt]');
  if (phone && !reduce && window.matchMedia('(pointer:fine)').matches) {
    var wrap = phone.parentElement;
    wrap.addEventListener('pointermove', function (e) {
      var r = wrap.getBoundingClientRect(); var x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      phone.style.transform = 'rotateY(' + (x * 10) + 'deg) rotateX(' + (-y * 8) + 'deg)'; phone.style.animation = 'none';
    });
    wrap.addEventListener('pointerleave', function () { phone.style.transform = ''; phone.style.animation = ''; });
  }

  /* ---------- Pulse draw: compute path lengths ---------- */
  document.querySelectorAll('.draw path').forEach(function (p) { try { p.style.setProperty('--len', Math.ceil(p.getTotalLength())); } catch (e) {} });

  /* ---------- Footer year ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();

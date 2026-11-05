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
    document.querySelectorAll('option[data-en]').forEach(function (el) { el.textContent = el.getAttribute('data-' + lang) || el.getAttribute('data-en'); });
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
  /* ---------- Mega menu ---------- */
  var items = document.querySelectorAll('.nav-item');
  function closeAll(except) { items.forEach(function (it) { if (it !== except) { it.classList.remove('is-open'); it.querySelector('.nav-btn').setAttribute('aria-expanded', 'false'); } }); }
  items.forEach(function (it) {
    var btn = it.querySelector('.nav-btn'); var t;
    function open() { clearTimeout(t); closeAll(it); it.classList.add('is-open'); btn.setAttribute('aria-expanded', 'true'); }
    function close() { t = setTimeout(function () { it.classList.remove('is-open'); btn.setAttribute('aria-expanded', 'false'); }, 120); }
    it.addEventListener('mouseenter', function () { if (window.matchMedia('(hover:hover)').matches) open(); });
    it.addEventListener('mouseleave', function () { if (window.matchMedia('(hover:hover)').matches) close(); });
    btn.addEventListener('click', function () { if (it.classList.contains('is-open') && window.matchMedia('(hover:hover)').matches) return; if (it.classList.contains('is-open')) { it.classList.remove('is-open'); btn.setAttribute('aria-expanded', 'false'); } else open(); });
    it.addEventListener('focusout', function (e) { if (!it.contains(e.relatedTarget)) { it.classList.remove('is-open'); btn.setAttribute('aria-expanded', 'false'); } });
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeAll(); });
  document.addEventListener('click', function (e) { if (!e.target.closest('.nav-item')) closeAll(); });

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


  /* ---------- Hero stage parallax (v3) ---------- */
  document.querySelectorAll('[data-parallax]').forEach(function (st) {
    if (reduce || !window.matchMedia('(pointer:fine)').matches) return;
    st.addEventListener('pointermove', function (e) {
      var r = st.getBoundingClientRect(); var x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      st.style.setProperty('--mx', (-x).toFixed(3)); st.style.setProperty('--my', (-y).toFixed(3));
    });
    st.addEventListener('pointerleave', function () { st.style.setProperty('--mx', 0); st.style.setProperty('--my', 0); });
  });

  /* ---------- Pulse draw: compute path lengths ---------- */
  document.querySelectorAll('.draw path').forEach(function (p) { try { p.style.setProperty('--len', Math.ceil(p.getTotalLength())); } catch (e) {} });

  /* ---------- Booking bar: route to the right page or the app ---------- */
  var base = document.body.getAttribute('data-base') || '';
  document.querySelectorAll('form[data-booking]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var need = f.querySelector('[name="need"]').value;
      var map = { urgent: 'care/treat-me-now.html', remote: 'care/remote-visit.html', clinic: 'care/clinic-visit.html', home: 'care/home-visit.html', specialist: 'care/specialists.html', chronic: 'care/chronic-care.html' };
      var who = f.querySelector('[name="who"]').value, ins = f.querySelector('[name="ins"]').value;
      var url = base + (map[need] || 'care/index.html') + '?lang=' + currentLang() + '#start';
      try { sessionStorage.setItem('tadawa.booking', JSON.stringify({ need: need, who: who, ins: ins })); } catch (err) {}
      location.href = url;
    });
  });

  /* ---------- Care chooser ---------- */
  var chooser = document.querySelector('[data-chooser]');
  if (chooser) {
    var result = chooser.querySelector('.chooser-result');
    var data = {
      fever: { en: ['Treat Me Now', 'Fever, flu, sore throat, cough, stomach upset and most everyday illness: a family doctor joins you by video within minutes, prescribes and arranges a sick leave if needed.', 'care/treat-me-now.html'], ar: ['عالجني الآن', 'الحمى والإنفلونزا والتهاب الحلق والسعال واضطرابات المعدة ومعظم الأمراض اليومية: ينضم إليك طبيب أسرة بالفيديو خلال دقائق، ويصف العلاج ويصدر إجازة مرضية عند الحاجة.', 'care/treat-me-now.html'] },
      checkup: { en: ['Remote visit', 'Routine check-ups, follow-ups, results review and prescription renewals: book a scheduled video appointment at a time that suits you.', 'care/remote-visit.html'], ar: ['استشارة عن بعد', 'المراجعات الدورية والمتابعات ومراجعة النتائج وتجديد الوصفات: احجز موعد فيديو في الوقت الذي يناسبك.', 'care/remote-visit.html'] },
      exam: { en: ['Clinic visit', 'Something that needs hands-on examination, blood tests, an ECG or a procedure: book your family doctor in Amman, Tafileh or Irbid.', 'care/clinic-visit.html'], ar: ['زيارة العيادة', 'ما يحتاج فحصاً سريرياً أو تحاليل أو تخطيط قلب أو إجراءً: احجز طبيب أسرتك في عمّان أو الطفيلة أو إربد.', 'care/clinic-visit.html'] },
      home: { en: ['Home visit', 'An elderly parent, a bed-bound patient, IV fluids, injections or wound care at home: a doctor comes to you.', 'care/home-visit.html'], ar: ['زيارة منزلية', 'والد مسن أو مريض طريح الفراش أو محاليل وريدية أو حقن أو عناية بالجروح في المنزل: يأتيك الطبيب.', 'care/home-visit.html'] },
      chronic: { en: ['Chronic care plan', 'Diabetes, hypertension, asthma or any long-term condition: regular follow-up with the same doctor and a care plan you track in the app.', 'care/chronic-care.html'], ar: ['خطة رعاية للأمراض المزمنة', 'السكري أو الضغط أو الربو أو أي حالة طويلة الأمد: متابعة منتظمة مع الطبيب نفسه وخطة رعاية تتابعها في التطبيق.', 'care/chronic-care.html'] },
      specialist: { en: ['Specialist referral', 'Eyes, heart, chest, neurology, surgery or rehabilitation: your family doctor refers you to a visiting specialist and books your turn.', 'care/specialists.html'], ar: ['تحويل إلى اختصاصي', 'العيون أو القلب أو الصدرية أو الأعصاب أو الجراحة أو التأهيل: يحوّلك طبيب أسرتك إلى اختصاصي زائر ويحجز دورك.', 'care/specialists.html'] },
      child: { en: ['Treat Me Now, for your child', 'Fever, cough, rash, tummy pain: add your child as a family profile and start a video visit. The doctor tells you if a clinic visit is needed.', 'care/family-medicine.html'], ar: ['عالجني الآن، لطفلك', 'حمى أو سعال أو طفح أو ألم بطن: أضف طفلك كحساب عائلي وابدأ زيارة فيديو. يخبرك الطبيب إن لزمت زيارة العيادة.', 'care/family-medicine.html'] },
      records: { en: ['Care plan & health record', 'Reports, prescriptions, lab results, medicines with reminders and your vitals live in the My Health tab.', 'care/health-record.html'], ar: ['خطة الرعاية والسجل الصحي', 'التقارير والوصفات ونتائج المختبر والأدوية مع التذكير والمؤشرات الحيوية كلها في تبويب «صحتي».', 'care/health-record.html'] }
    };
    chooser.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-need]'); if (!b) return;
      chooser.querySelectorAll('button[data-need]').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      var d = data[b.getAttribute('data-need')]; if (!d) return;
      var l = currentLang(), v = d[l];
      result.querySelector('h3').textContent = v[0]; result.querySelector('p').textContent = v[1];
      result.querySelector('a.btn').href = base + v[2] + '?lang=' + l;
      result.hidden = false;
      result.scrollIntoView({ block: 'nearest', behavior: reduce ? 'auto' : 'smooth' });
    });
  }

  /* ---------- Scroll story ---------- */
  document.querySelectorAll('[data-story]').forEach(function (story) {
    var steps = story.querySelectorAll('.story-step'), shots = story.querySelectorAll('.story-phone .scr img');
    function activate(i) { steps.forEach(function (s, k) { s.classList.toggle('is-active', k === i); }); shots.forEach(function (s, k) { s.classList.toggle('is-active', k === i); }); }
    activate(0);
    if (!('IntersectionObserver' in window)) return;
    var so = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) activate(Array.prototype.indexOf.call(steps, en.target)); });
    }, { rootMargin: '-45% 0px -45% 0px', threshold: 0 });
    steps.forEach(function (s) { so.observe(s); });
  });

  /* ---------- Sub-nav scrollspy ---------- */
  var spyLinks = document.querySelectorAll('.subnav a[href^="#"], .toc a[href^="#"]');
  if (spyLinks.length && 'IntersectionObserver' in window) {
    var targets = Array.prototype.map.call(spyLinks, function (a) { return document.querySelector(a.getAttribute('href')); }).filter(Boolean);
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        spyLinks.forEach(function (a) { a.classList.toggle('is-active', a.getAttribute('href') === '#' + en.target.id); });
      });
    }, { rootMargin: '-30% 0px -60% 0px', threshold: 0 });
    targets.forEach(function (t) { spy.observe(t); });
  }

  /* ---------- Help center search ---------- */
  var hs = document.querySelector('[data-help-search]');
  if (hs) {
    var faq = document.querySelector('.faq[data-searchable]');
    var entries = faq.querySelectorAll('details'), cats = faq.querySelectorAll('.cat');
    function filter(q) {
      q = q.trim().toLowerCase(); var shown = 0;
      entries.forEach(function (d) { var hit = !q || d.textContent.toLowerCase().indexOf(q) > -1; d.classList.toggle('is-hidden', !hit); if (hit) shown++; if (q && hit) d.open = true; });
      cats.forEach(function (c) { var n = c.nextElementSibling, any = false; while (n && !n.classList.contains('cat')) { if (n.tagName === 'DETAILS' && !n.classList.contains('is-hidden')) any = true; n = n.nextElementSibling; } c.classList.toggle('is-hidden', !any); });
      faq.classList.toggle('is-empty', shown === 0);
    }
    hs.addEventListener('input', function () { filter(hs.value); });
    var q0 = new URL(location.href).searchParams.get('q'); if (q0) { hs.value = q0; filter(q0); }
  }

  /* ---------- Footer year ---------- */
  document.querySelectorAll('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();

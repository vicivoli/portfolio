// Menu, hover previews on the index, filters, list/grid toggle, copy email, side tabs, lazy video.
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  // Always open a new page at the top; back/forward is left to the browser so you return to your place
  var navType = 'navigate';
  try { var ne = performance.getEntriesByType('navigation')[0]; if (ne) navType = ne.type; } catch (err) {}
  if (navType !== 'back_forward' && !location.hash) {
    var toTop = function () { window.scrollTo(0, 0); };
    toTop(); requestAnimationFrame(toTop); addEventListener('load', toTop);
  }

  // Fade for browsers without View Transitions
  var hasVT = 'onpagereveal' in window;
  if (!hasVT && !reduce) {
    document.documentElement.classList.add('no-vt');
    document.addEventListener('click', function (ev) {
      var a = ev.target.closest && ev.target.closest('a[href]');
      if (!a || a.target === '_blank' || ev.defaultPrevented || ev.metaKey || ev.ctrlKey || ev.shiftKey || ev.button !== 0) return;
      var u = new URL(a.href, location.href);
      if (u.origin !== location.origin || u.pathname === location.pathname || /\.pdf$/i.test(u.pathname)) return;
      ev.preventDefault();
      document.documentElement.classList.add('leaving');
      setTimeout(function () { location.href = a.href; }, 220);
    });
    addEventListener('pageshow', function (ev) { if (ev.persisted) document.documentElement.classList.remove('leaving'); });
  }

  // Smooth scroll only for links to a section on the same page
  document.addEventListener('click', function (ev) {
    var a = ev.target.closest && ev.target.closest('a[href*="#"]'); if (!a) return;
    var u = new URL(a.href, location.href);
    if (u.pathname !== location.pathname || !u.hash) return;
    var t = document.getElementById(u.hash.slice(1)); if (!t) return;
    ev.preventDefault();
    t.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
    history.replaceState(null, '', u.hash);
  });

  // Fit the big name to its column exactly
  var fitEls = $$('[data-fit]');
  var fit = function () {
    fitEls.forEach(function (el) {
      el.style.fontSize = '100px';
      var w = el.parentElement.clientWidth, sw = el.getBoundingClientRect().width;
      if (sw) el.style.fontSize = (100 * w / sw * 0.995) + 'px';
    });
  };
  if (fitEls.length) { fit(); addEventListener('resize', fit); if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit); }

  // Local time in Yakutsk
  var ykt = $('[data-ykt]');
  if (ykt) {
    var yf = new Intl.DateTimeFormat('en-US', { timeZone: 'Asia/Yakutsk', hour: 'numeric', minute: '2-digit' });
    var yt = function () { ykt.textContent = yf.format(new Date()); };
    yt(); setInterval(yt, 30000);
  }

  // Snow falls over the Yakutsk selfie on hover
  $$('[data-snow]').forEach(function (fig) {
    var cv = $('canvas', fig); if (!cv || reduce) return;
    var ctx = cv.getContext('2d'), flakes = [], on = false, raf = null, dpr = Math.min(2, window.devicePixelRatio || 1);
    var size = function () { var r = cv.getBoundingClientRect(); cv.width = r.width * dpr; cv.height = r.height * dpr; };
    var add = function () {
      var big = Math.random() < 0.22;
      flakes.push({ x: Math.random() * cv.width, y: -20 * dpr, r: (big ? 9 + Math.random() * 6 : 1.2 + Math.random() * 2.2) * dpr,
        vy: (big ? 0.6 : 0.8 + Math.random() * 1.2) * dpr, vx: (Math.random() - 0.5) * 0.4 * dpr, a: Math.random() * 6.28, big: big, rot: Math.random() * 6.28 });
    };
    var tick = function () {
      ctx.clearRect(0, 0, cv.width, cv.height);
      if (on && flakes.length < 140) { add(); if (Math.random() < 0.6) add(); }
      flakes = flakes.filter(function (f) { return f.y < cv.height + 30 * dpr; });
      flakes.forEach(function (f) {
        f.a += 0.02; f.x += f.vx + Math.sin(f.a) * 0.35 * dpr; f.y += f.vy; f.rot += 0.01;
        if (f.big) {
          ctx.save(); ctx.translate(f.x, f.y); ctx.rotate(f.rot); ctx.globalAlpha = 0.9;
          ctx.font = (f.r * 2) + 'px serif'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle'; ctx.fillStyle = '#fff';
          ctx.fillText('❄', 0, 0); ctx.restore();
        } else {
          ctx.globalAlpha = 0.85; ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.arc(f.x, f.y, f.r, 0, 6.28); ctx.fill();
        }
      });
      ctx.globalAlpha = 1;
      raf = (on || flakes.length) ? requestAnimationFrame(tick) : null;
    };
    fig.addEventListener('mouseenter', function () { size(); on = true; if (!raf) raf = requestAnimationFrame(tick); });
    fig.addEventListener('mouseleave', function () { on = false; });
    fig.addEventListener('touchstart', function () { size(); on = true; if (!raf) raf = requestAnimationFrame(tick); setTimeout(function () { on = false; }, 2500); }, { passive: true });
  });

  // Rolling numbers: each digit spins up to its value when the Impact list scrolls into view
  var rolls = $$('[data-roll]');
  if (rolls.length && !reduce && 'IntersectionObserver' in window) {
    rolls.forEach(function (el) {
      var txt = el.getAttribute('data-roll'), html = '', di = 0;
      for (var i = 0; i < txt.length; i++) {
        var ch = txt[i];
        if (/[0-9]/.test(ch)) {
          var stack = '';
          for (var n = 0; n <= 9; n++) stack += '<span>' + n + '</span>';
          html += '<span class="roll-d"><span class="roll-s" data-to="' + ch + '" style="transition-delay:' + (di * 90) + 'ms">' + stack + '</span></span>';
          di++;
        } else html += '<span class="roll-c">' + ch + '</span>';
      }
      el.setAttribute('aria-label', txt);
      el.innerHTML = html;
    });
    var rio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        $$('.roll-s', en.target).forEach(function (s) { s.style.transform = 'translateY(-' + s.getAttribute('data-to') + 'em)'; });
        rio.unobserve(en.target);
      });
    }, { threshold: 0.6 });
    rolls.forEach(function (el) { rio.observe(el); });
  }

  // Menu overlay
  var btn = $('.menu-btn'), menu = $('#menu');
  if (btn && menu) {
    btn.addEventListener('click', function () {
      var open = menu.hidden;
      menu.hidden = !open;
      btn.setAttribute('aria-expanded', String(open));
      btn.textContent = open ? 'Close' : 'Menu';
      document.body.style.overflow = open ? 'hidden' : '';
    });
    document.addEventListener('keydown', function (ev) { if (ev.key === 'Escape' && !menu.hidden) btn.click(); });
  }

  // Floating preview that follows the cursor over index rows
  var pv = $('.preview');
  var fine = window.matchMedia && matchMedia('(hover: hover) and (pointer: fine)').matches;
  if (pv && fine) {
    var x = 0, y = 0, cx = 0, cy = 0, raf = null, current = '';
    var loop = function () {
      cx += (x - cx) * (reduce ? 1 : 0.18); cy += (y - cy) * (reduce ? 1 : 0.18);
      pv.style.left = cx + 'px'; pv.style.top = cy + 'px';
      raf = Math.abs(x - cx) + Math.abs(y - cy) > 0.5 ? requestAnimationFrame(loop) : null;
    };
    document.addEventListener('mousemove', function (ev) {
      x = ev.clientX + 24 + pv.offsetWidth / 2; y = ev.clientY;
      if (x + pv.offsetWidth / 2 > innerWidth - 16) x = ev.clientX - 24 - pv.offsetWidth / 2;
      if (!raf) raf = requestAnimationFrame(loop);
    });
    $$('.r').forEach(function (r) {
      r.addEventListener('mouseenter', function () {
        var src = r.getAttribute('data-preview');
        if (src !== current) {
          current = src;
          pv.innerHTML = r.getAttribute('data-kind') === 'vid'
            ? '<video src="' + src + '" poster="' + r.getAttribute('data-still') + '" muted loop playsinline autoplay style="object-position:' + r.getAttribute('data-focus') + '"></video>'
            : '<img src="' + src + '" alt="">';
          var v = pv.querySelector('video'); if (v) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
        }
        pv.classList.add('on');
      });
      r.addEventListener('mouseleave', function () { pv.classList.remove('on'); });
    });
  }

  // Filters (rows and cards)
  var fbtns = $$('[data-filter]');
  fbtns.forEach(function (b) {
    b.addEventListener('click', function () {
      var f = b.getAttribute('data-filter');
      fbtns.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      $$('.r[data-cats], .card[data-cats]').forEach(function (el) {
        el.hidden = !(f === 'all' || el.getAttribute('data-cats').split(' ').indexOf(f) > -1);
      });
    });
  });

  // List / grid
  var vbtns = $$('[data-view]'), list = $('[data-list]'), grid = $('[data-grid]');
  vbtns.forEach(function (b) {
    b.addEventListener('click', function () {
      var v = b.getAttribute('data-view');
      vbtns.forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });
      if (list) list.hidden = v !== 'list';
      if (grid) { grid.hidden = v !== 'grid'; if (v === 'grid') observeAll(); }
    });
  });

  // Copy email
  $$('[data-copy]').forEach(function (b) {
    b.addEventListener('click', function () {
      var t = b.getAttribute('data-copy'), hint = $('.copy-hint', b);
      var ok = function () { b.classList.add('done'); if (hint) hint.textContent = 'Copied ❄'; setTimeout(function () { b.classList.remove('done'); if (hint) hint.textContent = 'Copy'; }, 1800); };
      var fallback = function () { var r = document.createRange(); r.selectNodeContents(b.firstElementChild); var s = getSelection(); s.removeAllRanges(); s.addRange(r); if (hint) hint.textContent = 'Press ⌘C'; };
      if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t).then(ok, fallback); else fallback();
    });
  });

  // Side tabs on case pages
  var tabs = $$('.toc a');
  if (tabs.length) {
    var secs = tabs.map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); }).filter(Boolean);
    var spy = function () {
      var line = innerHeight * 0.35, cur = secs[0];
      secs.forEach(function (s) { if (s.getBoundingClientRect().top <= line) cur = s; });
      if (innerHeight + scrollY >= document.documentElement.scrollHeight - 4) cur = secs[secs.length - 1];
      tabs.forEach(function (a) { a.classList.toggle('on', a.getAttribute('href') === '#' + cur.id); });
    };
    addEventListener('scroll', spy, { passive: true }); addEventListener('resize', spy); spy();
  }

  // Lazy videos: load near the screen, play while visible
  var io = 'IntersectionObserver' in window ? new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      var v = en.target;
      if (en.isIntersecting) {
        if (!v.getAttribute('src')) v.src = v.getAttribute('data-src');
        if (!reduce && !v.dataset.touched) { var p = v.play(); if (p && p.catch) p.catch(function () {}); }
      } else if (!v.paused) v.pause();
    });
  }, { rootMargin: '200px 0px', threshold: 0.15 }) : null;
  function observeAll() {
    $$('video[data-src]').forEach(function (v) {
      if (v.dataset.obs) return; v.dataset.obs = '1';
      if (io) io.observe(v); else v.src = v.getAttribute('data-src');
      v.addEventListener('pause', function () { if (document.activeElement === v) v.dataset.touched = '1'; });
    });
  }
  observeAll();
})();

// Menu, hover previews on the index, filters, list/grid toggle, copy email, side tabs, lazy video.
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

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
      var ok = function () { b.classList.add('done'); if (hint) hint.textContent = 'Copied'; setTimeout(function () { b.classList.remove('done'); if (hint) hint.textContent = 'Copy'; }, 1800); };
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

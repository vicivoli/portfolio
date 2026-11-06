#!/usr/bin/env python3
"""Builds the static portfolio from data.py.   Usage:  python3 build.py
Outputs index.html, works.html, contact.html, works/<slug>.html and works/snackpass/index.html."""
import html, json, os, re
from data import SITE, CATEGORIES, PROJECTS

ROOT = os.path.dirname(os.path.abspath(__file__))
BY = {p["slug"]: p for p in PROJECTS}
try:
    DIMS = json.load(open(os.path.join(ROOT, "media", "dims.json")))
except Exception:
    DIMS = {}
YEAR = 2026
try:
    WEBMAP = json.load(open(os.path.join(ROOT, "media", "webmap.json")))
except Exception:
    WEBMAP = {}


def W(name):
    """Lighter JPEG version of a heavy PNG, if one exists."""
    return WEBMAP.get(name, name)
e = html.escape


def slugify(c):
    return c.lower().replace(" & ", "-").replace(" ", "-")


def ratio(name):
    d = DIMS.get(name)
    return (d[0], d[1]) if d else (16, 9)


def url_for(p, pre):
    return pre + p["external"] if p.get("external") else f"{pre}works/{p['slug']}.html"


def still(p, pre):
    """A still image for a project (poster for videos)."""
    k, n = p["thumb"]
    return f"{pre}media/poster/{n.rsplit('.', 1)[0]}.jpg" if k == "vid" else f"{pre}media/{W(n)}"


def brand_attr(name):
    c = SITE.get("press_colors", {}).get(name, "")
    if c == "nbc":
        return ' class="pc nbc"'
    return f' class="pc" style="--c:{c}"' if c else ""


def brand_li(name):
    link = SITE.get("press_links", {}).get(name)
    if not link:
        return f"<li{brand_attr(name)}>{e(name)}</li>"
    ext = link.startswith("http")
    tgt = ' target="_blank" rel="noopener"' if ext else ""
    return f'<li{brand_attr(name)}><a href="{link}"{tgt}>{e(name)}<span class="arr">{"↗" if ext else "→"}</span></a></li>'


def media_el(kind, name, pre, mode, label="", focus=""):
    w, h = ratio(name)
    st = f' style="object-position:{focus}"' if focus else ""
    if kind == "loop":
        kind, mode = "vid", "loop"
    if kind == "vid":
        src = f"{pre}media/{'thumb/' if mode == 'thumb' else ''}{name}"
        poster = f"{pre}media/poster/{name.rsplit('.', 1)[0]}.jpg"
        extra = "" if mode in ("thumb", "loop") else " controls"
        return (f'<video data-src="{src}" poster="{poster}" muted loop playsinline preload="none"{extra} '
                f'width="{w}" height="{h}" aria-label="{e(label)}"{st}></video>')
    return f'<img src="{pre}media/{W(name)}" width="{w}" height="{h}" loading="lazy" decoding="async" alt="{e(label)}"{st}>'


def cats_of(p):
    return " ".join(sorted({slugify(c) for c in [p.get("type", "")] + p.get("cats", []) if c}))


# ---------- shared chrome ----------

def head(title, pre, desc=""):
    desc = desc or f"{SITE['name']} — {SITE['role']}. Content, film, brand and product design."
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:image" content="https://nikolaipetukhov.com/media/og.jpg">
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="icon" href="{pre}media/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="{pre}media/favicon-512.png" sizes="512x512" type="image/png">
<link rel="apple-touch-icon" href="{pre}media/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{pre}assets/style.css">
</head>
<body>
"""


def header(pre, active=""):
    home = pre or "./"
    items = [("Work", f"{pre}works.html"), ("About", f"{home}#about"), ("Contact", f"{pre}contact.html")]
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if n == active else ""}>{n}</a>' for n, h in items)
    nav += f'<a href="{home}#resume">Resume</a>'
    return f"""<header class="topbar">
  <a class="brand" href="{home}">{e(SITE['name'])}</a>
  <nav class="inline-nav" aria-label="Main">{nav}</nav>
  <button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
</header>
<div class="menu" id="menu" hidden><nav aria-label="Menu">{nav}</nav></div>
"""


def touch_block(pre=""):
    return f"""<section class="touch">
  <p class="label">Contact</p>
  <h2>Let’s make<br>something.</h2>
  <div class="touch-row">
    <button class="copy" type="button" data-copy="{SITE['email']}"><span>{e(SITE['email'])}</span><span class="copy-hint">Copy</span></button>
    <div class="links">
      <a href="{SITE['linkedin']}" target="_blank" rel="noopener">LinkedIn ↗</a>
      <a href="{SITE['instagram']}" target="_blank" rel="noopener">Instagram ↗</a>
      <a href="{pre or './'}#resume">Resume</a>
    </div>
  </div>
</section>
"""


def footer(pre):
    return f"""<footer class="foot"><span>{e(SITE['brand'])} ©{YEAR}</span><a href="#top">Back to top ↑</a></footer>
</main>
<div class="preview" aria-hidden="true"></div>
<script src="{pre}assets/site.js"></script>
</body>
</html>
"""


# ---------- index rows / cards ----------

def row(p, pre, i):
    k, n = p["thumb"]
    prev = f"{pre}media/thumb/{n}" if k == "vid" else f"{pre}media/{W(n)}"
    return f"""<a class="r" style="--accent:{p.get('accent','var(--ink)')}" href="{url_for(p, pre)}" data-cats="{cats_of(p)}" data-preview="{prev}" data-kind="{k}" data-still="{still(p, pre)}" data-focus="{p.get('focus','50% 50%')}">
  <span class="n">{i:02d}</span>
  <span class="t">{e(p['title'])}{LOCK if p.get('confidential') else ''}</span>
  <span class="m"><b>{e(p.get('type',''))}</b><span>{e(p.get('year',''))}</span></span>
  <span class="mini"><img src="{still(p, pre)}" alt="" loading="lazy" style="object-position:{p.get('focus','50% 50%')}"></span>
</a>"""


def card(p, pre):
    k, n = p["thumb"]
    return f"""<a class="card" style="--accent:{p.get('accent','var(--ink)')}" href="{url_for(p, pre)}" data-cats="{cats_of(p)}">
  <div class="thumb">{media_el(k, n, pre, 'thumb', p['title'], p.get('focus',''))}</div>
  <div class="card-meta"><span style="color:var(--ink);text-align:left">{e(p['title'])}{LOCK if p.get('confidential') else ''}</span><span>{e(p.get('type',''))} · {e(p.get('year',''))}</span></div>
</a>"""


def filters(projects):
    counts = {c: sum(1 for p in projects if slugify(c) in cats_of(p).split()) for c in CATEGORIES}
    b = f'<button type="button" aria-pressed="true" data-filter="all">All<sup>{len(projects)}</sup></button>'
    b += "".join(f'<button type="button" aria-pressed="false" data-filter="{slugify(c)}">{e(c)}<sup>{counts[c]}</sup></button>' for c in CATEGORIES if counts[c])
    return f'<div class="filters" role="group" aria-label="Filter by type">{b}</div>'


# ---------- pages ----------

def page_home():
    pre = ""
    f = SITE["featured"]
    fp = BY[f["slug"]]
    sel = [BY[s_] for s_ in SITE["selected"]]
    rows = "".join(row(p, pre, i + 1) for i, p in enumerate(sel))
    facts = "".join(f"<span><b>{e(a)}</b> {e(b)}</span>" for a, b in SITE["stats"])
    skills = "".join(f"<li>{e(x)}</li>" for x in SITE["skills"])
    press = "".join(brand_li(x) for x in SITE["press"])
    impact = "".join(f'<li><b data-roll="{e(a)}">{e(a)}</b><span>{e(b)}</span></li>' for a, b in SITE["impact"])
    exp = "".join(f'<div class="xr"><span>{e(r)}</span><span>{e(o)}</span><span>{e(y)}</span></div>' for r, o, y in SITE["experience"])
    resumes = "".join(f'<a class="btn" href="{pre}{u}" target="_blank" rel="noopener">Resume · {e(n)} ↗</a>' for n, u in SITE["resumes"])
    out = head(SITE['name'], pre) + header(pre) + '<main id="top">\n'
    out += f"""<section class="hero-name">
  <h1 data-fit aria-label="{e(SITE['name'])}">{''.join(f'<span aria-hidden="true">{ch}</span>' if ch != ' ' else ' ' for ch in e(SITE['name']))}</h1>
  <div class="hero-sub">
    <p>{SITE['summary']}</p>
    <p class="facts">{facts}</p>
  </div>
</section>
<section class="reel">
  <a class="reel-media" href="{url_for(fp, pre)}">
    <video data-src="{pre}media/{f['video']}" poster="{pre}media/{W(f['poster'])}" muted loop playsinline preload="none" width="16" height="9" aria-label="{e(f['label'])} showreel"></video>
  </a>
  <div class="reel-cap"><span><b>{e(f['label'])}</b> — {e(f['sub'])}</span><span>{e(f['note'].strip('()'))}</span></div>
</section>
<section class="index">
  <div class="index-head"><p class="label">Selected work</p><a class="label" href="works.html" style="color:var(--ink)">All work ({len(PROJECTS)}) →</a></div>
  <div class="rows">{rows}</div>
</section>
<section class="about" id="about">
  <div class="about-text">
    <p class="label">About</p>
    <h2>From the coldest<br>city on Earth.</h2>
    <div class="txt">{''.join(f"<p>{e(x)}</p>" for x in SITE['about_personal'])}</div>
  </div>
  <figure class="live" data-snow>
    <video data-src="{pre}media/{SITE['about_video']}" poster="{pre}media/poster/{SITE['about_video'].rsplit('.',1)[0]}.jpg" muted loop playsinline preload="none" width="720" height="900" aria-label="Nikolai in a frosted hood and face mask, winter in Yakutsk"></video>
    <canvas class="snow" aria-hidden="true"></canvas>
    <figcaption><span>Yakutsk, winter</span><span>Now in Yakutsk <b data-ykt>--:--</b></span></figcaption>
  </figure>
</section>
<section class="about-cols">
  <div><p class="label">What I do</p><ul>{skills}</ul></div>
  <div><p class="label">Featured in</p><ul>{press}</ul></div>
  <div><p class="label">Impact</p><ul class="impact">{impact}</ul></div>
</section>
<section class="exp" id="resume">
  <div class="exp-head"><p class="label">Experience</p></div>
  <div class="exp-rows">{exp}<div class="xr edu"><span>{e(SITE['education'][0])}</span><span>{e(SITE['education'][1])}</span><span>{e(SITE['education'][2])}</span></div></div>
</section>
"""
    out += touch_block(pre) + footer(pre)
    return out


def page_works():
    pre = ""
    rows = "".join(row(p, pre, i + 1) for i, p in enumerate(PROJECTS))
    cards = "".join(card(p, pre) for p in PROJECTS)
    out = head("Work — " + SITE["name"], pre) + header(pre, "Work") + '<main id="top">\n'
    out += f"""<section class="page-head"><h1>Work</h1></section>
<div class="index-head">{filters(PROJECTS)}
  <div class="views" role="group" aria-label="View"><button type="button" aria-pressed="true" data-view="list">List</button><button type="button" aria-pressed="false" data-view="grid">Grid</button></div>
</div>
<div class="rows" data-list>{rows}</div>
<div class="grid" data-grid hidden>{cards}</div>
"""
    out += touch_block(pre) + footer(pre)
    return out


def page_contact():
    pre = ""
    out = head("Contact — " + SITE["name"], pre) + header(pre, "Contact") + '<main id="top">\n'
    out += f"""<section class="contact">
  <div class="contact-text">
    <h1>Contact</h1>
    <p class="txt">{e(SITE['contact_text'])}</p>
    <dl class="contact-list">
      <div><dt>Email</dt><dd><button class="copy" type="button" data-copy="{SITE['email']}"><span>{e(SITE['email'])}</span><span class="copy-hint">Copy</span></button></dd></div>
      <div><dt>Socials</dt><dd><a href="{SITE['linkedin']}" target="_blank" rel="noopener">LinkedIn ↗</a><a href="{SITE['instagram']}" target="_blank" rel="noopener">Instagram ↗</a></dd></div>
      <div><dt>Based in</dt><dd>{e(SITE['location'])}</dd></div>
    </dl>
  </div>
  <figure class="portrait">{media_el('img', SITE['contact_image'], pre, 'full', 'Nikolai Petukhov')}</figure>
</section>
"""
    out += footer(pre)
    return out


def media_row(r, pre, title):
    items = []
    for item in r:
        k, n = item[0], item[1]
        capt = item[2] if len(item) > 2 else ""
        w, h = ratio(n)
        shape = "tall" if h > w * 1.15 else ("square" if h >= w * 0.87 else "wide")
        fc = f"<figcaption>{e(capt)}</figcaption>" if capt else ""
        items.append((shape, f'<figure class="mf {shape}"><div class="box" style="--ar:{w}/{h}">{media_el(k, n, pre, "full", capt or title)}</div>{fc}</figure>'))
    shapes = {s for s, _ in items}
    cls = "row" + (" single " + items[0][0] if len(items) == 1 else f" n{len(items)}")
    if len(items) > 1 and shapes == {"tall"}:
        cls += " portraits"
    return f'<div class="{cls}">' + "".join(h for _, h in items) + "</div>"


def toc(sections):
    return '<nav class="toc" aria-label="Sections">' + "".join(
        f'<a href="#{sid}"{" class=\"on\"" if i == 0 else ""}>{e(lbl)}</a>' for i, (sid, lbl) in enumerate(sections)) + "</nav>\n"


def next_link(p, pre):
    i = [x["slug"] for x in PROJECTS].index(p["slug"])
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    return f'<a class="next" href="{url_for(nxt, pre)}"><span class="label">Next project</span><span class="next-title">{e(nxt["title"])} →</span></a>'


def case_head(p, pre, hero_html, meta, client_html=""):
    return f"""<div class="wide"><a class="back" href="{pre}works.html">← All work</a></div>
<div class="wide">{hero_html}</div>
<div class="col">
  <header class="intro">
    {client_html}
    <h1>{e(p['title'])}</h1>
    <p class="sub">{e(p.get('tagline',''))}</p>
  </header>
  <dl class="meta">{meta}</dl>
</div>
"""


def render_blocks(blocks, pre, title):
    out = []
    for b in blocks:
        kind, val = b[0], b[1]
        if kind == "p":
            out.append(f"<p>{e(val)}</p>")
        elif kind == "lead":
            out.append(f'<p class="leadline">{e(val)}</p>')
        elif kind == "stats":
            out.append('<div class="stats">' + "".join(f'<div class="stat"><b>{e(a)}</b><span>{e(c)}</span></div>' for a, c in val) + "</div>")
        elif kind == "media":
            out.append('<div class="panel work">' + "".join(media_row(r, pre, title) for r in val) + "</div>")
        elif kind == "table":
            head_, rows_ = val
            th = "".join(f"<th>{e(h)}</th>" for h in head_)
            trs = "".join("<tr>" + "".join(f"<td>{e(c)}</td>" for c in r) + "</tr>" for r in rows_)
            out.append(f'<div class="tbl"><table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>')
        elif kind == "code":
            out.append(f'<pre class="code">{e(val)}</pre>')
        elif kind == "cards":
            out.append('<div class="decisions">' + "".join(f'<div class="card"><strong>{e(t)}</strong>{e(x)}</div>' for t, x in val) + "</div>")
        elif kind == "steps":
            out.append('<div class="panel flows">' + "".join(f'<div class="flow"><strong class="flow-t">{e(q)}</strong><div class="steps">' + '<i>→</i>'.join(f"<span>{e(x)}</span>" for x in st) + "</div></div>" for q, st in val) + "</div>")
        elif kind == "list":
            out.append('<ul class="credits">' + "".join(f"<li>{e(x)}</li>" for x in val) + "</ul>")
        elif kind == "press":
            out.append('<div class="press-list">' + "".join(f'<a href="{u}" target="_blank" rel="noopener"{brand_attr(nm)}>{e(nm)} ↗</a>' for nm, u in val) + "</div>")
        elif kind == "btn":
            out.append(f'<a class="btn" href="{val[1]}" target="_blank" rel="noopener">{e(val[0])} ↗</a>')
        elif kind == "quote":
            out.append(f'<blockquote>{e(val[0])}<cite>{e(val[1])}</cite></blockquote>')
        elif kind == "note":
            out.append(f'<p class="cap">{e(val)}</p>')
    return '<div class="stack">' + "".join(out) + "</div>"


LOCK = '<svg class="lock" viewBox="0 0 24 24" aria-hidden="true"><rect x="4.5" y="10.5" width="15" height="10" rx="2"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/></svg>'


def nda_hero(p, pre):
    k, n = p["thumb"]
    subj = f"{p['title']} project".replace(" ", "%20")
    return f"""<div class="hero dark nda"><div class="nda-bg">{media_el(k, n, pre, 'full', '')}</div>
  <div class="nda-card">{LOCK}
    <p class="nda-t">This project is confidential</p>
    <p class="nda-x">It’s protected by an NDA. I’d love to walk you through it on a call.</p>
    <a class="btn" href="{pre}contact.html">Contact me →</a>
  </div></div>"""


def page_project(p):
    pre = "../"
    media = p.get("media", [])
    first = media[0] if media else []
    rest = media[1:]
    if p.get("confidential"):
        hero = nda_hero(p, pre)
    elif len(first) == 1:
        k, n = first[0][0], first[0][1]
        w, h = ratio(n)
        wide = " wide-media" if w > h * 1.2 else ""
        hero = f'<div class="hero{" dark" if k == "vid" else ""}"><div class="hero-in{wide}">{media_el(k, n, pre, "full", p["title"])}</div></div>'
    else:
        hero = f'<div class="hero">{media_row(first, pre, p["title"])}</div>'
    meta_items = [("Role", p.get("role", "")), ("Year", p.get("year", ""))]
    meta_items += [(k, v) for k, v in p.get("meta", []) if k != "Year" and v != p["title"]]
    meta_items += p.get("extra_meta", [])
    meta = "".join(f"<div><dt>{e(k)}</dt><dd>{e(v)}</dd></div>" for k, v in meta_items[:4] if v)
    client = next((v for k, v in p.get("meta", []) if k == "Client" and v != p["title"]), "")
    client_html = f'<p class="client">Client <b>{e(client)}</b></p>' if client else f'<p class="client">{e(p.get("type",""))} <b>{e(p.get("year",""))}</b></p>'

    sections, n = [], 0

    def sec(sid, label, h2, inner, wide=False):
        nonlocal n
        n += 1
        sections.append((sid, label))
        h = f"<h2>{e(h2)}</h2>" if h2 else ""
        if wide:
            return f'<section id="{sid}" class="wide"><div class="col head"><p class="label" data-n="{n:02d}">{e(label)}</p>{h}</div>{inner}</section>'
        return f'<div class="col"><section id="{sid}"><div class="head"><p class="label" data-n="{n:02d}">{e(label)}</p>{h}</div>{inner}</section></div>'

    body = ""
    if p.get("sections"):
        for s_ in p["sections"]:
            has_media = any(b[0] == "media" for b in s_["blocks"])
            inner = render_blocks(s_["blocks"], pre, p["title"])
            if has_media:
                inner = f'<div class="wide-stack">{inner}</div>'
            body += sec(s_["id"], s_["label"], s_.get("h2", ""), inner, wide=has_media)
    else:
        info = "".join(f"<p>{e(t)}</p>" for t in p.get("info", []))
        body += sec("overview", "Overview", p.get("result", ""), f'<div class="stack">{info}</div>')
        if rest:
            body += sec("work", "The work", "", '<div class="panel work">' + "".join(media_row(r, pre, p["title"]) for r in rest) + "</div>", wide=True)
        res_inner = ""
        if p.get("stats"):
            res_inner += '<div class="stats">' + "".join(f'<div class="stat"><b>{e(a)}</b><span>{e(b)}</span></div>' for a, b in p["stats"]) + "</div>"
        if p.get("press"):
            res_inner += '<div class="press-list">' + "".join(f'<a href="{u}" target="_blank" rel="noopener">{e(nm)} ↗</a>' for nm, u in p["press"]) + "</div>"
        if p.get("live"):
            res_inner += f'<a class="btn" href="{p["live"]}" target="_blank" rel="noopener">See it live ↗</a>'
        if res_inner:
            body += sec("results", "Results", "", f'<div class="stack">{res_inner}</div>')
        if p.get("credits"):
            body += sec("credits", "Credits", "", '<ul class="credits">' + "".join(f"<li>{e(c)}</li>" for c in p["credits"]) + "</ul>")

    out = head(f"{p['title']} — {SITE['name']}", pre, p.get("tagline", "")) + header(pre, "Work")
    out += toc(sections) + '<main id="top" class="case">\n'
    out += case_head(p, pre, hero, meta, client_html)
    out += body
    out += f'<div class="wide">{next_link(p, pre)}</div>'
    out += footer(pre)
    return out


def page_snackpass():
    pre = "../../"
    p = BY["snackpass"]
    body = open(os.path.join(ROOT, "works/snackpass/body.html"), encoding="utf-8").read()
    body = body.replace('<video src="media/demo.mp4"', '<video class="sp-demo" src="media/demo.mp4"', 1)
    body = body.replace("</video>\n    </div>", '</video>\n      <div class="hero-labels" aria-hidden="true"><span style="left:19.6%">Categories</span><span style="left:50%">Search bar</span><span style="left:80.4%">Filters</span></div>\n    </div>', 1)
    # number the section labels and collect them for the side tabs
    sections, n = [], 0

    def numbered(m):
        nonlocal n
        n += 1
        return f'<p class="label" data-n="{n:02d}">'
    ids = re.findall(r'<section id="([^"]+)"', body)
    labels = re.findall(r'<section id="[^"]+"[^>]*>\s*<div class="[^"]*head">\s*<p class="label">([^<]+)</p>', body)
    body = re.sub(r'(?<=<div class="head">\n      )<p class="label">|(?<=<div class="col head">\n    )<p class="label">', numbered, body)
    sections = list(zip(ids, labels))
    out = head(f"{p['title']} — {SITE['name']}", pre, p.get("tagline", "")) + header(pre, "Work")
    out += toc(sections) + '<main id="top" class="case lc">\n'
    out += f'<div class="wide"><a class="back" href="{pre}works.html">← All work</a></div>\n'
    out += body
    out += f'<div class="wide">{next_link(p, pre)}</div>'
    out += footer(pre)
    return out


def write(path, text):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(text)


if __name__ == "__main__":
    write("index.html", page_home())
    write("works.html", page_works())
    write("contact.html", page_contact())
    for p in PROJECTS:
        if not p.get("external"):
            write(f"works/{p['slug']}.html", page_project(p))
    write("works/snackpass/index.html", page_snackpass())
    print("built", 4 + sum(1 for p in PROJECTS if not p.get("external")), "pages")

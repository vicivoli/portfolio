# nikolaipetukhov.com

Static portfolio site (replaces Framer). Plain HTML/CSS/JS, no build tools needed to host.

## Edit content
All text, links, categories and media lists are in `data.py`.
After editing, run:

    python3 build.py

This regenerates index.html, works.html, contact.html and works/*.html.
Put new images/videos in `media/`. For a new video, also add a 6-second
muted preview in `media/thumb/` and a poster frame in `media/poster/`.

## Publish on GitHub Pages
1. Create a repo (e.g. `portfolio`) and upload everything in this folder.
2. Settings → Pages → Source: "Deploy from a branch", branch `main`, folder `/ (root)`.
3. Custom domain: enter `nikolaipetukhov.com`, then point the domain's DNS to GitHub
   (A records 185.199.108.153, .109.153, .110.153, .111.153 and a CNAME `www` → <username>.github.io).

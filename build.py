#!/usr/bin/env python3
"""Erzeugt alle HTML-Seiten aus content.py.  Ausführen: python3 build.py"""
from pathlib import Path
from html import escape

from content import (SITE, HERO, TOOLS, SERVICES, ABOUT, FOOTER_WORDS,
                     PROJECTS, GROUPS, HERO_STACK, ALL_PROJECTS)

ROOT = Path(__file__).parent
BY_SLUG = {p["slug"]: p for p in PROJECTS}
_SIZES = {}


def img_size(name):
    """Breite und Höhe eines JPEG/PNG aus assets/img lesen (ohne externe Bibliotheken)."""
    if name not in _SIZES:
        data = (ROOT / "assets/img" / name).read_bytes()
        if data[:8] == b"\x89PNG\r\n\x1a\n":
            _SIZES[name] = (int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big"))
        else:
            i = 2
            while i < len(data):
                marker, length = data[i + 1], int.from_bytes(data[i + 2:i + 4], "big")
                if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                    _SIZES[name] = (int.from_bytes(data[i + 7:i + 9], "big"), int.from_bytes(data[i + 5:i + 7], "big"))
                    break
                i += 2 + length
    return _SIZES[name]


def img(base, name, alt="", lazy=True, extra=""):
    w, h = img_size(name)
    loading = ' loading="lazy" decoding="async"' if lazy else ""
    return f'<img src="{base}assets/img/{name}" alt="{escape(alt)}" width="{w}" height="{h}"{loading}{extra}>'

# ---------- Icons ----------
def svg(body, size=20, sw=1.8):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{body}</svg>')

ARROW = svg('<path d="M7 17 17 7M8 7h9v9"/>', 14, 2)

SOCIAL = {
    "instagram": ('<svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.2">'
                  '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/>'
                  '<circle cx="17.5" cy="6.5" r="0.6" fill="currentColor"/></svg>', "Instagram"),
    "behance": ('<svg viewBox="0 0 24 24" width="15" height="15" fill="currentColor"><path d="M8.2 11.4c.9-.4 1.4-1.1 '
                '1.4-2.2 0-2-1.5-2.7-3.4-2.7H1v11h5.4c2 0 3.9-1 3.9-3.2 0-1.4-.7-2.5-2.1-2.9zM3.4 8.4h2.3c.9 0 1.6.2 '
                '1.6 1.2 0 .9-.6 1.2-1.5 1.2H3.4V8.4zm2.5 7.2H3.4v-3h2.6c1 0 1.7.4 1.7 1.5 0 1.1-.8 1.5-1.8 1.5zM20.9 '
                '13.9c.2-2.7-1.4-4.9-4.1-4.9-2.5 0-4.2 1.9-4.2 4.3 0 2.5 1.6 4.3 4.2 4.3 1.9 0 3.2-.9 3.8-2.8h-2c-.2.7-1 '
                '1-1.7 1-1.3 0-2-.7-2-1.9h6zm-6-1.3c.1-1 .7-1.7 1.8-1.7s1.6.7 1.7 1.7h-3.5zM14.5 6.9h4.6v1.2h-4.6z"/></svg>',
                "Behance"),
    "linkedin": ('<svg viewBox="0 0 24 24" width="13" height="13" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 '
                 '5 2.5 2.5 0 0 1 0-5zM3 9.5h4V21H3zM9.5 9.5h3.8v1.6h.1c.5-1 1.8-2 3.8-2 4 0 4.8 2.6 4.8 6V21h-4v-5.2c0-1.2 '
                 '0-2.9-1.8-2.9s-2 1.4-2 2.8V21h-4z"/></svg>', "LinkedIn"),
}

SERVICE_ICONS = {
    "billboard": svg('<rect x="3" y="4" width="18" height="11" rx="1.5"/><path d="M8 15v5M16 15v5M3 20h18"/>'),
    "tag": svg('<path d="M3 12V4a1 1 0 0 1 1-1h8l9 9-9 9z"/><circle cx="7.5" cy="7.5" r="1.3" fill="currentColor"/>'),
    "book": svg('<path d="M4 5a2 2 0 0 1 2-2h13v15H6a2 2 0 0 0-2 2z"/><path d="M4 20a2 2 0 0 0 2 2h13v-4"/>'),
    "social": svg('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/>'),
    "wand": svg('<path d="m15 4 5 5L9 20l-5-5z"/><path d="M19 2v3M17.5 3.5h3M5 3v3M3.5 4.5h3"/>'),
    "box": svg('<path d="M12 2 3 7v10l9 5 9-5V7z"/><path d="m3 7 9 5 9-5M12 12v10"/>'),
    "layout": svg('<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 9v12"/>'),
}

TOOL_ICONS = {
    "Ae": ("After Effects", '<span class="tool-txt">Ae</span>'),
    "Ai": ("Illustrator", '<span class="tool-txt">Ai</span>'),
    "Ps": ("Photoshop", '<span class="tool-txt">Ps</span>'),
    "Pr": ("Premiere Pro", '<span class="tool-txt">Pr</span>'),
    "framer": ("Framer", '<svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M5 2h14v7h-7zM5 9h7l7 7H12v6l-7-7z"/></svg>'),
    "claude": ("Claude", '<svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round">'
               + "".join(f'<path d="M12 12 12 3" transform="rotate({a} 12 12)"/>' for a in range(0, 360, 30)) + '</svg>'),
    "chatgpt": ("ChatGPT", '<svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.7">'
                + "".join(f'<ellipse cx="12" cy="12" rx="4" ry="9" transform="rotate({a} 12 12)"/>' for a in (0, 60, 120)) + '</svg>'),
}


# ---------- Bausteine ----------
def social_links(cls="social"):
    return f'<div class="{cls}">' + "".join(
        f'<a href="{SITE[k]}" target="_blank" rel="noopener" aria-label="{label}">{icon}</a>'
        for k, (icon, label) in SOCIAL.items()) + "</div>"


def head(title, description, base, path="", image="ritter-cover.jpg"):
    url = SITE["url"] + path
    return f"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<script>document.documentElement.classList.add("js")</script>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<meta property="og:type" content="website">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(description)}">
<meta property="og:image" content="{SITE['url']}assets/img/{image}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="de_DE">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#fafafa">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/png" href="{base}assets/img/avatar-64.png">
<link rel="apple-touch-icon" href="{base}assets/img/apple-touch-icon.png">
<link rel="preload" href="{base}assets/fonts/switzer-500.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{base}assets/css/style.css">
<script defer src="{base}assets/js/main.js"></script>
</head>
<body>
<a class="skip-link" href="#main">Zum Inhalt springen</a>
<div class="frame">"""


def nav(base, current=""):
    cur = ' aria-current="page"' if current == "projects" else ""
    return f"""
<header class="nav" data-nav>
  <a class="nav-brand" href="{base if base else './'}" aria-label="Startseite"><img src="{base}assets/img/avatar-64.png" alt="" width="32" height="32"><span translate="no">{SITE['name']}</span></a>
  <nav class="nav-links" id="nav-links" aria-label="Hauptmenü">
    <a href="{base}projects/"{cur}>Arbeiten</a>
    <a href="{base}#branding">Branding</a>
    <a href="{base}#about">Über mich</a>
    <a class="nav-cta" href="mailto:{SITE['email']}">Kontakt</a>
  </nav>
  <button class="nav-toggle" type="button" aria-label="Menü öffnen" aria-expanded="false" aria-controls="nav-links"><i></i><i></i><i></i></button>
</header>"""


def footer(base):
    words = "".join(f'<span class="word{" is-active" if i == 0 else ""}">{w}</span>' for i, w in enumerate(FOOTER_WORDS))
    return f"""
</div>
<footer class="footer">
  <div class="footer-inner">
    <h2 class="footer-title">
      <span class="ft-line">Lass uns <span class="sr-only">{FOOTER_WORDS[0]}</span><span class="words" aria-hidden="true">{words}</span></span>
      <span class="ft-muted">gemeinsam großartige Arbeit.</span>
    </h2>
    <div class="footer-contact">
      <div><p class="label">E-Mail</p><a class="footer-mail" href="mailto:{SITE['email']}">{SITE['email']}</a></div>
      <div><p class="label">Social Media</p>{social_links("social social-dark")}</div>
    </div>
    <div class="footer-meta">
      <div><p class="label">Menü</p><a href="{base}projects/">Arbeiten</a><a href="{base}#branding">Branding</a><a href="{base}#services">Kompetenzen</a></div>
      <div><p class="label">Rechtliches</p><a href="{base}datenschutz/">Datenschutz</a></div>
      <p class="copy">© {SITE['year']} {SITE['name']}</p>
    </div>
  </div>
  <div class="footer-giant" aria-hidden="true" translate="no">ERNESTO</div>
</footer>
</body>
</html>
"""


def card(p, base, eager=False):
    return f"""
    <a class="card reveal" href="{base}projects/{p['slug']}/">
      <div class="card-media">{img(base, p['cover'], p['name'], lazy=not eager)}</div>
      <div class="card-info">
        <div><h3>{escape(p['name'])}</h3><p>{escape(p['category'])}</p></div>
        <span class="card-link">{ARROW}Projekt ansehen</span>
      </div>
    </a>"""


def all_projects_link(base):
    return f'<div class="center"><a class="text-link" href="{base}projects/">Alle Projekte ansehen {ARROW}</a></div>'


def group_section(g, base, first=False, link=True):
    muted, main = g["heading"]
    sid = "work" if first and base == "" else g["id"]
    heading = f'{muted} {main}' if main == "Projekte" else f'<span class="muted">{muted}</span><br>{main}'
    cards = "".join(card(BY_SLUG[s], base, first and i < 2) for i, s in enumerate(g["slugs"]))
    more = all_projects_link(base) if link and base == "" and g is [x for x in GROUPS if x["home"]][-1] else ""
    return f"""
  <section class="section" id="{sid}">
    <h2 class="h2 reveal">{heading}</h2>
    <div class="grid">{cards}
    </div>
    {more}
  </section>
"""


# ---------- Seiten ----------
def page_home():
    base = ""
    stack = "".join(
        f'<a class="stack-card" href="projects/{s}/" aria-label="{escape(BY_SLUG[s]["name"])}">'
        f'{img("", BY_SLUG[s]["cover"], lazy=False, extra=chr(32) + "fetchpriority=" + chr(34) + ("high" if k == 0 else "auto") + chr(34))}'
        f'<span class="stack-label">{escape(BY_SLUG[s]["name"])}<small>{escape(BY_SLUG[s]["category"])}</small></span></a>'
        for k, s in enumerate(HERO_STACK))
    dots = "".join(f'<button class="stack-dot" type="button" aria-label="{escape(BY_SLUG[s]["name"])} zeigen"></button>'
                   for s in HERO_STACK)
    dots += ('<button class="stack-pause" type="button" aria-label="Automatischen Wechsel pausieren" aria-pressed="false">'
             '<svg viewBox="0 0 24 24" width="12" height="12" fill="currentColor" aria-hidden="true">'
             '<path class="i-pause" d="M7 5h3v14H7zM14 5h3v14h-3z"/><path class="i-play" d="M8 5v14l11-7z"/></svg></button>')
    tools = "".join(f'<li class="tool" title="{name}" aria-label="{name}">{icon}</li>'
                    for name, icon in (TOOL_ICONS[t] for t in TOOLS))
    services = "".join(f'<li class="service reveal"><span class="service-icon">{SERVICE_ICONS[i]}</span>{escape(t)}</li>'
                       for i, t in SERVICES)
    about = "".join(f"<p>{escape(t)}</p>" for t in ABOUT)
    groups = "".join(group_section(g, base, first=(k == 0)) for k, g in enumerate(x for x in GROUPS if x["home"]))
    return head(SITE["title"], SITE["description"], base, "", HERO_STACK and BY_SLUG[HERO_STACK[0]]["cover"]) + nav(base) + f"""
<main id="main">
  <section class="hero">
    <div class="hero-text">
      <p class="badge"><span class="dot"></span>{SITE['available']}</p>
      <h1 class="display">{HERO['title']}</h1>
      <p class="lead">{HERO['text']}</p>
      <a class="btn" href="mailto:{SITE['email']}"><img src="assets/img/avatar-64.png" alt="" width="28" height="28">{HERO['cta']}</a>
    </div>
    <div class="stack-wrap">
      <div class="stack" data-stack aria-roledescription="Karussell" aria-label="Ausgewählte Projekte">{stack}</div>
      <div class="stack-dots" data-stack-dots>{dots}</div>
    </div>
  </section>

{groups}
  <section class="section split" id="services">
    <div>
      <h2 class="h2 reveal"><span class="muted">Kompetenzen</span><br>Was ich mitbringe.</h2>
      <p class="small-title">Meine Tools</p>
      <ul class="tools">{tools}</ul>
    </div>
    <ul class="services">{services}</ul>
  </section>

  <section class="section" id="about">
    <h2 class="h2 reveal"><span class="muted">Über mich</span><br>Design mit Liebe zum Detail.</h2>
    <div class="about">
      <div class="about-card reveal">
        <div class="portrait">
          {img("", "portrait.png", "Porträt von Ernesto Carrera")}
          {social_links("social social-overlay")}
        </div>
        <p class="about-name">Ernesto Carrera</p>
        <p class="about-role">Grafikdesigner</p>
      </div>
      <div class="about-text">{about}</div>
    </div>
  </section>
</main>""" + footer(base)


def page_projects():
    base = "../"
    groups = "".join(group_section(g, base, first=(k == 0)) for k, g in enumerate(GROUPS))
    return head(f"Arbeiten | {SITE['name']}", "Eine Auswahl meiner Projekte aus Außenwerbung, Bewegtbild, Branding und KI.",
                base, "projects/") + nav(base, "projects") + f"""
<main id="main">
  <section class="page-head">
    <h1 class="display reveal"><span class="muted">Meine</span><br>Arbeiten</h1>
    <p class="lead">Eine Auswahl meiner Projekte aus Außenwerbung, Bewegtbild, Branding und KI.</p>
  </section>
{groups}
</main>""" + footer(base)


def media_block(m, base):
    kind, src, caption = m
    if kind.startswith("video"):
        srcs = src if isinstance(src, list) else [src]
        cls = "media media-vertical" if kind == "video-vertical" else "media"
        vids = "".join(f'<div class="{cls}"><video src="{base}assets/video/{v}#t=0.5" muted loop playsinline controls '
                       f'preload="metadata" data-autoplay></video></div>' for v in srcs)
        inner = f'<div class="media-row">{vids}</div>' if len(srcs) > 1 else vids
    elif kind == "sheet":
        imgs = "".join(img(base, s, caption if k == 0 else "") for k, s in enumerate(src))
        inner = f'<div class="media sheet">{imgs}</div>'
    else:
        cls = "media-row" if len(src) > 1 else ""
        imgs = "".join(f'<div class="media">{img(base, s, caption)}</div>' for s in src)
        inner = f'<div class="{cls}">{imgs}</div>' if cls else imgs
    return f'<figure class="block reveal">{inner}<figcaption>{escape(caption)}</figcaption></figure>'


def page_project(p):
    base = "../../"
    group = next(g["slugs"] for g in GROUPS if p["slug"] in g["slugs"])
    order = group if len(group) >= 3 else ALL_PROJECTS
    i = order.index(p["slug"])
    more = [BY_SLUG[order[(i + k) % len(order)]] for k in (1, 2)]
    text = "".join(f"<p>{escape(t)}</p>" for t in p["text"])
    chips = "".join(f"<li>{escape(s)}</li>" for s in p["services"])
    link = (f'<a class="text-link" href="{p["link"][1]}" target="_blank" rel="noopener">{p["link"][0]} {ARROW}</a>'
            if p.get("link") else "")
    blocks = "".join(media_block(m, base) for m in p["media"])
    more_cards = "".join(card(m, base) for m in more)
    desc = " ".join(p["text"])
    desc = desc if len(desc) <= 160 else desc[:157].rsplit(" ", 1)[0] + "…"
    return head(f"{p['title']} | {SITE['name']}, Grafikdesigner", desc, base,
                f"projects/{p['slug']}/", p["cover"]) + nav(base, "projects") + f"""
<main id="main">
  <section class="project-head">
    <h1 class="h1 reveal">{p['heading']}</h1>
    <dl class="meta"><div><dt>Kunde</dt><dd>{escape(p['client'])}</dd></div><div><dt>Jahr</dt><dd>{p['year']}</dd></div></dl>
    <div class="project-text">{text}</div>
    <p class="small-label">Meine Aufgaben</p>
    <ul class="chips">{chips}</ul>
    {link}
  </section>
  <section class="section blocks">{blocks}</section>
  <section class="section">
    <h2 class="h2 reveal"><span class="muted">Weitere</span> Projekte</h2>
    <div class="grid">{more_cards}
    </div>
    {all_projects_link(base)}
  </section>
</main>""" + footer(base)


def page_privacy():
    base = "../"
    return head(f"Datenschutz | {SITE['name']}", "Datenschutzerklärung", base, "datenschutz/") + nav(base) + f"""
<main id="main">
  <section class="project-head legal">
    <h1 class="h1">Datenschutz&shy;erklärung</h1>
    <h2>Verantwortlicher</h2>
    <p>{SITE['name']}<br>E-Mail: <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
    <h2>Allgemeines</h2>
    <p>Diese Website ist ein persönliches Portfolio. Es gibt keine Kontaktformulare, kein Nutzerkonto und keine
    Analyse- oder Marketing-Tools. Es werden keine Cookies gesetzt. Schriften und Medien werden direkt von diesem
    Server geladen, nicht von Drittanbietern.</p>
    <h2>Server-Logfiles</h2>
    <p>Beim Aufruf der Website verarbeitet der Hosting-Anbieter technisch notwendige Daten (z.&nbsp;B. IP-Adresse,
    Datum und Uhrzeit, aufgerufene Seite, Browsertyp), um die Website auszuliefern und ihre Sicherheit zu gewährleisten
    (Art.&nbsp;6 Abs.&nbsp;1 lit.&nbsp;f DSGVO). Diese Daten werden nicht mit anderen Datenquellen zusammengeführt.</p>
    <h2>Kontakt per E-Mail</h2>
    <p>Wenn du mir eine E-Mail schreibst, verarbeite ich deine Angaben ausschließlich zur Bearbeitung deiner Anfrage
    (Art.&nbsp;6 Abs.&nbsp;1 lit.&nbsp;b und f DSGVO) und lösche sie, sobald sie nicht mehr benötigt werden.</p>
    <h2>Externe Links</h2>
    <p>Diese Website verlinkt auf Instagram, Behance und LinkedIn. Erst wenn du einen dieser Links anklickst, gelten
    die Datenschutzbestimmungen des jeweiligen Anbieters.</p>
    <h2>Deine Rechte</h2>
    <p>Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit
    und Widerspruch sowie das Recht, dich bei einer Datenschutz-Aufsichtsbehörde zu beschweren. Schreib mir dazu
    einfach an die oben genannte E-Mail-Adresse.</p>
  </section>
</main>""" + footer(base)


def page_404():
    base = SITE["url"]  # absolute Pfade, weil die 404-Seite unter jeder Adresse ausgeliefert wird
    return head(f"Seite nicht gefunden | {SITE['name']}", "Diese Seite gibt es nicht.", base, "404.html") + nav(base) + f"""
<main id="main">
  <section class="page-head notfound">
    <p class="small-label">Fehler 404</p>
    <h1 class="display"><span class="muted">Diese Seite</span><br>gibt es nicht.</h1>
    <p class="lead">Vielleicht wurde sie verschoben. Hier geht es weiter:</p>
    <div class="notfound-links">
      <a class="btn" href="{base}">Zur Startseite</a>
      <a class="text-link" href="{base}projects/">Alle Projekte ansehen {ARROW}</a>
    </div>
  </section>
</main>""" + footer(base)


def sitemap():
    paths = ["", "projects/", "datenschutz/"] + [f"projects/{p['slug']}/" for p in PROJECTS]
    urls = "".join(f"  <url><loc>{SITE['url']}{x}</loc></url>\n" for x in paths)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n'


def write(path, html):
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print("✓", path)


if __name__ == "__main__":
    write("index.html", page_home())
    write("projects/index.html", page_projects())
    for p in PROJECTS:
        write(f"projects/{p['slug']}/index.html", page_project(p))
    write("datenschutz/index.html", page_privacy())
    write("404.html", page_404())
    write("sitemap.xml", sitemap())

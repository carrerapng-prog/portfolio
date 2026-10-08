#!/usr/bin/env python3
"""Erzeugt alle HTML-Seiten aus content.py.  Ausführen: python3 build.py"""
from pathlib import Path
from html import escape

from content import (SITE, HERO, TOOLS, SERVICES, ABOUT, FOOTER_WORDS,
                     PROJECTS, GROUPS, HERO_STACK, ALL_PROJECTS, KI_PARTS)

ROOT = Path(__file__).parent
BY_SLUG = {p["slug"]: p for p in PROJECTS}

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


def head(title, description, base):
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
<meta property="og:image" content="{SITE['url']}assets/img/ritter-cover.jpg">
<meta property="og:url" content="{SITE['url']}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{base}assets/img/avatar.png">
<link rel="preload" href="{base}assets/fonts/switzer-500.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{base}assets/css/style.css">
<script defer src="{base}assets/js/main.js"></script>
</head>
<body>
<div class="frame">"""


def nav(base):
    return f"""
<header class="nav" data-nav>
  <a class="nav-brand" href="{base}"><img src="{base}assets/img/avatar.png" alt="" width="32" height="32"><span>{SITE['name']}</span></a>
  <nav class="nav-links">
    <a href="{base}projects/">Arbeiten</a>
    <a href="{base}#branding">Branding</a>
    <a href="{base}#about">Über mich</a>
    <a class="nav-cta" href="mailto:{SITE['email']}">Kontakt</a>
  </nav>
  <button class="nav-toggle" aria-label="Menü öffnen" aria-expanded="false"><i></i><i></i><i></i></button>
</header>"""


def footer(base):
    words = "".join(f'<span class="word{" is-active" if i == 0 else ""}">{w}</span>' for i, w in enumerate(FOOTER_WORDS))
    return f"""
</div>
<footer class="footer">
  <div class="footer-inner">
    <h2 class="footer-title">
      <span class="ft-line">Lass uns <span class="words" aria-label="{FOOTER_WORDS[0]}">{words}</span></span>
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
  <div class="footer-giant" aria-hidden="true">ERNESTO</div>
</footer>
</body>
</html>
"""


def card(p, base, eager=False):
    loading = "eager" if eager else "lazy"
    return f"""
    <a class="card reveal" href="{base}projects/{p['slug']}/">
      <div class="card-media"><img src="{base}assets/img/{p['cover']}" alt="{escape(p['name'])}" loading="{loading}"></div>
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
        f'<img src="assets/img/{BY_SLUG[s]["cover"]}" alt="">'
        f'<span class="stack-label">{escape(BY_SLUG[s]["name"])}<small>{escape(BY_SLUG[s]["category"])}</small></span></a>'
        for s in HERO_STACK)
    dots = "".join(f'<button class="stack-dot" aria-label="{escape(BY_SLUG[s]["name"])} zeigen"></button>'
                   for s in HERO_STACK)
    tools = "".join(f'<li class="tool" title="{name}" aria-label="{name}">{icon}</li>'
                    for name, icon in (TOOL_ICONS[t] for t in TOOLS))
    services = "".join(f'<li class="service reveal"><span class="service-icon">{SERVICE_ICONS[i]}</span>{escape(t)}</li>'
                       for i, t in SERVICES)
    about = "".join(f"<p>{escape(t)}</p>" for t in ABOUT)
    groups = "".join(group_section(g, base, first=(k == 0)) for k, g in enumerate(x for x in GROUPS if x["home"]))
    return head(SITE["title"], SITE["description"], base) + nav(base) + f"""
<main>
  <section class="hero">
    <div class="hero-text">
      <p class="badge"><span class="dot"></span>{SITE['available']}</p>
      <h1 class="display">{HERO['title']}</h1>
      <p class="lead">{HERO['text']}</p>
      <a class="btn" href="mailto:{SITE['email']}"><img src="assets/img/avatar.png" alt="" width="28" height="28">{HERO['cta']}</a>
    </div>
    <div class="stack-wrap">
      <div class="stack" data-stack>{stack}</div>
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
          <img src="assets/img/portrait.png" alt="Porträt von Ernesto Carrera" loading="lazy">
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
    return head(f"Arbeiten | {SITE['name']}", "Eine Auswahl meiner Projekte aus Außenwerbung, Bewegtbild, Branding und KI.", base) + nav(base) + f"""
<main>
  <section class="page-head">
    <h1 class="display reveal"><span class="muted">Meine</span><br>Arbeiten</h1>
    <p class="lead">Eine Auswahl meiner Projekte aus Außenwerbung, Bewegtbild, Branding und KI.</p>
  </section>
{groups}
</main>""" + footer(base)


def media_block(m, base):
    if m[0] == "section":
        _, sid, name, category, text = m
        paras = "".join(f"<p>{escape(t)}</p>" for t in text)
        return (f'<section class="subproject" id="{sid}"><p class="small-label">{escape(category)}</p>'
                f'<h2 class="h2 reveal">{escape(name)}</h2><div class="project-text">{paras}</div></section>')
    kind, src, caption = m
    if kind.startswith("video"):
        srcs = src if isinstance(src, list) else [src]
        cls = "media media-vertical" if kind == "video-vertical" else "media"
        vids = "".join(f'<div class="{cls}"><video src="{base}assets/video/{v}#t=0.5" muted loop playsinline controls '
                       f'preload="metadata" data-autoplay></video></div>' for v in srcs)
        inner = f'<div class="media-row">{vids}</div>' if len(srcs) > 1 else vids
    elif kind == "sheet":
        imgs = "".join(f'<img src="{base}assets/img/{s}" alt="" loading="lazy">' for s in src)
        inner = f'<div class="media sheet">{imgs}</div>'
    else:
        cls = "media-row" if len(src) > 1 else ""
        imgs = "".join(f'<div class="media"><img src="{base}assets/img/{s}" alt="{escape(caption)}" loading="lazy"></div>'
                       for s in src)
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
    parts = ""
    if p.get("parts"):
        parts = ('<p class="small-label">Inhalt</p><ul class="chips toc">' +
                 "".join(f'<li><a href="#{sid}">{escape(name)}</a></li>' for sid, name in p["parts"]) + "</ul>")
    more_cards = "".join(card(m, base) for m in more)
    return head(f"{p['title']} | {SITE['name']}, Grafikdesigner", " ".join(p["text"])[:160], base) + nav(base) + f"""
<main>
  <section class="project-head">
    <h1 class="h1 reveal">{p['heading']}</h1>
    <dl class="meta"><div><dt>Kunde</dt><dd>{escape(p['client'])}</dd></div><div><dt>Jahr</dt><dd>{p['year']}</dd></div></dl>
    <div class="project-text">{text}</div>
    <p class="small-label">Meine Aufgaben</p>
    <ul class="chips">{chips}</ul>
    {parts}
    {link}
  </section>
  <section class="section blocks">{blocks}</section>
  <section class="section">
    <h2 class="h2 reveal"><span class="muted">More</span> Projects</h2>
    <div class="grid">{more_cards}
    </div>
    {all_projects_link(base)}
  </section>
</main>""" + footer(base)


def page_privacy():
    base = "../"
    return head(f"Datenschutz | {SITE['name']}", "Datenschutzerklärung", base) + nav(base) + f"""
<main>
  <section class="project-head legal">
    <h1 class="h1">Datenschutz&shy;erklärung</h1>
    <h3>Verantwortlicher</h3>
    <p>{SITE['name']}<br>E-Mail: <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
    <h3>Allgemeines</h3>
    <p>Diese Website ist ein persönliches Portfolio. Es gibt keine Kontaktformulare, kein Nutzerkonto und keine
    Analyse- oder Marketing-Tools. Es werden keine Cookies gesetzt. Schriften und Medien werden direkt von diesem
    Server geladen, nicht von Drittanbietern.</p>
    <h3>Server-Logfiles</h3>
    <p>Beim Aufruf der Website verarbeitet der Hosting-Anbieter technisch notwendige Daten (z.&nbsp;B. IP-Adresse,
    Datum und Uhrzeit, aufgerufene Seite, Browsertyp), um die Website auszuliefern und ihre Sicherheit zu gewährleisten
    (Art.&nbsp;6 Abs.&nbsp;1 lit.&nbsp;f DSGVO). Diese Daten werden nicht mit anderen Datenquellen zusammengeführt.</p>
    <h3>Kontakt per E-Mail</h3>
    <p>Wenn du mir eine E-Mail schreibst, verarbeite ich deine Angaben ausschließlich zur Bearbeitung deiner Anfrage
    (Art.&nbsp;6 Abs.&nbsp;1 lit.&nbsp;b und f DSGVO) und lösche sie, sobald sie nicht mehr benötigt werden.</p>
    <h3>Externe Links</h3>
    <p>Diese Website verlinkt auf Instagram, Behance und LinkedIn. Erst wenn du einen dieser Links anklickst, gelten
    die Datenschutzbestimmungen des jeweiligen Anbieters.</p>
    <h3>Deine Rechte</h3>
    <p>Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit
    und Widerspruch sowie das Recht, dich bei einer Datenschutz-Aufsichtsbehörde zu beschweren. Schreib mir dazu
    einfach an die oben genannte E-Mail-Adresse.</p>
  </section>
</main>""" + footer(base)


def page_redirect(target):
    return f"""<!doctype html>
<html lang="de"><head><meta charset="utf-8"><title>Weiterleitung</title>
<meta http-equiv="refresh" content="0; url={target}"><link rel="canonical" href="{target}">
<script>location.replace("{target}")</script></head>
<body><a href="{target}">Weiter zu den KI-Projekten</a></body></html>
"""


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
    # Alte Adressen der einzelnen KI-Projekte leiten auf die gemeinsame Seite weiter
    for slug in KI_PARTS:
        write(f"projects/{slug}/index.html", page_redirect(f"../ki-projekte/#{slug}"))

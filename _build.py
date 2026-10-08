#!/usr/bin/env python3
"""Static site builder for SnoutsWise (Joshua Israel Ventures LLC).

Run:  python3 _build.py
Outputs plain HTML at the repo root (GitHub Pages, deploy from branch main /).

SWITCHING TO A CUSTOM DOMAIN: change SITE_URL below (one line), add a CNAME file
containing the bare domain, rebuild, commit, push. All internal links are relative.
"""
import json, math, os, re, html, datetime
import _photos

SITE_URL = "https://snoutswise.com/"   # <- the ONE line that sets the base URL (was https://joshuaofisrael.github.io/snoutswise/ before the domain)
SITE_NAME = "SnoutsWise"
LEGAL_NAME = "Joshua Israel Ventures LLC"
CONTACT_EMAIL = "joshuaofisrael@gmail.com"
GSC_TOKEN = ""          # Google Search Console HTML tag token (content="..."); empty = no tag
CF_BEACON_TOKEN = ""    # Cloudflare Web Analytics beacon token; empty = no beacon. NOTE: update privacy.html before enabling.
INDEXNOW_KEY = "f82447b1414b64e38975376b34f684d7"
TODAY = "2026-10-08"
OG_IMAGE = "og-image.png"

ROOT = os.path.dirname(os.path.abspath(__file__))

NAV = [("index.html", "Home"), ("breeds.html", "Breeds"), ("care.html", "Care"), ("health.html", "Health"),
       ("training.html", "Training"), ("behavior.html", "Behavior"), ("can-dogs-eat.html", "Can My Dog Eat This?"),
       ("dog-age-calculator.html", "Age Calculator"), ("blog/", "Blog"), ("faq.html", "FAQ"), ("glossary.html", "Glossary")]

# Logo: electric blue paw on a laser lemon badge with a tangerine ring (neon theme, 9 Oct 2026)
PAW = ('<ellipse cx="32" cy="41" rx="12" ry="10" fill="#2A2BD1"/><ellipse cx="17" cy="29" rx="5" ry="6.5" fill="#2A2BD1"/>'
       '<ellipse cx="26.5" cy="19.5" rx="5" ry="6.5" fill="#2A2BD1"/><ellipse cx="37.5" cy="19.5" rx="5" ry="6.5" fill="#2A2BD1"/>'
       '<ellipse cx="47" cy="29" rx="5" ry="6.5" fill="#2A2BD1"/><ellipse cx="28" cy="38" rx="3" ry="2" fill="#FF8A1F"/>')
LOGO = ('<svg role="img" width="40" height="40" viewBox="0 0 64 64" aria-labelledby="logo-t"><title id="logo-t">SnoutsWise logo</title>'
        '<circle cx="32" cy="32" r="29" fill="#FFE600" stroke="#FF8A1F" stroke-width="5"/>' + PAW + '</svg>')
# Small decorative doodles (inline SVG, aria-hidden)
DOODLE_PAWS = ('<svg class="doodle" aria-hidden="true" focusable="false" viewBox="0 0 72 72">'
               '<g fill="#FF8A1F" transform="rotate(-18 20 50) translate(6 34) scale(.42)"><ellipse cx="32" cy="41" rx="12" ry="10"/><ellipse cx="17" cy="29" rx="5" ry="6.5"/><ellipse cx="26.5" cy="19.5" rx="5" ry="6.5"/><ellipse cx="37.5" cy="19.5" rx="5" ry="6.5"/><ellipse cx="47" cy="29" rx="5" ry="6.5"/></g>'
               '<g fill="#2F4BEB" transform="rotate(14 48 22) translate(34 2) scale(.48)"><ellipse cx="32" cy="41" rx="12" ry="10"/><ellipse cx="17" cy="29" rx="5" ry="6.5"/><ellipse cx="26.5" cy="19.5" rx="5" ry="6.5"/><ellipse cx="37.5" cy="19.5" rx="5" ry="6.5"/><ellipse cx="47" cy="29" rx="5" ry="6.5"/></g></svg>')
DOODLE_BONE = ('<svg class="doodle" aria-hidden="true" focusable="false" viewBox="0 0 120 28">'
               '<g fill="#FF8A1F"><circle cx="8" cy="9" r="6"/><circle cx="8" cy="19" r="6"/><circle cx="44" cy="9" r="6"/><circle cx="44" cy="19" r="6"/><rect x="8" y="9" width="36" height="10" rx="5"/></g>'
               '<g fill="#2F4BEB" transform="translate(66 3) scale(.36)"><ellipse cx="32" cy="41" rx="12" ry="10"/><ellipse cx="17" cy="29" rx="5" ry="6.5"/><ellipse cx="26.5" cy="19.5" rx="5" ry="6.5"/><ellipse cx="37.5" cy="19.5" rx="5" ry="6.5"/><ellipse cx="47" cy="29" rx="5" ry="6.5"/></g>'
               '<g fill="#FF8A1F" transform="translate(92 3) scale(.36)"><ellipse cx="32" cy="41" rx="12" ry="10"/><ellipse cx="17" cy="29" rx="5" ry="6.5"/><ellipse cx="26.5" cy="19.5" rx="5" ry="6.5"/><ellipse cx="37.5" cy="19.5" rx="5" ry="6.5"/><ellipse cx="47" cy="29" rx="5" ry="6.5"/></g></svg>')
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fredoka:wght@600&family=Nunito:wght@400;700&display=swap">')

# SnoutsWise is a brand only (not a DBA); the publisher/organization is the LLC.
BRAND = {"@type": "Brand", "name": SITE_NAME, "url": SITE_URL, "logo": SITE_URL + "logo.png"}
ORG = {"@type": "Organization", "name": LEGAL_NAME, "legalName": LEGAL_NAME, "url": SITE_URL,
       "email": CONTACT_EMAIL, "logo": SITE_URL + "logo.png", "brand": BRAND}

PAGES = []      # filled by _content.py: dicts
SITEMAP = []    # (url, lastmod)


def esc(s):
    return html.escape(s, quote=True)


def strip_tags(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def nice_date(d):
    return datetime.date.fromisoformat(d).strftime("%-d %B %Y")


def page(path, title, desc, body, *, h1=None, lead=None, kind="article", faq=None, sources=None,
         related=None, crumbs=None, published=TODAY, updated=TODAY, nav=None, index=True, extra_head="",
         headline=None, script="", abs_links=False):
    PAGES.append(dict(path=path, title=title, desc=desc, body=body, h1=h1, lead=lead, kind=kind, faq=faq or [],
                      sources=sources or [], related=related or [], crumbs=crumbs, published=published,
                      updated=updated, nav=nav or path, index=index, extra_head=extra_head,
                      headline=headline or h1 or title, script=script, abs_links=abs_links))


def url_of(path):
    if path == "index.html":
        return SITE_URL
    if path.endswith("index.html"):
        return SITE_URL + path[:-len("index.html")]
    return SITE_URL + path


def render(p):
    depth = p["path"].count("/")
    R = SITE_URL if p["abs_links"] else "../" * depth
    canon = url_of(p["path"])
    graphs = []
    if p["path"] == "index.html":
        graphs.append({"@context": "https://schema.org", "@type": "WebSite", "name": SITE_NAME, "url": SITE_URL,
                       "publisher": ORG})
        graphs.append(dict({"@context": "https://schema.org"}, **ORG))
    elif p["kind"] in ("article", "post"):
        graphs.append({"@context": "https://schema.org", "@type": "BlogPosting" if p["kind"] == "post" else "Article",
                       "headline": strip_tags(p["headline"])[:110], "description": p["desc"],
                       "author": ORG,
                       "publisher": ORG, "datePublished": p["published"], "dateModified": p["updated"],
                       "image": SITE_URL + OG_IMAGE, "mainEntityOfPage": canon, "inLanguage": "en"})
    elif p["kind"] == "webpage":
        graphs.append({"@context": "https://schema.org", "@type": "WebPage", "name": strip_tags(p["headline"]),
                       "url": canon, "description": p["desc"], "publisher": ORG})
    if p["crumbs"]:
        items = [{"@type": "ListItem", "position": i + 1, "name": n, "item": url_of(u)} for i, (u, n) in enumerate(p["crumbs"])]
        graphs.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})
    if p["faq"]:
        graphs.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": strip_tags(q), "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a.replace("{R}", R))}}
            for q, a in p["faq"]]})
    ld = "".join('<script type="application/ld+json">%s</script>' % json.dumps(g, ensure_ascii=False) for g in graphs)
    for g in graphs:
        json.loads(json.dumps(g))

    nav = "".join('<a href="%s%s"%s>%s</a>' % (R, u, ' aria-current="page"' if (p["nav"] == u or (u == "blog/" and p["nav"].startswith("blog/"))) else "", esc(n)) for u, n in NAV)
    head = ['<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">']
    if GSC_TOKEN and p["path"] == "index.html":
        head.append('<meta name="google-site-verification" content="%s">' % GSC_TOKEN)
    head.append('<title>%s</title><meta name="description" content="%s">' % (esc(p["title"]), esc(p["desc"])))
    if p["index"]:
        head.append('<link rel="canonical" href="%s">' % canon)
    else:
        head.append('<meta name="robots" content="noindex">')
    head.append(FONTS + '<meta name="theme-color" content="#FFE600"><link rel="stylesheet" href="%sstyle.css"><link rel="icon" href="%sfavicon.svg" type="image/svg+xml">' % (R, R))
    head.append('<meta property="og:type" content="%s"><meta property="og:site_name" content="%s"><meta property="og:title" content="%s">'
                '<meta property="og:description" content="%s"><meta property="og:url" content="%s"><meta property="og:image" content="%s%s">'
                '<meta name="twitter:card" content="summary_large_image">' % ("article" if p["kind"] in ("article", "post") else "website",
                SITE_NAME, esc(p["title"]), esc(p["desc"]), canon, SITE_URL, OG_IMAGE))
    head.append(ld + p["extra_head"] + "</head><body>")
    out = ["".join(head)]
    out.append('<a class="skip" href="#main">Skip to content</a><header><a class="brand" href="%sindex.html">%s<span>%s</span></a>'
               '<button class="menu" aria-label="Menu" onclick="document.body.classList.toggle(\'open\')">&#9776;</button><nav aria-label="Main">%s</nav></header>' % (R, LOGO, SITE_NAME, nav))
    out.append('<main id="main">')
    if p["crumbs"]:
        out.append('<nav class="crumbs" aria-label="Breadcrumb">' + " &rsaquo; ".join(
            ('<a href="%s%s">%s</a>' % (R, u, esc(n)) if i < len(p["crumbs"]) - 1 else '<span>%s</span>' % esc(n))
            for i, (u, n) in enumerate(p["crumbs"])) + "</nav>")
    if p["h1"]:
        out.append("<h1>%s</h1>" % p["h1"])
    if p["kind"] in ("article", "post"):
        meta = "Last updated %s" % nice_date(p["updated"])
        if p["kind"] == "post":
            meta = "Published %s &middot; %s" % (nice_date(p["published"]), meta)
        out.append('<p class="meta">%s &middot; By the %s team</p>' % (meta, SITE_NAME))
    if p["lead"]:
        out.append('<p class="lead">%s</p>' % p["lead"])
    body = p["body"]
    if '<section class="hero">' in body:
        body = body.replace('<section class="hero">', '<section class="hero">' + DOODLE_PAWS + _photos.figure(p["path"], R, eager=True), 1)
    elif p["lead"] or p["h1"]:
        out.append(_photos.figure(p["path"], R))
    out.append(body)
    if p["faq"]:
        out.append('<section class="card" id="faq"><h2>Frequently asked questions</h2>' + "".join(
            "<h3>%s</h3><p>%s</p>" % (q, a) for q, a in p["faq"]) + "</section>")
    if p["related"]:
        out.append('<aside class="card related"><h2>Keep exploring</h2><ul>' + "".join(
            '<li><a href="{R}%s">%s</a></li>' % (u, esc(n)) for u, n in p["related"]) + "</ul></aside>")
    if p["sources"]:
        out.append('<section class="sources"><h2>Sources</h2><ol>' + "".join(
            '<li><a href="%s" rel="noopener">%s</a>, %s</li>' % (esc(u), esc(t), esc(pub)) for t, pub, u in p["sources"]) + "</ol></section>")
    if p["kind"] in ("article", "post") and p["path"] not in ("about.html",):
        out.append('<p class="note">General education only, not veterinary advice. If you are worried about your dog, contact your vet; in an emergency, contact an emergency vet straight away.</p>')
    out.append("</main>")
    out.append('<footer>' + DOODLE_BONE + '<section class="contact-us" aria-labelledby="cu"><h2 id="cu">Contact us</h2><p>Email <a href="mailto:%s">%s</a> or use our <a href="%scontact.html">contact form</a>.</p></section>'
               '<p class="flinks"><a href="%sterms.html">Terms</a> &middot; <a href="%sprivacy.html">Privacy</a> &middot; <a href="%sdisclaimer.html">Disclaimer</a> &middot; <a href="%scontact.html">Contact</a> &middot; <a href="%scredits/">Photo credits</a> &middot; <a href="%sabout.html">About</a> &middot; <a href="%sblog/">Blog</a> &middot; <a href="%ssitemap.xml">Sitemap</a></p>'
               '<p>%s: original educational content about dogs. All text and illustrations are original. Not a substitute for advice from your vet.</p>'
               '<p class="op">&copy; 2026 %s. All rights reserved. %s is owned and operated by %s.</p></footer>' % (CONTACT_EMAIL, CONTACT_EMAIL, R, R, R, R, R, R, R, R, R, SITE_NAME, LEGAL_NAME, SITE_NAME, LEGAL_NAME))
    if p["script"]:
        out.append("<script>%s</script>" % p["script"])
    if CF_BEACON_TOKEN:
        out.append("<!-- Cloudflare Web Analytics --><script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{\"token\": \"%s\"}'></script><!-- End Cloudflare Web Analytics -->" % CF_BEACON_TOKEN)
    out.append("</body></html>\n")
    doc = "\n".join(out).replace("{R}", R).replace("SITE_URL_PLACEHOLDER", SITE_URL)
    if "\u2014" in doc or "\u2013" in doc:
        raise SystemExit("dash found in %s" % p["path"])
    dest = os.path.join(ROOT, p["path"])
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as f:
        f.write(doc)
    if p["index"]:
        SITEMAP.append((canon, p["updated"]))


def write(name, text):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(text)


def extras():
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
          "".join("<url><loc>%s</loc><lastmod>%s</lastmod></url>\n" % (u, d) for u, d in SITEMAP + [(SITE_URL + "llms.txt", TODAY)]) + "</urlset>\n")
    bots = ["Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "GPTBot", "PerplexityBot", "Perplexity-User", "ClaudeBot",
            "Claude-SearchBot", "Claude-User", "Google-Extended", "Applebot", "Applebot-Extended", "DuckAssistBot", "Amazonbot"]
    # robots.txt is served at the custom domain root (https://snoutswise.com/robots.txt).
    write("robots.txt", "User-agent: *\nAllow: /\n\n" + "".join("User-agent: %s\nAllow: /\n\n" % b for b in bots) + "Sitemap: %ssitemap.xml\n" % SITE_URL)
    write(INDEXNOW_KEY + ".txt", INDEXNOW_KEY)
    write("indexnow.sh", """#!/usr/bin/env bash
# Ping IndexNow for https://snoutswise.com (host + keyLocation derived from SITE_URL). Usage: ./indexnow.sh URL [URL...]   (no args = every URL in the live sitemap)\n# Rule: after every publish/update, add URLs to the sitemap (rebuild), push, wait for Pages, then ping the changed https://snoutswise.com/ URLs.
# Reads SITE_URL and INDEXNOW_KEY from _build.py so a domain switch needs no edit here.
cd "$(dirname "$0")"
SITE=$(python3 -c 'import re;print(re.search(r"^SITE_URL = \\"([^\\"]+)",open("_build.py").read(),re.M).group(1))')
KEY=$(python3 -c 'import re;print(re.search(r"^INDEXNOW_KEY = \\"([^\\"]+)",open("_build.py").read(),re.M).group(1))')
HOST=$(python3 -c "from urllib.parse import urlparse;print(urlparse('$SITE').netloc)")
if [ $# -eq 0 ]; then set -- $(curl -s "${SITE}sitemap.xml" | grep -o '<loc>[^<]*' | sed 's/<loc>//'); fi
LIST=$(printf '%s\\n' "$@" | python3 -c 'import sys,json;print(json.dumps([l.strip() for l in sys.stdin if l.strip()]))')
curl -s -o /tmp/indexnow.out -w "IndexNow HTTP %{http_code} ($# URLs)\\n" -X POST https://api.indexnow.org/indexnow \\
  -H 'Content-Type: application/json; charset=utf-8' \\
  -d "{\\"host\\":\\"$HOST\\",\\"key\\":\\"$KEY\\",\\"keyLocation\\":\\"${SITE}${KEY}.txt\\",\\"urlList\\":$LIST}"
cat /tmp/indexnow.out; echo
""")
    os.chmod(os.path.join(ROOT, "indexnow.sh"), 0o755)


if __name__ == "__main__":
    import _content
    _content.register(page)
    _photos.register(page, [p["path"] for p in PAGES])
    for p in PAGES:
        render(p)
    extras()
    import _llms
    write("llms.txt", _llms.text(SITE_URL, SITE_NAME, LEGAL_NAME))
    print("built %d pages, %d sitemap urls" % (len(PAGES), len(SITEMAP) + 1))

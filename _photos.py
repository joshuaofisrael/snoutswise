"""Licensed photos (all opened and licence-checked on their Wikimedia Commons file pages, 9 Oct 2026).
Data lives in _photos.json; figures are injected by _build.py; /credits/ lists them all."""
import json, os, html
ROOT = os.path.dirname(os.path.abspath(__file__))
PHOTOS = json.load(open(os.path.join(ROOT, "_photos.json"), encoding="utf-8"))
BY_PAGE = {p["page"]: p for p in PHOTOS}
e = lambda s: html.escape(s, quote=True)

def credit(p, R):
    lic = e(p["licence"])
    if p["licence_url"]:
        lic = '<a href="%s" rel="noopener license">%s</a>' % (e(p["licence_url"]), lic)
    return 'Photo: <a href="%s" rel="noopener">%s</a>, %s, via Wikimedia Commons (cropped). <a href="%scredits/">All photo credits</a>' % (
        e(p["source"]), e(p["author"]), lic, R)

def figure(path, R, eager=False):
    p = BY_PAGE.get(path)
    if not p:
        return ""
    s = p["slug"]
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return ('<figure class="photo"><img src="{R}img/{s}-900.webp" srcset="{R}img/{s}-450.webp 450w, {R}img/{s}-900.webp 900w" '
            'sizes="(max-width: 820px) 92vw, {z}" width="900" height="600" alt="{a}" {l}><figcaption>{c}</figcaption></figure>').format(
            R=R, s=s, a=e(p["alt"]), l=load, c=credit(p, R), z="340px" if eager else "720px")

def register(page, live_paths):
    rows = "".join(
        '<tr><td><img src="{R}img/%s-450.webp" width="150" height="100" alt="%s" loading="lazy"></td><td><b>%s</b><br>Used on: <a href="{R}%s">%s</a></td>'
        '<td><a href="%s" rel="noopener">%s</a></td><td>%s</td><td>%s</td><td>%s</td></tr>' % (
            p["slug"], e(p["alt"]), e(p["title"]), p["page"].replace("index.html", ""), p["page"].replace("index.html", "") or "home",
            e(p["source"]), "Wikimedia Commons file page", e(p["author"]),
            ('<a href="%s" rel="noopener license">%s</a>' % (e(p["licence_url"]), e(p["licence"]))) if p["licence_url"] else e(p["licence"]),
            e(p["changes"])) for p in PHOTOS if p["page"] in live_paths)
    page("credits/index.html", "Photo Credits and Licences | SnoutsWise",
         "Every photo on SnoutsWise with its source, author and licence. All photos are public domain or Creative Commons licensed from Wikimedia Commons.",
         """
<p>Every photo on SnoutsWise is used under a free licence that allows commercial use. We opened each file's own page on Wikimedia Commons to check the licence before using it, and we credit each photographer here and in the caption under the photo. We cropped, resized and converted each photo to WebP; our edited versions are shared under the same licence as the original. Photos marked CC BY or CC BY-SA require attribution; public domain photos do not, but we credit them anyway.</p>
<div class="tablewrap"><table><thead><tr><th>Photo</th><th>File and page</th><th>Source</th><th>Author</th><th>Licence</th><th>Our changes</th></tr></thead><tbody>%s</tbody></table></div>
<h2>Illustrations, logo and games</h2><p>The logo, paw and bone doodles, icons and all game art are original drawings made for SnoutsWise by Joshua Israel Ventures LLC. Fonts are Fredoka and Nunito from Google Fonts, both under the SIL Open Font License.</p>
<p>If you believe a photo is credited incorrectly, please email <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a> and we will fix or remove it.</p>
""" % rows, h1="Photo credits", kind="webpage", crumbs=[("index.html", "Home"), ("credits/index.html", "Photo credits")])

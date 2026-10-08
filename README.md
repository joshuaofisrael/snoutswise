# SnoutsWise

Original, sourced dog information site (breeds, care, health, training, behavior). Operated by Joshua Israel Ventures LLC.

- Live: https://snoutswise.com/ (GitHub Pages custom domain; CNAME file in repo)
- Hosting: GitHub Pages, deploy from branch `main`, folder `/` (no Actions, no build on the server).
- Build: `python3 _build.py` regenerates all HTML, sitemap.xml, robots.txt, llms.txt and the IndexNow key file from `_content.py`, `_llms.py`.
- Domain: SITE_URL in `_build.py` is https://snoutswise.com/; CNAME contains snoutswise.com.
- Search Console: set `GSC_TOKEN` in `_build.py`. Cloudflare Web Analytics: set `CF_BEACON_TOKEN`.
- IndexNow: `./indexnow.sh` (all sitemap URLs) or `./indexnow.sh URL...` after every publish.
- Contact form: FormSubmit to joshuaofisrael@gmail.com.

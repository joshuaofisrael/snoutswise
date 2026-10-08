# SnoutsWise

Original, sourced dog information site (breeds, care, health, training, behavior). Operated by Joshua Israel Ventures LLC.

- Live (until a custom domain is set): https://joshuaofisrael.github.io/snoutswise/
- Hosting: GitHub Pages, deploy from branch `main`, folder `/` (no Actions, no build on the server).
- Build: `python3 _build.py` regenerates all HTML, sitemap.xml, robots.txt, llms.txt and the IndexNow key file from `_content.py`, `_llms.py`.
- Custom domain switch: edit `SITE_URL` in `_build.py`, add `CNAME` with the bare domain, rebuild, commit, push, then set the domain in Pages settings and enforce HTTPS.
- Search Console: set `GSC_TOKEN` in `_build.py`. Cloudflare Web Analytics: set `CF_BEACON_TOKEN`.
- IndexNow: `./indexnow.sh` (all sitemap URLs) or `./indexnow.sh URL...` after every publish.
- Contact form: FormSubmit to joshuaofisrael@gmail.com.

# Dog Field Guide SEO log

## 2026-10-08: v1 launch
Built as a sibling of SnakeWise (same plain static HTML approach, relative links, one CSS file), plus the gaps the Snake Bot playbook flagged: About, Contact, Privacy, blog, sources on every page, last updated dates, datePublished/dateModified/image in Article schema, og:image, BreadcrumbList, sitemap lastmod, no placeholder shop.
- Pages: home, breeds, care, health, training, behavior, can-dogs-eat (unique tool, about 70 foods), dog-age-calculator (tool), faq (FAQPage), glossary, about, contact, privacy, blog index + 5 posts.
- Unique assets: "Can dogs eat this?" searchable table with a source per row and deep links by category and food; dog age calculator (Wang et al. 2020 formula); chocolate dose estimator (Merck figures).
- Schema: WebSite + Organization (home), Article (pillars), BlogPosting (posts), FAQPage where visible FAQs exist, BreadcrumbList on all inner pages.
- robots.txt allows all listed AI and search crawlers + Sitemap line. NOTE: on a github.io project URL, robots.txt lives at /dogfieldguide/robots.txt and is not read by crawlers (they read the host root, which allows all by default). It becomes effective once the custom domain is live.
- IndexNow: key file at /dogfieldguide/<key>.txt with keyLocation; all sitemap URLs submitted (result below).

## Scorecard
| Date | Window | Impressions | Clicks | CTR | Avg pos | Indexed pages | Top100/20/10/3 queries | Growing pages | Declining pages | Conversions |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-08 | 7d | n/a (no GSC yet) | n/a | n/a | n/a | 20 URLs in sitemap | n/a | n/a | n/a | n/a |

## 2026-10-08 11:50 London: launch verification
- Pages builds: 5a453a7, 5102331, e07d34d all "built". All tested URLs 200; 404 page served for missing paths; seo-log.md, _build.py not published.
- Crawler UA check: 30/30 HTTP 200 (15 bots x home + can-dogs-eat).
- IndexNow: all 20 sitemap URLs submitted to api.indexnow.org, host joshuaofisrael.github.io, keyLocation /dogfieldguide/<key>.txt: HTTP 202 (accepted, key validation pending).
- Food lookup upgraded per mentor: Safe/Caution/Toxic verdicts, "Call your vet or ASPCA Animal Poison Control now: (888) 426-4435" (number verified on aspca.org) at top of every Caution and Toxic entry, "If eaten" advice, per entry "Last reviewed 8 Oct 2026" and sources.
- FormSubmit: one setup test submitted from the contact page; FormSubmit replied "This form needs Activation"; activation email sent to joshuaofisrael@gmail.com, pending click.

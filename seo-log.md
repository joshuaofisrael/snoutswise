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

## 2026-10-08 12:05 London: rebrand to SnoutsWise
- Site renamed Dog Field Guide -> SnoutsWise (titles, logo, copy, JSON-LD, OG/Twitter, OG image regenerated, llms.txt, footer, 404). Repo renamed joshuaofisrael/dogfieldguide -> joshuaofisrael/snoutswise; base URL now https://joshuaofisrael.github.io/snoutswise/ (old github.io path returns 404; GitHub does not redirect project Pages).
- Domain snoutswise.com pending purchase; no CNAME yet.
- IndexNow: all 21 sitemap URLs at the new base submitted: HTTP 202.

## 2026-10-08 12:35 London: custom domain snoutswise.com live
- DNS verified: apex A 185.199.108.153/109/110/111, www CNAME joshuaofisrael.github.io.
- CNAME file added; Pages custom domain set to snoutswise.com via API; SITE_URL = https://snoutswise.com/ and site rebuilt (canonicals, sitemap, robots Sitemap line, llms.txt, OG URLs, JSON-LD all on https://snoutswise.com/).
- Certificate approved about 12:32; https_enforced = true. http -> https, www -> apex and old github.io URLs all 301 to https://snoutswise.com/.
- robots.txt now effective at the host root.
- IndexNow: 21 sitemap URLs submitted for host snoutswise.com, keyLocation https://snoutswise.com/f82447b1414b64e38975376b34f684d7.txt: HTTP 202.
- FormSubmit: one setup test from https://snoutswise.com/contact.html; response "This form needs Activation", activation email sent to joshuaofisrael@gmail.com (pending click).

## 2026-10-08 14:30 London: light "cute" restyle + LLC legal pages
- Restyle (no URL, content or structure changes): cream #FFF8EC page, white #FFFFFF cards, peach #FFA27F and sunny yellow #FFD166 accents, header #FFE8D6, footer #FFEEDB, text #3B2A1F, muted #6B5444, headings #8F3A12, links #A13D14. Rounded 22px cards, pill buttons, soft shadows, dotted peach borders.
- Fonts: Google Fonts Fredoka 600 (headings) + Nunito 400/700 (body), display=swap, preconnect to fonts.googleapis.com and fonts.gstatic.com.
- New logo (brown paw on yellow badge with peach ring), favicon.svg, logo.png (9.9 KB), og-image.png (15 KB). Inline SVG paw and bone doodles (aria-hidden) in hero and footer.
- Food table: verdict cells now pill badges with icon + word + colour (Toxic #A1201A on #FFE0DA 6.18:1, Caution #7A4A00 on #FFF0BF 6.58:1, Safe #1D6A35 on #DCF3E2 5.67:1); poison-control call-out has a red left bar, phone icon, pink panel.
- WCAG check (/workspace/dog-site/contrast_check.py): every text/link/button pair passes AA; lowest 5.56:1 (link on header).
- Weight: style.css 4.0 -> 7.3 KB; home HTML 7.8 -> 10.1 KB; plus Google Fonts (2 families, 3 weights).
- LLC rule (SnoutsWise is a brand of Joshua Israel Ventures LLC, not a DBA): footer on every page "© 2026 Joshua Israel Ventures LLC. All rights reserved. SnoutsWise is owned and operated by Joshua Israel Ventures LLC." with Terms, Privacy, Disclaimer, Contact links; Contact us block kept.
- New pages: terms.html (LLC contracting party, general info only, as-is warranty disclaimer, limitation of liability, Florida law, brand owned by LLC) and disclaimer.html (accuracy, no vet relationship, emergency/APCC, no affiliate or ad links, FTC disclosure if that changes). Both in sitemap.xml and llms.txt.
- privacy.html rewritten: LLC is data controller; only GitHub Pages server logs, Google Fonts requests, FormSubmit contact form, email; no analytics, ads or affiliate cookies.
- About: "SnoutsWise is a brand of Joshua Israel Ventures LLC."
- JSON-LD: Organization name/legalName Joshua Israel Ventures LLC with brand {Brand: SnoutsWise}; WebSite publisher and Article author/publisher = the LLC.
- 8 Oct 14:30 London: governing law corrected to Florida (LLC is a Florida LLC, per Joshua via Personal assistant); venue state or federal courts located in Florida; no county named.
- Committed/pushed 9 Oct 2026 ~00:25 London (box freeze delayed the push). Pastel restyle ships as an interim look; neon photo redesign follows in a separate commit.

## 2026-10-09 00:45 London: NEON redesign with licensed photos (replaces pastel)
- Palette (own set, distinct from snakewise's dark purple/lime/cyan/pink neon): bright white base #FFFDF7 with soft lemon/blue/orange glow blobs; header gradient laser lemon #FFE600 -> #FFC21A -> tangerine #FF9A1F; electric blue #2F4BEB; ink #1A1633; muted #4A4566; headings #2A2BD1; links #1F3FD1; night footer #1A1633 with lemon links. Glowing cards/tiles (orange/blue/lemon box-shadow glows), gradient pill buttons, glow text-shadow on h1. Fonts unchanged (Fredoka 600 + Nunito 400/700). prefers-reduced-motion disables transitions/animations.
- WCAG AA: /workspace/dog-site/contrast_neon.py, 48 pairs, all pass, min 5.44:1 (Safe badge white on #0A7A3A). Badges: Toxic white on #B3001E pill (7.15:1, ✖), Caution ink on #FFE600 square-ish tag (13.73:1, ⚠), Safe white on #0A7A3A pill (5.44:1, ✔). Poison control call-out: pink panel, red bar, glow, phone icon.
- Logo/favicon/logo.png: electric blue paw on lemon badge with tangerine ring. OG image regenerated (19 KB).
- Photos: 8 live (home, breeds, care, health, training, behavior, can-dogs-eat, age calculator) + 2 staged for games/teachers. All from Wikimedia Commons; licence verified on each file page 9 Oct 2026 (CC BY 3.0/4.0, CC BY-SA 3.0/4.0, one public domain); no NC/ND, no people, no logos. Two Timothy A. Gonsalves photos rejected because the author asks to be contacted before commercial use. Self-hosted WebP 900x600 + 450x300 srcset, width/height set, lazy except home hero, real alt text, caption attribution + new /credits/ page (footer link).
- privacy.html: photo self-hosting note + "governed by the laws of the State of Florida"; disclaimer.html: Florida line.

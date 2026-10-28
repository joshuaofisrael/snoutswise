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

## 2026-10-09 London: Dog games (/games/)
- New: /games/ hub, /games/snack-or-nope/, /games/wag-signals/, /games/fetch-spotter/ (+ games/games.css, games/dog.js, games/CREDITS.md). Linked from home Tools grid and main nav; in sitemap and llms.txt.
- All assets original (inline SVG and code by SnoutsWise; sounds generated with WebAudio). Hub photo: Wikimedia Commons "Viljo koirarannalla 11.jpg" by kallerna, CC BY-SA 3.0, credited on /credits/.
- Privacy: no sign up, ads, cookies, trackers or data collection; best score only in localStorage on the device; sound off by default with mute toggle; keyboard + touch; prefers-reduced-motion respected. privacy.html updated with a games paragraph.
- JSON-LD: VideoGame (author/publisher/copyrightHolder Joshua Israel Ventures LLC) + BreadcrumbList; hub ItemList. Line "Games are original works © 2026 Joshua Israel Ventures LLC." on hub and each game.
- Facts: Snack or Nope? uses the food table's sources (ASPCA, AKC, Merck); Wag Signals uses RSPCA body language page and ASPCApro Canine Body Language Tips (both opened 8 Oct); Fetch Spotter uses AKC "Can Dogs See Color?" and ASPCApro (opened 8 Oct).
- Trademark checks (USPTO tmsearch wordmark search + web search, 8 Oct 2026):
  - "Snack or Nope?": USPTO "snack or nope" 0 records; snack* AND nope* 0 records; web: no game or product of that name found.
  - "Wag Signals": USPTO "wag signals" 0; wag* AND signal* 0; web: no match.
  - "Fetch Spotter": USPTO "fetch spotter" 0; fetch* AND spot* finds SEE SPOT FETCH (dead, IC 044), FETCH YOUR NEW BEST FRIEND AT PUPPYSPOT (dead, IC 035), SPOT. TRACK. FETCH! (live, IC 035, services, different wording); web: only a fictional app in a design case study.
  - Rejected: "Snack Sorter" (live USPTO mark SORT & SNACK, IC 021); "Bowl Patrol" (existing junior bowling program; echoes PAW Patrol).
  - Not legal advice; a knockout search only.

## 2026-10-09 London: Teachers hub, research page, citations
- New: /teachers/ (lesson ideas by grade band, vocabulary, games as activities), /teachers/dog-needs-worksheet.html (K-2, K-LS1-1), /teachers/dog-senses-fact-sheet.html (3-5, 4-LS1-2), /teachers/dog-traits-worksheet.html (3-8, 3-LS3-1 + MS-LS4-5), /research/ (5 papers, DOIs checked on Crossref; 4 guidelines). Print CSS; no ads. NGSS text quoted from nextgenscience.org (opened 8 Oct).
- LearningResource JSON-LD with educationalLevel, educationalAlignment (NGSS) and publisher Joshua Israel Ventures LLC. Research page: ItemList of ScholarlyArticle with DOI sameAs.
- Fact articles and posts: "Last reviewed" date shown; "Cite this page" box (APA, MLA, Chicago).
- Footer gains Teachers and Research links; home Tools grid gains "For teachers".
- Outreach (local only, gitignored, NOTHING SENT): outreach/edu-targets.csv (18 rows), edu-template.md, teacher-directories.md, pinterest-drafts.md.

## 2026-10-11 00:15 London: daily SEO action (internal linking + accurate lastmod for the grass cluster)
- Data: no Search Console/Bing data yet (GSC tag still pending), so ranked by the operator's priority list. Audit of main-content internal links showed today's new post (blog/why-do-dogs-eat-grass.html) had only 2 inbound links (home, blog index) and can-dogs-see-color had no pillar-page link; and sitemap lastmod is pinned to TODAY="2026-10-08" in _build.py, so changed pages kept a stale lastmod (Bing leans on lastmod).
- Action: (1) FAQ page gains two sourced Q&As (Why does my dog eat grass? / Can dogs see color?) in visible FAQ + FAQPage JSON-LD (now 14 Qs), linking to the posts; (2) behavior.html #problems gains a contextual paragraph linking the grass article, related links add grass + color posts, sources add Sueda 2008; (3) health.html related links add the grass article; (4) per-page updated="2026-10-11" only on pages genuinely changed today (home, health, behavior, faq, blog index, new post) so dateModified and sitemap lastmod are accurate; other pages untouched (no manufactured freshness); (5) new post meta description cut from 202 to about 150 chars to avoid truncation.
- Rationale: a new page answering a high-volume question ("why do dogs eat grass") gets discovered and weighted faster with links from pillar/FAQ pages and accurate lastmod; FAQ Q&A gives AI search engines a short citable answer.
- IndexNow: 8 changed URLs, HTTP 200 (00:16 London).
- Next: other posts' meta descriptions are 169 to 214 chars (can-dogs-see-color 214, blog index 211); trim in a later session. Consider replacing hard-coded TODAY with per-page dates everywhere.

## 2026-10-12 00:13 London: daily SEO action (meta descriptions for all blog posts)
- Data: still no Search Console/Bing data (GSC tag pending), so ranked by operator priority list. Technical check first: live robots.txt Allow all, sitemap and llms.txt include the new post, new post 200, no noindex. No serious indexing problem found, so took the item flagged "Next" on 11 Oct.
- Action: rewrote 6 overlong blog meta descriptions (169 to 214 chars) to 140 to 148 chars, each leading with the question/answer: can-dogs-see-color (214 -> 142), is-my-dog-overweight (182 -> 140), alpha-dog-myth (177 -> 141), dog-vaccine-schedule (176 -> 147), dog-ate-chocolate (171 -> 148), puppy-socialization-window (169 -> 140). Blog index description cut from 211 to about 140 and now names the new head-tilt post. New post (why-do-dogs-tilt-their-heads) written at 149.
- No dateModified/lastmod bump for the 6 posts (meta only, not content; no manufactured freshness). Changed-content pages today: home, blog index, behavior (new contextual head-tilt paragraph + related link + Sommese source), new post.
- Rationale: descriptions over ~155 chars get truncated in Google/Bing snippets, cutting off the answer; an answer-first snippet should raise CTR once impressions arrive and gives AI engines a clean summary.
- Commits: 2d82024 (article + behavior link + blog index meta), a1361ec (6 post metas). IndexNow: 6 URLs HTTP 200 + 6 URLs HTTP 200 (00:13 London).
- Next: page title lengths audit (several over 60 chars); add a head-tilt Q&A to faq.html; replace hard-coded TODAY default in _build.py with per-page dates.

## 2026-10-13 00:15 London: daily SEO action (FAQ + internal links for dream / head-tilt cluster)
- Data: still no Search Console/Bing data (GSC tag pending), so ranked by operator priority. Technical check: new post built with FAQPage JSON-LD, sitemap and llms.txt include it. Highest EV after a new article is inbound links from pillars/FAQ plus accurate lastmod (same pattern as 11 Oct grass cluster), and the prior "Next" note to add a head-tilt FAQ Q&A.
- Action (single cluster): (1) faq.html gains two sourced Q&As (Why do dogs tilt their heads? / Do dogs dream?) in visible FAQ + FAQPage JSON-LD (now 16 Qs), linking to both posts; (2) behavior.html #problems gains a REM/twitch contextual paragraph linking the dream article, related links add dream post, sources add Kis 2014/2017; (3) training.html gains a quiet-rest-after-learning sentence linking the dream article, related + kis2017 source; (4) health.html related adds dream post; (5) per-page updated="2026-10-13" only on pages genuinely changed (faq, behavior, training, health, plus article commit's home/blog index).
- Rationale: new high-interest query page ("do dogs dream") gets discovered faster with pillar/FAQ inbound links and accurate lastmod; FAQ Q&As give AI/search engines short citable answers for both today's and yesterday's topics.
- IndexNow: 9 URLs (dream post, blog index, home, faq, behavior, training, health, llms.txt, sitemap.xml), HTTP 200 (00:16 London).
- Next: page title lengths audit (several over 60 chars); replace hard-coded TODAY default in _build.py with per-page dates everywhere.

## 2026-10-14 00:15 London: daily SEO action (FAQ + internal links for jealousy cluster)
- Data: still no Search Console/Bing data (GSC tag pending). Highest EV after today's new post is inbound links from pillar/FAQ plus accurate lastmod (same pattern as dream/grass clusters).
- Action (single cluster): (1) faq.html gains one sourced Q&A (Do dogs feel jealousy?) in visible FAQ + FAQPage JSON-LD (now 17 Qs), linking the post; (2) behavior.html #problems gains a jealousy-like contextual paragraph linking the post, related links add the post, sources add Harris 2014 and Abdai 2018; (3) per-page updated="2026-10-14" only on pages genuinely changed (home, faq, behavior, blog index, new post).
- Rationale: new high-interest query page ("do dogs feel jealousy") gets discovered faster with pillar/FAQ inbound links and accurate lastmod; FAQ Q&A gives AI/search engines a short citable answer.
- News: no relevant dog news today (no solid two-source story found in slot).
- Outreach emails: skipped (no Joshua yes this run).
- IndexNow: 7 URLs (jealousy post, blog index, home, faq, behavior, llms.txt, sitemap.xml), HTTP 200 (00:16 London).
- Next: page title lengths audit; replace hard-coded TODAY default in _build.py with per-page dates everywhere.

## 2026-10-15 00:14 London: daily SEO action (FAQ + stress-table internal links for yawning cluster)
- Data: still no Search Console/Bing data. Highest EV after today's new post is inbound links from pillar/FAQ plus accurate lastmod (same pattern as previous clusters).
- Article: blog/why-do-dogs-yawn.html (Joly-Mascheroni 2008, Harr 2009, Romero 2013, Madsen 2013 DOIs verified via Crossref and abstracts read; AVSAB stress list).
- Action (single cluster): (1) faq.html gains a sourced Q&A (Why do dogs yawn?) in visible FAQ + FAQPage JSON-LD (now 18 Qs); (2) behavior.html stress-signal table yawning row links the post, related links add it, sources add Joly 2008 and Romero 2013; (3) home latest list and llms.txt include it; updated="2026-10-15" only on pages genuinely changed (home, faq, behavior, blog index).
- News: blog/big-dogs-age-faster-dna-study.html on Mariner et al., Science 8 Oct 2026 (DOI 10.1126/science.aeb2986 verified via Crossref; figures from the paper's abstract) plus ASU News release (opened); links dog age calculator and weight post.
- Outreach emails: skipped (no Joshua yes saved).
- IndexNow: 8 URLs, see below.
- Next: page title lengths audit; replace hard-coded TODAY default in _build.py with per-page dates.
- IndexNow result:  00:13

## 2026-10-16 00:14 London: daily SEO action (title length audit)
- Data: still no Search Console/Bing query data. Highest EV deferred item was the title length audit: 25 pages had titles over 60 chars, so Google was truncating them in results.
- Action: shortened 10 titles in _content.py to about 49-61 chars while keeping the main query words and the SnoutsWise brand (behavior, health, care, training, dog age calculator, and the overweight, alpha, chocolate, vaccine and socialization posts).
- Article: blog/can-dogs-smell-fear.html (Wilson 2022 PLOS ONE, D'Aniello 2018 Anim Cogn, Parr-Cortes 2024 Sci Rep; DOIs verified via Crossref, abstracts read). Linked from home latest, blog index, behavior related links, llms.txt.
- News: blog/dogs-bouba-kiki-effect-study.html on Biffi et al., Proc R Soc B 14 Oct 2026 (DOI 10.1098/rspb.2026.1209 verified via Crossref, abstract read) plus New Scientist 14 Oct 2026 (opened).
- Outreach emails: skipped (no Joshua yes saved in my chat).
- IndexNow: 17 URLs (two new posts, blog index, home, retitled pages, llms.txt, sitemap.xml), HTTP 200 (00:13 London).
- Next: shorten the remaining long titles in _edu.py/_games.py (teachers, research, games) and the faq/breeds/grass/tilt/yawn titles; replace hard-coded TODAY default in _build.py with per-page dates.

## 2026-10-18 00:13 London: daily SEO action (FAQ + training inbound link for pointing cluster)
- Data: still no Search Console/Bing query data. Highest EV after today's new post is inbound links from FAQ and the most relevant pillar plus accurate lastmod (same pattern as earlier clusters).
- Article: blog/do-dogs-understand-pointing.html (Hare et al. 2002 Science, Bray et al. 2021 Curr Biol, Salomons et al. 2021 Curr Biol; DOIs verified via Crossref, abstracts read via Crossref/PubMed). Linked from home latest, blog index, llms.txt.
- Action (single cluster): faq.html gains a sourced Q&A (Do dogs understand pointing?) in visible FAQ + FAQPage JSON-LD; training.html related links add the post and sources add Bray 2021; updated="2026-10-18" only on pages genuinely changed (home, blog index, faq, training).
- News: blog/dog-dementia-brain-study.html on Alsulami et al., npj Dementia 6 Oct 2026 (DOI 10.1038/s44400-026-00141-4 verified via Crossref, abstract read) plus UW Medicine Newsroom release (opened); links health, dog age calculator and big-dogs-age post.
- Outreach emails: skipped (no Joshua yes saved in my chat; also Sunday). Reframed outreach/edu-template.md draft to pitch SnoutsWise as a serious, cited resource on dog biology, behavior, health and care.
- Commits: d854db1 (article + SEO), e9b6536 (news). IndexNow: 8 URLs HTTP 200 + blog/index.html HTTP 200 (00:10 London).
- Next: shorten remaining long titles in _edu.py/_games.py and the faq/breeds/grass/tilt/yawn titles; replace hard-coded TODAY default in _build.py with per-page dates.

## 2026-10-19 00:11 London: daily SEO action (finish title length audit + drinking cluster links)
- Data: still no Search Console/Bing query data. Highest EV unfinished checklist item was the rest of the title audit: 11 more titles were over 60 chars and getting truncated in results.
- Action: shortened 11 titles to 44-55 chars (faq, breeds, grass, tilt, yawn, games hub, research, teachers hub and three teacher worksheets) keeping the main query words and brand.
- Article: blog/how-do-dogs-drink-water.html (Gart et al. 2015 PNAS, Crompton & Musinsky 2011 Biol Lett, Reis et al. 2010 Science; DOIs verified via Crossref, abstracts read). Linked from home latest, blog index, care related links, a new FAQ Q&A (visible + FAQPage JSON-LD) and llms.txt; updated="2026-10-19" only on pages genuinely changed.
- News: none. Best candidate (CANID cognitive test, Animal Cognition 12 Oct 2026, DOI 10.1007/s10071-026-02112-x) only had aggregator coverage as a second source and overlaps yesterday's dementia post, so skipped for quality.
- Outreach emails: skipped (no Joshua yes saved in my chat).
- Commit 6fcb877. IndexNow: 17 URLs HTTP 200 (00:10 London).
- Next: meta descriptions over 160 chars (privacy, teachers worksheets, behavior, glossary, faq, care, age calculator, wag signals); add the new DOIs to the research page if it is not auto-built from sources; replace hard-coded TODAY default in _build.py with per-page dates.

## 2026-10-20 00:17 London: daily SEO action (meta description length audit + tail wagging cluster)
- Data: still no Search Console/Bing query data. Highest EV unfinished checklist item was meta descriptions over 160 chars, which Google truncates in results.
- Action: shortened all 10 meta descriptions over 160 chars to 147-159 (behavior, care, dog age calculator, faq, wag signals game, glossary, privacy, teachers hub and two teacher sheets); a site-wide check now finds none over 160, the beacon and LLC footer on every page and no Michigan text.
- Article: blog/why-do-dogs-wag-their-tails.html (Leonetti et al. 2024 Biol Lett, open full text read; Siniscalchi et al. 2013 Curr Biol, abstract read via PubMed; Quaranta et al. 2007 Curr Biol, DOI verified via Crossref, findings reported as summarised by the 2024 review since the publisher page was behind a bot check). Linked from home latest, blog index, behavior related links, a new FAQ Q&A (visible + FAQPage JSON-LD) and llms.txt; updated="2026-10-20" only on pages genuinely changed.
- News: none tonight (lean pacing until the 22 Oct usage reset; no candidate verified in the slot).
- Outreach emails: skipped (no Joshua yes saved in my chat).
- Commit a449506. IndexNow: 15 URLs HTTP 200 (00:17 London).
- Next: add the new DOIs to the research page if it is not auto-built from sources; replace hard-coded TODAY default in _build.py with per-page dates; feeding calculator hub after 22 Oct.

## 21 Oct 2026
- Daily fact: do-dogs-recognize-themselves-in-mirror (Horowitz 2017 Behav Processes, Gallup 1970 Science; DOIs verified via Crossref/PubMed). FAQ Q&A schema, linked from home, blog index, llms.txt.
- Usage hold until 22 Oct reset: no SEO extras, no news post, no outreach, no browser.

## 23 Oct 2026
- Design, first step: 9 AI generated photo style images (hyper realistic dogs, no people, no text, WebP 1280x720, 29 to 108 KB) added with width/height, descriptive alt, lazy loading, honest "AI generated image" caption, and CSS polish (16:9 rounded card, soft shadow, responsive, reduced motion safe). Pages: the 5 newest articles (mirror, tail wag, drinking water, pointing, smell fear) plus blog index, FAQ, glossary, research. og:image (with width/height) and Article JSON-LD image now point to the page image on these pages. The 10 hub pages already had licensed Wikimedia photos. Credits page notes the AI images.
- Contact form checked: honeypot, thanks redirect, footer link on all pages OK; added a how-messages-are-used line. Form action unchanged (no FormSubmit alias switch, needs Joshua activation).
- Remaining without photos: older 14 articles, about, contact, contact-thanks, terms, privacy, disclaimer, 3 games, 3 teacher worksheets, credits.
- 23 Oct 2026 AdSense prep (Joshua approved via PA): added AdSense script and google-adsense-account meta to the head of every page (client ca-pub-5681559774142917, no ad units), ads.txt at root, Advertising, CCPA and EU/UK/Swiss consent section on privacy, and updated about, disclaimer, games, teachers and llms.txt wording that said no ads. No separate consent banner. IndexNow for privacy and home.

## 24 Oct 2026
- LLC rule: Joshua Israel Ventures LLC now appears only on terms, privacy, disclaimer and photo credits, each legal page with an ownership line (Florida LLC, Terms keep Florida law). Footer is "© 2026 SnoutsWise. All rights reserved." with Terms, Privacy, Disclaimer and Contact links. JSON-LD publisher and author, og:site_name and meta author are SnoutsWise; about, contact, teacher sheets, games and llms.txt no longer name the LLC. AdSense tags, ads.txt and the beacon kept. Commit d9860fa, live checked.
- Audit: one reusable "When to get veterinary help" block added to health, care, can dogs eat and 6 health related articles. ASPCA APCC (888) 426-4435 and Pet Poison Helpline (855) 764-7661 checked on their official sites today; no UK numbers given, UK readers told to call their vet. Last reviewed dates already shown on every article from dateModified. 67 source links checked: all resolve; 15 publisher sites (Merck, DOI publishers, Penn Today, Europe PMC, New Scientist) block scripted requests, and all 9 DOIs are registered at doi.org. Internal links: none broken. Every indexable page has a canonical. IndexNow for the full sitemap.

## 25 Oct 2026
- Daily fact: blog/can-dogs-sense-heat-with-their-nose.html (Bálint et al. 2020 Scientific Reports, DOI 10.1038/s41598-020-60439-y verified via Crossref, abstract read via Europe PMC). Article and FAQPage JSON-LD, linked from home latest, blog index, sitemap and llms.txt; internal links to behavior, health and three related articles.
- SEO: new long-tail query page with internal links and IndexNow ping; checklist extras held for the short slot (slot started 00:13).
- News: none (no verified candidate in the slot). Outreach emails: skipped (no Joshua yes saved in my chat). No browser use, no expenses.

## 26 Oct 2026
- Daily fact: blog/can-dogs-learn-toy-names.html (Fugazza et al. 2021 Scientific Reports 11:2222, DOI 10.1038/s41598-021-81699-2 verified via Crossref, abstract read via Europe PMC). Article and FAQPage JSON-LD, linked from home latest, blog index, sitemap and llms.txt.
- SEO: two-way internal linking with the head-tilt article (topic cluster on dog word learning); fixed a source-key collision before publish so the head-tilt article keeps its own Fugazza 2021 citation.
- News: none (no verified candidate in the slot). Outreach emails: skipped (no Joshua yes saved in my chat). No browser use, no expenses.
- 2026-10-26 09:05 slot: NamedScan fixes (commit b6e077b): visible SnoutsWise Editorial Team byline linking to about, Article/BlogPosting author is Organization SnoutsWise Editorial Team; no sameAs since no verified profiles; AdSense, ads.txt, Cloudflare untouched; live verified.

## 27 Oct 2026
- Daily fact: blog/do-dogs-like-baby-talk.html (Ben-Aderet et al. 2017 Proc R Soc B 284: 20162429, DOI 10.1098/rspb.2016.2429; Benjamin & Slocombe 2018 Animal Cognition 21: 353-364, DOI 10.1007/s10071-018-1172-4; both DOIs verified via Crossref, abstracts read via Europe PMC). Article and FAQPage JSON-LD, linked from home latest, blog index, sitemap and llms.txt.
- SEO: grew the dog word-learning topic cluster (baby talk, toy names, head tilt) with two-way internal links; new People Also Ask style FAQ targets "do dogs like baby talk".
- News: none (no verified candidate in the slot). Outreach emails: skipped (no Joshua yes saved in my chat). No browser use, no expenses.
- SEO push (one time, commit b85642a): new evergreen tool page how-much-to-feed-a-dog.html (target "how much to feed a dog by weight" / "dog calorie calculator"; Google autocomplete 27 Oct shows by weight, by weight kg, per day chart, calculator, to lose weight, puppy, rer formula). Calorie calculator (RER 70 x kg^0.75 x AAHA 2021 life stage factors, cups or grams from the label, 10 percent treat budget), lb and kg charts, AAHA vs Merck factor table, NRC 2006 owner table cross check (inactive and active rows within 0.5 percent of 95 and 130 x kg^0.75). Sources opened and read: Merck Vet Manual nutritional requirements, AAHA 2021 Box 1 PDF and feeding plans page, Cline et al. 2021 JAAHA 57(4):153-178 DOI 10.5326/JAAHA-MS-7232 and WSAVA 2011 JSAP 52(7):385-396 DOI 10.1111/j.1748-5827.2011.01079.x (both via Crossref; WSAVA PDF read), NRC owner booklet PDF. Article, FAQPage and Breadcrumb JSON-LD, byline, vet help block, Commons photo (CC BY-SA 2.0, credited; no free AI image tool available without spending).
- Internal links to the new page: home hero and Tools tile, care #feeding and related, health #weight and related, is-my-dog-overweight, dog-age-calculator, can-dogs-eat, FAQ; terms and disclaimer now name the feeding calculator.
- Titles and meta rewritten from autocomplete (all titles 60 or fewer, descriptions 150 to 160): home, breeds, care, health, training, behavior, can-dogs-eat, faq, blog index. Live checked; AdSense, ads.txt, Cloudflare beacon intact. IndexNow 17 URLs HTTP 200.

## 28 Oct 2026
- Daily fact: blog/why-do-dogs-make-puppy-dog-eyes.html (Kaminski et al. 2019 PNAS 116(29): 14677-14681, DOI 10.1073/pnas.1820653116; Kaminski et al. 2017 Scientific Reports 7: 12914, DOI 10.1038/s41598-017-12781-x; both DOIs verified via Crossref, abstracts read via Europe PMC). Article and FAQPage JSON-LD, linked from home latest, blog index, sitemap and llms.txt.
- SEO: new dog-human communication cluster link (two-way with baby talk, plus tilt-head related list); internal link to the feeding calculator page to pass authority to the new tool page.
- Legal hold check against RULE.md: no hold rule hit (no allegations, no personal info, no images, claims sourced and framed as hypothesis where the authors do). News: none. Outreach: skipped (no Joshua yes saved in my chat). No browser, no expenses.

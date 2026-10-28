#!/usr/bin/env python3
"""SnoutsWise pre-publish legal-hold gate (JI Ventures rule, Joshua 27 Oct 2026; /workspace/content-review/RULE.md,
with Amendment 1 severity tiers and Amendment 2 rework rounds). Mirrors the SnakeWise gate.
Called by _build.py after every build (held pages are removed from the site and saved as HOLD_REVIEW drafts)
and by the git pre-push hook (_hooks/pre-push), so no route publishes a flagged page.
Usage:
  _hold_check.py check FILE...                 exit 0 = pass, 3 = HOLD_REVIEW (prints reasons)
  _hold_check.py hold FILE TITLE               move FILE to drafts as HOLD_REVIEW + append queue.jsonl
  _hold_check.py moderate FILE "rule + fix" [TITLE]   independent ChatGPT review of a MODERATE item; exit 0 = cleared
Approval: a held item publishes only if /workspace/content-review/approvals.jsonl has
{"site":"snoutswise.com","sha256":<sha256 of the exact file>,"approved_by":"Joshua..."}; bots never write that.
SEVERITY: HIGH = rules 1, 2, 6, 8 (Joshua only, never self-cleared). MODERATE = rules 3, 4, 5, 7: fix first; the objective
detectors (3 licence record, 4 sources) must stop firing; remaining tripwires (5, 7) go to chatgpt_review.py and a SAFE
verdict is logged to moderate-clearances.jsonl tied to the exact sha256. Up to 3 rework rounds, then report to Personal assistant.
CODE ENFORCED: 2 (email, phone, street address patterns), 3 (every img/video needs a licence record in _photos.json, _aiimg.py
or credits; remote media and iframes held), 4 (blog posts and drafts must link at least one external source), 6 (election
wording), 8 (notice or embargo wording plus restrictions list), keyword tripwires for 1, 5, 7, edits after a clearance or approval.
JUDGEMENT ONLY: defamation beyond keywords (1), accuracy of a cited source (4), personalised advice beyond keywords (5),
headline strength and implied endorsement beyond keywords (7)."""
import sys, os, re, json, hashlib, datetime, shutil, html as H
ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = "snoutswise.com"; BOT = "Dog Site Bot (SnoutsWise)"
CR = "/workspace/content-review"; Q = CR + "/queue.jsonl"; AP = CR + "/approvals.jsonl"; DR = CR + "/drafts/snoutswise"
MC = CR + "/moderate-clearances.jsonl"; REVIEW = CR + "/bin/chatgpt_review.py"
RESTRICT = CR + "/restrictions-snoutswise.txt"  # one slug or path per line: blocked from (re)publication
OWN_DOMAINS = ("snoutswise.com", "schema.org", "googletagmanager.com", "googlesyndication.com", "google.com", "formsubmit.co",
               "fonts.googleapis.com", "fonts.gstatic.com", "w3.org", "cloudflareinsights.com", "creativecommons.org")
SITE_EMAIL_OK = ("@snoutswise.com", "joshuaofisrael@gmail.com")
PHONE_OK = ("888 426 4435", "855 764 7661")  # ASPCA APCC and Pet Poison Helpline, verified on official sites 24 Oct 2026
HIGH = {1, 2, 6, 8}; MODERATE = {3, 4, 5, 7}; OBJECTIVE = {3, 4}
KW = {
 1: r"\b(fraud\w*|scam\w*|corrupt\w*|embezzl\w*|arrested|indicted|charged with|convicted|lawsuit|sued|misconduct|dishonest\w*|cover-?up|criminal|puppy mill|negligen\w*)\b",
 5: r"\b(you should (give|inject|stop|start)|give (your dog )?\d+(\.\d+)? ?(mg|ml|tablets?)|(recommended|safe|human) dos(e|age)|induce vomiting at home|hydrogen peroxide|invest(ment|ing)?|guaranteed returns?|tax advice|legal advice)\b",
 6: r"\b(election|ballot|polling (place|station)|voter registration|vote by|voting day|certified results?|electoral)\b",
 7: r"\b(official partner|endorsed by|in partnership with|certified by|approved by the|vet approved|clinically proven|proves that|miracle|cures? (cancer|arthritis|anxiety)|100% (safe|accurate))\b",
 8: r"\b(embargo(ed)?|cease and desist|dmca|takedown notice|legal notice|reporting restriction|correction request)\b",
}
def now(): return datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def txt(h): return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", h, flags=re.S | re.I)))).replace("\u2011", "-")
def sev(R): return "HIGH" if any(n in HIGH or n == 0 for n, _, _ in R) else ("MODERATE" if R else None)
def _lines(p):
    if not os.path.exists(p): return []
    out = []
    for l in open(p, encoding="utf-8"):
        try: out.append(json.loads(l))
        except Exception: pass
    return out
def approved(p):
    h = sha(p)
    return any(j.get("sha256") == h and j.get("site") in (SITE, "SnoutsWise") and str(j.get("approved_by", "")).lower().startswith("joshua") for j in _lines(AP))
def moderate_cleared(p, R=None):
    R = check(p) if R is None else R
    if not R or sev(R) != "MODERATE" or any(n in OBJECTIVE for n, _, _ in R): return False
    h = sha(p)
    return any(j.get("site") == SITE and j.get("sha256") == h and str(j.get("chatgpt_verdict", "")).upper().startswith("SAFE") for j in _lines(MC))
def licensed():
    ok = set()
    try: ok |= {d["slug"] for d in json.load(open(os.path.join(ROOT, "_photos.json"))) if d.get("licence") and d.get("source")}
    except Exception: pass
    try:
        sys.path.insert(0, ROOT); import _aiimg; ok |= {v[0] for v in _aiimg.AI.values()}  # own AI images, captioned and credited
    except Exception: pass
    return ok
def check(path):
    h = open(path, encoding="utf-8", errors="replace").read(); t = txt(h); R = []
    for n, rx in KW.items():
        for m in re.finditer(rx, t, re.I):
            if n == 5 and re.search(r"\b(not|never|don'?t|do not|avoid|without)\b[^.]{0,40}$", t[max(0, m.start() - 60):m.start()], re.I): continue
            R.append((n, m.group(0), "keyword tripwire; review")); break
    for m in re.finditer(r"[\w.+-]+@[\w-]+\.[\w.]+", t):
        if not m.group(0).lower().rstrip(".").endswith(SITE_EMAIL_OK): R.append((2, m.group(0), "personal email address")); break
    for m in re.finditer(r"(?<![\w/.:-])(\+\d{1,3}[\s-]?)?\(?(\d{3})\)?[\s-](\d{3})[\s-](\d{4})(?![\w-])", t):
        if " ".join(m.group(2, 3, 4)) in PHONE_OK: continue
        R.append((2, m.group(0).strip(), "possible phone number")); break
    m = re.search(r"\b\d{1,5}\s+[A-Z][a-z]+(\s[A-Z][a-z]+)*\s(Street|St|Road|Rd|Drive|Dr|Avenue|Ave|Lane|Ln|Court|Ct|Boulevard|Blvd)\b", t)
    if m: R.append((2, m.group(0), "possible street address"))
    lic = licensed()
    for src in re.findall(r"<(?:img|source|video)[^>]+src(?:set)?=\"([^\" ]+)", h, re.I):
        s = re.sub(r"^https?://(www\.)?snoutswise\.com/", "", src)
        if s.startswith("data:image/svg"): continue
        slug = re.sub(r"(-\d{3,4})?\.(webp|jpe?g|png|gif|avif)$", "", os.path.basename(s))
        if s.startswith("http") or slug not in lic:
            R.append((3, src, "no documented licence record: add to _photos.json with source and licence, or drop the image"))
    for src in re.findall(r"<iframe[^>]+src=\"([^\"]+)", h, re.I): R.append((3, src, "embedded third party media"))
    ap = os.path.abspath(path)
    if os.path.basename(path) != "index.html" and ("/blog/" in ap or ap.startswith(DR) or "/drafts/" in ap):
        ext = [u for u in re.findall(r"href=\"(https?://[^\"]+)", h) if not any(d in u for d in OWN_DOMAINS)]
        if not ext: R.append((4, "(no external source links)", "post cites no source actually accessed"))
    for l in (open(RESTRICT).read().split("\n") if os.path.exists(RESTRICT) else []):
        l = l.strip()
        if l and not l.startswith("#") and (l in path or l == os.path.basename(path).rsplit(".", 1)[0]): R.append((8, l, "listed restriction or complaint")); break
    return R
def blocked(p):
    R = check(p); return (R and not approved(p) and not moderate_cleared(p, R)), R
def hold(path, title, R, move=True):
    os.makedirs(DR, exist_ok=True)
    dst = os.path.join(DR, os.path.relpath(os.path.abspath(path), ROOT).replace("/", "__").replace(".html", ".HOLD_REVIEW.html") if os.path.abspath(path).startswith(ROOT) else os.path.basename(path))
    if os.path.abspath(path) != os.path.abspath(dst): (shutil.move if move else shutil.copy)(path, dst)
    h = open(dst).read(); hs = sha(dst)
    src = sorted(set(u for u in re.findall(r"href=\"(https?://[^\"]+)", h) if not any(d in u for d in OWN_DOMAINS)))[:20]
    line = {"ts": now(), "site": SITE, "bot": BOT, "title": title, "flagged": "; ".join("[%d] %s" % (n, f) for n, f, _ in R),
            "rule": sorted(set(n for n, _, _ in R)), "sources": src, "suggestion": "; ".join(sorted(set(s for _, _, s in R))) +
            ("; HIGH: Joshua to approve this exact version or tell the bot to drop it (do not soften to bypass review)" if sev(R) == "HIGH" else ""),
            "severity": sev(R), "draft_path": dst, "sha256": hs, "status": "HOLD_REVIEW"}
    if not any(j.get("site") == SITE and j.get("sha256") == hs for j in _lines(Q)):  # no duplicate lines on rebuilds
        open(Q, "a").write(json.dumps(line, ensure_ascii=False) + "\n")
    return dst, line
def moderate_review(p, fix, title=None):
    import subprocess
    R = check(p)
    if not R: return True, {"verdict": "NO_FINDINGS"}
    if sev(R) != "MODERATE": return False, {"verdict": "HIGH", "reasons": ["HIGH severity rule: Joshua only"]}
    if any(n in OBJECTIVE for n, _, _ in R): return False, {"verdict": "NOT_FIXED", "reasons": ["licence or source detector still fires: fix it, review cannot clear it"]}
    if not os.path.exists(REVIEW) or not os.environ.get("OPENAI_API_KEY"): return False, {"verdict": "UNAVAILABLE", "reasons": ["no independent reviewer available"]}
    ctx = "; ".join("rule %d flag %r" % (n, f) for n, f, _ in R) + " | fix made: " + fix
    r = subprocess.run([sys.executable, REVIEW, p, ctx], capture_output=True, text=True, timeout=300)
    try: v = json.loads(r.stdout.strip().splitlines()[-1])
    except Exception: v = {"verdict": "UNSURE", "reasons": ["unparseable reviewer output: " + r.stdout[-300:] + r.stderr[-300:]]}
    ok = r.returncode == 0 and v.get("verdict") == "SAFE"
    if ok:
        open(MC, "a").write(json.dumps({"ts": now(), "site": SITE, "bot": BOT, "title": title or os.path.basename(p), "rule": sorted(set(n for n, _, _ in R)),
            "fix": fix, "chatgpt_verdict": "SAFE: " + "; ".join(map(str, v.get("reasons", [])))[:500], "sha256": sha(p),
            "file": os.path.relpath(p, ROOT) if os.path.abspath(p).startswith(ROOT) else p}, ensure_ascii=False) + "\n")
    return ok, v
def gate_built(paths):
    """Build step gate: every held page is removed from the site output and saved as a HOLD_REVIEW draft. Returns held list."""
    held = []
    for p in paths:
        bad, R = blocked(p)
        if bad:
            d, _ = hold(p, os.path.relpath(p, ROOT), R); held.append((p, d, R))
    return held
if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "check":
        bad = 0
        for p in a[1:]:
            b, R = blocked(p)
            if b:
                bad = 1; print("HOLD_REVIEW", sev(R), p); [print("  rule %d [%s]: %r : %s" % (n, "HIGH" if n in HIGH else "MODERATE", f, s)) for n, f, s in R]
            else: print("PASS" if not R else ("PASS (Joshua approved hash)" if approved(p) else "PASS (MODERATE, ChatGPT cleared hash)"), p)
        sys.exit(3 if bad else 0)
    if a and a[0] == "moderate" and len(a) >= 3:
        ok, v = moderate_review(a[1], a[2], a[3] if len(a) > 3 else None); print(json.dumps({"cleared": ok, **v}))
        sys.exit(0 if ok else 3)
    if a and a[0] == "hold":
        R = check(a[1]) or [(0, "manual", "held by bot judgement")]
        d, l = hold(a[1], a[2], R); print(json.dumps(l)); sys.exit(3)
    print(__doc__); sys.exit(2)

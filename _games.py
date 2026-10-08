"""SnoutsWise games hub and 3 original games. Code and art are original works
(c) 2026 Joshua Israel Ventures LLC. No libraries, no outside assets, no cookies, no tracking.
Facts come from sources opened on 9 Oct 2026 (RSPCA, ASPCApro, AKC) or the already sourced food table."""
import json, re, html

COPY = '<p class="copyline">Games are original works &copy; 2026 Joshua Israel Ventures LLC.</p>'
SAFE = ('<p class="gnote">No sign up, no ads, no cookies and no trackers. Your best score is saved only in this browser '
        '(localStorage) and is never sent to us. Sound is off unless you switch it on.</p>')

RSPCA = ("Understanding your dog's body language", "RSPCA", "https://www.rspca.org.uk/adviceandwelfare/pets/dogs/behaviour/understanding")
ASPCAPRO = ("Canine Body Language Tips", "ASPCApro (ASPCA)", "https://www.aspcapro.org/resource/canine-body-language-tips")
AKC_COLOR = ("Can Dogs See Color?", "American Kennel Club", "https://www.akc.org/expert-advice/health/are-dogs-color-blind/")

GAMES = [
    ("snack-or-nope", "Snack or Nope?", "Sort people foods into Safe, Caution or Toxic for dogs, then see the reason and the veterinary source.",
     "Quiz, sorting", "4 to adult"),
    ("wag-signals", "Wag Signals", "Read a cartoon dog's ears, eyes, mouth, body and tail and decide what it is trying to say.",
     "Quiz, body language", "6 to adult"),
    ("fetch-spotter", "Fetch Spotter", "Time your throw to land the ball by the flag, and find out why a yellow or blue ball is easier for dogs to spot.",
     "Timing, skill", "4 to adult"),
]

ICONS = {
 "snack-or-nope": '<svg class="gicon" viewBox="0 0 200 110" aria-hidden="true"><ellipse cx="100" cy="88" rx="70" ry="14" fill="#2F4BEB"/><path d="M34 70 Q100 120 166 70 Z" fill="#2F4BEB" stroke="#1A1633" stroke-width="4"/><circle cx="78" cy="56" r="15" fill="#0A7A3A" stroke="#1A1633" stroke-width="3"/><circle cx="104" cy="50" r="15" fill="#FFE600" stroke="#1A1633" stroke-width="3"/><circle cx="128" cy="58" r="15" fill="#B3001E" stroke="#1A1633" stroke-width="3"/><path d="M72 56l5 5 9-10" stroke="#fff" stroke-width="4" fill="none"/><path d="M104 42v10M104 57v1" stroke="#1A1633" stroke-width="4" stroke-linecap="round"/><path d="M122 52l12 12M134 52l-12 12" stroke="#fff" stroke-width="4"/></svg>',
 "wag-signals": '<svg class="gicon" viewBox="0 0 200 110" aria-hidden="true"><ellipse cx="96" cy="70" rx="48" ry="24" fill="#F5A54A" stroke="#1A1633" stroke-width="4"/><circle cx="146" cy="46" r="22" fill="#F5A54A" stroke="#1A1633" stroke-width="4"/><path d="M134 28 L140 0 L152 26 Z" fill="#C96A1E" stroke="#1A1633" stroke-width="3"/><ellipse cx="166" cy="54" rx="14" ry="9" fill="#FFE3B8" stroke="#1A1633" stroke-width="3"/><circle cx="178" cy="50" r="5" fill="#1A1633"/><path d="M144 42 q5 -5 10 0" stroke="#1A1633" stroke-width="3" fill="none"/><path d="M50 62 Q30 40 40 20" stroke="#1A1633" stroke-width="12" fill="none" stroke-linecap="round"/><path d="M50 62 Q30 40 40 20" stroke="#F5A54A" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M22 18 q-8 8 0 16 M14 12 q-14 14 0 28" stroke="#FF8A1F" stroke-width="3" fill="none"/></svg>',
 "fetch-spotter": '<svg class="gicon" viewBox="0 0 200 110" aria-hidden="true"><rect x="0" y="74" width="200" height="36" rx="10" fill="#5DBB63"/><path d="M20 70 Q90 -10 160 64" stroke="#2F4BEB" stroke-width="3" stroke-dasharray="6 6" fill="none"/><circle cx="160" cy="66" r="11" fill="#FFE600" stroke="#1A1633" stroke-width="3"/><path d="M150 64 q10 6 20 0" stroke="#fff" stroke-width="2" fill="none"/><path d="M182 76 V30" stroke="#1A1633" stroke-width="4"/><path d="M182 30 L200 38 L182 46 Z" fill="#FF8A1F" stroke="#1A1633" stroke-width="2"/></svg>',
}


def _strip(s):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()


def register(page, org, site_url, foods, sources):
    def vg(slug, name, desc, genre, ages):
        return {"@context": "https://schema.org", "@type": "VideoGame", "name": name, "url": site_url + "games/%s/" % slug,
                "description": desc, "genre": genre, "gamePlatform": "Web browser", "applicationCategory": "Game",
                "operatingSystem": "Any", "playMode": "SinglePlayer", "isAccessibleForFree": True, "inLanguage": "en",
                "typicalAgeRange": ages.replace(" to adult", "-"), "author": org, "publisher": org, "copyrightHolder": org,
                "copyrightYear": 2026, "image": site_url + "og-image.png"}

    def ldjson(o):
        return '<script type="application/ld+json">%s</script>' % json.dumps(o, ensure_ascii=False)

    css = '<link rel="stylesheet" href="{R}games/games.css">'

    # ---------------- HUB
    tiles = "".join('<a class="tile" href="{R}games/%s/">%s<h3>%s</h3><p>%s</p></a>' % (s, ICONS[s], n, d) for s, n, d, g, a in GAMES)
    hub_ld = {"@context": "https://schema.org", "@type": "ItemList", "name": "SnoutsWise dog games",
              "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": site_url + "games/%s/" % s, "name": n}
                                  for i, (s, n, d, g, a) in enumerate(GAMES)]}
    page("games/index.html", "Free Dog Games: Food Sorting, Body Language and Fetch | SnoutsWise",
         "Three free, original dog games that teach real facts: sort safe and toxic foods, read dog body language, and time a fetch throw. No sign up, no ads.",
         """
<div class="grid gamegrid">""" + tiles + """</div>
<section class="card"><h2>What you learn</h2><ul>
<li><b>Snack or Nope?</b> Which people foods are safe, risky or toxic for dogs, using the same verdicts and veterinary sources as our <a href="{R}can-dogs-eat.html">Can my dog eat this?</a> table.</li>
<li><b>Wag Signals:</b> how ears, eyes, mouth, body and tail show whether a dog is relaxed, playful, worried or warning you, based on RSPCA and ASPCA guidance. More in <a href="{R}behavior.html">dog behavior</a>.</li>
<li><b>Fetch Spotter:</b> why dogs find yellow and blue toys easier to see than red ones, from the American Kennel Club. More in <a href="{R}blog/can-dogs-see-color.html">Can dogs see color?</a></li></ul></section>
<section class="card"><h2>Safe for kids and classrooms</h2>""" + SAFE + """<p>Every game works with a mouse, a touchscreen or a keyboard, scales to phones, and respects your device's reduced motion setting.</p></section>
""" + COPY,
         h1="Dog games", kind="webpage", nav="games/",
         lead="Play three quick, original games and pick up real dog facts along the way. Each round ends with a fact card and the source it comes from.",
         extra_head=css + ldjson(hub_ld),
         related=[("can-dogs-eat.html", "Can my dog eat this?"), ("behavior.html", "Dog behavior"), ("blog/can-dogs-see-color.html", "Can dogs see color?"), ("training.html", "Training")],
         crumbs=[("index.html", "Home"), ("games/index.html", "Games")])

    # ---------------- SNACK OR NOPE
    data = [{"f": f, "v": v, "w": _strip(why.replace("{R}", "")), "a": "{R}can-dogs-eat.html#" + re.sub(r"[^a-z0-9]+", "-", f.lower().split("(")[0]).strip("-"),
             "s": [[sources[k][0], sources[k][1], sources[k][2]] for k in keys.split()]} for c, f, v, why, keys in foods]
    s1, n1, d1, g1, a1 = GAMES[0]
    js1 = r"""(function(){var D=__DATA__,L={yes:'Safe',caution:'Caution',no:'Toxic'},K='sw-best-snack-or-nope';
var st=document.getElementById('sn-stage'),ch=document.getElementById('sn-choices'),fc=document.getElementById('sn-fact'),sc=document.getElementById('sn-score'),rd=document.getElementById('sn-round'),be=document.getElementById('sn-best'),snd=document.getElementById('sn-sound');
var round=0,score=0,cur=null,deck=[],locked=false,sound=false,ac=null,best=0;try{best=+localStorage.getItem(K)||0}catch(e){}be.textContent=best;
function beep(f){if(!sound)return;try{ac=ac||new (window.AudioContext||window.webkitAudioContext)();var o=ac.createOscillator(),g=ac.createGain();o.frequency.value=f;g.gain.value=.08;o.connect(g);g.connect(ac.destination);o.start();o.stop(ac.currentTime+.15)}catch(e){}}
snd.onclick=function(){sound=!sound;snd.setAttribute('aria-pressed',sound);snd.textContent='Sound: '+(sound?'on':'off')};
function esc(s){return s.replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function shuffle(a){for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1)),t=a[i];a[i]=a[j];a[j]=t}return a}
function start(){deck=shuffle(D.slice()).slice(0,10);round=0;score=0;next()}
function next(){fc.hidden=true;locked=false;if(round>=deck.length)return end();cur=deck[round];round++;rd.textContent=round+' / '+deck.length;sc.textContent=score;
st.innerHTML='<div class="foodcard"><svg viewBox="0 0 120 50" width="120" height="50" aria-hidden="true"><path d="M10 14 Q60 64 110 14 Z" fill="#2F4BEB" stroke="#1A1633" stroke-width="4"/><ellipse cx="60" cy="14" rx="50" ry="7" fill="#9AA6F5" stroke="#1A1633" stroke-width="3"/></svg><p class="food">'+esc(cur.f)+'</p><p class="gnote">Can a dog eat this?</p></div>';
[].forEach.call(ch.querySelectorAll('button'),function(b){b.disabled=false});ch.querySelector('button').focus()}
function pick(v){if(locked||!cur)return;locked=true;var ok=v==cur.v;if(ok){score++;beep(880)}else beep(220);sc.textContent=score;
[].forEach.call(ch.querySelectorAll('button'),function(b){b.disabled=true});
fc.innerHTML='<h3 class="'+(ok?'ok':'bad')+'">'+(ok?'Yes! ':'Not quite. ')+'<span class="'+cur.v+'">'+L[cur.v]+'</span></h3><p>'+esc(cur.w)+'</p><p class="src">Source: '+cur.s.map(function(s){return '<a href="'+s[2]+'" rel="noopener">'+esc(s[1])+', '+esc(s[0])+'</a>'}).join('; ')+'. <a href="'+cur.a+'">See it in the full table</a>.</p><button class="btn" id="sn-next">'+(round>=deck.length?'See my score':'Next food')+'</button>';
fc.hidden=false;document.getElementById('sn-next').onclick=next;document.getElementById('sn-next').focus()}
function end(){cur=null;if(score>best){best=score;try{localStorage.setItem(K,best)}catch(e){}}be.textContent=best;
st.innerHTML='<div class="foodcard"><p class="food">You scored '+score+' out of '+deck.length+'</p><p>'+(score>=8?'Top dog! You really know your snacks.':score>=5?'Good sniffing! Check the full table to learn the rest.':'Keep practising: the full food table explains every answer.')+'</p><button class="btn" id="sn-again">Play again</button></div>';
[].forEach.call(ch.querySelectorAll('button'),function(b){b.disabled=true});document.getElementById('sn-again').onclick=start;document.getElementById('sn-again').focus()}
[].forEach.call(ch.querySelectorAll('button'),function(b){b.onclick=function(){pick(b.dataset.v)}});
document.addEventListener('keydown',function(e){if(e.target.tagName=='INPUT')return;var m={'1':'yes','2':'caution','3':'no'}[e.key];if(m&&!locked){e.preventDefault();pick(m)}});
start()})();""".replace("__DATA__", json.dumps(data, ensure_ascii=False))
    page("games/snack-or-nope/index.html", "Snack or Nope? Free Dog Food Safety Game | SnoutsWise",
         "Free original game: decide whether people foods are Safe, Caution or Toxic for dogs, then see the reason and the ASPCA, AKC or Merck source.",
         """
<div class="game" aria-label="Snack or Nope game">
<div class="gbar"><span>Food <span class="pill" id="sn-round">1 / 10</span></span><span>Score <span class="pill" id="sn-score" aria-live="polite">0</span></span><span>Best <span class="pill" id="sn-best">0</span></span><button class="btn ghost" id="sn-sound" aria-pressed="false">Sound: off</button></div>
<div class="gstage" id="sn-stage" aria-live="polite"></div>
<div class="choices" id="sn-choices"><button class="btn" data-v="yes"><span class="yes">Safe</span> treat <span class="kbd">1</span></button><button class="btn" data-v="caution"><span class="caution">Caution</span> <span class="kbd">2</span></button><button class="btn" data-v="no"><span class="no">Toxic</span> <span class="kbd">3</span></button></div>
<div class="factcard" id="sn-fact" hidden aria-live="polite"></div>
</div>
<p class="call"><b>Real emergency? This is a game, not advice.</b> If your dog ate something worrying, call your vet or the ASPCA Animal Poison Control Center: <a href="tel:+18884264435">(888) 426-4435</a>.</p>
<section class="card"><h2>How to play</h2><p>Each round shows 10 foods picked at random from our """ + str(len(foods)) + """ food list. Tap or click <b>Safe</b>, <b>Caution</b> or <b>Toxic</b>, or press 1, 2 or 3 on a keyboard. After every answer a fact card explains the verdict and links the source it comes from.</p>""" + SAFE + """</section>
<section class="card"><h2>What this game teaches</h2><ul><li>Some everyday foods are toxic to dogs, including chocolate, grapes and raisins, onions and garlic, macadamia nuts and the sweetener xylitol.</li><li>Many plain fruits and vegetables are fine as occasional treats.</li><li>"Caution" foods are not usually poisonous but can cause problems in larger amounts or when prepared the wrong way.</li></ul><p>Every verdict and reason comes from our <a href="{R}can-dogs-eat.html">Can my dog eat this?</a> table, sourced to the ASPCA, the American Kennel Club, the Merck Veterinary Manual and Cornell University.</p></section>
""" + COPY,
         h1="Snack or Nope?", kind="webpage", nav="games/",
         lead="Can a dog eat it? Sort 10 people foods into Safe, Caution or Toxic, and learn why after every answer.",
         extra_head=css + ldjson(vg(s1, n1, d1, g1, a1)), script=js1,
         sources=[sources["aspca_foods"], sources["akc_food"], sources["akc_fruit"], sources["merck_choc"], sources["merck_xyl"]],
         related=[("can-dogs-eat.html", "Can my dog eat this? full table"), ("blog/dog-ate-chocolate.html", "My dog ate chocolate"), ("games/index.html", "More dog games"), ("health.html", "Health basics")],
         crumbs=[("index.html", "Home"), ("games/index.html", "Games"), ("games/snack-or-nope/index.html", "Snack or Nope?")])

    # ---------------- WAG SIGNALS
    R_, A_ = "RSPCA", "ASPCApro"
    scen = [
        ({"ears": "natural", "eye": "soft", "mouth": "open", "tail": "neutral", "wag": "slow"}, 0,
         "Loose body, mouth open and relaxed, ears in a natural position, slow side to side wag.",
         "The RSPCA describes a relaxed, happy dog as having an open, relaxed mouth, ears in a natural position, normal shaped eyes, smooth hair and a wagging tail. ASPCApro adds that a loose, wide wag with other relaxed body language shows a relaxed, happy dog.", [0, 1]),
        ({"bow": 1, "ears": "natural", "eye": "soft", "mouth": "open", "tail": "high", "wag": "fast"}, 1,
         "Chest and front legs down, bottom up, tail high and wagging.",
         "This is a play bow. ASPCApro says dogs often start play with a play bow, followed by loose, bouncy movements. The RSPCA shows a dog inviting play with its bottom raised and a high, wagging tail.", [1, 0]),
        ({"low": 16, "head": "low", "ears": "back", "eye": "away", "mouth": "yawn", "tail": "tucked"}, 2,
         "Body and head held low, ears back, tail tucked under, yawning.",
         "The RSPCA lists exactly these signs for a worried dog that is uncomfortable and does not want you to come closer. ASPCApro notes that yawning can be an early sign of stress.", [0, 1]),
        ({"low": 6, "head": "low", "ears": "back", "eye": "away", "mouth": "closed", "tail": "tucked", "paw": 1}, 2,
         "Head lowered, looking away, ears back, one front paw raised, tail tucked.",
         "The RSPCA describes a worried dog lowering its head, avoiding eye contact, tucking its tail, putting its ears back and raising a front paw. ASPCApro lists looking away, lowering the head and raising a paw as signs of fear.", [0, 1]),
        ({"ears": "back", "eye": "whale", "mouth": "lick", "tail": "tucked"}, 2,
         "White of the eye showing, quick lip lick, ears back.",
         "ASPCApro calls a lot of white showing around the eye \"whale eye\", a sign of tension, and says yawning and lip licking can be early signs of stress, especially with a tight mouth.", [1]),
        ({"head": "up", "ears": "up", "eye": "hard", "mouth": "teeth", "wrinkle": 1, "hackles": 1, "tail": "high", "wag": "stiff"}, 3,
         "Stiff body leaning forward, hair raised, tail up and stiff, ears up, nose wrinkled, hard stare.",
         "The RSPCA describes an angry or very unhappy dog with weight forward, raised hair, a stiff raised tail, ears up and a wrinkled nose. ASPCApro says a high tail with short, stiff, rapid movements usually signals tension or potential aggression. Back away calmly and give the dog space.", [0, 1]),
        ({"low": 22, "head": "low", "ears": "flat", "eye": "whale", "mouth": "teeth", "tail": "tucked"}, 3,
         "Cowering low, tail tucked, ears flat, teeth showing.",
         "The RSPCA shows a cowering dog with its tail between its legs, ears flat and teeth showing as a very unhappy dog that wants you to go away. ASPCApro explains that a frightened dog that feels cornered may defend itself. Give it space.", [0, 1]),
        ({"ears": "natural", "eye": "soft", "mouth": "open", "tail": "heli"}, 0,
         "Loose body, open mouth, tail spinning round in circles.",
         "ASPCApro calls a tail that spins rapidly in circles a \"helicopter tail\" and says it shows friendliness, excitement and joy.", [1]),
    ]
    jsdata = [{"p": p, "a": a, "c": c, "e": e, "s": [[x[0], x[1], x[2]] for x in [(RSPCA, ASPCAPRO)[i] for i in ss]]} for p, a, c, e, ss in scen]
    s2, n2, d2, g2, a2 = GAMES[1]
    js2 = r"""(function(){var D=__DATA__,O=['Happy and friendly','Wants to play','Worried: give space','Warning: stay away'],K='sw-best-wag-signals';
var st=document.getElementById('ws-stage'),ch=document.getElementById('ws-choices'),fc=document.getElementById('ws-fact'),sc=document.getElementById('ws-score'),rd=document.getElementById('ws-round'),be=document.getElementById('ws-best'),cl=document.getElementById('ws-clue'),snd=document.getElementById('ws-sound');
var deck=[],i=0,score=0,locked=false,best=0,sound=false,ac=null;try{best=+localStorage.getItem(K)||0}catch(e){}be.textContent=best;
function beep(f){if(!sound)return;try{ac=ac||new (window.AudioContext||window.webkitAudioContext)();var o=ac.createOscillator(),g=ac.createGain();o.frequency.value=f;g.gain.value=.08;o.connect(g);g.connect(ac.destination);o.start();o.stop(ac.currentTime+.15)}catch(e){}}
snd.onclick=function(){sound=!sound;snd.setAttribute('aria-pressed',sound);snd.textContent='Sound: '+(sound?'on':'off')};
function shuffle(a){for(var k=a.length-1;k>0;k--){var j=Math.floor(Math.random()*(k+1)),t=a[k];a[k]=a[j];a[j]=t}return a}
ch.innerHTML=O.map(function(o,k){return '<button class="btn'+(k%2?' alt':'')+'" data-a="'+k+'">'+o+' <span class="kbd">'+(k+1)+'</span></button>'}).join('');
function start(){deck=shuffle(D.slice());i=0;score=0;show()}
function show(){fc.hidden=true;locked=false;if(i>=deck.length)return end();var d=deck[i];rd.textContent=(i+1)+' / '+deck.length;sc.textContent=score;
var p=Object.assign({label:'Cartoon dog: '+d.c},d.p);st.innerHTML=window.SWDog(p);cl.textContent='Clues: '+d.c;
[].forEach.call(ch.querySelectorAll('button'),function(b){b.disabled=false});ch.querySelector('button').focus()}
function pick(a){if(locked||i>=deck.length)return;locked=true;var d=deck[i],ok=a==d.a;if(ok){score++;beep(880)}else beep(220);sc.textContent=score;
[].forEach.call(ch.querySelectorAll('button'),function(b){b.disabled=true});i++;
fc.innerHTML='<h3 class="'+(ok?'ok':'bad')+'">'+(ok?'Yes! ':'Not quite. ')+'This dog: '+O[d.a]+'</h3><p>'+d.e+'</p><p class="src">Source: '+d.s.map(function(s){return '<a href="'+s[2]+'" rel="noopener">'+s[1]+', '+s[0]+'</a>'}).join('; ')+'</p><button class="btn" id="ws-next">'+(i>=deck.length?'See my score':'Next dog')+'</button>';
fc.hidden=false;document.getElementById('ws-next').onclick=show;document.getElementById('ws-next').focus()}
function end(){if(score>best){best=score;try{localStorage.setItem(K,best)}catch(e){}}be.textContent=best;cl.textContent='';
st.innerHTML='<div class="foodcard"><p class="food">You read '+score+' of '+deck.length+' dogs</p><p>'+(score>=7?'Expert dog whisperer!':score>=4?'Nice reading! Real dogs mix signals, so always look at the whole dog.':'Good start. Look at the ears, eyes, mouth, body and tail together.')+'</p><button class="btn" id="ws-again">Play again</button></div>';
[].forEach.call(ch.querySelectorAll('button'),function(b){b.disabled=true});document.getElementById('ws-again').onclick=start;document.getElementById('ws-again').focus()}
[].forEach.call(ch.querySelectorAll('button'),function(b){b.onclick=function(){pick(+b.dataset.a)}});
document.addEventListener('keydown',function(e){var k=+e.key;if(k>=1&&k<=4&&!locked){e.preventDefault();pick(k-1)}});
start()})();""".replace("__DATA__", json.dumps(jsdata, ensure_ascii=False))
    page("games/wag-signals/index.html", "Wag Signals: Free Dog Body Language Game | SnoutsWise",
         "Free original game: read a cartoon dog's ears, eyes, mouth, body and tail and decide if it is happy, playful, worried or warning you. Based on RSPCA and ASPCA guidance.",
         """
<div class="game" aria-label="Wag Signals game">
<div class="gbar"><span>Dog <span class="pill" id="ws-round">1 / 8</span></span><span>Score <span class="pill" id="ws-score" aria-live="polite">0</span></span><span>Best <span class="pill" id="ws-best">0</span></span><button class="btn ghost" id="ws-sound" aria-pressed="false">Sound: off</button></div>
<div class="gstage" id="ws-stage"></div><p class="gnote" id="ws-clue" aria-live="polite"></p>
<div class="choices" id="ws-choices"></div>
<div class="factcard" id="ws-fact" hidden aria-live="polite"></div>
</div>
<section class="card"><h2>How to play</h2><p>Look at the whole dog: ears, eyes, mouth, body and tail. Then choose what it is most likely saying, by tapping, clicking or pressing 1 to 4. A fact card after each dog explains the signals and links the source.</p>""" + SAFE + """</section>
<section class="card"><h2>What this game teaches</h2><ul><li>A relaxed dog has a loose body, a relaxed open mouth, ears in a natural position and a loose wag (RSPCA, ASPCApro).</li><li>A play bow, with the chest down and bottom up, is an invitation to play (ASPCApro).</li><li>A low body, tucked tail, ears back, yawning, lip licking, looking away and a raised paw can mean a dog is worried (RSPCA, ASPCApro).</li><li>A stiff body, raised hair, stiff high tail, wrinkled nose or showing teeth are warnings to give the dog space (RSPCA).</li><li>A wagging tail alone does not always mean a happy dog: speed, height and stiffness matter (ASPCApro).</li></ul>
<p>Real dogs mix signals and every dog is different. If a dog looks worried or warns you, calmly give it space, and ask a vet or qualified behaviorist about behavior worries. Read more in <a href="{R}behavior.html">dog behavior explained</a>.</p></section>
""" + COPY,
         h1="Wag Signals", kind="webpage", nav="games/",
         lead="What is this dog trying to say? Read 8 cartoon dogs and learn the body language signals the RSPCA and ASPCA teach.",
         extra_head=css + ldjson(vg(s2, n2, d2, g2, a2)) + '<script src="{R}games/dog.js"></script>', script=js2,
         sources=[RSPCA, ASPCAPRO],
         related=[("behavior.html", "Dog behavior explained"), ("blog/puppy-socialization-window.html", "Puppy socialization window"), ("games/index.html", "More dog games"), ("training.html", "Reward based training")],
         crumbs=[("index.html", "Home"), ("games/index.html", "Games"), ("games/wag-signals/index.html", "Wag Signals")])

    # ---------------- FETCH SPOTTER
    facts = [
        ("Dogs can see some colors", "Dogs are not limited to black and white. The AKC says dogs can make out yellow and blue, and combinations of those colors.", 0),
        ("Red balls get lost", "Red and orange are hard for dogs to pick out against green grass, so the AKC suggests not choosing a red toy for fetch in the grass.", 0),
        ("Two cones, not three", "People usually have three kinds of color sensing cone cells. The AKC explains that dogs have only two, much like a person with red green color blindness.", 0),
        ("Built for movement", "Dogs have more rods than cones in the retina. The AKC says rods are very sensitive cells that catch movement and work in low light.", 0),
        ("Let's play!", "When dogs start a game they often begin with a play bow, chest down and bottom up, according to ASPCApro.", 1),
        ("Cooling down", "Dogs pant to cool themselves and can also sweat through their paws, says ASPCApro. Give your dog water and rest breaks during fetch.", 1),
    ]
    fsrc = [AKC_COLOR, ASPCAPRO]
    s3, n3, d3, g3, a3 = GAMES[2]
    js3 = r"""(function(){var F=__FACTS__,S=__SRC__,K='sw-best-fetch-spotter',RM=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
var svg=document.getElementById('fs-svg'),ball=document.getElementById('fs-ball'),dog=document.getElementById('fs-dog'),flag=document.getElementById('fs-flag'),q=document.getElementById('fs-q'),mk=document.getElementById('fs-mark'),tb=document.getElementById('fs-throw'),fc=document.getElementById('fs-fact'),sc=document.getElementById('fs-score'),rd=document.getElementById('fs-round'),be=document.getElementById('fs-best'),msg=document.getElementById('fs-msg'),snd=document.getElementById('fs-sound');
var COL={yellow:'#FFE600',blue:'#2F4BEB',red:'#E0312B'},col='yellow',p=0,dir=1,run=false,busy=false,throwN=0,score=0,best=0,target=400,fi=Math.floor(Math.random()*F.length),sound=false,ac=null,last=0;
try{best=+localStorage.getItem(K)||0}catch(e){}be.textContent=best;
function beep(f){if(!sound)return;try{ac=ac||new (window.AudioContext||window.webkitAudioContext)();var o=ac.createOscillator(),g=ac.createGain();o.frequency.value=f;g.gain.value=.08;o.connect(g);g.connect(ac.destination);o.start();o.stop(ac.currentTime+.15)}catch(e){}}
snd.onclick=function(){sound=!sound;snd.setAttribute('aria-pressed',sound);snd.textContent='Sound: '+(sound?'on':'off')};
[].forEach.call(document.querySelectorAll('[data-col]'),function(b){b.onclick=function(){setCol(b.dataset.col)}});
function setCol(c){if(busy)return;col=c;ball.setAttribute('fill',COL[c]);[].forEach.call(document.querySelectorAll('[data-col]'),function(b){b.setAttribute('aria-pressed',b.dataset.col==c)})}
function loop(t){if(run){var dt=last?Math.min(50,t-last):16;last=t;p+=dir*dt*(RM?.05:.11);if(p>=100){p=100;dir=-1}if(p<=0){p=0;dir=1}mk.style.left=p+'%'}requestAnimationFrame(loop)}
function newRound(){throwN=0;score=0;sc.textContent=0;nextThrow()}
function nextThrow(){fc.hidden=true;busy=false;if(throwN>=5)return end();throwN++;rd.textContent=throwN+' / 5';target=260+Math.round(Math.random()*290);flag.setAttribute('transform','translate('+target+' 0)');
ball.setAttribute('cx',96);ball.setAttribute('cy',150);dog.setAttribute('transform','translate(0 0)');q.setAttribute('opacity',0);msg.textContent='Pick a ball color, then press Throw (or Space) when the marker is in the bright zone.';run=true;last=0;tb.disabled=false;tb.focus()}
function anim(dur,fn,done){if(RM){fn(1);done();return}var t0=null;function f(t){if(!t0)t0=t;var k=Math.min(1,(t-t0)/dur);fn(k);if(k<1)requestAnimationFrame(f);else done()}requestAnimationFrame(f)}
function doThrow(){if(busy||!run)return;run=false;busy=true;tb.disabled=true;beep(660);var x=96+p*4.9,x0=96;
anim(700,function(k){ball.setAttribute('cx',x0+(x-x0)*k);ball.setAttribute('cy',150-Math.sin(Math.PI*k)*110)},function(){
var diff=Math.abs(x-target),pts=Math.max(0,100-Math.round(diff/2)),red=col=='red';
anim(800,function(k){dog.setAttribute('transform','translate('+((x-110)*k)+' 0)')},function(){
function fin(){if(red)pts=Math.round(pts*.6);score+=pts;sc.textContent=score;beep(pts>70?990:330);
msg.textContent=(pts>=90?'Bullseye! ':pts>=60?'Great throw! ':pts>0?'Nice try! ':'Missed the flag! ')+'+'+pts+' points'+(red?' (the red ball was hard to spot, so your dog took longer)':'');
var f=F[fi++%F.length];fc.innerHTML='<h3>'+f[0]+'</h3><p>'+f[1]+'</p><p class="src">Source: <a href="'+S[f[2]][2]+'" rel="noopener">'+S[f[2]][1]+', '+S[f[2]][0]+'</a></p><button class="btn" id="fs-next">'+(throwN>=5?'See my score':'Next throw')+'</button>';fc.hidden=false;document.getElementById('fs-next').onclick=nextThrow;document.getElementById('fs-next').focus()}
if(red){q.setAttribute('transform','translate('+(x-110)+' 0)');q.setAttribute('opacity',1);setTimeout(function(){q.setAttribute('opacity',0);fin()},RM?300:1400)}else fin()})})}
function end(){if(score>best){best=score;try{localStorage.setItem(K,best)}catch(e){}}be.textContent=best;msg.textContent='Round over: '+score+' points out of 500. Press Play again for 5 more throws.';
fc.innerHTML='<h3>Round over: '+score+' / 500</h3><p>'+(score>=400?'Champion thrower!':score>=250?'Good arm! Try a yellow or blue ball for faster fetches.':'Keep practising: stop the marker in the bright zone.')+'</p><button class="btn" id="fs-again">Play again</button>';fc.hidden=false;document.getElementById('fs-again').onclick=newRound;document.getElementById('fs-again').focus()}
tb.onclick=doThrow;document.addEventListener('keydown',function(e){if(e.code=='Space'&&run&&e.target.tagName!='BUTTON'){e.preventDefault();doThrow()}var m={'1':'yellow','2':'blue','3':'red'}[e.key];if(m)setCol(m)});
setCol('yellow');requestAnimationFrame(loop);newRound()})();""".replace("__FACTS__", json.dumps(facts, ensure_ascii=False)).replace("__SRC__", json.dumps([list(x) for x in fsrc], ensure_ascii=False))
    scene = ('<svg id="fs-svg" viewBox="0 0 600 220" role="img" aria-label="A field with a dog on the left, a ball and a target flag">'
             '<defs><linearGradient id="fs-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#BFD3FF"/><stop offset="1" stop-color="#FFF7D6"/></linearGradient></defs>'
             '<rect width="600" height="220" fill="url(#fs-sky)"/><circle cx="540" cy="40" r="22" fill="#FFE600"/>'
             '<rect y="160" width="600" height="60" fill="#5DBB63"/><path d="M0 160 Q150 150 300 160 T600 160 V170 H0Z" fill="#4AA552"/>'
             '<g id="fs-flag"><path d="M0 172 V110" stroke="#1A1633" stroke-width="4"/><path d="M0 110 L26 119 L0 128 Z" fill="#FF8A1F" stroke="#1A1633" stroke-width="2"/><ellipse cx="0" cy="174" rx="22" ry="5" fill="#FFE600" opacity=".7"/></g>'
             '<g id="fs-dog"><g transform="translate(20 104) scale(.3)">'
             '<ellipse cx="150" cy="118" rx="72" ry="36" fill="#F5A54A" stroke="#1A1633" stroke-width="6"/><rect x="99" y="134" width="18" height="56" rx="9" fill="#F5A54A" stroke="#1A1633" stroke-width="6"/><rect x="173" y="134" width="18" height="56" rx="9" fill="#F5A54A" stroke="#1A1633" stroke-width="6"/>'
             '<circle cx="222" cy="88" r="30" fill="#F5A54A" stroke="#1A1633" stroke-width="6"/><path d="M208 66 Q188 84 200 104 Q216 90 224 62 Z" fill="#C96A1E" stroke="#1A1633" stroke-width="5"/><ellipse cx="252" cy="98" rx="23" ry="14" fill="#FFE3B8" stroke="#1A1633" stroke-width="5"/><ellipse cx="272" cy="92" rx="7" ry="6" fill="#1A1633"/><path d="M223 82 q7 -7 14 0" stroke="#1A1633" stroke-width="5" fill="none"/>'
             '<path d="M82 108 Q60 80 70 56" stroke="#1A1633" stroke-width="17" fill="none" stroke-linecap="round"/><path d="M82 108 Q60 80 70 56" stroke="#F5A54A" stroke-width="11" fill="none" stroke-linecap="round"/></g></g>'
             '<g id="fs-q" opacity="0"><text x="96" y="96" font-size="34" font-weight="700" fill="#1A1633" font-family="Fredoka,Nunito,sans-serif">?</text></g>'
             '<circle id="fs-ball" cx="96" cy="150" r="9" fill="#FFE600" stroke="#1A1633" stroke-width="3"/></svg>')
    page("games/fetch-spotter/index.html", "Fetch Spotter: Free Dog Fetch Timing Game | SnoutsWise",
         "Free original game: time your throw to land the ball by the flag, and learn why yellow and blue toys are easier for dogs to see. Facts from the AKC and ASPCA.",
         """
<div class="game" aria-label="Fetch Spotter game">
<div class="gbar"><span>Throw <span class="pill" id="fs-round">1 / 5</span></span><span>Score <span class="pill" id="fs-score" aria-live="polite">0</span></span><span>Best <span class="pill" id="fs-best">0</span></span><button class="btn ghost" id="fs-sound" aria-pressed="false">Sound: off</button></div>
<div class="gstage">""" + scene + """</div>
<div style="position:relative;height:26px;margin:.8rem 0;border-radius:999px;background:linear-gradient(90deg,#E3E9FF 0%,#E3E9FF 55%,#FFE600 62%,#FF8A1F 80%,#FFE600 88%,#E3E9FF 95%);box-shadow:0 0 0 2px #2F4BEB" aria-hidden="true"><div id="fs-mark" style="position:absolute;top:-5px;left:0;width:10px;height:36px;margin-left:-5px;border-radius:6px;background:#1A1633"></div></div>
<p class="gnote" id="fs-msg" aria-live="polite"></p>
<div class="choices"><button class="btn ghost" data-col="yellow" aria-pressed="true">Yellow ball <span class="kbd">1</span></button><button class="btn ghost" data-col="blue" aria-pressed="false">Blue ball <span class="kbd">2</span></button><button class="btn ghost" data-col="red" aria-pressed="false">Red ball <span class="kbd">3</span></button><button class="btn" id="fs-throw">Throw! <span class="kbd">Space</span></button></div>
<div class="factcard" id="fs-fact" hidden aria-live="polite"></div>
</div>
<section class="card"><h2>How to play</h2><p>The marker slides along the power bar. Press <b>Throw!</b>, tap it, or press the space bar to stop it. The flag moves every throw, so aim for the distance shown. You get 5 throws, up to 100 points each. Try a red ball too, and see why dogs find it harder to spot in the grass.</p>""" + SAFE + """</section>
<section class="card"><h2>What this game teaches</h2><ul><li>Dogs can make out yellow and blue, and combinations of those colors (AKC).</li><li>Red and orange toys are hard for dogs to see against green grass (AKC).</li><li>Dogs have two kinds of color sensing cones where most people have three (AKC).</li><li>Dogs often start play with a play bow, and they pant and sweat through their paws to cool down (ASPCApro).</li></ul><p>Read the full story in <a href="{R}blog/can-dogs-see-color.html">Can dogs see color?</a></p></section>
""" + COPY,
         h1="Fetch Spotter", kind="webpage", nav="games/",
         lead="Time your throw, land the ball by the flag, and discover which ball colors a dog can spot best.",
         extra_head=css + ldjson(vg(s3, n3, d3, g3, a3)), script=js3,
         sources=[AKC_COLOR, ASPCAPRO],
         related=[("blog/can-dogs-see-color.html", "Can dogs see color?"), ("care.html", "Exercise and everyday care"), ("games/index.html", "More dog games"), ("training.html", "Training")],
         crumbs=[("index.html", "Home"), ("games/index.html", "Games"), ("games/fetch-spotter/index.html", "Fetch Spotter")])

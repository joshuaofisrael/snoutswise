"""Teachers hub, printable worksheets and research page for SnoutsWise.
Original text and art (c) 2026 Joshua Israel Ventures LLC. NGSS codes verified on nextgenscience.org 9 Oct 2026.
Papers verified via Crossref DOI records 9 Oct 2026."""
import json

NGSS = {
 "K-LS1-1": ("Use observations to describe patterns of what plants and animals (including humans) need to survive.", "https://www.nextgenscience.org/pe/k-ls1-1-molecules-organisms-structures-and-processes"),
 "3-LS3-1": ("Analyze and interpret data to provide evidence that plants and animals have traits inherited from parents and that variation of these traits exists in a group of similar organisms.", "https://www.nextgenscience.org/pe/3-ls3-1-heredity-inheritance-and-variation-traits"),
 "4-LS1-2": ("Use a model to describe that animals receive different types of information through their senses, process the information in their brain, and respond to the information in different ways.", "https://www.nextgenscience.org/pe/4-ls1-2-molecules-organisms-structures-and-processes"),
 "MS-LS4-5": ("Gather and synthesize information about technologies that have changed the way humans influence the inheritance of desired traits in organisms.", "https://www.nextgenscience.org/pe/ms-ls4-5-biological-evolution-unity-and-diversity"),
}
PAPERS = [
 ("Neitz J, Geist T, Jacobs GH", 1989, "Color vision in the dog", "Visual Neuroscience", "3(2):119-125", "10.1017/s0952523800004430",
  "Behavioral tests with three dogs showed the dog retina has two classes of cone pigment, with peaks near 429 nm and 555 nm, so dogs have dichromatic (two color channel) vision.", "blog/can-dogs-see-color.html"),
 ("Kasparson AA, Badridze J, Maximov VV", 2013, "Colour cues proved to be more informative for dogs than brightness", "Proceedings of the Royal Society B", "280(1766):20131356", "10.1098/rspb.2013.1356",
  "Eight previously untrained dogs chose between stimuli that differed in both brightness and color, and relied on color rather than brightness.", "blog/can-dogs-see-color.html"),
 ("Wang T, Ma J, Hogan AN, et al. (including Ostrander EA and Ideker T)", 2020, "Quantitative translation of dog-to-human aging by conserved remodeling of the DNA methylome", "Cell Systems", "11(2):176-185", "10.1016/j.cels.2020.06.006",
  "Compared age related DNA methylation changes in Labrador Retrievers and people to build a dog to human age conversion, the basis of our dog age calculator.", "dog-age-calculator.html"),
 ("Kealy RD, Lawler DF, Ballam JM, et al.", 2002, "Effects of diet restriction on life span and age-related changes in dogs", "Journal of the American Veterinary Medical Association", "220(9):1315-1320", "10.2460/javma.2002.220.1315",
  "In 48 Labrador Retrievers studied as pairs for life, dogs fed 25% less than their pair mates had a longer median life span and later onset of chronic disease.", "blog/is-my-dog-overweight.html"),
 ("Mech LD", 1999, "Alpha status, dominance, and division of labor in wolf packs", "Canadian Journal of Zoology", "77(8):1196-1203", "10.1139/z99-099",
  "Based on 13 summers observing wild wolves on Ellesmere Island, concludes that a typical wolf pack is a family led by the parents, not a group constantly fighting for alpha status.", "blog/alpha-dog-myth.html"),
]
GUIDES = [
 ("2022 AAHA Canine Vaccination Guidelines", "American Animal Hospital Association", "https://www.aaha.org/resources/2022-aaha-canine-vaccination-guidelines/", "blog/dog-vaccine-schedule.html"),
 ("Position Statement on Puppy Socialization", "American Veterinary Society of Animal Behavior", "https://avsab.org/wp-content/uploads/2019/01/Puppy-Socialization-Position-Statement-FINAL.pdf", "blog/puppy-socialization-window.html"),
 ("Position Statement on Humane Dog Training (2021)", "American Veterinary Society of Animal Behavior", "https://avsab.org/wp-content/uploads/2021/08/AVSAB-Humane-Dog-Training-Position-Statement-2021.pdf", "training.html"),
 ("Body Condition Score: Dog", "World Small Animal Veterinary Association", "https://wsava.org/wp-content/uploads/2020/01/Body-Condition-Score-Dog.pdf", "blog/is-my-dog-overweight.html"),
]
RSPCA = ("Understanding your dog's body language", "RSPCA", "https://www.rspca.org.uk/adviceandwelfare/pets/dogs/behaviour/understanding")
ASPCAPRO = ("Canine Body Language Tips", "ASPCApro (ASPCA)", "https://www.aspcapro.org/resource/canine-body-language-tips")
AKC_COLOR = ("Can Dogs See Color?", "American Kennel Club", "https://www.akc.org/expert-advice/health/are-dogs-color-blind/")
NOADS = '<p class="gnote noprint">Free to print and copy for classroom use. No sign up, no ads, and no student data collected. &copy; 2026 Joshua Israel Ventures LLC.</p>'
PRINT = '<p class="noprint"><button class="btn" onclick="window.print()">Print this page</button></p>'


def ngss_box(codes):
    return '<aside class="card"><h2>NGSS connection</h2><ul>' + "".join(
        '<li><a href="%s" rel="noopener"><b>%s</b></a>: %s</li>' % (NGSS[c][1], c, NGSS[c][0]) for c in codes) + \
        '</ul><p class="gnote">Standards text quoted from nextgenscience.org. This activity supports, but does not by itself fully assess, the performance expectation.</p></aside>'


def register(page, org, site_url, S):
    def lr(path, name, desc, levels, rtype, codes):
        o = {"@context": "https://schema.org", "@type": "LearningResource", "name": name, "url": site_url + path.replace("index.html", ""),
             "description": desc, "educationalLevel": levels, "learningResourceType": rtype, "inLanguage": "en",
             "isAccessibleForFree": True, "audience": {"@type": "EducationalAudience", "educationalRole": "teacher"},
             "publisher": org, "author": org, "copyrightHolder": org, "copyrightYear": 2026}
        if codes:
            o["educationalAlignment"] = [{"@type": "AlignmentObject", "alignmentType": "teaches", "educationalFramework": "Next Generation Science Standards",
                                          "targetName": c, "targetDescription": NGSS[c][0], "targetUrl": NGSS[c][1]} for c in codes]
        return '<script type="application/ld+json">%s</script>' % json.dumps(o, ensure_ascii=False)

    crumbs = lambda p, n: [("index.html", "Home"), ("teachers/index.html", "Teachers"), (p, n)]

    # ------------- HUB
    page("teachers/index.html", "Free Dog Science Resources for Teachers: Worksheets, Lessons, Games | SnoutsWise",
         "Free printable dog fact sheets and worksheets with answer keys, lesson ideas by grade band linked to NGSS, a vocabulary list and classroom games. No sign up, no ads.",
         """
<section class="card"><h2>Printables (free, no sign up)</h2><ul>
<li><a href="{R}teachers/dog-needs-worksheet.html"><b>What does a dog need?</b></a> Grades K to 2 worksheet with answer key. NGSS K-LS1-1.</li>
<li><a href="{R}teachers/dog-senses-fact-sheet.html"><b>Dog senses and body language fact sheet</b></a> Grades 3 to 5, with a short quiz and answer key. NGSS 4-LS1-2.</li>
<li><a href="{R}teachers/dog-traits-worksheet.html"><b>Traits, breeds and selective breeding</b></a> Grades 3 to 8 worksheet with answer key. NGSS 3-LS3-1 and MS-LS4-5.</li></ul>
<p>Each printable is a print friendly page: use your browser's print button or the Print button on the page. Facts are sourced to veterinary organizations, the American Kennel Club and peer reviewed papers listed on our <a href="{R}research/">research page</a>.</p></section>
<section class="card"><h2>Lesson ideas by grade band</h2>
<h3>Kindergarten to grade 2</h3><ul><li><b>Needs of a dog (K-LS1-1):</b> look at photos of dogs eating, drinking and resting, list what every dog needs, then complete the <a href="{R}teachers/dog-needs-worksheet.html">worksheet</a>. Extend: compare with what a plant needs.</li><li><b>Safe snacks sort:</b> play <a href="{R}games/snack-or-nope/">Snack or Nope?</a> together on the board and talk about why some human foods are not safe for dogs.</li></ul>
<h3>Grades 3 to 5</h3><ul><li><b>How dogs sense the world (4-LS1-2):</b> read the <a href="{R}teachers/dog-senses-fact-sheet.html">fact sheet</a>, then have groups draw a model showing a dog seeing a ball, the information reaching its brain, and how it responds.</li><li><b>Reading signals:</b> play <a href="{R}games/wag-signals/">Wag Signals</a> as a class and record which body parts gave the best clues.</li><li><b>Traits in a litter (3-LS3-1):</b> use the <a href="{R}teachers/dog-traits-worksheet.html">traits worksheet</a> data table to compare puppies and parents.</li></ul>
<h3>Grades 6 to 8</h3><ul><li><b>Selective breeding (MS-LS4-5):</b> students research how breed groups were developed for jobs such as herding, hunting or guarding, using the <a href="{R}breeds.html">breed groups guide</a> and the AKC, then complete part B of the <a href="{R}teachers/dog-traits-worksheet.html">traits worksheet</a>.</li><li><b>Test the toy color claim:</b> play <a href="{R}games/fetch-spotter/">Fetch Spotter</a>, read <a href="{R}blog/can-dogs-see-color.html">Can dogs see color?</a>, and design a fair test of which ball color is easiest to spot on grass.</li></ul>
<h3>Grades 9 to 12</h3><ul><li><b>Reading real science:</b> students pick a paper from our <a href="{R}research/">research page</a>, find the question, method, sample size and main finding, and judge how far the result can be generalized (for example, a study of one breed). No NGSS code is claimed for this activity.</li></ul></section>
<section class="card"><h2>Games as classroom activities</h2><ul><li><a href="{R}games/snack-or-nope/">Snack or Nope?</a> food safety sorting, about 10 minutes.</li><li><a href="{R}games/wag-signals/">Wag Signals</a> body language quiz, about 10 minutes.</li><li><a href="{R}games/fetch-spotter/">Fetch Spotter</a> timing game with dog vision facts, about 5 minutes.</li></ul><p>All games are free, need no accounts and collect no student data. Best scores stay in the browser only.</p></section>
<section class="card" id="vocabulary"><h2>Vocabulary list</h2><dl>
<dt>Breed</dt><dd>A group of dogs with a shared look and set of traits, developed by people through selective breeding.</dd>
<dt>Trait</dt><dd>A feature of a living thing, such as coat color, ear shape or size.</dd>
<dt>Inherited</dt><dd>Passed from parents to their offspring.</dd>
<dt>Variation</dt><dd>Differences between individuals of the same kind, such as puppies in one litter.</dd>
<dt>Selective breeding (artificial selection)</dt><dd>When people choose which animals have offspring, to pass on traits they want.</dd>
<dt>Cone cell</dt><dd>A cell in the eye that works in bright light and detects color. Dogs have two kinds; most people have three.</dd>
<dt>Rod cell</dt><dd>A very sensitive cell in the eye that works in low light and helps detect movement.</dd>
<dt>Dichromatic</dt><dd>Having two types of cone cells, so seeing color through two channels.</dd>
<dt>Body language</dt><dd>How an animal communicates with its posture, face, ears, tail and movements.</dd>
<dt>Play bow</dt><dd>Chest and front legs down, bottom up: a dog's invitation to play.</dd>
<dt>Whale eye</dt><dd>When a dog shows a lot of the white of its eye, a sign of tension.</dd>
<dt>Toxic</dt><dd>Poisonous; able to cause harm or illness.</dd>
</dl><p>More terms in our <a href="{R}glossary.html">dog glossary</a>.</p></section>
<section class="card"><h2>For older students and researchers</h2><p>Our <a href="{R}research/">research page</a> lists the peer reviewed papers and veterinary guidelines behind our articles, with DOIs. Fact articles include a <b>Cite this page</b> box in APA, MLA and Chicago style.</p></section>
""" + NOADS,
         h1="Dog science for teachers", kind="webpage", nav="teachers/",
         lead="Free, print friendly dog science for classrooms: fact sheets and worksheets with answer keys, lesson ideas by grade band linked to NGSS where they fit, a vocabulary list and three classroom games. No sign up, no ads, no student data.",
         extra_head=lr("teachers/index.html", "SnoutsWise dog science resources for teachers", "Printable dog worksheets, fact sheets, lesson ideas, vocabulary and games for K to 12 classrooms.",
                       ["Kindergarten", "Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8", "High school"], ["Lesson plan", "Worksheet"], list(NGSS)),
         related=[("research/index.html", "Research behind SnoutsWise"), ("games/index.html", "Dog games"), ("glossary.html", "Dog glossary"), ("breeds.html", "Breed groups")],
         crumbs=[("index.html", "Home"), ("teachers/index.html", "Teachers")])

    # ------------- K-2 WORKSHEET
    page("teachers/dog-needs-worksheet.html", "What Does a Dog Need? Free K-2 Worksheet with Answer Key | SnoutsWise",
         "Free printable kindergarten to grade 2 worksheet: what a dog needs to live and grow, safe and unsafe foods, with an answer key. Linked to NGSS K-LS1-1.",
         PRINT + """
<section class="card printable"><h2>Name: ____________________ &nbsp; Date: __________</h2>
<h3>Part 1. Circle the things every dog needs to live and grow.</h3>
<ol><li>Food &nbsp;&nbsp; 2. Water &nbsp;&nbsp; 3. A video game &nbsp;&nbsp; 4. A safe place to rest &nbsp;&nbsp; 5. A hat</li></ol>
<h3>Part 2. Draw a line from the dog to what it needs.</h3>
<p>Thirsty dog &nbsp;&#8594;&nbsp; ______________ &nbsp;&nbsp;&nbsp; Hungry dog &nbsp;&#8594;&nbsp; ______________ &nbsp;&nbsp;&nbsp; Sleepy dog &nbsp;&#8594;&nbsp; ______________</p>
<p class="gnote">Word bank: water, a bed, dog food</p>
<h3>Part 3. Safe or not safe? Write S for safe or N for not safe.</h3>
<p>___ Grapes &nbsp;&nbsp; ___ Plain carrot &nbsp;&nbsp; ___ Chocolate &nbsp;&nbsp; ___ Plain apple slice (no seeds) &nbsp;&nbsp; ___ Onion</p>
<h3>Part 4. Draw a dog and its water bowl.</h3><div style="height:180px;border:3px dashed #9AA6F5;border-radius:18px"></div>
</section>
<section class="card"><h2>Answer key (for teachers)</h2><ol>
<li>Part 1: food, water and a safe place to rest. All animals need food in order to live and grow, and all living things need water (NGSS K-LS1-1).</li>
<li>Part 2: thirsty dog: water; hungry dog: dog food; sleepy dog: a bed.</li>
<li>Part 3: grapes N, plain carrot S, chocolate N, plain apple slice without seeds S, onion N. The ASPCA lists grapes, chocolate and onions as foods to keep away from pets; the American Kennel Club lists plain carrots and apple slices (without seeds or core) as safe treats in moderation.</li>
<li>Part 4: any drawing showing a dog with water.</li></ol>
<p>Want a game version? Play <a href="{R}games/snack-or-nope/">Snack or Nope?</a> on the class screen.</p></section>
""" + ngss_box(["K-LS1-1"]) + NOADS,
         h1="Worksheet: What does a dog need?", kind="webpage", nav="teachers/",
         lead="A one page worksheet for kindergarten to grade 2 about what dogs need to live and grow, plus a safe or not safe food check. Answer key below the worksheet.",
         extra_head=lr("teachers/dog-needs-worksheet.html", "What does a dog need? Worksheet", "K to 2 worksheet on animal needs and safe foods for dogs, with answer key.", ["Kindergarten", "Grade 1", "Grade 2"], "Worksheet", ["K-LS1-1"]),
         sources=[S["aspca_foods"], S["akc_fruit"], S["akc_food"]],
         related=[("teachers/index.html", "All teacher resources"), ("can-dogs-eat.html", "Can my dog eat this?"), ("care.html", "Dog care basics")],
         crumbs=crumbs("teachers/dog-needs-worksheet.html", "What does a dog need?"))

    # ------------- 3-5 FACT SHEET
    page("teachers/dog-senses-fact-sheet.html", "Dog Senses and Body Language Fact Sheet for Grades 3-5 | SnoutsWise",
         "Free printable fact sheet for grades 3 to 5: how dogs see color, why they notice movement, and how they show feelings with body language. Quiz and answer key included. NGSS 4-LS1-2.",
         PRINT + """
<section class="card printable"><h2>Dog senses and body language: fact sheet</h2>
<h3>How dogs see</h3><ul>
<li>Dogs do not see only in black and white. They can make out yellow and blue, and mixes of those colors (American Kennel Club).</li>
<li>Dog eyes have two kinds of cone cells for color. Most people have three. Scientists call this dichromatic vision (Neitz, Geist and Jacobs, 1989).</li>
<li>In one experiment, dogs relied on color, not brightness, to choose between colored targets (Kasparson and colleagues, 2013).</li>
<li>Dogs have more rod cells than cone cells. Rods work in low light and help catch movement (American Kennel Club).</li>
<li>Red and orange toys are hard for dogs to see on green grass; yellow and blue are easier (American Kennel Club).</li></ul>
<h3>How dogs show feelings</h3><ul>
<li>A relaxed dog has a loose body, an open relaxed mouth and ears in a natural position (RSPCA).</li>
<li>A play bow, chest down and bottom up, invites play (ASPCApro).</li>
<li>A worried dog may hold its body and head low, tuck its tail, put its ears back, yawn or lick its lips (RSPCA, ASPCApro).</li>
<li>A stiff body, raised hair and a stiff, high tail are warnings to give a dog space (RSPCA).</li></ul>
<h3>Quick quiz</h3><ol>
<li>How many kinds of cone cells do dogs have? ______</li>
<li>Name two colors dogs can see well. ______ and ______</li>
<li>What kind of eye cell helps dogs notice movement in low light? ______</li>
<li>A dog has its chest down and its bottom up. What does it want? ______________</li>
<li>Model it: draw arrows to show a dog seeing a ball, its brain getting the information, and the dog running to fetch it.</li></ol>
</section>
<section class="card"><h2>Answer key (for teachers)</h2><ol><li>Two.</li><li>Yellow and blue.</li><li>Rod cells.</li><li>To play (a play bow).</li><li>Eyes (sense) &#8594; brain (processes the information) &#8594; legs and body (respond by running to the ball). This mirrors NGSS 4-LS1-2: senses, brain, response.</li></ol>
<p>Follow up with <a href="{R}games/wag-signals/">Wag Signals</a> and <a href="{R}games/fetch-spotter/">Fetch Spotter</a>.</p></section>
""" + ngss_box(["4-LS1-2"]) + NOADS,
         h1="Fact sheet: Dog senses and body language", kind="webpage", nav="teachers/",
         lead="A printable fact sheet for grades 3 to 5 on how dogs see and how they show feelings, with a five question quiz and answer key.",
         extra_head=lr("teachers/dog-senses-fact-sheet.html", "Dog senses and body language fact sheet", "Grades 3 to 5 fact sheet and quiz on dog vision and body language, with answer key.", ["Grade 3", "Grade 4", "Grade 5"], "Worksheet", ["4-LS1-2"]),
         sources=[AKC_COLOR, S["neitz1989"], S["kasparson2013"], RSPCA, ASPCAPRO],
         related=[("teachers/index.html", "All teacher resources"), ("blog/can-dogs-see-color.html", "Can dogs see color?"), ("behavior.html", "Dog behavior")],
         crumbs=crumbs("teachers/dog-senses-fact-sheet.html", "Dog senses fact sheet"))

    # ------------- 3-8 TRAITS WORKSHEET
    page("teachers/dog-traits-worksheet.html", "Dog Traits, Breeds and Selective Breeding Worksheet (Grades 3-8) | SnoutsWise",
         "Free printable worksheet: compare traits of puppies and parents, then explore how selective breeding created dog breeds for different jobs. Answer key included. NGSS 3-LS3-1 and MS-LS4-5.",
         PRINT + """
<section class="card printable"><h2>Name: ____________________ &nbsp; Date: __________</h2>
<h3>Part A (grades 3 to 5). Traits in a family</h3>
<p>Here is made up data for a mother dog, a father dog and their four puppies.</p>
<div class="tablewrap"><table><thead><tr><th>Dog</th><th>Coat color</th><th>Ear shape</th><th>Coat length</th></tr></thead><tbody>
<tr><td>Mother</td><td>Black</td><td>Floppy</td><td>Short</td></tr><tr><td>Father</td><td>Yellow</td><td>Floppy</td><td>Short</td></tr>
<tr><td>Puppy 1</td><td>Black</td><td>Floppy</td><td>Short</td></tr><tr><td>Puppy 2</td><td>Yellow</td><td>Floppy</td><td>Short</td></tr>
<tr><td>Puppy 3</td><td>Black</td><td>Floppy</td><td>Short</td></tr><tr><td>Puppy 4</td><td>Black</td><td>Floppy</td><td>Short</td></tr></tbody></table></div>
<ol><li>Which trait is the same in every dog? ______________</li><li>Which trait varies among the puppies? ______________</li><li>Where did the puppies get their coat colors from? ______________</li></ol>
<h3>Part B (grades 6 to 8). Breeds made by people</h3>
<p>Read the <a href="{R}breeds.html">breed groups guide</a>. The American Kennel Club sorts breeds into seven groups, many of them named for the jobs the dogs were bred to do.</p>
<ol start="4"><li>Name two AKC breed groups named after a job. ______________ and ______________</li>
<li>Pick one group. What traits would breeders have chosen to help those dogs do that job? ______________</li>
<li>Explain in your own words how selective breeding is different from natural selection. ______________</li></ol>
</section>
<section class="card"><h2>Answer key (for teachers)</h2><ol>
<li>Ear shape and coat length (floppy, short) are the same in every dog.</li>
<li>Coat color varies (black or yellow).</li>
<li>From their parents: offspring inherit traits from their parents (NGSS 3-LS3-1). The data are invented for practice.</li>
<li>Any two of: Sporting, Hound, Working, Herding (the other AKC groups are Terrier, Toy and Non-Sporting). See the AKC groups article.</li>
<li>Accept reasoned answers, for example herding dogs selected for responsiveness and stamina, hounds for scenting or speed.</li>
<li>In selective breeding, people choose which animals reproduce to pass on desired traits (NGSS MS-LS4-5, LS4.B); in natural selection, the environment determines which traits help animals survive and reproduce.</li></ol></section>
""" + ngss_box(["3-LS3-1", "MS-LS4-5"]) + NOADS,
         h1="Worksheet: Traits, breeds and selective breeding", kind="webpage", nav="teachers/",
         lead="A two part worksheet: grades 3 to 5 compare traits in a dog family; grades 6 to 8 explore how people created breeds through selective breeding. Answer key included.",
         extra_head=lr("teachers/dog-traits-worksheet.html", "Traits, breeds and selective breeding worksheet", "Grades 3 to 8 worksheet on inherited traits, variation and artificial selection in dogs.", ["Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8"], "Worksheet", ["3-LS3-1", "MS-LS4-5"]),
         sources=[S["akc_groups"], S["rkc_groups"]],
         related=[("teachers/index.html", "All teacher resources"), ("breeds.html", "Breed groups guide"), ("glossary.html", "Glossary")],
         crumbs=crumbs("teachers/dog-traits-worksheet.html", "Traits and breeds worksheet"))

    # ------------- RESEARCH
    rows = "".join('<li><b>%s (%d).</b> %s. <i>%s</i> %s. <a href="https://doi.org/%s" rel="noopener">doi:%s</a><br>%s <span class="gnote">Used in: <a href="{R}%s">%s</a></span></li>' % (
        a, y, t, j, v, d, d, summ, used, used) for a, y, t, j, v, d, summ, used in PAPERS)
    grows = "".join('<li><a href="%s" rel="noopener">%s</a>, %s. <span class="gnote">Used in: <a href="{R}%s">%s</a></span></li>' % (u, t, p, used, used) for t, p, u, used in GUIDES)
    ld = {"@context": "https://schema.org", "@type": "ItemList", "name": "Peer reviewed papers behind SnoutsWise",
          "itemListElement": [{"@type": "ListItem", "position": i + 1, "item": {"@type": "ScholarlyArticle", "name": t, "datePublished": str(y),
                               "isPartOf": {"@type": "Periodical", "name": j}, "sameAs": "https://doi.org/" + d}} for i, (a, y, t, j, v, d, s, u) in enumerate(PAPERS)]}
    page("research/index.html", "Research Behind SnoutsWise: Peer Reviewed Dog Science Papers with DOIs | SnoutsWise",
         "The peer reviewed papers and veterinary guidelines behind SnoutsWise articles, with DOIs and plain language summaries, for students, teachers and researchers.",
         """
<section class="card"><h2>Peer reviewed papers</h2><ol>""" + rows + """</ol><p class="gnote">Each DOI was checked against its Crossref record on 9 October 2026. Summaries are our own plain language descriptions of each paper's abstract.</p></section>
<section class="card"><h2>Veterinary guidelines and position statements</h2><ul>""" + grows + """</ul></section>
<section class="card"><h2>How to cite SnoutsWise</h2><p>Fact articles have a <b>Cite this page</b> box with APA, MLA and Chicago formats. For school work, we recommend citing the original paper or guideline as well as our page.</p></section>
""",
         h1="Research behind SnoutsWise", kind="webpage", nav="teachers/",
         lead="For students and researchers: the peer reviewed papers and veterinary guidelines our articles rely on, with DOIs, plain language summaries and the pages that use them.",
         extra_head='<script type="application/ld+json">%s</script>' % json.dumps(ld, ensure_ascii=False),
         related=[("teachers/index.html", "Teacher resources"), ("about.html", "How we write and source"), ("blog/index.html", "Blog")],
         crumbs=[("index.html", "Home"), ("research/index.html", "Research")])

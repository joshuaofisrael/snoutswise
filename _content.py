"""Page content for Dog Field Guide. Original writing; every factual claim is tied to a listed source."""
import math

S = {
 "aspca_foods": ("People Foods to Avoid Feeding Your Pets", "ASPCA Animal Poison Control", "https://www.aspca.org/pet-care/aspca-poison-control/people-foods-avoid-feeding-your-pets"),
 "merck_choc": ("Chocolate Toxicosis in Animals", "Merck Veterinary Manual", "https://www.merckvetmanual.com/toxicology/food-hazards/chocolate-toxicosis-in-animals"),
 "merck_xyl": ("Xylitol Toxicosis in Dogs", "Merck Veterinary Manual", "https://www.merckvetmanual.com/toxicology/food-hazards/xylitol-toxicosis-in-dogs"),
 "merck_foodpet": ("Food Hazards (pet owner version)", "Merck Veterinary Manual", "https://www.merckvetmanual.com/special-pet-topics/poisoning/food-hazards"),
 "cornell_xyl": ("Xylitol toxicities", "Cornell University College of Veterinary Medicine", "https://www.vet.cornell.edu/departments-centers-and-institutes/riney-canine-health-center/canine-health-topics/xylitol-toxicities"),
 "merck_vitals": ("Normal Physiological Values for Dogs", "Merck Veterinary Manual", "https://www.merckvetmanual.com/multimedia/table/normal-physiological-values-for-dogs"),
 "akc_food": ("People Foods Dogs Can and Can't Eat", "American Kennel Club", "https://www.akc.org/expert-advice/nutrition/human-foods-dogs-can-and-cant-eat/"),
 "akc_fruit": ("Fruits and Vegetables Dogs Can or Can't Eat", "American Kennel Club", "https://www.akc.org/expert-advice/nutrition/fruits-vegetables-dogs-can-and-cant-eat/"),
 "akc_groups": ("The 7 AKC Dog Breed Groups Explained", "American Kennel Club", "https://www.akc.org/expert-advice/lifestyle/7-akc-dog-breed-groups-explained/"),
 "rkc_groups": ("What is a pedigree dog?", "The Royal Kennel Club", "https://www.royalkennelclub.com/your-dog/getting-a-dog/are-you-ready/what-is-a-pedigree-dog/"),
 "aaha_vax": ("2022 AAHA Canine Vaccination Guidelines (updated 2024)", "American Animal Hospital Association", "https://www.aaha.org/resources/2022-aaha-canine-vaccination-guidelines/"),
 "aaha_table": ("Recommendations for core and noncore canine vaccines", "American Animal Hospital Association", "https://www.aaha.org/resources/2022-aaha-canine-vaccination-guidelines/recommendations-for-core-and-noncore-canine-vaccines/"),
 "aaha_cdv": ("Key Vaccination: Canine Distemper Virus", "American Animal Hospital Association", "https://www.aaha.org/resources/2022-aaha-canine-vaccination-guidelines/canine-distemper-virus-cdv/"),
 "avsab_puppy": ("Position Statement on Puppy Socialization", "American Veterinary Society of Animal Behavior", "https://avsab.org/wp-content/uploads/2019/01/Puppy-Socialization-Position-Statement-FINAL.pdf"),
 "avsab_train": ("Position Statement on Humane Dog Training (2021)", "American Veterinary Society of Animal Behavior", "https://avsab.org/wp-content/uploads/2021/08/AVSAB-Humane-Dog-Training-Position-Statement-2021.pdf"),
 "mech": ("Mech LD (1999). Alpha status, dominance, and division of labor in wolf packs. Canadian Journal of Zoology 77(8):1196 to 1203", "U.S. Geological Survey record", "https://pubs.usgs.gov/publication/1001725"),
 "wsava_bcs": ("Body Condition Score: Dog (chart)", "World Small Animal Veterinary Association", "https://wsava.org/wp-content/uploads/2020/01/Body-Condition-Score-Dog.pdf"),
 "penn_kealy": ("Study finds dogs fed a reduced calorie diet live nearly two years longer (Kealy et al., 2002)", "Penn Today, University of Pennsylvania", "https://penntoday.upenn.edu/news/study-finds-dogs-fed-reduced-calorie-diet-live-nearly-two-years-longer-dogs-unrestricted-diet"),
 "avma_dental": ("Pet dental care", "American Veterinary Medical Association", "https://www.avma.org/resources-tools/pet-owners/petcare/pet-dental-care"),
 "rspca_heat": ("Heatstroke in dogs", "RSPCA", "https://www.rspca.org.uk/adviceandwelfare/pets/dogs/health/heatstroke"),
 "gov_chip": ("Get your dog or cat microchipped", "GOV.UK", "https://www.gov.uk/get-your-dog-microchipped"),
 "wang2020": ("Wang T, et al. (2020). Quantitative Translation of Dog-to-Human Aging by Conserved Remodeling of the DNA Methylome. Cell Systems 11:176 to 185", "PubMed Central (open access)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC7484147/"),
}
def src(*keys):
    return [S[k] for k in keys]

def register(page):
    home(page); breeds(page); care(page); health(page); training(page); behavior(page)
    can_dogs_eat(page); age_calc(page); faq(page); glossary(page); trust(page); blog(page)

# ------------------------------------------------------------------ HOME
def home(page):
    body = """
<section class="hero"><h1>Dog Field Guide: plain answers about breeds, care, health, training and behavior</h1>
<p class="lead">Dog Field Guide is a free, independent guide for dog owners. It explains breed groups, everyday care, health basics such as vaccines and normal vital signs, reward based training and dog behavior, and every page lists the veterinary and kennel club sources it relies on. Start with the tools below if you have an urgent question.</p>
<a class="btn" href="{R}can-dogs-eat.html">Can my dog eat this? Food lookup</a> <a class="btn alt" href="{R}dog-age-calculator.html">Dog age calculator</a></section>
<h2>Tools</h2>
<div class="grid">
<a class="tile" href="{R}can-dogs-eat.html"><h3>Can my dog eat this?</h3><p>Our signature lookup: about 70 foods rated Safe, Caution or Toxic, with the reason, the source and what to do if eaten.</p></a>
<a class="tile" href="{R}dog-age-calculator.html"><h3>Dog age in human years</h3><p>Calculator based on the 2020 epigenetic clock study, not the old "times seven" rule.</p></a>
<a class="tile" href="{R}blog/dog-ate-chocolate.html"><h3>Dog ate chocolate?</h3><p>Estimate the dose from the type and amount, then call your vet.</p></a>
</div>
<h2>Guides</h2>
<div class="grid">
<a class="tile" href="{R}breeds.html"><h3>Breeds and breed groups</h3><p>What the AKC and Royal Kennel Club groups mean and how to choose a breed.</p></a>
<a class="tile" href="{R}care.html"><h3>Everyday care</h3><p>Feeding, weight, exercise, grooming, teeth, ID and hot weather.</p></a>
<a class="tile" href="{R}health.html"><h3>Health basics</h3><p>Normal vital signs, vaccines, warning signs and when to call a vet.</p></a>
<a class="tile" href="{R}training.html"><h3>Training</h3><p>How reward based training works and the first skills to teach.</p></a>
<a class="tile" href="{R}behavior.html"><h3>Behavior</h3><p>Body language, socialization, the dominance myth and problem behaviors.</p></a>
<a class="tile" href="{R}faq.html"><h3>Dog FAQ</h3><p>Short, sourced answers to common dog questions.</p></a>
<a class="tile" href="{R}glossary.html"><h3>Glossary</h3><p>Plain English definitions of dog and veterinary terms.</p></a>
<a class="tile" href="{R}blog/"><h3>Blog</h3><p>Answer first articles on one question at a time.</p></a>
</div>
<section class="card"><h2>Quick facts</h2><ul>
<li>A healthy adult dog's average body temperature is about 101 to 102.5&deg;F (38.3 to 39.2&deg;C), and its resting breathing rate is about 18 to 34 breaths a minute (<a href="{R}health.html#vitals">more on normal vital signs</a>).</li>
<li>Grapes, raisins, onions, garlic, chocolate, macadamia nuts and the sweetener xylitol are all on the ASPCA's list of foods to keep away from dogs (<a href="{R}can-dogs-eat.html">see the full table</a>).</li>
<li>The American Veterinary Society of Animal Behavior calls the first three months of life the primary window for puppy socialization (<a href="{R}blog/puppy-socialization-window.html">how to use it safely</a>).</li>
<li>In a 14 year study of Labrador retrievers, dogs fed 25 percent less than their littermates lived a median 1.8 years longer (<a href="{R}blog/is-my-dog-overweight.html">how to check your dog's weight</a>).</li>
</ul></section>
<section class="card"><h2>Latest from the blog</h2><ul>
<li><a href="{R}blog/dog-ate-chocolate.html">My dog ate chocolate: how much is dangerous?</a></li>
<li><a href="{R}blog/puppy-socialization-window.html">The puppy socialization window: when it closes and what to do</a></li>
<li><a href="{R}blog/dog-vaccine-schedule.html">How often do dogs need vaccines? Core and non core vaccines explained</a></li>
<li><a href="{R}blog/alpha-dog-myth.html">Is the "alpha dog" idea true? What the research says</a></li>
<li><a href="{R}blog/is-my-dog-overweight.html">Is my dog overweight? How to use the 9 point body condition score</a></li>
</ul></section>
<p class="note">Dog Field Guide is general education, not veterinary advice. If your dog may have eaten something toxic or seems unwell, contact your vet or an emergency vet now. In the US, the ASPCA Animal Poison Control Center is on (888) 426-4435.</p>
"""
    page("index.html", "Dog Field Guide: Dog Breeds, Care, Health, Training & Behavior",
         "Free, sourced guide for dog owners: breed groups, care, health basics, reward based training, behavior, a can dogs eat this food table and a dog age calculator.",
         body, kind="home")

# ------------------------------------------------------------------ BREEDS
def breeds(page):
    body = """
<nav class="jump" aria-label="On this page"><b>Jump to:</b> <a href="#akc">AKC groups</a> &middot; <a href="#rkc">Royal Kennel Club groups</a> &middot; <a href="#compare">Side by side</a> &middot; <a href="#choosing">Choosing a breed</a> &middot; <a href="#mixed">Mixed breeds and rescue dogs</a></nav>
<section id="akc"><h2>The seven AKC breed groups</h2>
<p>The American Kennel Club (AKC) shows its recognized breeds in seven groups, and each group is organized by the original work its breeds were developed to do. The best dog in each group goes on to compete for Best in Show.</p>
<div class="tablewrap"><table><thead><tr><th>AKC group</th><th>Original purpose</th><th>Examples the AKC gives</th></tr></thead><tbody>
<tr><td>Sporting</td><td>Helping hunters find and retrieve feathered game; retrievers for waterfowl, setters, spaniels and pointers for upland birds</td><td>Labrador Retriever, German Shorthaired Pointer, Cocker Spaniel</td></tr>
<tr><td>Hound</td><td>Pursuing warm blooded quarry, either by sight and speed (sighthounds) or by scent (scenthounds)</td><td>Bloodhound, Dachshund, Greyhound</td></tr>
<tr><td>Working</td><td>Pulling sleds and carts, guarding flocks and homes, protecting families</td><td>Boxer, Great Dane, Rottweiler</td></tr>
<tr><td>Terrier</td><td>Going to ground after rodents and other vermin, or digging them out</td><td>Bull Terrier, Scottish Terrier, West Highland White Terrier</td></tr>
<tr><td>Toy</td><td>Companionship; small enough to sit in a lap</td><td>Chihuahua, Pug, Shih Tzu</td></tr>
<tr><td>Non-Sporting</td><td>A mixed group of breeds whose jobs do not fit the other six</td><td>Varied; most are kept today as companions</td></tr>
<tr><td>Herding</td><td>Moving livestock such as sheep, cattle and even reindeer</td><td>German Shepherd Dog</td></tr>
</tbody></table></div></section>
<section id="rkc"><h2>The seven Royal Kennel Club groups (UK)</h2>
<p>In the UK, The Royal Kennel Club places each of its 223 recognized breeds in one of seven groups. It says purebred dogs make up around 75 percent of the UK's roughly 9 million dogs.</p>
<div class="tablewrap"><table><thead><tr><th>RKC group</th><th>What the Royal Kennel Club says it covers</th><th>Examples it names</th></tr></thead><tbody>
<tr><td>Gundog</td><td>Dogs originally trained to find and/or retrieve game; split into retrievers, spaniels, hunt point retrieve breeds, and pointers and setters</td><td>(retrievers, spaniels, pointers, setters)</td></tr>
<tr><td>Hound</td><td>Breeds used for hunting by scent or by sight</td><td>Beagle and Bloodhound (scent); Whippet and Greyhound (sight)</td></tr>
<tr><td>Pastoral</td><td>Herding dogs associated with cattle, sheep, reindeer and other cloven footed animals; often a weatherproof double coat</td><td>The Collie family, Old English Sheepdog, Samoyed</td></tr>
<tr><td>Terrier</td><td>Dogs bred to hunt vermin; the name comes from the Latin <i>terra</i>, earth</td><td>(many terrier breeds)</td></tr>
<tr><td>Toy</td><td>Small companion or lap dogs, some placed here simply because of their size</td><td>(small companion breeds)</td></tr>
<tr><td>Utility</td><td>Miscellaneous breeds, mainly of non sporting origin, each bred for a specific function</td><td>Bulldog, Dalmatian, Akita, Poodle</td></tr>
<tr><td>Working</td><td>Breeds developed as guards and search and rescue dogs</td><td>Boxer, Great Dane, St Bernard</td></tr>
</tbody></table></div></section>
<section id="compare" class="card"><h2>AKC and Royal Kennel Club groups side by side</h2>
<p>The two systems line up closely but use different names. Roughly: AKC Sporting is the RKC Gundog group, AKC Herding is the RKC Pastoral group, and AKC Non-Sporting is closest to the RKC Utility group. Hound, Terrier, Toy and Working exist in both. Individual breeds can sit in different groups in different countries, so check the breed on the relevant kennel club's own site.</p></section>
<section id="choosing"><h2>How to choose a breed (a practical checklist)</h2>
<p>The Royal Kennel Club's advice is to learn what job a breed was developed to do, because that explains much of its natural behavior. A breed made to work all day will usually need more to do than one bred as a lap companion. Use the group tables above as a starting point, then ask:</p>
<ol>
<li><b>What was the breed made for?</b> Herding, retrieving, guarding, chasing by sight or following a scent all shape how a dog behaves at home and on walks.</li>
<li><b>How much time can you give each day</b> for exercise, training and play, every day, in all weather?</li>
<li><b>Coat care.</b> Some coats need regular brushing or professional grooming; ask breeders or the breed club what is involved.</li>
<li><b>Size and space.</b> Think about car space, stairs, lifting an older dog and the cost of food and medicine, which rise with body weight.</li>
<li><b>Health.</b> The Royal Kennel Club notes that many breeds have DNA tests or screening schemes. Ask to see the parents' health test results for the conditions relevant to that breed.</li>
<li><b>Heat tolerance.</b> The RSPCA lists flat faced (brachycephalic) breeds among the dogs most at risk of heatstroke because they cannot pant as effectively. See our <a href="{R}care.html#heat">hot weather advice</a>.</li>
</ol></section>
<section id="mixed"><h2>Mixed breeds and rescue dogs</h2>
<p>Breed groups describe tendencies, not guarantees: individual dogs vary, and many wonderful dogs are mixes. When you meet a rescue dog, the rescue's notes on how that particular dog behaves with people, other dogs, children and being left alone usually tell you more than a guess at its ancestry. Whatever dog you choose, early <a href="{R}behavior.html#socialization">socialization</a> and <a href="{R}training.html">reward based training</a> matter more than the label.</p></section>
"""
    page("breeds.html", "Dog Breed Groups Explained: AKC vs Royal Kennel Club | Dog Field Guide",
         "The seven AKC and seven Royal Kennel Club dog breed groups compared side by side, what each was bred for, and a practical checklist for choosing a breed.",
         body, h1="Dog breeds and breed groups explained",
         lead="Kennel clubs sort dog breeds into groups based on the work they were originally bred to do. The American Kennel Club uses seven groups (Sporting, Hound, Working, Terrier, Toy, Non-Sporting and Herding) and The Royal Kennel Club in the UK also uses seven (Gundog, Hound, Pastoral, Terrier, Toy, Utility and Working). A breed's original job is one of the best clues to how much exercise, training and company it will need.",
         sources=src("akc_groups", "rkc_groups", "rspca_heat"),
         related=[("care.html", "Everyday dog care"), ("training.html", "Reward based training"), ("behavior.html", "Dog behavior"), ("faq.html", "Dog FAQ"), ("glossary.html", "Glossary")],
         crumbs=[("index.html", "Home"), ("breeds.html", "Breeds")])

# ------------------------------------------------------------------ CARE
def care(page):
    body = """
<nav class="jump" aria-label="On this page"><b>Jump to:</b> <a href="#feeding">Feeding</a> &middot; <a href="#weight">Weight</a> &middot; <a href="#exercise">Exercise and enrichment</a> &middot; <a href="#teeth">Teeth</a> &middot; <a href="#grooming">Grooming</a> &middot; <a href="#id">ID and microchips</a> &middot; <a href="#heat">Hot weather</a> &middot; <a href="#home">Home hazards</a></nav>
<section id="feeding"><h2>Feeding</h2>
<p>Most dogs do best on a complete and balanced dog food as their main diet; the American Kennel Club advises that people food should only ever be an occasional, plain treat and never a replacement for it. Introduce any new food slowly, one at a time, in small amounts. Fresh water should always be available.</p>
<p>Some common foods are dangerous to dogs: chocolate, grapes and raisins, onions, garlic and chives, macadamia nuts, alcohol, raw yeast dough and anything sweetened with xylitol all appear on the ASPCA's list of foods to avoid. Our <a href="{R}can-dogs-eat.html">Can dogs eat this?</a> table covers more than 50 foods.</p></section>
<section id="weight"><h2>Keeping a healthy weight</h2>
<p>Vets assess weight with a body condition score rather than the scale alone. On the 9 point scale used on the WSAVA chart, an ideal dog (score 4 to 5) has ribs you can feel without excess fat, a waist visible from above and a tucked up belly seen from the side. Keeping dogs lean matters: in a 14 year study of 48 Labrador retrievers, the dogs fed 25 percent less than their littermates lived a median of 13 years compared with 11.2 years, and developed hip osteoarthritis later. See <a href="{R}blog/is-my-dog-overweight.html">how to body condition score your dog</a>.</p></section>
<section id="exercise"><h2>Exercise and enrichment</h2>
<p>How much exercise a dog needs depends on its age, health and breed type (see <a href="{R}breeds.html#choosing">what a breed was made for</a>). Daily walks, sniffing time, play and short training sessions all count. Mental work matters as well as physical: food puzzle toys, scatter feeding and learning new cues give dogs something to do. The AVSAB recommends teaching puppies to spend some time playing alone with favorite toys, such as stuffed food toys, or resting in a safe place, which helps them learn to settle without you.</p></section>
<section id="teeth"><h2>Teeth</h2>
<p>The American Veterinary Medical Association says periodontal disease is the most common dental condition in dogs, and that by about 3 years old most dogs will very likely show early signs of it. Its advice:</p>
<ul><li>Brushing is the single most effective thing you can do at home. Daily is best, but several times a week can be effective.</li>
<li>Have your vet check your dog's teeth at least once a year.</li>
<li>Book a check sooner for bad breath, broken or loose teeth, tartar, dropping food, drooling, reduced appetite, pain, bleeding or swelling around the mouth.</li>
<li>The American Veterinary Dental College does not recommend "anesthesia free" cleanings, because they cannot clean or inspect below the gumline, where most dental disease happens.</li></ul></section>
<section id="grooming"><h2>Grooming</h2>
<p>Grooming needs vary hugely between coat types. Regular brushing removes loose hair and lets you spot lumps, ticks, skin problems and sore paws early. Check ears and nails as part of the routine and get your dog used to being handled all over from puppyhood, which the AVSAB recommends as part of socialization. If grooming causes fear or pain, stop and ask your vet or a groomer for help rather than forcing it.</p></section>
<section id="id"><h2>ID and microchips</h2>
<p>A microchip and an up to date registration greatly improve the chance of getting a lost dog back. In the UK it is the law: all dogs must be microchipped and registered on an approved database by 8 weeks old, owners must keep the details up to date, and a dog must also wear a collar and tag with the owner's name and address in a public place. Rules differ in other countries, so check locally.</p></section>
<section id="heat"><h2>Hot weather and heatstroke</h2>
<p>The RSPCA warns that heatstroke can kill. Dogs most at risk include flat faced breeds, dogs with thick coats, puppies, older dogs and dogs with breathing problems. Warning signs include heavy or noisy panting, thick drooling, red gums and tongue, weakness, confusion, vomiting or diarrhea, muscle spasms, seizures and collapse.</p>
<p><b>Cool first, transport second.</b> The RSPCA's advice is to stop exercise, get the dog into shade, pour water that is cooler than the dog over its neck, belly and thighs (not its head), fan it, and then take it to the nearest vet in a cool, ventilated car, calling ahead. Do not lay wet towels over a dog, as they can trap heat. Never leave a dog in a parked car on a warm day.</p></section>
<section id="home"><h2>Common hazards at home</h2>
<ul><li>Sugar free gum, sweets, some peanut butters and baked goods can contain xylitol, which can cause dangerously low blood sugar in dogs (<a href="{R}can-dogs-eat.html#xylitol">details</a>).</li>
<li>Chocolate and cocoa products, especially baking chocolate and cocoa powder (<a href="{R}blog/dog-ate-chocolate.html">chocolate dose estimator</a>).</li>
<li>Bins containing bones, corn cobs, fruit pits or grapes; the AKC warns that cobs, pits and cooked poultry bones can cause blockages or injuries.</li>
<li>Raw bread dough, which can expand in the stomach and produce alcohol, according to the ASPCA.</li></ul></section>
"""
    page("care.html", "Dog Care Basics: Feeding, Weight, Teeth, Grooming & Safety | Dog Field Guide",
         "Everyday dog care with sources: what to feed, keeping a healthy weight, exercise, brushing teeth, grooming, microchip rules and how to cool a dog with heatstroke.",
         body, h1="Dog care basics",
         lead="Good everyday care comes down to a complete and balanced diet, keeping your dog lean, daily exercise and mental stimulation, regular tooth brushing, grooming suited to the coat, permanent ID, and protecting your dog from heat and household toxins. The sections below explain each one and link to the veterinary sources behind the advice.",
         sources=src("akc_food", "aspca_foods", "wsava_bcs", "penn_kealy", "avsab_puppy", "avma_dental", "gov_chip", "rspca_heat"),
         related=[("health.html", "Dog health basics"), ("can-dogs-eat.html", "Can dogs eat this? food table"), ("blog/is-my-dog-overweight.html", "Is my dog overweight?"), ("breeds.html", "Breed groups"), ("training.html", "Training")],
         crumbs=[("index.html", "Home"), ("care.html", "Care")])

# ------------------------------------------------------------------ HEALTH
def health(page):
    body = """
<nav class="jump" aria-label="On this page"><b>Jump to:</b> <a href="#vitals">Normal vital signs</a> &middot; <a href="#emergency">When to call a vet now</a> &middot; <a href="#vaccines">Vaccines</a> &middot; <a href="#poisoning">Poisoning</a> &middot; <a href="#heatstroke">Heatstroke</a> &middot; <a href="#teeth">Teeth</a> &middot; <a href="#weight">Weight</a> &middot; <a href="#checkups">Checkups</a></nav>
<section id="vitals" class="card"><h2>Normal vital signs for dogs</h2>
<div class="tablewrap"><table><thead><tr><th>Measure</th><th>Normal range (Merck Veterinary Manual)</th></tr></thead><tbody>
<tr><td>Body temperature (average)</td><td>101 to 102.5&deg;F (38.3 to 39.2&deg;C)</td></tr>
<tr><td>Heart rate</td><td>70 to 120 beats per minute; small dogs have faster heart rates than large dogs</td></tr>
<tr><td>Breathing rate at rest</td><td>18 to 34 breaths per minute</td></tr>
<tr><td>Average lifespan</td><td>8 to 16 years, depending on breed</td></tr>
</tbody></table></div>
<p>To count breaths, watch your dog's chest rise and fall while it is relaxed or asleep and count for 30 seconds, then double it. Knowing your own dog's normal numbers when it is well makes changes easier to spot.</p></section>
<section id="emergency"><h2>When to call a vet straight away</h2>
<p>Trust your instincts: you know your dog. Contact a vet or emergency vet immediately if your dog:</p>
<ul><li>has eaten, or may have eaten, something toxic (chocolate, grapes or raisins, xylitol, medicines, rat bait and so on), even if it seems fine now;</li>
<li>collapses, has a seizure, or is suddenly weak, wobbly or confused;</li>
<li>is struggling to breathe or breathing noisily, or has pale, blue or very red gums;</li>
<li>shows signs of heatstroke such as heavy panting, thick drool and weakness (<a href="#heatstroke">cool first</a>, then go);</li>
<li>is repeatedly vomiting, has bloody diarrhea, or has a swollen, hard belly;</li>
<li>has been hit by a car or badly injured, even if it seems to recover.</li></ul></section>
<section id="vaccines"><h2>Vaccines</h2>
<p>The American Animal Hospital Association (AAHA) divides dog vaccines into <b>core</b> vaccines, recommended for all dogs unless there is a medical reason not to, and <b>non core</b> vaccines, recommended for some dogs depending on lifestyle, location and risk. Its core list is canine distemper, adenovirus type 2, parvovirus, leptospirosis (added as core in the 2024 update) and rabies. Non core vaccines include Bordetella (kennel cough), Lyme disease, canine influenza and, in the US, a Western diamondback rattlesnake toxoid.</p>
<div class="tablewrap"><table><thead><tr><th>Vaccine</th><th>Puppy series (AAHA)</th><th>Boosters (AAHA)</th></tr></thead><tbody>
<tr><td>Distemper, adenovirus, parvovirus (with or without parainfluenza)</td><td>At least 3 doses of a combination vaccine between 6 and 16 weeks, 2 to 4 weeks apart</td><td>One dose within a year of the puppy series, then every 3 years</td></tr>
<tr><td>Leptospirosis</td><td>Two doses 2 to 4 weeks apart, from 12 weeks</td><td>One dose within a year, then yearly</td></tr>
<tr><td>Rabies</td><td colspan="2">As required by local law</td></tr>
</tbody></table></div>
<p>These are US guidelines; schedules and legal rules differ by country, and your vet will tailor them to your dog. Read more in <a href="{R}blog/dog-vaccine-schedule.html">How often do dogs need vaccines?</a></p></section>
<section id="poisoning"><h2>Poisoning</h2>
<p>If you think your dog has eaten something toxic, note what it was and how much, then call your vet or a pet poison line straight away; do not wait for symptoms. In the US the ASPCA Animal Poison Control Center number is (888) 426-4435. The Merck Veterinary Manual advises against trying to make a dog vomit at home after xylitol, because blood sugar can fall fast. Check foods in our <a href="{R}can-dogs-eat.html">Can dogs eat this?</a> table, and use the <a href="{R}blog/dog-ate-chocolate.html">chocolate dose estimator</a> while you phone the vet.</p></section>
<section id="heatstroke"><h2>Heatstroke</h2>
<p>The RSPCA's rule is <b>cool first, transport second</b>: stop activity, move the dog into shade, pour water cooler than the dog over its body (avoiding the head), fan it, then drive to a vet in a cool, ventilated car. Do not cover the dog with wet towels. See <a href="{R}care.html#heat">hot weather care</a> for risk factors and warning signs.</p></section>
<section id="teeth"><h2>Teeth</h2>
<p>Periodontal disease is the most common dental condition in dogs, according to the AVMA, which recommends an annual dental check by your vet and regular tooth brushing at home. <a href="{R}care.html#teeth">More on dental care</a>.</p></section>
<section id="weight"><h2>Weight</h2>
<p>Extra weight shortens lives. In the Kealy lifetime study, Labradors kept lean lived a median 1.8 years longer than their heavier littermates and needed treatment for osteoarthritis later. Use the <a href="{R}blog/is-my-dog-overweight.html">body condition score guide</a> to check your dog.</p></section>
<section id="checkups"><h2>Routine checkups</h2>
<p>Regular checkups let your vet review vaccines, parasite prevention, teeth, weight and any lumps or changes you have noticed. The AAHA guidelines say each dog's vaccine needs should be reassessed at least once a year. Write down questions beforehand, and mention changes in appetite, thirst, energy, toileting or behavior; behavior changes can be a sign of pain or illness.</p></section>
"""
    page("health.html", "Dog Health Basics: Normal Vital Signs, Vaccines & Warning Signs | Dog Field Guide",
         "Normal dog temperature, heart rate and breathing rate, core vaccines and booster schedule, emergency warning signs, poisoning and heatstroke first steps.",
         body, h1="Dog health basics",
         lead="A healthy adult dog has an average body temperature of 101 to 102.5&deg;F (38.3 to 39.2&deg;C), a heart rate of 70 to 120 beats per minute and a resting breathing rate of 18 to 34 breaths per minute, according to the Merck Veterinary Manual. The basics of keeping a dog healthy are core vaccines, a lean body weight, dental care, regular checkups and knowing which warning signs mean you should call a vet immediately.",
         sources=src("merck_vitals", "aaha_vax", "aaha_table", "aspca_foods", "merck_foodpet", "rspca_heat", "avma_dental", "penn_kealy"),
         related=[("care.html", "Everyday care"), ("blog/dog-vaccine-schedule.html", "Dog vaccine schedule"), ("can-dogs-eat.html", "Can dogs eat this?"), ("blog/dog-ate-chocolate.html", "Dog ate chocolate"), ("dog-age-calculator.html", "Dog age calculator")],
         crumbs=[("index.html", "Home"), ("health.html", "Health")])

# ------------------------------------------------------------------ TRAINING
def training(page):
    body = """
<nav class="jump" aria-label="On this page"><b>Jump to:</b> <a href="#why">Why reward based</a> &middot; <a href="#how">How it works</a> &middot; <a href="#first">First skills</a> &middot; <a href="#avoid">What to avoid</a> &middot; <a href="#trainer">Choosing a trainer</a></nav>
<section id="why"><h2>Why reward based training</h2>
<p>The American Veterinary Society of Animal Behavior's 2021 position statement summarizes the research this way:</p>
<ul><li><b>It works better.</b> Reward based methods have been shown to be more effective than aversive methods. In one survey study (Hiby and colleagues, 2004) obedience was highest in dogs trained only with rewards, lowest in dogs trained only with aversive methods, and in between for a mix of the two.</li>
<li><b>It is kinder.</b> In observational studies, dogs trained with aversive tools showed more stress behaviors during training, such as a tense or lowered body, lip licking, tail lowering, lifting a front paw, panting, yawning and yelping.</li>
<li><b>It does not create problems.</b> Survey studies link aversive training to later aggression and anxiety. Surveys cannot prove cause and effect, but AVSAB points out that if aversive methods solved problem behaviors, you would expect the opposite pattern.</li>
<li><b>Even for recall.</b> Recall is the most common reason owners use shock collars, yet a 2020 study (China and colleagues) found no difference in the proportion of ignored cues between shock collar training and reward based training, and the reward trained dogs responded faster.</li></ul>
<p>Reward based training does not mean "anything goes". AVSAB stresses that dogs learn best with structure, routine and clear boundaries, taught without fear, intimidation or pain.</p></section>
<section id="how"><h2>How reward based training works</h2>
<p>The idea is simple: behavior that is rewarded is repeated. You make the right choice easy, mark the moment it happens, and pay for it with something your dog values.</p>
<dl>
<dt>Marker</dt><dd>A click from a clicker or a short word such as "yes" that tells the dog exactly which moment earned the reward.</dd>
<dt>Reward</dt><dd>Whatever your dog wants right now: small soft treats, a toy, a game, praise, or access to sniffing or greeting.</dd>
<dt>Luring</dt><dd>Guiding the dog into a position with a treat held at its nose, then fading the lure into a hand signal.</dd>
<dt>Capturing</dt><dd>Marking and rewarding something the dog does on its own, such as lying down on its bed.</dd>
<dt>Shaping</dt><dd>Rewarding small steps toward a final behavior, for example a glance at the mat, then a step onto it, then lying on it.</dd>
<dt>Management</dt><dd>Arranging the environment so the unwanted behavior cannot be practiced while you teach an alternative: a baby gate, a lead, or putting the shoes away.</dd>
</dl>
<p>Keep sessions short (a few minutes), end while your dog is still keen, and practice in easy places before busier ones.</p></section>
<section id="first"><h2>First skills to teach</h2>
<h3>Name and attention</h3><p>Say your dog's name once; the moment it looks at you, mark and reward. Repeat in different rooms, then outside.</p>
<h3>Sit</h3><p>Hold a treat at the dog's nose and move it slowly up and back over its head. As its rear touches the floor, mark and reward. After a few repetitions, make the same movement with an empty hand and reward from your other hand. Add the word "sit" just before the hand signal once the dog is doing it reliably.</p>
<h3>Recall (come when called)</h3><p>Start indoors at short distances. Say your cue in a happy voice, run backwards a couple of steps, and throw a party with a high value treat when your dog reaches you. Never call your dog to something it dislikes, and never punish it when it arrives, however long it took. Use a long line outdoors until the recall is solid.</p>
<h3>Loose lead walking</h3><p>Reward your dog often for being next to you with a slack lead. If the lead tightens, stop and wait, or turn the other way, and reward when it comes back to your side. Let your dog sniff as a reward too.</p>
<h3>Settle on a mat</h3><p>Capture calm: drop a treat between your dog's paws whenever it lies down on its mat, gradually waiting a little longer. This is valuable for cafes, visitors and vet waiting rooms.</p>
<p>For puppies, pair these with a <a href="{R}blog/puppy-socialization-window.html">socialization plan</a>.</p></section>
<section id="avoid"><h2>What to avoid</h2>
<p>AVSAB advises avoiding training tools and techniques that involve:</p>
<ul><li><b>pain</b>: choke chains, prong collars and electronic shock collars;</li>
<li><b>intimidation</b>: squirt bottles, shaker cans, compressed air, shouting, staring, or forceful handling such as "alpha rolls" and "dominance downs";</li>
<li><b>physical correction</b>: lead jerks and physical force;</li>
<li><b>flooding</b>: forcing a dog to stay in a situation that frightens it until it stops reacting.</li></ul>
<p>It lists the documented fallout as increased anxiety and fear related aggression, avoidance and learned helplessness. Read why "being the alpha" is not the answer in <a href="{R}blog/alpha-dog-myth.html">Is the alpha dog idea true?</a></p></section>
<section id="trainer"><h2>Choosing a trainer</h2>
<p>AVSAB recommends trainers who are certified, humane and effective, and suggests watching a class before signing up. It specifically advises against hiring trainers who talk about "dominance", "leader of the pack" or "alpha" theories. For serious problems such as aggression or severe fear, start with your vet, who can rule out pain or illness and refer you to a veterinary behaviorist.</p></section>
"""
    page("training.html", "Reward Based Dog Training: How It Works & First Skills | Dog Field Guide",
         "Why vets recommend reward based dog training, how markers, luring and shaping work, step by step first skills (sit, recall, loose lead) and what tools to avoid.",
         body, h1="Dog training: the reward based approach",
         lead="Veterinary behavior experts recommend reward based training for all dogs: you teach the behavior you want and reward it, instead of punishing mistakes. The American Veterinary Society of Animal Behavior says the evidence shows reward based methods are more effective than aversive ones and better for welfare and the dog and owner relationship, and that there is no evidence aversive training is ever necessary.",
         sources=src("avsab_train", "avsab_puppy", "mech"),
         related=[("behavior.html", "Dog behavior"), ("blog/alpha-dog-myth.html", "The alpha dog myth"), ("blog/puppy-socialization-window.html", "Puppy socialization window"), ("breeds.html", "Breed groups"), ("faq.html", "Dog FAQ")],
         crumbs=[("index.html", "Home"), ("training.html", "Training")])

# ------------------------------------------------------------------ BEHAVIOR
def behavior(page):
    body = """
<nav class="jump" aria-label="On this page"><b>Jump to:</b> <a href="#stress">Stress signals</a> &middot; <a href="#socialization">Socialization</a> &middot; <a href="#dominance">The dominance myth</a> &middot; <a href="#problems">Problem behaviors</a> &middot; <a href="#help">Getting help</a></nav>
<section id="stress"><h2>Reading stress and fear</h2>
<p>Dogs communicate mostly through posture and movement, and the whole body tells you more than any one part. The AVSAB position statement on training lists behaviors that researchers recorded as stress related in dogs:</p>
<div class="tablewrap"><table><thead><tr><th>Signal</th><th>What to look for</th></tr></thead><tbody>
<tr><td>Tense body</td><td>Stiff, frozen or very still posture</td></tr>
<tr><td>Lowered posture</td><td>Crouching, body held low</td></tr>
<tr><td>Lip licking</td><td>Quick flicks of the tongue when no food is around</td></tr>
<tr><td>Tail lowering</td><td>Tail held low or tucked</td></tr>
<tr><td>Lifting a front leg</td><td>One paw raised, often with other signals</td></tr>
<tr><td>Panting</td><td>Panting when not hot or tired</td></tr>
<tr><td>Yawning</td><td>Yawning in a tense situation rather than when sleepy</td></tr>
<tr><td>Yelping</td><td>Sudden high pitched cries</td></tr>
</tbody></table></div>
<p>When you see several of these together, give your dog space and make the situation easier: increase distance, stop what you were doing, or leave. Pushing a frightened dog to "face its fear" is flooding, which AVSAB advises against.</p></section>
<section id="socialization"><h2>Socialization</h2>
<p>The AVSAB calls the first three months of life the primary and most important time for puppy socialization, the period when sociability outweighs fear. Puppies should meet as many new people, well socialized animals, places and experiences as can be achieved safely, without overwhelming them. AVSAB says puppy classes can start as early as 7 to 8 weeks, as long as the puppy has had at least one set of vaccines at least 7 days before the first class, a first deworming, and stays up to date. It warns that incomplete socialization raises the risk of fear, avoidance and aggression later. Full details: <a href="{R}blog/puppy-socialization-window.html">The puppy socialization window</a>.</p></section>
<section id="dominance"><h2>The dominance myth</h2>
<p>The idea that dogs are constantly trying to become "alpha" over their owners traces back to studies of unrelated captive wolves. The wolf biologist L. David Mech, after 13 summers watching wild wolves on Ellesmere Island, concluded that a typical wild pack is a family, with the parents guiding the group. AVSAB advises against trainers who use "dominance", "leader of the pack" or "alpha" explanations and against forceful techniques such as alpha rolls. Most behavior that gets labeled dominance, such as pulling on the lead, jumping up or guarding food, is better explained by what the dog has learned pays off, or by fear. <a href="{R}blog/alpha-dog-myth.html">Read the full explainer</a>.</p></section>
<section id="problems"><h2>Common problem behaviors: a general approach</h2>
<p>AVSAB notes that common issues such as jumping up, barking and house training can be managed by arranging the environment well and rewarding the behavior you want, while more serious concerns such as aggression, anxiety and fear need a treatment plan. A general approach for everyday problems:</p>
<ol><li><b>Rule out pain and illness.</b> Sudden behavior changes can have a medical cause, so see your vet first.</li>
<li><b>Work out what the dog gets from the behavior.</b> Attention, food, play, distance from something scary, or relief from boredom.</li>
<li><b>Manage it.</b> Prevent rehearsal with gates, leads, closed doors or by putting temptations away.</li>
<li><b>Teach and reward an alternative.</b> Sit to greet instead of jumping; go to the mat when the doorbell rings; chew a toy instead of the sofa.</li>
<li><b>Meet the underlying need.</b> More exercise, sniffing, chewing outlets or company, depending on the cause.</li></ol>
<p>AVSAB also recommends teaching puppies to enjoy short periods alone with a stuffed food toy, and offering a wide variety of experiences in the first year, which it links to a lower risk of separation related behavior.</p></section>
<section id="help"><h2>When to get professional help</h2>
<p>Seek help early for aggression, fear that is getting worse, behavior when left alone that leads to injury or damage, or any behavior that puts people or other animals at risk. AVSAB says animals with aggression should be treated with humane methods with no exceptions, and that trainers struggling with a case should refer to a vet, a board certified veterinary behaviorist or a certified applied animal behaviorist.</p></section>
"""
    page("behavior.html", "Dog Behavior Explained: Stress Signals, Socialization & Dominance | Dog Field Guide",
         "How to read stress and fear in dogs, why puppy socialization matters, what research says about dominance and alpha theory, and a step by step approach to problem behavior.",
         body, h1="Dog behavior explained",
         lead="Most dog behavior makes sense once you ask what the dog is feeling and what the behavior gets it. Learn to spot stress signals such as lip licking, yawning, a lowered body and tucked tail; socialize puppies carefully during their first three months; and set aside the old dominance or alpha model, which wolf research and veterinary behaviorists no longer support.",
         sources=src("avsab_train", "avsab_puppy", "mech"),
         related=[("training.html", "Reward based training"), ("blog/alpha-dog-myth.html", "Is the alpha dog idea true?"), ("blog/puppy-socialization-window.html", "Puppy socialization window"), ("health.html", "Health basics"), ("glossary.html", "Glossary")],
         crumbs=[("index.html", "Home"), ("behavior.html", "Behavior")])

# ------------------------------------------------------------------ CAN DOGS EAT
FOODS = [
 # (category, food, verdict[no|caution|yes], why, sources)
 ("Sweets and snacks", "Chocolate (milk and dark)", "no", "Contains theobromine and caffeine (methylxanthines). Darker chocolate is more dangerous. Can cause vomiting, restlessness, a racing heart, tremors and seizures. Use our <a href=\"{R}blog/dog-ate-chocolate.html\">chocolate dose estimator</a> and call your vet.", "aspca_foods merck_choc"),
 ("Sweets and snacks", "Cocoa powder and baking chocolate", "no", "The most concentrated sources: Merck lists about 28.5 mg of methylxanthines per gram in cocoa powder and 15.5 mg/g in unsweetened baking chocolate, versus about 2.3 mg/g in milk chocolate.", "merck_choc"),
 ("Sweets and snacks", "White chocolate", "caution", "Very little theobromine (Merck calls it a negligible source), but it is high in fat and sugar; Merck notes the fat in chocolate products may trigger pancreatitis in susceptible animals.", "merck_choc"),
 ("Sweets and snacks", "Xylitol (sugar free gum, sweets, some peanut butters, baked goods, toothpaste)", "no", "In dogs xylitol triggers a rapid insulin release. Merck links doses above about 100 mg/kg to dangerously low blood sugar and above about 500 mg/kg to possible liver failure. Signs can start within 30 to 60 minutes. Go to a vet immediately; do not make the dog vomit at home.", "aspca_foods merck_xyl merck_foodpet cornell_xyl"),
 ("Sweets and snacks", "Ice cream", "caution", "The AKC advises not sharing it: lots of sugar, and some dogs are lactose intolerant. Frozen dog safe fruit is a better treat.", "akc_food"),
 ("Sweets and snacks", "Salty snacks (crisps, pretzels, salted nuts)", "caution", "Too much salt can cause thirst, vomiting, diarrhea and, in large amounts, tremors and seizures, according to the ASPCA.", "aspca_foods"),
 ("Sweets and snacks", "Popcorn (plain, air popped)", "yes", "OK in moderation if unsalted and unbuttered, according to the AKC. Unpopped kernels are a choking hazard.", "akc_food"),
 ("Sweets and snacks", "Honey", "yes", "The AKC lists honey among foods dogs can eat. It is mostly sugar, so keep it to a small amount.", "akc_food"),
 ("Drinks", "Coffee, tea and caffeinated drinks", "no", "Caffeine is a methylxanthine like the toxins in chocolate; the ASPCA lists vomiting, hyperactivity, abnormal heart rhythm, tremors and seizures as possible effects.", "aspca_foods"),
 ("Drinks", "Alcohol", "no", "Can cause vomiting, incoordination, breathing difficulty, tremors, coma and death. Alcohol is absorbed quickly, so get veterinary help promptly.", "aspca_foods"),
 ("Drinks", "Milk", "caution", "Dogs do not make much lactase, so milk can cause diarrhea or stomach upset. A little is OK for dogs that tolerate it.", "aspca_foods akc_food"),
 ("Fruit", "Grapes", "no", "Can cause kidney damage, and the AKC warns of sudden kidney failure. No amount has been proven safe. Call your vet even if only a few were eaten.", "aspca_foods akc_fruit"),
 ("Fruit", "Raisins (and raisin bread or cakes)", "no", "Dried grapes carry the same kidney risk as grapes.", "aspca_foods akc_food"),
 ("Fruit", "Cherries (whole, pits, stems)", "no", "The AKC warns that apart from the flesh, cherry plants contain cyanide. Watch for dilated pupils, difficulty breathing and red gums after pits are eaten; that is an emergency.", "akc_fruit"),
 ("Fruit", "Avocado", "caution", "The AKC says not to feed it: the pit, skin and leaves contain persin, which can cause vomiting and diarrhea, and the flesh is high in fat. (The ASPCA notes avocado is most dangerous to birds, rabbits, horses and ruminants.) The large pit is also a choking and blockage risk.", "akc_fruit aspca_foods"),
 ("Fruit", "Tomatoes", "caution", "Ripe tomato flesh is generally safe, but the green parts of the plant contain solanine; the AKC suggests skipping tomatoes and keeping dogs out of tomato plants.", "akc_fruit"),
 ("Fruit", "Citrus and oranges", "yes", "Small amounts of the flesh are unlikely to cause more than minor stomach upset (ASPCA). Remove peel and seeds; peels, stems and leaves contain irritating oils.", "aspca_foods akc_fruit"),
 ("Fruit", "Apples", "yes", "Fine as a treat with the core and seeds removed (AKC).", "akc_fruit"),
 ("Fruit", "Bananas", "yes", "OK in moderation; high in sugar, so a treat rather than a staple (AKC).", "akc_fruit"),
 ("Fruit", "Blueberries", "yes", "Safe, small and easy to use as training treats (AKC).", "akc_fruit"),
 ("Fruit", "Strawberries", "yes", "Safe in moderation; they contain natural sugar (AKC).", "akc_fruit"),
 ("Fruit", "Raspberries", "yes", "Safe in moderation. The AKC notes they contain small natural amounts of xylitol, so keep portions small.", "akc_fruit"),
 ("Fruit", "Watermelon", "yes", "The flesh is safe; remove the rind and seeds, which can cause blockages (AKC).", "akc_fruit"),
 ("Fruit", "Cantaloupe (melon)", "yes", "Safe in moderation; high in sugar, so go easy for overweight or diabetic dogs (AKC).", "akc_fruit"),
 ("Fruit", "Mango", "yes", "Safe without the hard pit, which is a choking hazard (AKC). High in sugar.", "akc_fruit"),
 ("Fruit", "Peaches", "yes", "Fresh flesh only. The pit contains cyanide and canned peaches are usually in sugary syrup (AKC).", "akc_fruit"),
 ("Fruit", "Pears", "yes", "Cut into chunks with the pit and seeds removed; skip canned pears in syrup (AKC).", "akc_fruit"),
 ("Fruit", "Pineapple", "yes", "A few chunks with the peel and crown removed; avoid tinned pineapple in syrup (AKC).", "akc_fruit"),
 ("Fruit", "Cranberries (unsweetened)", "yes", "Safe in small amounts; too many can upset the stomach, and dried cranberries for people are often sweetened (AKC).", "akc_fruit"),
 ("Fruit", "Coconut and coconut oil", "caution", "Small amounts are not likely to cause serious harm, but the oils can cause stomach upset and loose stools (ASPCA). Keep the hairy husk away (AKC).", "aspca_foods akc_food"),
 ("Vegetables", "Onions", "no", "Onions are in the Allium family and can damage red blood cells and cause anemia. The AKC says Japanese breeds such as Akitas and Shiba Inus are more severely affected.", "aspca_foods akc_fruit"),
 ("Vegetables", "Garlic", "no", "An Allium, and the AKC says it is significantly more toxic to dogs than other Alliums. Signs can be delayed, so monitor for several days.", "aspca_foods akc_food"),
 ("Vegetables", "Chives and leeks", "no", "Also Alliums, with the same red blood cell risk as onions.", "aspca_foods akc_fruit"),
 ("Vegetables", "Wild mushrooms", "no", "Some wild species are highly poisonous, so treat any wild mushroom as an emergency (AKC).", "akc_fruit"),
 ("Vegetables", "Supermarket mushrooms (plain, washed)", "yes", "The AKC says washed mushrooms sold for people are generally fine for dogs. Avoid garlic, onion or butter in cooking.", "akc_fruit"),
 ("Vegetables", "Corn on the cob", "no", "The cob can cause an intestinal blockage (AKC).", "akc_food"),
 ("Vegetables", "Corn kernels (off the cob)", "yes", "Plain kernels are fine; corn is a common dog food ingredient (AKC).", "akc_food"),
 ("Vegetables", "Carrots", "yes", "A low calorie, crunchy snack (AKC).", "akc_fruit"),
 ("Vegetables", "Green beans", "yes", "Safe raw, steamed or canned as long as they are plain; choose no salt canned beans (AKC).", "akc_fruit"),
 ("Vegetables", "Peas", "yes", "Fresh or frozen peas are OK on occasion; avoid canned peas with added salt (AKC).", "akc_fruit"),
 ("Vegetables", "Cucumber", "yes", "Low calorie and hydrating (AKC).", "akc_fruit"),
 ("Vegetables", "Celery", "yes", "Safe as a crunchy snack; cut into small pieces (AKC).", "akc_fruit"),
 ("Vegetables", "Broccoli", "caution", "Small amounts only. Florets can irritate the stomach and tough stalks have caused blockages in the esophagus; cooked is better (AKC).", "akc_fruit"),
 ("Vegetables", "Brussels sprouts", "yes", "Safe, but can cause a lot of gas (AKC).", "akc_fruit"),
 ("Vegetables", "Spinach", "caution", "Not toxic in normal amounts, but high in oxalic acid; the AKC suggests choosing other vegetables.", "akc_fruit"),
 ("Vegetables", "Asparagus", "caution", "Not unsafe, but too tough raw and of little benefit cooked (AKC).", "akc_fruit"),
 ("Vegetables", "Pumpkin (plain, 100 percent puree)", "yes", "Plain cooked pumpkin or 100 percent pumpkin puree is fine; avoid spiced pie filling (AKC).", "akc_fruit"),
 ("Nuts and seeds", "Macadamia nuts", "no", "Can cause weakness, incoordination, vomiting, tremors and overheating, usually within 12 hours (ASPCA).", "aspca_foods akc_food"),
 ("Nuts and seeds", "Almonds", "no", "The AKC says to avoid them: they can block the esophagus if not chewed, and salted almonds add salt. Their fat can also cause vomiting and pancreatitis (ASPCA).", "akc_food aspca_foods"),
 ("Nuts and seeds", "Walnuts and pecans", "caution", "High in oils and fats that can cause vomiting, diarrhea and possibly pancreatitis (ASPCA).", "aspca_foods"),
 ("Nuts and seeds", "Peanuts (unsalted)", "yes", "Safe in moderation; avoid salted peanuts and large amounts of fat (AKC).", "akc_food"),
 ("Nuts and seeds", "Peanut butter", "yes", "Fine in small amounts, but check the label first: it must not contain xylitol (AKC).", "akc_food"),
 ("Nuts and seeds", "Cashews (unsalted)", "yes", "A few at a time only, unsalted (AKC).", "akc_food"),
 ("Meat, fish and eggs", "Bones (cooked poultry bones, raw bones)", "no", "Bones can splinter or cause blockages and injuries to the gut that may need surgery (ASPCA, AKC).", "aspca_foods akc_food"),
 ("Meat, fish and eggs", "Raw meat and raw eggs", "caution", "Can carry Salmonella and E. coli, harmful to pets and people. Raw egg white can interfere with biotin absorption (ASPCA, AKC).", "aspca_foods akc_food"),
 ("Meat, fish and eggs", "Cooked eggs", "yes", "Fully cooked eggs are safe and a good protein source (AKC).", "akc_food"),
 ("Meat, fish and eggs", "Raw or undercooked fish and salmon", "no", "Can carry parasites that make dogs seriously ill; always cook fish thoroughly (AKC).", "akc_food"),
 ("Meat, fish and eggs", "Cooked fish and salmon (boneless)", "yes", "Fully cooked and cooled, with small bones removed (sardines' soft bones are the exception), no more than about twice a week according to the AKC.", "akc_food"),
 ("Meat, fish and eggs", "Tuna", "caution", "Small amounts only; canned tuna contains some mercury and sodium. Choose tuna in water, unseasoned (AKC).", "akc_food"),
 ("Meat, fish and eggs", "Shrimp (cooked, shelled)", "yes", "A few now and then, fully cooked with the shell, tail, head and legs removed (AKC).", "akc_food"),
 ("Meat, fish and eggs", "Turkey (plain, cooked, no skin or bones)", "yes", "Safe without excess fat, skin, seasoning or bones; poultry bones splinter (AKC).", "akc_food"),
 ("Meat, fish and eggs", "Pork (plain, cooked)", "yes", "Plain, in small amounts, with fat trimmed and no seasoning (AKC).", "akc_food"),
 ("Meat, fish and eggs", "Ham", "caution", "High in salt and fat; a small piece is all right occasionally (AKC).", "akc_food"),
 ("Dairy", "Cheese", "caution", "Small to moderate amounts are fine for most dogs; choose lower fat cheeses such as mozzarella or cottage cheese (AKC).", "akc_food"),
 ("Dairy", "Plain yogurt", "yes", "OK if your dog digests dairy well. Avoid added sugar and never use artificially sweetened yogurt (AKC).", "akc_food"),
 ("Grains and baking", "Raw yeast bread dough", "no", "Can expand in the stomach, causing painful bloating or a twisted stomach, and the yeast produces alcohol (ASPCA). An emergency.", "aspca_foods"),
 ("Grains and baking", "Bread (plain)", "caution", "Small amounts of plain bread will not hurt, but it offers no nutrition; never raisin bread (AKC).", "akc_food"),
 ("Grains and baking", "Rice, wheat and other grains", "yes", "Dogs do not need to be grain free; grains are fine unless your vet advises otherwise for allergies (AKC).", "akc_food"),
 ("Grains and baking", "Quinoa", "yes", "Found in some dog foods and fine plain (AKC).", "akc_food"),
 ("Grains and baking", "Cinnamon", "caution", "Not toxic, but the AKC advises avoiding it: it can irritate the mouth and stomach, and inhaled powder can cause coughing.", "akc_food"),
]
LABEL = {"no": "Toxic or dangerous", "caution": "Caution: small amounts or avoid", "yes": "Safe: plain, in moderation"}
SHORT = {"no": "Toxic", "caution": "Caution", "yes": "Safe in moderation"}
IF_EATEN = {
 "no": "Call even if your dog seems fine; signs can be delayed. Have the amount, the time and your dog's weight ready. Do not make your dog vomit unless a vet tells you to.",
 "caution": "Many small amounts cause no problem or only mild stomach upset, but a vet or poison line can tell you whether your dog's amount needs treatment. Get help straight away for vomiting, diarrhea, weakness or pain.",
 "yes": "No action needed for a small, plain amount. Call your vet if it contained xylitol, onion, garlic or raisins, or your dog becomes unwell.",
}
IF_EATEN_OVERRIDE = {
 "Bones (cooked poultry bones, raw bones)": "Do not try to make your dog vomit. Watch for vomiting, straining, a painful belly or not eating, which need urgent care.",
 "Corn on the cob": "A swallowed cob can cause a blockage. Vomiting, not eating or a painful belly need urgent care.",
 "Xylitol (sugar free gum, sweets, some peanut butters, baked goods, toothpaste)": "Go to a vet immediately; blood sugar can drop within 30 to 60 minutes. Do not make your dog vomit at home.",
 "Raw yeast bread dough": "Go to a vet immediately: bloating and alcohol poisoning are both possible.",
}

def slug(s):
    import re
    return re.sub(r"[^a-z0-9]+", "-", s.lower().split("(")[0]).strip("-")

def can_dogs_eat(page):
    cats = []
    for c, *_ in FOODS:
        if c not in cats:
            cats.append(c)
    n = len(FOODS)
    rows = []
    for c in cats:
        rows.append('<tr class="cat" id="%s"><th colspan="3">%s</th></tr>' % (slug(c), c))
        for cat, food, v, why, keys in FOODS:
            if cat != c:
                continue
            refs = "; ".join('<a href="%s" rel="noopener">%s, %s</a>' % (S[k][2], S[k][1], S[k][0]) for k in keys.split())
            call = '<p class="call"><b>Call your vet or ASPCA Animal Poison Control now: <a href="tel:+18884264435">(888) 426-4435</a></b>. Outside the US, call your vet or emergency vet.</p>' if v != "yes" else ""
            rows.append('<tr id="%s" data-v="%s"><td><b>%s</b></td><td class="%s">%s</td><td>%s<p>%s</p><p><b>If eaten:</b> %s</p><p class="note">Last reviewed 8 Oct 2026 &middot; Sources: %s</p></td></tr>' % (slug(food), v, food, v, SHORT[v], call, why, IF_EATEN_OVERRIDE.get(food, IF_EATEN[v]), refs))
    counts = {k: sum(1 for f in FOODS if f[2] == k) for k in LABEL}
    body = """
<p class="note" style="font-style:normal"><b>Emergency?</b> If your dog has eaten something marked <span class="no">Toxic</span>, call your vet or emergency vet now, with the food, amount and your dog's weight to hand. In the US you can also call the ASPCA Animal Poison Control Center on (888) 426-4435.</p>
<div class="tool"><label for="q">Search %d foods</label><input id="q" class="search" type="search" placeholder="Type a food, e.g. grapes, cheese, peanut butter" autocomplete="off">
<div class="row" style="margin-top:.6rem" role="group" aria-label="Filter by verdict"><button class="btn" data-f="all">All</button> <button class="btn alt" data-f="no">Toxic (%d)</button> <button class="btn alt" data-f="caution">Caution (%d)</button> <button class="btn alt" data-f="yes">Safe (%d)</button></div><p id="count" class="note" aria-live="polite"></p></div>
<nav class="jump" aria-label="Jump to category"><b>Jump to:</b> %s</nav>
<div class="tablewrap"><table id="foods"><thead><tr><th>Food</th><th>Verdict</th><th>What to do, why, and sources</th></tr></thead><tbody>%s</tbody></table></div>
<section class="card"><h2>How to read this table</h2><ul>
<li><span class="no">Toxic</span>: poisonous or physically dangerous. Keep it out of reach; if eaten, call a vet.</li>
<li><span class="caution">Caution</span>: not usually poisonous, but risky in larger amounts, for some dogs, or when prepared the wrong way. Our sources advise small amounts or avoiding it.</li>
<li><span class="yes">Safe in moderation</span>: generally safe as an occasional treat when plain (no salt, sugar, butter, onion, garlic or seasoning) and cut into bite sized pieces.</li></ul>
<p>Treats of any kind should be a small part of the diet, and new foods should be introduced one at a time. Dogs with health conditions, such as pancreatitis, diabetes, kidney disease or food allergies, may need stricter rules; ask your vet. Every verdict above comes from the ASPCA, the American Kennel Club, the Merck Veterinary Manual or Cornell University College of Veterinary Medicine, linked on each row.</p></section>
""" % (n, counts["no"], counts["caution"], counts["yes"], " &middot; ".join('<a href="#%s">%s</a>' % (slug(c), c) for c in cats), "".join(rows))
    script = """(function(){var q=document.getElementById('q'),f='all',rows=[].slice.call(document.querySelectorAll('#foods tbody tr')),c=document.getElementById('count');
function run(){var t=q.value.trim().toLowerCase(),shown=0;rows.forEach(function(r){if(r.classList.contains('cat')){r.hidden=!!t||f!='all';return}var ok=(!t||r.textContent.toLowerCase().indexOf(t)>-1)&&(f=='all'||r.dataset.v==f);r.hidden=!ok;if(ok)shown++});c.textContent=shown+' food'+(shown==1?'':'s')+' shown'}
q.addEventListener('input',run);[].forEach.call(document.querySelectorAll('[data-f]'),function(b){b.addEventListener('click',function(){f=b.dataset.f;[].forEach.call(document.querySelectorAll('[data-f]'),function(x){x.className='btn'+(x==b?'':' alt')});run()})});
var h=location.hash.slice(1);if(h){var e=document.getElementById(h);if(e&&!e.classList.contains('cat'))e.style.outline='2px solid #f0a640'}run()})();"""
    faq = [
        ("Can dogs eat grapes or raisins?", "No. The ASPCA says grapes and raisins can cause kidney damage in dogs, and the AKC says no amount has been proven safe. Call your vet if your dog eats any, even a few."),
        ("Can dogs eat peanut butter?", "Yes, in small amounts, as long as the label shows it does not contain xylitol. Xylitol can cause a dangerous drop in blood sugar in dogs."),
        ("Can dogs eat cheese?", "Most dogs can have small amounts of cheese. The AKC suggests lower fat types such as mozzarella or cottage cheese, and some dogs do not digest dairy well."),
        ("Can dogs eat avocado?", "The AKC advises against it: the pit, skin and leaves contain persin, which can cause vomiting and diarrhea, the flesh is high in fat, and the pit can cause a blockage. The ASPCA notes avocado is most dangerous to birds, rabbits, horses and ruminants."),
        ("Can dogs eat bones?", "Bones are best avoided. The ASPCA warns that bones can injure or block the digestive tract, sometimes needing surgery, and the AKC notes cooked poultry bones splinter."),
        ("Can dogs eat bananas, apples and blueberries?", "Yes. The AKC lists all three as safe treats in moderation. Remove apple cores and seeds, and remember bananas are high in sugar."),
        ("Is a little garlic or onion OK for dogs?", "No. Onions, garlic, chives and leeks belong to the Allium family, which can damage a dog's red blood cells. The AKC says garlic is significantly more toxic to dogs than the other Alliums and that signs can be delayed for days."),
        ("What should I do if my dog ate something toxic?", "Call your vet, an emergency vet or a pet poison line straight away, even if your dog seems well. Note what was eaten, how much and when, and your dog's weight. Do not try to make your dog vomit unless a vet tells you to."),
    ]
    page("can-dogs-eat.html", "Can My Dog Eat This? %d Foods Rated Safe, Caution or Toxic | Dog Field Guide" % n,
         "Look up %d foods: which are toxic to dogs (grapes, chocolate, xylitol, onions), which need caution and which are safe, with sources and what to do if eaten." % n,
         body, h1="Can my dog eat this? %d foods rated Safe, Caution or Toxic" % n,
         lead="The foods most dangerous to dogs are chocolate and cocoa, grapes and raisins, onions, garlic and other Alliums, xylitol (in sugar free products), macadamia nuts, alcohol, raw yeast dough and caffeine. Many plain fruits and vegetables, such as apples, blueberries, carrots and green beans, are fine as occasional treats. Search the table below for a verdict and the veterinary or kennel club source behind it.",
         faq=faq, sources=src("aspca_foods", "akc_food", "akc_fruit", "merck_choc", "merck_xyl", "merck_foodpet", "cornell_xyl"),
         related=[("blog/dog-ate-chocolate.html", "Dog ate chocolate? Dose estimator"), ("health.html#poisoning", "Poisoning: first steps"), ("care.html#feeding", "Feeding your dog"), ("blog/is-my-dog-overweight.html", "Is my dog overweight?"), ("faq.html", "Dog FAQ")],
         crumbs=[("index.html", "Home"), ("can-dogs-eat.html", "Can dogs eat this?")], script=script)

# ------------------------------------------------------------------ AGE CALCULATOR
def human_age(d):
    return 16 * math.log(d) + 31

def age_calc(page):
    rows = "".join("<tr><td>%d</td><td>%d</td><td>%d</td></tr>" % (y, round(human_age(y)), 7 * y) for y in range(1, 17))
    body = """
<div class="tool"><h2 style="margin-top:0">Calculate your dog's age</h2>
<div class="row"><div><label for="y">Years</label><input id="y" type="number" min="0" max="25" step="1" value="5" inputmode="numeric" style="width:6rem"></div>
<div><label for="m">Months</label><input id="m" type="number" min="0" max="11" step="1" value="0" inputmode="numeric" style="width:6rem"></div>
<button class="btn" id="go" type="button">Calculate</button></div>
<p class="result" id="out" aria-live="polite"></p>
<p class="note">Formula: human age = 16 &times; ln(dog age in years) + 31 (Wang et al., 2020). Works for dogs aged 3 months and over.</p></div>
<h2 id="table">Dog years to human years table</h2>
<div class="tablewrap"><table><thead><tr><th>Dog age (years)</th><th>Epigenetic clock estimate (human years)</th><th>Old "times 7" rule</th></tr></thead><tbody>%s</tbody></table></div>
<section id="method"><h2>Where the formula comes from</h2>
<p>In 2020, a research team (Wang and colleagues) published a study in the journal <i>Cell Systems</i> comparing DNA methylation, chemical marks on DNA that change in a predictable way as mammals age, in 104 Labrador retrievers spanning a 16 year age range with methylation data from humans. Matching each dog to the humans with the most similar methylation patterns produced a curved, logarithmic relationship rather than a straight line. Combining two matching analyses gave a single function: <b>human age = 16 ln(dog age) + 31</b>.</p>
<p>The authors checked it against life stages. It translated an 8 week old puppy to roughly a 9 month old baby, the stage when baby teeth come through in both species, and the typical Labrador lifespan of 12 years to about 70 human years, close to worldwide human life expectancy. The match was closest for the infant, juvenile and senior stages and more approximate in between, where the dog epigenome changed faster than physiology tables suggested.</p></section>
<section id="limits" class="card"><h2>Limits worth knowing</h2><ul>
<li><b>One breed.</b> The study used only Labrador retrievers. Small breeds tend to live longer than giant breeds (the Merck Veterinary Manual gives an average lifespan range of 8 to 16 years depending on breed), so the same formula will fit some dogs better than others.</li>
<li><b>Fast early years.</b> Because of the logarithm, the first year of a dog's life maps to about 31 human years, and later years add much less.</li>
<li><b>It is an analogy.</b> A "human years" number is a way to picture life stage, not a medical measure. Your vet's view of your dog's health matters more for care decisions.</li></ul></section>
""" % rows
    script = """(function(){var y=document.getElementById('y'),m=document.getElementById('m'),o=document.getElementById('out');
function calc(){var a=(+y.value||0)+(+m.value||0)/12;if(a<0.25){o.innerHTML='Enter an age of at least 3 months.';return}
var h=16*Math.log(a)+31;o.innerHTML='A dog aged <b>'+a.toFixed(a%1?2:0).replace(/\\.?0+$/,'')+' years</b> is roughly <b>'+Math.round(h)+' in human years</b> by the epigenetic clock (the old times 7 rule would say '+Math.round(a*7)+').'}
document.getElementById('go').addEventListener('click',calc);y.addEventListener('input',calc);m.addEventListener('input',calc);calc()})();"""
    faq = [
        ("Is one dog year really seven human years?", "No. The times seven rule is not based on research. The 2020 epigenetic study of Labrador retrievers found dogs age very fast early on: a 1 year old dog compares to a human of about 31, while later years add far less."),
        ("How old is a 10 year old dog in human years?", "About 68, using the epigenetic clock formula human age = 16 ln(10) + 31. The old times seven rule would say 70."),
        ("Does the formula work for small and giant breeds?", "It was built from Labrador retrievers only, so it is most reliable for medium to large dogs with a similar lifespan. Smaller breeds usually live longer and giant breeds shorter, so treat the result as a rough guide."),
    ]
    page("dog-age-calculator.html", "Dog Age Calculator: Dog Years to Human Years (Science Based) | Dog Field Guide",
         "Convert dog years to human years with the epigenetic clock formula from the 2020 Cell Systems study (16 ln(age) + 31), plus a full table and the limits of the method.",
         body, h1="Dog age calculator: dog years to human years",
         lead="The best evidence based conversion comes from a 2020 study of DNA methylation in 104 Labrador retrievers, which found that human age is roughly 16 &times; ln(dog age) + 31. By that formula a 1 year old dog is about 31 in human years, a 4 year old about 53, a 10 year old about 68 and a 14 year old about 73. Dogs age very quickly early in life and more slowly later, so the old times 7 rule is wrong at both ends.",
         faq=faq, sources=src("wang2020", "merck_vitals"),
         related=[("health.html", "Dog health basics"), ("care.html", "Everyday care"), ("blog/is-my-dog-overweight.html", "Keeping your dog lean"), ("can-dogs-eat.html", "Can dogs eat this?"), ("faq.html", "Dog FAQ")],
         crumbs=[("index.html", "Home"), ("dog-age-calculator.html", "Dog age calculator")], script=script)

# ------------------------------------------------------------------ FAQ
def faq(page):
    qs = [
        ("What is a normal temperature for a dog?", "The Merck Veterinary Manual gives an average body temperature of 101 to 102.5&deg;F (38.3 to 39.2&deg;C) for dogs. See <a href=\"{R}health.html#vitals\">normal vital signs</a>."),
        ("How fast should a dog breathe at rest?", "About 18 to 34 breaths per minute at rest, according to the Merck Veterinary Manual. Count chest movements for 30 seconds while your dog is relaxed and double it."),
        ("Which foods are toxic to dogs?", "The ASPCA's list includes chocolate, coffee and caffeine, grapes and raisins, onions, garlic and chives, macadamia nuts, xylitol, alcohol and raw yeast dough. Check any food in our <a href=\"{R}can-dogs-eat.html\">Can dogs eat this?</a> table."),
        ("How much chocolate is dangerous for a dog?", "It depends on the type of chocolate and the dog's weight. The Merck Veterinary Manual says mild signs can appear at about 20 mg of methylxanthines per kg of body weight, heart effects at 40 to 50 mg/kg and seizures at 60 mg/kg or more. Use our <a href=\"{R}blog/dog-ate-chocolate.html\">chocolate estimator</a> and call your vet."),
        ("How often do dogs need vaccines?", "Under the AAHA guidelines, after the puppy series and a booster within a year, the distemper, adenovirus and parvovirus combination is boosted every 3 years, leptospirosis yearly, and rabies as local law requires. <a href=\"{R}blog/dog-vaccine-schedule.html\">Full explanation</a>."),
        ("When should I start socializing my puppy?", "Straight away. The AVSAB calls the first three months the primary socialization window and says puppy classes can start at 7 to 8 weeks once the puppy has had a first set of vaccines at least 7 days earlier and a first deworming. <a href=\"{R}blog/puppy-socialization-window.html\">How to do it safely</a>."),
        ("Is dominance or alpha training a good idea?", "No. Veterinary behaviorists at the AVSAB advise against dominance based and aversive methods, and wolf research shows wild packs are families rather than groups fighting for alpha status. <a href=\"{R}blog/alpha-dog-myth.html\">What the research says</a>."),
        ("How do I know if my dog is overweight?", "Use a body condition score: at an ideal weight you can feel the ribs without excess fat and see a waist from above. <a href=\"{R}blog/is-my-dog-overweight.html\">Step by step guide</a>."),
        ("How old is my dog in human years?", "By the 2020 epigenetic clock formula, human age is about 16 &times; ln(dog age) + 31, so a 1 year old dog is about 31 and a 10 year old about 68. Try the <a href=\"{R}dog-age-calculator.html\">dog age calculator</a>."),
        ("How often should I brush my dog's teeth?", "The AVMA says daily brushing is best, but several times a week can be effective, alongside a dental check by your vet at least once a year."),
        ("Does my dog legally need a microchip?", "In the UK, yes: all dogs must be microchipped and registered by 8 weeks old, and must wear a collar and tag with the owner's name and address in public. Other countries have their own rules."),
        ("What should I do if my dog has heatstroke?", "Cool first, transport second, says the RSPCA: stop activity, move to shade, pour water cooler than the dog over its body (not the head), fan it, then go to a vet in a cool car. Do not cover the dog with wet towels."),
    ]
    page("faq.html", "Dog FAQ: Quick, Sourced Answers to Common Dog Questions | Dog Field Guide",
         "Short, sourced answers to common dog questions: normal temperature, toxic foods, chocolate, vaccine schedules, socialization, alpha training, weight, teeth and heatstroke.",
         '<p>Each answer links to a fuller page with the sources.</p>', h1="Dog FAQ",
         lead="Quick answers to the questions dog owners ask most, drawn from veterinary and welfare sources such as the Merck Veterinary Manual, AAHA, AVSAB, AVMA, the ASPCA and the RSPCA.",
         faq=qs, sources=src("merck_vitals", "aspca_foods", "merck_choc", "aaha_table", "avsab_puppy", "avsab_train", "wsava_bcs", "wang2020", "avma_dental", "gov_chip", "rspca_heat"),
         related=[("health.html", "Health basics"), ("care.html", "Everyday care"), ("training.html", "Training"), ("behavior.html", "Behavior"), ("glossary.html", "Glossary")],
         crumbs=[("index.html", "Home"), ("faq.html", "FAQ")])

# ------------------------------------------------------------------ GLOSSARY
def glossary(page):
    terms = [
        ("Allium", "The plant family that includes onions, garlic, chives and leeks, all of which can damage dogs' red blood cells. See <a href=\"{R}can-dogs-eat.html#onions\">onions</a>."),
        ("Aversive training", "Training that relies on force, pain, or physical or emotional discomfort, such as lead jerks or shock collars. Not recommended by the AVSAB."),
        ("Body condition score (BCS)", "A hands on rating of body fat, commonly on a 9 point scale where 4 to 5 is ideal. See <a href=\"{R}blog/is-my-dog-overweight.html\">how to score your dog</a>."),
        ("Brachycephalic", "Flat faced or short nosed. Brachycephalic dogs cannot pant as effectively and are at higher risk of heatstroke (RSPCA)."),
        ("Breed standard", "A kennel club's detailed description of how a breed should look, move and behave."),
        ("Capturing", "Marking and rewarding a behavior the dog offers on its own."),
        ("Core vaccine", "A vaccine recommended for all dogs unless there is a medical reason not to. In the AAHA guidelines: distemper, adenovirus type 2, parvovirus, leptospirosis and rabies."),
        ("Flooding", "Keeping an animal in a frightening situation until it stops reacting. Advised against by the AVSAB."),
        ("Gundog", "Royal Kennel Club group of dogs bred to find and/or retrieve game; broadly equivalent to the AKC Sporting group."),
        ("Leptospirosis", "A bacterial disease that can affect dogs and people; added to the AAHA core vaccine list in 2024."),
        ("Luring", "Guiding a dog into a position with a treat, then fading the treat into a hand signal."),
        ("Marker", "A click or word that tells the dog the exact moment it earned a reward."),
        ("Methylxanthines", "Stimulant compounds, including theobromine and caffeine, that make chocolate, coffee and caffeine toxic to dogs."),
        ("Non core vaccine", "A vaccine recommended for some dogs depending on lifestyle, location and risk, such as Bordetella, Lyme disease or canine influenza."),
        ("Parvovirus", "A serious viral disease of dogs; one of the core vaccines."),
        ("Pastoral", "Royal Kennel Club group of herding dogs; broadly equivalent to the AKC Herding group."),
        ("Periodontal disease", "Disease of the gums and tissues holding the teeth; the most common dental condition in dogs (AVMA)."),
        ("Reward based training", "Teaching by reinforcing the behavior you want with things the dog values. Recommended by the AVSAB for all dogs."),
        ("Shaping", "Rewarding small steps that build toward a final behavior."),
        ("Socialization", "Positive, safe exposure to people, animals, places and experiences, most important in a puppy's first three months."),
        ("Theobromine", "The main toxic methylxanthine in chocolate. Merck gives its half life in dogs as 17.5 hours."),
        ("Xylitol", "A sugar alcohol sweetener that triggers a dangerous insulin release and low blood sugar in dogs."),
    ]
    body = '<dl class="card">' + "".join('<dt id="%s">%s</dt><dd>%s</dd>' % (slug(t), t, d) for t, d in terms) + "</dl>"
    page("glossary.html", "Dog Glossary: Plain English Dog & Vet Terms | Dog Field Guide",
         "Plain English definitions of dog care, health, training and breed terms: core vaccine, body condition score, brachycephalic, methylxanthines, shaping, xylitol and more.",
         body, h1="Dog glossary",
         lead="Short, plain English definitions of terms you will meet on vet visits, in training classes and on kennel club sites, each linked to the page that explains it in more depth.",
         sources=src("aaha_table", "avsab_train", "rspca_heat", "avma_dental", "merck_choc", "wsava_bcs", "rkc_groups"),
         related=[("faq.html", "Dog FAQ"), ("breeds.html", "Breed groups"), ("health.html", "Health basics"), ("training.html", "Training")],
         crumbs=[("index.html", "Home"), ("glossary.html", "Glossary")])

# ------------------------------------------------------------------ TRUST PAGES
def trust(page):
    page("about.html", "About Dog Field Guide: Who We Are & How We Write | Dog Field Guide",
         "Who runs Dog Field Guide, what it covers, how the content is researched and sourced, and how to report a correction.",
         """
<h2>Who runs this site</h2>
<p>Dog Field Guide is operated by Joshua Israel Ventures LLC. It is an independent publication and is not affiliated with any kennel club, veterinary organization, pet food company or retailer named on the site.</p>
<h2>What we cover</h2>
<p>Practical, plain English information for dog owners: <a href="{R}breeds.html">breed groups</a>, <a href="{R}care.html">everyday care</a>, <a href="{R}health.html">health basics</a>, <a href="{R}training.html">training</a> and <a href="{R}behavior.html">behavior</a>, plus tools such as the <a href="{R}can-dogs-eat.html">Can dogs eat this?</a> table and the <a href="{R}dog-age-calculator.html">dog age calculator</a>.</p>
<h2>How content is produced</h2>
<ul><li>Pages are researched and written by the Dog Field Guide editorial team with the help of AI tools, then checked against primary and authoritative sources such as the Merck Veterinary Manual, the American Animal Hospital Association, the American Veterinary Society of Animal Behavior, the American Veterinary Medical Association, the ASPCA, the RSPCA, the American Kennel Club, The Royal Kennel Club, university veterinary schools and peer reviewed studies.</li>
<li>Every page lists its sources, and facts and figures are attributed to the organization that published them. We do not invent statistics, quotes, experts or personal experiences.</li>
<li>We are not veterinarians, and nothing here replaces an examination by a vet who knows your dog. Health and safety pages say so and point to emergency help.</li>
<li>Each page shows when it was last updated. We review pages when guidelines change.</li></ul>
<h2>Money</h2>
<p>The site is free to read. It currently carries no advertising, sponsored content or affiliate links. If that changes, we will say so clearly on the affected pages and in our <a href="{R}privacy.html">privacy policy</a>.</p>
<h2>Corrections</h2>
<p>Spotted an error or an outdated guideline? Please email <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a> or use the <a href="{R}contact.html">contact form</a> with the page and the source, and we will check and correct it.</p>
""", h1="About Dog Field Guide", kind="webpage",
         lead="Dog Field Guide is a free, independent reference for dog owners, operated by Joshua Israel Ventures LLC. We turn veterinary and kennel club guidance into clear, practical pages and show the sources behind every claim.",
         crumbs=[("index.html", "Home"), ("about.html", "About")])

    page("contact.html", "Contact Dog Field Guide | Dog Field Guide",
         "Contact Dog Field Guide by email or form with questions, corrections or suggestions. Operated by Joshua Israel Ventures LLC.",
         """
<p>Email us at <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>, or send a message with the form below. We read every message, although we cannot always reply individually.</p>
<p class="note" style="font-style:normal"><b>We cannot give veterinary advice for individual dogs.</b> If your dog is unwell, injured or may have eaten something toxic, contact your vet or an emergency vet now.</p>
<form class="card" action="https://formsubmit.co/joshuaofisrael@gmail.com" method="POST">
<input type="hidden" name="_subject" value="[Contact: Dog Field Guide]">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_next" value="SITE_URL_PLACEHOLDERcontact-thanks.html">
<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<label for="name">Name</label><input id="name" name="name" type="text" required autocomplete="name">
<label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email">
<label for="topic">Topic</label><select id="topic" name="topic"><option>Question</option><option>Correction</option><option>Suggestion</option><option>Other</option></select>
<label for="message">Message</label><textarea id="message" name="message" rows="6" required></textarea>
<p class="note">Messages are delivered by FormSubmit to our inbox. See our <a href="{R}privacy.html">privacy policy</a>.</p>
<button class="btn" type="submit">Send message</button>
</form>
""", h1="Contact us", kind="webpage",
         lead="Questions, corrections and suggestions are welcome. The quickest way to reach Dog Field Guide is email: joshuaofisrael@gmail.com.",
         crumbs=[("index.html", "Home"), ("contact.html", "Contact")])

    page("contact-thanks.html", "Message sent | Dog Field Guide", "Thank you for contacting Dog Field Guide.",
         '<p>Thank you, your message has been sent. If it needs a reply, we will answer by email.</p><p><a class="btn" href="{R}index.html">Back to the home page</a></p>',
         h1="Thanks for your message", kind="webpage", index=False, nav="contact.html")

    page("privacy.html", "Privacy Policy | Dog Field Guide",
         "How Dog Field Guide handles data: no accounts, no advertising cookies, contact form messages processed by FormSubmit, and how to reach us.",
         """
<p class="meta">Last updated 8 October 2026</p>
<h2>Who we are</h2><p>Dog Field Guide is operated by Joshua Israel Ventures LLC. Contact: <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>.</p>
<h2>What we collect</h2>
<ul><li><b>Browsing.</b> The site has no user accounts and sets no advertising or tracking cookies. It is hosted on GitHub Pages, and GitHub may log technical information such as IP addresses for security and operation; see GitHub's privacy statement.</li>
<li><b>Analytics.</b> We may use Cloudflare Web Analytics, a privacy focused, cookieless service, to count page views in aggregate. It does not use cookies or build profiles of individual visitors. If and when it is enabled, it loads a small script from static.cloudflareinsights.com.</li>
<li><b>Contact form.</b> If you use the contact form, your name, email address and message are sent through FormSubmit (formsubmit.co) to our email inbox. We use them only to read and reply to your message. Email us at any time to ask us to delete your message.</li>
<li><b>Email.</b> If you email us directly, we keep your message and address only as long as needed to deal with it.</li></ul>
<h2>Advertising and affiliates</h2><p>The site currently shows no ads and contains no affiliate links. We will update this policy before that changes.</p>
<h2>Third party links</h2><p>Pages link to outside sources such as veterinary manuals and kennel clubs. Their own privacy policies apply when you visit them.</p>
<h2>Children</h2><p>The site is general information for a general audience and does not knowingly collect personal information from children.</p>
<h2>Your rights</h2><p>Depending on where you live, you may have rights to access, correct or delete personal data we hold about you. Email us and we will respond.</p>
<h2>Changes</h2><p>We will post any changes on this page with a new date.</p>
""", h1="Privacy policy", kind="webpage",
         crumbs=[("index.html", "Home"), ("privacy.html", "Privacy")])

    page("404.html", "Page Not Found | Dog Field Guide", "That page could not be found.",
         '<p>We could not find that page. Try the <a href="{R}index.html">home page</a>, the <a href="{R}can-dogs-eat.html">Can dogs eat this?</a> table or the <a href="{R}faq.html">dog FAQ</a>.</p>',
         h1="This page wandered off", kind="webpage", index=False, abs_links=True, nav="")

# ------------------------------------------------------------------ BLOG
POSTS = []

def post(page, slug_, title, desc, h1, lead, body, faq=None, sources=None, related=None, script=""):
    POSTS.append((slug_, h1, desc))
    page("blog/%s.html" % slug_, title, desc, body, h1=h1, lead=lead, kind="post", faq=faq, sources=sources,
         related=related, script=script, crumbs=[("index.html", "Home"), ("blog/index.html", "Blog"), ("blog/%s.html" % slug_, h1)])

CHOC_JS = """(function(){var C={cocoa:28.5,baking:15.5,dark:5.6,milk:2.3,white:0.04};
var w=document.getElementById('cw'),wu=document.getElementById('cwu'),t=document.getElementById('ct'),pc=document.getElementById('cpct'),a=document.getElementById('ca'),au=document.getElementById('cau'),o=document.getElementById('cout'),pr=document.getElementById('pctrow');
function run(){pr.hidden=t.value!='pct';var kg=(+w.value||0)*(wu.value=='lb'?0.4536:1),g=(+a.value||0)*(au.value=='oz'?28.35:1);
if(!kg||!g){o.innerHTML='Enter your dog\\'s weight and the amount eaten.';return}
var c=t.value=='pct'?15.5*Math.min(100,Math.max(0,+pc.value||0))/100:C[t.value],d=g*c/kg,msg;
if(d<20)msg='This is below the roughly 20 mg/kg level at which Merck says mild signs can appear, but individual dogs vary and the label may be inaccurate. <b>Call your vet for advice.</b>';
else if(d<40)msg='<b>Mild signs possible</b> (vomiting, diarrhea, increased thirst) at around 20 mg/kg and above. <b>Call your vet now.</b>';
else if(d<60)msg='<b>Heart effects possible</b>: Merck lists cardiotoxic effects at 40 to 50 mg/kg. <b>Call your vet or emergency vet now.</b>';
else msg='<b>Seizure range</b>: Merck says seizures can occur at 60 mg/kg or more. <b>This is an emergency: go to a vet now.</b>';
o.innerHTML='Estimated dose: <b>'+Math.round(d)+' mg of methylxanthines per kg</b> of body weight. '+msg}
[w,wu,t,pc,a,au].forEach(function(e){e.addEventListener('input',run);e.addEventListener('change',run)});run()})();"""

def blog(page):
    # 1 chocolate
    post(page, "dog-ate-chocolate", "My Dog Ate Chocolate: How Much Is Dangerous? (Dose Estimator) | Dog Field Guide",
         "Dog ate chocolate? Estimate the theobromine dose by chocolate type and your dog's weight using Merck Veterinary Manual figures, learn the warning signs and what to do now.",
         "My dog ate chocolate: how much is dangerous?",
         "Chocolate is dangerous because it contains theobromine and caffeine, and the risk depends on the type of chocolate and your dog's weight. The Merck Veterinary Manual says mild signs can appear at about 20 mg of these compounds per kg of body weight, heart problems at 40 to 50 mg/kg and seizures at 60 mg/kg or more; cocoa powder and baking chocolate are by far the most concentrated. If your dog has eaten chocolate, call your vet now and use the estimator below to give them the numbers.",
         """
<div class="tool"><h2 style="margin-top:0">Chocolate dose estimator</h2>
<div class="row"><div><label for="cw">Dog's weight</label><input id="cw" type="number" min="0" step="0.1" value="10" style="width:7rem"> <select id="cwu" aria-label="Weight unit"><option value="kg">kg</option><option value="lb">lb</option></select></div>
<div><label for="ct">Type of chocolate</label><select id="ct"><option value="milk">Milk chocolate</option><option value="dark">Dark or semisweet chocolate</option><option value="baking">Unsweetened baking chocolate</option><option value="cocoa">Cocoa powder</option><option value="pct">Bar with cocoa % on label</option><option value="white">White chocolate</option></select></div>
<div id="pctrow" hidden><label for="cpct">Cocoa %</label><input id="cpct" type="number" min="0" max="100" value="70" style="width:6rem"></div>
<div><label for="ca">Amount eaten</label><input id="ca" type="number" min="0" step="1" value="50" style="width:7rem"> <select id="cau" aria-label="Amount unit"><option value="g">grams</option><option value="oz">ounces</option></select></div></div>
<p class="result" id="cout" aria-live="polite"></p>
<p class="note">An estimate only, using average methylxanthine levels from the Merck Veterinary Manual. Real products vary, and some dogs react at lower doses. It does not replace a vet. In the US, the ASPCA Animal Poison Control Center is on (888) 426-4435.</p></div>
<h2>What to do right now</h2>
<ol><li><b>Work out what and how much.</b> Find the wrapper. Note the type of chocolate (or the cocoa percentage), roughly how much is missing, and when it was eaten.</li>
<li><b>Weigh your dog</b> or use its last weight from the vet.</li>
<li><b>Call your vet, an emergency vet or a pet poison line</b> and give them those numbers. Do this even if your dog seems completely normal: Merck says signs usually appear 6 to 12 hours after eating.</li>
<li><b>Do not try home remedies</b> unless a vet tells you to. Merck notes vets may induce vomiting if the chocolate was eaten recently (for example within 2 hours) and the dog is still well, but this should be done under veterinary guidance.</li></ol>
<h2>Why chocolate is toxic to dogs</h2>
<p>Chocolate is made from roasted cacao seeds, which contain two stimulants called methylxanthines: theobromine and caffeine. Theobromine is present at 3 to 10 times the concentration of caffeine, and both contribute to poisoning. They stimulate the nervous system and the heart. Dogs also clear theobromine slowly; Merck gives its half life in dogs as 17.5 hours, compared with 4.5 hours for caffeine, which helps explain why signs can last a long time.</p>
<h2>Which chocolate is most dangerous?</h2>
<div class="tablewrap"><table><thead><tr><th>Type</th><th>Methylxanthines (Merck)</th><th>Relative risk</th></tr></thead><tbody>
<tr><td>Cocoa powder</td><td>28.5 mg/g (807 mg/oz)</td><td class="no">Highest</td></tr>
<tr><td>Unsweetened baking chocolate</td><td>15.5 mg/g (440 mg/oz)</td><td class="no">Very high</td></tr>
<tr><td>Cocoa bean hull garden mulch</td><td>about 9 mg/g (255 mg/oz), though some mulches have it removed</td><td class="no">High</td></tr>
<tr><td>Semisweet and sweet dark chocolate</td><td>5.3 to 5.6 mg/g (150 to 160 mg/oz)</td><td class="no">High</td></tr>
<tr><td>Milk chocolate</td><td>2.3 mg/g (64 mg/oz)</td><td class="caution">Moderate</td></tr>
<tr><td>White chocolate</td><td>0.04 mg/g (1.1 mg/oz)</td><td class="caution">Negligible stimulant, but fatty</td></tr>
</tbody></table></div>
<p>For bars labeled with a cocoa percentage, Merck's method is to multiply the percentage by the figure for unsweetened chocolate: a 70 percent bar has about 0.70 &times; 15.5 = roughly 10.9 mg per gram. The estimator above does the same.</p>
<h2>A worked example</h2>
<p>A 10 kg (22 lb) dog eats 50 g (about 1.8 oz) of milk chocolate. That is 50 &times; 2.3 = 115 mg of methylxanthines, or 11.5 mg per kg: below the level at which Merck says mild signs typically start, but still worth a call to the vet. If the same dog ate 50 g of 70 percent dark chocolate, the dose would be about 50 &times; 10.9 &divide; 10 = roughly 54 mg/kg, in the range where Merck says heart effects occur. That is an emergency. Merck also gives a rule of thumb that about 1 oz of milk chocolate per pound of body weight (62 g/kg) is potentially lethal.</p>
<h2>Signs of chocolate poisoning</h2>
<p>According to Merck, early signs include increased thirst, vomiting, diarrhea, a swollen belly and restlessness. These can progress to hyperactivity, increased urination, wobbliness, rigid muscles, tremors and seizures, along with a fast heart rate, abnormal heart rhythms, rapid breathing, high body temperature and, in severe cases, collapse or coma. In severe cases signs can last up to 72 hours. The high fat content of chocolate can also trigger pancreatitis in susceptible dogs.</p>
<h2>How vets treat it</h2>
<p>There is no simple test or antidote; diagnosis is based on what was eaten and the signs. Treatment may include making the dog vomit if it is caught early, medicines to control vomiting, tremors and heart rhythm, intravenous fluids, and monitoring of heart rhythm and temperature. The sooner a vet is involved, the more options there are.</p>
<h2>Preventing it</h2>
<ul><li>Keep chocolate, cocoa and baking supplies in closed cupboards, not on low tables or in bags on the floor.</li>
<li>Be extra careful at holidays, when gifts, advent calendars and chocolate eggs are around; remind visitors and children not to share.</li>
<li>Avoid cocoa bean hull mulch in gardens your dog uses.</li>
<li>Check other foods for chocolate, coffee and xylitol in our <a href="{R}can-dogs-eat.html">Can dogs eat this?</a> table.</li></ul>
""",
         faq=[("Can a small piece of chocolate kill a dog?", "A small piece of milk chocolate is unlikely to be fatal for a medium or large dog, but the risk rises sharply with darker chocolate, cocoa powder and smaller dogs. Merck says mild signs can start at about 20 mg/kg, so always calculate the dose and call your vet."),
              ("How long after eating chocolate will a dog get sick?", "The Merck Veterinary Manual says signs usually appear 6 to 12 hours after ingestion, and in severe cases can last up to 72 hours."),
              ("Is white chocolate safe for dogs?", "White chocolate contains only negligible amounts of theobromine, so it is very unlikely to cause stimulant poisoning, but its fat and sugar can still upset the stomach and may trigger pancreatitis in susceptible dogs.")],
         sources=src("merck_choc", "aspca_foods"),
         related=[("can-dogs-eat.html", "Can dogs eat this? food table"), ("health.html#poisoning", "Poisoning: first steps"), ("health.html#emergency", "When to call a vet now"), ("care.html#home", "Household hazards")],
         script=CHOC_JS)

    # 2 socialization
    post(page, "puppy-socialization-window", "Puppy Socialization Window: When It Closes & What to Do | Dog Field Guide",
         "Why the first three months matter most for puppy socialization, when puppy classes can start before vaccinations finish, and a safe week by week socialization checklist.",
         "The puppy socialization window: when it closes and what to do",
         "The American Veterinary Society of Animal Behavior (AVSAB) says the first three months of a puppy's life are the primary and most important window for socialization, because sociability outweighs fear during this period. It recommends starting puppy classes as early as 7 to 8 weeks, as long as the puppy has had at least one set of vaccines at least 7 days before the first class and a first deworming, rather than waiting until vaccinations are complete.",
         """
<h2>Why the window matters</h2>
<p>Puppies are born ready to learn what is normal in their world. During roughly the first three months, new people, animals, sounds and places are more likely to be met with curiosity than fear. The AVSAB position statement warns that incomplete or improper socialization during this time increases the risk of fear, avoidance and aggression later in life.</p>
<p>The stakes are high. The same statement says behavior problems are the greatest threat to the bond between owners and dogs, the number one cause of dogs being given up to shelters, and, in AVSAB's words, the number one cause of death for dogs under three years old, ahead of infectious disease.</p>
<h2>But what about vaccines?</h2>
<p>This is the dilemma every new owner faces: puppies are not fully vaccinated until about 16 weeks, but the best socialization window closes around 12 weeks. AVSAB's position is clear: it should be the standard of care for puppies to be socialized <i>before</i> they are fully vaccinated. It explains that maternal immunity, the first vaccines and sensible care make the risk of infection relatively small compared with the risk of death from a behavior problem.</p>
<p>The practical compromise AVSAB recommends:</p>
<ul><li>Puppy classes from 7 to 8 weeks, with at least one set of vaccines at least 7 days before the first class and a first deworming, then staying up to date.</li>
<li>Classes held on surfaces that are easy to clean and disinfect, such as indoors, with every puppy vaccinated and free of disease and parasites.</li>
<li>Avoiding dog parks and other areas heavily used by dogs whose vaccination or health status is unknown.</li></ul>
<p>Ask your vet about local disease risks; they can help you plan which places are sensible before the vaccine course is finished. See our <a href="{R}blog/dog-vaccine-schedule.html">vaccine schedule explainer</a>.</p>
<h2>What good socialization looks like</h2>
<p>Socialization is not about meeting as many dogs as possible. It means positive, safe experiences, at a pace the puppy is comfortable with. AVSAB stresses exposure "without causing over stimulation", which shows up as excessive fear, withdrawal or avoidance. Quality beats quantity: one calm, happy meeting is worth more than ten overwhelming ones.</p>
<h3>A socialization checklist</h3>
<div class="tablewrap"><table><thead><tr><th>Category</th><th>Ideas</th></tr></thead><tbody>
<tr><td>Handling</td><td>Gently touching paws, ears, mouth and tail with treats; being lifted; brushing; a pretend vet check. AVSAB says puppies should learn to accept handling of all body parts.</td></tr>
<tr><td>People</td><td>Calm adults and children of different ages and appearances; people in hats, coats, uniforms and sunglasses; people with walking sticks or wheelchairs.</td></tr>
<tr><td>Animals</td><td>Healthy, vaccinated, friendly adult dogs; cats or other pets in the household, introduced slowly.</td></tr>
<tr><td>Surfaces and objects</td><td>Grass, gravel, tiles, metal grates, steps, a wobble board; tunnels and boxes to explore, as AVSAB suggests.</td></tr>
<tr><td>Sounds</td><td>Household appliances, doorbells, traffic, thunder or fireworks recordings played quietly while the puppy eats or plays.</td></tr>
<tr><td>Places and travel</td><td>Short car trips (AVSAB encourages as many as possible), being carried past busy streets, cafes or shops, the vet's waiting room for a treat and a cuddle.</td></tr>
<tr><td>Alone time</td><td>Short periods resting in a crate or pen with a stuffed food toy. AVSAB says this teaches puppies to amuse themselves and may help prevent over attachment.</td></tr>
</tbody></table></div>
<h2>How to do it well</h2>
<ol><li><b>Let the puppy choose.</b> Allow it to approach new things in its own time, and reward curiosity.</li>
<li><b>Pair new things with good things.</b> Treats, play and praise make new experiences pleasant.</li>
<li><b>Watch for stress signals</b> such as lip licking, yawning, a tucked tail, a lowered body or freezing (see <a href="{R}behavior.html#stress">reading stress</a>), and back off if you see them.</li>
<li><b>Keep sessions short</b> and end on a good note.</li>
<li><b>Use reward based training.</b> AVSAB says positive, consistent training is associated with fewer behavior problems and better obedience than methods involving punishment or human dominance. Start with the <a href="{R}training.html#first">first skills</a>.</li></ol>
<h2>After 12 weeks</h2>
<p>The window does not slam shut. AVSAB strongly encourages owners to keep socializing beyond three months and to continue offering a wide variety of experiences throughout the first year, which it links to a lower risk of separation related behavior. If your puppy is showing fear, AVSAB advises seeking veterinary guidance early rather than waiting for it to grow out of it.</p>
""",
         faq=[("When does the puppy socialization window close?", "The AVSAB describes the first three months of life as the primary socialization window. Socialization should continue after that, but the early weeks are the most important."),
              ("Can I take my puppy to classes before it is fully vaccinated?", "AVSAB says puppies can start classes as early as 7 to 8 weeks if they have had at least one set of vaccines at least 7 days before the first class and a first deworming, with classes held on easily disinfected surfaces. Avoid dog parks and areas used by dogs of unknown vaccination status until your vet says otherwise."),
              ("What if my puppy is scared of new things?", "Go slower, increase distance and pair new experiences with treats and play. If fear persists or worsens, AVSAB recommends seeking veterinary guidance.")],
         sources=src("avsab_puppy", "avsab_train"),
         related=[("behavior.html#socialization", "Behavior: socialization"), ("training.html", "Reward based training"), ("blog/dog-vaccine-schedule.html", "Dog vaccine schedule"), ("blog/alpha-dog-myth.html", "The alpha dog myth")])

    # 3 vaccines
    post(page, "dog-vaccine-schedule", "How Often Do Dogs Need Vaccines? Core vs Non Core Explained | Dog Field Guide",
         "Do dogs need yearly vaccines? What the AAHA guidelines say about core vaccines (distemper, parvo, adenovirus, leptospirosis, rabies), puppy series timing and booster intervals.",
         "How often do dogs need vaccines? Core and non core vaccines explained",
         "Not every vaccine is yearly. Under the American Animal Hospital Association (AAHA) guidelines, after the puppy series and one booster within a year, the distemper, adenovirus and parvovirus combination vaccine is boosted every 3 years, the leptospirosis vaccine every year, and rabies as local law requires. Non core vaccines such as kennel cough, Lyme disease and canine influenza are given, usually yearly, only to dogs whose lifestyle or location puts them at risk.",
         """
<h2>Core and non core vaccines</h2>
<p>The AAHA, whose canine vaccination guidelines are widely used by vets in North America, sorts vaccines into two groups:</p>
<ul><li><b>Core vaccines</b> are recommended for all dogs, whatever their lifestyle, unless there is a specific medical reason not to vaccinate: canine distemper virus, canine adenovirus type 2, canine parvovirus type 2, leptospirosis and rabies. Leptospirosis was added to the core list in a 2024 update.</li>
<li><b>Non core vaccines</b> are recommended for some dogs based on lifestyle, geographic location and risk of exposure: Bordetella bronchiseptica (often part of "kennel cough" protection), canine Lyme disease, canine influenza and the Western diamondback rattlesnake toxoid. The AAHA notes that where a disease such as Lyme is common, local vets may treat that vaccine as core.</li></ul>
<h2>The puppy series</h2>
<p>Puppies need several doses because antibodies passed on from their mother can block a vaccine from working. The AAHA's distemper guidance explains that these maternal antibodies decline over time and are usually gone by 12 to 14 weeks, which is why doses are repeated every 2 to 4 weeks until the puppy is over 16 weeks old (some vets prefer to give a final dose at 18 to 20 weeks where distemper risk is high).</p>
<div class="tablewrap"><table><thead><tr><th>Vaccine</th><th>Puppies 16 weeks or younger</th><th>Dogs over 16 weeks (first time)</th><th>Boosters</th></tr></thead><tbody>
<tr><td>Distemper, adenovirus, parvovirus (with or without parainfluenza)</td><td>At least 3 doses of a combination vaccine between 6 and 16 weeks, 2 to 4 weeks apart</td><td>2 doses, 2 to 4 weeks apart</td><td>One dose within 1 year of the last initial dose, then every 3 years</td></tr>
<tr><td>Leptospirosis</td><td>2 doses, 2 to 4 weeks apart, starting at 12 weeks</td><td>2 doses, 2 to 4 weeks apart</td><td>One dose within 1 year, then every year</td></tr>
<tr><td>Rabies</td><td colspan="3">As required by law</td></tr>
<tr><td>Bordetella (non core)</td><td colspan="2">One intranasal or oral dose, or two injected doses, for dogs at risk</td><td>Yearly</td></tr>
<tr><td>Lyme disease (non core)</td><td colspan="2">2 doses, 2 to 4 weeks apart</td><td>One dose within 1 year, then yearly</td></tr>
<tr><td>Canine influenza (non core)</td><td colspan="2">2 doses, 2 to 4 weeks apart</td><td>One dose within 1 year, then yearly</td></tr>
</tbody></table></div>
<p class="note">Source: AAHA 2022 Canine Vaccination Guidelines, Table 2, as updated in 2024. These are general recommendations; vets adapt them to each dog and to vaccine labels.</p>
<h2>So why does my dog see the vet every year?</h2>
<p>Because some vaccines, such as leptospirosis and most non core vaccines, really are yearly, and because the AAHA recommends that each dog's vaccine needs be reassessed at least once a year as travel, lifestyle and local disease risks change. An annual visit is also the chance for a full health check, teeth, weight and parasite prevention. So a yearly appointment is normal, even if your dog does not get every vaccine every year.</p>
<p>On the 3 year interval for distemper, the AAHA says annual boosters are not necessary after the first adult booster. It also notes that longer immunity than 3 years has been suggested but is largely unsubstantiated in peer reviewed research, which is why it does not recommend going longer.</p>
<h2>Overdue or unknown history</h2>
<p>Adopted a dog with no records, or missed a booster? The AAHA's guidance is that the benefits of vaccinating outweigh the risks in most cases where vaccination history is unknown, summed up as "when in doubt, vaccinate". For rabies, follow local law. Your vet will advise on restarting a series.</p>
<h2>Outside the US</h2>
<p>The AAHA guidelines are written for North America. Which diseases are common, which vaccines are licensed, and the legal rules for rabies all differ by country, so your local vet's schedule may look a little different. The core idea is the same everywhere: protect every dog against the most serious widespread diseases, and add other vaccines based on real risk.</p>
""",
         faq=[("Do dogs need vaccines every year?", "Some do and some do not. Under the AAHA guidelines, leptospirosis and most non core vaccines are yearly, while the distemper, adenovirus and parvovirus combination is given every 3 years after the first adult booster. Rabies follows local law."),
              ("What are the core vaccines for dogs?", "The AAHA lists canine distemper, canine adenovirus type 2, canine parvovirus, leptospirosis and rabies as core vaccines recommended for all dogs."),
              ("When is a puppy fully vaccinated?", "The AAHA recommends repeating the combination vaccine every 2 to 4 weeks until the puppy is over 16 weeks old, followed by a booster within a year. Your vet will tell you when your puppy's course is complete.")],
         sources=src("aaha_vax", "aaha_table", "aaha_cdv"),
         related=[("health.html#vaccines", "Health: vaccines"), ("blog/puppy-socialization-window.html", "Puppy socialization window"), ("health.html#checkups", "Routine checkups"), ("glossary.html#core-vaccine", "Glossary: core vaccine")])

    # 4 alpha
    post(page, "alpha-dog-myth", "Is the Alpha Dog Idea True? What Research Says About Dominance | Dog Field Guide",
         "Do you need to be the alpha or pack leader? Where the dominance idea came from, what wolf research by L. David Mech found, and why veterinary behaviorists reject alpha training.",
         "Is the \"alpha dog\" idea true? What the research says about dominance",
         "No. The popular idea that your dog is trying to dominate you, and that you must act as the \"alpha\", is not supported by modern research. Wolf biologist L. David Mech found that wild wolf packs are families led by the parents rather than groups fighting for rank, and the American Veterinary Society of Animal Behavior advises against trainers who rely on dominance, pack leader or alpha theories and against forceful techniques such as alpha rolls.",
         """
<h2>Where the alpha idea came from</h2>
<p>The classic picture of a wolf pack is a group of individuals constantly competing for rank, kept in check by an "alpha" male and female. In his 1999 paper in the <i>Canadian Journal of Zoology</i>, Mech points out that most research on wolf pack social dynamics had been done on "non natural assortments of captive wolves", unrelated adults housed together. Dog training borrowed that picture and concluded that dogs, as descendants of wolves, must be trying to climb a hierarchy in the home, and that owners should win by force.</p>
<h2>What wild wolves actually do</h2>
<p>Mech based his paper on a literature review and 13 summers of observing free living wolves on Ellesmere Island in the Canadian Arctic. He concluded that the typical wolf pack is a family: the adult parents guide the group's activities through a division of labor, with the female mainly leading pup care and defense and the male mainly leading foraging, food provision and travel. In other words, the "alphas" are simply the parents, and their status comes from being the parents, not from winning fights.</p>
<h2>Dogs are not wolves anyway</h2>
<p>Even if captive wolf studies had been right about wolves, dogs living with people are a different situation: a different species relationship, a different environment, and thousands of years of domestication. Explaining a dog's behavior toward its owner with a model built on unrelated captive wolves stacks one shaky assumption on another.</p>
<h2>What veterinary behaviorists say</h2>
<p>The American Veterinary Society of Animal Behavior's 2021 position statement on humane dog training:</p>
<ul><li>advises that clients should be steered away from trainers who discuss out dated ideas such as "dominance", "leader of the pack" or "alpha" theories;</li>
<li>lists forceful manipulation such as "alpha rolls" and "dominance downs" among intimidation techniques to avoid, along with shouting, staring and physical corrections;</li>
<li>notes that aversive methods are associated with increased anxiety, fear related aggression, avoidance and learned helplessness;</li>
<li>says reward based methods are more effective and that there is no evidence aversive training is necessary.</li></ul>
<p>An earlier AVSAB puppy socialization statement made the same point: positive, consistent training is associated with fewer behavior problems and greater obedience than methods involving punishment or encouraging human dominance.</p>
<h2>So what is going on when my dog...</h2>
<div class="tablewrap"><table><thead><tr><th>Behavior often called "dominant"</th><th>A more useful explanation</th><th>What helps</th></tr></thead><tbody>
<tr><td>Pulling on the lead</td><td>Pulling gets the dog where it wants to go, so it is reinforced every walk.</td><td>Reward a loose lead; stop when the lead goes tight (<a href="{R}training.html#first">how to</a>).</td></tr>
<tr><td>Jumping up</td><td>An enthusiastic greeting that gets attention, even negative attention.</td><td>Reward four paws on the floor or a sit; manage greetings with a lead.</td></tr>
<tr><td>Going through doors first</td><td>The interesting stuff is on the other side.</td><td>Teach a short wait at the door with rewards, if it matters to you.</td></tr>
<tr><td>Growling over food or toys</td><td>Worry about losing something valuable (resource guarding).</td><td>Do not snatch or punish; trade for something better and ask your vet or a qualified behavior professional for help.</td></tr>
<tr><td>Not coming when called</td><td>Something else is more rewarding than you right now.</td><td>Make coming back the best deal in the park; use a long line while training.</td></tr>
</tbody></table></div>
<p>Punishing a growl is risky: it can suppress the warning without changing the worry behind it. For any aggression, AVSAB says to use humane methods with no exceptions and to involve a vet or a qualified behavior professional.</p>
<h2>Leadership without force</h2>
<p>Dogs do need structure. AVSAB is explicit that reward based training does not mean letting dogs do whatever they want: animals learn best with structure, routine and guidelines, taught without fear, intimidation or pain. Think of yourself less as an alpha and more as a good teacher or parent: you control the resources, set up the environment so the right choice is easy, and reward the behavior you want to see more of. Start with our <a href="{R}training.html">training guide</a>.</p>
""",
         faq=[("Should I be the alpha or pack leader for my dog?", "No. Veterinary behaviorists at AVSAB advise against dominance or alpha based training. Be a consistent teacher instead: provide structure and reward the behavior you want."),
              ("Did the scientist who studied alpha wolves change his mind?", "L. David Mech's 1999 paper, based on 13 summers watching wild wolves, concluded that a typical wild pack is a family led by the parents, and that most earlier research on pack dominance came from unnatural groups of captive wolves."),
              ("Is an alpha roll ever OK?", "AVSAB lists alpha rolls and dominance downs among intimidation techniques that should be avoided, because aversive methods are linked to fear, anxiety and aggression.")],
         sources=src("mech", "avsab_train", "avsab_puppy"),
         related=[("training.html", "Reward based training"), ("behavior.html#dominance", "Behavior: the dominance myth"), ("behavior.html#problems", "Problem behaviors"), ("blog/puppy-socialization-window.html", "Puppy socialization window")])

    # 5 weight
    post(page, "is-my-dog-overweight", "Is My Dog Overweight? How to Use the 9 Point Body Condition Score | Dog Field Guide",
         "Check your dog's weight at home with the 9 point body condition score used on the WSAVA chart: ribs, waist and belly tuck explained, plus what a lifetime study found about lean dogs.",
         "Is my dog overweight? How to use the 9 point body condition score",
         "Your dog is probably at a healthy weight if you can easily feel its ribs under a thin layer of fat, see a waist behind the ribs when you look down from above, and see the belly tuck up when you look from the side. That is a score of 4 to 5 on the 9 point body condition score used on the World Small Animal Veterinary Association (WSAVA) chart; 6 and above is over ideal. It matters: in a 14 year study, Labradors kept lean lived a median 1.8 years longer than their heavier littermates.",
         """
<h2>How to body condition score your dog in three checks</h2>
<ol><li><b>Feel the ribs.</b> Run your flat hands along your dog's sides. At an ideal weight the ribs are easy to feel with only a thin covering of fat, a bit like the back of your hand. If you have to press hard to find them, your dog is carrying extra fat.</li>
<li><b>Look from above.</b> Stand over your dog. You should see a waist, an inward curve behind the ribs.</li>
<li><b>Look from the side.</b> The belly should tuck up between the ribs and the back legs rather than hang level or sag.</li></ol>
<p>Fluffy coats hide a lot, so rely on your hands as much as your eyes.</p>
<h2>The 9 point scale, in plain English</h2>
<p>This summary paraphrases the descriptions on the WSAVA body condition score chart for dogs.</p>
<div class="tablewrap"><table><thead><tr><th>Score</th><th>Category</th><th>What you find</th></tr></thead><tbody>
<tr><td>1</td><td class="no">Under ideal</td><td>Ribs, spine, pelvic bones and other bones visible from a distance; no body fat; obvious muscle loss.</td></tr>
<tr><td>2</td><td class="no">Under ideal</td><td>Ribs, spine and pelvic bones easily visible; no fat can be felt; some muscle loss.</td></tr>
<tr><td>3</td><td class="caution">Under ideal</td><td>Ribs easy to feel and may be visible with no fat felt; tops of the spine visible; pelvic bones becoming prominent; obvious waist and tuck.</td></tr>
<tr><td>4</td><td class="yes">Ideal</td><td>Ribs easy to feel with minimal fat covering; waist easily seen from above; belly tuck evident.</td></tr>
<tr><td>5</td><td class="yes">Ideal</td><td>Ribs can be felt without excess fat; waist seen behind the ribs from above; belly tucked up from the side.</td></tr>
<tr><td>6</td><td class="caution">Over ideal</td><td>Ribs felt with slight excess fat; waist visible from above but not prominent; belly tuck still apparent.</td></tr>
<tr><td>7</td><td class="caution">Over ideal</td><td>Ribs hard to feel under heavy fat; fat deposits over the lower back and base of the tail; waist absent or barely visible.</td></tr>
<tr><td>8</td><td class="no">Over ideal</td><td>Ribs cannot be felt, or only with firm pressure; heavy fat over the lower back and tail base; no waist and no tuck; belly may be visibly swollen.</td></tr>
<tr><td>9</td><td class="no">Over ideal</td><td>Massive fat deposits over the chest, spine and tail base; fat on the neck and legs; no waist or tuck; obvious belly distension.</td></tr>
</tbody></table></div>
<h2>Why a lean dog matters: the lifetime study</h2>
<p>The best known evidence comes from a 14 year study, published by Kealy and colleagues in the <i>Journal of the American Veterinary Medical Association</i> in 2002 and described by the University of Pennsylvania School of Veterinary Medicine, one of the partner institutions. Researchers paired 48 Labrador retrievers from seven litters, and from 8 weeks of age fed one dog in each pair 25 percent less than its littermate. The study was funded and run by Nestl&eacute; Purina PetCare with university partners.</p>
<ul><li>The leaner dogs lived a median of <b>13 years</b>, compared with <b>11.2 years</b> for their littermates, who were uniformly overweight: a difference of 1.8 years.</li>
<li>Hip osteoarthritis was less common and appeared later. By age 10, 6 of the restricted dogs had hip osteoarthritis compared with 19 of the others.</li>
<li>The leaner dogs did not need treatment for osteoarthritis until a mean age of 13.3 years, about three years later than the control group.</li>
<li>Other chronic conditions also started later, by 2.1 years on average.</li></ul>
<p>One study in one breed cannot predict exactly what will happen to your dog, but it is strong evidence that keeping dogs lean, with ribs you can feel and a visible waist, is one of the most valuable things an owner can do.</p>
<h2>If your dog scores 6 or more</h2>
<ol><li><b>See your vet first.</b> They can confirm the score, set a target weight and safe rate of loss, and check for medical causes.</li>
<li><b>Measure food.</b> Weigh or measure every meal rather than estimating, and feed for the target weight your vet suggests rather than the current weight.</li>
<li><b>Count treats.</b> Treats, chews and table scraps add up. Use part of the daily food allowance as training treats, or low calorie options such as green beans or carrot pieces (see the <a href="{R}can-dogs-eat.html">Can dogs eat this?</a> table).</li>
<li><b>Add activity gradually</b>, especially for older or very overweight dogs: longer sniffy walks, gentle play and food puzzle toys.</li>
<li><b>Re-score every couple of weeks</b> and weigh regularly on the same scale.</li></ol>
<p>Never put a dog on a crash diet; sudden severe restriction can be harmful, so let your vet guide the plan.</p>
""",
         faq=[("What is the ideal body condition score for a dog?", "On the 9 point scale used on the WSAVA chart, 4 to 5 is ideal: ribs easy to feel without excess fat, a visible waist from above and a tucked belly from the side."),
              ("Can I tell if my dog is overweight just by weighing it?", "Not reliably on its own, because healthy weight varies between individual dogs. A body condition score, done with your hands and eyes, tells you how much fat your dog carries. Use both, and ask your vet for a target weight."),
              ("Do lean dogs live longer?", "In a 14 year study of 48 Labrador retrievers, dogs fed 25 percent less than their littermates lived a median of 13 years versus 11.2 years and developed osteoarthritis later.")],
         sources=src("wsava_bcs", "penn_kealy"),
         related=[("care.html#weight", "Care: healthy weight"), ("health.html#weight", "Health: weight"), ("can-dogs-eat.html", "Low calorie treat ideas"), ("dog-age-calculator.html", "Dog age calculator")])

    # blog index
    items = "".join('<article class="card"><h2><a href="{R}blog/%s.html">%s</a></h2><p>%s</p><p class="meta">Published 8 October 2026</p></article>' % (s, h, d) for s, h, d in POSTS)
    page("blog/index.html", "Dog Field Guide Blog: Answer First Dog Care Articles | Dog Field Guide",
         "Answer first articles on single dog questions: chocolate poisoning doses, the puppy socialization window, vaccine schedules, the alpha dog myth and body condition scoring.",
         items, h1="Dog Field Guide blog", kind="webpage",
         lead="Each article answers one dog question directly at the top, then explains the detail and the sources behind it.",
         crumbs=[("index.html", "Home"), ("blog/index.html", "Blog")], nav="blog/")

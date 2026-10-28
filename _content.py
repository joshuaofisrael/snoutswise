"""Page content for SnoutsWise. Original writing; every factual claim is tied to a listed source."""
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
 "neitz1989": ("Neitz J, Geist T, Jacobs GH (1989). Color vision in the dog. Visual Neuroscience 3(2):119 to 125", "Cambridge University Press", "https://doi.org/10.1017/s0952523800004430"),
 "kasparson2013": ("Kasparson AA, Badridze J, Maximov VV (2013). Colour cues proved to be more informative for dogs than brightness. Proceedings of the Royal Society B 280:20131356", "PubMed Central (open access)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3730601/"),
 "miller1995": ("Miller PE, Murphy CJ (1995). Vision in dogs. Journal of the American Veterinary Medical Association 207(12):1623 to 1634", "Europe PMC record", "https://europepmc.org/article/MED/7493905"),
 "akc_color": ("Can Dogs See Color?", "American Kennel Club", "https://www.akc.org/expert-advice/health/are-dogs-color-blind/"),
 "sueda2008": ("Sueda KLC, Hart BL, Cliff KD (2008). Characterisation of plant eating in dogs. Applied Animal Behaviour Science 111(1-2):120 to 132. DOI 10.1016/j.applanim.2007.05.018", "Elsevier", "https://doi.org/10.1016/j.applanim.2007.05.018"),
 "stahler2006": ("Stahler DR, Smith DW, Guernsey DS (2006). Foraging and feeding ecology of the gray wolf (Canis lupus): lessons from Yellowstone National Park, Wyoming, USA. The Journal of Nutrition 136(7):1923S to 1926S. DOI 10.1093/jn/136.7.1923S", "PubMed record", "https://pubmed.ncbi.nlm.nih.gov/16772460/"),
 "hart2021": ("Hart BL, Hart LA, Thigpen AP, Willits NH (2021). Characteristics of plant eating in domestic cats. Animals 11(7):1853. DOI 10.3390/ani11071853", "PubMed Central (open access)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC8300339/"),
 "becuwe2012": ("Bécuwe-Bonnet V, Bélanger MC, Frank D, Parent J, Hélie P (2012). Gastrointestinal disorders in dogs with excessive licking of surfaces. Journal of Veterinary Behavior 7(4):194 to 204. DOI 10.1016/j.jveb.2011.07.003", "Elsevier", "https://doi.org/10.1016/j.jveb.2011.07.003"),
 "aspca_plants": ("Toxic and Non-Toxic Plants", "ASPCA Animal Poison Control", "https://www.aspca.org/pet-care/aspca-poison-control/toxic-and-non-toxic-plants"),
 "sommese2022": ("Sommese A, Miklósi Á, Pogány Á, Temesi A, Dror S, Fugazza C (2022; online 2021). An exploratory analysis of head-tilting in dogs. Animal Cognition 25(3):701 to 705. DOI 10.1007/s10071-021-01571-8", "Springer Nature (open access)", "https://doi.org/10.1007/s10071-021-01571-8"),
 "fugazza2021": ("Fugazza C, Dror S, Sommese A, Temesi A, Miklósi Á (2021). Word learning dogs (Canis familiaris) provide an animal model for studying exceptional performance. Scientific Reports 11:14070. DOI 10.1038/s41598-021-93581-2", "Scientific Reports (open access)", "https://doi.org/10.1038/s41598-021-93581-2"),
 "ratcliffe2014": ("Ratcliffe VF, Reby D (2014). Orienting asymmetries in dogs' responses to different communicatory components of human speech. Current Biology 24(24):2908 to 2912. DOI 10.1016/j.cub.2014.10.030", "PubMed record", "https://pubmed.ncbi.nlm.nih.gov/25454584/"),
 "mertens2023": ("Mertens A, Schenk H, Volk H (2023). Current definition, diagnosis, and treatment of canine and feline idiopathic vestibular syndrome. Frontiers in Veterinary Science 10:1263976. DOI 10.3389/fvets.2023.1263976", "Frontiers (open access)", "https://doi.org/10.3389/fvets.2023.1263976"),
 "kis2014": ("Kis A, Szakadát S, Kovács E, Gácsi M, Simor P, Gombos F, Topál J, Miklósi Á, Bódizs R (2014). Development of a non-invasive polysomnography technique for dogs (Canis familiaris). Physiology & Behavior 130:149 to 156. DOI 10.1016/j.physbeh.2014.04.004", "Elsevier / author manuscript (real.mtak.hu)", "https://doi.org/10.1016/j.physbeh.2014.04.004"),
 "kis2017": ("Kis A, Szakadát S, Gácsi M, Kovács E, Simor P, Török C, Gombos F, Bódizs R, Topál J (2017). The interrelated effect of sleep and learning in dogs (Canis familiaris); an EEG and behavioural study. Scientific Reports 7:41873. DOI 10.1038/srep41873", "Scientific Reports (open access)", "https://doi.org/10.1038/srep41873"),
 "bodizs2020": ("Bódizs R, Kis A, Gácsi M, Topál J (2020). Sleep in the dog: comparative, behavioral and translational relevance. Current Opinion in Behavioral Sciences 33:25 to 33. DOI 10.1016/j.cobeha.2019.12.006", "Elsevier (open access CC BY-NC-ND)", "https://doi.org/10.1016/j.cobeha.2019.12.006"),
 "harris2014": ("Harris CR, Prouvost C (2014). Jealousy in Dogs. PLoS ONE 9(7): e94597. DOI 10.1371/journal.pone.0094597", "PLoS ONE (open access)", "https://doi.org/10.1371/journal.pone.0094597"),
 "abdai2018": ("Abdai J, Baño Terencio C, Pérez Fraga P, Miklósi Á (2018). Investigating jealous behaviour in dogs. Scientific Reports 8:8911. DOI 10.1038/s41598-018-27251-1", "Scientific Reports (open access)", "https://doi.org/10.1038/s41598-018-27251-1"),
 "mariner2026": ("Mariner BL, McCoy BM, Greenier A, Brassington L, et al. (2026). Epigenetic aging and transposon dysregulation reflect size-related lifespan compression in dogs. Science 394(6820), published 8 October 2026. DOI 10.1126/science.aeb2986", "Science", "https://doi.org/10.1126/science.aeb2986"),
 "asu2026": ("Caspermeyer J (8 October 2026). Why big dogs age faster. ASU News, Arizona State University", "ASU News", "https://news.asu.edu/20261008-health-and-medicine-why-big-dogs-age-faster"),
 "joly2008": ("Joly-Mascheroni RM, Senju A, Shepherd AJ (2008). Dogs catch human yawns. Biology Letters 4(5): 446-448. DOI 10.1098/rsbl.2008.0333", "Biology Letters", "https://doi.org/10.1098/rsbl.2008.0333"),
 "harr2009": ("Harr AL, Gilbert VR, Phillips KA (2009). Do dogs (Canis familiaris) show contagious yawning? Animal Cognition 12(6): 833-837. DOI 10.1007/s10071-009-0233-0", "Animal Cognition", "https://doi.org/10.1007/s10071-009-0233-0"),
 "madsen2013": ("Madsen EA, Persson T (2013). Contagious yawning in domestic dog puppies (Canis lupus familiaris): the effect of ontogeny and emotional closeness on low-level imitation in dogs. Animal Cognition 16(2): 233-240. DOI 10.1007/s10071-012-0568-9", "Animal Cognition", "https://doi.org/10.1007/s10071-012-0568-9"),
 "romero2013": ("Romero T, Konno A, Hasegawa T (2013). Familiarity bias and physiological responses in contagious yawning by dogs support link to empathy. PLoS ONE 8(8): e71365. DOI 10.1371/journal.pone.0071365", "PLoS ONE (open access)", "https://doi.org/10.1371/journal.pone.0071365"),
 "wilson2022": ("Wilson C, Campbell K, Petzel Z, Reeve C (2022). Dogs can discriminate between human baseline and psychological stress condition odours. PLOS ONE 17(9): e0274143. DOI 10.1371/journal.pone.0274143", "PLOS ONE (open access)", "https://doi.org/10.1371/journal.pone.0274143"),
 "daniello2018": ("D'Aniello B, Semin GR, Alterisio A, Aria M, Scandurra A (2018). Interspecies transmission of emotional information via chemosignals: from humans to dogs (Canis lupus familiaris). Animal Cognition 21(1): 67-78. DOI 10.1007/s10071-017-1139-x", "Animal Cognition", "https://doi.org/10.1007/s10071-017-1139-x"),
 "hare2002": ("Hare B, Brown M, Williamson C, Tomasello M (2002). The domestication of social cognition in dogs. Science 298(5598): 1634-1636. DOI 10.1126/science.1072702", "Science", "https://doi.org/10.1126/science.1072702"),
 "bray2021": ("Bray EE, Gnanadesikan GE, Horschler DJ, Levy KM, Kennedy BS, Famula TR, MacLean EL (2021). Early-emerging and highly heritable sensitivity to human communication in dogs. Current Biology 31(14): 3132-3136. DOI 10.1016/j.cub.2021.04.055", "Current Biology", "https://doi.org/10.1016/j.cub.2021.04.055"),
 "salomons2021": ("Salomons H, Smith KCM, Callahan-Beckel M, et al. (2021). Cooperative communication with humans evolved to emerge early in domestic dogs. Current Biology 31(14): 3137-3144. DOI 10.1016/j.cub.2021.06.051", "Current Biology (free full text via PubMed Central)", "https://doi.org/10.1016/j.cub.2021.06.051"),
 "alsulami2026": ("Alsulami A, Bogdani M, MacLean EL, Keene CD, McGrath S, Dog Aging Project Consortium, Latimer CS, Moreno JA (2026). Alzheimer's disease neuropathological characterization of the dog brain and relationship to biofluid biomarkers and cognitive function. npj Dementia 2: 88. DOI 10.1038/s44400-026-00141-4", "npj Dementia (open access)", "https://doi.org/10.1038/s44400-026-00141-4"),
 "uw2026ccd": ("Similar brain patterns seen in dogs, humans with dementia (6 October 2026)", "UW Medicine Newsroom", "https://newsroom.uw.edu/news-releases/similar-brain-patterns-seen-in-dogs-humans-with-dementia"),
 "parrcortes2024": ("Parr-Cortes Z, M\u00fcller C, Talas L, Mendl M, Guest C, Rooney N (2024). The odour of an unfamiliar stressed or relaxed person affects dogs' responses to a cognitive bias test. Scientific Reports 14: 15843. DOI 10.1038/s41598-024-66147-1", "Scientific Reports (open access)", "https://doi.org/10.1038/s41598-024-66147-1"),
 "biffi2026": ("Biffi E, Pedretti G, Normando S, Lazebnik T, Loconsole M, Valsecchi P (2026). Hearing shapes: the Bouba-Kiki effect in adult domestic dogs. Proceedings of the Royal Society B 293(2080): 20261209. DOI 10.1098/rspb.2026.1209", "Proceedings of the Royal Society B (open access)", "https://doi.org/10.1098/rspb.2026.1209"),
 "newsci2026bouba": ("Woodford J (14 October 2026). Dogs are susceptible to the bouba-kiki effect. New Scientist.", "New Scientist", "https://www.newscientist.com/article/2593290-dogs-are-susceptible-to-the-bouba-kiki-effect/"),
 "quaranta2007": ("Quaranta A, Siniscalchi M, Vallortigara G (2007). Asymmetric tail-wagging responses by dogs to different emotive stimuli. Current Biology 17(6): R199-R201. DOI 10.1016/j.cub.2007.02.008", "Current Biology", "https://doi.org/10.1016/j.cub.2007.02.008"),
 "siniscalchi2013": ("Siniscalchi M, Lusito R, Vallortigara G, Quaranta A (2013). Seeing left- or right-asymmetric tail wagging produces different emotional responses in dogs. Current Biology 23(22): 2279-2282. DOI 10.1016/j.cub.2013.09.027", "Current Biology", "https://doi.org/10.1016/j.cub.2013.09.027"),
 "balint2020": ("Bálint A, Andics A, Gácsi M, Gábor A, Czeibert K, Luce CM, Miklósi Á, Kröger RHH (2020). Dogs can sense weak thermal radiation. Scientific Reports 10: 3736. DOI 10.1038/s41598-020-60439-y", "Scientific Reports", "https://doi.org/10.1038/s41598-020-60439-y"),
 "fugazza2021rapid": ("Fugazza C, Andics A, Magyari L, Dror S, Zempléni A, Miklósi Á (2021). Rapid learning of object names in dogs. Scientific Reports 11: 2222. DOI 10.1038/s41598-021-81699-2", "Scientific Reports", "https://doi.org/10.1038/s41598-021-81699-2"),
 "kaminski2019": ("Kaminski J, Waller BM, Diogo R, Hartstone-Rose A, Burrows AM (2019). Evolution of facial muscle anatomy in dogs. Proceedings of the National Academy of Sciences 116(29): 14677-14681. DOI 10.1073/pnas.1820653116", "PNAS", "https://doi.org/10.1073/pnas.1820653116"),
 "kaminski2017": ("Kaminski J, Hynds J, Morris P, Waller BM (2017). Human attention affects facial expressions in domestic dogs. Scientific Reports 7: 12914. DOI 10.1038/s41598-017-12781-x", "Scientific Reports", "https://doi.org/10.1038/s41598-017-12781-x"),
 "benaderet2017": ("Ben-Aderet T, Gallego-Abenza M, Reby D, Mathevon N (2017). Dog-directed speech: why do we use it and do dogs pay attention to it? Proceedings of the Royal Society B 284: 20162429. DOI 10.1098/rspb.2016.2429", "Proceedings of the Royal Society B", "https://doi.org/10.1098/rspb.2016.2429"),
 "benjamin2018": ("Benjamin A, Slocombe K (2018). 'Who's a good boy?!' Dogs prefer naturalistic dog-directed speech. Animal Cognition 21: 353-364. DOI 10.1007/s10071-018-1172-4", "Animal Cognition", "https://doi.org/10.1007/s10071-018-1172-4"),
 "horowitz2017": ("Horowitz A (2017). Smelling themselves: Dogs investigate their own odours longer when modified in an 'olfactory mirror' test. Behavioural Processes 143: 17-24. DOI 10.1016/j.beproc.2017.08.001", "Behavioural Processes", "https://doi.org/10.1016/j.beproc.2017.08.001"),
 "gallup1970": ("Gallup GG Jr (1970). Chimpanzees: self-recognition. Science 167(3914): 86-87. DOI 10.1126/science.167.3914.86", "Science", "https://doi.org/10.1126/science.167.3914.86"),
 "leonetti2024": ("Leonetti S, Cimarelli G, Hersh TA, Ravignani A (2024). Why do dogs wag their tails? Biology Letters 20(1): 20230407. DOI 10.1098/rsbl.2023.0407", "Biology Letters", "https://doi.org/10.1098/rsbl.2023.0407"),
 "gart2015": ("Gart S, Socha JJ, Vlachos PP, Jung S (2015). Dogs lap using acceleration-driven open pumping. Proceedings of the National Academy of Sciences 112(52): 15798-15802. DOI 10.1073/pnas.1514842112", "PNAS", "https://doi.org/10.1073/pnas.1514842112"),
 "crompton2011": ("Crompton AW, Musinsky C (2011). How dogs lap: ingestion and intraoral transport in Canis familiaris. Biology Letters 7(6): 882-884. DOI 10.1098/rsbl.2011.0336", "Biology Letters", "https://doi.org/10.1098/rsbl.2011.0336"),
 "reis2010": ("Reis PM, Jung S, Aristoff JM, Stocker R (2010). How cats lap: water uptake by Felis catus. Science 330(6008): 1231-1234. DOI 10.1126/science.1195421", "Science", "https://doi.org/10.1126/science.1195421"),
 "prato2018": ("Prato-Previde E, Nicotra V, Pelosi A, Valsecchi P (2018). Pet dogs' behavior when the owner and an unfamiliar person attend to a faux rival. PLoS ONE 13(4): e0194577. DOI 10.1371/journal.pone.0194577", "PLoS ONE (open access)", "https://doi.org/10.1371/journal.pone.0194577"),
 "merck_nutr": ("Sanderson SL. Nutritional Requirements of Small Animals (full review Nov 2023, updated Sept 2024)", "Merck Veterinary Manual", "https://www.merckvetmanual.com/management-and-nutrition/nutrition-small-animals/nutritional-requirements-of-small-animals"),
 "aaha_box1": ("2021 AAHA Nutrition and Weight Management Guidelines for Dogs and Cats, Box 1: Energy Requirement Calculations (PDF)", "American Animal Hospital Association", "https://www.aaha.org/wp-content/uploads/globalassets/02-guidelines/2021-nutrition-and-weight-management/resourcepdfs/nutritiongl_box1.pdf"),
 "aaha_feed": ("Feeding Plans for Healthy, Appropriate Weight Cats and Dogs (2021 AAHA Nutrition and Weight Management Guidelines)", "American Animal Hospital Association", "https://www.aaha.org/resources/2021-aaha-nutrition-and-weight-management-guidelines/feeding-plans-for-healthy-appropriate-weight-cats-and-dogs/"),
 "cline2021": ("Cline MG, Burns KM, Coe JB, Downing R, Durzi T, Murphy M, Parker V (2021). 2021 AAHA Nutrition and Weight Management Guidelines for Dogs and Cats. Journal of the American Animal Hospital Association 57(4): 153-178. DOI 10.5326/JAAHA-MS-7232", "JAAHA", "https://doi.org/10.5326/JAAHA-MS-7232"),
 "wsava_assess": ("WSAVA Nutritional Assessment Guidelines Task Force: Freeman L, Becvarova I, Cave N, et al. (2011). WSAVA Nutritional Assessment Guidelines. Journal of Small Animal Practice 52(7): 385-396. DOI 10.1111/j.1748-5827.2011.01079.x", "World Small Animal Veterinary Association", "https://wsava.org/wp-content/uploads/2020/01/WSAVA-Nutrition-Assessment-Guidelines-2011-JSAP.pdf"),
 "nrc_dog": ("Your Dog's Nutritional Needs: A Science Based Guide for Pet Owners (2006), based on Nutrient Requirements of Dogs and Cats", "National Research Council, The National Academies", "https://nap.nationalacademies.org/resource/10668/dog_nutrition_final_fix.pdf"),
}
import datetime
def nice(d):
    return datetime.date.fromisoformat(d).strftime("%-d %B %Y")

def src(*keys):
    return [S[k] for k in keys]

def register(page):
    home(page); breeds(page); care(page); health(page); training(page); behavior(page)
    can_dogs_eat(page); age_calc(page); feed_calc(page); faq(page); glossary(page); trust(page); blog(page)

# ------------------------------------------------------------------ HOME
def home(page):
    body = """
<section class="hero"><h1>SnoutsWise: plain answers about breeds, care, health, training and behavior</h1>
<p class="lead">SnoutsWise is a free, independent guide for dog owners. It explains breed groups, everyday care, health basics such as vaccines and normal vital signs, reward based training and dog behavior, and every page lists the veterinary and kennel club sources it relies on. Start with the tools below if you have an urgent question.</p>
<a class="btn" href="{R}can-dogs-eat.html">Can my dog eat this? Food lookup</a> <a class="btn alt" href="{R}how-much-to-feed-a-dog.html">How much to feed a dog</a> <a class="btn alt" href="{R}dog-age-calculator.html">Dog age calculator</a></section>
<h2>Tools</h2>
<div class="grid">
<a class="tile" href="{R}can-dogs-eat.html"><h3>Can my dog eat this?</h3><p>Our signature lookup: about 70 foods rated Safe, Caution or Toxic, with the reason, the source and what to do if eaten.</p></a>
<a class="tile" href="{R}how-much-to-feed-a-dog.html"><h3>How much to feed a dog</h3><p>Daily calorie calculator and chart by weight, using the RER formula and AAHA life stage factors, with cups or grams from your food label.</p></a>
<a class="tile" href="{R}dog-age-calculator.html"><h3>Dog age in human years</h3><p>Calculator based on the 2020 epigenetic clock study, not the old "times seven" rule.</p></a>
<a class="tile" href="{R}blog/dog-ate-chocolate.html"><h3>Dog ate chocolate?</h3><p>Estimate the dose from the type and amount, then call your vet.</p></a>
<a class="tile" href="{R}games/"><h3>Dog games</h3><p>Three free, original games: sort safe and toxic snacks, read dog body language and play fetch.</p></a>""" + ("" if __import__("os").environ.get("SW_NO_EDU") else "<a class=\"tile\" href=\"{R}teachers/\"><h3>For teachers</h3><p>Free printable dog worksheets and fact sheets with answer keys, lesson ideas and classroom games.</p></a>") + """
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
<li><a href="{R}blog/why-do-dogs-make-puppy-dog-eyes.html">Why do dogs make puppy dog eyes? A muscle wolves mostly lack</a></li>
<li><a href="{R}blog/do-dogs-like-baby-talk.html">Do dogs like baby talk? Puppies do, and adult dogs like it with dog words</a></li>
<li><a href="{R}blog/can-dogs-learn-toy-names.html">Can dogs learn the names of their toys? A few gifted dogs can, fast</a></li>
<li><a href="{R}blog/can-dogs-sense-heat-with-their-nose.html">Can dogs sense heat with their nose? A 2020 study says yes</a></li>
<li><a href="{R}blog/do-dogs-recognize-themselves-in-mirror.html">Do dogs recognize themselves in a mirror? Not by sight, but maybe by smell</a></li>
<li><a href="{R}blog/why-do-dogs-wag-their-tails.html">Why do dogs wag their tails? It signals arousal, not just happiness</a></li>
<li><a href="{R}blog/how-do-dogs-drink-water.html">How do dogs drink water? A fast tongue pulls up a column of water</a></li>
<li><a href="{R}blog/dog-dementia-brain-study.html">News: senior dogs with dementia show early Alzheimer's-like brain changes</a></li>
<li><a href="{R}blog/do-dogs-understand-pointing.html">Do dogs understand pointing? Yes, and puppies can do it from about 8 weeks</a></li>
<li><a href="{R}blog/dogs-bouba-kiki-effect-study.html">News: dogs match "bouba" to round shapes and "kiki" to spiky ones</a></li>
<li><a href="{R}blog/can-dogs-smell-fear.html">Can dogs smell fear? The evidence says they can pick up on it</a></li>
<li><a href="{R}blog/big-dogs-age-faster-dna-study.html">News: big dogs show faster DNA aging, a Science study finds</a></li>
<li><a href="{R}blog/why-do-dogs-yawn.html">Why do dogs yawn? Sometimes stress, sometimes they catch yours</a></li>
<li><a href="{R}blog/do-dogs-feel-jealousy.html">Do dogs feel jealousy? They show jealousy-like behaviour in experiments</a></li>
<li><a href="{R}blog/do-dogs-dream.html">Do dogs dream? They have REM sleep, but dreams are still unproven</a></li>
<li><a href="{R}blog/why-do-dogs-tilt-their-heads.html">Why do dogs tilt their heads? It may mean they are listening hard</a></li>
<li><a href="{R}blog/why-do-dogs-eat-grass.html">Why do dogs eat grass? Usually because it is normal</a></li>
<li><a href="{R}blog/can-dogs-see-color.html">Can dogs see color? Yes, mostly blues and yellows</a></li>
<li><a href="{R}blog/dog-ate-chocolate.html">My dog ate chocolate: how much is dangerous?</a></li>
<li><a href="{R}blog/puppy-socialization-window.html">The puppy socialization window: when it closes and what to do</a></li>
<li><a href="{R}blog/dog-vaccine-schedule.html">How often do dogs need vaccines? Core and non core vaccines explained</a></li>
<li><a href="{R}blog/alpha-dog-myth.html">Is the "alpha dog" idea true? What the research says</a></li>
<li><a href="{R}blog/is-my-dog-overweight.html">Is my dog overweight? How to use the 9 point body condition score</a></li>
</ul></section>
<p class="note">SnoutsWise is general education, not veterinary advice. If your dog may have eaten something toxic or seems unwell, contact your vet or an emergency vet now. In the US, the ASPCA Animal Poison Control Center is on (888) 426-4435.</p>
"""
    page("index.html", "SnoutsWise: Sourced Dog Care Tips for New Owners",
         "Vet sourced dog care tips for new and experienced owners: feeding calculator, foods dogs can and can't eat, normal vital signs, dog age calculator and training.",
         body, kind="home", updated="2026-10-27")

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
    page("breeds.html", "Dog Breed Groups Explained: AKC vs Kennel Club | SnoutsWise",
         "Dog breed groups explained: the seven AKC and seven Royal Kennel Club groups side by side, what each group was bred for, and a checklist for choosing a breed.",
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
<p>How much to feed depends on your dog's weight, life stage and activity rather than the bag alone. Vets estimate daily calories from the resting energy requirement and a life stage factor; our <a href="{R}how-much-to-feed-a-dog.html">dog feeding calculator and calorie chart</a> does the sums and converts them into cups or grams, then you fine tune by body condition.</p>
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
    page("care.html", "Dog Care Tips for Beginners: Food, Teeth, Coat | SnoutsWise",
         "Dog care tips for beginners, with vet sources: how much to feed, keeping a healthy weight, exercise, brushing teeth, grooming, microchips and hot weather care.",
         body, h1="Dog care basics",
         lead="Good everyday care comes down to a complete and balanced diet, keeping your dog lean, daily exercise and mental stimulation, regular tooth brushing, grooming suited to the coat, permanent ID, and protecting your dog from heat and household toxins. The sections below explain each one and link to the veterinary sources behind the advice.",
         sources=src("akc_food", "aspca_foods", "wsava_bcs", "penn_kealy", "avsab_puppy", "avma_dental", "gov_chip", "rspca_heat"),
         related=[("how-much-to-feed-a-dog.html", "How much to feed a dog"), ("health.html", "Dog health basics"), ("blog/how-do-dogs-drink-water.html", "How dogs drink water"), ("can-dogs-eat.html", "Can dogs eat this? food table"), ("blog/is-my-dog-overweight.html", "Is my dog overweight?"), ("breeds.html", "Breed groups"), ("training.html", "Training")],
         crumbs=[("index.html", "Home"), ("care.html", "Care")], updated="2026-10-27")

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
<p>Extra weight shortens lives. In the Kealy lifetime study, Labradors kept lean lived a median 1.8 years longer than their heavier littermates and needed treatment for osteoarthritis later. Use the <a href="{R}blog/is-my-dog-overweight.html">body condition score guide</a> to check your dog, and the <a href="{R}how-much-to-feed-a-dog.html">feeding calculator</a> to estimate daily calories.</p></section>
<section id="checkups"><h2>Routine checkups</h2>
<p>Regular checkups let your vet review vaccines, parasite prevention, teeth, weight and any lumps or changes you have noticed. The AAHA guidelines say each dog's vaccine needs should be reassessed at least once a year. Write down questions beforehand, and mention changes in appetite, thirst, energy, toileting or behavior; behavior changes can be a sign of pain or illness.</p></section>
"""
    page("health.html", "Normal Dog Temperature and Vital Signs Chart | SnoutsWise",
         "Normal dog temperature in F and C, resting heart and breathing rates from the Merck Vet Manual, plus core vaccines, warning signs, poisoning and heatstroke aid.",
         body, h1="Dog health basics",
         lead="A healthy adult dog has an average body temperature of 101 to 102.5&deg;F (38.3 to 39.2&deg;C), a heart rate of 70 to 120 beats per minute and a resting breathing rate of 18 to 34 breaths per minute, according to the Merck Veterinary Manual. The basics of keeping a dog healthy are core vaccines, a lean body weight, dental care, regular checkups and knowing which warning signs mean you should call a vet immediately.",
         sources=src("merck_vitals", "aaha_vax", "aaha_table", "aspca_foods", "merck_foodpet", "rspca_heat", "avma_dental", "penn_kealy"),
         related=[("care.html", "Everyday care"), ("blog/dog-vaccine-schedule.html", "Dog vaccine schedule"), ("can-dogs-eat.html", "Can dogs eat this?"), ("blog/dog-ate-chocolate.html", "Dog ate chocolate"), ("how-much-to-feed-a-dog.html", "How much to feed a dog"), ("blog/why-do-dogs-eat-grass.html", "Why do dogs eat grass?"), ("blog/do-dogs-dream.html", "Do dogs dream?"), ("dog-age-calculator.html", "Dog age calculator")],
         crumbs=[("index.html", "Home"), ("health.html", "Health")], updated="2026-10-27")

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
<p>Keep sessions short (a few minutes), end while your dog is still keen, and practice in easy places before busier ones. After a hard new cue, a quiet rest helps: research on dog sleep and learning found that performance on new commands often improved after a nap or a night's sleep, while stacking an unrelated lesson in the same hour can interfere (<a href="{R}blog/do-dogs-dream.html">sleep, REM and learning</a>).</p></section>
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
    page("training.html", "Positive Reinforcement Dog Training Basics | SnoutsWise",
         "Positive reinforcement dog training basics: why vets back reward based methods, how markers, luring and shaping work, first skills to teach and tools to avoid.",
         body, h1="Dog training: the reward based approach",
         lead="Veterinary behavior experts recommend reward based training for all dogs: you teach the behavior you want and reward it, instead of punishing mistakes. The American Veterinary Society of Animal Behavior says the evidence shows reward based methods are more effective than aversive ones and better for welfare and the dog and owner relationship, and that there is no evidence aversive training is ever necessary.",
         sources=src("avsab_train", "avsab_puppy", "mech", "kis2017", "bray2021"),
         related=[("behavior.html", "Dog behavior"), ("blog/do-dogs-understand-pointing.html", "Do dogs understand pointing?"), ("blog/alpha-dog-myth.html", "The alpha dog myth"), ("blog/puppy-socialization-window.html", "Puppy socialization window"), ("blog/do-dogs-dream.html", "Do dogs dream? Sleep and learning"), ("breeds.html", "Breed groups"), ("faq.html", "Dog FAQ")],
         crumbs=[("index.html", "Home"), ("training.html", "Training")], updated="2026-10-18")

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
<tr><td>Yawning</td><td>Yawning in a tense situation rather than when sleepy (<a href="{R}blog/why-do-dogs-yawn.html">why dogs yawn</a>)</td></tr>
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
<p>Not every odd habit is a problem. Eating grass, for example, is common and usually normal: in a survey of 1,571 plant eating dogs, most did not seem ill beforehand or vomit afterwards (<a href="{R}blog/why-do-dogs-eat-grass.html">why dogs eat grass and when to call a vet</a>).</p>
<p>Head tilting is another everyday habit. In a 2021 study of 40 dogs, dogs that knew the names of their toys tilted their heads on 43% of requests, against 2% for typical dogs, which suggests the tilt goes with listening closely to meaningful words. A tilt that stays, or comes with stumbling or circling, is a reason to see a vet (<a href="{R}blog/why-do-dogs-tilt-their-heads.html">why dogs tilt their heads</a>).</p>
<p>Twitching, soft barks or paddling paws during a nap are usually REM sleep, not a behavior problem. Dogs have measurable REM with rapid eye movements and low muscle tone; whether that equals human-style dreaming is still unproven. After learning new commands, sleep can help performance improve (<a href="{R}blog/do-dogs-dream.html">do dogs dream and what REM research shows</a>).</p>
<p>Pushing in when you pet another dog is often jealousy-like behaviour, not "dominance". In experiments, dogs push, get between and sometimes snap more when owners affectionately attend to a rival dog (or a stuffed dog) than to a nonsocial object or a book (<a href="{R}blog/do-dogs-feel-jealousy.html">do dogs feel jealousy</a>).</p>
<p>AVSAB also recommends teaching puppies to enjoy short periods alone with a stuffed food toy, and offering a wide variety of experiences in the first year, which it links to a lower risk of separation related behavior.</p></section>
<section id="help"><h2>When to get professional help</h2>
<p>Seek help early for aggression, fear that is getting worse, behavior when left alone that leads to injury or damage, or any behavior that puts people or other animals at risk. AVSAB says animals with aggression should be treated with humane methods with no exceptions, and that trainers struggling with a case should refer to a vet, a board certified veterinary behaviorist or a certified applied animal behaviorist.</p></section>
"""
    page("behavior.html", "Dog Body Language and Stress Signals Explained | SnoutsWise",
         "Read dog body language: stress and fear signals, what tail wags mean, why puppy socialization matters, and what research says about alpha theory and problems.",
         body, h1="Dog behavior explained",
         lead="Most dog behavior makes sense once you ask what the dog is feeling and what the behavior gets it. Learn to spot stress signals such as lip licking, yawning, a lowered body and tucked tail; socialize puppies carefully during their first three months; and set aside the old dominance or alpha model, which wolf research and veterinary behaviorists no longer support.",
         sources=src("avsab_train", "avsab_puppy", "mech", "sueda2008", "sommese2022", "kis2014", "kis2017", "harris2014", "abdai2018", "joly2008", "romero2013"),
         related=[("training.html", "Reward based training"), ("blog/why-do-dogs-wag-their-tails.html", "Why do dogs wag their tails?"), ("blog/alpha-dog-myth.html", "Is the alpha dog idea true?"), ("blog/puppy-socialization-window.html", "Puppy socialization window"), ("blog/why-do-dogs-eat-grass.html", "Why do dogs eat grass?"), ("blog/why-do-dogs-tilt-their-heads.html", "Why do dogs tilt their heads?"), ("blog/do-dogs-dream.html", "Do dogs dream?"), ("blog/do-dogs-feel-jealousy.html", "Do dogs feel jealousy?"), ("blog/why-do-dogs-yawn.html", "Why do dogs yawn?"), ("blog/can-dogs-smell-fear.html", "Can dogs smell fear?"), ("blog/can-dogs-see-color.html", "Can dogs see color?"), ("health.html", "Health basics"), ("glossary.html", "Glossary")],
         crumbs=[("index.html", "Home"), ("behavior.html", "Behavior")], updated="2026-10-20")

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
            rows.append('<tr id="%s" data-v="%s"><td><b>%s</b></td><td class="%s"><span class="%s">%s</span></td><td>%s<p>%s</p><p><b>If eaten:</b> %s</p><p class="note">Last reviewed 8 Oct 2026 &middot; Sources: %s</p></td></tr>' % (slug(food), v, food, v, v, SHORT[v], call, why, IF_EATEN_OVERRIDE.get(food, IF_EATEN[v]), refs))
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
var h=location.hash.slice(1);if(h){var e=document.getElementById(h);if(e&&!e.classList.contains('cat'))e.style.outline='3px solid #A13D14'}run()})();"""
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
    page("can-dogs-eat.html", "Foods Dogs Can and Can't Eat: %d Foods Checked | SnoutsWise" % n,
         "Look up %d foods: which are toxic to dogs (grapes, chocolate, xylitol, onions), which need caution and which are safe, with sources and what to do if eaten." % n,
         body, h1="Can my dog eat this? %d foods rated Safe, Caution or Toxic" % n,
         lead="The foods most dangerous to dogs are chocolate and cocoa, grapes and raisins, onions, garlic and other Alliums, xylitol (in sugar free products), macadamia nuts, alcohol, raw yeast dough and caffeine. Many plain fruits and vegetables, such as apples, blueberries, carrots and green beans, are fine as occasional treats. Search the table below for a verdict and the veterinary or kennel club source behind it.",
         faq=faq, sources=src("aspca_foods", "akc_food", "akc_fruit", "merck_choc", "merck_xyl", "merck_foodpet", "cornell_xyl"),
         related=[("blog/dog-ate-chocolate.html", "Dog ate chocolate? Dose estimator"), ("health.html#poisoning", "Poisoning: first steps"), ("care.html#feeding", "Feeding your dog"), ("how-much-to-feed-a-dog.html", "How much to feed a dog"), ("blog/is-my-dog-overweight.html", "Is my dog overweight?"), ("faq.html", "Dog FAQ")],
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
    page("dog-age-calculator.html", "Dog Age Calculator: Dog Years to Human Years | SnoutsWise",
         "Convert dog years to human years with the epigenetic clock formula from a 2020 Cell Systems study (16 ln(age) + 31), plus a full table and its limits.",
         body, h1="Dog age calculator: dog years to human years",
         lead="The best evidence based conversion comes from a 2020 study of DNA methylation in 104 Labrador retrievers, which found that human age is roughly 16 &times; ln(dog age) + 31. By that formula a 1 year old dog is about 31 in human years, a 4 year old about 53, a 10 year old about 68 and a 14 year old about 73. Dogs age very quickly early in life and more slowly later, so the old times 7 rule is wrong at both ends.",
         faq=faq, sources=src("wang2020", "merck_vitals"),
         related=[("health.html", "Dog health basics"), ("care.html", "Everyday care"), ("blog/is-my-dog-overweight.html", "Keeping your dog lean"), ("how-much-to-feed-a-dog.html", "How much to feed a dog"), ("can-dogs-eat.html", "Can dogs eat this?"), ("faq.html", "Dog FAQ")],
         crumbs=[("index.html", "Home"), ("dog-age-calculator.html", "Dog age calculator")], script=script)

# ------------------------------------------------------------------ FEEDING CALCULATOR (27 Oct 2026)
# Formulas and factors read on 27 Oct 2026: Merck Veterinary Manual (RER, MER table, 30% variation),
# AAHA 2021 Box 1 PDF (life stage factors, 4.5 kg worked example), AAHA feeding plans page (90/10 rule, 4 to 7 day changes),
# WSAVA 2011 assessment guidelines (treats over 10% a risk factor, 30% variation), NRC 2006 owner booklet (energy table, meals).
def rer(kg):
    return 70 * kg ** 0.75

def feed_calc(page):
    lb_rows = "".join(
        "<tr><td>%d lb (%.1f kg)</td><td>%d</td><td>%d to %d</td><td>%d to %d</td><td>%d to %d</td></tr>" % (
            lb, lb * 0.45359237, round(rer(lb * 0.45359237)),
            round(rer(lb * 0.45359237) * 1.4), round(rer(lb * 0.45359237) * 1.6),
            round(rer(lb * 0.45359237) * 1.6), round(rer(lb * 0.45359237) * 1.8),
            round(rer(lb * 0.45359237) * 1.0), round(rer(lb * 0.45359237) * 1.2))
        for lb in (5, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100))
    kg_rows = "".join(
        "<tr><td>%d kg</td><td>%d</td><td>%d to %d</td><td>%d to %d</td><td>%d to %d</td></tr>" % (
            kg, round(rer(kg)), round(rer(kg) * 1.4), round(rer(kg) * 1.6), round(rer(kg) * 1.6), round(rer(kg) * 1.8),
            round(rer(kg) * 1.0), round(rer(kg) * 1.2))
        for kg in (2, 5, 8, 10, 15, 20, 25, 30, 35, 40, 50))
    ex10 = rer(10)
    body = """
<div class="tool"><h2 style="margin-top:0">Dog calorie and feeding calculator</h2>
<div class="row"><div><label for="fw">Weight</label><input id="fw" type="number" min="0.5" max="120" step="0.1" value="10" inputmode="decimal" style="width:6rem"></div>
<div><label for="fu">Unit</label><select id="fu"><option value="kg">kg</option><option value="lb">lb</option></select></div>
<div><label for="fs">Life stage</label><select id="fs">
<option value="1.4,1.6" selected>Neutered adult</option>
<option value="1.6,1.8">Intact adult (not neutered)</option>
<option value="1.0,1.2">Inactive or gains weight easily</option>
<option value="1.0,1.0">Weight loss (use the target weight your vet sets)</option>
<option value="3.0,3.0">Puppy under 4 months</option>
<option value="2.0,2.0">Puppy 4 months or older</option>
<option value="1.6,2.0">Working dog, light work</option>
</select></div></div>
<div class="row"><div><label for="fk">Food energy from the label (optional)</label><input id="fk" type="number" min="0" step="1" placeholder="e.g. 350" inputmode="numeric" style="width:7rem"></div>
<div><label for="fku">Per</label><select id="fku"><option value="cup">kcal per cup</option><option value="kg">kcal per kg</option><option value="can">kcal per can</option></select></div></div>
<p class="result" id="out" aria-live="polite"></p>
<p class="note">Method: resting energy requirement (RER) = 70 &times; (body weight in kg)<sup>0.75</sup>, multiplied by the canine life stage factor from the 2021 AAHA guidelines. Results are a starting point, not a prescription: individual dogs can need about 30 percent more or less.</p></div>
<section id="how"><h2>How the calculation works</h2>
<p>Vets estimate a dog's daily calories in two steps. The Merck Veterinary Manual and the 2021 AAHA Nutrition and Weight Management Guidelines both start from the <b>resting energy requirement (RER)</b>, the energy a healthy dog uses at rest in a comfortable temperature:</p>
<p style="font-size:1.15rem"><b>RER (kcal per day) = 70 &times; (body weight in kg)<sup>0.75</sup></b></p>
<p>Merck notes that this exponential formula works for dogs of any size. A simpler straight line version, 30 &times; weight in kg + 70, is only meant for dogs heavier than 2 kg and lighter than 45 kg, because energy needs do not rise in a straight line with body weight.</p>
<p>The second step multiplies RER by a <b>life stage factor</b> to get the <b>maintenance energy requirement (MER)</b>, the calories a dog needs each day to hold its weight with normal activity. AAHA's own worked example is a 10 lb (4.5 kg) neutered dog: RER is about 216 kcal, and 216 &times; 1.4 gives 302 kcal a day.</p>
<p>A kilocalorie (kcal) is the same unit as the capital C "Calorie" printed on food labels, as both the Merck Veterinary Manual and the National Research Council explain.</p></section>
<section id="factors"><h2>Life stage factors: AAHA and Merck compared</h2>
<p>The two references use slightly different multipliers. AAHA gives a range for each group; Merck gives a single number. Both call the result a starting point.</p>
<div class="tablewrap"><table><thead><tr><th>Dog</th><th>AAHA 2021 factor (&times; RER)</th><th>Merck Veterinary Manual factor (&times; RER)</th></tr></thead><tbody>
<tr><td>Neutered adult</td><td>1.4 to 1.6</td><td>1.6</td></tr>
<tr><td>Intact adult</td><td>1.6 to 1.8</td><td>1.8</td></tr>
<tr><td>Inactive or obesity prone</td><td>1.0 to 1.2</td><td>1.4</td></tr>
<tr><td>Weight loss</td><td>1.0</td><td>not listed</td></tr>
<tr><td>Puppy under 4 months</td><td>3.0</td><td>3</td></tr>
<tr><td>Puppy 4 months or older</td><td>2.0</td><td>2</td></tr>
<tr><td>Pregnant (last 21 days)</td><td>3.0</td><td>not listed</td></tr>
<tr><td>Nursing mother</td><td>3.0 to 6.0 or more, depending on litter size and week</td><td>not listed</td></tr>
<tr><td>Working dog</td><td>light 1.6 to 2.0, moderate 2.0 to 5.0, heavy 5.0 to 11.0</td><td>not listed</td></tr>
</tbody></table></div>
<p>AAHA adds that sedentary and indoor pets may need less than these factors suggest. Merck makes a similar point: dogs living in households often need fewer calories a day than dogs kept in kennels, and breed matters too (Newfoundlands appear to need fewer calories than Great Danes). Pregnant, nursing and hard working dogs vary so much that their feeding plan should come from your vet, which is why the calculator above leaves them out.</p></section>
<h2 id="chart">How much to feed a dog by weight: calorie chart</h2>
<p>Daily calories worked out with the RER formula and the AAHA adult factors, rounded to the nearest whole kcal. Use the weight your dog should be, not just the weight it is, if it is carrying extra fat.</p>
<div class="tablewrap"><table><thead><tr><th>Weight</th><th>RER (kcal per day)</th><th>Neutered adult (1.4 to 1.6)</th><th>Intact adult (1.6 to 1.8)</th><th>Inactive (1.0 to 1.2)</th></tr></thead><tbody>""" + lb_rows + """</tbody></table></div>
<h3 id="chart-kg">Dog feeding chart in kg</h3>
<div class="tablewrap"><table><thead><tr><th>Weight</th><th>RER (kcal per day)</th><th>Neutered adult</th><th>Intact adult</th><th>Inactive</th></tr></thead><tbody>""" + kg_rows + """</tbody></table></div>
<section id="nrc"><h2>A cross check with the National Research Council table</h2>
<p>The National Research Council (NRC) wrote the reference text <i>Nutrient Requirements of Dogs and Cats</i> (2006), and its free owner booklet <i>Your Dog's Nutritional Needs</i> gives average daily energy needs for adult dogs:</p>
<div class="tablewrap"><table><thead><tr><th>Type of dog</th><th>10 lb</th><th>30 lb</th><th>50 lb</th><th>70 lb</th><th>90 lb</th></tr></thead><tbody>
<tr><td>Inactive dogs</td><td>296</td><td>674</td><td>989</td><td>1,272</td><td>1,540</td></tr>
<tr><td>Adult active dogs</td><td>404</td><td>922</td><td>1,353</td><td>1,740</td><td>2,100</td></tr>
<tr><td>Young adult active dogs</td><td>436</td><td>993</td><td>1,451</td><td>1,876</td><td>2,264</td></tr>
<tr><td>Older active dogs</td><td>327</td><td>745</td><td>1,093</td><td>1,407</td><td>1,700</td></tr>
</tbody></table></div>
<p class="note">Figures in kcal per day, from the NRC booklet (2006).</p>
<p>We checked these numbers against the same weight to the power 0.75 scaling. Every figure in the inactive row is within 0.5 percent of 95 &times; kg<sup>0.75</sup>, and every figure in the active row is within 0.5 percent of 130 &times; kg<sup>0.75</sup>. In RER terms, that is about 1.36 &times; RER for inactive dogs and 1.86 &times; RER for active ones. So the NRC averages sit at the generous end: its inactive row is close to AAHA's neutered adult range rather than AAHA's 1.0 to 1.2 for inactive dogs, and its active row is just above the intact adult range. The experts agree on the method but not on one exact number, which is why every source says to treat the result as a starting point and adjust by body condition. The booklet describes active dogs as those with strong stimulus and ample chance to exercise, such as dogs in multi dog households, in the country or with a large yard.</p></section>
<section id="cups"><h2>Turning calories into cups or grams</h2>
<p>Calories only become useful once you know how much energy is in your dog's food. AAHA notes that AAFCO, the body behind US pet food rules, requires calorie content on dog food and treat labels (chews and bones are not included). If the packaging is not available, AAHA suggests the company's website or customer service line.</p>
<ol><li>Find the daily calories from the calculator or chart.</li>
<li>Find the food's calories per cup, can or kilogram on the label.</li>
<li>Divide. For example, if a dog needs 550 kcal and a food provides 350 kcal per cup, that is 550 &divide; 350 = about 1.6 cups a day. If the label gives 3,500 kcal per kg, the same dog needs 550 &divide; 3,500 &times; 1,000 = about 157 g a day. (These label values are made up for the example; use your own food's numbers.)</li>
<li>Split the total into meals. The NRC booklet says it is fine to feed an adult dog once or twice a day, while puppies need two to three meals a day.</li></ol>
<p>A kitchen scale is more accurate than a scoop, because cups of kibble vary. AAHA points out that pet food feeding guides are not standardized, so the amount on the bag is also only a starting point. Merck adds that if a dog needs much less food than the label suggests (10 to 30 percent less) to stay at an ideal weight, a less energy dense food may suit it better, because feeding a small amount of a standard food also cuts every other nutrient.</p></section>
<section id="treats" class="card"><h2>Treats: the 10 percent rule</h2>
<p>The AAHA guidelines say a complete and balanced food should supply at least 90 percent of a dog's calories, with treats, chews and other foods making up no more than 10 percent. The WSAVA nutritional assessment guidelines list snacks, treats and table food above 10 percent of total calories as a nutritional risk factor. The calculator shows this treat budget for you; if you use it, cut the main food by the same amount. For low calorie treat ideas, check our <a href="{R}can-dogs-eat.html">Can dogs eat this?</a> table.</p></section>
<section id="adjust"><h2>Check and adjust: why the number is only a start</h2>
<p>Dogs of the same weight can need very different amounts. Merck says any given dog may need as much as 30 percent more or fewer calories than another dog of the same weight, and the WSAVA guidelines give the same 30 percent figure in either direction for dogs. So:</p>
<ul><li><b>Weigh your dog regularly</b> on the same scale, and score its body condition. On the 9 point scale used by WSAVA, 4 to 5 is ideal; any score below 4 or above 5 is flagged as a risk factor. Our <a href="{R}blog/is-my-dog-overweight.html">body condition score guide</a> shows how to do it with your hands and eyes.</li>
<li><b>Adjust gradually.</b> If your dog is gaining, feed a little less; if it is losing weight it should not, feed a little more, and ask your vet if the change is unexplained.</li>
<li><b>Change foods slowly.</b> AAHA suggests moving to a new diet over 4 to 7 days, and WSAVA notes some dogs have fewer stomach upsets when food is changed over 7 to 10 days.</li>
<li><b>Ask about unusually low needs.</b> Merck advises checking for medical causes such as an underactive thyroid (hypothyroidism) when a dog needs surprisingly few calories to stay at its ideal weight.</li></ul>
<p>Keeping dogs lean pays off. In a 14 year study of 48 Labrador retrievers, dogs fed 25 percent less than their littermates lived a median of 13 years compared with 11.2 years (see <a href="{R}care.html#weight">healthy weight</a> and <a href="{R}health.html#weight">weight and health</a>).</p></section>
<section id="limits" class="card"><h2>When not to rely on a calculator</h2>
<p>This page is general information for healthy dogs, not veterinary advice. Ask your vet for a feeding plan if your dog is pregnant or nursing, a puppy of a large or giant breed, a working or sport dog, underweight or overweight, on a prescription or homemade diet, or has any medical condition such as kidney, liver, heart or digestive disease, diabetes or a thyroid problem. Sudden changes in appetite, thirst or weight are a reason to see your vet.</p></section>
"""
    script = """(function(){var w=document.getElementById('fw'),u=document.getElementById('fu'),s=document.getElementById('fs'),k=document.getElementById('fk'),ku=document.getElementById('fku'),o=document.getElementById('out');
function r(x){return Math.round(x)}
function amt(c){var e=+k.value||0;if(e<=0)return '';var lo=c[0]/e,hi=c[1]/e,t;
if(ku.value=='kg'){t=r(lo*1000)==r(hi*1000)?r(lo*1000)+' g':r(lo*1000)+' to '+r(hi*1000)+' g';return '<br>That is about <b>'+t+' of food a day</b> at '+e+' kcal per kg.'}
var n=ku.value=='cup'?'cups':'cans',f=function(x){return (Math.round(x*10)/10).toString()};t=f(lo)==f(hi)?f(lo):f(lo)+' to '+f(hi);
return '<br>That is about <b>'+t+' '+n+' a day</b> at '+e+' kcal per '+ku.value+'.'}
function calc(){var kg=(+w.value||0)*(u.value=='lb'?0.45359237:1);if(kg<0.5||kg>120){o.innerHTML='Enter a weight between 0.5 and 120 kg (about 1 to 265 lb).';return}
var f=s.value.split(',').map(Number),R=70*Math.pow(kg,0.75),c=[R*f[0],R*f[1]],d=r(c[0])==r(c[1])?r(c[0]):r(c[0])+' to '+r(c[1]);
o.innerHTML='Resting energy requirement: <b>'+r(R)+' kcal</b> a day.<br>Estimated daily need: <b>'+d+' kcal</b> a day.'+amt(c)+'<br>Treat budget (10 percent or less): about <b>'+r(c[1]*0.1)+' kcal</b>, taken out of the main food.'}
[w,u,s,k,ku].forEach(function(el){el.addEventListener('input',calc);el.addEventListener('change',calc)});calc()})();"""
    faq = [
        ("How much should I feed my dog a day?", "Work out its daily calories, then divide by the calories in its food. For a healthy neutered adult, vets start from 70 &times; (weight in kg)<sup>0.75</sup> and multiply by 1.4 to 1.6 (AAHA 2021). A 10 kg neutered dog needs roughly %d to %d kcal a day, adjusted up or down by how its weight and body condition change." % (round(ex10 * 1.4), round(ex10 * 1.6))),
        ("How many calories does a dog need per day by weight?", "Using the RER formula and AAHA factors, a neutered adult needs about %d to %d kcal at 5 kg, %d to %d kcal at 10 kg, %d to %d kcal at 20 kg and %d to %d kcal at 30 kg. Individual dogs can vary by about 30 percent either way." % (
            round(rer(5) * 1.4), round(rer(5) * 1.6), round(ex10 * 1.4), round(ex10 * 1.6), round(rer(20) * 1.4), round(rer(20) * 1.6), round(rer(30) * 1.4), round(rer(30) * 1.6))),
        ("What is RER for dogs?", "RER is the resting energy requirement, the calories a healthy dog uses at rest in a comfortable temperature. The Merck Veterinary Manual gives it as 70 &times; (body weight in kg)<sup>0.75</sup>, a formula that works for dogs of any size."),
        ("How many treats can I give my dog?", "Keep treats, chews and table food to 10 percent or less of daily calories, as the AAHA guidelines advise, and reduce the main food to match. WSAVA treats more than 10 percent from snacks as a nutritional risk factor."),
        ("Should I follow the feeding guide on the dog food bag?", "Use it as a starting point. AAHA notes feeding guides on pet food are not standardized, so check your dog's weight and body condition score every few weeks and adjust the amount."),
        ("How many times a day should I feed my dog?", "The National Research Council says once or twice a day is fine for adult dogs, while puppies need two to three meals a day."),
    ]
    page("how-much-to-feed-a-dog.html", "How Much to Feed a Dog: Calorie Calculator | SnoutsWise",
         "How much to feed a dog by weight: free calorie calculator and chart in kg and lb, using the RER formula with AAHA, Merck and NRC guidance, plus a treat budget.",
         body, h1="How much to feed a dog: calorie calculator and chart",
         lead="A healthy neutered adult dog needs roughly 70 &times; (its weight in kg)<sup>0.75</sup> &times; 1.4 to 1.6 kcal a day, the method used in the 2021 AAHA veterinary guidelines. That works out at about %d to %d kcal a day for a 10 kg (22 lb) dog. Enter your dog's weight below, add the calories from the food label to convert the result into cups or grams, then fine tune by watching weight and body condition." % (round(ex10 * 1.4), round(ex10 * 1.6)),
         faq=faq, sources=src("aaha_box1", "aaha_feed", "cline2021", "merck_nutr", "wsava_assess", "nrc_dog", "wsava_bcs", "penn_kealy"),
         related=[("blog/is-my-dog-overweight.html", "Is my dog overweight? Body condition score guide"), ("care.html#feeding", "Care: feeding basics"), ("health.html#weight", "Health: weight"), ("can-dogs-eat.html", "Can dogs eat this? food table"), ("dog-age-calculator.html", "Dog age calculator"), ("blog/how-do-dogs-drink-water.html", "How dogs drink water")],
         crumbs=[("index.html", "Home"), ("care.html", "Care"), ("how-much-to-feed-a-dog.html", "How much to feed a dog")], script=script,
         published="2026-10-27", updated="2026-10-27")

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
        ("How much should I feed my dog?", "Start from its daily calories: vets use 70 &times; (weight in kg)<sup>0.75</sup>, multiplied by a life stage factor such as 1.4 to 1.6 for a neutered adult (AAHA 2021), then divide by the calories in the food. Adjust by weight and body condition. Try the <a href=\"{R}how-much-to-feed-a-dog.html\">feeding calculator</a>."),
        ("How do I know if my dog is overweight?", "Use a body condition score: at an ideal weight you can feel the ribs without excess fat and see a waist from above. <a href=\"{R}blog/is-my-dog-overweight.html\">Step by step guide</a>."),
        ("Why does my dog eat grass?", "Usually because it is normal dog behavior. In a 2008 survey of 1,571 plant eating dogs, 68% ate plants daily or weekly, only 9% often seemed ill beforehand and only 22% often vomited afterwards. See a vet if it suddenly increases or comes with vomiting, diarrhea or lethargy. <a href=\"{R}blog/why-do-dogs-eat-grass.html\">What the research says</a>."),
        ("Can dogs see color?", "Yes, mostly blues and yellows. Dogs have two types of cone cells instead of the three most people have, so their color vision is similar to a person with red green color blindness. <a href=\"{R}blog/can-dogs-see-color.html\">How dogs see color</a>."),
        ("Why do dogs tilt their heads?", "Often when they hear a word that means something to them. In a 2021 study of 40 dogs, dogs that knew toy names tilted on 43% of fetch requests versus 2% for typical dogs. A tilt that stays, or comes with stumbling or flicking eyes, needs a vet. <a href=\"{R}blog/why-do-dogs-tilt-their-heads.html\">What the research found</a>."),
        ("Do dogs dream?", "Dogs have clear REM sleep with rapid eye movements and low muscle tone, which is why they twitch in naps. Dream content is unproven. Sleep after learning new commands can improve performance. <a href=\"{R}blog/do-dogs-dream.html\">What REM research shows</a>."),
        ("Do dogs feel jealousy?", "They show jealousy-like behaviour: more pushing, getting between and sometimes snapping when owners pet a rival dog than a toy or book. Human-style conscious jealousy is still debated. <a href=\"{R}blog/do-dogs-feel-jealousy.html\">What experiments show</a>."),
        ("Why do dogs yawn?", "Often from tiredness, but yawning is also a stress signal when it comes with lip licking or a lowered body. Some dogs catch human yawns: 21 of 29 dogs did in a 2008 study, more from owners than strangers in a 2013 study. <a href=\"{R}blog/why-do-dogs-yawn.html\">What the studies found</a>."),
        ("Do dogs understand pointing?", "Most dogs do. A 2021 study of 375 eight-week-old puppies found they followed human gestures well with no sign of needing to learn it, and over 40% of the variation was genetic. Hand-raised wolves do worse. <a href=\"{R}blog/do-dogs-understand-pointing.html\">What the studies show</a>."),
        ("Why do dogs wag their tails?", "Mainly to communicate. A wag shows a dog is aroused or engaged, and research links it with both positive and negative states, so a wagging dog is not always a friendly one. Dogs also tend to wag more to the right for their owner and more to the left for an unfamiliar dominant dog. <a href=\"{R}blog/why-do-dogs-wag-their-tails.html\">What the research shows</a>."),
        ("How do dogs drink water?", "By lapping. A dog curls its tongue backward, dips it in and pulls it up very fast, which lifts a column of water that the dog bites off before it falls. The backward curl helps the dog drink more per lap, and also explains the splashing. <a href=\"{R}blog/how-do-dogs-drink-water.html\">The physics of lapping</a>."),
        ("How old is my dog in human years?", "By the 2020 epigenetic clock formula, human age is about 16 &times; ln(dog age) + 31, so a 1 year old dog is about 31 and a 10 year old about 68. Try the <a href=\"{R}dog-age-calculator.html\">dog age calculator</a>."),
        ("How often should I brush my dog's teeth?", "The AVMA says daily brushing is best, but several times a week can be effective, alongside a dental check by your vet at least once a year."),
        ("Does my dog legally need a microchip?", "In the UK, yes: all dogs must be microchipped and registered by 8 weeks old, and must wear a collar and tag with the owner's name and address in public. Other countries have their own rules."),
        ("What should I do if my dog has heatstroke?", "Cool first, transport second, says the RSPCA: stop activity, move to shade, pour water cooler than the dog over its body (not the head), fan it, then go to a vet in a cool car. Do not cover the dog with wet towels."),
    ]
    page("faq.html", "Dog Questions and Answers: Quick Sourced FAQ | SnoutsWise",
         "Dog questions and answers with sources: how much to feed, normal temperature, tail wagging, yawning, dreaming, eating grass, color vision, vaccines and heat.",
         '<p>Each answer links to a fuller page with the sources.</p>', h1="Dog FAQ",
         lead="Quick answers to the questions dog owners ask most, drawn from veterinary and welfare sources such as the Merck Veterinary Manual, AAHA, AVSAB, AVMA, the ASPCA and the RSPCA.",
         faq=qs, sources=src("merck_vitals", "aspca_foods", "merck_choc", "aaha_table", "avsab_puppy", "avsab_train", "wsava_bcs", "aaha_box1", "sueda2008", "neitz1989", "sommese2022", "kis2014", "kis2017", "harris2014", "abdai2018", "joly2008", "romero2013", "wang2020", "avma_dental", "gov_chip", "rspca_heat"),
         related=[("health.html", "Health basics"), ("care.html", "Everyday care"), ("training.html", "Training"), ("behavior.html", "Behavior"), ("blog/why-do-dogs-yawn.html", "Why do dogs yawn?"), ("blog/do-dogs-feel-jealousy.html", "Do dogs feel jealousy?"), ("glossary.html", "Glossary")],
         crumbs=[("index.html", "Home"), ("faq.html", "FAQ")], updated="2026-10-27")

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
    page("glossary.html", "Dog Glossary: Plain English Dog & Vet Terms | SnoutsWise",
         "Plain English definitions of dog care, health, training and breed terms: core vaccine, body condition score, brachycephalic, methylxanthines and more.",
         body, h1="Dog glossary",
         lead="Short, plain English definitions of terms you will meet on vet visits, in training classes and on kennel club sites, each linked to the page that explains it in more depth.",
         sources=src("aaha_table", "avsab_train", "rspca_heat", "avma_dental", "merck_choc", "wsava_bcs", "rkc_groups"),
         related=[("faq.html", "Dog FAQ"), ("breeds.html", "Breed groups"), ("health.html", "Health basics"), ("training.html", "Training")],
         crumbs=[("index.html", "Home"), ("glossary.html", "Glossary")])

# ------------------------------------------------------------------ TRUST PAGES
def trust(page):
    page("about.html", "About SnoutsWise: Who We Are & How We Write | SnoutsWise",
         "Who runs SnoutsWise, what it covers, how the content is researched and sourced, and how to report a correction.",
         """
<h2>Who runs this site</h2>
<p>SnoutsWise is an independent publication. It is not affiliated with any kennel club, veterinary organization, pet food company or retailer named on the site.</p>
<h2>What we cover</h2>
<p>Practical, plain English information for dog owners: <a href="{R}breeds.html">breed groups</a>, <a href="{R}care.html">everyday care</a>, <a href="{R}health.html">health basics</a>, <a href="{R}training.html">training</a> and <a href="{R}behavior.html">behavior</a>, plus tools such as the <a href="{R}can-dogs-eat.html">Can dogs eat this?</a> table and the <a href="{R}dog-age-calculator.html">dog age calculator</a>.</p>
<h2>How content is produced</h2>
<ul><li>Pages are researched and written by the SnoutsWise editorial team with the help of AI tools, then checked against primary and authoritative sources such as the Merck Veterinary Manual, the American Animal Hospital Association, the American Veterinary Society of Animal Behavior, the American Veterinary Medical Association, the ASPCA, the RSPCA, the American Kennel Club, The Royal Kennel Club, university veterinary schools and peer reviewed studies.</li>
<li>Every page lists its sources, and facts and figures are attributed to the organization that published them. We do not invent statistics, quotes, experts or personal experiences.</li>
<li>We are not veterinarians, and nothing here replaces an examination by a vet who knows your dog. Health and safety pages say so and point to emergency help.</li>
<li>Each page shows when it was last updated. We review pages when guidelines change.</li></ul>
<h2>Money</h2>
<p>The site is free to read. It may show advertising through Google AdSense. It carries no sponsored content or affiliate links, and ads never change what we write. Details are in our <a href="{R}disclaimer.html">disclaimer</a> and in our <a href="{R}privacy.html">privacy policy</a>. See also our <a href="{R}terms.html">terms of use</a>.</p>
<h2>Corrections</h2>
<p>Spotted an error or an outdated guideline? Please email <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a> or use the <a href="{R}contact.html">contact form</a> with the page and the source, and we will check and correct it.</p>
""", h1="About SnoutsWise", kind="webpage",
         lead="SnoutsWise is a free, independent reference for dog owners. We turn veterinary and kennel club guidance into clear, practical pages and show the sources behind every claim.",
         crumbs=[("index.html", "Home"), ("about.html", "About")])

    page("contact.html", "Contact SnoutsWise | SnoutsWise",
         "Contact SnoutsWise by email or form with questions, corrections or suggestions.",
         """
<p>Email us at <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>, or send a message with the form below. We read every message, although we cannot always reply individually.</p>
<p class="note" style="font-style:normal"><b>We cannot give veterinary advice for individual dogs.</b> If your dog is unwell, injured or may have eaten something toxic, contact your vet or an emergency vet now.</p>
<form class="card" action="https://formsubmit.co/joshuaofisrael@gmail.com" method="POST">
<input type="hidden" name="_subject" value="[Contact: SnoutsWise]">
<input type="hidden" name="_template" value="table">
<input type="hidden" name="_captcha" value="false">
<input type="hidden" name="_next" value="SITE_URL_PLACEHOLDERcontact-thanks.html">
<input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
<label for="name">Name</label><input id="name" name="name" type="text" required autocomplete="name">
<label for="email">Email</label><input id="email" name="email" type="email" required autocomplete="email">
<label for="topic">Topic</label><select id="topic" name="topic"><option>Question</option><option>Correction</option><option>Suggestion</option><option>Other</option></select>
<label for="message">Message</label><textarea id="message" name="message" rows="6" required></textarea>
<p class="note">We use your name, email and message only to read and answer your note and to improve the site. We do not sell them or add you to any list. Messages are delivered by FormSubmit to our inbox. See our <a href="{R}privacy.html">privacy policy</a>.</p>
<button class="btn" type="submit">Send message</button>
</form>
""", h1="Contact us", kind="webpage",
         lead="Questions, corrections and suggestions are welcome. The quickest way to reach SnoutsWise is email: joshuaofisrael@gmail.com.",
         crumbs=[("index.html", "Home"), ("contact.html", "Contact")])

    page("contact-thanks.html", "Message sent | SnoutsWise", "Thank you for contacting SnoutsWise.",
         '<p>Thank you, your message has been sent. If it needs a reply, we will answer by email.</p><p><a class="btn" href="{R}index.html">Back to the home page</a></p>',
         h1="Thanks for your message", kind="webpage", index=False, nav="contact.html")

    page("privacy.html", "Privacy Policy | SnoutsWise",
         "How Joshua Israel Ventures LLC handles data on SnoutsWise: hosting logs, Google Fonts, the contact form, cookieless Cloudflare Web Analytics, opt in Google Analytics 4, and Google AdSense advertising and cookies.",
         """
<p class="meta">Last updated 28 October 2026</p>
<p class="op">&copy; 2026 Joshua Israel Ventures LLC. All rights reserved. SnoutsWise is a trade name of Joshua Israel Ventures LLC, a Florida limited liability company.</p>
<h2>Who we are</h2><p>SnoutsWise is a brand of Joshua Israel Ventures LLC. Joshua Israel Ventures LLC owns and operates snoutswise.com and is the data controller for personal information collected through it ("we", "us"). Contact: <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>.</p>
<h2>What we collect today</h2>
<ul><li><b>Hosting server logs.</b> The site is hosted on GitHub Pages, run by GitHub, Inc. When you visit, GitHub's servers may automatically log technical information such as your IP address, browser type, the page requested and the time, for security and to keep the service running. We do not receive these logs. See <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">GitHub's privacy statement</a>.</li>
<li><b>Fonts.</b> Pages load the Fredoka and Nunito fonts from Google Fonts (fonts.googleapis.com and fonts.gstatic.com). To deliver them, your browser connects to Google's servers, which receive your IP address and browser information. See <a href="https://developers.google.com/fonts/faq/privacy" rel="noopener">Google Fonts privacy information</a> and <a href="https://policies.google.com/privacy" rel="noopener">Google's privacy policy</a>.</li>
<li><b>Contact form.</b> If you use the <a href="{R}contact.html">contact form</a>, your name, email address, chosen topic and message are sent through FormSubmit (formsubmit.co) to our email inbox, which is a Gmail account provided by Google. We use them only to read and reply to your message.</li>
<li><b>Email.</b> If you email us directly, we receive your email address and whatever you include in the message.</li></ul>
<h2>Analytics</h2><p>We use Cloudflare Web Analytics to count visits and see which pages are popular. It is cookieless: it sets no cookies, does not use local storage, and does not fingerprint visitors or track them across sites. Cloudflare processes basic request data such as the page URL, referrer, browser type and approximate country to produce aggregate statistics. See <a href="https://www.cloudflare.com/privacypolicy/">Cloudflare's privacy policy</a>.</p><h2 id="analytics">Google Analytics 4 (only if you accept)</h2><p>We also use Google Analytics 4, a service of Google LLC, to understand how visitors use SnoutsWise so we can improve it. Google Analytics does not load until you click <b>Accept</b> in our analytics banner. If you click <b>Decline</b>, or make no choice, it is not loaded and sets no cookies.</p><p><b>What it collects.</b> Usage data such as the pages you view, time on page, how you arrived (for example a search engine or a link) and clicks on the site, plus device data such as browser, operating system, screen size, language and approximate location (city or country) derived from your IP address. Google Analytics 4 does not log or store IP addresses. We see this only as aggregate reports, we do not use it to identify you, and we do not use it for advertising.</p><p><b>Cookies.</b> If you accept, Google Analytics sets first party cookies named <code>_ga</code> and <code>_ga_GRC8LBNEX4</code>, which last up to two years and let it tell repeat visits apart. Your choice itself is stored in your browser's local storage as <code>mtm-analytics-consent</code>.</p><p><b>Consent.</b> We use Google Consent Mode. For visitors in the European Economic Area, the UK and Switzerland, analytics and advertising storage start as denied by default, and Google's consent message described below controls advertising choices. For every visitor, analytics storage stays denied until you accept our banner. You can change your mind at any time with the <a href="{R}privacy.html#analytics" data-consent-open>Cookie settings</a> link at the bottom of every page, which shows the banner again; choosing Decline then removes the Google Analytics cookies.</p><p><b>Opt out.</b> You can also block Google Analytics on every website with the <a href="https://tools.google.com/dlpage/gaoptout" rel="noopener">Google Analytics opt out browser add on</a>. See <a href="https://policies.google.com/privacy" rel="noopener">Google's privacy policy</a> and <a href="https://policies.google.com/technologies/partner-sites" rel="noopener">how Google uses information from sites that use its services</a>.</p><h2>Advertising</h2><p>Joshua Israel Ventures LLC may show ads on SnoutsWise through Google AdSense. Google and its partners use cookies and similar technologies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies lets it and its partners show ads to you based on your visit to this site and other sites on the internet. To learn how Google uses data when you use our site, and how to opt out of personalized advertising, see <a href="https://policies.google.com/technologies/ads" rel="noopener">How Google uses information from sites or apps that use our services</a>. You can also opt out of many third party advertising cookies at <a href="https://www.aboutads.info/choices" rel="noopener">aboutads.info/choices</a>.</p>
<p><b>California residents (CCPA).</b> You can opt out of the sale or sharing of your personal information for advertising through the Google and aboutads.info links above, and by emailing us. We do not otherwise sell personal information.</p>
<p><b>Visitors in the EU, UK and Switzerland.</b> Google shows you a consent choice about cookies and personalized ads. You can accept, decline or change your choice there, and ads will respect it. Our own analytics banner covers Google Analytics only.</p>
<h2>What we do not use</h2><p>The site has no user accounts and sets no cookies of its own, apart from the Google Analytics cookies described above if you accept them. Apart from Google AdSense, described above, it uses no advertising networks, and it has no affiliate links or affiliate cookies. If we add any, we will update this policy before they go live.</p>
<h2>How we use and share information</h2><p>We use contact form messages and emails only to respond to you and to improve or correct the site. We do not sell personal information. Advertising through Google AdSense is described in the Advertising section above. The service providers named above (GitHub, Cloudflare, Google and FormSubmit) process data on our behalf or as part of delivering their services, under their own privacy terms.</p>
<h2>How long we keep it</h2><p>We keep messages only as long as needed to deal with them and then delete them. Email us at any time to ask us to delete your message.</p>
<h2>Third party links</h2><p>Pages link to outside sources such as veterinary manuals and kennel clubs. Their own privacy policies apply when you visit them.</p>
<h2>Children</h2><p>The site is general information for a general audience and does not knowingly collect personal information from children under 13.</p>
<h2>Your rights</h2><p>Depending on where you live, you may have rights to access, correct or delete personal data we hold about you, or to object to how we use it. Email <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a> and we will respond.</p>
<h2>Games</h2><p>Our <a href="{R}games/">games</a> save your best score in your own browser (localStorage) so you can try to beat it. It stays on your device, is never sent to us, and contains no personal information. Clear your browser's site data to remove it.</p>
<h2>Photos</h2><p>Photos on the site are stored on our own pages (self hosted), so viewing them does not contact any other service. See <a href="{R}credits/">photo credits</a>.</p>
<h2>Changes and governing law</h2><p>We will post any changes on this page with a new date. This policy forms part of our <a href="{R}terms.html">terms of use</a>, which are governed by the laws of the State of Florida.</p>
""", h1="Privacy policy", kind="webpage",
         related=[("terms.html", "Terms of use"), ("disclaimer.html", "Disclaimer"), ("contact.html", "Contact us")],
         crumbs=[("index.html", "Home"), ("privacy.html", "Privacy")])

    page("terms.html", "Terms of Use | SnoutsWise",
         "Terms of use for SnoutsWise, owned and operated by Joshua Israel Ventures LLC: general information only, no warranties, limitation of liability, Florida law.",
         """
<p class="meta">Last updated 27 October 2026</p>
<p class="op">&copy; 2026 Joshua Israel Ventures LLC. All rights reserved. SnoutsWise is a trade name of Joshua Israel Ventures LLC, a Florida limited liability company.</p>
<h2>Who you are dealing with</h2><p>These terms of use govern your use of snoutswise.com (the "site"). The site is owned and operated by Joshua Israel Ventures LLC ("we", "us", "our"), which is the contracting party for everything on the site. SnoutsWise is a brand owned by Joshua Israel Ventures LLC; it is not a separate company. By using the site you agree to these terms. If you do not agree, please do not use the site.</p>
<h2>General information only, not professional advice</h2><p>Everything on the site, including articles, the food table, the dog age calculator, the feeding calculator and the chocolate dose estimator, is general educational information about dogs. It is not veterinary, medical or other professional advice, and it is not a substitute for an examination by a vet who knows your dog. Using the site does not create a veterinarian, client and patient relationship or any other professional relationship. If your dog may be ill, injured or poisoned, contact your vet or an emergency vet straight away. See our <a href="{R}disclaimer.html">disclaimer</a>.</p>
<h2>Our content</h2><p>The text, illustrations, design, and the SnoutsWise name and logo are owned by Joshua Israel Ventures LLC unless stated otherwise. You are welcome to link to any page and to quote short passages with a credit and a link back. Please do not republish substantial parts of the site without our written permission.</p>
<h2>Using the site</h2><p>Do not use the site for any unlawful purpose or try to disrupt it or the services that host it.</p>
<h2>Links to other sites</h2><p>We link to outside sources so you can check our facts. We do not control those sites and are not responsible for their content, availability or privacy practices.</p>
<h2>No warranties</h2><p>The site and all its content are provided "as is" and "as available". To the fullest extent permitted by law, Joshua Israel Ventures LLC disclaims all warranties, express or implied, including warranties of accuracy, completeness, merchantability, fitness for a particular purpose and non-infringement. We do not promise that the site will be error free, up to date or always available.</p>
<h2>Limitation of liability</h2><p>To the fullest extent permitted by law, Joshua Israel Ventures LLC and its members, managers and contributors will not be liable for any indirect, incidental, special, consequential or punitive damages, or for any loss or harm (including harm to any animal) arising from your use of, or reliance on, the site or its content. Our total liability for any claim relating to the site is limited to one hundred US dollars (US$100). Some jurisdictions do not allow certain limits on liability, so some of these limits may not apply to you.</p>
<h2>Governing law</h2><p>These terms are governed by the laws of the State of Florida, United States, without regard to its conflict of law rules. Any dispute will be resolved in the state or federal courts located in Florida.</p>
<h2>Changes to these terms</h2><p>We may update these terms from time to time. The date at the top shows the latest version, and continuing to use the site means you accept the updated terms.</p>
<h2>Contact</h2><p>Questions about these terms: <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>.</p>
""", h1="Terms of use", kind="webpage",
         related=[("privacy.html", "Privacy policy"), ("disclaimer.html", "Disclaimer"), ("about.html", "About SnoutsWise")],
         crumbs=[("index.html", "Home"), ("terms.html", "Terms")])

    page("disclaimer.html", "Disclaimer | SnoutsWise",
         "SnoutsWise disclaimer: general information only, no vet relationship, what to do in an emergency, and our advertising and affiliate disclosure.",
         """
<p class="meta">Last updated 27 October 2026</p>
<p class="call"><b>Emergency? Call your vet, an emergency vet, or the ASPCA Animal Poison Control Center: <a href="tel:+18884264435">(888) 426-4435</a></b>. Outside the US, call your vet or local emergency vet.</p>
<h2>Accuracy</h2><p>We research every page and link the veterinary, welfare and kennel club sources it relies on, and we review pages when guidance changes. Even so, information can be incomplete, out of date or wrong, guidelines differ between organizations and countries, and every dog is different. Joshua Israel Ventures LLC makes no guarantee that the content is accurate, complete or suitable for your dog. Please check the linked sources and ask your vet before acting on anything you read here. If you spot an error, <a href="{R}contact.html">tell us</a>.</p>
<h2>No vet or professional relationship</h2><p>We are not veterinarians. Reading the site, using its tools or contacting us does not create a veterinarian, client and patient relationship or any other professional relationship. Do not delay getting veterinary care, or ignore advice from your vet, because of something you read on SnoutsWise. For behavior problems such as aggression, ask your vet or a qualified veterinary behaviorist.</p>
<h2>Tools and calculators</h2><p>The food table, dog age calculator, feeding calculator and chocolate dose estimator give general estimates for information only. They cannot account for your dog's health, the exact product eaten or other factors a vet would consider.</p>
<h2>Affiliate and advertising disclosure</h2><p>SnoutsWise may show advertising served by Google AdSense, which is labelled as advertising and is separate from our content. We have no affiliate links or sponsored content, and we are not paid to mention any product, organization or website. If that changes, we will add a clear disclosure, as required by the US Federal Trade Commission, on the affected pages and update this page and our <a href="{R}privacy.html">privacy policy</a>.</p>
<p class="op">&copy; 2026 Joshua Israel Ventures LLC. All rights reserved. SnoutsWise is a trade name of Joshua Israel Ventures LLC, a Florida limited liability company.</p>
<h2>Who is responsible</h2><p>SnoutsWise is a brand of Joshua Israel Ventures LLC, which owns and operates the site. Use of the site is also governed by our <a href="{R}terms.html">terms of use</a>, under the laws of the State of Florida. Contact: <a href="mailto:joshuaofisrael@gmail.com">joshuaofisrael@gmail.com</a>.</p>
""", h1="Disclaimer", kind="webpage",
         related=[("terms.html", "Terms of use"), ("privacy.html", "Privacy policy"), ("health.html", "Dog health basics")],
         crumbs=[("index.html", "Home"), ("disclaimer.html", "Disclaimer")])

    page("404.html", "Page Not Found | SnoutsWise", "That page could not be found.",
         '<p>We could not find that page. Try the <a href="{R}index.html">home page</a>, the <a href="{R}can-dogs-eat.html">Can dogs eat this?</a> table or the <a href="{R}faq.html">dog FAQ</a>.</p>',
         h1="This page wandered off", kind="webpage", index=False, abs_links=True, nav="")

# ------------------------------------------------------------------ BLOG
POSTS = []

def post(page, slug_, title, desc, h1, lead, body, faq=None, sources=None, related=None, script="", published="2026-10-08"):
    POSTS.append((slug_, h1, desc, published))
    page("blog/%s.html" % slug_, title, desc, body, h1=h1, lead=lead, kind="post", faq=faq, sources=sources,
         related=related, script=script, published=published, updated=published, crumbs=[("index.html", "Home"), ("blog/index.html", "Blog"), ("blog/%s.html" % slug_, h1)])

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
    post(page, "dog-ate-chocolate", "My Dog Ate Chocolate: How Much Is Dangerous? | SnoutsWise",
         "Dog ate chocolate? Estimate the theobromine dose from chocolate type and your dog's weight with Merck Veterinary Manual figures, plus warning signs.",
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
    post(page, "puppy-socialization-window", "Puppy Socialization Window: When It Closes | SnoutsWise",
         "The puppy socialization window is the first three months. When classes can start before vaccines finish, plus a safe week by week checklist.",
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
    post(page, "dog-vaccine-schedule", "Dog Vaccines: How Often? Core vs Non Core | SnoutsWise",
         "Do dogs need yearly vaccines? What AAHA guidelines say about core vaccines (distemper, parvo, adenovirus, lepto, rabies), puppy shots and boosters.",
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
    post(page, "alpha-dog-myth", "Is the Alpha Dog Idea True? What Research Says | SnoutsWise",
         "Do you need to be the alpha? Where the dominance idea came from, what L. David Mech's wolf research found and why vet behaviorists reject it.",
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
    post(page, "is-my-dog-overweight", "Is My Dog Overweight? Body Condition Score Guide | SnoutsWise",
         "Is your dog overweight? Use the WSAVA 9 point body condition score at home: ribs, waist and tuck explained, plus why lean dogs lived longer.",
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
<li><b>Measure food.</b> Weigh or measure every meal rather than estimating, and feed for the target weight your vet suggests rather than the current weight. Our <a href="{R}how-much-to-feed-a-dog.html">dog calorie calculator</a> shows how vets estimate daily calories.</li>
<li><b>Count treats.</b> Treats, chews and table scraps add up. Use part of the daily food allowance as training treats, or low calorie options such as green beans or carrot pieces (see the <a href="{R}can-dogs-eat.html">Can dogs eat this?</a> table).</li>
<li><b>Add activity gradually</b>, especially for older or very overweight dogs: longer sniffy walks, gentle play and food puzzle toys.</li>
<li><b>Re-score every couple of weeks</b> and weigh regularly on the same scale.</li></ol>
<p>Never put a dog on a crash diet; sudden severe restriction can be harmful, so let your vet guide the plan.</p>
""",
         faq=[("What is the ideal body condition score for a dog?", "On the 9 point scale used on the WSAVA chart, 4 to 5 is ideal: ribs easy to feel without excess fat, a visible waist from above and a tucked belly from the side."),
              ("Can I tell if my dog is overweight just by weighing it?", "Not reliably on its own, because healthy weight varies between individual dogs. A body condition score, done with your hands and eyes, tells you how much fat your dog carries. Use both, and ask your vet for a target weight."),
              ("Do lean dogs live longer?", "In a 14 year study of 48 Labrador retrievers, dogs fed 25 percent less than their littermates lived a median of 13 years versus 11.2 years and developed osteoarthritis later.")],
         sources=src("wsava_bcs", "penn_kealy"),
         related=[("how-much-to-feed-a-dog.html", "How much to feed a dog"), ("care.html#weight", "Care: healthy weight"), ("health.html#weight", "Health: weight"), ("can-dogs-eat.html", "Low calorie treat ideas"), ("dog-age-calculator.html", "Dog age calculator")])

    # 6 daily fact: color vision (8 Oct 2026)
    post(page, "can-dogs-see-color", "Can Dogs See Color? Yes, Mostly Blues and Yellows | SnoutsWise",
         "Can dogs see color? Yes. Dogs have two cone types and see mainly blues and yellows, like red green color blind people. What it means for toys.",
         "Can dogs see color? Yes, mostly blues and yellows",
         "Yes. Dogs do not see the world in black and white. Their eyes have two types of color sensing cone cells instead of the three most people have, so they see mainly blues and yellows, much like a person with red green color blindness. Reds, oranges and greens are hard for them to tell apart, which is why a yellow or blue ball is easier for a dog to spot on grass than a red one.",
         """
<h2>Where the black and white myth came from</h2>
<p>The American Kennel Club traces the idea that dogs see only black and gray to Will Judy, a dog writer and publisher, who wrote in his 1937 manual <i>Training the Dog</i> that the outside world probably appears to dogs as "varying highlights of black and gray". The AKC notes there was little research to back the claim, but it stuck for decades.</p>
<h2>What the research found</h2>
<p>In 1989, Jay Neitz, Timothy Geist and Gerald Jacobs tested the color vision of three dogs in a series of behavioral experiments, published in <i>Visual Neuroscience</i>. Their results showed that the dog retina contains two classes of cone pigment, with peak sensitivities at about 429 nanometers (short, bluish wavelengths) and about 555 nanometers (longer wavelengths). They concluded that dogs have dichromatic color vision: real color vision, but built on two cone types rather than three. The AKC summarizes the practical result: a dog's color vision is similar to that of a person with red green color blindness, so dogs can make out yellow and blue and combinations of them, while a green lawn or a red cushion looks more like a dull brownish gray.</p>
<h2>Do dogs actually use color?</h2>
<p>For a long time scientists assumed color mattered little to dogs. A 2013 study in <i>Proceedings of the Royal Society B</i> by Anna Kasparson and colleagues tested that. Eight untrained dogs, working outdoors in daylight, learned to pick a paper card that differed from the other card in both color and brightness, for example dark yellow versus light blue, to find food. In test trials the researchers swapped the brightness, offering light yellow versus dark blue. The dogs kept choosing by color rather than by brightness, and half of them chose by color in all ten tests. The authors concluded that in normal daylight, color can be the main visual cue even for animals with only two cone types.</p>
<h2>What dogs see better than we do</h2>
<p>A 1995 review of canine vision in the <i>Journal of the American Veterinary Medical Association</i> by Paul Miller and Christopher Murphy found that dogs fall short of people in color perception, sharpness of vision, focusing range and the overlap between the two eyes. But dogs probably beat us at seeing in dim light, telling apart shades of gray, noticing how fast an image changes (flicker), and width of view, and perhaps at detecting motion. The AKC's chief veterinary officer, Dr. Jerry Klein, explains that dogs have more rods, the light sensitive cells used in low light, plus a reflective layer behind the retina called the tapetum that boosts night vision.</p>
<h2>What it means for you and your dog</h2>
<ul><li><b>Pick blue or yellow toys</b> for fetch on grass. The AKC points out that red and orange, the most popular toy colors, are hard for dogs to pick out against a green lawn.</li>
<li><b>Use blue and yellow to teach "which one".</b> If you are teaching your dog to tell two toys apart, the AKC suggests making one blue and one yellow.</li>
<li><b>Do not blame stubbornness</b> if your dog runs straight past a red ball. It may simply be hard to see.</li></ul>
""",
         faq=[("Are dogs color blind?", "Not completely. Dogs have two types of cone cells and see color mostly in blues and yellows. Their vision is often compared to a person with red green color blindness."),
              ("What colors can dogs see best?", "Blue and yellow. Reds, oranges and greens tend to look similar to a dog, closer to brownish or grayish tones."),
              ("Can dogs see better in the dark than people?", "Probably yes. A 1995 review in the Journal of the American Veterinary Medical Association concluded that dogs likely function better than people in dim light, helped by more rod cells and a reflective tapetum behind the retina.")],
         sources=src("neitz1989", "kasparson2013", "miller1995", "akc_color"),
         related=[("behavior.html", "Dog behavior"), ("training.html", "Reward based training"), ("care.html", "Everyday care"), ("blog/puppy-socialization-window.html", "Puppy socialization window")],
         published="2026-10-08")

    # 7 daily fact: grass eating (11 Oct 2026)
    post(page, "why-do-dogs-eat-grass", "Why Do Dogs Eat Grass? What Studies Found | SnoutsWise",
         "Why do dogs eat grass? A study of 1,571 dogs found 68% ate plants daily or weekly and most were not sick first. What it means and when to call a vet.",
         "Why do dogs eat grass? Usually because it is normal",
         "Most dogs eat grass simply because it is normal dog behavior, not because they are sick. In the largest study so far, a survey of 1,571 owners of plant eating dogs published in <i>Applied Animal Behaviour Science</i> in 2008, 68% of the dogs ate plants daily or weekly, only 9% often seemed unwell beforehand and only 22% often vomited afterwards. Researchers think the habit may be inherited from wild ancestors, since wolves eat grass too. A dog that suddenly eats grass frantically, vomits repeatedly or seems unwell should still see a vet.",
         """
<h2>What the biggest study found</h2>
<p>Researchers at the University of California, Davis, School of Veterinary Medicine, Karen Sueda, Benjamin Hart and Kelly Cliff, set out to test the common explanations for grass eating. They ran three surveys. In a pilot survey of 25 veterinary students who had dogs, every student said their dog ate grass. In a survey of 47 owners of healthy dogs visiting a teaching hospital whose dogs had daily access to plants, 79% said their dog had eaten grass or other plants. Then an internet survey gathered 3,340 replies, of which 1,571 met the study's criteria.</p>
<p>In that large group:</p>
<ul><li><b>68%</b> of dogs ate plants daily or weekly; the rest did so once a month or less.</li>
<li><b>Grass</b> was the plant most often eaten for 79% of dogs, and 98% of owners said their dog ate grass at least sometimes. Other plants included berries, sticks and leaves.</li>
<li><b>92%</b> of owners said their dog rarely showed signs of illness before or after eating plants.</li>
<li><b>78%</b> said their dog rarely vomited afterwards. Only 22% reported frequent vomiting.</li>
<li><b>Younger dogs</b> ate plants more often than older dogs, and were less likely to look ill before or vomit after.</li>
<li>Sex, neutering status, breed group and type of diet showed no link with how often dogs ate plants.</li></ul>
<p>The authors concluded that plant eating, and grass eating in particular, appears to be a normal behavior of domestic dogs across all breed groups.</p>
<h2>Do dogs eat grass because they feel sick?</h2>
<p>Sometimes, but not usually. The study found that dogs that did look ill before eating plants were more likely to vomit afterwards than dogs that looked fine. The authors suggest stomach or gut discomfort may sometimes trigger plant eating, and that grass may irritate the stomach enough to cause vomiting. But that was the minority pattern. Most dogs looked normal before and kept the grass down.</p>
<h2>Is it a sign of a missing nutrient?</h2>
<p>The evidence so far says probably not. In the large survey, the type of diet (commercial, home cooked or raw) made no difference to how often dogs ate plants. In the clinic survey, none of the dogs that did not eat plants were given extra vegetables or fruit, while 10 of the 37 plant eaters were, which suggests that adding plant food to the diet does not stop the habit. The authors called this a provisional conclusion and said a detailed study of specific nutrients, such as fiber, vitamins or minerals, is still needed.</p>
<h2>Why would dogs have this habit at all?</h2>
<p>Dogs share it with their wild relatives. A study of gray wolves in Yellowstone National Park, published in <i>The Journal of Nutrition</i> in 2006 by Daniel Stahler, Douglas Smith and Debra Guernsey, found that summer scat samples showed a more varied diet than winter kills, including vegetation; the Davis team notes that plant matter turned up in roughly 74% of those summer samples. Some grass gets swallowed by accident with prey, but deliberate grass eating by wolves has also been recorded.</p>
<p>One idea is that grass helps flush out intestinal worms. The naturalist Adolph Murie reported in 1944 that he saw blades of grass wrapped around worms in wolf droppings. Sueda and colleagues point out that young canids tend to carry more intestinal parasites, and young dogs eat grass most often, which fits this idea. It is still a hypothesis: nobody has yet shown in controlled studies that grass eating reduces worms in pet dogs.</p>
<p>Cats show a similar pattern. A 2021 study in <i>Animals</i> by Benjamin Hart and colleagues, based on two surveys of cat owners, found that very few cats looked ill before eating plants, and concluded that plant eating in cats, as in dogs, mostly reflects normal behavior.</p>
<h2>When grass eating is a reason to call the vet</h2>
<p>Occasional grazing in a healthy dog is common. Talk to your vet if you notice any of these:</p>
<ul><li>A sudden change: your dog starts eating grass much more often, or frantically.</li>
<li>Repeated vomiting, diarrhea, blood in vomit or stool, a poor appetite, weight loss or tiredness (see our <a href="{R}health.html#emergency">signs that need a vet</a>).</li>
<li>Grass eating together with constant licking of floors, carpets or walls. In a 2012 study in the <i>Journal of Veterinary Behavior</i>, Bécuwe-Bonnet and colleagues examined 19 dogs that licked surfaces excessively and found gastrointestinal problems in 14 of them, including gut inflammation, delayed stomach emptying, chronic pancreatitis and giardia. After treatment, the licking improved significantly in 10 of 17 dogs followed up. Odd eating and licking habits can be a sign of a hidden stomach problem rather than just a behavior quirk.</li></ul>
<h2>How to keep grass eating safe</h2>
<ul><li><b>Know your plants.</b> Grass is not the only thing dogs nibble. Check garden and house plants against the ASPCA's list of toxic and non toxic plants, and see our <a href="{R}care.html#home">common hazards at home</a>.</li>
<li><b>Avoid treated lawns.</b> Keep your dog off grass that has just been sprayed or fertilized, and follow the product label on when pets can go back on it.</li>
<li><b>Stay on top of parasite control.</b> Ask your vet what worming and parasite prevention suits your dog's age and lifestyle.</li>
<li><b>Do not punish it.</b> For a healthy dog, grazing is normal behavior. If you would rather it stopped, redirect with a reward based cue such as "leave it" (see <a href="{R}training.html">reward based training</a>).</li></ul>
""",
         faq=[("Is it OK for my dog to eat grass?", "For most healthy dogs, yes. A 2008 study of 1,571 plant eating dogs found grass eating is common and usually not linked to illness. Keep your dog off lawns treated with chemicals and away from toxic plants, and see a vet if the habit suddenly increases or comes with vomiting, diarrhea or lethargy."),
              ("Do dogs eat grass to make themselves sick?", "Usually not. In the 2008 survey only 22% of owners said their dog frequently vomited after eating plants, and only 9% said their dog often seemed ill beforehand."),
              ("Does eating grass mean my dog is missing something in its diet?", "There is no good evidence for that. In the 2008 study, diet type made no difference to how often dogs ate plants, although the authors said specific nutrients such as fiber have not yet been studied in detail."),
              ("Why do puppies eat more grass than older dogs?", "Younger dogs ate plants more often in the 2008 study. One idea is that grass eating evolved to help expel intestinal worms, which are more common in young canids, but this has not been proven in pet dogs."),
              ("When should I worry about my dog eating grass?", "Call your vet if your dog suddenly eats grass frantically or much more often, vomits repeatedly, has diarrhea, stops eating, loses weight or also licks floors and surfaces excessively, which a 2012 study linked to gastrointestinal disease.")],
         sources=src("sueda2008", "stahler2006", "hart2021", "becuwe2012", "aspca_plants"),
         related=[("health.html", "Dog health basics"), ("behavior.html", "Dog behavior"), ("care.html", "Everyday care"), ("can-dogs-eat.html", "Can my dog eat this?"), ("blog/can-dogs-see-color.html", "Can dogs see color?")],
         published="2026-10-11")

    # 8 daily fact: head tilting (12 Oct 2026)
    post(page, "why-do-dogs-tilt-their-heads", "Why Do Dogs Tilt Their Heads? The Research | SnoutsWise",
         "Why do dogs tilt their heads? In a 2021 study, dogs that knew toy names tilted on 43% of requests vs 2% for other dogs. Plus when a tilt needs a vet.",
         "Why do dogs tilt their heads? It may mean they are listening hard",
         "Dogs often tilt their heads when they hear a word that means something to them. In a 2021 study of 40 dogs in <i>Animal Cognition</i>, dogs that had learned the names of their toys tilted their heads on 43% of requests to fetch a toy, compared with just 2% for typical dogs given the same training. The researchers think the tilt may be linked to paying close attention to meaningful speech, and each dog tended to tilt to the same side every time. A tilt that does not go away, or comes with stumbling, circling or flicking eyes, is different: that can be a balance (vestibular) problem and needs a vet.",
         """
<h2>The first study of head tilting in dogs</h2>
<p>Head tilting is one of the most familiar dog behaviors, yet until recently no study had described it. A team at the Department of Ethology at Eötvös Loránd University in Budapest, led by Andrea Sommese and Claudia Fugazza, filmed 40 dogs during tests in which owners asked their dog to fetch a particular toy by name, for example "bring rope!". The toys were in another room, so the dog had to rely on the word alone.</p>
<p>The dogs fell into two groups. Seven were "gifted word learners", rare dogs that pick up the names of toys quickly. The other 33 were typical family dogs that loved toys. All of them went through the same three month training program to learn the names of two new toys, with the same weekly coaching for their owners.</p>
<p>What the researchers found:</p>
<ul><li><b>43% vs 2%.</b> Across the monthly tests, the gifted word learners tilted their heads on 43% of trials. The typical dogs tilted on only 2%.</li>
<li><b>Familiar is not enough.</b> The typical dogs had heard the toy names just as often over three months, so simply knowing the sound of a word did not trigger tilting. The authors suggest the tilt is linked to hearing a word that is meaningful to the dog, and may be a sign of increased attention.</li>
<li><b>Each dog has a side.</b> A dog's tilt direction stayed consistent across tests months apart, so the authors treat it as a stable individual trait, a bit like paw preference.</li>
<li><b>It is not about where the sound comes from.</b> Whether the owner stood to the left, right or in front made no difference to the direction of the tilt.</li></ul>
<p>The study was small and exploratory. All six gifted dogs that took part in the later tests were Border collies, but so were 18 of the typical dogs that rarely tilted, so the authors warn against linking frequent tilting to that breed.</p>
<h2>How rare are dogs that learn words?</h2>
<p>Very rare. In a companion study in <i>Scientific Reports</i>, the same team gave 34 ordinary family dogs (puppies and adults, all keen on toys) three months of intensive play based training to learn two toy names. Only one of them passed the tests. The six already "word knowledgeable" dogs, found after a two year search around the world, all passed and went on to learn between 2 and 13 new toy names a month. Most dogs respond to tone of voice, routines and gestures rather than to the names of objects, and that is completely normal (see our guide to <a href="{R}behavior.html">dog behavior</a>).</p>
<h2>Do dogs process speech on one side of the brain?</h2>
<p>There are clues that they might. In a 2014 study in <i>Current Biology</i>, Victoria Ratcliffe and David Reby at the University of Sussex played dogs recordings of a familiar command from speakers on both sides and noted which way each dog turned its head. Dogs turned one way when the meaningful sounds of the words were made more noticeable, and the other way when the tone of voice and speaker cues were boosted. Because each side of the head is wired mainly to the opposite side of the brain, the authors concluded that dogs may, like people, handle the words and the emotional tone of speech in different brain hemispheres. Head turning is not the same movement as head tilting, but the Budapest team cites this work as one reason to think the side a dog tilts to could reflect how its brain processes speech. That link has not been proven yet.</p>
<h2>Other ideas you may have heard</h2>
<p>You will often read that dogs tilt their heads to see past their muzzle or to work out where a sound is coming from. These are reasonable guesses, but we have not found published studies that test them, so treat them as unproven. The one thing the 2021 study did check, the owner's position, made no difference to the direction of the tilt.</p>
<h2>When a head tilt is a reason to call the vet</h2>
<p>A quick, curious tilt when you talk to your dog is normal. A tilt that stays there is not. A constant head tilt is a classic sign of a problem with the vestibular system, the inner ear and brain parts that control balance. A 2023 review in <i>Frontiers in Veterinary Science</i> describes idiopathic vestibular syndrome, a common cause in dogs over nine, as usually starting suddenly with a head tilt toward the affected side, abnormal eye movements, a wobbly, unbalanced walk and sometimes nausea or vomiting. Many dogs improve within days and recover within two to four weeks, but a slight tilt can remain. Vets only diagnose it after ruling out other causes such as middle or inner ear infection, stroke, inflammation of the brain, injury and tumors.</p>
<p>Contact your vet promptly if your dog has any of these:</p>
<ul><li>A head tilt that does not go away when you stop talking.</li>
<li>Stumbling, leaning, falling or circling to one side.</li>
<li>Eyes flicking side to side or up and down on their own.</li>
<li>Head shaking, scratching at an ear, ear odor or discharge.</li>
<li>Vomiting, drooling, a drooping face or seeming dull or confused (see our <a href="{R}health.html#emergency">signs that need a vet</a>).</li></ul>
<h2>Fun ways to use your dog's head tilt</h2>
<ul><li><b>Notice what triggers it.</b> If your dog tilts for "walk", "ball" or a favorite toy's name, it may be telling you which words matter to it most.</li>
<li><b>Teach a toy name the kind way.</b> Short, playful sessions where you name a toy while you play with it are how word learning dogs picked up names. Do not worry if your dog never learns any; most do not (see <a href="{R}training.html">reward based training</a>).</li>
<li><b>Reward calm attention.</b> A tilt means your dog is focused on you, which is a great moment for a treat and praise.</li></ul>
""",
         faq=[("Why do dogs tilt their heads when you talk to them?", "Probably because they are paying close attention to words that mean something to them. In a 2021 study of 40 dogs, dogs that knew the names of their toys tilted their heads on 43% of requests to fetch a toy, compared with 2% for typical dogs."),
              ("Do smarter dogs tilt their heads more?", "In the one study so far, dogs that were unusually good at learning toy names tilted much more often. That suggests a link with processing meaningful words, but it does not mean a dog that never tilts is less intelligent."),
              ("Why does my dog always tilt its head to the same side?", "That is normal. The 2021 study found each dog's tilt direction stayed the same across tests months apart, so researchers treat it as a stable individual trait, like paw preference."),
              ("Can all dogs learn the names of toys?", "Very few can. In a 2021 study, only 1 of 34 typical family dogs learned two toy names after three months of training, while a handful of rare gifted dogs learned many."),
              ("When is a head tilt a sign of a health problem?", "When it stays even when nothing is going on, or comes with stumbling, circling, falling, flicking eyes, head shaking or vomiting. These can be signs of vestibular (balance) disease or an inner ear problem, so contact your vet.")],
         sources=src("sommese2022", "fugazza2021", "ratcliffe2014", "mertens2023"),
         related=[("behavior.html", "Dog behavior"), ("training.html", "Reward based training"), ("blog/why-do-dogs-make-puppy-dog-eyes.html", "Why do dogs make puppy dog eyes?"), ("blog/can-dogs-learn-toy-names.html", "Can dogs learn toy names?"), ("health.html", "Dog health basics"), ("blog/can-dogs-see-color.html", "Can dogs see color?"), ("blog/why-do-dogs-eat-grass.html", "Why do dogs eat grass?")],
         published="2026-10-12")


    # 9 daily fact: do dogs dream / REM sleep (13 Oct 2026)
    post(page, "do-dogs-dream", "Do Dogs Dream? What REM Sleep Research Shows | SnoutsWise",
         "Do dogs dream? They have clear REM sleep with rapid eye movements. Sleep also helps them remember new commands. What science can and cannot say.",
         "Do dogs dream? They have REM sleep, but dreams are still unproven",
         "Dogs have the same basic sleep stages people do, including REM sleep with rapid eye movements and relaxed muscles. That is why paws, whiskers and soft barks during a nap look so much like dreaming. Scientists can measure that REM state with brain and muscle sensors, but they cannot ask a dog what it experiences, so human-style dreaming is still an open question. What is solid: after dogs learn new commands, their sleep brain waves change, and their performance often improves after a nap or a night's sleep.",
         """
<h2>What scientists can measure in a sleeping dog</h2>
<p>In 2014, a Budapest team led by Anna Kis published a fully non-invasive way to record sleep in family dogs while their owners sat nearby. They used soft scalp electrodes (EEG), eye movement sensors (EOG), muscle tone (EMG), breathing and heart rate, the same kind of polysomnography used in people. Twenty-two adult pet dogs and twelve adult humans each took a three hour afternoon nap.</p>
<p>The dog recordings showed the same main stages people have:</p>
<ul><li><b>Drowsiness</b>: lighter sleep with faster brain waves and some muscle tone.</li>
<li><b>Slow wave sleep (SWS / Non-REM)</b>: deeper sleep with large, slow delta waves and lower muscle tone.</li>
<li><b>REM sleep</b>: rapid eye movements, fast brain activity, muscular atonia (very low muscle tone), and irregular breathing and heartbeat.</li></ul>
<p>Sleep was polyphasic: dogs switched between stages often. In that three hour session, average sleep efficiency was about 43% (time asleep out of the recording), with wide individual differences. Mean REM time was about 16.5 minutes and mean SWS about 21.6 minutes, though some dogs had little or no REM or SWS in that afternoon nap. Dogs' age also showed up in the EEG: older dogs had less relative delta power and more alpha and beta power in SWS and REM, a pattern familiar from human aging research.</p>
<h2>So are those twitches dreams?</h2>
<p>During REM, many dogs twitch their legs, whiskers or ears, or make quiet sounds. That fits what the sensors show: the body is mostly paralyzed (atonia) while the brain and eyes are active, so small movements can break through. A 2020 review by Robert Bodizs and colleagues notes that dogs meet the behavioral and polygraphic criteria for both Non-REM and REM sleep, including facial or leg twitches in REM.</p>
<p>None of that proves a dog is "seeing" a dream story the way people report dreams. Proving that would need a way to link brain patterns to an experience the animal can report. Reviews of mammal dreaming make the same point: REM is necessary for the kind of vivid dreaming people describe, but it is not the same as proof that a dog has one. The honest answer today is that dogs have REM sleep that looks a lot like ours, and the twitching is consistent with an active brain during that stage, while the content of any dog dream remains unknown.</p>
<h2>How much do dogs sleep, and in what pattern?</h2>
<p>Comparative sleep databases often list about 10.1 hours of average daily sleep for domestic dogs, with published estimates ranging from roughly 7.7 to 16 hours. Dogs are mainly diurnal: most inactivity falls between about 21:00 and 06:00, with a rest period in the afternoon. Their sleep cycles are short. Reviews describe ultradian cycles of about 20 minutes (roughly 12 minutes of drowsiness or Non-REM plus about 6 minutes of REM), compared with about 90 minutes in adult humans. Sleep is also polyphasic, with brief wake-sleep cycles through the day and night.</p>
<p>That short cycle pattern may help dogs adapt to changing human schedules. Bodizs and colleagues note that dogs can cope with shift work better than people often do, partly because their natural brief cycles let them catch rest in pieces.</p>
<h2>Sleep helps dogs remember new commands</h2>
<p>In 2017, Kis and colleagues taught 15 dogs to link unfamiliar spoken words to the already known actions "sit" and "lie down", then recorded three hours of sleep. Compared with a matched non-learning session, post-learning Non-REM sleep showed more delta power and less alpha power, and REM sleep showed more delta power. After the nap, performance on the new commands rose compared with the pre-sleep baseline. Dogs whose REM sleep had less delta and more beta power improved more.</p>
<p>A second experiment with 53 dogs looked at what happened in the hour after learning. Dogs that slept, walked on leash, or played all showed better long-term performance a week later. Dogs that learned an unrelated new task in that hour did not improve a week later, which suggests interfering learning can block consolidation. Play briefly hurt immediate retest scores (likely attention or arousal), but those dogs still improved after a night at home. A one hour sleep bout alone was not enough to raise immediate scores the way the three hour nap had, which matches human work showing longer sleep often helps more.</p>
<p>So when you teach a new cue, give your dog a quiet rest afterward and avoid piling on a second hard lesson in the same hour (see <a href="{R}training.html">reward based training</a>).</p>
<h2>When sleep problems need a vet</h2>
<p>Ordinary twitching in REM is normal. Violent thrashing, howling, growling or biting during sleep can be REM sleep behavior disorder, in which the usual muscle paralysis fails. Brachycephalic breeds (such as English bulldogs) are prone to sleep disordered breathing with snoring and daytime sleepiness. Narcolepsy, often linked to orexin pathway problems, causes sudden sleep attacks and emotion triggered loss of muscle tone. Contact your vet if sleep looks unsafe or daytime alertness collapses (see <a href="{R}health.html#emergency">signs that need a vet</a>).</p>
<h2>Practical takeaways for owners</h2>
<ul><li><b>Let sleeping dogs lie.</b> Soft twitches and quiet sounds in a nap are usually REM, not a reason to wake them.</li>
<li><b>Protect rest after training.</b> A nap or quiet evening helps new cues stick; stacking unrelated lessons right after can interfere.</li>
<li><b>Match the schedule.</b> Dogs already prefer night sleep and an afternoon rest. Sudden all night disturbance is harder on them than short daytime interruptions.</li>
<li><b>Watch for red flags.</b> Violent dream-like acting out, loud breathing pauses, or sudden collapses during play need veterinary advice.</li></ul>
""",
         faq=[("Do dogs dream when they twitch in their sleep?", "Twitching during REM sleep is common and fits an active brain with mostly paralyzed muscles. That looks like dreaming from the outside, but scientists cannot confirm what a dog experiences. What is measured is REM sleep, not dream content."),
              ("Do dogs have the same sleep stages as people?", "Yes in outline. Non-invasive recordings show drowsiness, slow wave (Non-REM) sleep and REM sleep with rapid eye movements and low muscle tone, similar to human polysomnography."),
              ("How much sleep does a dog need?", "Comparative databases often cite about 10 hours a day on average, with published estimates from about 8 to 16 hours. Dogs sleep in short cycles and often nap by day as well as at night."),
              ("Does sleep help dogs learn?", "Yes. After dogs learned new command words, their sleep EEG changed and performance improved after a three hour nap. A second study found that sleep, a quiet walk or play all allowed long-term gains a week later, while learning an unrelated task in the same hour blocked that improvement."),
              ("When should I worry about my dog's sleep?", "If your dog violently acts out dreams, snores with pauses and is exhausted by day, or collapses into sleep during excitement, contact your vet. Soft REM twitches alone are usually normal.")],
         sources=src("kis2014", "kis2017", "bodizs2020"),
         related=[("behavior.html", "Dog behavior"), ("training.html", "Reward based training"), ("health.html", "Dog health basics"), ("blog/why-do-dogs-tilt-their-heads.html", "Why do dogs tilt their heads?"), ("blog/why-do-dogs-eat-grass.html", "Why do dogs eat grass?")],
         published="2026-10-13")


    # 10 daily fact: do dogs feel jealousy (14 Oct 2026)
    post(page, "do-dogs-feel-jealousy", "Do Dogs Feel Jealousy? What Experiments Show | SnoutsWise",
         "Do dogs feel jealousy? Experiments show more pushy, between-owner behaviour when owners pet a rival dog than a toy or book. What science can and cannot say.",
         "Do dogs feel jealousy? They show jealousy-like behaviour in experiments",
         "When owners pet what looks like another dog, pet dogs often push in, try to get between them, and sometimes snap more than when the owner pets a nonsocial object or reads a book. That pattern matches a simple form of jealousy seen in human infants: protect a valued bond from an interloper. Follow-up work with real dogs as rivals found the same kind of owner-oriented interrupting. Scientists still debate whether dogs have a conscious jealous feeling the way people do, and some studies with fake rivals found weaker or unclear results.",
         """
<h2>The first lab-style test of dog jealousy</h2>
<p>In 2014, Christine Harris and Caroline Prouvost at UC San Diego adapted a method used with six-month-old human babies. They tested 36 small pet dogs at home. Owners ignored their own dog while they affectionately petted and talked to one of three things, in counterbalanced order:</p>
<ul><li><b>A stuffed dog</b> that could bark, whine and wag its tail for a few seconds when a button was pressed (the jealousy condition).</li>
<li><b>A novel jack-o-lantern pail</b> treated the same way (affection to a nonsocial object).</li>
<li><b>A children's pop-up book</b> read aloud (loss of attention without an interloper).</li></ul>
<p>Coders scored behaviours that owners and infant studies link to jealousy: pushing or touching the owner or object, getting between them, attention toward the owner, and aggression such as snapping.</p>
<p>Dogs showed significantly more of those behaviours toward the stuffed dog than toward the jack-o-lantern or the book. About one quarter snapped at the stuffed dog during the interaction, versus only one dog in each of the other conditions. After the owner set the object down, 36% snapped at the stuffed dog. Dogs also pushed or touched the owner and the object more in the stuffed-dog condition, and tried to get between owner and object more often. Whining was higher than in the book condition. Barking did not differ clearly across conditions.</p>
<p>Attention rose when the owner showed affection: dogs looked more at the owner and at the object in the affection conditions than while the owner read. They looked even more at the stuffed dog than at the jack-o-lantern. Most dogs treated the toy as dog-like: 86% sniffed its anal region during or after the trial, the same kind of social investigation dogs use with other dogs.</p>
<h2>What about a real dog rival?</h2>
<p>Critics argued a stuffed dog that barks and wags on cue might startle dogs or invite territorial reactions at home, rather than jealousy. In 2018, Judit Abdai and colleagues at Eotvos Lorand University tested dogs from multi-dog households with real partners: a familiar housemate dog and an unfamiliar dog as social rivals, plus familiar and unfamiliar nonsocial objects. Owners focused attention on each partner in turn.</p>
<p>Dogs showed more owner-oriented behaviour and more attempts to interrupt the owner-partner interaction when the partner was another dog than when it was an object. Interrupt attempts differed across conditions (Friedman test on 22 dogs, p &lt; 0.001), with more interruptions for social than nonsocial partners. The authors conclude the pattern fits a functional description of jealous behaviour: it appears when a valued relationship is threatened by a social third party, not merely when attention is lost.</p>
<h2>Why some studies still urge caution</h2>
<p>Also in 2018, Emanuela Prato-Previde and colleagues ran two studies (36 dogs each) with a book, a puppet and a fake dog (furry in Study 1, plastic in Study 2), handled by the owner or a stranger. Dogs often sniffed the fake dog's ano-genital area, but aggressive biting never occurred, and many classic jealousy markers were absent or rare. Differences between the fake dog and the puppet were clearer only in Study 2. Dogs paid similar attention when a stranger handled the fake dog as when the owner did, which is not the pattern expected if jealousy is only about protecting the bond with the owner.</p>
<p>Their conclusion is careful: they do not rule out a rudimentary form of jealousy, but they argue fake rivals are a weak test and that future work should use real social interlopers and more naturalistic setups. That is why Abdai's real-dog design matters, and why the honest answer for owners is "jealousy-like behaviour, yes; full human-style jealousy, not proven."</p>
<h2>What this means for owners</h2>
<ul><li><b>Expect pushiness when you pet another dog.</b> Getting between you and a guest dog is common in these studies. Manage with a lead, distance or a short "go to mat" cue rather than scolding (see <a href="{R}training.html">reward based training</a>).</li>
<li><b>Rule out fear and pain first.</b> Sudden snapping when you touch another animal can also be fear or redirected aggression. Check for stress signals such as lip licking, a tucked tail or a stiff body (<a href="{R}behavior.html#stress">reading stress</a>), and see a vet if behaviour changes suddenly.</li>
<li><b>Do not use dominance labels.</b> Jealousy-like interrupting is about protecting access to you, not becoming "alpha". AVSAB advises against alpha rolls and dominance explanations (<a href="{R}blog/alpha-dog-myth.html">the alpha dog myth</a>).</li>
<li><b>Train calm sharing.</b> Reward your dog for staying on a mat while you greet another dog or person, then release them for a turn. Short, successful rehearsals beat forcing them to "get over it".</li></ul>
""",
         faq=[("Do dogs feel jealousy like people do?", "Dogs show jealousy-like behaviour: more pushing, getting between and sometimes snapping when owners affectionately attend to a rival dog or stuffed dog than to a nonsocial object or a book. Whether they have a conscious jealous feeling like adults do is still debated."),
              ("What did the first jealousy experiment find?", "Harris and Prouvost (2014) tested 36 small dogs at home. Dogs snapped, pushed and tried to get between more when owners petted a stuffed dog than a jack-o-lantern or while reading a book. About 86% sniffed the stuffed dog's rear, suggesting they treated it as dog-like."),
              ("Does a real dog rival change the result?", "Yes. Abdai and colleagues (2018) used familiar and unfamiliar real dogs plus objects. Dogs interrupted and oriented to the owner more for dog partners than for objects, which fits jealousy as protecting a social bond."),
              ("Why do some scientists still doubt it?", "Prato-Previde and colleagues (2018) found that fake dogs often failed to trigger clear jealousy markers, and dogs reacted similarly when a stranger handled the fake dog. They urge using real social interlopers before claiming human-like jealousy."),
              ("How should I handle a jealous dog?", "Manage space, reward calm alternatives such as going to a mat, and avoid dominance punishments. If snapping or fear is escalating, contact your vet or a certified behaviour professional (see <a href=\"{R}behavior.html#help\">when to get help</a>).")],
         sources=src("harris2014", "abdai2018", "prato2018"),
         related=[("behavior.html", "Dog behavior"), ("training.html", "Reward based training"), ("blog/alpha-dog-myth.html", "Is the alpha dog idea true?"), ("blog/do-dogs-dream.html", "Do dogs dream?"), ("blog/why-do-dogs-tilt-their-heads.html", "Why do dogs tilt their heads?")],
         published="2026-10-14")


    # 11 daily fact: why do dogs yawn (15 Oct 2026)
    post(page, "why-do-dogs-yawn", "Why Do Dogs Yawn? Stress or Contagion | SnoutsWise",
         "Why do dogs yawn? Often from tiredness or stress, and some dogs catch human yawns, more from owners than strangers. What the studies found.",
         "Why do dogs yawn? Sometimes stress, sometimes they catch yours",
         "Dogs yawn when they are sleepy, but yawning is also one of the stress signals vets and behaviour researchers watch for, alongside lip licking and a lowered body. Several experiments also suggest that some dogs catch human yawns: in the first study, 21 of 29 dogs yawned after watching a person yawn, and none did after a fake mouth movement. Later studies found the effect is stronger with the owner than a stranger and only shows up after about 7 months of age, though one video study found almost no contagion at all.",
         """
<h2>Yawning as a stress signal</h2>
<p>A yawn on its own does not mean your dog is unhappy. Context matters. The American Veterinary Society of Animal Behavior lists yawning among the behaviours researchers recorded as stress related during training, together with lip licking, a lowered body or tail, lifting a front paw and panting (see <a href="{R}behavior.html#stress">reading stress and fear</a>). A yawn at the vet, during a tense greeting or while being told off is more likely to be a stress yawn than one at bedtime.</p>
<h2>Do dogs catch human yawns?</h2>
<p>In 2008, Ramiro Joly-Mascheroni, Atsushi Senju and Alex Shepherd at Birkbeck, University of London, had a person sit in front of each of 29 dogs and either yawn or make similar mouth movements without yawning. 21 of the 29 dogs yawned after watching the yawn, and none yawned after the control mouth movements. The authors suggested this might reflect a rudimentary form of empathy, and that because yawning changes arousal, catching yawns could help dogs and people coordinate.</p>
<p>The result has not always repeated. In 2009, Aimee Harr and colleagues showed 15 dogs videos of humans and dogs yawning or simply opening their mouths. Only one dog yawned significantly more to the yawning videos, mostly to the human ones. Watching a screen may be a weaker test than a live person, but it is a reminder that the effect is not universal.</p>
<h2>Owners are more contagious than strangers</h2>
<p>In 2013, Teresa Romero, Akitsugu Konno and Toshikazu Hasegawa at the University of Tokyo tested 25 dogs with live yawns from their owner and from an unfamiliar experimenter. Dogs yawned more in the yawning condition than the control, and more when the owner yawned than the stranger. Heart rate, measured in 21 of the dogs, did not differ between conditions, which the authors read as evidence that these yawns were not a stress response.</p>
<p>The same year, Elainie Madsen and Tomas Persson at Lund University tested 35 puppies aged 4 to 14 months. The puppies yawned contagiously, but only dogs older than about 7 months showed it, and in their study a familiar person was not more contagious than an unfamiliar one. They link the age effect to a developmental increase in attention to others, similar to how yawn contagion rises in young children.</p>
<h2>What this means for owners</h2>
<ul><li><b>Read yawns in context.</b> Sleepy yawns at night are normal. Repeated yawning with lip licking, a tucked tail or turning away in a tense moment is your cue to give space or end the session.</li>
<li><b>Training sessions:</b> if your dog starts yawning a lot, make the task easier and keep sessions short (see <a href="{R}training.html">reward based training</a>).</li>
<li><b>Do not read too much into catching yawns.</b> A dog that yawns back may be tuned in to you, but a dog that does not is not less attached. The studies disagree on how strong and how social the effect is.</li>
<li><b>See your vet</b> if yawning suddenly increases with other changes such as drooling, pawing at the mouth or lethargy, since mouth pain or illness can change behaviour.</li></ul>
""",
         faq=[("Why does my dog yawn so much?", "Often because they are tired or settling down, but yawning is also one of the stress signals AVSAB lists alongside lip licking, a lowered body and panting. Look at the situation: repeated yawns in a tense moment usually mean your dog needs a break."),
              ("Can dogs catch yawns from people?", "Some can. In a 2008 study, 21 of 29 dogs yawned after watching a person yawn and none after fake mouth movements. A 2009 video study found only 1 of 15 dogs showed clear contagion, so the effect varies."),
              ("Do dogs yawn more when their owner yawns?", "In a 2013 study of 25 dogs, dogs yawned more when their owner yawned than when a stranger did, and their heart rate did not rise, suggesting the yawns were not stress. A puppy study the same year did not find an owner effect."),
              ("Do puppies catch yawns?", "Madsen and Persson (2013) tested 35 dogs aged 4 to 14 months and found contagious yawning only in dogs older than about 7 months."),
              ("Is yawning a sign my dog is stressed?", "It can be, especially with other signals such as lip licking, a tucked tail or lifting a paw. A single yawn at bedtime is just tiredness. See <a href=\"{R}behavior.html#stress\">reading stress</a>.")],
         sources=src("joly2008", "harr2009", "romero2013", "madsen2013", "avsab_train"),
         related=[("behavior.html", "Dog behavior"), ("training.html", "Reward based training"), ("blog/do-dogs-feel-jealousy.html", "Do dogs feel jealousy?"), ("blog/do-dogs-dream.html", "Do dogs dream?"), ("blog/why-do-dogs-tilt-their-heads.html", "Why do dogs tilt their heads?")],
         published="2026-10-15")


    # news 15 Oct 2026: big dogs age faster (Science, Dog Aging Project)
    post(page, "big-dogs-age-faster-dna-study", "Why Big Dogs Age Faster: New DNA Study in Science | SnoutsWise",
         "News: a Dog Aging Project study in Science finds large dogs show faster DNA aging, with the biggest changes in jumping genes. What it means for owners.",
         "News: big dogs show faster DNA aging, a Science study finds",
         "A study of 894 pet dogs in the Dog Aging Project, published in Science on 8 October 2026, found that larger dogs, males and younger dogs carry DNA methylation patterns that look older than their age, and that dogs whose epigenetic age ran ahead of their real age had a higher risk of death. The biggest size difference was in transposable elements, sometimes called jumping genes: large dogs lost methylation there 31% faster with age than small dogs. Whether this causes faster aging or is a side effect is still unknown.",
         """
<h2>What the researchers did</h2>
<p>The team, led by Blaise Mariner and senior author Noah Snyder-Mackler at Arizona State University, analysed 1,640 blood DNA methylation profiles from 894 companion dogs in the Dog Aging Project, a large US study of pet dogs. Methylation marks are small chemical tags on DNA that shift in predictable ways with age, so they can be used as a molecular clock. Using dogs with known birthdates, the team built an age predictor that, according to the paper's summary, explained 86% of the variation in age with a median error of under a year (0.82 years).</p>
<h2>What they found</h2>
<ul><li><b>Older than expected meant higher risk.</b> Dogs whose epigenetic age was higher than their real age had higher mortality risk, which suggests the clock tracks real biological ageing rather than just birthdays.</li>
<li><b>Size, sex and youth mattered.</b> Larger dogs, males and younger dogs showed patterns consistent with faster epigenetic ageing.</li>
<li><b>Jumping genes were the hotspot for size.</b> Most of the genome's transposable elements lost methylation with age, and that loss was 31% stronger in larger dogs, including in a class called LINE1s. Methylation normally helps keep these elements quiet.</li></ul>
<p>In ASU's news release, Mariner called it one of the clearest molecular signatures yet that lines up with the known trade-off between body size and lifespan in dogs. The release also notes that more research is needed to tell whether LINE1 activity is a cause or a consequence of ageing.</p>
<h2>What it means for owners</h2>
<ul><li><b>Nothing to change today.</b> This is basic research. There is no test or treatment from it you can buy, and it does not mean any individual large dog will be unhealthy.</li>
<li><b>Big dogs do tend to be "older" sooner.</b> That fits the long-known pattern that giant and large breeds have shorter average lifespans, which is why vets often suggest earlier senior check-ups for big breeds. Ask your vet when your dog should start them.</li>
<li><b>Weight still matters.</b> Keeping any dog lean is one of the few proven ways to add healthy years (see <a href="{R}blog/is-my-dog-overweight.html">is my dog overweight?</a>).</li>
<li><b>Curious about "dog years"?</b> Our <a href="{R}dog-age-calculator.html">dog age calculator</a> uses an earlier, smaller DNA methylation clock from 2020 that compares dog and human ageing.</li></ul>
""",
         faq=[("Why do big dogs die younger?", "Nobody knows the full answer, but a 2026 Science study of 894 Dog Aging Project dogs found larger dogs show faster DNA methylation ageing, especially in transposable elements, where age-related loss was 31% stronger than in smaller dogs."),
              ("What is epigenetic age?", "An estimate of biological age from chemical marks on DNA called methylation. In this study, dogs whose epigenetic age ran ahead of their real age had a higher risk of death."),
              ("Does this study change how I should care for my large dog?", "Not directly. It is basic research with no new test or treatment. Keep your dog lean, keep up regular vet visits, and ask your vet when to start senior check-ups for a large breed.")],
         sources=src("mariner2026", "asu2026", "wang2020"),
         related=[("dog-age-calculator.html", "Dog age calculator"), ("health.html", "Dog health basics"), ("blog/is-my-dog-overweight.html", "Is my dog overweight?"), ("blog/why-do-dogs-yawn.html", "Why do dogs yawn?")],
         published="2026-10-15")


    # news 18 Oct 2026: Alzheimer's-like brain changes in senior dogs (npj Dementia)
    post(page, "dog-dementia-brain-study", "Dog Dementia Brains Resemble Early Alzheimer's | SnoutsWise",
         "News: an npj Dementia study of 24 senior dogs found Alzheimer's-like amyloid deposits, heavier in dogs with cognitive decline. What it means.",
         "News: senior dogs with dementia show early Alzheimer's-like brain changes",
         "A study published in npj Dementia on 6 October 2026 examined the brains of 24 senior pet dogs donated by their owners. The dogs had amyloid-beta deposits similar to the early stages of Alzheimer's disease in people, and dogs rated as cognitively impaired had more of it. Age was the strongest predictor of how much amyloid built up. The researchers say aging pet dogs could help scientists study the earliest stages of Alzheimer's.",
         """
<h2>What the researchers did</h2>
<p>Abdullatif Alsulami, Julie Moreno, Caitlin Latimer and colleagues, working with the Dog Aging Project, examined post-mortem brain tissue from 24 client-owned senior dogs. According to UW Medicine, the analyses were carried out at Colorado State University and UW Medicine in Seattle. The team adapted the staging methods pathologists use for human Alzheimer's disease and compared the brain findings with each dog's earlier score on the Canine Cognitive Dysfunction Rating, a questionnaire about behaviour, and with blood biomarkers.</p>
<h2>What they found</h2>
<ul><li>The senior dogs had amyloid-beta deposits in a pattern consistent with early regional involvement in the human staging system.</li>
<li>Some had phosphorylated tau, another protein linked to Alzheimer's, but it was variable and restricted to certain regions. No neuritic plaques were found.</li>
<li>Cognitively impaired dogs had a greater amyloid burden, and age was the strongest predictor of amyloid build-up.</li>
<li>Blood levels of a protein called GFAP rose with amyloid plaque burden. The other blood markers tested did not track it.</li></ul>
<p>In the UW Medicine release, Latimer said no one had mapped this pathology in dogs before and that the dogs could represent a model of the earliest stages of Alzheimer's disease. Moreno said the work supports companion dogs as an important model for studying Alzheimer's and related diseases.</p>
<h2>What it means for owners</h2>
<ul><li><b>Canine cognitive dysfunction is real.</b> UW Medicine notes it is typically seen in dogs over 8 years old, with signs such as disorientation, changes in social interaction and a decline in everyday function.</li>
<li><b>Tell your vet about changes in an older dog.</b> Getting lost in familiar places, changed sleep, new house soiling or less interest in family can have many causes, including pain or other illness, so a check-up comes first (see <a href="{R}health.html">dog health basics</a>).</li>
<li><b>This is not a test or a treatment yet.</b> The study was small and looked at brains after death. Blood markers such as GFAP need more research before they could help in the clinic.</li>
<li><b>Big dogs age faster.</b> Use our <a href="{R}dog-age-calculator.html">dog age calculator</a> and read about <a href="{R}blog/big-dogs-age-faster-dna-study.html">size and DNA aging</a> to know when your dog counts as a senior.</li></ul>
""",
         faq=[("Can dogs get Alzheimer's disease?", "Dogs get canine cognitive dysfunction, a form of dementia. A 2026 npj Dementia study found senior dogs develop early Alzheimer's-like amyloid deposits, with more in cognitively impaired dogs."),
              ("What are signs of dementia in dogs?", "Signs include disorientation, changes in social interaction and a decline in everyday function, typically in dogs over about 8 years old. See your vet, because pain and other illnesses can cause similar changes."),
              ("Is there a blood test for dog dementia?", "Not yet in routine use. In the 2026 study, blood GFAP levels rose with amyloid plaque burden, but the other markers tested did not, and more research is needed.")],
         sources=src("alsulami2026", "uw2026ccd"),
         related=[("health.html", "Dog health basics"), ("blog/big-dogs-age-faster-dna-study.html", "Big dogs age faster"), ("dog-age-calculator.html", "Dog age calculator"), ("blog/do-dogs-dream.html", "Do dogs dream?")],
         published="2026-10-18")


    # 15 daily fact: why do dogs wag their tails (20 Oct 2026)
    post(page, "why-do-dogs-wag-their-tails", "Why Do Dogs Wag Their Tails? What Science Says | SnoutsWise",
         "Why do dogs wag their tails? Wagging signals arousal, not only happiness, and the side it leans to can differ. What the research shows.",
         "Why do dogs wag their tails? It signals arousal, not just happiness",
         "Dogs wag their tails mainly as a social signal, and a wag shows that a dog is aroused or engaged, not always that it is happy. A 2024 Biology Letters review found tail wagging is linked with both positive and negative arousal. Studies from the University of Bari also found that dogs tend to wag more to the right for things they want to approach, such as their owner, and more to the left for things that make them want to withdraw, and that other dogs notice the difference.",
         """
<h2>A wag means arousal, not always joy</h2>
<p>In a 2024 Biology Letters review, Silvia Leonetti, Andrea Ravignani and colleagues pulled together what is known about tail wagging. People tend to read any wag as a happy dog, but the review notes that quantitative studies have produced patchy results. Wagging is frequently associated with both positive and negative arousal, and several studies found that the time a dog spends wagging rises with its heart rate. There is indirect evidence linking wagging with oxytocin, especially when dogs are reunited with a familiar person, while links with the stress hormone cortisol are inconsistent across studies.</p>
<h2>Left and right wags can mean different things</h2>
<p>Angelo Quaranta, Marcello Siniscalchi and Giorgio Vallortigara reported in a 2007 Current Biology paper that tail wagging is asymmetric. As the 2024 review summarizes this line of work, dogs show a right-side wagging bias, linked to activity in the left side of the brain, for stimuli with a positive emotional value such as their owner or a familiar person. They show left-biased wagging, linked to the right side of the brain, for stimuli that make them want to withdraw, such as an unfamiliar dominant dog.</p>
<h2>Other dogs read the direction of a wag</h2>
<p>In a 2013 follow-up in Current Biology, Siniscalchi and colleagues showed dogs video images of other dogs wagging with a left or right bias. Dogs watching left-biased wagging had higher heart activity and scored higher for anxious behavior than dogs watching right-biased wagging. The authors say this shows dogs are sensitive to the tail signals of other dogs and could be useful for dog welfare work.</p>
<h2>Why dogs wag more than wolves</h2>
<p>The 2024 review asks why dogs wag their tails more often, and in more situations, than close relatives such as wolves. The authors offer two hypotheses to be tested: wagging may have increased as a side effect of selecting dogs for tameness and docility during domestication, or people may have favoured it directly because humans are drawn to rhythmic movement. Neither idea is proven yet, and the authors call wagging one of the most visible but least studied animal behaviors.</p>
<h2>What this means for owners</h2>
<ul><li><b>Read the whole dog, not just the tail.</b> A wag tells you a dog is engaged. Check the body, ears, mouth and the situation before you approach (see <a href="{R}behavior.html">dog behavior</a> and <a href="{R}behavior.html#stress">reading stress</a>).</li>
<li><b>Do not assume a wagging dog is friendly.</b> Since wagging also goes with negative arousal, a stiff dog wagging while it stares or growls is not inviting contact. Let unfamiliar dogs come to you, or not at all.</li>
<li><b>The side is a subtle clue, not a rule.</b> The left and right findings come from group averages in lab studies, so do not try to judge one dog's mood from wag direction alone.</li>
<li><b>Notice changes.</b> If your dog stops wagging, holds its tail oddly or yelps when the tail is touched, a vet check is worth it, since pain can change tail carriage (see <a href="{R}health.html">dog health basics</a>).</li></ul>
""",
         faq=[("Why do dogs wag their tails?", "Mainly to communicate. A 2024 Biology Letters review found tail wagging goes with both positive and negative arousal, so a wag means a dog is engaged, not always happy."),
              ("Does a wagging tail mean a dog is happy?", "Not always. Wagging is linked with both positive and negative arousal. Look at the whole body and the situation, and be careful with a stiff dog that wags while staring or growling."),
              ("What does it mean when a dog wags to the right or left?", "Studies from the University of Bari found dogs tend to wag more to the right for things they want to approach, such as their owner, and more to the left for things that trigger withdrawal, such as an unfamiliar dominant dog."),
              ("Can dogs read other dogs' tail wags?", "Yes. In a 2013 Current Biology study, dogs watching videos of left-biased wagging dogs had higher heart activity and more anxious behavior than dogs watching right-biased wagging.")],
         sources=src("leonetti2024", "quaranta2007", "siniscalchi2013"),
         related=[("behavior.html", "Dog behavior"), ("blog/why-do-dogs-yawn.html", "Why do dogs yawn?"), ("blog/can-dogs-smell-fear.html", "Can dogs smell fear?"), ("blog/why-do-dogs-tilt-their-heads.html", "Why do dogs tilt their heads?"), ("training.html", "Reward based training")],
         published="2026-10-20")

    # 20 daily fact: puppy dog eyes (28 Oct 2026)
    post(page, "why-do-dogs-make-puppy-dog-eyes", "Why Do Dogs Make Puppy Dog Eyes? The Science | SnoutsWise",
         "Why do dogs make puppy dog eyes? A 2019 PNAS study found dogs have an eyebrow-raising muscle wolves lack, and dogs make more faces when people watch.",
         "Why do dogs make puppy dog eyes? A muscle wolves mostly lack",
         "That pleading look, with the inner eyebrows raised and the eyes looking bigger, has a real anatomical basis. A 2019 study in PNAS found that dogs have a small muscle for raising the inner eyebrow that wolves do not have in the same way, and a 2017 study found that dogs make more facial movements when a person is paying attention to them.",
         """
<h2>A muscle for raising the eyebrows</h2>
<p>In the 2019 study, researchers from the UK and US dissected the heads of dogs and wolves. A muscle called the levator anguli oculi medialis, which raises the inner eyebrow intensely, was present in all the dogs studied but not in the wolves in the same way.</p>
<h2>Dogs use the movement more than wolves</h2>
<p>The team also filmed dogs and wolves meeting a person. Dogs raised their inner eyebrows more often and more intensely than wolves did, and the most intense movements were seen only in dogs.</p>
<h2>Why it might matter to people</h2>
<p>The movement makes the eyes look bigger and more baby-like, and it resembles the face humans make when sad. The authors suggest it may trigger a nurturing response in people. Their hypothesis is that, during domestication, dogs with expressive eyebrows had an advantage and that puppy dog eyes are the result of selection based on human preferences. This is a hypothesis, not a proven cause.</p>
<h2>Dogs make more faces when we are watching</h2>
<p>A 2017 study in Scientific Reports, from the University of Portsmouth, placed dogs in front of a person who was either facing them or turned away, with or without food. Dogs made significantly more facial movements, including the eyebrow raise, when the person was paying attention. Food on its own made no difference. The researchers say this suggests dog facial expressions may be active attempts to communicate, not just automatic displays of emotion.</p>
<h2>What this means for owners</h2>
<ul><li><b>The look is partly aimed at you.</b> It is one way dogs communicate with people, so read it together with the rest of your dog's <a href="{R}behavior.html">body language</a>.</li>
<li><b>It is not proof of guilt or sadness.</b> The studies measured facial movements, not feelings. See also <a href="{R}blog/do-dogs-feel-jealousy.html">what research says about dog emotions</a>.</li>
<li><b>Puppy eyes at mealtimes are not hunger proof.</b> Stick to a measured portion with our <a href="{R}how-much-to-feed-a-dog.html">dog feeding calculator</a> and keep treats to about 10 percent of daily calories.</li></ul>
""",
         faq=[("Why do dogs make puppy dog eyes?", "A 2019 PNAS study found dogs have a muscle that raises the inner eyebrow intensely, which wolves lack in the same form. The authors suggest people may have favored dogs with this expression during domestication."),
              ("Do wolves make puppy dog eyes?", "Rarely. In the 2019 study, wolves raised their inner eyebrows less often and less intensely than dogs, and the most intense movements were seen only in dogs."),
              ("Do dogs make faces on purpose?", "A 2017 study found dogs made more facial movements when a person was watching them than when the person was turned away, which suggests the expressions may be partly meant to communicate.")],
         sources=src("kaminski2019", "kaminski2017"),
         related=[("behavior.html", "Dog behavior"), ("blog/do-dogs-like-baby-talk.html", "Do dogs like baby talk?"), ("blog/do-dogs-understand-pointing.html", "Do dogs understand pointing?"), ("blog/why-do-dogs-tilt-their-heads.html", "Why do dogs tilt their heads?"), ("how-much-to-feed-a-dog.html", "How much to feed a dog")],
         published="2026-10-28")

    # 19 daily fact: dog-directed speech (27 Oct 2026)
    post(page, "do-dogs-like-baby-talk", "Do Dogs Like Baby Talk? What Studies Show | SnoutsWise",
         "Do dogs like baby talk? Puppies react strongly to high-pitched dog-directed speech, and a 2018 study found adult dogs prefer it when paired with dog words.",
         "Do dogs like baby talk? Puppies do, and adult dogs like it with dog words",
         "Most people talk to dogs in a higher, slower, sing-song voice, much like the way adults speak to babies. Studies suggest it is not wasted effort. A 2017 study found that puppies react strongly to this dog-directed speech, and a 2018 study found that adult dogs paid more attention to, and preferred to spend time near, a person using it, as long as the words were about dogs too.",
         """
<h2>We all do it</h2>
<p>In a 2017 study in Proceedings of the Royal Society B, French and British researchers recorded adults speaking to photos of puppies, adult dogs and old dogs. People used dog-directed speech with dogs of every age. The voice pattern was much the same for all ages, except that pitch went highest for puppies.</p>
<h2>Puppies respond strongly</h2>
<p>The team then played recordings to dogs with no person in sight. Puppies were highly reactive to dog-directed speech, and pitch was a key factor in how they responded. Older dogs in this setup did not react any differently to dog-directed speech than to normal speech.</p>
<h2>Adult dogs prefer it in real life</h2>
<p>A 2018 study in Animal Cognition from the University of York used a more natural setup, with real speakers in the room. Adult dogs paid more attention to, and showed more friendly behavior toward, a person using dog-directed speech than a person using normal adult speech.</p>
<h2>It is the voice plus the words</h2>
<p>In a second experiment the researchers mixed things up, using a dog-directed voice with ordinary adult words and a normal voice with dog words like "good boy" and "walkies". Neither mix made a clear difference on its own. The authors suggest it is the combination of the sing-song voice and dog-relevant words that dogs like.</p>
<h2>What this means for owners</h2>
<ul><li><b>Talking to your dog in a warm, high voice is fine.</b> It may help get a puppy's attention and may strengthen your bond with an adult dog.</li>
<li><b>Use words that matter to your dog.</b> In the 2018 study, the voice worked best together with dog-related words. This fits with <a href="{R}training.html">reward based training</a> and with research on <a href="{R}blog/can-dogs-learn-toy-names.html">dogs learning words</a>.</li>
<li><b>Watch your dog's response.</b> Every dog is different, so notice what gets a relaxed, interested reaction (see <a href="{R}behavior.html">dog behavior</a> and <a href="{R}blog/why-do-dogs-tilt-their-heads.html">why dogs tilt their heads</a>).</li></ul>
""",
         faq=[("Do dogs like baby talk?", "Studies suggest many do. A 2017 study found puppies react strongly to high-pitched dog-directed speech, and a 2018 study found adult dogs paid more attention to and preferred a person using it with dog-related words."),
              ("Why do people talk to dogs in a high voice?", "A 2017 study found people use dog-directed speech with dogs of all ages, with the highest pitch for puppies. The authors suggest it is a natural way of trying to connect with listeners who do not speak."),
              ("Do older dogs respond to dog-directed speech?", "In recorded playback tests, older dogs did not react differently, but in a 2018 study with real speakers, adult dogs preferred a person using dog-directed speech with dog words.")],
         sources=src("benaderet2017", "benjamin2018"),
         related=[("behavior.html", "Dog behavior"), ("training.html", "Reward based training"), ("blog/why-do-dogs-make-puppy-dog-eyes.html", "Why do dogs make puppy dog eyes?"), ("blog/can-dogs-learn-toy-names.html", "Can dogs learn toy names?"), ("blog/why-do-dogs-tilt-their-heads.html", "Why do dogs tilt their heads?"), ("blog/dogs-bouba-kiki-effect-study.html", "Dogs and the bouba-kiki effect")],
         published="2026-10-27")

    # 18 daily fact: toy name learning (26 Oct 2026)
    post(page, "can-dogs-learn-toy-names", "Can Dogs Learn the Names of Their Toys? | SnoutsWise",
         "Can dogs learn toy names? A 2021 Scientific Reports study found two gifted dogs learned new toy names in four tries, but 20 family dogs did not.",
         "Can dogs learn the names of their toys? A few gifted dogs can, fast",
         "Most dogs learn words like sit and walk, but learning the names of objects is different. A 2021 study in Scientific Reports found that two dogs who already knew many toy names could learn a new toy's name after hearing it just four times while playing with their owner. The same test with 20 ordinary family dogs found no sign of learning, which suggests this is a rare talent.",
         """
<h2>The gifted dogs</h2>
<p>Researchers in Hungary tested two dogs that already knew the names of multiple toys. Each dog heard a new toy's name four times and was then tested on whether it had learned which toy the name belonged to.</p>
<h2>Play beats puzzles</h2>
<p>The dogs met new names in two ways. In one, the owner named the toy while playing with the dog. In the other, the dog had to work out which unfamiliar toy matched a new word by ruling out the toys it already knew. Both dogs succeeded after the social play sessions but not after the exclusion task, so the authors suggest that fast word learning in dogs depends on a social setting.</p>
<h2>Memory fades without practice</h2>
<p>The dogs still remembered the new names after two minutes, but their memory tended to fade after 10 minutes and after an hour. Four exposures seem to be enough to learn a name, but not enough to keep it for long.</p>
<h2>Most dogs could not do it</h2>
<p>The team ran the same play-based procedure with 20 typical family dogs. None showed evidence of learning the new names. The authors say future studies should find out whether the skill comes from rare individual talent or from earlier practice with object names.</p>
<h2>What this means for owners</h2>
<ul><li><b>Do not worry if your dog does not learn toy names.</b> In this study ordinary family dogs did not learn them, so it is not a sign that anything is wrong.</li>
<li><b>If you want to try, keep it playful.</b> The gifted dogs learned best when names came up during play with their owner, which fits the <a href="{R}training.html">reward based training</a> approach.</li>
<li><b>Head tilts may be part of it.</b> A separate study linked frequent head tilting to dogs that know toy names (see <a href="{R}blog/why-do-dogs-tilt-their-heads.html">why dogs tilt their heads</a>).</li></ul>
""",
         faq=[("Can dogs learn the names of their toys?", "A few can. In a 2021 Scientific Reports study, two dogs that already knew many toy names learned a new one after four exposures during play, but 20 typical family dogs did not."),
              ("How do gifted dogs learn toy names best?", "In the study, the dogs learned new names when the owner named the toy while playing, not when they had to work it out by ruling out familiar toys."),
              ("Do dogs remember new toy names?", "The gifted dogs remembered them after two minutes, but memory tended to fade after 10 minutes and one hour, so more practice may be needed.")],
         sources=src("fugazza2021rapid"),
         related=[("training.html", "Reward based training"), ("blog/do-dogs-like-baby-talk.html", "Do dogs like baby talk?"), ("blog/why-do-dogs-tilt-their-heads.html", "Why do dogs tilt their heads?"), ("blog/do-dogs-understand-pointing.html", "Do dogs understand pointing?"), ("blog/dogs-bouba-kiki-effect-study.html", "Dogs and the bouba-kiki effect")],
         published="2026-10-26")

    # 17 daily fact: heat sensing nose (25 Oct 2026)
    post(page, "can-dogs-sense-heat-with-their-nose", "Can Dogs Sense Heat With Their Nose? | SnoutsWise",
         "Can dogs sense heat with their nose? A 2020 Scientific Reports study found dogs can detect weak radiant heat from a distance. What it found.",
         "Can dogs sense heat with their nose? A 2020 study says yes",
         "The bare, often moist skin at the tip of a dog's nose, called the rhinarium, is cold and packed with nerves. A 2020 study in Scientific Reports found that dogs can tell a warm object from a neutral one by its radiating heat alone, and that warm stimuli light up a part of the dog brain that handles touch and body sensation. The authors call it a sensory ability not described before in a carnivore.",
         """
<h2>What the rhinarium is</h2>
<p>The rhinarium is the naked, often moist skin on the tip of the nose. In dogs it is prominent and richly supplied with nerves, which suggested to researchers that it does more than help with smell. The study also notes that the nose tips of carnivores are considerably colder than those of plant eaters such as horses and cattle, and the team guessed that this coldness could make the dog nose especially sensitive to radiant heat.</p>
<h2>The training test</h2>
<p>Researchers in Hungary and Sweden trained three dogs to choose between two objects placed at a distance. One object was about room temperature. The other was warmed to about the surface temperature of a furry mammal. The dogs could not tell them apart by sight or smell, only by the heat the warm one gave off, and they learned to pick it out.</p>
<h2>The brain scans</h2>
<p>The team then scanned 13 awake, trained dogs with functional MRI while showing them heat stimuli at similar temperatures. The warm stimulus caused a stronger response in the left somatosensory association cortex, a brain area that processes body sensations, than the neutral one did.</p>
<h2>What this does and does not show</h2>
<p>The study shows that dogs can detect weak radiant heat and that their brains respond to it. It does not prove how dogs use this sense in daily life. The authors suggest it may have helped dogs' wild ancestors find warm prey, but that idea still needs testing, and the behaviour experiment used only three dogs.</p>
<h2>What this means for owners</h2>
<ul><li><b>The nose is a whole sensing organ.</b> Beyond smell, the nose tip also seems to pick up warmth, one more reason dogs explore the world nose first (see <a href="{R}behavior.html">dog behavior</a>).</li>
<li><b>Health questions go to your vet.</b> This research is about sensing, not health, so ask your vet about any change in your dog's nose such as cracking, bleeding or discharge (see <a href="{R}health.html">dog health</a>).</li></ul>
""",
         faq=[("Can dogs sense heat with their nose?", "Yes. A 2020 Scientific Reports study trained dogs to pick a warm object from a neutral one by its radiant heat alone."),
              ("Why is a dog's nose cold?", "The study notes that the nose tips of carnivores like dogs are much colder than those of plant eaters, and suggests the coldness may help the nose detect radiant heat."),
              ("What part of the dog brain responds to heat?", "In brain scans of 13 awake dogs, warm stimuli caused a stronger response in the left somatosensory association cortex.")],
         sources=src("balint2020"),
         related=[("behavior.html", "Dog behavior"), ("blog/can-dogs-smell-fear.html", "Can dogs smell fear?"), ("blog/do-dogs-recognize-themselves-in-mirror.html", "Do dogs recognize themselves in a mirror?"), ("blog/can-dogs-see-color.html", "Can dogs see color?")],
         published="2026-10-25")

    # 16 daily fact: mirror self-recognition (21 Oct 2026)
    post(page, "do-dogs-recognize-themselves-in-mirror", "Do Dogs Recognize Themselves in a Mirror? | SnoutsWise",
         "Do dogs recognize themselves in a mirror? Dogs fail the classic mirror test, but a 2017 smell-based study suggests they know their own odour.",
         "Do dogs recognize themselves in a mirror? Not by sight, but maybe by smell",
         "Dogs do not pass the classic mirror test, so there is no good evidence that they recognize their own reflection. But dogs live in a world of smell, and a 2017 study in Behavioural Processes built an \"olfactory mirror\" from each dog's own urine. Dogs sniffed their own scent longer when it had been changed with an extra odour, which the author reads as a sign that they recognize the scent as their own.",
         """
<h2>The classic mirror test</h2>
<p>In 1970 the psychologist Gordon Gallup reported in Science that chimpanzees given time with a mirror began to use it to inspect parts of their own bodies. When they were later marked with dye on spots they could only see in the mirror, they touched the marks. This mark test became the standard check for mirror self-recognition. Dogs have not passed it: as the 2017 study below notes, dogs do well on many social thinking tasks but have not passed the test of mirror self-recognition.</p>
<h2>Why a mirror may be the wrong test for dogs</h2>
<p>Alexandra Horowitz of Barnard College argued that a visual test may not suit a species whose main sense is smell, and that dogs may not be motivated to care about a mark on their fur. So she designed a smell version of the test, based on how dogs naturally sniff the scent marks of other dogs.</p>
<h2>The olfactory mirror study</h2>
<p>Dogs were offered canisters to sniff. In the key test one held the dog's own urine, the \"olfactory mirror\", and another held the dog's own urine with an extra odour added. Dogs spent longer investigating their own scent when it was modified than when it was not, which Horowitz reads as recognising the scent as being of or from themselves. Dogs also spent longer on the scent of other known or unknown dogs than on their own. In a second experiment they spent longer on the modified sample than on the added odour by itself, which suggests novelty alone does not explain the result.</p>
<h2>What this does and does not show</h2>
<p>The study suggests dogs can tell their own scent from changed versions and from other dogs, which is a kind of self-recognition by smell. It does not prove that dogs have self-awareness in the human sense, and it is one study that other labs would need to repeat.</p>
<h2>What this means for owners</h2>
<ul><li><b>Barking at a mirror is normal.</b> Some dogs react to their reflection and others ignore it. Either is fine, and neither tells you how clever your dog is.</li>
<li><b>Let your dog sniff on walks.</b> Scent is how dogs gather information about other dogs and themselves (see <a href="{R}behavior.html">dog behavior</a> and <a href="{R}blog/can-dogs-smell-fear.html">can dogs smell fear?</a>).</li></ul>
""",
         faq=[("Do dogs recognize themselves in a mirror?", "There is no good evidence they do by sight. Dogs have not passed the classic mirror mark test."),
              ("Can dogs recognize their own smell?", "A 2017 Behavioural Processes study found dogs sniffed their own urine longer when an extra odour was added, suggesting they recognize their own scent."),
              ("Why does my dog ignore its reflection?", "No one knows for sure, but dogs rely heavily on smell and a reflection carries no dog scent, which may be one reason it holds little interest.")],
         sources=src("horowitz2017", "gallup1970"),
         related=[("behavior.html", "Dog behavior"), ("blog/can-dogs-smell-fear.html", "Can dogs smell fear?"), ("blog/do-dogs-understand-pointing.html", "Do dogs understand pointing?"), ("blog/why-do-dogs-wag-their-tails.html", "Why do dogs wag their tails?")],
         published="2026-10-21")


    # 14 daily fact: how do dogs drink water (19 Oct 2026)
    post(page, "how-do-dogs-drink-water", "How Do Dogs Drink Water? The Physics of Lapping | SnoutsWise",
         "How do dogs drink water? They curl the tongue back and pull it up fast, lifting a water column they bite off. Why dogs are messy drinkers.",
         "How do dogs drink water? A fast tongue pulls up a column of water",
         "Dogs cannot suck water up the way people do, so they lap. A dog curls the tip of its tongue backward, dips it into the bowl and then whips it upward very fast. That pulls a column of water up out of the bowl, and the dog times its bite to close on the column just as it breaks off. High speed video studies also show that water clings to the surface of the tongue, and that a dog needs at least three laps to move a mouthful back to its throat.",
         """
<h2>Dogs lap with a fast upward flick</h2>
<p>In a 2015 PNAS study, Sean Gart, Sunghwan Jung and colleagues filmed a wide range of dogs of different breeds and body sizes while they drank, and built physical experiments that copied the motion of a dog's tongue leaving the water. They found that dogs accelerate the tongue upward more quickly than cats do. That fast pull drags a column of water up out of the bowl, and the dog times its bite to coincide with the moment the column pinches off, so it catches the water before it falls back.</p>
<h2>Why dogs are such messy drinkers</h2>
<p>The same study explains the splashing. A dog curls its tongue backward, like a ladle facing the wrong way, and the authors found that this backward curl increases the size of the water column. That lets a dog drink more per lap than it could with a straight tongue, at the cost of water flying around the bowl.</p>
<h2>Water sticks to the tongue, then gets trapped</h2>
<p>A 2011 Biology Letters study by A. W. Crompton and Catherine Musinsky used high speed light video and X-ray video of drinking dogs. They reported that, like cats, dogs rely on liquid sticking to the tongue rather than simply scooping it. Water rides up on the tongue's surface as it is drawn back, and a tight contact between the tongue and the ridges on the roof of the mouth (the palatal rugae) traps the water so it does not fall out when the tongue goes out again. They found that at least three lapping cycles are needed to move liquid through a dog's mouth to the throat.</p>
<h2>How this compares with cats</h2>
<p>Cats were studied first. In a 2010 Science paper, Pedro Reis, Sunghwan Jung and colleagues showed that cats curl the tongue so its upper surface touches the water, then lift it rapidly so a column of liquid grows by inertia until gravity breaks it, and close their jaws to capture it. They also found lapping speed is tuned to body mass, a pattern that held from house cats to lions. Cats do this neatly with a light touch, while dogs plunge the curled tongue in and accelerate it harder, which is where the mess comes from.</p>
<h2>What this means for owners</h2>
<ul><li><b>Splashing is normal.</b> It comes from the backward curl of the tongue, not bad manners. A wide, heavy bowl on a mat or an easy to wipe floor helps.</li>
<li><b>Keep fresh water available.</b> Refill and clean the bowl daily, and offer extra water and shade on hot days (see <a href="{R}care.html">everyday dog care</a> and <a href="{R}health.html">dog health basics</a>).</li>
<li><b>Watch for changes.</b> If your dog suddenly drinks much more or much less than usual, or struggles to lap, call your vet rather than guessing at the cause.</li>
<li><b>Lapping takes a few goes.</b> Since a mouthful needs at least three laps to reach the throat, a dog drinking for a while at the bowl is just working through that cycle.</li></ul>
""",
         faq=[("How do dogs drink water?", "By lapping. A dog curls its tongue backward, dips it in and accelerates it upward, pulling up a column of water that it bites off just as the column breaks."),
              ("Why are dogs such messy drinkers?", "A 2015 PNAS study found the backward curl of a dog's tongue increases the size of the water column, so dogs drink more per lap but splash more too."),
              ("Do dogs scoop water with their tongue?", "Not mainly. X-ray video in a 2011 Biology Letters study showed water clings to the tongue surface and is trapped against ridges on the roof of the mouth, with at least three laps needed to move it to the throat."),
              ("Do dogs and cats drink the same way?", "Both lap and both rely on water sticking to the tongue, but cats touch the surface lightly while dogs plunge the curled tongue in and accelerate it faster than cats do.")],
         sources=src("gart2015", "crompton2011", "reis2010"),
         related=[("care.html", "Everyday dog care"), ("health.html", "Dog health basics"), ("blog/why-do-dogs-eat-grass.html", "Why do dogs eat grass?"), ("blog/can-dogs-see-color.html", "Can dogs see color?"), ("blog/do-dogs-understand-pointing.html", "Do dogs understand pointing?")],
         published="2026-10-19")


    # 13 daily fact: do dogs understand pointing (18 Oct 2026)
    post(page, "do-dogs-understand-pointing", "Do Dogs Understand Pointing? What Studies Show | SnoutsWise",
         "Do dogs understand pointing? Yes: even 8 week old puppies follow human points, and studies link the skill to domestication and genes.",
         "Do dogs understand pointing? Yes, and puppies can do it from about 8 weeks",
         "Most dogs follow a human pointing gesture to find hidden food, and they do it without special training. A 2021 study of 375 eight-week-old puppies found they were highly skilled at using human gestures, with no sign that they needed to learn it, and that over 40% of the variation in point following was down to genes. Wolf puppies raised by people do much worse, which points to domestication shaping this skill.",
         """
<h2>Dogs beat great apes and hand-raised wolves</h2>
<p>In a 2002 Science paper, Brian Hare and colleagues noted that dogs are more skilful than great apes at tasks where they must read human signals, such as pointing or looking, to find hidden food. In their experiments, wolves raised by humans did not show the same skills, while domestic puppies only a few weeks old did, even puppies that had had little human contact. The authors concluded that domestication selected dogs for social thinking skills that let them communicate with people in unusual ways.</p>
<h2>Puppies follow points before they could have learned it</h2>
<p>In 2021, Emily Bray, Evan MacLean and colleagues tested 375 puppies at 8 weeks old, all from an assistance dog breeding programme, on a set of social tasks. The puppies were highly skilled at using a range of human gestures, and the researchers found no evidence that their performance depended on learning. Because the puppies' family trees were known, the team could estimate heritability: over 40% of the variation in point following and in attention to human faces was linked to genetic factors.</p>
<h2>Dog puppies versus wolf puppies</h2>
<p>A companion 2021 study led by Hannah Salomons and Brian Hare compared 44 dog puppies and 37 wolf puppies aged 5 to 18 weeks. The wolf puppies were raised with intensive human contact. Dog puppies were more attracted to people, read human gestures more skilfully and made more eye contact with humans than the wolf puppies. On tasks that did not involve people, such as memory and self control, the two species performed similarly. The authors say this fits the idea that domestication boosted dogs' ability to cooperate and communicate with humans.</p>
<h2>What this means for owners</h2>
<ul><li><b>Pointing is a ready-made training tool.</b> Most dogs already follow a clear point, so you can use it to direct your dog to a toy, a mat or a dropped treat, then reward the result (see <a href="{R}training.html">reward based training</a>).</li>
<li><b>Dogs differ.</b> Since part of the skill is inherited, some dogs follow points more easily than others. A dog that struggles is not being stubborn. Make the gesture bigger, get closer to the target and reward small successes.</li>
<li><b>Get your dog's attention first.</b> Say your dog's name or make eye contact before you point, then point clearly and hold it for a moment.</li>
<li><b>Watch what your dog tells you back.</b> Dogs read our signals closely, and theirs are worth reading too (see <a href="{R}behavior.html">dog behavior</a> and <a href="{R}blog/why-do-dogs-tilt-their-heads.html">why dogs tilt their heads</a>).</li></ul>
""",
         faq=[("Do dogs understand pointing?", "Most do. Studies show dogs follow human pointing to find hidden food far better than great apes or hand-raised wolves, and puppies can do it by 8 weeks old."),
              ("Do puppies need to learn to follow a point?", "Apparently not. A 2021 Current Biology study of 375 eight-week-old puppies found they were highly skilled at using human gestures and found no evidence their performance required learning."),
              ("Is following a point genetic in dogs?", "Partly. The same 2021 study found over 40% of the variation in puppies' point following and attention to human faces was attributable to genetic factors."),
              ("Can wolves follow human pointing?", "Not as well as dogs. In 2002 and 2021 studies, wolves raised by people did worse than dog puppies at reading human gestures, while doing about as well on non-social tasks.")],
         sources=src("hare2002", "bray2021", "salomons2021"),
         related=[("training.html", "Reward based training"), ("behavior.html", "Dog behavior"), ("blog/why-do-dogs-tilt-their-heads.html", "Why do dogs tilt their heads?"), ("blog/dogs-bouba-kiki-effect-study.html", "Dogs match sounds to shapes"), ("blog/puppy-socialization-window.html", "Puppy socialization window")],
         published="2026-10-18")


    # 12 daily fact: can dogs smell fear (16 Oct 2026)
    post(page, "can-dogs-smell-fear", "Can Dogs Smell Fear? What Odour Studies Found | SnoutsWise",
         "Can dogs smell fear and stress? Studies show dogs can tell stressed from calm human odour and react to fear sweat. What the research found.",
         "Can dogs smell fear? The evidence says they can pick up on it",
         "Dogs cannot read your mind, but several experiments show they can detect changes in human body odour linked to fear and stress, even with no sight or sound of the person. In a 2022 study, trained dogs picked a stressed person's breath and sweat sample over the same person's calm sample in 93.75% of 720 trials. Other studies found that the smell of human fear sweat made dogs more stressed, and that stress odour made dogs more cautious in a decision task.",
         """
<h2>Dogs can tell stressed odour from calm odour</h2>
<p>In 2022, Clara Wilson and colleagues collected breath and sweat samples from 36 people before and after a stressful mental arithmetic task, and checked that the task really raised stress using self reports and physiological measures. Four dogs trained to alert on the stress samples were then offered a choice of three pots: the person's stress sample, the same person's calm sample from before the task, and a blank. The dogs chose the stress sample with 90% to 96.88% accuracy, 93.75% across all 720 trials. Because the two samples came from the same person, the dogs must have been smelling a change linked to stress, not just who the person was.</p>
<h2>Fear sweat changes how dogs behave</h2>
<p>A 2018 study by Biagio D'Aniello and colleagues asked whether untrained pet dogs react to these smells. They collected armpit sweat from male donors under fear and happiness conditions, then exposed Labrador and Golden retrievers to fear sweat, happy sweat or a no-sweat control while their owner and a stranger were in the room. In the fear odour condition the dogs showed more stress behaviours and had higher heart rates than in the happy or control conditions. In the happy odour condition they approached and interacted with the stranger more and with their owner less.</p>
<h2>Stress odour can make dogs more cautious</h2>
<p>In 2024, Zoe Parr-Cortes and colleagues tested 18 dogs in a cognitive bias task, where dogs learn that a bowl in one spot has food and a bowl in another spot does not, then are shown bowls in ambiguous spots in between. With odour from unfamiliar stressed volunteers present, dogs were less likely to approach the ambiguous bowl closest to the unrewarded spot than with no odour. The authors read this as possible risk-reduction behaviour, a sign that human stress smell may nudge dogs toward a more pessimistic mood and affect how they learn.</p>
<h2>What this means for owners</h2>
<ul><li><b>"Smelling fear" is real, with limits.</b> The studies show dogs can detect and react to odour changes from fear and stress. They do not show dogs understand the emotion the way a person would, and dogs also read your body language and voice.</li>
<li><b>Your stress can rub off.</b> If you are tense at the vet or during a tricky greeting, your dog may pick up on it. Slow breathing and calm handling help both of you. Watch for your dog's own stress signals such as lip licking, yawning or a tucked tail (see <a href="{R}behavior.html#stress">reading stress</a> and <a href="{R}blog/why-do-dogs-yawn.html">why dogs yawn</a>).</li>
<li><b>Do not stare down or run from an unfamiliar dog</b> to "hide" fear. Stand still, turn side on and let the dog lose interest. Never approach a dog that is growling or stiff.</li>
<li><b>Training sessions:</b> train when you are calm, and keep sessions short and positive (see <a href="{R}training.html">reward based training</a>).</li></ul>
""",
         faq=[("Can dogs really smell fear?", "Experiments suggest they can detect odour changes linked to fear and stress. In a 2018 study, pet retrievers exposed to fear sweat showed more stress behaviours and higher heart rates than dogs exposed to happy sweat or no sweat."),
              ("How accurate are dogs at smelling human stress?", "In a 2022 PLOS ONE study, four trained dogs picked a person's post-stress breath and sweat sample over the same person's calm sample with 93.75% accuracy across 720 trials."),
              ("Does my stress affect my dog?", "It may. A 2024 Scientific Reports study found dogs exposed to the smell of stressed strangers were more cautious in an ambiguous food task, which the authors linked to a more pessimistic state. Dogs also respond to your voice and body language."),
              ("Should I hide my fear around a strange dog?", "You cannot hide your smell, but calm behaviour matters most. Stand still, turn side on, avoid staring and do not run. Never approach a dog that is growling or stiff.")],
         sources=src("wilson2022", "daniello2018", "parrcortes2024"),
         related=[("behavior.html", "Dog behavior"), ("training.html", "Reward based training"), ("blog/why-do-dogs-yawn.html", "Why do dogs yawn?"), ("blog/do-dogs-feel-jealousy.html", "Do dogs feel jealousy?"), ("blog/can-dogs-see-color.html", "Can dogs see color?")],
         published="2026-10-16")


    # news 16 Oct 2026: bouba-kiki effect in dogs (Proc B)
    post(page, "dogs-bouba-kiki-effect-study", "Dogs Match Sounds to Shapes: Bouba-Kiki Study | SnoutsWise",
         "News: a Proceedings B study finds pet dogs link the word bouba with a round shape and kiki with a spiky one, like people do. What it means.",
         "News: dogs match \"bouba\" to round shapes and \"kiki\" to spiky ones",
         "People around the world tend to call a rounded shape \"bouba\" and a spiky shape \"kiki\". A study published in Proceedings of the Royal Society B on 14 October 2026 found that adult pet dogs show a similar link: they looked more at a rounded shape while \"bouba\" was played and looked at and explored a spiky shape while \"kiki\" was played. The authors say this suggests the sound and shape link is not unique to human language.",
         """
<h2>What the researchers did</h2>
<p>Eleonora Biffi and colleagues, led from the University of Parma in Italy according to New Scientist, showed pet dogs a rounded shape on one side of a room and a spiky shape on the other while the nonsense words were played. In the first experiment, 51 owners sat holding their adult dogs. New Scientist reports that 56% of dogs lingered on the round shape when they heard \"bouba\" and 63% focused on the spiky shape when they heard \"kiki\".</p>
<p>To rule out owners giving hidden cues, the team repeated the test with owners wearing headphones playing music so they could not hear the words. The result held, with a slightly stronger bias toward the round shape for \"bouba\".</p>
<h2>Why it matters</h2>
<p>The bouba-kiki effect has long been described in people as a case of sound symbolism linked to language. The paper notes that 3-day-old chicks also show it, and the dog result adds to evidence that it may be a broader matching between hearing and vision rather than something language creates. In New Scientist, Biffi said it may reflect general principles of how the brain combines information from different senses, while Attila Andics at Eotvos Lorand University, who was not an author, said a next question is whether dogs learn these links or are born with the expectation.</p>
<p>The authors say more work is needed on what the link is for and how it develops. Biffi told New Scientist the team is now testing puppies and wild canids such as foxes, and would like to test cats.</p>
<h2>What it means for owners</h2>
<ul><li><b>Nothing to change.</b> This is basic research on perception, not a training method.</li>
<li><b>Dogs process human sounds in rich ways.</b> It fits other research showing dogs pay close attention to how we speak (see <a href="{R}blog/why-do-dogs-tilt-their-heads.html">why dogs tilt their heads</a>).</li>
<li><b>Clear, consistent cue words still help.</b> Short, distinct words for each cue are easier for dogs to learn (see <a href="{R}training.html">reward based training</a>).</li></ul>
""",
         faq=[("What is the bouba-kiki effect?", "The tendency to match the made-up word bouba with a rounded shape and kiki with a spiky shape. It has been reported in people across many cultures and in young chicks."),
              ("Do dogs show the bouba-kiki effect?", "A 2026 Proceedings B study found adult pet dogs looked more at a rounded shape when bouba was played and at a spiky shape when kiki was played, even when owners could not hear the words."),
              ("Does this mean dogs understand language?", "No. The authors and outside experts say it points to general links between hearing and vision rather than language. It is not yet known whether dogs learn the link or are born with it.")],
         sources=src("biffi2026", "newsci2026bouba"),
         related=[("blog/why-do-dogs-tilt-their-heads.html", "Why do dogs tilt their heads?"), ("blog/can-dogs-smell-fear.html", "Can dogs smell fear?"), ("training.html", "Reward based training"), ("behavior.html", "Dog behavior")],
         published="2026-10-16")


    # blog index
    items = "".join('<article class="card"><h2><a href="{R}blog/%s.html">%s</a></h2><p>%s</p><p class="meta">Published %s</p></article>' % (s, h, d, nice(pd)) for s, h, d, pd in sorted(POSTS, key=lambda x: x[3], reverse=True))
    page("blog/index.html", "Dog Facts Explained by Research | SnoutsWise Blog",
         "Dog facts explained by research: why dogs tilt their heads, eat grass, yawn and dream, and whether they like baby talk or see color, answered with sources.",
         items, h1="SnoutsWise blog", kind="webpage",
         lead="Each article answers one dog question directly at the top, then explains the detail and the sources behind it.",
         crumbs=[("index.html", "Home"), ("blog/index.html", "Blog")], nav="blog/", updated="2026-10-20")

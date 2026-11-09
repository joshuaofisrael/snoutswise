"""AI generated, photo style images (made 23 Oct 2026 with the Grok Bot image tool for SnoutsWise).
No real people, no text in the images. Every figure carries an honest 'AI generated image' caption."""
import html
e = lambda s: html.escape(s, quote=True)
W, H = 1280, 720
AI = {
    "blog/why-do-dogs-pant.html": ("ai-dog-panting", "A golden retriever sitting on a porch with its mouth open and tongue out"),
    "blog/why-do-dogs-lick-people.html": ("ai-dog-licking", "A beagle gently licking a person's hand outdoors"),
    "blog/do-dogs-recognize-themselves-in-mirror.html": ("ai-dog-mirror", "A golden retriever sitting on a rug in a bright room, looking at its own reflection in a tall floor mirror"),
    "blog/why-do-dogs-wag-their-tails.html": ("ai-dog-tail-wag", "A black and white border collie running across a park lawn with its tail in mid wag"),
    "blog/how-do-dogs-drink-water.html": ("ai-dog-drinking", "A yellow Labrador lapping water from a steel bowl, with its tongue curled and droplets splashing"),
    "blog/do-dogs-understand-pointing.html": ("ai-dog-attention", "An attentive beagle sitting in a sunny garden with its gaze fixed on something just outside the frame"),
    "blog/can-dogs-smell-fear.html": ("ai-dog-sniffing", "A black Labrador in a meadow at golden hour with its nose raised, sniffing the air"),
    "blog/index.html": ("ai-dog-living-room", "A shaggy terrier mix lying on a woven rug in a sunlit living room and looking at the camera"),
    "faq.html": ("ai-dog-head-tilt", "A Jack Russell terrier tilting its head in curiosity against a soft green background"),
    "glossary.html": ("ai-dog-eye-closeup", "Close up of a dog's amber eye, ear and fur texture"),
    "research/index.html": ("ai-dog-study", "A focused border collie sitting calmly on a plain mat in a bright room"),
    "blog/why-do-dogs-circle-before-lying-down.html": ("ai-dog-circling-bed", "A scruffy terrier mix mid turn, circling on a round dog bed in a sunlit living room before lying down"),
    # registration only (second in-body image for the circling post; not a real page path, see _photos.py-style figure call in _content.py)
    "blog/why-do-dogs-circle-before-lying-down.html#paws": ("ai-dog-circling-paws", "Close up of a dog's front paws pressing down into a rumpled blanket mid turn before lying down"),
    # Added 2 Nov 2026 so every blog post has a hero/thumbnail image (owner rule)
    "blog/dog-ate-chocolate.html": ("ai-dog-chocolate-kitchen", "A chocolate Labrador sniffing at an open box of chocolates spilled on a kitchen floor"),
    "blog/puppy-socialization-window.html": ("ai-puppy-socialization", "A litter of young puppies exploring a colorful ball toy together in a bright puppy playpen"),
    "blog/dog-vaccine-schedule.html": ("ai-dog-vet-table", "A calm dog sitting on a stainless steel exam table in a bright veterinary clinic room"),
    "blog/alpha-dog-myth.html": ("ai-dog-pack-walk", "Three dogs of different breeds walking together side by side across a grassy field at golden hour"),
    "blog/is-my-dog-overweight.html": ("ai-dog-bowl-weight", "A rounded, chubby dachshund standing next to an empty steel food bowl on a kitchen floor"),
    "blog/can-dogs-see-color.html": ("ai-dog-color-field", "A golden retriever standing in a wildflower meadow full of blue and yellow flowers"),
    "blog/why-do-dogs-eat-grass.html": ("ai-dog-eating-grass", "A golden retriever grazing on green grass in a sunny backyard lawn"),
    "blog/why-do-dogs-tilt-their-heads.html": ("ai-dog-tilt-listening", "A curious mixed breed dog tilting its head while listening intently indoors"),
    "blog/do-dogs-dream.html": ("ai-dog-sleeping-dream", "A dog sleeping curled up on a soft bed in dim, cozy bedroom light"),
    "blog/do-dogs-feel-jealousy.html": ("ai-dogs-jealousy", "Two dogs sitting near a single toy on a living room floor, each eyeing the other"),
    "blog/why-do-dogs-yawn.html": ("ai-dog-yawning", "A dog mid yawn while lying on a couch in a sunlit living room"),
    "blog/big-dogs-age-faster-dna-study.html": ("ai-dogs-size-compare", "A large Great Dane and a small terrier standing side by side on a lawn"),
    "blog/dog-dementia-brain-study.html": ("ai-dog-senior-resting", "An elderly, grey muzzled dog resting calmly on a cushion in a quiet room"),
    "blog/do-dogs-know-when-you-are-sad.html": ("ai-dog-comfort", "A dog resting its chin on a folded blanket on a sofa, looking up attentively"),
    "blog/do-dogs-prefer-praise-or-food.html": ("ai-dog-treat-choice", "A dog sitting on a kitchen floor in front of two small bowls, one holding treats and one empty"),
    "blog/why-do-dogs-make-puppy-dog-eyes.html": ("ai-dog-puppy-eyes", "A close up of a dog with big round eyes looking up appealingly indoors"),
    "blog/do-dogs-like-baby-talk.html": ("ai-dog-ears-up", "A small terrier with ears perked up and its head cocked, sitting on a rug indoors"),
    "blog/can-dogs-learn-toy-names.html": ("ai-dog-toys", "A dog lying among colorful plush toys scattered on a living room floor, sniffing one"),
    "blog/can-dogs-sense-heat-with-their-nose.html": ("ai-dog-nose-closeup", "An extreme close up of a dog's wet black nose in soft directional light"),
    "blog/dogs-bouba-kiki-effect-study.html": ("ai-dog-shapes", "A dog looking curiously at two simple wooden shapes, one round and one spiky, on the floor"),
    "blog/why-do-dogs-howl-at-sirens.html": ("ai-dog-howling", "A mixed-breed dog outdoors with its head tilted up mid howl"),
    # registration only (mid-body ears image for the howl post)
    "blog/why-do-dogs-howl-at-sirens.html#ears": ("ai-dog-ears-up", "A small terrier with ears perked up and its head cocked, sitting on a rug indoors"),
    "blog/why-do-dogs-sniff-each-others-butts.html": ("ai-dogs-greeting-sniff", "Two relaxed dogs greeting nose to tail on a grassy park path"),
    # registration only (mid-body trail image for the sniffing post)
    "blog/why-do-dogs-sniff-each-others-butts.html#trail": ("ai-dogs-trail-sniff", "Two friendly dogs calmly sniffing near each other on a shaded trail"),
}

def has(path):
    return path in AI

def src(path):
    return AI[path][0] + ".webp"

def figure(path, R):
    if path not in AI:
        return ""
    s, alt = AI[path]
    return ('<figure class="photo ai"><img src="{R}img/{s}.webp" width="{w}" height="{h}" alt="{a}" loading="lazy" decoding="async">'
            '<figcaption>AI generated image, made for SnoutsWise. It is an illustration in a photo style, not a real photograph of a real event. '
            '<a href="{R}credits/">About our images</a></figcaption></figure>').format(R=R, s=s, w=W, h=H, a=e(alt))

def thumb(path, R, w=320, h=180):
    """Small lazy-loaded card/list thumbnail using the same hero image as figure(), no caption."""
    if path not in AI:
        return ""
    s, alt = AI[path]
    return '<img class="thumb" src="{R}img/{s}.webp" width="{w}" height="{h}" alt="{a}" loading="lazy" decoding="async">'.format(
        R=R, s=s, w=w, h=h, a=e(alt))

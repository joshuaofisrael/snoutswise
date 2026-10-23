"""AI generated, photo style images (made 23 Oct 2026 with the Grok Bot image tool for SnoutsWise).
No real people, no text in the images. Every figure carries an honest 'AI generated image' caption."""
import html
e = lambda s: html.escape(s, quote=True)
W, H = 1280, 720
AI = {
    "blog/do-dogs-recognize-themselves-in-mirror.html": ("ai-dog-mirror", "A golden retriever sitting on a rug in a bright room, looking at its own reflection in a tall floor mirror"),
    "blog/why-do-dogs-wag-their-tails.html": ("ai-dog-tail-wag", "A black and white border collie running across a park lawn with its tail in mid wag"),
    "blog/how-do-dogs-drink-water.html": ("ai-dog-drinking", "A yellow Labrador lapping water from a steel bowl, with its tongue curled and droplets splashing"),
    "blog/do-dogs-understand-pointing.html": ("ai-dog-attention", "An attentive beagle sitting in a sunny garden with its gaze fixed on something just outside the frame"),
    "blog/can-dogs-smell-fear.html": ("ai-dog-sniffing", "A black Labrador in a meadow at golden hour with its nose raised, sniffing the air"),
    "blog/index.html": ("ai-dog-living-room", "A shaggy terrier mix lying on a woven rug in a sunlit living room and looking at the camera"),
    "faq.html": ("ai-dog-head-tilt", "A Jack Russell terrier tilting its head in curiosity against a soft green background"),
    "glossary.html": ("ai-dog-eye-closeup", "Close up of a dog's amber eye, ear and fur texture"),
    "research/index.html": ("ai-dog-study", "A focused border collie sitting calmly on a plain mat in a bright room"),
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

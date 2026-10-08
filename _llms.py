import os

EDU = """
## Teachers and research
- [Dog science for teachers]({u}teachers/): free printable worksheets and fact sheets with answer keys, lesson ideas by grade band (NGSS K-LS1-1, 3-LS3-1, 4-LS1-2, MS-LS4-5), vocabulary and classroom games; no ads, no sign up
- [Worksheet: What does a dog need? (K to 2)]({u}teachers/dog-needs-worksheet.html)
- [Fact sheet: Dog senses and body language (grades 3 to 5)]({u}teachers/dog-senses-fact-sheet.html)
- [Worksheet: Traits, breeds and selective breeding (grades 3 to 8)]({u}teachers/dog-traits-worksheet.html)
- [Research behind SnoutsWise]({u}research/): peer reviewed papers with DOIs and veterinary guidelines used across the site
"""


def text(u, name, legal):
    return _text(u, name, legal).replace("\n## Blog\n", ("" if os.environ.get("SW_NO_EDU") else EDU.format(u=u)) + "\n## Blog\n", 1)


def _text(u, name, legal):
    return f"""# {name}

> {name} is a free, independent, sourced guide for dog owners. It explains dog breed groups (AKC and Royal Kennel Club), everyday care, health basics such as normal vital signs and vaccine schedules, reward based training and dog behavior, and offers a searchable table of foods dogs can and cannot eat, a science based dog age calculator and a chocolate dose estimator. Every page lists its veterinary, welfare or kennel club sources. {name} is a brand of {legal}, which owns and operates the site.

The content is general education, not veterinary advice; readers are told to contact a vet for individual dogs and emergencies.

## Guides
- [Dog breeds and breed groups]({u}breeds.html): the seven AKC groups and seven Royal Kennel Club groups compared, and a checklist for choosing a breed
- [Dog care basics]({u}care.html): feeding, healthy weight, exercise, tooth brushing, grooming, UK microchip law and heatstroke first aid
- [Dog health basics]({u}health.html): normal temperature, heart and breathing rates, core vaccines and booster intervals, emergency warning signs, poisoning
- [Dog training]({u}training.html): why vets recommend reward based training, how markers, luring and shaping work, first skills, tools to avoid
- [Dog behavior]({u}behavior.html): stress signals, puppy socialization, the dominance myth and a general approach to problem behavior
- [Dog FAQ]({u}faq.html): short sourced answers to common dog questions
- [Dog glossary]({u}glossary.html): plain English definitions of dog care, health and training terms

## Tools
- [Can dogs eat this? food table]({u}can-dogs-eat.html): searchable verdicts (toxic, caution, safe in moderation) with reasons, sources and what to do if eaten for about 70 foods
  - Categories: [Sweets and snacks]({u}can-dogs-eat.html#sweets-and-snacks), [Drinks]({u}can-dogs-eat.html#drinks), [Fruit]({u}can-dogs-eat.html#fruit), [Vegetables]({u}can-dogs-eat.html#vegetables), [Nuts and seeds]({u}can-dogs-eat.html#nuts-and-seeds), [Meat, fish and eggs]({u}can-dogs-eat.html#meat-fish-and-eggs), [Dairy]({u}can-dogs-eat.html#dairy), [Grains and baking]({u}can-dogs-eat.html#grains-and-baking)
- [Dog age calculator]({u}dog-age-calculator.html): dog years to human years using human age = 16 ln(dog age) + 31 (Wang et al., Cell Systems 2020), with a table and limitations
- [Chocolate dose estimator]({u}blog/dog-ate-chocolate.html): methylxanthine dose by chocolate type and dog weight, using Merck Veterinary Manual figures

## Games
- [Dog games hub]({u}games/): three free original games, no sign up, no ads, no cookies
- [Snack or Nope?]({u}games/snack-or-nope/): sort people foods into Safe, Caution or Toxic for dogs, with sources
- [Wag Signals]({u}games/wag-signals/): dog body language quiz based on RSPCA and ASPCApro guidance
- [Fetch Spotter]({u}games/fetch-spotter/): fetch timing game teaching which ball colors dogs see best (AKC)

## Blog
- [Can dogs see color? Yes, mostly blues and yellows]({u}blog/can-dogs-see-color.html)
- [My dog ate chocolate: how much is dangerous?]({u}blog/dog-ate-chocolate.html)
- [The puppy socialization window: when it closes and what to do]({u}blog/puppy-socialization-window.html)
- [How often do dogs need vaccines? Core and non core vaccines explained]({u}blog/dog-vaccine-schedule.html)
- [Is the "alpha dog" idea true? What the research says about dominance]({u}blog/alpha-dog-myth.html)
- [Is my dog overweight? How to use the 9 point body condition score]({u}blog/is-my-dog-overweight.html)

## Optional
- [About]({u}about.html): who operates the site and how content is researched and sourced
- [Contact]({u}contact.html): email joshuaofisrael@gmail.com or use the contact form
- [Privacy]({u}privacy.html): data controller Joshua Israel Ventures LLC; hosting logs, Google Fonts and the FormSubmit contact form only
- [Terms of use]({u}terms.html): Joshua Israel Ventures LLC is the contracting party; general information only; Florida law
- [Photo credits]({u}credits/): source, author and licence for every photo (Wikimedia Commons, CC BY, CC BY-SA, public domain)
- [Disclaimer]({u}disclaimer.html): not veterinary advice, emergency contacts, no affiliate or advertising links
"""

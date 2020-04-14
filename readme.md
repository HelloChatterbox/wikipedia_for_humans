# Wikipedia for humans

Parsing wikipedia is a mess, not anymore

## Install

```bash
pip install wikipedia_for_humans
```

## Usage

For humans / voice assistants / chatbots

```python
import wikipedia_for_humans

# ask - search paragraphs
answer = wikipedia_for_humans.summary("dog")

"""
The dog (Canis familiaris when considered a distinct species or 
Canis lupus familiaris when considered a subspecies of the wolf) is a 
member of the genus Canis (canines), which forms part of the wolf-like canids, 
and is the most widely abundant terrestrial carnivore. The dog and the 
extant (...) """

answer = wikipedia_for_humans.ask_about("lifespan", "dog")

"""
In 2013, a study found that mixed breeds live on average 1.2 years longer 
than pure breeds, and that increasing body-weight was negatively correlated 
with longevity .The typical lifespan of dogs varies widely among breeds, but 
for most the median longevity, the age at which half the dogs in a population
 have died and half are still alive, ranges from 10 to 13 years. Individual
  dogs may live well beyond the median of their breed.
"""


answer = wikipedia_for_humans.ask_about("wolf", "dog")
"""
'Although dogs are the most abundant and widely distributed terrestrial '
 'carnivores, the potential of feral and free-ranging dogs to compete with '
 'other large carnivores is limited by their strong association with humans. '
 'For example, a review of the studies in the competitive effects of dogs on '
 'sympatric carnivores did not mention any research on competition between '
 'dogs and wolves. Although wolves are known to kill dogs, they tend to live '
 'in pairs or in small packs in areas where they are highly persecuted, giving '
 'them a disadvantage facing large dog groups.Wolves kill dogs wherever they '
 'are found together. One study reported that in Wisconsin in 1999 more '
 'compensation had been paid for losses due to wolves taking dogs than for '
 'wolves taking livestock. In Wisconsin wolves will often kill hunting dogs, '
 "possibly because the dogs are in the wolf's territory. (...)
 """

# tldr - search sentences
answer = wikipedia_for_humans.tldr("dog")
"""
The dog  is a member of the genus Canis , which forms part of the wolf-like canids, and is the most widely abundant terrestrial carnivore
"""

answer = wikipedia_for_humans.tldr_about("lifespan", "dog")
"""
the heavier the dog the shorter its lifespan
"""

answer = wikipedia_for_humans.tldr_about("wolf", "dog")
"""
The dog and the extant gray wolf are sister taxa, as modern wolves are not closely related to the population of wolves that was first domesticated
"""
```

parsing content

```python
import wikipedia_for_humans

# searching pages
pages = wikipedia_for_humans.search_pages("dogs", 5)

for page_name in pages:
    page = wikipedia_for_humans.get_page(page_name)
    print(page["title"], ":", page["summary"][:60])

# search in page content
search_term = "wolf"
page_name = "dog"
best_paragraph, score = wikipedia_for_humans.search_in_page(search_term,
                                                            page_name)
best_sentence, score = wikipedia_for_humans.search_in_page(search_term,
                                                           page_name,
                                                           paragraphs=False)

print("### Sentence level scores for", search_term)
for sentence, score in wikipedia_for_humans.search_sentences(search_term,
                                                             page_name):
    print(score, sentence)

"""
### Sentence level scores for wolf
0.5738636363636364 The dog and the extant gray wolf are sister taxa, as modern wolves are not closely related to the population of wolves that was first domesticated
0.5510204081632654 A strategy has been reported in Russia where one wolf lures a dog into heavy brush where another wolf waits in ambush
0.4123711340206186 The temporalis muscle that closes the jaws is more robust in wolves
0.3861003861003861 Although the numbers of dogs killed each year are relatively low, it induces a fear of wolves entering villages and farmyards to take dogs, and losses of dogs to wolves has led to demands for more liberal wolf hunting regulations
0.38095238095238093 The teeth of gray wolves are also proportionately larger than those of dogs
0.37974683544303794 Wolves kill dogs wherever they are found together
0.356687898089172 The paws of a dog are half the size of those of a wolf, and their tails tend to curl upwards, another trait not found in wolves
0.3409090909090909 One study reported that in Wisconsin in 1999 more compensation had been paid for losses due to wolves taking dogs than for wolves taking livestock
0.33898305084745767 Dogs generally have brown eyes and wolves almost always have amber or light colored eyes
0.33834586466165406 In Wisconsin wolves will often kill hunting dogs, possibly because the dogs are in the wolf's territory
0.30612244897959184 Dogs generally show reduced fear and aggression compared with wolves
0.3007518796992481 Wolves do not have dewclaws on their back legs, unless there has been admixture with dogs that had them
0.29285714285714287 He classified the domestic dog as Canis familiaris, and on the next page he classified the wolf as Canis lupus
0.2631578947368421 Domesticated dogs are clearly distinguishable from wolves by starch gel electrophoresis of red blood cell acid phosphatase
0.25974025974025977 Most dogs lack a functioning pre-caudal gland and enter estrus twice yearly, unlike gray wolves which only do so once a year
0.2484472049689441 This has been made more complicated by the recent proposal that an initial wolf population split into East and West Eurasian groups
0.24691358024691357 The domestication of animals commenced over 15,000 years ago, beginning with the grey wolf (Canis lupus) by nomadic hunter-gatherers
0.22388059701492535 In 2016, a study found that there were only 11 fixed genes that showed variation between wolves and dogs
0.22043010752688172 Linnaeus considered the dog to be a separate species from the wolf because of its cauda recurvata - its upturning tail which is not found in any other canid
0.21505376344086022 Domestic dogs inherited complex behaviors, such as bite inhibition, from their wolf ancestors, which would have been pack hunters with complex body language
0.2061855670103093 Despite their close genetic relationship and the ability to inter-breed, there are a number of diagnostic features to distinguish the gray wolves from domestic dogs
"""

print("### Paragraph level scores for", search_term)
for paragraph, score in wikipedia_for_humans.search_paragraphs(search_term,
                                                               page_name):
    print(score, paragraph)

"""
### Paragraph level scores for wolf
0.2725190839694656
 'Although dogs are the most abundant and widely distributed terrestrial '
 'carnivores, the potential of feral and free-ranging dogs to compete with '
 'other large carnivores is limited by their strong association with humans. '
 'For example, a review of the studies in the competitive effects of dogs on '
 'sympatric carnivores did not mention any research on competition between '
 'dogs and wolves. Although wolves are known to kill dogs, they tend to live '
 'in pairs or in small packs in areas where they are highly persecuted, giving '
 'them a disadvantage facing large dog groups.Wolves kill dogs wherever they '
 'are found together. (...)
 
0.19205298013245026
 "The origin of the domestic dog includes the dog's evolutionary divergence "
 'from the wolf, its domestication, and its development into dog types and dog '
 'breeds. The dog is a member of the genus Canis, which forms part of the '
 'wolf-like canids, and was the first species and the only large carnivore to '
 'have been domesticated. The dog and the extant gray wolf are sister taxa, as '
 'modern wolves are not closely related to the population of wolves that was '
 'first domesticated.The genetic divergence between dogs and wolves occurred '
 'between 40,000–20,000 years ago, (...)
"""

```

page disambiguation

```python
import wikipedia_for_humans

page = "Mercury"

# automatic disambiguation in all "human" methods should pick most common usage
answer = wikipedia_for_humans.tldr(page)
answer = wikipedia_for_humans.tldr_about("health", page)


# manually handle disambiguation pages
# NOTE: new_search_term is not guaranteed to be a valid page name
new_search_term, score = wikipedia_for_humans.disambiguate(page)
print(new_search_term, ":", wikipedia_for_humans.tldr(new_search_term))
"""
Mercury (element) : Mercury is a chemical element with the symbol Hg and atomic number 80 
"""

new_search_term, score = wikipedia_for_humans.disambiguate(page, "planet")
print(new_search_term, ":", wikipedia_for_humans.tldr(new_search_term))
"""
Mercury (planet) : Mercury is the smallest and innermost planet in the Solar System 
"""

new_search_term, score = wikipedia_for_humans.disambiguate(page, "god")
print(new_search_term, ":", wikipedia_for_humans.tldr(new_search_term))
"""
Mercury (mythology) : Mercury is a major god in Roman religion and mythology, being one of the 12 Dii Consentes within the ancient Roman pantheon 
"""

print("######## Top Candidate Pages")
# inspect disambiguation results
for candidate, score in wikipedia_for_humans.disambiguate(page, all_matches=True):
    print(score, candidate)

"""
0.5 Mercury (element), a metallic chemical element with the symbol 'Hg'
0.5 Mercury (mythology), a Roman god
0.5 Mercury (planet), the nearest to the Sun
"""


print("######## All Candidate Pages matching {films}")
for candidate, score in wikipedia_for_humans.disambiguate(page, "films", all_matches=True):
    if score >= 0.4:
        print(score, candidate)

"""
1.0 Mercury (film)
0.8 A fictional Minnesota town in the 2011 film Young Adult
0.4 The Mercury Cinema
"""
```

## Motivation

Searching wikipedia by voice should be easy

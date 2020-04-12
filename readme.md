# Wikipedia for humans

Parsing wikipedia is a mess, not anymore

## Install

```bash
pip install wikipedia_for_humans
```

## Usage

For voice assistants / chatbots

```python
import wikipedia_for_humans

# summary
answer = wikipedia_for_humans.summary("dog")

"""
The dog (Canis familiaris when considered a distinct species or 
Canis lupus familiaris when considered a subspecies of the wolf) is a 
member of the genus Canis (canines), which forms part of the wolf-like canids, 
and is the most widely abundant terrestrial carnivore. The dog and the 
extant (...) """

# search inside a page - search best paragraph
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
The origin of the domestic dog includes the dog's evolutionary divergence 
from the wolf, its domestication, and its development into dog types and dog 
breeds. The dog is a member of the genus Canis, which forms part of the
 wolf-like canids, and was the first species and the only large carnivore 
 to have been domesticated.  (...)"""

# tldr
answer = wikipedia_for_humans.tldr("dog")

"""
The dog  is a member of the genus Canis , which forms part of the wolf-like canids, and is the most widely abundant terrestrial carnivore
"""

# tldr search - search best sentence
answer = wikipedia_for_humans.tldr_about("lifespan", "dog")

"""
the heavier the dog the shorter its lifespan
"""

answer = wikipedia_for_humans.tldr_about("wolf", "dog")

"""
The relationship between the presence of a dog and success in the hunt is often mentioned as a primary reason for the domestication of the wolf, and a 2004 study of hunter groups with and without a dog gives quantitative support to the hypothesis that the benefits of cooperative hunting was an important factor in wolf domestication"""
```

parsing content

```python
import wikipedia_for_humans


# searching
search_results = wikipedia_for_humans.search_wikipedia("dogs", 5)

for page_name in search_results["pages"]:
    page = wikipedia_for_humans.get_page(page_name)
    print(page["title"], ":", page["summary"][:60])


# search in page content
search_term = "wolf"
page_name = "dog"
answer, conf = wikipedia_for_humans.search_in_page(search_term, page_name)

for answer, conf in wikipedia_for_humans.search_in_page(search_term, page_name,
                                          all_matches=True):
    print(conf, answer[:40])

```

## Motivation

Searching wikipedia by voice should be easy

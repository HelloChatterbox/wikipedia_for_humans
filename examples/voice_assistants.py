import wikipedia_for_humans

# summary
answer = wikipedia_for_humans.summary("dog")

"""
The dog (Canis familiaris when considered a distinct species or 
Canis lupus familiaris when considered a subspecies of the wolf) is a 
member of the genus Canis (canines), which forms part of the wolf-like canids, 
and is the most widely abundant terrestrial carnivore. The dog and the 
extant (...) """

# search inside a page
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

# tldr
answer = wikipedia_for_humans.tldr("dog")
"""
The dog  is a member of the genus Canis , which forms part of the wolf-like canids, and is the most widely abundant terrestrial carnivore
"""

# tldr search
answer = wikipedia_for_humans.tldr_about("lifespan", "dog")
"""
the heavier the dog the shorter its lifespan
"""

answer = wikipedia_for_humans.tldr_about("wolf", "dog")
"""
The dog and the extant gray wolf are sister taxa, as modern wolves are not closely related to the population of wolves that was first domesticated
"""
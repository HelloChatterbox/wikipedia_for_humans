import wikipedia_for_humans

# searching
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
    if score > 0.5:
        print(score, sentence)

"""
### Sentence level scores for wolf
0.9666666666666668 The relationship between the presence of a dog and success in the hunt is often mentioned as a primary reason for the domestication of the wolf, and a 2004 study of hunter groups with and without a dog gives quantitative support to the hypothesis that the benefits of cooperative hunting was an important factor in wolf domestication
0.7189655172413792 A strategy has been reported in Russia where one wolf lures a dog into heavy brush where another wolf waits in ambush
0.6500000000000001 The origin of the domestic dog includes the dog's evolutionary divergence from the wolf, its domestication, and its development into dog types and dog breeds
0.6333333333333333 2 years, but several breeds, including miniature bull terriers, bloodhounds, and Irish wolfhounds are nearly as short-lived, with median longevities of 6 to 7 years
0.5722222222222222 The paws of a dog are half the size of those of a wolf, and their tails tend to curl upwards, another trait not found in wolves
0.5666666666666667 In 1999, a study of mitochondrial DNA indicated that the domestic dog may have originated from multiple grey wolf populations, with the dingo and New Guinea singing dog "breeds" having developed at a time when human populations were more isolated from each other
0.55 The dog is a member of the genus Canis, which forms part of the wolf-like canids, and was the first species and the only large carnivore to have been domesticated
0.55 The dog and the extant gray wolf are sister taxa, as modern wolves are not closely related to the population of wolves that was first domesticated
0.55 In 2020, a literature review of canid domestication stated that modern dogs were not descended from the same Canis lineage as modern wolves, and proposes that dogs may be descended from a Pleistocene wolf closer in size to a village dog
0.55 In 1957, the dog Laika became the first animal to be launched into Earth orbit, aboard the Soviets' Sputnik 2; she died during the flight
0.5166666666666666 He classified the domestic dog as Canis familiaris, and on the next page he classified the wolf as Canis lupus
0.5166666666666666 Linnaeus considered the dog to be a separate species from the wolf because of its cauda recurvata - its upturning tail which is not found in any other canid
"""


print("### Paragraph level scores for", search_term)
for paragraph, score in wikipedia_for_humans.search_paragraphs(search_term,
                                                               page_name):
    if score > 0.5:
        print(score, paragraph)

"""
### Paragraph level scores for wolf
1.0 "The origin of the domestic dog includes the dog's evolutionary divergence "
 'from the wolf, its domestication, and its development into dog types and dog '
 'breeds. The dog is a member of the genus Canis, which forms part of the '
 'wolf-like canids, and was the first species and the only large carnivore to '
 'have been domesticated. The dog and the extant gray wolf are sister taxa, as '
 'modern wolves are not closely related to the population of wolves that was '
 'first domesticated.The genetic divergence between dogs and wolves occurred '
 'between 40,000–20,000 years ago, just before or during the Last Glacial '
 'Maximum. This timespan represents the upper time-limit for the commencement '
 'of domestication because it is the time of divergence and not the time of '
 'domestication, which occurred later. The domestication of animals commenced '
 'over 15,000 years ago, beginning with the grey wolf (Canis lupus) by nomadic '
 'hunter-gatherers. The archaeological record and genetic analysis show the '
 'remains of the Bonn–Oberkassel dog buried beside humans 14,200 years ago to '
 'be the first undisputed dog, with disputed remains occurring 36,000 years '
 'ago. The domestication of the dog predates agriculture. It was not until '
 '11,000 years ago that people living in the Near East entered into '
 'relationships with wild populations of aurochs, boar, sheep, and goats.Where '
 'the domestication of the dog took place remains debated, with the most '
 'plausible proposals spanning Western Europe, Central Asia and East Asia. '
 'This has been made more complicated by the recent proposal that an initial '
 'wolf population split into East and West Eurasian groups. These two groups, '
 'before going extinct, were domesticated independently into two distinct dog '
 'populations between 14,000 and 6,400 years ago. The Western Eurasian dog '
 'population was gradually and partially replaced by East Asian dogs '
 'introduced by humans at least 6,400 years ago. This proposal is also '
 'debated.In 2020, a literature review of canid domestication stated that '
 'modern dogs were not descended from the same Canis lineage as modern wolves, '
 'and proposes that dogs may be descended from a Pleistocene wolf closer in '
 'size to a village dog.'
"""
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
 'are found together. One study reported that in Wisconsin in 1999 more '
 'compensation had been paid for losses due to wolves taking dogs than for '
 'wolves taking livestock. In Wisconsin wolves will often kill hunting dogs, '
 "possibly because the dogs are in the wolf's territory. A strategy has been "
 'reported in Russia where one wolf lures a dog into heavy brush where another '
 'wolf waits in ambush. In some instances, wolves have displayed an '
 'uncharacteristic fearlessness of humans and buildings when attacking dogs, '
 'to the extent that they have to be beaten off or killed. Although the '
 'numbers of dogs killed each year are relatively low, it induces a fear of '
 'wolves entering villages and farmyards to take dogs, and losses of dogs to '
 'wolves has led to demands for more liberal wolf hunting regulations.Coyotes '
 'and big cats have also been known to attack dogs. Leopards in particular are '
 'known to have a predilection for dogs, and have been recorded to kill and '
 'consume them regardless of their size. Tigers in Manchuria, Indochina, '
 'Indonesia, and Malaysia are also reported to kill dogs. Striped hyenas are '
 'known to kill dogs in Turkmenistan, India, and the Caucasus.'
 
0.19205298013245026
 "The origin of the domestic dog includes the dog's evolutionary divergence "
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
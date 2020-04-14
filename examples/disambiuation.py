from wikipedia_for_humans import tldr, disambiguate, tldr_about

page = "Mercury"


# automatic disambiguation in all "human" methods should pick most common usage
answer = tldr(page)
answer = tldr_about("health", page)


# manually handle disambiguation pages
new_search_term, score = disambiguate(page)
print(new_search_term, ":", tldr(new_search_term))
"""
Mercury (element) : Mercury is a chemical element with the symbol Hg and atomic number 80 
"""

new_search_term, score = disambiguate(page, "planet")
print(new_search_term, ":", tldr(new_search_term))
"""
Mercury (planet) : Mercury is the smallest and innermost planet in the Solar System 
"""

new_search_term, score = disambiguate(page, "god")
print(new_search_term, ":", tldr(new_search_term))
"""
Mercury (mythology) : Mercury is a major god in Roman religion and mythology, being one of the 12 Dii Consentes within the ancient Roman pantheon 
"""

print("######## Top Candidate Pages")
# inspect disambiguation results
for candidate, score in disambiguate(page, all_matches=True):
    print(score, candidate)

"""
0.5 Mercury (element), a metallic chemical element with the symbol 'Hg'
0.5 Mercury (mythology), a Roman god
0.5 Mercury (planet), the nearest to the Sun
"""


print("######## All Candidate Pages matching {films}")
for candidate, score in disambiguate(page, "films", all_matches=True):
    if score >= 0.4:
        print(score, candidate)

"""
1.0 Mercury (film)
0.8 A fictional Minnesota town in the 2011 film Young Adult
0.4 The Mercury Cinema
"""
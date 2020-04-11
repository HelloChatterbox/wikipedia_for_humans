import wikipedia_for_humans


# searching
pages = wikipedia_for_humans.search_wikipedia("dogs", 5)

for page_name in pages["pages"]:
    page = wikipedia_for_humans.get_page(page_name)
    print(page["title"], ":", page["summary"][:60])


# search in page content
search_term = "wolf"
page_name = "dog"
answer, conf = wikipedia_for_humans.search_in_page(search_term, page_name)
print(answer)

for answer, conf in wikipedia_for_humans.search_in_page(search_term, page_name,
                                          all_matches=True):
    print(conf, answer[:40])

# always returns a dict or None
pages = wikipedia_for_humans.search_wikipedia("jthsgrfd")
assert pages is None
sections = wikipedia_for_humans.get_sections("dog")
assert isinstance(sections, dict)
page = wikipedia_for_humans.get_page("rdfhgjklhygtf")
assert page is None


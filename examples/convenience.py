import wikipedia_for_humans
from wikipedia_for_humans import short_answer, short_summary, tldr
from wikipedia_for_humans import best_paragraph, best_sentence, \
    ask_about, tldr_about
from wikipedia_for_humans import summary, long_answer

# Convenience aliases, use whatever feels right in your code

page = "mercury god"
assert short_answer(page) == tldr(page) == short_summary(page)
assert long_answer(page) == summary(page)

query = "gaul"
assert best_paragraph(query, page) == ask_about(query, page)
assert best_sentence(query, page) == tldr_about(query, page)


# always returns a dict or None
pages = wikipedia_for_humans.search_wikipedia("jthsgrfd")
assert pages is None
sections = wikipedia_for_humans.get_sections("dog")
assert isinstance(sections, dict)
page = wikipedia_for_humans.get_page("rdfhgjklhygtf")
assert page is None

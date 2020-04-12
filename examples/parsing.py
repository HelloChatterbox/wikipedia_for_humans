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

for sentence, score in wikipedia_for_humans.search_sentences(search_term,
                                                             page_name):
    if score > 0.5:
        print(score, sentence[:40])

for paragraph, score in wikipedia_for_humans.search_paragraphs(search_term,
                                                               page_name):
    if score > 0.5:
        print(score, paragraph[:40])

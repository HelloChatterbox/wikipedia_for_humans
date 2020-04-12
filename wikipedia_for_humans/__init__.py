import wikipediaapi
import requests
import re
from wikipedia_for_humans.util import match_one, fuzzy_match, split_sentences


def _get_page(page_name, lang="en"):
    wiki_wiki = wikipediaapi.Wikipedia(lang)
    page_py = wiki_wiki.page(page_name)
    return page_py


def _get_summary(page_name, lang="en"):
    if isinstance(page_name, str):
        page = _get_page(page_name, lang)
    else:
        # TODO confirm page is page object
        page = page_name
    return page.summary


def _get_title(page_name, lang="en"):
    if isinstance(page_name, str):
        page = _get_page(page_name, lang)
    else:
        # TODO confirm page is page object
        page = page_name
    return page.title


def _get_text(page_name, lang="en"):
    if isinstance(page_name, str):
        page = _get_page(page_name, lang)
    else:
        # TODO confirm page is page object
        page = page_name
    return page.text


def get_sections(page_name, lang="en"):
    if isinstance(page_name, str):
        page = _get_page(page_name, lang)
    else:
        # TODO confirm page is page object
        page = page_name
    if page is None:
        return None

    n = {}

    def parse_sections(sections, level=0):
        for s in sections:
            parse_sections(s.sections, level + 1)
            n[s.title] = s.text

    parse_sections(page.sections)
    return n


def get_page(page_name, lang="en"):
    page = _get_page(page_name, lang)
    if page.exists():
        return {"title": _get_title(page),
                "summary": _get_summary(page),
                "sections": get_sections(page),
                "text": _get_text(page)}
    return None


def search_wikipedia(query, limit=3):
    params = {"search": query,
              "format": "json",
              "namespace": 0,
              "limit": limit,
              "formatversion": 2,
              "action": "opensearch"}
    r = requests.get("https://en.wikipedia.org/w/api.php", params=params)
    _, results, _, urls = r.json()
    if len(results) == 0:
        return None
    return {"pages": results, "urls": urls}


def summary(query, lang="en"):
    results = search_wikipedia(query, limit=1)
    if results is None:
        return ""
    page = _get_page(results["pages"][0], lang)
    answer = _get_summary(page, lang)
    return answer


def short_answer(query, lang="en"):
    answer = summary(query, lang)
    return re.sub(r'\([^)]*\)', '', answer.split(".")[0])


def search_in_page(query, page_name, lang="en", all_matches=False,
                   thresh=0.15, paragraphs=True):
    sections = get_sections(page_name, lang)

    # search text inside sections
    candidates = []
    scores = []
    for sec in sections:
        # total half assed scoring metric #0
        # if query is a section title boost score
        base_score = fuzzy_match(sec.lower(), query.lower())
        for c in split_sentences(sections[sec], paragraphs):
            scores.append(base_score)
            candidates.append(c)

    query = query.strip()
    for idx, c in enumerate(candidates):
        c = c.lower()
        score = scores[idx]
        for word in c.split():
            # total half assed scoring metric #1
            # each time query appears in sentence/paragraph boost score
            if query.lower() in word:
                # magic numbers are bad
                score += 0.16
            # total half assed scoring metric #2
            # each time page name appears in sentence/paragraph boost score
            if word in page_name.lower():
                # magic numbers are bad
                score += 0.05
        scores[idx] = score


    best_conf = max(scores)
    best = candidates[scores.index(best_conf)]
    # this is a fake percent, sorry folks
    scores = [s if s < 0.9 else 0.93 for s in scores]
    if best_conf > 1:
        best_conf = 0.97

    if not all_matches:
        return best, best_conf

    data = []
    for idx, c in enumerate(candidates):
        if scores[idx] >= thresh:
            data.append((c, scores[idx]))
    return data


def ask_about(query, page_name, lang="en"):
    answer, conf = search_in_page(query, page_name, lang, all_matches=False)
    if conf < 0.3:
        return None
    return re.sub(r'\([^)]*\)', '', answer.split("\n")[0])


def tldr_about(query, page_name, lang="en"):
    answer, conf = search_in_page(query, page_name, lang, all_matches=False,
                                  paragraphs=False)
    if conf < 0.3:
        return None
    return re.sub(r'\([^)]*\)', '', answer.split("\n")[0])


def tldr(query, lang="en"):
    return short_answer(query, lang)

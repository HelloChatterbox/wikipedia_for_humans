import wikipediaapi
import requests
import re
from wikipedia_for_humans.util import match_one, fuzzy_match


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


def search_in_page(query, page_name, lang="en", all_matches=False, thresh=0.2):
    sections = get_sections(page_name, lang)

    # search text inside sections
    candidates = []
    scores = []
    for sec in sections:
        base_score = fuzzy_match(sec, query)

        for c in sections[sec].split("\n"):
            c = c.strip()
            if c:
                scores.append(base_score)
                candidates.append(c)

    # prune and score
    for idx, c in enumerate(candidates):
        score = scores[idx] + fuzzy_match(c, query)

        for word in c.split():
            if query.rstrip("s") in word:
                score += 0.1
        scores[idx] = score

    best_conf = max(scores)
    best = candidates[scores.index(best_conf)]

    if not all_matches:
        return best, best_conf

    # fake percent
    scores = [s if s < 0.9 else 0.91 for s in scores ]

    data = []
    for idx, c in enumerate(candidates):
        if scores[idx] > thresh:
            data.append((c, scores[idx]))
    return data


def ask_about(query, page_name, lang="en"):
    answer, conf = search_in_page(query, page_name, lang, all_matches=False)
    if conf < 0.5:
        return None
    return re.sub(r'\([^)]*\)', '', answer.split("\n")[0])


def tldr(query, lang="en"):
    return short_answer(query, lang)

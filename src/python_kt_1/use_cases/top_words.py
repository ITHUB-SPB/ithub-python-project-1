from typing import Literal
from ..core.preprocess import filter_stopwords, clean_words
from python_kt_1.core.tokenize import tokenize_text


def _count_words(words: list) -> dict:
    """Подсчет количества вхождений каждого слова."""

    counter = {}
    for word in words:
        if word:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    return counter


def _sort_by_count(item: tuple) -> int:
    """Сортирует по количеству вхождений, от большего к меньшему."""

    return -item[1]


def _apply_stemming(words: list) -> list:
    """Стемминг средствами nltk."""

    from nltk.stem.snowball import SnowballStemmer
    stemmer = SnowballStemmer("russian")
    result = []
    for word in words:
        if word:
            result.append(stemmer.stem(word))
    return result


def _apply_lemmatization(words: list) -> list:
    """Лемматизация средствами spaCy."""

    import spacy
    nlp = spacy.load("ru_core_news_sm")
    text = " ".join(words)
    doc = nlp(text)
    result = []
    for token in doc:
        if token.text.strip():
            result.append(token.lemma_)
    return result


def _filter_by_pos(words: list, pos_tags: list) -> list:
    """Фильтрация слов по частям речи средствами spaCy."""

    import spacy
    nlp = spacy.load("ru_core_news_sm")
    text = " ".join(words)
    doc = nlp(text)
    result = []
    for token in doc:
        if token.pos_ in pos_tags and token.text.strip():
            result.append(token.lemma_)
    return result


def top_words(
    text: str,
    normalize_mode: Literal["stemming", "lemmatization"] = "stemming",
    pos: list = ["__all__"]
) -> list:
    """Подсчет топ-N-важных слов.

    Получает текст, разбивает на слова, убирает пунктуацию и пробельные символы,
    фильтрует стоп-слова, нормализует (либо стемминг, либо лемматизация),
    подсчитывает и возвращает список кортежей для топ-N-важных слов.
    """

    initial_words = tokenize_text(text)["words"]
    words_after_clean = clean_words(initial_words)
    words_after_filter = filter_stopwords(words_after_clean)

    if pos != ["__all__"]:
        words_after_filter = _filter_by_pos(words_after_filter, pos)
    elif normalize_mode == "stemming":
        words_after_filter = _apply_stemming(words_after_filter)
    elif normalize_mode == "lemmatization":
        words_after_filter = _apply_lemmatization(words_after_filter)

    return sorted(_count_words(words_after_filter).items(), key=_sort_by_count)

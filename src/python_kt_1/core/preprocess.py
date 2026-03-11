import pathlib
from typing import Set
from string import punctuation, whitespace

def _load_stopwords() -> Set[str]:
    path_to_file = pathlib.Path() / "src" / "python_kt_1" / "core" / "stopwords.txt"
    with open(path_to_file, encoding="utf-8") as f:
        return set(f.read().splitlines())


def filter_stopwords(words: list[str]) -> list[str]:
    stopwords_lower = _load_stopwords()
    stopwords_title = set(stopword.title() for stopword in stopwords_lower)
    stopwords_upper = set(stopword.upper() for stopword in stopwords_lower)

# Объединяем все варианты регистров
    all_stopwords = set(stopwords_lower) | stopwords_title | stopwords_upper

# Фильтруем слова
    return [
        word for word in words
        if word and word not in all_stopwords  # слово не пустое и не стоп-слово
    ]

def clean_words(words: list[str]) -> list[str]:
    return [word.strip(punctuation + whitespace + "—«»…") for word in words]
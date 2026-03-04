import pathlib
import re
from typing import Set
from string import punctuation, whitespace
import spacy
from nltk.stem.snowball import SnowballStemmer #нормальзация текста 

def _load_stopwords() -> Set[str]:
    path_to_file = pathlib.Path(__file__).parent / "stopwords.txt"
    if not path_to_file.exists():
        return set()
    with open(path_to_file, encoding="utf-8") as f:
        return set(f.read().splitlines())

def filter_stopwords(words: list[str]) -> list[str]:
    stopwords_lower = _load_stopwords()
    return [
        word for word in words 
        if word.lower() not in stopwords_lower and len(word) > 1
    ]

def clean_words(words: list[str]) -> list[str]:
    return [word.strip(punctuation + whitespace + "—«»…") for word in words]

def stem_words(words: list[str]) -> list[str]:
    stemmer = SnowballStemmer("russian")
    return [stemmer.stem(word) for word in words]

def lemmatize_words(words: list[str]) -> list[str]:
    try:
        nlp = spacy.load("ru_core_news_sm", disable=["parser", "ner"])
    except OSError:
        return words 
    doc = nlp(" ".join(words))
    return [token.lemma_ for token in doc]

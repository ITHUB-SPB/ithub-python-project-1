# TODO
# DONE tokenize_text_by_words 
# очистка от знаков препинания
# DONE фильтр по стоп-словам 
from string import punctuation, whitespace
from typing import Iterable

from .tokenize import tokenize_text_by_words


def preprocess_text(text: str) -> Iterable[str]:
    """
    Предобработка текста:
    - токенизация по словам
    - фильтр по стоп-словам
    - очистка от знаков препинания.
    Returns:
        Список слов, используемых в тексте
    """
    words = tokenize_text_by_words(text)

    for index in range(len(words)):
        words[index] = words[index].strip(punctuation + whitespace + "—«»")

    with open('src\python_kt_1\core\stopwords.txt', encoding="utf-8") as f:
        stop_words = f.read().splitlines()

    words = [w.upper() for w in words if w and not w.lower() in stop_words]

    return words

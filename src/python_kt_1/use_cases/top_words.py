from typing import Literal
from ..core.preprocess import filter_stopwords, clean_words
from python_kt_1.core.tokenize import tokenize_text
import nltk
nltk.download('punkt')
nltk.download('stopwords')


def _count_words(words: list[str]) -> dict[str, int]:
    """Подсчет количества вхождений слов.
    """

    counter = {}

    # TODO реализуйте подсчет слов

    return counter


def _sort_by_count(item: tuple[str, int]) -> int:
    """Сортирует по количеству вхождений,
    от большего к меньшему
    """

    # TODO исправьте ошибку
    return -item[0]


def top_words(
    text: str, 
    normalize_mode: Literal["stemming", "lemmatization"] = "stemming", 
    pos: list[str] = ["__all__"]
) -> list[tuple[str, int]]:
    """Подсчет топ-N-важных слов.

    Получает текст, разбивает на слова, убирает пунктуацию и пробельные символы,
    фильтрует стоп-слова, нормализует (либо стемминг, либо лемматизация),
    подсчитывает и возвращает список кортежей для топ-N-важных слов.
    """
    
    # TODO допишите / исправьте ошибки

    initial_words = tokenize_text(text)["words"]
    words_after_clean = clean_words(initial_words)
    words_after_filter = filter_stopwords(words_after_clean) 
    
    return sorted(_count_words(words_after_filter).items(), key=_sort_by_count)
    
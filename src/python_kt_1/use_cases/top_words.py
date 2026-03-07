from typing import Iterable
import pymorphy3
from nltk import SnowballStemmer
from collections import Counter

morph = pymorphy3.MorphAnalyzer()
def lemmatization_text(words: Iterable[str]) -> Iterable[str]:
    """
    Лемматизация текста."""
    return [morph.parse(word)[0].normal_form for word in words]

stemmer = SnowballStemmer("russian")
def stemming_text(words: Iterable[str]) -> Iterable[str]:
    """
    Стемминг текста.
    """
    return [stemmer.stem(word) for word in words]

def count_words(words: Iterable[str], pos: list[str] = ["__all__"]) -> dict[str, int]:
    """
    Подсчет количества вхождений слов.
    """
    count_words = dict[str, int]()

    for word in words:
        word_pos = morph.parse(word)[0].tag.POS
        if "__all__" not in pos and word_pos not in pos:
            continue
        if word in count_words:
            count_words[word] += 1
        else:
            count_words[word] = 1
    return count_words

def format_top_words(count_words: dict[str, int]) -> str:
    """
    Форматирование результата подсчета слов в строку для вывода.
    """
    sorted_count_words = dict(sorted(count_words.items(), key=lambda item: item[1], reverse=True)[:30])
    return "\n".join([f"{word}: {count}" for word, count in sorted_count_words.items()])

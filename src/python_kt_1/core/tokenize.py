from .types import Tokens
from typing import Iterable
from string import punctuation, whitespace

def tokenize_text_by_words(text:str) -> Iterable[str]:
    """
    Разбиение текста на слова.
    """
    text = text.replace("\n", " ").replace("\r\n", " ")
    words = text.split(" ")
    return words

def tokenize_text(text: str) -> Tokens:
    """Разбиение текста на токены.

    Разбиение текста на токены:
    - параграфы (абзацы),
    - предложения,
    - слова
    """

    # TODO

    return {
        "paragraphs": [],
        "sentences": [],
        "words": tokenize_text_by_words(text),
    }

import re
from .types import Tokens

def _get_words(text: str) -> list[str]:
    """Разбиение на слова (без обработки)
    """

    # TODO: исправьте регулярку
    return re.split(' ', text)


def tokenize_text(text: str) -> Tokens:
    """Разбиение текста на токены.

    Разбиение текста на токены:
    - параграфы (абзацы),
    - предложения,
    - слова
    """

    # TODO допишите функции _get_paragraphs, _get_sentences

    return {
        "paragraphs": [],
        "sentences": [],
        "words": _get_words(text),
    }

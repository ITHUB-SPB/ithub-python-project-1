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

    return {
        "paragraphs": _get_paragraphs(text),
        "sentences": _get_sentences(text),
        "words": _get_words(text),
    }

def _get_paragraphs(text: str) -> list[str]:
    """
    Разбивает текст на параграфы (абзацы).
    
    Args:
        text: исходный текст
        
    Returns:
        список параграфов
    """
    # Разделяем по двум и более переводам строки
    import re
    paragraphs = re.split(r'\n\s*\n', text)

    # Убираем пустые параграфы и лишние пробелы
    paragraphs = [p.strip() for p in paragraphs if p.strip()]

    return paragraphs

def _get_sentences(text: str) -> list[str]:
    """
    Разбивает текст на предложения.
    
    Args:
        text: исходный текст
        
    Returns:
        список предложений
    """
    import re

    # Регулярное выражение для поиска границ предложений
    # Ищем . ! ? за которыми следует пробел или конец строки
    sentence_endings = r'(?<=[.!?])\s+(?=[А-ЯA-Z])|(?<=[.!?])$'

    # Временная замена многоточия
    text = text.replace('...', '###ELLIPSIS###')

    # Разбиваем на предложения
    sentences = re.split(sentence_endings, text)

    # Возвращаем многоточие
    sentences = [s.replace('###ELLIPSIS###', '...') for s in sentences]

    # Очистка и фильтрация
    sentences = [s.strip() for s in sentences if s.strip()]

    return sentences

def _get_words(text: str) -> list[str]:
    """
    Разбивает текст на слова.
    
    Args:
        text: исходный текст
        
    Returns:
        список слов
    """
    import re

    # Приводим к нижнему регистру
    text = text.lower()

    # Удаляем пунктуацию и цифры, оставляем только слова
    # \w+ находит последовательности букв
    words = re.findall(r'\b[а-яёa-z]+\b', text, re.IGNORECASE)

    return words
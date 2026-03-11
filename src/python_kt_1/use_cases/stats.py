import re
import unicodedata
import pathlib

from ..core.types import TextStats, SymbolStats, Tokens, TokensStats


def stats(text: str, pos: bool = False) -> TextStats:
    """Функция для подсчета статистик.

    Args:
        text: текст для расчета статистик
        pos: опция, добавляет аналитику по частям речи

    Returns:
        Статистика, сгруппированная по токенам, символам и,
        опционально, морфологическим характеристикам

        Например, для строки `\tПроверка!\nНовая строка` это
        будет:
        {
            "tokens": {
                "paragraphs": 2,
                "sentences": 2,
                "words": 3,
            },
            "symbols": {
                "alphas": {
                    "quantity": 19,
                    "percent": 82.61
                },
                "digits": {
                    "quantity": 0,
                    "percent": 0.00
                },
                "spaces": {
                    "quantity": 3,
                    "percent": 13.04
                },
                "punctuation": {
                    "quantity": 1,
                    "percent": 4.35
                }
            }
        }

    """

    result = {"tokens": _get_tokens_stats(text), "symbols": _get_symbols_stats(text)}
    if pos:
        result["pos"] = _get_pos_stats(text)
    return result


def _get_symbols_stats(text: str) -> SymbolStats:
    """Посимвольная статистика (количество и процент)."""

    count_alphas = 0
    count_digits = 0
    count_spaces = 0
    count_punctuation = 0

    for symbol in text:
        if symbol.isalpha():
            count_alphas += 1
        elif symbol.isdigit():
            count_digits += 1
        elif unicodedata.category(symbol).startswith('P'):
            count_punctuation += 1
        else:
            count_spaces += 1

    total = len(text)

    def percent(count):
        return round(count / total * 100, 2) if total > 0 else 0.0

    return {
        "alphas":      {"quantity": count_alphas,      "percent": percent(count_alphas)},
        "digits":      {"quantity": count_digits,      "percent": percent(count_digits)},
        "spaces":      {"quantity": count_spaces,      "percent": percent(count_spaces)},
        "punctuation": {"quantity": count_punctuation, "percent": percent(count_punctuation)},
    }


def _get_tokens_stats(text: str) -> TokensStats:
    """Подсчет количества токенов."""
    text = text.strip()

    paragraphs = [p for p in text.split('\n') if p.strip()]
    sentences = [s for s in re.split(r'(?<=[.!?»])\s+', text) if s.strip()]
    words = re.findall(r'\b\w+\b', text)

    return {
        "paragraphs": len(paragraphs),
        "sentences": len(sentences),
        "words": len(words),
    }


def _get_pos_stats(text: str) -> dict:
    """Подсчет pos-аналитики с помощью SpaCy."""

    import spacy
    try:
        nlp = spacy.load("ru_core_news_sm")
    except OSError:
        return {}
    doc = nlp(text)
    counts = {}
    for token in doc:
        pos = token.pos_
        if pos != "SPACE":
            if pos not in counts:
                counts[pos] = 0
            counts[pos] += 1
    return counts

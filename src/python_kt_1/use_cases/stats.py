import re
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

    return {"tokens": _get_tokens_stats(text), "symbols": _get_symbols_stats(text)}


def _get_symbols_stats(text: str) -> SymbolStats:
    """Посимвольная статистика (количество и процент).

    """
    
    count_alphas = 0
    count_digits = 0
    count_spaces = 0
    count_punctuation = 0

    for symbol in text:
        if symbol.isalpha():
            count_alphas += 1
        elif symbol.isdigit():
            count_digits += 1
        elif symbol.isspace():
            count_spaces += 1
        else:
            count_punctuation += 1

    return {
        "alphas": {"quantity": count_alphas, "percent": round(count_alphas / len(text) * 100, 2)},
        "digits": {"quantity": count_digits, "percent": round},
        "spaces": {"quantity": count_spaces, "percent": round(count_spaces / len(text) * 100, 2)},
        "punctuation": {"quantity": count_punctuation, "percent": round(count_punctuation / len(text) * 100, 2)},
    }



def _get_tokens_stats(text: str) -> TokensStats:
    """Подсчет количества токенов."""
    text = text.strip()
    return {
        "paragraphs": len(text.splitlines()),
        "sentences": len(re.split('[.!?]\s+', text)),
        "words": len(re.split('\s+', text)),
    }


def _get_pos_stats(text: str):
    """Подсчет pos-аналитики"""

    return

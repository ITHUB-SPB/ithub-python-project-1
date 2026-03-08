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
    """Посимвольная статистика (количество и процент)."""
    text_length = len(text)
    ix = 0
    punctuation_marks = set('.,!?;:-—()[]{}""\'\'<>…')

    count_alphas = 0
    count_digits = 0
    count_spaces = 0
    count_punctuation = 0

    while ix < text_length:
        curr = text[ix]
        if curr.isdigit():
            count_digits+=1
        elif curr.isspace():
            count_spaces+=1
        elif curr.isalpha():
            count_alphas+=1
        elif curr in punctuation_marks:
            count_punctuation += 1
        ix+=1

    per_alp = round(count_alphas / text_length * 100, 1)
    per_digit = round(count_digits / text_length * 100, 1)
    per_space = round(count_spaces / text_length * 100, 1)
    per_punctuation = round(count_punctuation / text_length * 100, 1)


    return {
        "alphas": {"quantity": count_alphas, "percent":per_alp },
        "digits": {"quantity": count_digits, "percent": per_digit},
        "spaces": {"quantity": count_spaces, "percent":per_space },
        "punctuation": {"quantity": count_punctuation, "percent": per_punctuation},
    }


def _get_tokens_stats(text: str) -> TokensStats:
    """Подсчет количества токенов."""
    text = text.strip()

    return {
        "paragraphs": 0,
        "sentences": 0,
        "words": 0
    }


def _get_pos_stats(text: str):
    """Подсчет pos-аналитики"""

    return

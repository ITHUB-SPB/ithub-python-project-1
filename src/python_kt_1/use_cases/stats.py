import re
import pathlib

from ..core.types import TextStats, SymbolStats, Tokens


def stats(text: str, pos: bool = False) -> TextStats:
    '''Функция для подсчета статистик.

    Args:
        text: текст для расчета статистик 
        pos: опция, добавляет аналитику по частям речи

    Returns:
        Статистика, сгруппированная по токенам, символам и,
        опционально, морфологическим характеристикам, например: [
            { "result": "kitten", "start": 17, "end": 22 },
            { "result": "kitten", "start": 43, "end": 48 }
        ] или [
            { "result": "KG", "start": 5, "end": 6 },
            { "result": "G", "start": 6, "end": 6 },
        ]
    '''
    
    return {
        "tokens": _get_tokens_stats(text),
        "symbols": _get_symbols_stats(text)
    }


def _get_symbols_stats(text: str) -> SymbolStats:
    count_alphas = 0
    count_digits = 0
    count_spaces = 0
    count_punctuation = 0

    return {
        "alphas": {
            "quantity": count_alphas,
            "percent": 0.5
        },
        "digits": {
            "quantity": count_digits,
            "percent": 0.5
        },
        "spaces": {
            "quantity": count_spaces,
            "percent": 0.5
        },
        "punctuation": {
            "quantity": count_punctuation,
            "percent": 0.5
        }
    }


def _get_tokens_stats(text: str):
    '''Подсчет количества токенов.

    '''
    
    # TODO

    return {
        "paragraphs": 0,
        "sentences": 0,
        "words": 0,
    }

import pytest
import pytest_mock

from python_kt_1.use_cases.stats import (
    stats,
    _get_symbols_stats,
    _get_tokens_stats,
    _get_pos_stats,
)
from python_kt_1.core import types


def test_tokens_stats_text(text: str):
    """Проверка подсчета крупных токенов на цельном тексте."""

    actual = _get_tokens_stats(text)

    assert actual["paragraphs"] == 4
    assert actual["sentences"] == 8


@pytest.mark.parametrize(
    "fixture_name, expected",
    [
        ("paragraph_one_sentence", {"sentences": 1, "words": 23}),
        ("paragraph_two_sentences", {"sentences": 2, "words": 16 + 23}),
        ("paragraph_four_sentences", {"sentences": 4, "words": 28 + 27 + 22 + 8}),
    ],
)
def test_tokens_stats_paragraph(
    fixture_name: str, expected: types.TokensStats, request: pytest.FixtureRequest
):
    """Проверка подсчета токенов на параграфах."""

    paragraph = request.getfixturevalue(fixture_name)
    actual = _get_tokens_stats(paragraph)

    assert actual["sentences"] == expected["sentences"]
    assert actual["words"] == expected["words"]


@pytest.mark.parametrize(
    "symbol_type, expected",
    [("alphas", 172), ("digits", 0), ("spaces", 40), ("punctuation", 10)],
)
def test_symbols_stats_paragraph(paragraph_two_sentences, symbol_type, expected):
    """Проверка подсчета символов."""

    actual = _get_symbols_stats(paragraph_two_sentences)

    assert actual[symbol_type]["quantity"] == expected

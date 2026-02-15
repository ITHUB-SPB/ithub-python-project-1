import re
import pathlib
import typing

from ..core.types import SearchResult


def search(
    pattern: str, file_path: pathlib.Path, is_regex: bool = False
) -> typing.Iterable[SearchResult]:
    """Поиск подстроки в текстовом файле

    Args:
        pattern: строка либо корректное регулярное выражение
        file_path: путь к текстовому файлу для поиска

    Returns:
        Последовательность найденных результатов с указанием
        совпадения, начала и конца фрагмента, например: [
            { "result": "kitten", "start": 17, "end": 22 },
            { "result": "kitten", "start": 43, "end": 48 }
        ] или [
            { "result": "KG", "start": 5, "end": 6 },
            { "result": "G", "start": 6, "end": 6 },
        ]

    Raises:
        InvalidRegEx: в случае передачи некорректного регулярного выражения
    """

    text = file_path.read_text(encoding="utf-8")

    return []

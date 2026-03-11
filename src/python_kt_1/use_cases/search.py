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

    if is_regex:
        return regex_search(pattern, text)
    return normal_search(pattern, text)


def regex_search(pattern: str, text: str) -> list[SearchResult]:
    try:
        return [
            {"result": match.group(), "start": match.start(), "end": match.end()}
            for match in re.finditer(pattern, text)
        ]
    except re.error:
        raise re.error("Invalid regular expression")


def normal_search(pattern: str, text: str) -> list[SearchResult]:
    results = []
    start = 0
    while True:
        pos = text.find(pattern, start)
        if pos == -1:
            break

        results.append({
            "result": pattern,
            "start": pos,
            "end": pos + len(pattern) - 1,
        })
        start = pos + 1
    return results
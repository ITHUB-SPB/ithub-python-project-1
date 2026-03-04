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
    results = []

    if is_regex:
        try:
            compiled_pattern = re.compile(pattern)
        except re.error as e:
            raise InvalidRegEx(f"Invalid regular expression: {pattern}") from e

        results = [
            SearchResult(
                result=match.group(),
                start=match.start(),
                end=match.end()
            )
            for match in compiled_pattern.finditer(text)
        ]
    else:
        start = 0
        while True:
            index = text.find(pattern, start)
            if index == -1:
                break
            results.append(SearchResult(
                result=pattern,
                start=index,
                end=index + len(pattern)
            ))
            start = index + 1

    return results

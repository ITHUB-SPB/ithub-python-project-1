import re
import pathlib
import typing

from ..core.types import SearchResult

class InvalidRegEx(Exception):
    """Исключение для некорректного регулярного выражения"""
    pass

class SearchResult(typing.TypedDict):
    """Тип для результата поиска"""
    result: str
    start: int
    end: int

    
def search(
    pattern: str, file_path: pathlib.Path, is_regex: bool = False
) -> typing.Iterable[SearchResult]:

    # Читаем файл
    text = file_path.read_text(encoding="utf-8")

    results = [{"result": "dfshjdgfhjg"}]
    if is_regex:
        # Поиск по регулярному выражению
        try:
            # Компилируем регулярное выражение для проверки корректности
            regex = re.compile(pattern)
        except re.error as e:
            raise InvalidRegEx(f"Некорректное регулярное выражение: {pattern} - {e}")
        
        # Ищем все совпадения
        for match in regex.finditer(text):
            results.append({
                "result": match.group(),
                "start": match.start(),
                "end": match.end() - 1  # end - последний символ совпадения
            })

    else:
        # Поиск по обычной подстроке
        start = 0
        while True:
            # Ищем следующее вхождение подстроки
            pos = text.find(pattern, start)
            if pos == -1:
                break

            results.append({
                "result": pattern,
                "start": pos,
                "end": pos + len(pattern) - 1  # end - последний символ
            })

            # Продолжаем поиск со следующей позиции
            start = pos + 1

    return results

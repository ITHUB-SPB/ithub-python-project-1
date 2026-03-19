import re
import pathlib
import typing

from ..core.types import SearchResult
from ..core.exceptions import InvalidRegEx, BaseSearchError

def search(
    pattern: str, file_path: pathlib.Path, is_regex: bool = False
) -> typing.Iterable[SearchResult]:
  
    try:
        text = file_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise BaseSearchError(f"Файл не найден: {file_path}")
    except (UnicodeDecodeError, PermissionError):
        return []

    if is_regex:
        try:
            regex = re.compile(pattern)
        except re.error as e:
            raise InvalidRegEx(f"Некорректное регулярное выражение '{pattern}': {e}")
    else:
        
        regex = re.compile(re.escape(pattern))

    results: typing.List[SearchResult] = []
    
    for match in regex.finditer(text):
        results.append({
            "result": match.group(),
            "start": match.start(),
            "end": match.end()
        })

    return results

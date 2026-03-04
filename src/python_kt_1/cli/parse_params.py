import mimetypes
import pathlib
import itertools
from typing import Iterable

from ..core.exceptions import InvalidPathArguments

def is_text_file(file_path: pathlib.Path) -> bool:
    """Проверяет, является ли файл текстовым
    
    Args:
        file_path: путь к файлу
        
    Returns:
        True если файл текстовый, False иначе
    """

    # Проверка по MIME-типу
    mime_type, _ = mimetypes.guess_type(str(file_path))
    if mime_type and mime_type.startswith('text/'):
        return True
    
    # Попытка прочитать файл как текст
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(8192)
            if b'\x00' in chunk:
                return False
            chunk.decode('utf-8')
            return True
    except (UnicodeDecodeError, IOError):
        return False


def get_files_from_path_arguments(*args: pathlib.Path) -> Iterable[pathlib.Path]:
    """Возвращает список путей к текстовым файлам

    Проверяет аргументы на соответствие схеме:
    - один и более файлов,
    - либо ровно одна директория
    """

    files_counter, dirs_counter = 0, 0
    files = []
    directory = None

    for path in args:
        if path.is_dir():
            dirs_counter += 1
            directory = path
        elif path.is_file():
            files_counter += 1
            files.append(path)

    if dirs_counter > 1:
        raise InvalidPathArguments("Передано более одной директории")

    if dirs_counter and files_counter:
        raise InvalidPathArguments("Смешанное задание директорий и файлов")

    if not dirs_counter and not files_counter:
        raise InvalidPathArguments("Не передано ни одного файла или директории")

    if directory:
        files = list(directory.rglob('*'))
        files = [f for f in files if f.is_file()]


    text_files = []

    for file_path in files:
        if is_text_file(file_path):
            text_files.append(file_path)

    return text_files

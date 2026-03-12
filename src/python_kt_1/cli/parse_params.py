import pathlib
import itertools
from typing import Iterable


def get_files_from_path_arguments(*args: pathlib.Path) -> Iterable[pathlib.Path]:
    """Возвращает список путей к текстовым файлам

    Проверяет аргументы на соответствие схеме:
    - один и более файлов,
    - либо ровно одна директория
    """

    files_counter, dirs_counter = 0, 0
    files: list[pathlib.Path] = []
    directory = ""

    for path in args:
        if not path.exists():
            raise Exception("Тут ничего нет")
        elif path.is_dir():
            dirs_counter += 1
            directory = path
        elif path.is_file():
            files_counter += 1
            if (path.suffix == '.txt'):
                files.append(path)

    if dirs_counter > 1:
        raise Exception("Передано более одной директории")

    if dirs_counter and files_counter:
        raise Exception("Смешанное задание директорий и файлов")

    if dirs_counter == 1:
        return list(directory.rglob('*.txt'))
    else:
        return files

    return args

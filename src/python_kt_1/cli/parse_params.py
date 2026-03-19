import pathlib
from typing import Iterable, List
from ..core.exceptions import PathArgumentError

def get_files_from_path_arguments(*args: pathlib.Path) -> Iterable[pathlib.Path]:


    files_counter, dirs_counter = 0, 0

    for path in args:
        if path.is_dir():
            dirs_counter += 1
        elif path.is_file():
            files_counter += 1

    if dirs_counter > 1:
        raise PathArgumentError("Передано более одной директории") 

    if dirs_counter and files_counter:
        raise PathArgumentError("Смешанное задание директорий и файлов")

    result_files: List[pathlib.Path] = []

    for path in args:
        if path.is_dir():
            result_files.extend(path.rglob("*.txt"))
        
        elif path.is_file():
            if path.suffix.lower() == ".txt":
                result_files.append(path)
            else:
                pass

    return result_files

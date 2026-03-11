# cli/exceptions.py
"""
Модуль с кастомными исключениями для проекта текстового поиска.
Все исключения унаследованы от соответствующих базовых классов для логичной обработки ошибок.
"""

class TextSearchError(Exception):
    """Базовое исключение для всех ошибок текстового поиска"""
    pass


# Исключения, связанные с аргументами командной строки
class ArgumentError(TextSearchError, ValueError):
    """Ошибка в аргументах командной строки"""
    pass


class MultipleDirectoriesError(ArgumentError):
    """Исключение при передаче более одной директории"""

    def __init__(self, directories_count: int):
        self.directories_count = directories_count
        super().__init__(
            f"Передано {directories_count} директорий. "
            f"Можно указать только одну директорию или несколько файлов."
        )


class MixedArgumentsError(ArgumentError):
    """Исключение при смешивании файлов и директорий"""

    def __init__(self, files_count: int, dirs_count: int):
        self.files_count = files_count
        self.dirs_count = dirs_count
        super().__init__(
            f"Смешанное задание аргументов: {files_count} файлов и {dirs_count} директорий. "
            f"Укажите либо только файлы, либо одну директорию."
        )


class NoFilesFoundError(TextSearchError, FileNotFoundError):
    """Исключение, когда не найдено подходящих файлов для поиска"""

    def __init__(self, path, extensions=None):
        self.path = path
        self.extensions = extensions or ['.txt']
        ext_str = ', '.join(self.extensions)
        super().__init__(
            f"Не найдено файлов с расширениями [{ext_str}] в {path}"
        )


# Исключения, связанные с обработкой файлов
class FileProcessingError(TextSearchError, IOError):
    """Ошибка при обработке файла"""

    def __init__(self, file_path, original_error=None):
        self.file_path = file_path
        self.original_error = original_error
        msg = f"Ошибка при обработке файла {file_path}"
        if original_error:
            msg += f": {original_error}"
        super().__init__(msg)


class FileEncodingError(FileProcessingError, UnicodeError):
    """Ошибка кодировки файла"""

    def __init__(self, file_path, encoding='utf-8', original_error=None):
        self.encoding = encoding
        super().__init__(
            file_path,
            original_error or f"Файл не может быть прочитан в кодировке {encoding}"
        )


class FilePermissionError(FileProcessingError, PermissionError):
    """Ошибка доступа к файлу"""

    def __init__(self, file_path, original_error=None):
        super().__init__(
            file_path,
            original_error or "Недостаточно прав для чтения файла"
        )


# Исключения, связанные с поиском
class SearchError(TextSearchError):
    """Базовое исключение для ошибок поиска"""
    pass


class InvalidPatternError(SearchError, ValueError):
    """Исключение для некорректного шаблона поиска"""

    def __init__(self, pattern, reason=None):
        self.pattern = pattern
        msg = f"Некорректный шаблон поиска: '{pattern}'"
        if reason:
            msg += f" - {reason}"
        super().__init__(msg)


class InvalidRegexError(InvalidPatternError):
    """Исключение для некорректного регулярного выражения"""

    def __init__(self, pattern, regex_error=None):
        self.regex_error = regex_error
        reason = f"ошибка регулярного выражения: {regex_error}" if regex_error else None
        super().__init__(pattern, reason)


class EmptyPatternError(InvalidPatternError):
    """Исключение для пустого шаблона поиска"""

    def __init__(self):
        super().__init__("", "Шаблон поиска не может быть пустым")


# Исключения для конфигурации
class ConfigurationError(TextSearchError):
    """Ошибка в конфигурации приложения"""
    pass
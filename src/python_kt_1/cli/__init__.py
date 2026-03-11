import pathlib
from time import localtime, strftime
from typing import Literal, Annotated

import typer

import python_kt_1.use_cases as use_cases
from .parse_params import get_files_from_path_arguments

app = typer.Typer()


@app.command()
def stats(
    input: Annotated[
        pathlib.Path,
        typer.Argument(
            help="Путь к файлу для анализа", exists=True, readable=True, file_okay=True
        ),
    ],
    output: Annotated[
        pathlib.Path | None,
        typer.Option(
            "--output", "-o", help="Путь к файлу для сохранения отчета", writable=True
        ),
    ] = None,
    pos: Annotated[
        bool, typer.Option(help="Добавить к отчету анализ частей речи")
    ] = False,
):
    """Статистика по текстовому файлу.

    Возможности:
    - подсчёт абзацев, предложений, слов,
    - количество и процент символов по типам,
    - опционально, статистика по частям речи.

    Два формата вывода:
    - форматированный консольный вывод,
    - неформатированный вывод в файл.
    """
    
    text = input.read_text(encoding="utf-8")
    result = use_cases.stats(text)

    print(result)


@app.command()
def search(
    pattern: Annotated[str, typer.Argument(help="Строка или регулярное выражение")],
    input: Annotated[
        list[pathlib.Path],
        typer.Argument(
            help="Файл(ы) или директория для поиска", exists=True, readable=True
        ),
    ],
    regex: Annotated[
        bool, typer.Option(help="Искать по регулярному выражению")
    ] = False,
    rich: Annotated[
        bool, typer.Option(help="Использовать форматированный вывод")
    ] = False,
):
    """Текстовый поиск по файлам или директории.

    Возможности:
    - вывод совпадений по релевантным файлам с указанием местоположений,
    - поиск по обычной строке либо регулярному выражению,
    - опционально, режим форматированного вывода
    """

    try:
        files_paths = get_files_from_path_arguments(*input)

        results = []
        for path in files_paths:
            filename = str(path.resolve())
            result = use_cases.search(pattern, path, regex)
            results.append((filename, result))

        print(results)

    except Exception as exc:
        print(exc)


@app.command("word-cloud")
def word_cloud(
        input: Annotated[
            pathlib.Path,
            typer.Argument(help="Исходный текстовый файл", exists=True, readable=True),
        ],
        output: Annotated[
            Optional[pathlib.Path],
            typer.Option("--output", "-o", help="Путь для сохранения PNG файла")
        ] = None,
        preprocess_mode: Annotated[
            Literal["basic", "stemming", "lemmatization"],
            typer.Option("--mode", "-m", help="Режим предобработки текста")
        ] = "stemming",
):
    """Построение облака важных слов.

    Построение облака важных слов из текстового файла.

    Возможности:
    - сохранение результата (изображения) в файл
    - три уровня предобработки (базовый, стемминг, лемматизация).
    """

    try:
        # Читаем текст из файла
        text = input.read_text(encoding="utf-8")

        # Вызываем use case
        result = use_cases.word_cloud(text, preprocess_mode)

        # Извлекаем имя файла из результата
        import re
        match = re.search(r'файл: (\S+\.png)', result)
        if match and output:
            default_file = Path(match.group(1))
            if default_file.exists():
                # Добавляем расширение .png если нужно
                if not output.suffix:
                    output = output.with_suffix('.png')
                elif output.suffix.lower() != '.png':
                    output = output.with_suffix('.png')

                # Переименовываем
                default_file.rename(output)
                result = result.replace(str(default_file), str(output))

        # Выводим результат
        print(result)

    except FileNotFoundError:
        print(f"Ошибка: файл {input} не найден")
        raise typer.Exit(code=1)
    except UnicodeDecodeError:
        print(f"Ошибка: не удалось прочитать файл {input} в кодировке UTF-8")
        raise typer.Exit(code=1)
    except Exception as e:
        print(f"Ошибка при создании облака слов: {e}")
        raise typer.Exit(code=1)
    """Построение облака важных слов.

    Построение облака важных слов

    Возможности:
    - сохранение результата (изображения) в файл
    - три уровня предобработки (базовый, стемминг, лемматизация).
    """



@app.command(name="top-words")
def top_words(
    input: Annotated[
        pathlib.Path,
        typer.Argument(help="Исходный текстовый файл", exists=True, readable=True),
    ],
    output: pathlib.Path | None = None,
    normalize_mode: Literal["stemming", "lemmatization"] = "stemming",
    pos: list[str] = ["__all__"],
):
    """Подсчет топ-N-важных слов.

    Подсчет топ-N-важных слов

    Возможности:
    - указание N слов,
    - фильтр по POS-тегам,
    - базовая предобработка (фильтр по стоп-словам, токенизация),
    - два типа нормализации (стемминг, лемматизация),
    - запись результатов в файл.

    """

    text = input.read_text(encoding="utf-8")
    result = use_cases.top_words(text, normalize_mode, pos)

    print(result)


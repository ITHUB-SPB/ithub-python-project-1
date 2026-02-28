import pathlib
from time import localtime, strftime
from typing import Literal, Annotated

import typer

import python_kt_1.use_cases as use_cases
from .parse_params import get_files_from_path_arguments

from rich.console import Console
from . import renderer

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
    stats = use_cases.stats(text, pos=pos)

    if output:
        if output.exists():
            choice = typer.prompt(f"Файл {output.resolve()} уже существует. Что сделать?\n"
                         "1. Перезаписать\n"
                         "2. Дописать в конец\n"
                         "3. Указать другой путь\n",
                         type=int, default=1, show_default=False)
            if choice == 2:
                existing_content = output.read_text(encoding="utf-8")
                stats = existing_content + "\n" + str(stats)
            elif choice == 3:
                new_path = typer.prompt("Введите новый путь для сохранения отчета", type=str)
                output = pathlib.Path(new_path)

        output.write_text(str(stats), encoding="utf-8")
        print(f"Отчет сохранен в {output.resolve()}")
        return
    
    result = renderer.format_output_stats(stats)
    console = Console()
    console.print(result)


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
    output: pathlib.Path | None = pathlib.Path("/")
    / f"{strftime('%H_%M_$S', localtime())}_output.png",
    preprocess_mode: Literal["basic", "stemming", "lemmatization"] = "stemming",
):
    """Построение облака важных слов.

    Построение облака важных слов

    Возможности:
    - сохранение результата (изображения) в файл
    - три уровня предобработки (базовый, стемминг, лемматизация).
    """

    pass


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

    pass

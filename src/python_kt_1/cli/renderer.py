# cli/renderer.py
import typing
from rich.console import Console
from rich.table import Table
from rich.text import Text
from rich.panel import Panel
from rich.live import Live
import time

# Тип для результатов поиска (адаптируйте под ваш формат)
SearchResult = typing.List[typing.Tuple[int, str, typing.List[int]]]
FileResults = typing.List[typing.Tuple[str, SearchResult]]

def render_simple_results(results: FileResults, pattern: str) -> None:
    """Простой текстовый вывод (без rich)"""
    for filename, matches in results:
        if matches:
            print(f"\n{filename}")
            for line_num, line, positions in matches:
                pos_str = ", ".join([str(p) for p in positions])
                print(f"  {line_num}:{pos_str}: {line}")

    total_files = len([r for r in results if r[1]])
    total_matches = sum(len(m[1]) for r in results for m in [r[1]] if m)
    print(f"\nНайдено совпадений в {total_files} файлах, всего {total_matches} строк с совпадениями")

def render_rich_results(results: FileResults, pattern: str) -> None:
    """Форматированный вывод с использованием rich"""
    console = Console()

    if not results:
        console.print("[yellow]Совпадений не найдено[/yellow]")
        return

    # Создаем таблицу для общего обзора
    table = Table(title=f"Результаты поиска: [bold cyan]'{pattern}'[/bold cyan]",
                  show_header=True,
                  header_style="bold magenta")

    table.add_column("Файл", style="cyan", no_wrap=False)
    table.add_column("Строка", justify="right", style="green")
    table.add_column("Содержимое", style="white")
    table.add_column("Позиции", justify="center", style="yellow")

    total_matches = 0

    for filename, matches in results:
        if not matches:
            continue

        # Для каждого совпадения добавляем строку в таблицу
        for i, (line_num, line, positions) in enumerate(matches):
            # Подсвечиваем искомый паттерн в строке
            highlighted_line = highlight_pattern(line, pattern, positions)

            # Форматируем позиции
            pos_text = ", ".join([str(p) for p in positions])

            # Для первой строки файла показываем имя файла, для остальных - пусто
            file_display = filename if i == 0 else ""

            table.add_row(
                file_display,
                str(line_num),
                highlighted_line,
                pos_text
            )
            total_matches += 1

    console.print(table)

    # Статистика
    total_files = len([r for r in results if r[1]])
    console.print(Panel.fit(
        f"[bold green]Найдено совпадений:[/bold green] в [cyan]{total_files}[/cyan] файлах, "
        f"[yellow]{total_matches}[/yellow] строк с совпадениями",
        border_style="blue"
    ))

def render_rich_detailed(results: FileResults, pattern: str) -> None:
    """Детальный форматированный вывод с подсветкой каждого файла"""
    console = Console()

    if not results:
        console.print("[yellow]Совпадений не найдено[/yellow]")
        return

    total_matches = 0

    for filename, matches in results:
        if not matches:
            continue

        # Заголовок файла
        console.print(f"\n[bold cyan]📄 {filename}[/bold cyan]")

        # Создаем таблицу для строк файла
        file_table = Table(show_header=True, header_style="bold", box=None)
        file_table.add_column("№", style="dim", width=4)
        file_table.add_column("Строка", style="white")
        file_table.add_column("Позиции", style="yellow", width=10)

        for line_num, line, positions in matches:
            highlighted_line = highlight_pattern(line, pattern, positions)
            pos_text = ", ".join([str(p) for p in positions])
            file_table.add_row(str(line_num), highlighted_line, pos_text)
            total_matches += 1

        console.print(file_table)

    # Итоговая статистика
    total_files = len([r for r in results if r[1]])
    console.print(f"\n[bold green]Итого:[/bold green] {total_files} файлов, {total_matches} совпадений")

def highlight_pattern(line: str, pattern: str, positions: typing.List[int]) -> str:
    """Подсвечивает найденный паттерн в строке"""
    if not positions:
        return line

    text = Text(line)
    pattern_len = len(pattern)

    for pos in positions:
        if pos + pattern_len <= len(line):
            text.stylize("bold red", pos, pos + pattern_len)

    return text

def render_rich_live_preview(results: FileResults, pattern: str) -> None:
    """Живой просмотр с обновлением (для демонстрации возможностей)"""
    console = Console()

    with Live(console=console, refresh_per_second=4) as live:
        for i, (filename, matches) in enumerate(results):
            if not matches:
                continue

            # Создаем панель для каждого файла
            content = []
            for line_num, line, positions in matches:
                highlighted = highlight_pattern(line, pattern, positions)
                content.append(f"  [green]{line_num}:[/green] {highlighted}")

            panel = Panel(
                "\n".join(content),
                title=f"[cyan]{filename}[/cyan]",
                border_style="blue"
            )

            # Обновляем live display
            live.update(panel)
            time.sleep(0.5)  # Задержка для демонстрации

def render_results(results: FileResults, pattern: str, use_rich: bool = False, detailed: bool = False) -> None:
    """Основная функция рендеринга, выбирает нужный формат"""
    if not use_rich:
        render_simple_results(results, pattern)
    else:
        if detailed:
            render_rich_detailed(results, pattern)
        else:
            render_rich_results(results, pattern)
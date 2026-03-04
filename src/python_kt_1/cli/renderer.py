import pathlib
import typing
from rich.console import Console
from rich.table import Table
from ..core.types import SearchResult

console = Console()

def render_search_results(file_path: pathlib.Path, results: typing.Iterable[SearchResult]):
    """Отрисовка таблицы результатов для конкретного файла."""
    
    if not results:
        return

    table = Table(title=f"Файл: [bold blue]{file_path}[/bold blue]", show_header=True, header_style="bold magenta")
    table.add_column("Найдено", style="green")
    table.add_column("Начало", justify="right")
    table.add_column("Конец", justify="right")

    for res in results:
        table.add_row(
            res["result"],
            str(res["start"]),
            str(res["end"])
        )

    console.print(table)
    console.print("\n")

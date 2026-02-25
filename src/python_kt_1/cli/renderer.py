from typing import Iterable
from rich.console import Console
from rich.table import Table

from ..core.types import SearchResult

console = Console()

def render_plain(file_path: str, results: Iterable[SearchResult]):
    print({file_path: results})

def render_rich(file_path: str, results: Iterable[SearchResult]):
    table = Table(title=f"Результат для {file_path}")

    table.add_column("Start")
    table.add_column("End")
    table.add_column("Match")

    for result in results:
        table.add_row(
            str(result["start"]),
            str(result["end"]),
            result["result"],
        )

    console.print(table)
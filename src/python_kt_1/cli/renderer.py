from rich.console import Console
from rich.table import Table
import os

def render_search_results(results: list[list]):
    table = Table(title="Результат")

    table.add_column("Файл", style="cyan", no_wrap=False)
    table.add_column("Слово", justify="right", style="green")
    table.add_column("Начало", style="white")
    table.add_column("Конец", style="white")

    for file in results:
        filename = os.path.basename(file[0])


        for text in file[1]:
            table.add_row(filename, text["result"], str(text["start"]), str(text["end"]))



    console = Console()
    console.print(table)





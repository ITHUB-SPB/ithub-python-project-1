from rich.table import Table
from ..core.types import TextStats
from rich import box

def format_quantity_percent(data: dict) -> str:
    return f"{data['quantity']} ({data['percent']}%)"


def format_output_stats(stats: TextStats) -> Table:
    table = Table(title="Анализ текста в файле", header_style="bold magenta", box=box.MINIMAL_HEAVY_HEAD)

    tokens = stats["tokens"]
    symbols = stats["symbols"]

    table.add_column("Категория", style="cyan")
    table.add_column("Значение", style="dim")

    table.add_row("Параграфы", str(tokens["paragraphs"]))
    table.add_row("Предложения", str(tokens["sentences"]))
    table.add_row("Слова", str(tokens["words"]))

    table.add_section()

    table.add_row("Буквы", format_quantity_percent(symbols["alphas"]))
    table.add_row("Цифры", format_quantity_percent(symbols["digits"]))
    table.add_row("Пробелы", format_quantity_percent(symbols["spaces"]))
    table.add_row("Пунктуация", format_quantity_percent(symbols["punctuation"]))

    if "pos" in stats:
        table.add_section()
        pos_stats = stats["pos"]
        for pos_tag, count in pos_stats.items():
            table.add_row(pos_tag, str(count))

    return table
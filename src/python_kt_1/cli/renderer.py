from rich.console import Console
from rich.table import Table


def render_stats(result: dict) -> None:
    """Форматированный вывод статистики в консоль."""

    console = Console()

    # Таблица токенов
    tokens = result.get("tokens", {})
    tokens_table = Table(title="Токены")
    tokens_table.add_column("Тип", style="cyan")
    tokens_table.add_column("Количество", style="magenta")
    tokens_table.add_row("Абзацы", str(tokens.get("paragraphs", 0)))
    tokens_table.add_row("Предложения", str(tokens.get("sentences", 0)))
    tokens_table.add_row("Слова", str(tokens.get("words", 0)))
    console.print(tokens_table)

    # Таблица символов
    symbols = result.get("symbols", {})
    sym_table = Table(title="Символы")
    sym_table.add_column("Тип", style="cyan")
    sym_table.add_column("Количество", style="magenta")
    sym_table.add_column("Процент", style="green")
    for key, data in symbols.items():
        sym_table.add_row(key, str(data["quantity"]), str(data["percent"]) + "%")
    console.print(sym_table)

    # Таблица частей речи (если передан флаг --pos)
    pos = result.get("pos")
    if pos:
        pos_table = Table(title="Части речи (POS)")
        pos_table.add_column("Часть речи", style="cyan")
        pos_table.add_column("Количество", style="magenta")
        sorted_pos = sorted(pos.items(), key=lambda x: x[1], reverse=True)
        for tag, count in sorted_pos:
            pos_table.add_row(tag, str(count))
        console.print(pos_table)

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

def renderer(stats_data):
    console = Console()

    table = Table(title="статистика")
    table.add_column("тип", style="cyan")
    table.add_column("количество", justify="right", style="green")
    table.add_column("процент", justify="right", style="yellow")
    
    table.add_row("буквы", str(stats_data.symbols.alphas.quantity), f"{stats_data.symbols.alphas.percent}%")
    table.add_row("цифры", str(stats_data.symbols.digits.quantity), f"{stats_data.symbols.digits.percent}%")
    table.add_row("пробелы", str(stats_data.symbols.spaces.quantity), f"{stats_data.symbols.spaces.percent}%")
    table.add_row("знаки", str(stats_data.symbols.punctuation.quantity), f"{stats_data.symbols.punctuation.percent}%")
    
    console.print(table)
    
    console.print(Panel.fit(
        f"абзацев: {stats_data.paragraphs} | "
        f"предложений: {stats_data.sentences} | "
        f"слов: {stats_data.words}",
        title="общее"
    ))
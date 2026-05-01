# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

from rich.console import Console
from rich.pretty import Pretty

console = Console()

def show(data: dict[str, object]) -> None:
    console.print(Pretty(data))

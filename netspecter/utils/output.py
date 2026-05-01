# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

from rich.console import Console
from rich.pretty import Pretty
import sys
import json

console = Console()

def show(data: dict[str, object], as_json: bool = False) -> None:
    if as_json:
        if sys.stdout.isatty():
            console.print_json(data=data, indent=2, sort_keys=True)
        else:
            print(json.dumps(data, indent=2, sort_keys=True, default=str))
    else:
        console.print(Pretty(data))

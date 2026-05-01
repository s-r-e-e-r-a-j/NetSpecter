# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

from rich.console import Console
from rich.pretty import Pretty
import sys
import json
from datetime import datetime, date

console = Console()

def sanitize(obj):
    if isinstance(obj, dict):
        return {k: sanitize(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [sanitize(i) for i in obj]
    elif isinstance(obj, tuple):
        return [sanitize(i) for i in obj]
    elif isinstance(obj, bytes):
        return obj.decode(errors="ignore")
    elif isinstance(obj, set):
        return sorted([sanitize(i) for i in obj])
    elif isinstance(obj,(datetime, date)):
        return obj.isoformat()
    else:
        return obj

def show(data: dict[str, object], as_json: bool = False) -> None:
    if as_json:
        safe_data = sanitize(data)
        if sys.stdout.isatty():
            console.print_json(data=safe_data, indent=2)
        else:
            print(json.dumps(safe_data, indent=2))
    else:
        console.print(Pretty(data))

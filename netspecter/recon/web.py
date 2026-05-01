# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

import requests
from netspecter.utils.user_agent import get_random

def probe_web(target: str, timeout: int) -> dict[str, object]:
    try:
        url = target if target.startswith("http") else f"http://{target}"
        headers = {
            "User-Agent": get_random()
        }
        r = requests.get(url, headers=headers,  timeout=timeout)
        title = ""
        if "<title>" in r.text:
            title = r.text.split("<title>")[1].split("</title>")[0]
        return {
            "status": r.status_code,
            "server": r.headers.get("Server"),
            "title": title
        }
    except:
        return {}

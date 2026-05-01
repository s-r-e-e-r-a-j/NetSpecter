# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

import requests
from netspecter.utils.user_agent import get_random

def get_geo(ip: str) -> dict[str, object]:
    try:
        headers = {
            "User-Agent": get_random()
        }
        return requests.get(f"http://ip-api.com/json/{ip}", headers=headers, timeout=5).json()
    except:
        return {}

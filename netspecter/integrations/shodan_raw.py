# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

import shodan
from netspecter.utils.config import load


def fetch(ip: str) -> dict[str, object]:
    cfg = load()
    key = cfg.get("SHODAN", "api_key", fallback=None)

    if not key:
        return {"error": "missing_api_key"}

    try:
        api = shodan.Shodan(key)

        result = api.host(ip)

        return {
            "ok": True,
            "data": result
        }

    except shodan.APIError as e:
        return {
            "error": "shodan_api_error",
            "message": str(e)
        }

    except Exception as e:
        return {
            "error": "exception",
            "message": str(e)
        }

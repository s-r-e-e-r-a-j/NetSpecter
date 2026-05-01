# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

from netspecter.integrations.shodan_raw import fetch
from netspecter.intelligence.extractor import extract
from netspecter.intelligence.analyzer import analyze
from netspecter.intelligence.scorer import score

def full_lookup(target: str) -> dict[str, object]:
    raw = fetch(target)

    if not raw or "error" in raw:
        return {
            "error": raw.get("error", "shodan_failed"),
            "status": raw.get("status"),
            "response": raw.get("response") or raw.get("message")
        }

    data = extract(raw)

    if "error" in data:
        return data

    return {
        "data": data,
        "analysis": analyze(data),
        "risk": score(data)
    }

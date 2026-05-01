# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

def score(data: dict[str, object]) -> str:
    if not data or "error" in data:
        return "UNKNOWN"

    ports: list[int] = data.get("ports") or []
    vulns: dict = data.get("vulns") or {}

    r = 0

    if 22 in ports:
        r += 10
    if 3389 in ports:
        r += 30
    if 3306 in ports:
        r += 25
    if vulns:
        r += 40

    if r >= 60:
        return "CRITICAL"
    if r >= 30:
        return "HIGH"
    if r >= 10:
        return "MEDIUM"

    return "LOW"

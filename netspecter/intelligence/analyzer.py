# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

def analyze(data: dict[str, object]) -> dict[str, object]:
    if not data or "error" in data:
        return {"issues": ["invalid_or_failed_shodan_response"]}

    ports = data.get("ports") or []
    vulns = data.get("vulns") or {}

    issues = []

    if 22 in ports:
        issues.append("ssh exposed")
    if 3389 in ports:
        issues.append("rdp exposed")
    if 3306 in ports:
        issues.append("mysql exposed")
    if vulns:
        issues.append("vulnerabilities detected")

    if data.get("os"):
        issues.append(f"os detected: {data['os']}")

    return {"issues": issues}

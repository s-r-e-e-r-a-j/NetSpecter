# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

def extract(raw: dict) -> dict[str, object]:
    if not raw:
        return {"error": "empty_response"}

    if "error" in raw:
        return raw

    data = raw.get("data", {})

    return {
        "ip": data.get("ip_str"),
        "ports": data.get("ports", []),
        "org": data.get("org"),
        "isp": data.get("isp"),
        "os": data.get("os"),
        "asn": data.get("asn"),
        "hostnames": data.get("hostnames", []),
        "country": data.get("country_name"),
        "city": data.get("city"),
        "vulns": data.get("vulns", {}),
        "services": [
            {
                "port": s.get("port"),
                "product": s.get("product"),
                "version": s.get("version"),
                "banner": s.get("data"),
                "transport": s.get("transport"),
            }
            for s in data.get("data", [])
            if isinstance(s, dict)
        ],
        "raw": data,
        "mode": "shodan_host"
    }

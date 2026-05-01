# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

import dns.resolver

def get_dns(domain: str) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for t in ["A", "MX", "NS", "TXT"]:
        try:
            ans = dns.resolver.resolve(domain, t)
            out[t] = [str(r) for r in ans]
        except:
            out[t] = []
    return out

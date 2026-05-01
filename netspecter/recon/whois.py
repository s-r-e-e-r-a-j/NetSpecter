# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

import whois

def get_whois(domain: str) -> dict[str, object]:
    try:
        return dict(whois.whois(domain))
    except:
        return {}

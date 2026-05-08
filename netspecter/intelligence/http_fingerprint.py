# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

import requests
import re
from netspecter.utils.user_agent import get_random


def http_fingerprint(url: str) -> dict[str, object]:
    try:
        if not url.startswith("http"):
            url = "http://" + url

        headers_req = {
            "User-Agent": get_random()
        }

        r = requests.get(
            url,
            timeout=5,
            allow_redirects=True,
            headers=headers_req
        )

        headers = dict(r.headers)

        return {
            "status_code": r.status_code,
            "final_url": r.url,
            "server": headers.get("Server"),
            "content_type": headers.get("Content-Type"),

            "security_headers": {
                "hsts": headers.get("Strict-Transport-Security"),
                "csp": headers.get("Content-Security-Policy"),
                "x_frame": headers.get("X-Frame-Options"),
                "x_xss": headers.get("X-XSS-Protection"),
                "powered_by": headers.get("X-Powered-By")
            },

            "powered_by": headers.get("X-Powered-By"),
            "location": headers.get("Location"),
            "set_cookie_present": "Set-Cookie" in headers,
            "cookie_count": len(r.cookies),
            "content_length": headers.get("Content-Length"),

            "redirected": url != r.url,
            "redirect_chain_length": len(r.history) if r.history else 0,

            "title": extract_title(r.text),
            "title_length": len(extract_title(r.text) or ""),

            "encoding": r.encoding
        }

    except Exception as e:
        return {
            "error": str(e)
        }


def extract_title(html: str) -> str | None:
    try:
        match = re.search(
            r"<title[^>]*>(.*?)</title>",
            html,
            re.IGNORECASE | re.DOTALL
        )
        if match:
            return match.group(1).strip()
    except:
        pass
    return None

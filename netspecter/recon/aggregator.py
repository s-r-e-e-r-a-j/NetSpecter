# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

import asyncio
import socket
from netspecter.recon.dns import get_dns
from netspecter.recon.web import probe_web
from netspecter.recon.reverse_dns import reverse_dns
from netspecter.recon.whois import get_whois
from netspecter.recon.geo import get_geo
from netspecter.intelligence.shodan_full import full_lookup
from netspecter.intelligence.tls_intel import get_tls_info
from netspecter.intelligence.http_fingerprint import http_fingerprint

async def build_profile(target: str, full: bool, timeout: int) -> dict[str, object]:
    tasks = [
        asyncio.to_thread(get_dns, target),
        asyncio.to_thread(probe_web, target, timeout),
        asyncio.to_thread(reverse_dns, target),
        asyncio.to_thread(get_whois, target),
        asyncio.to_thread(get_geo, target),
    ]

    dns, web, rev, whois, geo = await asyncio.gather(*tasks)
    tls_data = None
    http_data = None

    if target and "." in target:
        tls_data = await asyncio.to_thread(get_tls_info, target)
        http_data = await asyncio.to_thread(http_fingerprint, target)
    data: dict[str, object] = {
        "target": target,
        "dns": dns,
        "web": web,
        "tls":tls_data,
        "http":http_data,
        "reverse_dns": rev,
        "whois": whois,
        "geo": geo,
        "intelligence": {}
    }

    if full:
        ip = target
        try:
            ip = socket.gethostbyname(target)
        except:
            pass

        data["intelligence"] = await asyncio.to_thread(full_lookup, ip)

    return data

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

async def build_profile(target: str, full: bool, timeout: int) -> dict[str, object]:
    tasks = [
        asyncio.to_thread(get_dns, target),
        asyncio.to_thread(probe_web, target, timeout),
        asyncio.to_thread(reverse_dns, target),
        asyncio.to_thread(get_whois, target),
        asyncio.to_thread(get_geo, target),
    ]

    dns, web, rev, whois, geo = await asyncio.gather(*tasks)

    data: dict[str, object] = {
        "target": target,
        "dns": dns,
        "web": web,
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

# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

import socket

def reverse_dns(ip: str) -> str | None:
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return None

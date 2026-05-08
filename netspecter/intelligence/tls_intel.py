# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

import ssl
import socket


def clean(value: str | None) -> str | None:
    if not value:
        return value
    return value.replace("\n", " ").strip()


def get_tls_info(domain: str, port: int = 443) -> dict[str, object]:
    try:
        context = ssl.create_default_context()

        with socket.create_connection((domain, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

        subject = {
            k: clean(v)
            for k, v in dict(x[0] for x in cert.get("subject", [])).items()
        }

        issuer_raw = dict(x[0] for x in cert.get("issuer", []))

        issuer = {
            k: clean(str(v))
            for k, v in issuer_raw.items()
        }

        san = cert.get("subjectAltName", [])
        san_clean = [
            value for typ, value in san if typ == "DNS"
        ]

        return {
            "subject": subject,
            "issuer": issuer,
            "version": cert.get("version"),
            "serial_number": cert.get("serialNumber"),
            "not_before": cert.get("notBefore"),
            "not_after": cert.get("notAfter"),
            "san": san_clean,
            "valid": True
        }

    except Exception as e:
        return {
            "valid": False,
            "error": str(e)
        }

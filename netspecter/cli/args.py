# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

import argparse

def get_args():
    p = argparse.ArgumentParser(
        prog="netspecter",
        description="NetSpecter Intelligence Engine",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Examples:
  netspecter recon example.com
  netspecter recon 8.8.8.8 --full
"""
    )

    sub = p.add_subparsers(dest="cmd", required=True)

    r = sub.add_parser("recon", help="run reconnaissance")

    r.add_argument("target")
    r.add_argument("--full", action="store_true")
    r.add_argument("--timeout", type=int, default=5)
    r.add_argument("--json", action="store_true", help="output result in JSON format")

    return p.parse_args()

# Developer: Sreeraj
# GitHub: https://github.com/s-r-e-e-r-a-j

import asyncio
from netspecter.cli.args import get_args
from netspecter.recon.aggregator import build_profile
from netspecter.utils.output import show

async def main() -> None:
    args = get_args()

    if args.cmd == "recon":
        data = await build_profile(args.target, args.full, args.timeout)
        show(data, args.json)

def run() -> None:
    asyncio.run(main())

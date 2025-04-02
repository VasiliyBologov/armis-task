import asyncio

import conf

import qualys
import crowdstrike


if __name__ == "__main__":
    cfg = conf.load_config()

    asyncio.run(qualys.run(cfg))
    asyncio.run(crowdstrike.run(cfg))
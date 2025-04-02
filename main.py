import sys
import asyncio

import conf

import qualys
import crowdstrike


if __name__ == "__main__":
    cfg = conf.load_config()
    api = sys.argv[1]
    runer = {
        "qualys": qualys.run(cfg),
        "crowdstrike": crowdstrike.run(cfg),
    }

    asyncio.run(runer[api])

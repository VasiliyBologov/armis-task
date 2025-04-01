import conf

import qualys
import crowdstrike


if __name__ == "__main__":
    cfg = conf.load_config()

    qualys.run(cfg)
    crowdstrike.run(cfg)
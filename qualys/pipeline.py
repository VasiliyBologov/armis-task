import logging

import crowdstrike.api as api
import crowdstrike.models as model
import crowdstrike.database as database

import conf
import db


def run(cfg: conf.Config):
    qualys_db = db.create_connection(cfg.mongo_url, cfg.mongo_db, cfg.qualys_hosts_collection)

    skip = 0
    chank_size = 2
    while True:
        res, err, limit = api.fetch_data(cfg, skip=skip, limit=chank_size)
        if err:
            if err == "less_limit":
                chank_size -= 1
                continue
            if chank_size == 0:
                break
            logging.error(err)
            break
        data = []
        for r in res:
            result = model.HostAsset(**r)
            data.append(result)
        skip += limit

        database.bulk_write(qualys_db, data)
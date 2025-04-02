import logging

import qualys.api as api
import qualys.models as model

import conf
import db


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


async def run(cfg: conf.Config):
    log.info(f"Starting pipeline")
    qualys_db = await db.create_connection(cfg.mongo_url, cfg.mongo_db, cfg.qualys_hosts_collection)

    skip = 0
    chank_size = 2
    while True:
        res, err, limit = await api.fetch_data(cfg, skip=skip, limit=chank_size)
        if err:
            if err == "less_limit":
                chank_size -= 1
                log.warning(f"Catch 'less_limit' error: {err}")
                continue
            if chank_size == 0:
                log.warning(f"Catch 'chank_size' = 0")
                break
            log.warning(f"Catch unknown error: {err}")
            break
        data = []
        for r in res:
            result = model.HostAsset(**r)
            data.append(result)
        skip += limit

        await db.bulk_write(qualys_db, data)

    log.info(f"Pipeline finished")

import pymongo
import pymongo.errors
import logging

import qualys.models as model


def bulk_write(db: pymongo.synchronous.collection.Collection, data: list[model.HostAsset]):
    documents = []
    for host in data:
        documents.append(pymongo.UpdateOne({"_id": host.id}, {"$set": host.dict()}, upsert=True))

    try:
        db.bulk_write(documents)
    except pymongo.errors.BulkWriteError as bwe:
        logging.error(bwe.details)

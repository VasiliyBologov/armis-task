from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from pymongo import UpdateOne
from pymongo.errors import BulkWriteError
import logging

async def create_connection(url, db, collection) -> AsyncIOMotorCollection:
    """
    Async connector to mongodb database.
    :param url: mongo db connection string
    :param db: name of database
    :param collection: name of collection
    :return: DB connection
    """
    client = AsyncIOMotorClient(url)
    db = client[db]
    return db[collection]


async def bulk_write(db: AsyncIOMotorCollection, data):
    """
    Bulk write to mongodb database.
    :param db: DB connection
    :param data: list of data to write
    """
    documents = []
    for host in data:
        documents.append(UpdateOne({"_id": host.id}, {"$set": host.model_dump()}, upsert=True))

    try:
        await db.bulk_write(documents)
    except BulkWriteError as bwe:
        logging.error(bwe.details)

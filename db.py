from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from pymongo import UpdateOne
from pymongo.errors import BulkWriteError
import logging

async def create_connection(url, db, collection) -> AsyncIOMotorCollection:
    client = AsyncIOMotorClient(url)
    db = client[db]
    return db[collection]


async def bulk_write(db: AsyncIOMotorCollection, data):
    documents = []
    for host in data:
        documents.append(UpdateOne({"_id": host.id}, {"$set": host.model_dump()}, upsert=True))

    try:
        await db.bulk_write(documents)
    except BulkWriteError as bwe:
        logging.error(bwe.details)

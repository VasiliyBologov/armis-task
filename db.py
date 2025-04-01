import pymongo

def create_connection(url, db, collection) -> pymongo.synchronous.collection.Collection:
    client = pymongo.MongoClient(url)
    db = client[db]
    return db[collection]


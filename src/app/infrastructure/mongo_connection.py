from pymongo import MongoClient
from app.config.settings import (
    MONGO_URI,
    MONGO_DB
)


def get_database():
    uri = MONGO_URI
    db_name = MONGO_DB

    client = MongoClient(uri)
    return client[db_name]

import pymongo

from database.settings import (
    MONGO_USER,
    MONGO_PASS,
    MONGO_ARGS,
    MONGO_PORT,
    MONGO_HOST,
    MONGO_DB,
)

if MONGO_USER and MONGO_PASS:
    client = pymongo.MongoClient(
        "mongodb://{}:{}@{}:{}/{}".format(
            MONGO_USER, MONGO_PASS, MONGO_HOST, MONGO_PORT, MONGO_ARGS
        ),
    )
else:
    client = pymongo.MongoClient(
        "mongodb://{}:{}/{}".format(MONGO_HOST, MONGO_PORT, MONGO_ARGS),
    )

db = client[MONGO_DB]

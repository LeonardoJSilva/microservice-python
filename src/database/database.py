import logging
import pymongo

from database.settings import (
    MONGO_USER,
    MONGO_PASS,
    MONGO_ARGS,
    MONGO_PORT,
    MONGO_HOST,
    MONGO_DB,
)

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y - %I:%M:%S %p',
                    level=logging.INFO)
logging.info("Connecting in Database")

try:
    if MONGO_USER and MONGO_PASS:
        logging.info(f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_ARGS}")
        client = pymongo.MongoClient(
            f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_ARGS}",
        )
    else:
        logging.info(f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_ARGS}")
        client = pymongo.MongoClient(
            f"mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_ARGS}",
        )
    db = client[MONGO_DB]

except Exception:
    logging.error("Fail to connect in Database")

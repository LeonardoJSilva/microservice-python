import logging
from pymongo import IndexModel, ASCENDING
from umongo import Instance, Document, fields
from database.database import db

instance: Instance = Instance(db)


@instance.register
class ProductDB(Document):
    name = fields.StringField(required=True)
    code = fields.IntegerField(required=True)
    description = fields.StringField(required=True)
    quantity = fields.IntegerField(required=True)
    supplier = fields.IntegerField(required=True)

    class Meta:
        collection_name = "products"
        strict = False
        indexes = [IndexModel([("code", ASCENDING), ("supplier", ASCENDING)], unique=True)]


try:
    ProductDB.ensure_indexes()
    logging.info("Connected successfully in database")
except Exception:
    logging.error("Fail to connect in database")
    raise

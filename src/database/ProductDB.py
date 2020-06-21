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
    deleted = fields.BooleanField(required=True, default=False)

    class Meta:
        collection_name = "products"
        strict = False
        indexes = [IndexModel([("code", ASCENDING), ("supplier", ASCENDING)], unique=True)]


ProductDB.ensure_indexes()




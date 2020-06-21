from decouple import config

MONGO_HOST = config("MONGO_HOST", default="localhost")
MONGO_PORT = config("MONGO_PORT", default=27017, cast=int)
MONGO_USER = config("MONGO_USERNAME", default="")
MONGO_PASS = config("MONGO_PASSWORD", default="")
MONGO_ARGS = config("MONGO_ARGUMENTS", default="")
MONGO_DB = config("MONGO_DATABASE", default="products")

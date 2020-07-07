from decouple import config

SUPPLIERS_HOST = config("SUPPLIERS_HOST", default="localhost")
SUPPLIERS_PORT = config("SUPPLIERS_PORT", default="50051")

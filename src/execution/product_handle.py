import json
import logging
from aiohttp import web
from aiohttp.web_response import Response
from database.ProductDAO import ProductDAO
from database.ProductDB import ProductDB
from database.utils import convert_to_mongo_document
from entities.Product import Product
from validations.validator import validator_data

logger = logging.getLogger()


async def create_product_handle(product_data: dict) -> Response:
    validate_result = validator_data(product_data)
    if validate_result.errors:
        logger.info("Error when validating")
        return web.Response(status=422, body=json.dumps(validate_result.errors))

    logger.info(f"Validation success for product code {product_data['code']} and supplier {product_data['supplier']}")

    validated_data = validate_result.document
    product = Product(**validated_data)

    product_db = ProductDAO.find_by_code_and_supplier(product.code, product.supplier)
    if product_db:
        return web.Response(status=422, body="Product existent in the database")

    product_db = convert_to_mongo_document(product, ProductDB)

    if product_db is None:
        return web.Response(status=500, body="Internal Error")

    product_db.commit()

    logger.info(f"Persistence success for product code {product_data['code']} and supplier {product_data['supplier']}")

    return web.Response(status=200, body=json.dumps(product.__dict__))

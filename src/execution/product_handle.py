import json
import logging
from aiohttp import web
from aiohttp.web_response import Response
from database.ProductDAO import ProductDAO
from database.ProductDB import ProductDB
from database.utils import convert_to_mongo_document
from entities.Product import Product
from grpc_suppliers.grpc_suppliers import GrpcSuppliers
from validations.validator import data_validator


async def create_product_handle(product_data: dict) -> Response:
    validate_result = data_validator(product_data)
    if validate_result.errors:
        logging.error("Error when validating")
        return web.Response(status=422, body=json.dumps(validate_result.errors))

    logging.info(f"Validation success for product code {product_data['code']} of supplier {product_data['supplier']}")

    response = GrpcSuppliers().get_suppliers_by_codes([product_data['supplier']])

    if not len(response.Codes):
        logging.info(f"Supplier with code {product_data['supplier']} not existent or was deleted")
        return web.Response(status=422,
                            body=f"Supplier with code {product_data['supplier']} not founded or was deleted")

    validated_data = validate_result.document
    product = Product(**validated_data)

    product_db = await ProductDAO.get_by_code_and_supplier(product.code, product.supplier)
    if product_db:
        logging.info(f"Product existent in the database")
        return web.Response(status=422, body="Product existent in the database")

    product_db = convert_to_mongo_document(product, ProductDB)

    if product_db is None:
        return web.Response(status=500, body="Internal Error")

    product_db.commit()

    logging.info(f"Persistence success for product code {product_data['code']} of supplier {product_data['supplier']}")

    return web.Response(status=200, body=json.dumps(product.__dict__))


async def get_all_product_handle() -> Response:
    all_products = await ProductDAO.get_all()

    logging.info("Get for all products")

    return web.Response(status=200, body=json.dumps([product.dump() for product in all_products]))


async def get_product_by_code_handle(supplier: int, code: int) -> Response:
    product_db = await ProductDAO.get_by_code_and_supplier(code, supplier)

    logging.info(f"Get for product code {code} of supplier {supplier}")

    body = product_db.dump() if product_db is not None else f"Product {code} of supplier {supplier} not found"
    if type(body) is dict:
        del body['id']

    status = 200 if type(body) is dict else 404

    return web.Response(status=status, body=json.dumps(body) if status == 200 else body)


async def delete_product_by_code_handle(supplier: int, code: int) -> Response:
    product_db = await ProductDAO.get_by_code_and_supplier(code, supplier)

    await ProductDAO.delete_by_code_and_supplier(product_db) if product_db is not None else None

    logging.info(f"Delete for product code {code} of supplier {supplier}")

    body = None if product_db is not None else f"Product {code} of supplier {supplier} not found"
    status = 204 if body is None else 404

    logging.info(body if body is not None else f"Product {code} of supplier {supplier} successfully deleted")

    return web.Response(status=status, body=body)

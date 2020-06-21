import logging
from cerberus import Validator

logger = logging.getLogger()


def validator_data(product_data: dict) -> Validator:
    schema = {'name': {'type': 'string', 'required': True}, 'code': {'type': 'integer', 'required': True},
              'description': {'type': 'string', 'required': True},
              'quantity': {'type': 'integer', 'required': True}, 'supplier': {'type': 'integer', 'required': True}}
    validator = Validator()
    logger.info(f"Validating product code {product_data['code']} and supplier {product_data['supplier']}")
    validator.validate(product_data, schema)
    return validator

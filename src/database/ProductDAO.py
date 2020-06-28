from typing import List
from database.ProductDB import ProductDB


class ProductDAO:

    @staticmethod
    async def get_all() -> List[ProductDB]:
        return ProductDB.find({}, {"_id": 0})

    @staticmethod
    async def get_by_code_and_supplier(code: int, supplier: int) -> ProductDB:
        return ProductDB.find_one({"code": code, "supplier": supplier})

    @staticmethod
    async def delete_by_code_and_supplier(product: ProductDB) -> None:
        product.delete()

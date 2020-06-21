from database.ProductDB import ProductDB


class ProductDAO:

    @staticmethod
    def find_by_code_and_supplier(code: int, supplier: int) -> ProductDB:
        return ProductDB.find_one({"code": code, "supplier": supplier})

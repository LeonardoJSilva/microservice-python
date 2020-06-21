
class Product:
    def __init__(self, name: str, code: int, description: str, quantity: int, supplier: int, deleted: bool = False):
        self.name = name
        self.code = code
        self.description = description
        self.quantity = quantity
        self.supplier = supplier
        self.deleted = deleted

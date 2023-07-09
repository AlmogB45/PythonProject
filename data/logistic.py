from abc import ABC


class ILogistic(ABC):
    def add_product_to_shelves(self, product, department):
        pass

    def remove_product_from_shelves(self, product, department):
        pass
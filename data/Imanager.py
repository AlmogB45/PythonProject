from abc import ABC


class IManager(ABC):
    def sell_product_to_customer(self):
        pass

    def purchase_product(self, product_name, customer_name):
        pass

    def get_customers_with_purchases(self):
        pass
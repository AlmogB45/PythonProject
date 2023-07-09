from data.person import Person
from entities.client import Client
from entities.employee import Employee


class Cashier(Employee):
    def __init__(self, register_number: int, employee_number: int, ID: int, name: str, age: int, phone_number: str):
        super().__init__(employee_number, ID, name, age, phone_number)
        self.register_number = register_number

    def purchase_product(self, client: Client, product):
        client.purchased_products.append(product)

    def __str__(self):
        print(f"register number: {self.register_number}")
        super().__str__()

    def __eq__(self, other):
        if isinstance(other, Cashier):
            return self.employee_number == other.employee_number
        return False

from data.file_handler import FileHandler
from data.logistic import ILogistic
from data.manager import IManager
from data.person import Person
from entities.Product import Product
from entities.employee import Employee


class ShiftManager(Employee, ILogistic, IManager):
    def __init__(self, employee_number, ID: int, name: str, age: int, phone_number: str):
        super().__init__(employee_number, ID, name, age, phone_number)
        self.file_handler = FileHandler()

    def add_product_to_shelves(self):
        product_name = input("Enter the product name: ")
        product_type = input("Enter the product type: ")
        product_price = float(input("Enter the product price: "))

        product = Product(product_name, product_type, product_price)
        self.file_handler.write_product_to_file(product)

        print(f"Product '{product_name}' added to the shelves.")

    def remove_product_from_shelves(self):
        product_name = input("Enter the product name: ")
        self.file_handler.remove_product_from_file(product_name)

        print(f"Product '{product_name}' removed from the shelves.")

    def add_employee(self, employee, employee_list):
        employee_list.append(employee)

    def remove_employee(self, employee, employee_list):
        if employee in employee_list:
            employee_list.remove(employee)

    def get_client_by_purchase_date(self, client, purchase_date):
        return [client for client in client if client.purchase_date == purchase_date]

    def __str__(self):
        print(f"employee number: {self.employee_number}")
        super().__str__()

    def __eq__(self, other):
        if isinstance(other, ShiftManager):
            return self.employee_number == other.employee_number
        return False

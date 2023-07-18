from data.file_handler import FileHandler
from data.logistic import ILogistic
from entities.Product import Product
from entities.employee import Employee

RESET = "\033[0m"
GREEN = "\033[32m"


def print_color(text, color):
    print(color + text + RESET)


class Sorter(Employee,ILogistic):
    def __init__(self, employee_number, employee_type, ID, name: str, age):
        super().__init__(employee_number, employee_type, ID, name, age)
        self.vest_color = "yellow"
        self.file_handler = FileHandler()

    def add_product_to_shelves(self):
        product_name = input("Enter the product name: ")
        product_type = input("Enter the product type: ")
        product_price = float(input("Enter the product price: "))

        product = Product(product_name, product_type, product_price)
        self.file_handler.write_product_to_file(product)

        print(GREEN, f"Product '{product_name}' added to the shelves.", RESET)

    def remove_product_from_shelves(self):
        product_name = input("Enter the product name: ")
        self.file_handler.remove_product_from_file(product_name)

        print(GREEN, f"Product '{product_name}' removed from the shelves.", RESET)

    def __str__(self):
        print(f""""vest color: {self.vest_color}
employee number: {self.employee_number}""")
        super().__str__()
    
    def __eq__(self, other):
        if isinstance(other, Sorter):
            return self.employee_number == other.employee_number
        return False


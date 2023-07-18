from data.Imanager import IManager
from data.file_handler import FileHandler
from entities.Product import Product
from entities.employee import Employee
from data.Login import Login



RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"


def print_color(text, color):
    print(color + text + RESET)


class ChiefManager(Employee,IManager):
    def __init__(self, employee_number: object, employee_type: object, ID: object, name: object, age: object):
        super().__init__(employee_number, employee_type, ID, name, age)

        self.file_handler = FileHandler()
        self.products = FileHandler.read_product_from_file()
        self.customer_names = []

    def add_employee(self):
        employee_name = input("Enter employee name: ")
        employee_password = input("Enter employee password: ")
        worker_type = input("Enter worker type: ")

        Login.EmployeeManager.add_employee(employee_name, employee_password, worker_type)

    def remove_employee(self):
        # Prompt for the employee name to be removed
        employee_name_to_remove = input("Enter employee name to remove: ")

        # Read all existing employee credentials
        with open("C:\\Users\\Almog-Laptop\\OneDrive\\Desktop\\FinalSuper\\data\\credentials.txt", "r") as f:
            lines = f.readlines()

        # Filter out the lines containing the employee to be removed
        updated_lines = [line for line in lines if not line.startswith(f"{employee_name_to_remove},")]

        # Write back the updated credentials file
        with open("C:\\Users\\Almog-Laptop\\OneDrive\\Desktop\\FinalSuper\\data\\credentials.txt", "w") as f:
            f.writelines(updated_lines)

    # def print_all_products(self):
    #     print("Products available in the file:")
    #     for product in self.products:
    #         print(f"Product Name: {product.name}")
    #         print(f"Product Type: {product.type}")
    #         print(f"Product Price: {product.price}")
    #         print("----------")

    def sell_product_to_customer(self):
        product_name = input("Enter the product name: ")
        customer_name = input("Enter the customer name: ")
        self.purchase_product(product_name, customer_name)
        self.customer_names.append(customer_name)

    def purchase_product(self, product_name, customer_name):
        # Check if the product exists in the file.
        product = None
        for prod in self.products:
            if prod.name == product_name:
                product = prod
                break

        if product is None:
            print(RED, "Product not found.")
            return

        # Print a purchase successful message.
        print(GREEN, f"Purchase successful for {customer_name}.")

    def get_customers_with_purchases(self):
        print("Customers with purchases:")
        for customer_name in self.customer_names:
            print(customer_name)








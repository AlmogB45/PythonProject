from data.Imanager import IManager
from data.Login import Login
from data.file_handler import FileHandler
from data.logistic import ILogistic
from entities.Product import Product
from entities.employee import Employee

RESET = "\033[0m"
GREEN = "\033[32m"
RED = "\033[31m"


def print_color(text, color):
    print(color + text + RESET)


class ShiftManager(Employee, ILogistic,IManager):
    def __init__(self, employee_number, ID: int, name: str, age: int, phone_number: str):
        super().__init__(employee_number, ID, name, age, phone_number)
        self.file_handler = FileHandler()
        self.products = FileHandler.read_product_from_file()
        self.customer_names = []

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

    def add_employee(self):
        employee_name = input("Enter employee name: ")
        employee_password = input("Enter employee password: ")
        worker_type = input("Enter worker type: ")

        Login.EmployeeManager.add_employee(employee_name, employee_password, worker_type)

    def remove_employee(self):
        # Prompt for the employee name to be removed
        employee_name_to_remove = input("Enter employee name to remove: ")

        # Read all existing employee credentials
        with open(Login.get_credentials_file_path(), "r") as f:
            lines = f.readlines()

        # Filter out the lines containing the employee to be removed
        updated_lines = [line for line in lines if not line.startswith(f"{employee_name_to_remove},")]

        # Write back the updated credentials file
        with open(Login.get_credentials_file_path(), "w") as f:
            f.writelines(updated_lines)

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

    # def read_product_from_file(self):
    #     products = []
    #
    #     try:
    #         with open("C:\\Users\\Almog-Laptop\\OneDrive\\Desktop\\FinalSuper\\data\\products.txt", 'r') as file:
    #             for line in file:
    #                 data = line.strip().split(",")
    #
    #                 if len(data) == 3:
    #                     name = data[0]
    #                     type = data[1]
    #                     price = float(data[2])  # Convert the price to float
    #
    #                     prod = Product(name, type, price)
    #                     products.append(prod)
    #
    #     except IOError as e:
    #         print(RED, "Error reading file:", e)
    #
    #     return products
    #
    def get_customers_with_purchases(self):
        print("Customers with purchases:")
        for customer_name in self.customer_names:
            print(customer_name)

    # def get_client_by_purchase_date(self, client, purchase_date):
    #     return [client for client in client if client.purchase_date == purchase_date]

    def __str__(self):
        print(f"employee number: {self.employee_number}")
        super().__str__()

    def __eq__(self, other):
        if isinstance(other, ShiftManager):
            return self.employee_number == other.employee_number
        return False

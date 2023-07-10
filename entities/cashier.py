from data.person import Person
from entities.Product import Product
from entities.client import Client
from entities.employee import Employee


class Cashier(Employee):

    def __init__(self, register_number: int, employee_number: int, ID: int, name: str, age: int, phone_number: str):
        super().__init__(employee_number, ID, name, age, phone_number)
        self.register_number = register_number
        self.products = self.read_product_from_file()

    def sell_product_to_customer(self):
        product_name = input("Enter the product name: ")
        customer_name = input("Enter the customer name: ")
        self.purchase_product(product_name, customer_name)

    def purchase_product(self, product_name, customer_name):

        # Check if the product exists in the file.
        product = None
        for prod in self.products:
            if prod.name == product_name:
                product = prod
                break

        if product is None:
            print("Product not found.")
            return

        # Print a purchase successful message.
        print(f"Purchase successful for {customer_name}.")

    def read_product_from_file(self):
        products = []

        try:
            with open("C:\\Users\\Almog-Laptop\\OneDrive\\Desktop\\FinalSuper\\data\\products.txt", 'r') as file:
                for line in file:
                    data = line.strip().split(",")

                    if len(data) == 3:
                        name = data[0]
                        type = data[1]
                        price = float(data[2])  # Convert the price to float

                        prod = Product(name, type, price)
                        products.append(prod)

        except IOError as e:
            print("Error reading file:", e)

        return products

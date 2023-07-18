from entities.Product import Product
from entities.employee import Employee

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"



def print_color(text, color):
    print(color + text + RESET)


class Cashier(Employee):

    def __init__(self, name: str, register_number: int, ID: int, age: int, phone_number: str):
        super().__init__(name, ID, name, age, phone_number)
        self.register_number = register_number
        self.products = self.read_product_from_file()
        self.customers_with_purchases = {}

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
            print(RED, "Product not found.")
            return

        # Print a purchase successful message.
        print(GREEN, f"Purchase successful for {customer_name}.")
        # Track customers with purchases
        if customer_name in self.customers_with_purchases:
            self.customers_with_purchases[customer_name].append(product)
        else:
            self.customers_with_purchases[customer_name] = [product]

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
            print(RED, "Error reading file:", e)

        return products



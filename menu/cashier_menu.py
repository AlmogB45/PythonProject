import sys
from entities.Product import Product



class CashierMenu:

    def __init__(self):
        self.products = self.read_product_from_file()

    def display_menu(self):
        while True:
            print("-------- Cashier Menu --------")
            print("\n")
            print("1. Sell product to customer")
            print("2. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.sell_product_to_customer()
            elif choice == "2":
                print("\n")
                print("*** thank you and see you soon at the super ***")
                sys.exit()
            elif choice == "q":
                break
            else:
                print("Invalid choice. Please try again.")

    def sell_product_to_customer(self):
        product_name = input("Enter the product name: ")
        customer_name = input("Enter the customer name: ")
        self.purchase_product(product_name, customer_name)

    def purchase_product(self, product_name, customer_name):
        """Purchases a product from the product.txt file.

        Args:
          product_name: The name of the product to purchase.
          customer_name: The name of the customer purchasing the product.
        """

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


if __name__ == "__main__":
    cashier_menu = CashierMenu()
    cashier_menu.display_menu()


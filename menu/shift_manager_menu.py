from entities.shift_manager import ShiftManager
from entities.Product import Product
import sys

class ShiftManagerMenu:
    def __init__(self):
        self.shift_manager = ShiftManager(employee_number=329, ID=2903, name="JOE", phone_number="2902", age=23)
        self.products = self.read_product_from_file()
        self.customer_names = []

    def display_menu(self):
        while True:
            print("-------- Shift Manager Menu --------")
            print("1. Sell product to customer")
            print("2. Add product to shelves")
            print("3. Remove product from shelves")
            print("4. Add employee")
            print("5. Update employee")
            print("6. Get customers with purchases")
            print("7. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.sell_product_to_customer()
            elif choice == "2":
                self.shift_manager.add_product_to_shelves()
            elif choice == "3":
                self.shift_manager.remove_product_from_shelves()
            elif choice == "4":
                self.add_employee()
            elif choice == "5":
                self.update_employee()
            elif choice == "6":
                self.get_customers_with_purchases()
            elif choice == "7":
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
        self.customer_names.append(customer_name)

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

    def get_customers_with_purchases(self):
        print("Customers with purchases:")
        for customer_name in self.customer_names:
            print(customer_name)

    def add_employee(self):
        # Logic to add an employee
        pass

    def update_employee(self):
        # Logic to update an employee
        pass


if __name__ == "__main__":
    shift_manager_menu = ShiftManagerMenu()
    shift_manager_menu.display_menu()

from data.file_handler import FileHandler
from entities.client import Client
import sys



class ClientMenu:

    def __init__(self):
        self.client = Client("29302", "93034", "MEO", "23",)

    def display_menu(self):
        while True:
            print("-------- Customer Menu --------")
            print("\n")
            print("1. Add product to shopping list")
            print("2. Show your products from shopping list")
            print("3. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_product_to_shopping_list()
            elif choice == "2":
                self.buy_products_from_shopping_list()
            elif choice == "3":
                print("\n")
                print("*** thank you and see you soon at the super ****")
                sys.exit()
            elif choice == "q":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_product_to_shopping_list(self):
        # Logic to add a product to the customer's shopping list
        product_name = input("Enter the product name: ")
        products_available = FileHandler.read_product_from_file()  # Read products from file

        while product_name != "" and product_name != "q":
            product_found = False
            for product in products_available:
                if product.name == product_name:
                    self.client.shopping_list.append(product)
                    print("Product added to shopping list.")
                    product_found = True
                    break

            if not product_found:
                print("Product not available.")

            product_name = input("Enter the product name: ")

        if product_name == "q":
            print("Exiting...")

    def buy_products_from_shopping_list(self):
        if not self.client.shopping_list:
            print("Shopping list is empty.")
            return

        total_cost = 0

        print("-------- Shopping List --------")
        for product in self.client.shopping_list:
            print(f"Product: {product.name}, Price: ${product.price}")
            total_cost += product.price

        #print("-------------------------")
        #print(f"Total cost: ${total_cost}")
        #print("Purchase completed.")

        # Clear the shopping list after the purchase
        #self.client.shopping_list = []

    #def read_products_from_file(self):
    #    products_available = []
    #    with open("C://Users//Mickael HALIMI//Documents//FinalSuper[1]//FinalSuper//data//products.txt", "r") as file:
    #        for line in file:
    #            product = line.strip().split(",")
    #            products_available.append(product[0])  # Assuming product name is in the first position
    #    return products_available

    #def get_product_cost(self, product_name):
        # Logic to retrieve the cost of a product from a data source (e.g., file, database)
    #    with open("C://Users//Mickael HALIMI//Documents//FinalSuper[1]//FinalSuper//data//products.txt", "r") as file:
    #        for line in file:
    #            product = line.strip().split(",")
    #            if product[0] == product_name:
    #                return product[2]  # Assuming product cost is in the second position

    #   return None

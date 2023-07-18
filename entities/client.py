from data.file_handler import FileHandler
from data.person import Person
from menu.chief_manager_menu import ChiefManagerMenu

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"


def print_color(text, color):
    print(color + text + RESET)


class Client(Person):
    def __init__(self, client_id, ID, name, age):
        super().__init__(ID, name, age)
        self.client_id = client_id
        self.shopping_list = []
        self.purchased_products = []

    def remove_product_from_shopping_list(self, product):
        if product in self.shopping_list:
            self.shopping_list.remove(product)

    def __str__(self):
        print(f"""customer id: {self.client_id}
shopping list :{self.shopping_list}
purchased products : {self.purchased_products}""")
        super().__str__()

    def __eq__(self, other):
        if isinstance(other, Client):
            return self.client_id == other.client_id
        return False

    def add_product_to_shopping_list(self):
        # Logic to add a product to the customer's shopping list
        product_name = input("Enter the product name: ")
        products_available = FileHandler.read_product_from_file()  # Read products from file

        while product_name != "" and product_name != "q":
            product_found = False
            for product in products_available:
                if product.name == product_name:
                    self.client.shopping_list.append(product)
                    print(GREEN, "Product added to shopping list.", RESET)
                    product_found = True
                    break

            if not product_found:
                print(RED, "Product not available.", RESET)

            product_name = input("Enter the product name: ")

        if product_name == "q":
            print(RED, "Exiting...")

    def buy_products_from_shopping_list(self):
        if not self.client.shopping_list:
            print(RED, "Shopping list is empty.")
            return

        total_cost = 0

        print("-------- Shopping List --------")
        for product in self.client.shopping_list:
            print(GREEN, f"Product: {product.name}, Price: ${product.price}", RESET)
            total_cost += product.price

    def get_customers_with_purchases(self):
        customers_with_purchases = ChiefManagerMenu.get_customers_with_purchases(self)

        if customers_with_purchases is not None:
            return list(customers_with_purchases)
        else:
            return []

    def calculate_revenue(self):
        chief_manager_menu = ChiefManagerMenu()
        customers_with_purchases = chief_manager_menu.get_customers_with_purchases()
        total_revenue = 0

        for customer in customers_with_purchases:
            customer_total = sum([product.price for product in customers_with_purchases[customer]])
            total_revenue += customer_total

        return total_revenue
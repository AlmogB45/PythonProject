from entities.client import Client


class ClientMenu:

    def display_menu(self):
        while True:
            print("-------- customer Menu --------")
            print("1. Add product to shopping list")
            print("2. Buy products from shopping list")
            print("3. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_product_to_shopping_list()
            elif choice == "2":
                self.buy_products_from_shopping_list()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    def add_product_to_shopping_list(self):
        client = Client("29302", "93034", "MEO", "23", "93094")
        # Logic to add a product to the customer's shopping list
        product_name = input("Enter the product name: ")
        products_available = self.read_products_from_file()  # Read products from file

        while product_name != "" and product_name != "q":
            if product_name in products_available:
                client.shopping_list.append(product_name)
                print("Product added to shopping list.")
                print(client.shopping_list)
            else:
                print("Product not available.")

            product_name = input("Enter the product name: ")

        if product_name == "q":
            print("Exiting...")

    def read_products_from_file(self):
        products_available = []
        with open("C:\\Users\\Almog-Laptop\\OneDrive\\Desktop\\FinalSuper\\menu\\products.txt", "r") as file:
            for line in file:
                product = line.strip().split(",")
                products_available.append(product[0])  # Assuming product name is in the first position
        return products_available

    def buy_products_from_shopping_list(self): # TODO Function not working, need to fix!
        if not self.client.shopping_list:
            print("The shopping list is empty.")
        else:
            total_price = 0
            purchase_history = []

            with open("C:\\Users\\Almog-Laptop\\OneDrive\\Desktop\\FinalSuper\\menu\\products.txt", "r") as file:
                products_info = [line.strip().split(",") for line in file]

            for product in self.client.shopping_list:
                found = False
                for info in products_info:
                    if info[0] == product:
                        price = float(info[2])
                        total_price += price
                        purchase_history.append(info)
                        found = True
                        break
                if not found:
                    print(f"Product '{product}' not found in the products list.")

            self.client.shopping_list = []
            print("Shopping list has been cleared.")
            print("Successfully Purchased.")
            print("Total Price:", total_price)

            # Save purchase history to a file
            with open("purchase_history.txt", "a") as file:
                for info in purchase_history:
                    file.write(",".join(info) + "\n")


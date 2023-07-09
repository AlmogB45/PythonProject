from entities.client import Client


class ClientMenu:
    #def __init__(self, client):
     #   self.client = client

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
        client = Client("29302","93034","MEO","23","93094")
        # Logic to add a product to the customer's shopping list
        product_name = input("Enter the product name: ")
        client.shopping_list.append(product_name)
        print("Product added to shopping list.")
        print(client.shopping_list)

    def buy_products_from_shopping_list(self):
        client = Client("29302","93034","MEO","23","93094")
      #  # Logic to buy products from the client's shopping list
       # if len(client.shopping_list) == 0:
        #    print("Shopping list is empty.")
       # else:
        #    for product in client.shopping_list:
                # Call the method to buy the product from a cashier
         #       client.buy_product(product)
          #  client.shopping_list.clear()
           # print("Products purchased successfully.")

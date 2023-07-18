from data.file_handler import FileHandler
from entities import client
from entities.client import Client
import sys

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"


def print_color(text, color):
    print(color + text + RESET)


class ClientMenu:

    def __init__(self):
        self.client = Client("29302", "93034", "MEO", "23",)

    def display_menu(self):
        while True:
            print(RED, "\n-------- Customer Menu --------\n", BLUE)
            print("1. Add product to shopping list" )
            print("2. Show your products from shopping list")
            print("3. Exit", RESET)

            choice = input("Enter your choice: ")
            if choice == "1":
                client.Client.add_product_to_shopping_list(self)
            elif choice == "2":
                client.Client.buy_products_from_shopping_list(self)
            elif choice == "3":
                print("\n")
                print(BLUE, "*** thank you and see you soon at the super ****")
                sys.exit()
            elif choice == "q":
                break
            else:
                print(RED, "Invalid choice. Please try again.")



import sys
from entities.sorter import Sorter

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"


def print_color(text, color):
    print(color + text + RESET)


class OrdererMenu:

    def __init__(self):
        self.sorter = Sorter(employee_number=28,employee_type="sorter",ID=121293,name="lkd",age=23)

    def display_menu(self):
        while True:
            print(RED, "-------- Orderer Menu --------\n", BLUE)
            print("1. Add product to shelves")
            print("2. Remove product from shelves")
            print("3. Exit", RESET)

            choice = input("Enter your choice: ")
            if choice == "1":
                self.sorter.add_product_to_shelves()
            elif choice == "2":
                self.sorter.remove_product_from_shelves()
            elif choice == "3":
                print("\n")
                print(BLUE, "*** thank you and see you soon at the super ***")
                sys.exit()
            elif choice == "q":
                break
            else:
                print(RED, "Invalid choice. Please try again.")



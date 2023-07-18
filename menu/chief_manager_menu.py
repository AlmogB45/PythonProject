from entities import chief_manager
import sys
from entities.chief_manager import ChiefManager
from entities.shift_manager import ShiftManager

RESET = "\033[0m"
RED = "\033[31m"
BLUE = "\033[34m"


def print_color(text, color):
    print(color + text + RESET)


class ChiefManagerMenu:
    def __init__(self):
        self.manager = ChiefManager(None, None, None, None, None)

    def display_menu(self):
        while True:
            print(RED, "\n-------- Chief Manager Menu --------\n", BLUE)
            print("1. Add employee")
            print("2. Remove employee")
            print("3. Get products on shelves")
            print("4. Sell products to costumer")
            print("5. Get costumers with purchases")
            print("7. Exit", RESET)

            choice = input("Enter your choice: ")
            if choice == "1":
                self.manager.add_employee()
            elif choice == "2":
                self.manager.remove_employee()
            elif choice == "3":
                self.manager.print_all_products()
            elif choice == "4":
                self.manager.sell_product_to_customer()
            elif choice == "5":
                self.manager.get_customers_with_purchases()
            elif choice == "7":
                print("\n")
                print(BLUE, "*** thank you and see you soon at the super ***")
                sys.exit()
            elif choice == "q":
                break
            else:
                print(RED, "Invalid choice. Please try again.")


if __name__ == "__main__":
    menu = ChiefManagerMenu(chief_manager)
    menu.display_menu()
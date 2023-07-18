import sys
from entities import cashier
from entities.cashier import Cashier

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
CYAN = "\033[36m"

def print_color(text, color):
    print(color + text + RESET)


class CashierMenu:
    def display_menu(self):
        while True:
            print(RED, "\n-------- Cashier Menu --------\n", BLUE)
            print("1. Sell product to customer")
            print("2. Exit", RESET)

            choice = input("Enter your choice: ")
            if choice == "1":
                print(CYAN, "\nPlease identify yourself and choose the register you wish to operate (1-10)\n", RESET)
                Cashier.register_number = int(input("Enter the register number: "))
                if Cashier.register_number > 10:
                    print(RED, "Invalid credentials, returning to home page")
                    break
                Cashier.name = input("Enter the name: ")
                cashier.Cashier(Cashier.name, Cashier.register_number, ID=0, age=0, phone_number=0).sell_product_to_customer()

            elif choice == "2":
                print("\n")
                print("*** thank you and see you soon at the super ***", BLUE)
                sys.exit()
            elif choice == "q":
                break
            else:
                print("Invalid choice. Please try again.", RED)

if __name__ == "__main__":
    cashier_menu = CashierMenu()
    cashier_menu.display_menu()



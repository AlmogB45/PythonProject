from entities.shift_manager import ShiftManager
import sys

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"


def print_color(text, color):
    print(color + text + RESET)


class ShiftManagerMenu:
    def __init__(self):
        self.shift_manager = ShiftManager(employee_number=329, ID=2903, name="JOE", phone_number="2902", age=23)
        # self.products = self.read_product_from_file()
        # self.customer_names = []

    def display_menu(self):
        while True:
            print(RED, "\n-------- Shift Manager Menu --------\n", BLUE)
            print("1. Sell product to customer")
            print("2. Add product to shelves")
            print("3. Remove product from shelves")
            print("4. Add employee")
            print("5. Remove employee")
            print("6. Get customers with purchases")
            print("7. Exit", RESET)

            choice = input("Enter your choice: ")
            if choice == "1":
                self.shift_manager.sell_product_to_customer()
            elif choice == "2":
                self.shift_manager.add_product_to_shelves()
            elif choice == "3":
                self.shift_manager.remove_product_from_shelves()
            elif choice == "4":
                self.shift_manager.add_employee()
            elif choice == "5":
                self.shift_manager.remove_employee()
            elif choice == "6":
                self.shift_manager.get_customers_with_purchases()
            elif choice == "7":
                print("\n")
                print(BLUE, "*** thank you and see you soon at the super ***")
                sys.exit()
            elif choice == "q":
                break
            else:
                print(RED, "Invalid choice. Please try again.")


if __name__ == "__main__":
    shift_manager_menu = ShiftManagerMenu()
    shift_manager_menu.display_menu()

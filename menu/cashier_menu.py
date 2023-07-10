import sys
from entities import cashier

from entities.cashier import Cashier


class CashierMenu:
    def display_menu(self):
        while True:
            print("-------- Cashier Menu --------")
            print("\n")
            print("1. Sell product to customer")
            print("2. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                print("Please identify yourself and choose the register you wish to operate (1-10)")
                register_number = int(input("Enter the register number: "))
                if register_number > 10:
                    print("Invalid credentials, returning to home page")
                    break
                employee_number = int(input("Enter the employee number: "))
                ID = int(input("Enter the ID: "))
                name = input("Enter the name: ")
                age = int(input("Enter the age: "))
                phone_number = input("Enter the phone number: ")
                cashier.Cashier(register_number, employee_number, ID, name, age,
                                phone_number).sell_product_to_customer()

            elif choice == "2":
                print("\n")
                print("*** thank you and see you soon at the super ***")
                sys.exit()
            elif choice == "q":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cashier_menu = CashierMenu()
    cashier_menu.display_menu()


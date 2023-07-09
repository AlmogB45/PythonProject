from entities.chief_manager import ChiefManager
from menu.client_menu import ClientMenu
from menu.orderer_menu import OrdererMenu
from menu.cashier_menu import CashierMenu
from menu.shift_manager_menu import ShiftManagerMenu
from menu.chief_manager_menu import ChiefManagerMenu


class MainMenu:

    def initialize_application(self):
        # Initialize the necessary objects
        chief_manager = ChiefManager(employee_number="1",employee_type="m", ID="123", name="patrick",age="21",
                                     phone_number="0232")

        # Initialize the menus
        client_menu = ClientMenu()
        orderer_menu = OrdererMenu()
        cashier_menu = CashierMenu()
        shift_manager_menu = ShiftManagerMenu()
        chief_manager_menu = ChiefManagerMenu(chief_manager)

        # Display the main menu
        while True:
            print("-------- Super App --------")
            print("1. Client")
            print("2. Orderer")
            print("3. Cashier")
            print("4. Shift Manager")
            print("5. Chief Manager")
            print("6. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                client_menu.display_menu()
            elif choice == "2":
                orderer_menu.display_menu()
            elif choice == "3":
                cashier_menu.display_menu()
            elif choice == "4":
                shift_manager_menu.display_menu()
            elif choice == "5":
                chief_manager_menu.display_menu()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Please try again.")
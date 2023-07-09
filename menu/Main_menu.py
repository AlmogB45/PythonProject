import self as self

from entities import chief_manager
from entities.chief_manager import ChiefManager
from menu.client_menu import ClientMenu
from menu.orderer_menu import OrdererMenu
from menu.cashier_menu import CashierMenu
from menu.shift_manager_menu import ShiftManagerMenu
from menu.chief_manager_menu import ChiefManagerMenu


class MainMenu:
    def initialize_application(self):



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
            print("2. Worker")

            choice = input("Enter your choice: ")
            if choice == "1":
                client_menu.display_menu()
            elif choice == "2":
                username = input("Enter your username: ")
                password = input("Enter your password: ")

                if self.validate_credentials(username, password):
                    while True:
                        print("-------- Worker Menu --------")
                        print("1. Cashier")
                        print("2. Shift Manager")
                        print("3. Chief Manager")
                        print("4. Back to Main Menu")

                        worker_choice = input("Enter your choice: ")
                        if worker_choice == "1":
                            cashier_menu.display_menu()
                        elif worker_choice == "2":
                            shift_manager_menu.display_menu()
                        elif worker_choice == "3":
                            chief_manager_menu.display_menu()
                        elif worker_choice == "4":
                            break
                        else:
                            print("Invalid choice. Please try again.")

    def validate_credentials(self, username, password):
        # Check the credentials against a file
        with open("C:\\Users\\Almog-Laptop\\OneDrive\\Desktop\\FinalSuper\\menu\\credentials.txt", "r") as file:
            for line in file:
                stored_username, stored_password = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    return True
        return False


# Example usage
# main_menu = MainMenu()
# main_menu.initialize_application()

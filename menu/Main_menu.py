from data.Login import Login
from menu.client_menu import ClientMenu
from menu.orderer_menu import OrdererMenu
from menu.cashier_menu import CashierMenu
from menu.shift_manager_menu import ShiftManagerMenu
from menu.chief_manager_menu import ChiefManagerMenu

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"


def print_color(text, color):
    print(color + text + RESET)


class MainMenu:
    def initialize_application(self):

        # Initialize the menus
        client_menu = ClientMenu()
        orderer_menu = OrdererMenu()
        cashier_menu = CashierMenu()
        shift_manager_menu = ShiftManagerMenu()
        chief_manager_menu = ChiefManagerMenu()

        # Display the main menu
        while True:
            print(RED, "\n-------- Super App --------\n", BLUE)
            print("1. Client")
            print("2. Worker\n", RESET)

            choice = input("Enter your choice: ")
            if choice == "1":
                client_menu.display_menu()
            elif choice == "2":
                username = input("\nEnter your username: ")
                password = input("Enter your password: ")
                login = Login(username,password)

                if login.validate_credentials():

                    if login.worker_type == "Cashier":
                        cashier_menu.display_menu()
                    elif login.worker_type == "Orderer":
                        orderer_menu.display_menu()
                    elif login.worker_type == "Shift Manager":
                        shift_manager_menu.display_menu()
                    elif login.worker_type == "Manager":
                        chief_manager_menu.display_menu()



# Example usage
# main_menu = MainMenu()
# main_menu.initialize_application()

import sys

class CashierMenu:
    #def __init__(self, cashier):
     #   self.cashier = cashier

    def display_menu(self):
        while True:
            print("-------- Cashier Menu --------")
            print("\n")
            print("1. Sell product to customer")
            print("2. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.sell_product_to_customer()
            elif choice == "2":
                print("\n")
                print("*** thank you and see you soon at the super ***")
                sys.exit()
            elif choice == "q":
                break
            else:
                print("Invalid choice. Please try again.")

    def sell_product_to_customer(self):
        # Logic to sell a product to a customer
        product_name = input("Enter the product name: ")
        customer_name = input("Enter the customer name: ")
        product = Product(product_name)
        customer = Customer(customer_name)
        self.cashier.sell_product(product, customer)
        print("Product sold to customer.")
from entities.employee import Employee
import sys

class ChiefManagerMenu:

    def display_menu(self):
        while True:
            print("-------- Chief Manager Menu --------")
            print("\n")
            print("1. Sell product to customer")
            print("2. Add product to shelves")
            print("3. Remove product from shelves")
            print("4. Add employee")
            print("5. Update employee")
            print("6. Get customers with purchases")
           # print("7. Get total daily revenue")
            print("7. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.sell_product_to_customer()
            elif choice == "2":
                self.add_product_to_shelves()
            elif choice == "3":
                self.remove_product_from_shelves()
            elif choice == "4":
                self.add_employee()
            elif choice == "5":
                self.update_employee()
            elif choice == "6":
                self.get_customers_with_purchases()
            #elif choice == "7":
            #    self.get_total_daily_revenue()
            elif choice == "7":
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
       # product = Product(product_name)
        #customer = Customer(customer_name)
        #self.chief_manager.sell_product(product, customer)
        print("Product sold to customer.")

    def add_product_to_shelves(self):
        # Logic to add a product to the supermarket shelves
        product_name = input("Enter the product name: ")
        department_name = input("Enter the department name: ")
        #product = Product(product_name)
        #department = Department(department_name)
        #self.chief_manager.add_product_to_shelves(product, department)
        print("Product added to shelves.")

    def remove_product_from_shelves(self):
        # Logic to remove a product from the supermarket shelves
        product_name = input("Enter the product name: ")
        department_name = input("Enter the department name: ")
        #product = Product(product_name)
       # department = Department(department_name)
        #self.chief_manager.remove_product_from_shelves(product, department)
        print("Product removed from shelves.")

    def add_employee(self):
        # Logic to add an employee
        employee_name = input("Enter the employee name: ")
        employee_type = input("Enter the employee type: ")
        employee = Employee(employee_name, employee_type)
        self.chief_manager.add_employee(employee)
        print("Employee added.")

    def update_employee(self):
        # Logic to update an employee
        employee_name = input("Enter the employee name: ")
        employee_type = input("Enter the employee type: ")
        employee = Employee(employee_name, employee_type)
        self.chief_manager.update_employee(employee)
        print("Employee updated.")

    def get_customers_with_purchases(self):
        # Logic to get customers with purchases
        purchases = self.chief_manager.get_customers_with_purchases()
        if purchases:
            print("Customers with purchases:")
            for customer, products in purchases.items():
                print(f"Customer: {customer}")
                print("Purchased Products:")
                for product in products:
                    print(f"- {product}")
                print()
        else:
            print("No customers with purchases.")

    #def get_total_daily_revenue(self):
        # Logic to get the total daily revenue
     #   revenue = self.chief_manager.get_total_daily

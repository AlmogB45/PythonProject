
class OrdererMenu:
    #def __init__(self, orderer):
     #   self.orderer = orderer

    def display_menu(self):
        while True:
            print("-------- Orderer Menu --------")
            print("1. Add product to shelves")
            print("2. Remove product from shelves")
            print("3. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                self.add_product_to_shelves()
            elif choice == "2":
                self.remove_product_from_shelves()
            elif choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")

    #def add_product_to_shelves(self):

        #Logic to add a product to the supermarket shelves
       #product_name = input("Enter the product name: ")
        #department_name = input("Enter the department name: ")
        #product = Product(product_name)
        #department = Department(department_name)
        #self.orderer.add_product_to_shelves(product, department)
        #print("Product added to shelves.")

    def remove_product_from_shelves(self):
        # Logic to remove a product from the supermarket shelves
        product_name = input("Enter the product name: ")
        department_name = input("Enter the department name: ")
        product = Product(product_name)
        department = Department(department_name)
        self.orderer.remove_product_from_shelves(product, department)
        print("Product removed from shelves.")

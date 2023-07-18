from entities.Product import Product


class FileHandler:
    @staticmethod
    def read_product_from_file():
        products = []

        try:
            with open("C:\\Users\\Almog-Laptop\\OneDrive\\Desktop\\FinalSuper\\data\\products.txt", 'r') as file:
                for line in file:
                    data = line.strip().split(",")

                    if len(data) == 3:
                        name = data[0]
                        type = data[1]
                        price = float(data[2])  # Convert the price to float

                        prod = Product(name, type, price)
                        products.append(prod)

        except IOError as e:
            print("Error reading file:", e)

        return products

    @staticmethod
    def write_product_to_file(product):
        try:
            with open("C:\\Users\\Almog-Laptop\\OneDrive\\Desktop\\FinalSuper\\data\\products.txt",
                      'a') as file:
                file.write(f"{product.name},{product.type},{product.price}\n")
        except IOError as e:
            print("Error writing to file:", e)

    @staticmethod
    def remove_product_from_file(product_name):
        try:
            lines = []
            with open("C:\\Users\\Almog-Laptop\\OneDrive\\Desktop\\FinalSuper\\data\\products.txt",
                      'r') as file:
                lines = file.readlines()

            with open("C:\\Users\\Almog-Laptop\\OneDrive\\Desktop\\FinalSuper\\data\\products.txt",
                      'w') as file:
                for line in lines:
                    product = line.strip().split(",")
                    if product[0] != product_name:
                        file.write(line)
        except IOError as e:
            print("Error removing product from file:", e)

    @classmethod
    def get_customers_with_purchases(cls):
        pass


from entities.Product import Product
import os


class FileHandler:

    # returns the file path of products.txt based on user's home directory
    @staticmethod
    def get_products_file_path():
        file_path = os.path.join(os.path.dirname(__file__), 'products.txt')
        return file_path

    @staticmethod
    def read_product_from_file():
        products = []

        try:
            with open(FileHandler.get_products_file_path(),
                      'r') as file:
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
            with open(FileHandler.get_products_file_path(),
                      'a') as file:
                file.write(f"{product.name},{product.type},{product.price}\n")
        except IOError as e:
            print("Error writing to file:", e)

    @staticmethod
    def remove_product_from_file(product_name):
        try:
            lines = []
            with open(FileHandler.get_products_file_path(),
                      'r') as file:
                lines = file.readlines()

            with open(FileHandler.get_products_file_path(),
                      'w') as file:
                for line in lines:
                    product = line.strip().split(",")
                    if product[0] != product_name:
                        file.write(line)
        except IOError as e:
            print("Error removing product from file:", e)


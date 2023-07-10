from data.person import Person


class Client(Person):
    def __init__(self, client_id, ID, name, age):
        super().__init__(ID, name, age)
        self.client_id = client_id
        self.shopping_list = []
        self.purchased_products = []

    def remove_product_from_shopping_list(self, product):
        if product in self.shopping_list:
            self.shopping_list.remove(product)

    def __str__(self):
        print(f"""customer id: {self.client_id}
shopping list :{self.shopping_list}
purchased products : {self.purchased_products}""")
        super().__str__()

    def __eq__(self, other):
        if isinstance(other, Client):
            return self.client_id == other.client_id
        return False

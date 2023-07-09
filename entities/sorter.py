from data.logistic import ILogistic
from data.person import Person
from entities.employee import Employee


class Sorter(Employee,ILogistic):
    def __init__(self, employee_number: int, ID: int, name: str, age: int, phone_number: str):
        super().__init__(employee_number, ID, name, age, phone_number)
        self.vest_color = "yellow"

    def add_product_to_shelves(self, product, department):
        department.add_product(product)

    def remove_product_from_shelves(self, product, department):
        department.remove_product(product)

    def __str__(self):
        print(f""""vest color: {self.vest_color}
employee number: {self.employee_number}""")
        super().__str__()
    
    def __eq__(self, other):
        if isinstance(other, Sorter):
            return self.employee_number == other.employee_number
        return False


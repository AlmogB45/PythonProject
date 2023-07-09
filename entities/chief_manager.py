from data.manager import IManager
from entities.employee import Employee


class ChiefManager(Employee,IManager):
    def __init__(self, employee_number,employee_type, ID, name, age, phone_number):
        super().__init__(employee_number,employee_type, ID, name, age, phone_number)

    def add_employee(self, employee, employee_list):
        employee_list.append(employee)

    def remove_employee(self, employee, employee_list):
        if employee in employee_list:
            employee_list.remove(employee)

    def get_products_on_shelves(self, department):
        return department.get_products()

    def get_client_purchases(self, date, client_list=None):
        purchases = []
        for client in client_list:
            if date == client.purchase_date:
                purchases.append(client.purchased_products)
        return purchases

    def get_total_revenue(self, client_list, date):
        total_revenue = 0
        for client in client_list:
            if date == client.purchase_date:
                for product in client.purchased_products:
                    total_revenue += product.price
        return total_revenue

    def __str__(self):
        print(f"employee number: {self.employee_number}")
        super().__str__()
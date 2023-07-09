from abc import ABC


class IManager(ABC):
    def add_employee(self, employee, employee_list):
        pass

    def remove_employee(self, employee, employee_list):
        pass

    def get_total_revenue(self, customer_list, date):
       pass
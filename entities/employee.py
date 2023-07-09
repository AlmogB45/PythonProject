from data.person import Person


class Employee(Person):
    def __init__(self, employee_number,employee_type, ID, name: str, age, phone_number: str):
        super().__init__(ID, name, age, phone_number)
        self.employee_number = employee_number
        self.employee_type: str = employee_type

    def __str__(self):
        print(f"""Employee number: {self.employee_number}
Employee type: {self.employee_type}""")

    def __eq__(self, other):
        if isinstance(other, Employee):
            return self.employee_number == other.employee_number
        return False

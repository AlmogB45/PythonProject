from data.person import Person


class Employee(Person):
    def __init__(self,employee_type,passWord, ID, userName: str, age):
        super().__init__(ID, userName, age)
        self.employee_type: str = employee_type
        self.passWord = passWord

    def __str__(self):
        print(f"Employee type: {self.employee_type}")

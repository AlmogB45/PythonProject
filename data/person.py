from abc import ABC


class Person(ABC):
    def __init__(self, ID, name, age, phone_number):
        self.ID = ID
        self.name = name
        self.age = age
        self.phone_number = phone_number

    def __str__(self):
        print(
            f"""id:{self.ID}
name:{self.name}
age:{self.age}
tel:{self.phone_number}
""")

    def __eq__(self, other):
        pass

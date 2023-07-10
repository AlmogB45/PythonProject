from abc import ABC


class Person(ABC):
    def __init__(self, ID, name, age):
        self.ID = ID
        self.name = name
        self.age = age

    def __str__(self):
        print(
            f"""id:{self.ID}
name:{self.name}
age:{self.age}
tel:{self.phone_number}
""")

    def __eq__(self, other):
        pass

from entities.employee import Employee


def read_users_from_file():
    users = []

    try:
        with open("/data/workers.txt", 'r') as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 5:
                    employee_number = data[0]
                    employee_type = data[1]
                    ID = data[2]
                    name = data[3]
                    age = data[4]
                    phone_number = data[5]

                    user = Employee(employee_number, employee_type, ID, name, age, phone_number)
                    users.append(user)

    except IOError as e:
        print("Error reading file:", e)

    return users

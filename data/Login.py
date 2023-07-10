class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.stored_username = None
        self.stored_password = None
        self.worker_type = None

        with open("C://Users//Mickael HALIMI//Documents//FinalSuper[1]//FinalSuper//data//credentials.txt",
                  "r") as file:
            for line in file:
                stored_username, stored_password, worker_type = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    self.stored_username = stored_username
                    self.stored_password = stored_password
                    self.worker_type = worker_type
                    break

    def validate_credentials(self):
        with open("C://Users//Mickael HALIMI//Documents//FinalSuper[1]//FinalSuper//data//credentials.txt",
                  "r") as file:
            for line in file:
                stored_username, stored_password, worker_type = line.strip().split(",")
                if self.username == stored_username and self.password == stored_password:
                    return True
        return False

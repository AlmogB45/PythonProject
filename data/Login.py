import os


class Login:
    
    # returns the file path of products.txt based on user's home directory
    @staticmethod
    def get_credentials_file_path():
        file_path = os.path.join(os.path.dirname(__file__), 'credentials.txt')
        return file_path
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.stored_username = None
        self.stored_password = None
        self.worker_type = None

        with open(Login.get_credentials_file_path(),
                  "r") as file:
            for line in file:
                stored_username, stored_password, worker_type = line.strip().split(",")
                if username == stored_username and password == stored_password:
                    self.stored_username = stored_username
                    self.stored_password = stored_password
                    self.worker_type = worker_type
                    break

    def validate_credentials(self):
        with open(Login.get_credentials_file_path(),
                  "r") as file:
            for line in file:
                stored_username, stored_password, worker_type = line.strip().split(",")
                if self.username == stored_username and self.password == stored_password:
                    return True
        return False

    class EmployeeManager:
        @staticmethod
        def add_employee(username, password, worker_type):
            new_credentials = f"{username},{password},{worker_type}\n"

            with open(Login.get_credentials_file_path(), "a") as file:
                file.write(new_credentials)


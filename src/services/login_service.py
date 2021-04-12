from services.database_operations import(
    add_user,
    get_credentials,
)

class LoginService():
    def __init__(self, window):
        self.window = window

    def check_username_length(self, username):
        return bool(len(username) >= 3)

    def check_username_and_password(self, username, password):
        return bool((username, password) in get_credentials())

    def check_credentials_not_matching(self, username):
        return bool([item for item in get_credentials() if item[0] == username])

    def register_new_user(self, username, password):
        add_user(username, password)
        return True

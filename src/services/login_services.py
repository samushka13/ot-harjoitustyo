from repositories.database_services import database_services as default_database


class LoginServices:
    """Class that describes all login-related services.

    Attributes:
        database: The current database.
    """

    def __init__(self, database=default_database):
        """Class constructor that initializes the class
        with an appropriate database service.

        Args:
            database: The current database.
        """

        self.database = database

    def check_username_length(self, username):
        """Checks the length of the username.

        Args:
            username (str): The user's username.

        Returns:
            True, if the username is long enough, or False, if it's not.
        """

        return bool(len(username) >= 3)

    def check_username_and_password(self, username, password):
        """Checks if the input credentials already exist.

        Args:
            username (str): The user's username.
            password (str): The user's password.

        Returns:
            True, if the credentials exist, or False, if they don't.
        """

        return bool((username, password) in self.database.get_credentials())

    def check_credentials_not_matching(self, username):
        """Checks if the username doesn't match the password.

        Args:
            username (str): The user's username.

        Returns:
            True, if the username and password doesn't match, or False, if they do.
        """

        return bool([item for item in self.database.get_credentials() if item[0] == username])

    def register_new_user(self, username, password):
        """Calls a DatabaseServices method which adds the new user to the database.

        Args:
            username (str): The user's username.
            password (str): The user's password.
        """

        self.database.add_user(username, password)

    def check_registration_success(self, new_user):
        """Checks if the newly added user is in the database.

        Args:
            new_user (str): The new user's username.

        Returns:
            True, if the new user is in the database, or False, if not.
        """

        return bool(new_user in self.database.get_users())

    def check_for_users(self):
        """Checks if any users exist.

        Returns:
            True, if any exist, or False, if none exist.
        """

        return bool(len(self.list_all_users()) > 0)

    def list_all_users(self):
        """Calls a DatabaseServices class method which returns a list of users.

        Returns:
            users (list): A sorted, formatted list of all users.
        """

        users = '\n'.join(sorted(self.database.get_users()))

        return users

    def handle_login(self, current_user):
        """Destroys the current view and initializes a new one.

        Args:
            current_user (str): The current user's username.
        """

        self.database.remove_logged_in_users()
        self.database.add_logged_in_user(current_user)


login_services = LoginServices()

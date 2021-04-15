from ui.settings_view import SettingsView
from ui.dialogs import whats_new_dialog
from entities.user import User

class LoginServices:
    """Class that describes login-related services.

    Attributes:
        window: Value of the current view's window.
    """

    def __init__(self, window, database):
        """Class constructor that initializes the login-related services.

        Args:
            window: Value of the current view's window.
        """

        self.window = window
        self.database = database

    def check_username_length(self, username):
        """Checks the length of the username.

        Args:
            username: String value of the user's username.
        Returns:
            True, if the username is long enough, or False, if it's not.
        """

        return bool(len(username) >= 3)

    def check_username_and_password(self, username, password):
        """Checks if the credentials are already in the database.

        Args:
            username: String value of the user's username.
            password: String value of the user's password.
        Returns:
            True, if the credentials are in the database, or False, if they're not.
        """

        return bool((username, password) in self.database.get_credentials())

    def check_credentials_not_matching(self, username):
        """Checks if the username doesn't match the password.

        Args:
            username: String value of the user's username.
        Returns:
            True, if the username and password doesn't match, or False, if they do.
        """

        return bool([item for item in self.database.get_credentials() if item[0] == username])

    def register_new_user(self, username, password):
        """Calls a database_services method that adds the new user to the database.

        Args:
            username: String value of the user's username.
            password: String value of the user's password.
        Returns:
            The result of a database operation method call,
            which in this case is a tuple of the user's username and password.
        """

        return self.database.add_user(User(username, password))

    def check_registration_success(self, new_user):
        """Checks if the newly added user is in the database.

        Args:
            new_user: String value of the user's username.
        Returns:
            True, if the user is in the database, or False, if not.
        """

        return bool(new_user in self.database.get_users())

    def check_for_users(self):
        """Checks if there are any users in the database.
        
        Returns:
            True, if any exist, or False, if none exist.
        """

        return bool(len(self.database.get_sorted_users()) > 0)

    def list_all_users(self):
        """Calls a database_services method that returns
        all users in a formatted list.
        
        Returns:
            A sorted list of all users by calling a database operation.
        """

        return self.database.get_sorted_users()

    def handle_view_change(self, window, current_user):
        """Destroys the current view and initializes a new one.

        Args:
            window: Value of the current view's window.
            current_user: String value of the user's username.
        """

        # The dialog will be removed eventually.
        if whats_new_dialog() == 'ok':
            self.database.remove_logged_in_users()
            self.database.add_logged_in_user(current_user)
            window.destroy()
            SettingsView(self.database)

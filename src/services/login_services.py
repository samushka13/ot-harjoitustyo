from services.settings_services import SettingsServices
from ui.settings import SettingsView
from entities.user import User
from ui.dialogs import whats_new_dialog

class LoginServices():
    """Class that describes login-related services.

    Attributes:
        window: Value of the current view's window.
        database: Value of the current database.
    """

    def __init__(self, window, database):
        """Class constructor that initializes the login-related services.

        Args:
            window: Value of the current view's window.
            database: Value of the current database.
        """

        self.window = window
        self.database = database

    def check_username_length(self, username):
        """Checks the username's length and
        returns True, if it's long enough, or False, if it isn't.

        Args:
            username: String value of the user's username.
        """

        return bool(len(username) >= 3)

    def check_username_and_password(self, username, password):
        """Checks if the credentials are already in the database and
        returns True, if they are, or False, if they aren't.

        Args:
            username: String value of the user's username.
            password: String value of the user's password.
        """

        return bool((username, password) in self.database.get_credentials())

    def check_credentials_not_matching(self, username):
        """Checks if the username doesn't match the password and
        returns True, if it doesn't, or False, if it does.

        Args:
            username: String value of the user's username.
        """

        return bool([item for item in self.database.get_credentials() if item[0] == username])

    def register_new_user(self, username, password):
        """Calls a database_services method that adds the new user to the database.

        Args:
            username: String value of the user's username.
            password: String value of the user's password.
        """

        return self.database.add_user(User(username, password))

    def check_registration_success(self, new_user):
        """Checks if the newly added user is in the database and
        returns True, if it is, or False, if it isn't.

        Args:
            new_user: String value of the user's username.
        """

        return bool(new_user.username in self.database.get_users())

    def check_for_users(self):
        """Checks if there are any users in the database and
        returns True, if there is, or False, if there isn't."""

        return bool(len(self.database.get_sorted_users()) > 0)

    def list_all_users(self):
        """Calls a database_services method that returns
        all users in a formatted list."""

        return self.database.get_sorted_users()

    def handle_view_change(self, window, current_user):
        """Destroys the current view and opens a new one.

        Args:
            window: Value of the current view's window.
            current_user: String value of the user's username.
        """

        # The dialog will be removed eventually.
        if whats_new_dialog() == 'ok':
            window.destroy()
            return SettingsView(SettingsServices(current_user, self.database))

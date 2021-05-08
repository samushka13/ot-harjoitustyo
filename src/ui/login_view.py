import tkinter as tk
from services.login_services import login_services
from ui.settings_view import settings_view
from ui.widgets import (
    title_label,
    basic_label,
    button,
    entry,
)
from ui.dialogs import (
    show_invalid_username_dialog,
    show_login_error_dialog,
    show_login_success_dialog,
    show_username_created_dialog,
    show_registration_error_dialog,
    show_users_dialog,
    show_no_users_dialog,
)
from ui.stylings import (
    get_window_settings,
    LOGIN_WINDOW_NAME,
    LOGIN_WINDOW_SIZE,
    X,
    Y,
)


class LoginView:
    """Class that describes the UI of the login view.

    Attributes:
        service: The current services class entity.
    """

    def __init__(self, service=login_services):
        """Class constructor that initializes the class with
        appropriate services and attributes.

        Args:
            service: The current services class entity.
        """

        self.service = service
        self.window = None
        self.username_input = None
        self.password_input = None

    def initialize_window(self):
        """Initializes the window with appropriate settings and widgets."""

        self.window = tk.Tk()
        get_window_settings(self.window, LOGIN_WINDOW_NAME, LOGIN_WINDOW_SIZE)
        self._build_layout()
        self._build_title()
        self.username_input = self._build_username_widgets()
        self.password_input = self._build_password_widgets()
        self._build_action_buttons()
        self.window.mainloop()

    def _build_layout(self):
        """Builds the layout of the parent window.
        Essentially just a bunch of row and column configurations."""

        for i in (0,5):
            self.window.grid_rowconfigure(i, weight=2)
        for i in range(1,5):
            self.window.grid_rowconfigure(i, weight=0)
        for i in (0,1):
            self.window.grid_columnconfigure(i, weight=1)

    def _build_title(self):
        """Builds the title of the view."""

        title_label(self.window, "Login or Create Username"
        ).grid(column=0, row=0, columnspan=2, padx=X)

    def _build_username_widgets(self):
        """Builds the username subtitle and entry field (with focus).

        Returns:
            username_entry (widget): The username input field.
        """

        basic_label(self.window, "Username",
        ).grid(column=0, row=1, columnspan=2, pady=Y)

        username_entry = entry(self.window, 30)
        username_entry.grid(column=0, row=2, columnspan=2)
        username_entry.focus()

        return username_entry

    def _build_password_widgets(self):
        """Builds the password subtitle and entry field (with focus).

        Returns:
            password_entry (widget): The password input field.
        """

        basic_label(self.window, "Password",
        ).grid(column=0, row=3, columnspan=2, pady=Y)

        password_entry = entry(self.window, 30, "*")
        password_entry.grid(column=0, row=4, columnspan=2)

        return password_entry

    def _build_action_buttons(self):
        """Builds the action buttons of the parent view."""

        button(self.window, "Proceed", self._handle_login_event,
        ).grid(column=0, row=5, padx=X, pady=Y, sticky="e")

        button(self.window, "Users", self._show_users,
        ).grid(column=1, row=5, padx=X, pady=Y, sticky="w")

    def _handle_login_event(self):
        """Checks credentials with the help of LoginServices
        and accommodates the UI accordingly."""

        username = self.username_input.get()
        password = self.password_input.get()

        if self.service.check_username_length(username) is False:
            self._handle_invalid_username()
        elif self.service.check_username_and_password(username, password) is True:
            self._handle_successful_login(username)
        else:
            if self.service.check_credentials_not_matching(username) is True:
                self._handle_no_credentials_match()
            else:
                self.service.register_new_user(username, password)
                if self.service.check_registration_success(username) is True:
                    self._handle_successful_registration(username)
                else:
                    self._handle_unsuccessful_registration()

    def _handle_invalid_username(self):
        """Shows an appropriate dialog after which
        provides focus on the username entry widget."""

        show_invalid_username_dialog()
        self.window.focus()
        self.username_input.focus()

    def _handle_no_credentials_match(self):
        """Shows an appropriate dialog after which
        provides focus on the username entry widget."""

        show_login_error_dialog()
        self.window.focus()
        self.username_input.focus()

    def _handle_successful_login(self, username):
        """Shows an appropriate dialog after which
        closes the current window and opens a new one.

        Args:
            username: String value of the user's username.
        """

        show_login_success_dialog(username)
        self._handle_view_change(username)

    def _handle_successful_registration(self, username):
        """Shows an appropriate dialog after which
        calls another method that handles the view change.

        Args:
            username: String value of the user's username.
        """

        show_username_created_dialog(username)
        self._handle_view_change(username)

    def _handle_unsuccessful_registration(self):
        """Shows an appropriate dialog after which
        provides focus on the username entry widget."""

        show_registration_error_dialog()
        self.window.focus()
        self.username_input.focus()

    def _show_users(self):
        """Shows a dialog with a list of registered usernames.
        Closing the dialog provides focus on the username entry widget."""

        if self.service.check_for_users() is True:
            show_users_dialog(self.service.list_all_users())
        else:
            show_no_users_dialog()

        self.window.focus()
        self.username_input.focus()

    def _handle_view_change(self, current_user):
        """Destroys the current window and initializes a new one.

        Args:
            current_user (str): The current user's username.
        """

        self.service.handle_login(current_user)
        self.window.destroy()
        settings_view.initialize_window()


login_view = LoginView()

import tkinter as tk
from services.ui_services import get_window_settings
from services.login_service import LoginService
from services.view_manager import open_settings_view
from ui.stylings import (
    LOGIN_WINDOW_NAME,
    LOGIN_WINDOW_SIZE,
    X,
    Y,
)
from ui.dialogs import (
    show_invalid_username_dialog,
    show_login_error_dialog,
    show_login_success_dialog,
    show_username_created_dialog,
    show_users_dialog,
)
from ui.widgets import (
    get_title_label,
    get_basic_label,
    get_basic_button,
    get_basic_entry,
)

class LoginView:
    def __init__(self):
        """Initializes the window with appropriate settings, services and widgets."""

        self.window = tk.Tk()
        get_window_settings(
            self.window,
            LOGIN_WINDOW_NAME,
            LOGIN_WINDOW_SIZE,
        )
        self.service = LoginService(self.window)
        self._build_layout()
        self._build_title()
        self.username_input = self._build_username_widgets()
        self.password_input = self._build_password_widgets()
        self._build_action_buttons()
        self.window.mainloop()

    def _build_layout(self):
        """Builds the layout of the parent view."""

        for i in (0,5):
            self.window.grid_rowconfigure(i, weight=2)
        for i in (1,2,3,4,6):
            self.window.grid_rowconfigure(i, weight=0)
        for i in (0,1):
            self.window.grid_columnconfigure(i, weight=1)

    def _build_title(self):
        """Builds the title of the view."""

        get_title_label(
            self.window,
            "Login or Create Username"
        ).grid(column=0, row=0, columnspan=2, padx=X)

    def _build_username_widgets(self):
        """Builds the username subtitle and entry field (with focus)."""

        get_basic_label(
            self.window,
            "Username",
        ).grid(column=0, row=1, columnspan=2, pady=Y)

        username_entry = get_basic_entry(self.window, 30)
        username_entry.grid(column=0, row=2, columnspan=2)
        username_entry.focus()

        return username_entry

    def _build_password_widgets(self):
        """Builds the password subtitle and entry field (with focus)."""

        get_basic_label(
            self.window,
            "Password",
        ).grid(column=0, row=3, columnspan=2, pady=Y)

        password_entry = get_basic_entry(self.window, 30, "*")
        password_entry.grid(column=0, row=4, columnspan=2)

        return password_entry

    def _build_action_buttons(self):
        """Builds the action buttons of the parent view."""

        get_basic_button(
            self.window,
            "Proceed",
            10,
            self._handle_login,
        ).grid(column=0, row=5, padx=X, pady=Y, sticky="e")

        get_basic_button(
            self.window,
            "Users",
            10,
            self._show_users,
        ).grid(column=1, row=5, padx=X, pady=Y, sticky="w")

    def _handle_login(self):
        """Checks credentials with the help of LoginService
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
                self._handle_successful_registration(username)

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
        closes the current window and opens a new one."""

        show_login_success_dialog(username)
        open_settings_view(self.window)

    def _handle_successful_registration(self, username):
        """Shows an appropriate dialog after which
        closes the current window and opens a new one."""

        show_username_created_dialog(username)
        open_settings_view(self.window)

    def _show_users(self):
        """Shows a dialog with a list of registered usernames.
        Closing the dialog provides focus on the username entry widget."""

        if show_users_dialog() == 'ok':
            self.window.focus()
            self.username_input.focus()

import tkinter as tk
from services.database_operations import(
    add_user,
    get_credentials,
)
from services.ui_services import get_window_settings
from ui.settings import SettingsView
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
        self.window = tk.Tk()
        get_window_settings(
            self.window,
            LOGIN_WINDOW_NAME,
            LOGIN_WINDOW_SIZE,
        )

        # ------------------------------------------------------
        # Row and column configurations:
        # ------------------------------------------------------

        for i in (0,5):
            self.window.grid_rowconfigure(i, weight=2)
        for i in (1,2,3,4,6):
            self.window.grid_rowconfigure(i, weight=0)
        for i in (0,1):
            self.window.grid_columnconfigure(i, weight=1)

        # ------------------------------------------------------
        # Widgets:
        # ------------------------------------------------------

        get_title_label(
            self.window,
            "Login or Create Username"
        ).grid(column=0, row=0, columnspan=2, padx=X)

        get_basic_label(
            self.window,
            "Username",
        ).grid(column=0, row=1, columnspan=2, pady=Y)

        self.username_input = get_basic_entry(self.window, 30)
        self.username_input.grid(column=0, row=2, columnspan=2)
        self.username_input.focus()

        get_basic_label(
            self.window,
            "Password",
        ).grid(column=0, row=3, columnspan=2, pady=Y)

        self.password_input = get_basic_entry(self.window, 30, "*")
        self.password_input.grid(column=0, row=4, columnspan=2)

        get_basic_button(
            self.window,
            "Proceed",
            10,
            self.check_credentials,
        ).grid(column=0, row=5, padx=X, pady=Y, sticky="e")

        get_basic_button(
            self.window,
            "Users",
            10,
            self.show_users,
        ).grid(column=1, row=5, padx=X, pady=Y, sticky="w")

        self.window.mainloop()

    # ------------------------------------------------------
    # Functions that handle button commands:
    # ------------------------------------------------------

    def check_credentials(self):
        if len(self.username_input.get()) < 3:
            show_invalid_username_dialog()
            self.window.focus()
            self.username_input.focus()
        elif (self.username_input.get(), self.password_input.get()) in get_credentials():
            show_login_success_dialog(self.username_input.get())
            self.open_settings_view()
        else:
            if [item for item in get_credentials() if item[0] == self.username_input.get()]:
                show_login_error_dialog()
                self.window.focus()
                self.username_input.focus()
            else:
                add_user(self.username_input.get(), self.password_input.get())
                show_username_created_dialog(self.username_input.get())
                self.open_settings_view()

    def show_users(self):
        if show_users_dialog() == 'ok':
            self.window.focus()
            self.username_input.focus()

    # ------------------------------------------------------
    # Function that handles view changes:
    # ------------------------------------------------------

    def open_settings_view(self):
        self.window.destroy()
        SettingsView()

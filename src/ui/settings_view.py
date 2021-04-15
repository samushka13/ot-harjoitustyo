import tkinter as tk
from services.settings_services import SettingsServices
from ui.custom_content_view import CustomContentView
from ui.rules_view import RulesView
from ui.stylings import (
    get_window_settings,
    SETTINGS_WINDOW_NAME,
    SETTINGS_WINDOW_SIZE,
    X,
    Y,
)
from ui.widgets import (
    get_title_label,
    get_basic_label,
    get_basic_button,
    get_combobox,
)
from ui.dialogs import (
    show_player_number_error_dialog,
    show_player_name_error_dialog,
    show_category_number_error_dialog,
    show_game_not_ready_dialog,
)

class SettingsView:
    """Class that describes the UI of the settings view."""

    def __init__(self, database):
        """Class constructor that initializes the window
        with appropriate settings, services and widgets."""

        self.window = tk.Tk()
        get_window_settings(self.window, SETTINGS_WINDOW_NAME, SETTINGS_WINDOW_SIZE)
        self.database = database
        self.service = SettingsServices(self.window, self.database)
        self._build_layout()
        self._build_widgets()
        self.window.mainloop()

    def _build_layout(self):
        """Builds the layout of the parent window.
        Essentially just a bunch of row and column configurations."""

        for i in (0,14):
            self.window.grid_rowconfigure(i, weight=1)
        for i in range(1,14):
            self.window.grid_rowconfigure(i, weight=0)
        for i in (0,1,2):
            self.window.grid_columnconfigure(i, weight=1)

    def _build_widgets(self):
        """Builds the widgets of the parent window."""

        get_title_label(
            self.window,
            "Game Settings"
        ).grid(column=0, row=0, columnspan=3)

        get_basic_label(
            self.window,
            "Players"
        ).grid(column=0, row=1, pady=Y)
        self.players = self._build_player_entries()

        get_basic_label(
            self.window,
            "Categories"
        ).grid(column=1, row=1, pady=Y)
        self.categories = self._build_category_comboboxes()

        get_basic_label(
            self.window,
            "Board Size"
        ).grid(column=2, row=1, pady=Y)
        self.board_size = self._build_board_size_combobox()

        get_basic_button(
            self.window,
            "Game Rules",
            self._open_rules_view
        ).grid(column=0, row=14, padx=X)

        get_basic_button(
            self.window,
            "Start Game",
            self._handle_game_start
        ).grid(column=2, row=14, padx=X)

        get_basic_button(
            self.window,
            "  Logout  ",
            self._handle_logout
        ).grid(column=0, row=0, padx=X)

        get_basic_button(
            self.window,
            "Custom Content",
            self._open_questions_view
        ).grid(column=2, row=0, padx=X)

    def _build_player_entries(self):
        """Builds the player name entry widgets.

        Returns:
            List of entry fields.
        """

        entry_fields = []
        i = 0
        for i in range(0,6):
            entry_field = get_combobox(self.window)
            entry_field['values'] = self.service.get_default_players()
            if i == 0:
                entry_field.set(f"{self.service.get_default_players()[0]}")
            else:
                entry_field.set("Add player")
            entry_field.grid(column=0, row=2+i, padx=X)
            entry_fields.append(entry_field)
            i += 1
        entry_fields[0].focus()
        return entry_fields

    def _build_category_comboboxes(self):
        """Builds the category selection widgets.

        Returns:
            List of comboboxes.
        """

        comboboxes = []
        i = 0
        for i in range(0,12):
            category_combobox = get_combobox(self.window)
            categories = self.service.get_categories()
            category_combobox['values'] = categories
            category_combobox.state(['readonly'])
            category_combobox.set("Add category")

            # This fills the categories automatically with existing values.
            #
            # if len(categories) < 12:
            #     if len(categories) == 0:
            #         category_combobox.set("")
            #     else:
            #         if i < len(categories):
            #             category_combobox.set(categories[i])
            #         else:
            #             category_combobox.set(categories[i-len(categories)])

            category_combobox.grid(column=1, row=2+i)
            comboboxes.append(category_combobox)
            i += 1
        return comboboxes

    def _build_board_size_combobox(self):
        """Builds the board size selection widget.

        Returns:
            A combobox.
        """

        board_size_combobox = get_combobox(self.window)
        board_size_combobox['values'] = [x[0] for x in self.service.get_default_board_sizes()]
        board_size_combobox.state(['readonly'])
        board_size_combobox.set(self.service.get_default_board_sizes()[2][0])
        board_size_combobox.grid(column=2, row=2, padx=X)
        return board_size_combobox

    def _handle_game_start(self):
        """Calls SettingsServices class methods which collect and
        validate the selected settings and accommodates the UI accordingly."""

        self.service.collect_player_settings(self.players)
        self.service.collect_category_settings(self.categories)
        self.service.collect_board_size_settings(self.board_size)

        if self.service.check_player_number_validity() is False:
            show_player_number_error_dialog()
        elif self.service.check_player_names_validity() is False:
            show_player_name_error_dialog()
        elif self.service.check_category_number_validity() is False:
            show_category_number_error_dialog()
        else:
            self._open_game_view()
        self.window.focus()

    def _open_questions_view(self):
        """Destroys the current view and initializes a new one."""

        self.window.destroy()
        CustomContentView(self.database)

    def _open_rules_view(self):
        """Initializes a new view on top of the current view."""

        RulesView()

    def _open_game_view(self):
        """Destroys the current view and initializes a new one."""

        show_game_not_ready_dialog()
        # from WIP.game_view import GameView
        #
        # # These will later come from elsewhere, when it's possible
        # # for the user to manually select colors in the settings.
        # # -------------------------------------------------
        # p_cols = self.collect_player_color_settings()
        # c_cols = self.collect_category_color_settings()
        # # -------------------------------------------------
        #
        # self.window.destroy()
        # GameView(self.database, self.players, p_cols, self.categories, c_cols, self.board_size)

    def _handle_logout(self):
        """Calls SettingsServices class methods which logs out all users,
        the ndestroys the current window and initialzies a new one."""

        self.service.logout_users()
        self.window.destroy()
        from ui.login_view import LoginView
        LoginView(self.database)

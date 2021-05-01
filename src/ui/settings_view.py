import tkinter as tk
from services.settings_services import settings_services
from ui.custom_content_view import custom_content_view
from ui.rules_view import rules_view
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
)

class SettingsView:
    """Class that describes the UI of the settings view."""

    def __init__(self, service=settings_services):
        """Class constructor that initializes the class with appropriate services."""

        self.window = None
        self.service = service
        self.players = None
        self.categories = None
        self.board_size = None

    def initialize_window(self):
        """Initializes the window with appropriate settings and widgets."""

        self.window = tk.Tk()
        get_window_settings(self.window, SETTINGS_WINDOW_NAME, SETTINGS_WINDOW_SIZE)
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
            categories.append("")
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

        players = self.service.collect_player_settings(self.players)
        player_colors = self.service.collect_player_color_settings()
        categories = self.service.collect_category_settings(self.categories)
        category_colors = self.service.collect_category_color_settings()
        board_size = self.service.collect_board_size_settings(self.board_size)

        if self.service.check_player_number_validity() is False:
            show_player_number_error_dialog()
            self.window.focus()
        elif self.service.check_player_names_validity() is False:
            show_player_name_error_dialog()
            self.window.focus()
        elif self.service.check_category_number_validity() is False:
            show_category_number_error_dialog()
            self.window.focus()
        else:
            self.service.handle_session_save(players, categories, board_size)
            self._open_game_view(player_colors, category_colors)

    def _open_questions_view(self):
        """Destroys the current window and initializes a new one."""

        self.window.destroy()
        custom_content_view.initialize_window()

    def _open_rules_view(self):
        """Initializes a new window on top of the current one."""

        rules_view.initialize_window()

    def _open_game_view(self, player_colors, category_colors):
        """Destroys the current window and initializes a new one."""

        from ui.game_view import GameView
        self.window.destroy()
        GameView().initialize_window(player_colors, category_colors)

    def _handle_logout(self):
        """Calls SettingsServices class methods which logs out all users,
        the ndestroys the current window and initialzies a new one."""

        from ui.login_view import login_view
        self.service.logout_users()
        self.window.destroy()
        login_view.initialize_window()


settings_view = SettingsView()

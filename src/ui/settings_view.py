import tkinter as tk
from services.settings_services import settings_services
from ui.custom_content_view import custom_content_view
from ui.rules_view import rules_view
from ui.widgets import (
    title_label,
    basic_label,
    button,
    combobox,
)
from ui.dialogs import (
    show_player_number_error_dialog,
    show_player_name_error_dialog,
    show_category_number_error_dialog,
    show_about_otdb_dialog,
    show_no_otdb_connection_dialog,
)
from ui.stylings import (
    get_window_settings,
    SETTINGS_WINDOW_NAME,
    SETTINGS_WINDOW_SIZE,
    X, Y,
)


class SettingsView:
    """Class that describes the UI of the settings view."""

    def __init__(self, service=settings_services):
        """Class constructor that initializes the class with appropriate services."""

        self.service = service
        self.window = None
        self.players = None
        self.categories = None
        self.board_size = None

    def initialize_window(self):
        """Initializes the window with appropriate settings and widgets."""

        self.window = tk.Tk()
        get_window_settings(self.window, SETTINGS_WINDOW_NAME, SETTINGS_WINDOW_SIZE)
        self._build_layout()
        self._build_labels_and_entries()
        self._build_buttons()
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

    def _build_labels_and_entries(self):
        """Builds the label and entry widgets of the parent window."""

        title_label(
            self.window,
            "Game Settings"
        ).grid(column=0, row=0, columnspan=3)

        basic_label(
            self.window,
            "Players"
        ).grid(column=0, row=1, pady=Y)

        self.players = self._build_player_entries()

        basic_label(
            self.window,
            "Categories"
        ).grid(column=1, row=1, pady=Y)

        self.categories = self._build_category_comboboxes()

        basic_label(
            self.window,
            "Board Size"
        ).grid(column=2, row=1, pady=Y)

        self.board_size = self._build_board_size_combobox()

    def _build_buttons(self):
        """Builds the button widgets of the parent window."""

        button(
            self.window,
            "  Logout  ",
            self._handle_logout
        ).grid(column=0, row=0, padx=X)

        button(
            self.window,
            "Custom Content",
            self._open_questions_view
        ).grid(column=2, row=0, padx=X)

        button(
            self.window,
            "Game Rules",
            self._open_rules_view
        ).grid(column=0, row=14, padx=X)

        button(
            self.window,
            "About Open Trivia DB",
            show_about_otdb_dialog
        ).grid(column=1, row=14, padx=X)

        button(
            self.window,
            "Start Game",
            self._handle_game_start_event
        ).grid(column=2, row=14, padx=X)

    def _build_player_entries(self):
        """Builds the player name entry widgets with a loop.

        The default value of the first entry widget is
        set to the currently logged in user's username.

        Returns:
            player_comboboxes (list): Widgets for selecting players.
        """

        player_comboboxes = []
        for i in range(0,6):
            player_combobox = combobox(self.window)
            player_combobox['values'] = self.service.get_default_players()[1:]
            if i == 0:
                player_combobox.set(f"{self.service.get_default_players()[0]}")
            else:
                player_combobox.set("Add player")
            player_combobox.grid(column=0, row=2+i, padx=X)
            player_comboboxes.append(player_combobox)
        player_comboboxes[0].focus()

        return player_comboboxes

    def _build_category_comboboxes(self):
        """Builds the category selection widgets with a loop.

        The default value of the first two boxes is
        set to the Open Trivia Database category.

        Returns:
            category_comboboxes (list): Widgets for selecting categories.
        """

        category_comboboxes = []
        categories = self.service.get_categories()
        for i in range(0,12):
            category_combobox = combobox(self.window)
            category_combobox['values'] = categories
            category_combobox.state(['readonly'])
            if i in (0,1):
                category_combobox.set(categories[-2])
            else:
                category_combobox.set("Add category")
            category_combobox.grid(column=1, row=2+i)
            category_comboboxes.append(category_combobox)

        return category_comboboxes

    def _build_board_size_combobox(self):
        """Builds the board size selection widget.

        Returns:
            board_size_combobox (widget): The board size selection box.
        """

        board_size_combobox = combobox(self.window)
        board_size_combobox['values'] = [x[0] for x in self.service.get_default_board_sizes()]
        board_size_combobox.state(['readonly'])
        board_size_combobox.set(self.service.get_default_board_sizes()[2][0])
        board_size_combobox.grid(column=2, row=2, padx=X)

        return board_size_combobox

    def _handle_game_start_event(self):
        """Calls other methods which handle the collection and validation
        of the selected settings, then accommodates the UI accordingly."""

        self._handle_settings_collection()

        if self.service.check_settings_validity() is True:
            self.service.handle_session_save()
            self._open_game_view()
        else:
            self._handle_game_not_being_able_to_start()

    def _handle_settings_collection(self):
        """Calls services class methods which collect the selected settings."""

        self.service.collect_player_settings(self.players)
        self.service.collect_player_color_settings()
        self.service.collect_category_settings(self.categories)
        self.service.collect_category_color_settings()
        self.service.collect_board_size_settings(self.board_size)

    def _handle_game_not_being_able_to_start(self):
        """Accommodates the UI based on the reason why a game
        could not be started."""

        if self.service.check_player_number_validity() is False:
            show_player_number_error_dialog()
        elif self.service.check_player_names_validity() is False:
            show_player_name_error_dialog()
        elif self.service.check_category_number_validity() is False:
            show_category_number_error_dialog()
        elif self.service.check_otdb_connection() is False:
            show_no_otdb_connection_dialog()

        self.window.focus()

    def _open_questions_view(self):
        """Destroys the current window and initializes a new one."""

        self.window.destroy()
        custom_content_view.initialize_window()

    def _open_rules_view(self):
        """Initializes a new window on top of the current one."""

        rules_view.initialize_window()

    def _open_game_view(self):
        """Destroys the current window and initializes a new one."""

        from ui.game_view import GameView
        self.window.destroy()
        GameView(self.service.player_colors, self.service.category_colors).initialize_window()

    def _handle_logout(self):
        """Calls SettingsServices class methods which logs out all users,
        the ndestroys the current window and initialzies a new one."""

        from ui.login_view import login_view
        self.service.logout_users()
        self.window.destroy()
        login_view.initialize_window()


settings_view = SettingsView()

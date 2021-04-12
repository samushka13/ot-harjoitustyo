import tkinter as tk
from tkinter import ttk
from services.ui_services import get_window_settings
from services.database_operations import get_categories
from ui.game import GameView
from ui.custom_questions import CustomQuestionsView
from ui.stylings import (
    SETTINGS_WINDOW_NAME,
    SETTINGS_WINDOW_SIZE,
    X,
    Y,
)
from ui.widgets import (
    get_title_label,
    get_basic_label,
    get_basic_button,
)
from ui.dialogs import (
    show_player_number_error,
    show_player_name_error,
    show_category_number_error,
)

class SettingsView:
    def __init__(self, service):
        self.window = tk.Tk()
        get_window_settings(
            self.window,
            SETTINGS_WINDOW_NAME,
            SETTINGS_WINDOW_SIZE,
        )

        self.service = service

        self.board_sizes = self.service.get_default_board_sizes()

        # ------------------------------------------------------
        # Row and column configurations:
        # ------------------------------------------------------

        for i in (0,14):
            self.window.grid_rowconfigure(i, weight=1)
        for i in (1,2,3,4,5,6,7,8,9,10,11,12,13):
            self.window.grid_rowconfigure(i, weight=0)
        for i in (0,1,2):
            self.window.grid_columnconfigure(i, weight=1)

        # ------------------------------------------------------
        # Widgets:
        # ------------------------------------------------------

        get_title_label(
            self.window,
            "Game Settings"
        ).grid(column=0, row=0, columnspan=3)

        # ------------------------------------------------------
        # Right-side widgets:
        # ------------------------------------------------------

        get_basic_label(
            self.window,
            "Players"
        ).grid(column=0, row=1, pady=Y)
        self.players = self.get_player_entries()

        # ------------------------------------------------------
        # Middle widgets:
        # ------------------------------------------------------

        get_basic_label(
            self.window,
            "Categories"
        ).grid(column=1, row=1, pady=Y)
        self.categories = self.get_category_comboboxes()

        # ------------------------------------------------------
        # Left-side widgets:
        # ------------------------------------------------------

        get_basic_label(
            self.window,
            "Board Size"
        ).grid(column=2, row=1, pady=Y)
        self.board_size = self.get_board_size_combobox()

        # ------------------------------------------------------
        # Buttons:
        # ------------------------------------------------------

        get_basic_button(
            self.window,
            "Custom Questions",
            15,
            self.open_questions_view
        ).grid(column=0, row=14, padx=X, sticky="E")

        get_basic_button(
            self.window,
            "Start Game",
            15,
            self.open_game_view
        ).grid(column=2, row=14, padx=X, sticky="W")

        # ------------------------------------------------------

        self.window.mainloop()

    # ------------------------------------------------------
    # Comboboxes:
    # ------------------------------------------------------

    def get_player_entries(self):
        entry_fields = []
        i = 0
        for i in range(0,6):
            entry_field = ttk.Combobox(self.window, width=30)
            entry_field['values'] = self.service.get_default_players()
            if i == 0:
                entry_field.set(f"{self.service.get_default_players()[0]}")
            else:
                entry_field.set("Add player")
            entry_field.grid(column=0, row=2+i)
            entry_fields.append(entry_field)
            i += 1
        return entry_fields, entry_fields[0].focus()

    def get_board_size_combobox(self):
        board_size_combobox = ttk.Combobox(self.window, width=30)
        board_size_combobox['values'] = [x[0] for x in self.board_sizes]
        board_size_combobox.state(['readonly'])
        board_size_combobox.set([x[0] for x in self.board_sizes][2])
        board_size_combobox.grid(column=2, row=2)
        return board_size_combobox

    def get_category_comboboxes(self):
        comboboxes = []
        i = 0
        for i in range(0,12):
            category_combobox = ttk.Combobox(self.window, width=30)
            categories = get_categories()
            category_combobox['values'] = categories
            category_combobox.state(['readonly'])
            category_combobox.set("Add category")

            # This could be used to fill the categories automatically with existing values.
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

    # ------------------------------------------------------
    # Function that returns all the settings:
    # ------------------------------------------------------

    def collect_settings(self):
        players = []
        for entry in self.players[0]:
            if entry.get() == "" or entry.get() == "Add player":
                pass
            else:
                players.append(entry.get())

        board_size = None
        for i in range(0, len(self.board_sizes)):
            if self.board_size.get() == [x[0] for x in self.board_sizes][i]:
                board_size = [x[1] for x in self.board_sizes][i]

        categories = []
        for category in self.categories:
            if category.get() == "" or category.get() == "Add category":
                pass
            else:
                categories.append(category.get())

        return players, board_size, categories

    # ------------------------------------------------------
    # Functions that handle view changes:
    # ------------------------------------------------------

    def open_questions_view(self):
        self.window.destroy()
        CustomQuestionsView(self.service)

    def open_game_view(self):
        players = self.collect_settings()[0]
        board_size = self.collect_settings()[1]
        categories = self.collect_settings()[2]
        if len(players) == 0:
            show_player_number_error()
            self.window.focus()
        elif len(set(players)) != len(players):
            show_player_name_error()
            self.window.focus()
        elif len(categories) < 2:
            show_category_number_error()
            self.window.focus()
        else:
            self.window.destroy()
            GameView(self.service, players, board_size, categories)

import tkinter as tk
from services.ui_services import get_window_settings
from ui.board import GameView
from ui.custom_questions import CustomQuestionsView
from ui.stylings import (
    SETTINGS_WINDOW_NAME,
    SETTINGS_WINDOW_SIZE,
    X,
    Y,
)
from ui.widgets import (
    get_players_combobox,
    get_category_comboboxes,
    get_board_size_combobox,
    get_title_label,
    get_basic_label,
    get_basic_button,
)

class SettingsView:
    def __init__(self):
        self.window = tk.Tk()
        get_window_settings(
            self.window,
            SETTINGS_WINDOW_NAME,
            SETTINGS_WINDOW_SIZE,
        )

        # ------------------------------------------------------
        # Row and column configurations:
        # ------------------------------------------------------

        for i in (0,11):
            self.window.grid_rowconfigure(i, weight=1)
        for i in (1,3,5):
            self.window.grid_rowconfigure(i, weight=0)
        for i in (2,4,6,7,8,9,10):
            self.window.grid_rowconfigure(i, weight=0)
        for i in (0,1):
            self.window.grid_columnconfigure(i, weight=1)

        # ------------------------------------------------------
        # Widgets:
        # ------------------------------------------------------

        get_title_label(
            self.window,
            "Game Settings"
        ).grid(column=0, row=0, columnspan=2)
        get_basic_label(
            self.window,
            "Players"
        ).grid(column=0, row=1, columnspan=2, pady=Y)
        get_players_combobox(self.window)
        get_basic_label(
            self.window,
            "Board Size"
        ).grid(column=0, row=3, columnspan=2, pady=Y)
        get_board_size_combobox(self.window)
        get_basic_label(
            self.window,
            "Categories"
        ).grid(column=0, row=5, columnspan=2, pady=Y)
        get_category_comboboxes(self.window)
        get_basic_button(
            self.window,
            "Custom Questions",
            15,
            self.open_questions_view
        ).grid(column=0, row=11, padx=X, sticky="E")
        get_basic_button(
            self.window,
            "Start Game",
            15,
            self.open_game_view
        ).grid(column=1, row=11, padx=X, sticky="W")

        # ------------------------------------------------------

        self.window.mainloop()

    # ------------------------------------------------------
    # Functions that handle view changes:
    # ------------------------------------------------------

    def open_questions_view(self):
        self.window.destroy()
        CustomQuestionsView()

    def open_game_view(self):
        self.window.destroy()
        GameView()

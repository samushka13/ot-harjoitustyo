import tkinter as tk
from custom_questions import CustomQuestionsView
from board import GameView
from ui.stylings import SETTINGS_WINDOW_NAME, SETTINGS_WINDOW_SIZE, BACKGROUND, X, Y, TITLE_FONT
from ui.widgets import get_players_combobox, get_category_comboboxes, get_board_size_combobox

class SettingsView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(SETTINGS_WINDOW_NAME)
        self.window.geometry(SETTINGS_WINDOW_SIZE)
        self.window.resizable(False, False)
        self.window.configure(bg=BACKGROUND)
        self.window.bind_class("Button", "<Return>", self.bind_key_to_button)
        self.window.focus()

        for i in (0,11):
            self.window.grid_rowconfigure(i, weight=2)
        for i in (1,3,5):
            self.window.grid_rowconfigure(i, weight=1)
        for i in (2,4,6,7,8,9,10):
            self.window.grid_rowconfigure(i, weight=0)
        for i in (0,1):
            self.window.grid_columnconfigure(i, weight=1)

        label = tk.Label(self.window, text="Game Settings", font=TITLE_FONT)
        label.grid(column=0, row=0, columnspan=2, padx=X, pady=Y)

        label = tk.Label(self.window, text="Players")
        label.grid(column=0, row=1, columnspan=2, padx=X, pady=Y)

        get_players_combobox(self.window)

        label = tk.Label(self.window, text="Board Size")
        label.grid(column=0, row=3, columnspan=2, padx=X, pady=Y)

        get_board_size_combobox(self.window)

        label = tk.Label(self.window, text="Categories")
        label.grid(column=0, row=5, columnspan=2, padx=X, pady=Y)

        get_category_comboboxes(self.window)

        btn_questions = tk.Button(
            self.window,
            text="Custom Questions",
            width=15,
            command=self.open_questions_view,
        )
        btn_questions.grid(column=0, row=11, padx=X, pady=Y, sticky="E")

        btn_users = tk.Button(
            self.window,
            text="Start Game",
            width=15,
            command=self.open_game_view,
        )
        btn_users.grid(column=1, row=11, padx=X, pady=Y, sticky="W")

        self.window.mainloop()

    def open_questions_view(self):
        self.window.destroy()
        CustomQuestionsView()

    def open_game_view(self):
        self.window.destroy()
        GameView()

    def bind_key_to_button(self, window):
        window.widget.invoke()

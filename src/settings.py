import tkinter as tk
import sqlite3
from tkinter import ttk
from custom_questions import CustomQuestionsView
from board import GameView

db = sqlite3.connect("test.db")
db.isolation_level = None
db.row_factory = sqlite3.Row

X = 20
Y = 0

class SettingsView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Trivioboros')
        self.window.minsize(720,720)
        self.window.geometry('720x720')
        self.window.resizable(False, False)
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

        self.label = tk.Label(self.window, text="Game Settings", font=('Helvetica', 16, 'bold'))
        self.label.grid(column=0, row=0, columnspan=2, padx=X, pady=Y)

        label = tk.Label(self.window, text="Players")
        label.grid(column=0, row=1, columnspan=2, padx=X, pady=Y)

        self.get_players_combobox()

        label = tk.Label(self.window, text="Board Size")
        label.grid(column=0, row=3, columnspan=2, padx=X, pady=Y)

        self.get_board_size_combobox()

        label = tk.Label(self.window, text="Categories")
        label.grid(column=0, row=5, columnspan=2, padx=X, pady=Y)

        self.get_category_comboboxes()

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

    def get_players_combobox(self):
        players_combobox = ttk.Combobox(self.window, width=30)
        values = players_combobox['values'] = [2,3,4,5,6]
        players_combobox.state(['readonly'])
        players_combobox.set(values[0])
        players_combobox.grid(column=0, row=2, columnspan=2, padx=X, pady=Y)
        return players_combobox, players_combobox.focus()

    def get_board_size_combobox(self):
        board_size_combobox = ttk.Combobox(self.window, width=30)
        values = board_size_combobox['values'] = ["Tiny (least difficult)","Small","Medium","Large","Insane (most difficult)"]
        board_size_combobox.state(['readonly'])
        board_size_combobox.set(values[2])
        board_size_combobox.grid(column=0, row=4, columnspan=2, padx=X, pady=Y)
        return board_size_combobox

    def get_category_comboboxes(self):
        comboboxes = []
        i = 0
        for i in range(0,5):
            category_combobox = ttk.Combobox(self.window, width=30)
            values = []
            for row in db.execute("SELECT category FROM Questions GROUP BY category").fetchall():
                values.append(row['category'])
            category_combobox['values'] = values
            category_combobox.state(['readonly'])

            if len(values) < 5:
                if len(values) == 0:
                    category_combobox.set("")
                else:
                    category_combobox.set(values[0])
            else:
                category_combobox.set(values[i])
            category_combobox.grid(column=0, row=6+i, columnspan=2, padx=X, pady=Y)
            comboboxes.append(category_combobox)
            i += 1
        return comboboxes

    def open_questions_view(self):
        CustomQuestionsView()

    def open_game_view(self):
        self.window.destroy()
        GameView()

    def bind_key_to_button(self, window):
        window.widget.invoke()

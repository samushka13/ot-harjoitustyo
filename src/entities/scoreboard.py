import tkinter as tk
from tkinter import DISABLED
from ui.widgets import get_display_textbox

class Scoreboard:
    def __init__(self, window, canvas, players: list, p_col: list, categories: list, c_col: list):
        self.window = window
        self.canvas = canvas
        self.players = players
        self.player_colors = p_col
        self.categories = categories
        self.category_colors = c_col

    def _build(self):

        # -------------------------------------------------
        # Player names:
        # -------------------------------------------------

        i = 0
        y_increase = 0
        while i < len(self.players):
            player = get_display_textbox(self.window, 1, 15)
            player.place(x=30, y=30+y_increase, anchor="w")
            player.insert(tk.END, self.players[i])
            player.config(state=DISABLED, fg=self.player_colors[i])
            i += 1
            y_increase += 30

        # -------------------------------------------------
        # Player points:
        # -------------------------------------------------

        player_index = 0
        y_increase = 0
        while player_index < len(self.players):
            category_index = 0
            x_increase = 0
            while category_index < len(self.categories):
                self.canvas.create_oval(
                    530-x_increase, 20+y_increase, 510-x_increase, 40+y_increase,
                    fill="",
                    outline=self.category_colors[category_index],
                )
                category_index += 1
                x_increase += 30
            player_index += 1
            y_increase += 30

    def highlight_player(self):
        pass

    def add_point(self):
        pass

    def remove_point(self):
        pass

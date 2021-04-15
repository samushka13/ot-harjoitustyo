import tkinter as tk
from tkinter import DISABLED
from ui.widgets import get_display_textbox
from ui.stylings import TEXT_FONT

class Scoreboard:
    def __init__(self, window, canvas, players, player_colors, categories, category_colors):
        self.window = window
        self.canvas = canvas
        self.players = players
        self.player_colors = player_colors
        self.categories = categories
        self.category_colors = category_colors
        self.pointer = None

    def _build(self):

        # -------------------------------------------------
        # Player names:
        # -------------------------------------------------

        i = 0
        y_increase = 0
        while i < len(self.players):
            player = get_display_textbox(self.window, 1, 25, TEXT_FONT)
            player.place(x=40, y=30+y_increase, anchor="w")
            player.insert(tk.END, self.players[i])
            player.config(state=DISABLED, fg=self.player_colors[i])
            i += 1
            y_increase += 25

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
                    530-x_increase, 25+y_increase, 517-x_increase, 38+y_increase,
                    fill="",
                    outline=self.category_colors[category_index],
                )
                category_index += 1
                x_increase += 20
            player_index += 1
            y_increase += 25

    def highlight_player(self, player):
        self.pointer = self.canvas.create_polygon(
            30, 27+(player*25),
            39, 32+(player*25),
            30, 37+(player*25),
            fill=self.player_colors[player],
            outline="",
        )
        return self.pointer

    def remove_previous_highlight(self):
        self.canvas.delete(self.pointer)

    def add_point(self):
        pass

    def remove_point(self):
        pass

import tkinter as tk
from tkinter import DISABLED
from ui.widgets import get_display_textbox
from ui.stylings import TEXT_FONT, BACKGROUND

class Scoreboard:
    """Class that describes a scoreboard entity.

    Attributes:
        service (class): The current services class entity.
        window (window): A tkinter window.
        canvas (widget): A tkinter canvas widget.
        player_colors (list): The player colors.
        category_colors (list): The category colors.
        points (list): The players' points.
    """
    def __init__(self, service, window, canvas, player_colors, category_colors, points):
        """Class constructor that initiates a new scoreboard for the game view window.
        The board is drawn on a tkinter canvas widget.

        Args:
            service (class): The current services class.
            window (window): A tkinter window.
            canvas (widget): A tkinter canvas widget.
            player_colors (list): List of player colors.
            category_colors (list): List of category colors.
            points (list): The players' points.
        """
        self.canvas = canvas
        self.players = service.get_players()
        self.player_colors = player_colors
        self.categories = service.get_categories()
        self.category_colors = category_colors
        self.highlighter = None
        self._build_player_names(window)
        self.draw_player_points(points)

    def _build_player_names(self, window):
        """Builds the player names on the scoreboard with a drawing loop.
        """
        i = 0
        y_increase = 0
        while i < len(self.players):
            player = get_display_textbox(window, 1, 25, TEXT_FONT)
            player.place(x=40, y=30+y_increase, anchor="w")
            player.insert(tk.END, self.players[i])
            player.config(state=DISABLED, fg=self.player_colors[i])
            i += 1
            y_increase += 25

    def draw_player_points(self, points):
        """Builds the player points on the scoreboard with a drawing loop.
        """
        player = 0
        point_item = 0
        y_increase = 0
        while player < len(self.players):
            category = 0
            x_increase = 0
            while category < len(self.categories):
                if points[point_item][2] == 1:
                    self.canvas.create_oval(
                        530-x_increase, 25+y_increase, 517-x_increase, 38+y_increase,
                        fill=self.category_colors[category],
                        outline=self.category_colors[category],
                    )
                else:
                    self.canvas.create_oval(
                        530-x_increase, 25+y_increase, 517-x_increase, 38+y_increase,
                        fill=BACKGROUND,
                        outline=self.category_colors[category],
                    )
                category += 1
                point_item += 1
                x_increase += 20
            player += 1
            y_increase += 25

    def highlight_player(self, player):
        """Highlights the current player with a triangular pointer.

        Args:
            player (str): The current player.
        """
        self.highlighter = self.canvas.create_polygon(
            30, 27+(player*25),
            39, 32+(player*25),
            30, 37+(player*25),
            fill=self.player_colors[player],
            outline="",
        )

    def remove_previous_highlighter(self):
        """Removes the previous highlighter.
        """
        self.canvas.delete(self.highlighter)

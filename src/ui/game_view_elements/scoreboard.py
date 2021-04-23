import tkinter as tk
from tkinter import DISABLED
from ui.widgets import get_display_textbox
from ui.stylings import TEXT_FONT

class Scoreboard:
    """Class that describes a scoreboard entity.

    Attributes:
        service (class): The current services class.
        window (window): A tkinter window.
        canvas (widget): A tkinter canvas widget.
        player_colors (list): List of player colors.
        category_colors (list): List of category colors.
    """
    def __init__(self, service, window, canvas, player_colors, category_colors):
        """Class constructor that initiates a new scoreboard for the game view window.
        The board is drawn on a tkinter canvas widget.

        Args:
            service (class): The current services class.
            window (window): A tkinter window.
            canvas (widget): A tkinter canvas widget.
            player_colors (list): List of player colors.
            category_colors (list): List of category colors.
        """
        self.service = service
        self.window = window
        self.canvas = canvas
        self.players = self.service.get_players()
        self.player_colors = player_colors
        self.categories = self.service.get_categories()
        self.category_colors = category_colors
        self.highlighter = None
        self._build_player_names()
        self._build_player_points()

    def _build_player_names(self):
        """Builds the player names on the scoreboard with a drawing loop.
        """
        i = 0
        y_increase = 0
        while i < len(self.players):
            player = get_display_textbox(self.window, 1, 25, TEXT_FONT)
            player.place(x=40, y=30+y_increase, anchor="w")
            player.insert(tk.END, self.players[i])
            player.config(state=DISABLED, fg=self.player_colors[i])
            i += 1
            y_increase += 25

    def _build_player_points(self):
        """Builds the player points on the scoreboard with a drawing loop.
        """
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
        """Highlights the current player with a triangular pointer.

        Args:
            player (str): The current player.

        Returns:
            widget: The category pointer.
        """
        self.highlighter = self.canvas.create_polygon(
            30, 27+(player*25),
            39, 32+(player*25),
            30, 37+(player*25),
            fill=self.player_colors[player],
            outline="",
        )

    def remove_previous_highlight(self):
        """Removes the previous highlighter.
        """
        self.canvas.delete(self.highlighter)

    def add_point_to_player(self, category):
        # This should be made to draw a filled circle on top of the default one,
        # if the player doesn't already have a point in the category.
        pass

    def remove_point_from_player(self, category):
        # This should be made to remove the filled circle from on top of the default one,
        # if the player has a point in the category.
        pass

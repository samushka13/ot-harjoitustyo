import tkinter as tk
from tkinter import DISABLED
from ui.widgets import display_textbox
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
        """Class constructor that initializes a new scoreboard for the game view window.
        The board is drawn on a tkinter canvas widget.

        Args:
            service (class): The current services class.
            window (window): A tkinter window.
            canvas (widget): A tkinter canvas widget.
            player_colors (list): The player colors.
            category_colors (list): The category colors.
            points (list): The players' points.
        """

        self.canvas = canvas
        self.players = service.players
        self.player_colors = player_colors
        self.categories = service.categories
        self.category_colors = category_colors
        self.highlighter = None
        self._draw_player_names(window)
        self.draw_player_points(points)

    def _draw_player_names(self, window):
        """Draw the player names on the scoreboard with a loop."""

        y_increase = 0
        for i in range(len(self.players)):
            player = display_textbox(window, 1, 25, TEXT_FONT)
            player.place(x=40, y=30+y_increase, anchor="w")
            player.insert(tk.END, self.players[i])
            player.config(state=DISABLED, fg=self.player_colors[i])
            y_increase += 25

    def draw_player_points(self, points):
        """Draws the player points on the scoreboard with a loop."""

        point_index = 0
        for i in range(len(self.players)):
            x_increase = 0
            for j in range(len(self.categories)):
                if points[point_index][2] == 1:
                    self.canvas.create_oval(
                        530-x_increase, 25+(i*25), 517-x_increase, 38+(i*25),
                        fill=self.category_colors[j],
                        outline=self.category_colors[j],
                    )
                else:
                    self.canvas.create_oval(
                        530-x_increase, 25+(i*25), 517-x_increase, 38+(i*25),
                        fill=BACKGROUND,
                        outline=self.category_colors[j],
                    )
                point_index += 1
                x_increase += 20

    def highlight_player(self, player):
        """Highlights the current player with a triangular pointer.

        Args:
            player (int): The current player.
        """

        self.highlighter = self.canvas.create_polygon(
            30, 27+(player*25),
            39, 32+(player*25),
            30, 37+(player*25),
            fill=self.player_colors[player],
            outline="",
        )

    def remove_previous_highlighter(self):
        """Removes the previous highlighter."""

        self.canvas.delete(self.highlighter)

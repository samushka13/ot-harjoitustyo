import tkinter as tk
from tkinter import DISABLED
from ui.widgets import display_textbox
from ui.stylings import TEXT_FONT

class CategoryBoard:
    """Class that describes a category board entity.

    Attributes:
        service (class): The current services class.
        window (window): A tkinter window.
        canvas (widget): A tkinter canvas widget.
        category_colors (list): List of category colors.
    """

    def __init__(self, service, window, canvas, category_colors):
        """Class constructor that initializes a new category board for the game view window.
        The board is drawn on a tkinter canvas widget.

        Args:
            service (class): The current services class.
            window (window): A tkinter window.
            canvas (widget): A tkinter canvas widget.
            category_colors (list): List of category colors.
        """

        self.window = window
        self.canvas = canvas
        self.category_colors = category_colors
        self.categories = service.categories
        self.highlighter = None
        self._draw_board()

    def _draw_board(self):
        """Draws the category board on the canvas with a loop."""

        x_increase = 0
        y_increase = 0
        for i in range(len(self.categories)):
            category = display_textbox(self.window, 1, 25, TEXT_FONT)
            category.place(x=40+x_increase, y=560+y_increase, anchor="w")
            category.insert(tk.END, self.categories[i])
            category.config(state=DISABLED, fg=self.category_colors[i])
            y_increase += 25
            if i == 5:
                x_increase += 250
                y_increase = 0

    def highlight_category(self, category):
        """Draws a triangular pointer next to the current category.

        Args:
            category (int): The current category's index value.
        """

        if category < 6:
            self.highlighter = self.canvas.create_polygon(
                30, 557+(category*25),
                39, 562+(category*25),
                30, 567+(category*25),
                fill=self.category_colors[category],
                outline="",
            )
        else:
            self.highlighter = self.canvas.create_polygon(
                280, 557+((category-6)*25),
                289, 562+((category-6)*25),
                280, 567+((category-6)*25),
                fill=self.category_colors[category],
                outline="",
            )

    def remove_previous_highlighter(self):
        """Deletes the previous highlighter widget."""

        self.canvas.delete(self.highlighter)

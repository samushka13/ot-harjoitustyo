import tkinter as tk
import random
from tkinter import DISABLED
from ui.widgets import get_display_textbox
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
        """Class constructor that initiates a new category board for the game view window.
        The board is drawn on a tkinter canvas widget.

        Args:
            service (class): The current services class.
            window (window): A tkinter window.
            canvas (widget): A tkinter canvas widget.
            category_colors (list): List of category colors.
        """
        self.service = service
        self.window = window
        self.canvas = canvas
        self.categories = self.service.get_categories()
        self.category_colors = category_colors
        self.highlighter = ""
        self._build_board()

    def _build_board(self):
        """Builds the category board on the canvas with a drawing loop.
        """
        category_index = 1
        x_increase = 0
        y_increase = 0
        special_category = get_display_textbox(self.window, 1, 25, TEXT_FONT)
        special_category.place(x=40+x_increase, y=560+y_increase, anchor="w")
        special_category.insert(tk.END, self.categories[0])
        special_category.config(state=DISABLED, fg=self.category_colors[0])
        while category_index < len(self.categories):
            category = get_display_textbox(self.window, 1, 25, TEXT_FONT)
            category.place(x=40+x_increase, y=585+y_increase, anchor="w")
            category.insert(tk.END, self.categories[category_index])
            category.config(state=DISABLED, fg=self.category_colors[category_index])
            category_index += 1
            y_increase += 25
            if category_index == 6:
                x_increase += 250
                y_increase = -25

    def highlight_category(self, category):
        """Highlights the current category with a triangular pointer.

        Args:
            category (str): The current category.

        Returns:
            widget: The category pointer.
        """
        if category in self.categories:
            i = random.choice([x for x, c in enumerate(self.categories) if c == category])
            if i < 6:
                self.highlighter = self.canvas.create_polygon(
                    30, 557+(i*25),
                    39, 562+(i*25),
                    30, 567+(i*25),
                    fill=self.category_colors[i],
                    outline="",
                )
            else:
                self.highlighter = self.canvas.create_polygon(
                    280, 557+((i-6)*25),
                    289, 562+((i-6)*25),
                    280, 567+((i-6)*25),
                    fill=self.category_colors[i],
                    outline="",
                )
        return self.highlighter

    def remove_previous_highlight(self):
        """Removes the previous highlighter.
        """
        self.canvas.delete(self.highlighter)

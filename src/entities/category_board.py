import tkinter as tk
from tkinter import DISABLED
from ui.widgets import get_display_textbox

class CategoryBoard:
    def __init__(self, window, categories: list, category_colors: list):
        self.window = window
        self.categories = categories
        self.category_colors = category_colors

    def _build(self):
        category_index = 1
        x_increase = 0
        y_increase = 0
        special_category = get_display_textbox(self.window, 1, 20)
        special_category.place(x=30+x_increase, y=560+y_increase, anchor="w")
        special_category.insert(tk.END, self.categories[0])
        special_category.config(state=DISABLED, fg=self.category_colors[0])
        while category_index < len(self.categories):
            category = get_display_textbox(self.window, 1, 20)
            category.place(x=30+x_increase, y=590+y_increase, anchor="w")
            category.insert(tk.END, self.categories[category_index])
            category.config(state=DISABLED, fg=self.category_colors[category_index])
            category_index += 1
            y_increase += 30
            if category_index == 5:
                x_increase += 250
                y_increase = -30

    def highlight_category(self):
        pass

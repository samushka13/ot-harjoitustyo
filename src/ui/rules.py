import tkinter as tk
from tkinter import DISABLED
from services.ui_services import get_window_settings
from ui.stylings import (
    RULES_WINDOW_NAME,
    RULES_WINDOW_SIZE,
    TITLE_FONT,
    TEXT_FONT,
)
from ui.widgets import get_display_textbox
from entities.settings import (
    GAME_RULES_TITLE,
    GAME_RULES_TEXT,
)

def show_rules():
    window = tk.Tk()
    get_window_settings(window, RULES_WINDOW_NAME, RULES_WINDOW_SIZE)

    title = get_display_textbox(window, 1, 85, TITLE_FONT)
    title.place(x=30, y=30)
    title.insert(tk.END, GAME_RULES_TITLE)
    title.config(state=DISABLED)

    rules = get_display_textbox(window, 40, 85, TEXT_FONT)
    rules.place(x=30, y=80)
    rules.insert(tk.END, GAME_RULES_TEXT)
    rules.config(state=DISABLED)

    window.mainloop()

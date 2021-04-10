import tkinter as tk
from tkinter import DISABLED
from services.ui_services import get_window_settings
from ui.stylings import (
    RULES_WINDOW_NAME,
    RULES_WINDOW_SIZE,
    TITLE_FONT,
    TEXT_FONT,
)
from ui.widgets import (
    get_display_textbox,
    get_basic_button,
)
from entities.settings import (
    GAME_RULES_TITLE,
    GAME_RULES_TEXT,
)

class RulesView():
    def __init__(self):
        self.rules_window = tk.Tk()
        get_window_settings(self.rules_window, RULES_WINDOW_NAME, RULES_WINDOW_SIZE)

        title = get_display_textbox(self.rules_window, 1, 85, TITLE_FONT)
        title.place(x=30, y=30)
        title.insert(tk.END, GAME_RULES_TITLE)
        title.config(state=DISABLED)

        rules = get_display_textbox(self.rules_window, 40, 85, TEXT_FONT)
        rules.place(x=30, y=80)
        rules.insert(tk.END, GAME_RULES_TEXT)
        rules.config(state=DISABLED)

        get_basic_button(
            self.rules_window,
            "Got it!",
            10,
            command=self._close_window,
        ).place(x=370, y=620, anchor="center")

        self.rules_window.mainloop()

    def _close_window(self):
        self.rules_window.destroy()

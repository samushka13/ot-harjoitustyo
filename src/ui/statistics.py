import tkinter as tk
from tkinter import DISABLED
from services.ui_services import get_window_settings
from ui.widgets import get_display_textbox
from ui.stylings import (
    STATISTICS_WINDOW_NAME,
    STATISTICS_WINDOW_SIZE,
    TITLE_FONT,
    TEXT_FONT,
)

def show_statistics():
    window = tk.Tk()
    get_window_settings(window, STATISTICS_WINDOW_NAME, STATISTICS_WINDOW_SIZE)

    title = get_display_textbox(window, 1, 85, TITLE_FONT)
    title.place(x=30, y=30)
    title.insert(tk.END, "Statistics")
    title.config(state=DISABLED)

    statistics = get_display_textbox(window, 40, 85, TEXT_FONT)
    statistics.place(x=30, y=80)
    statistics.insert(tk.END, "Nothing to see here just yet.")
    statistics.config(state=DISABLED)

    window.mainloop()

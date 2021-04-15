import tkinter as tk
from tkinter import DISABLED
from ui.widgets import (
    get_display_textbox,
    get_basic_button,
)
from ui.stylings import (
    get_window_settings,
    STATISTICS_WINDOW_NAME,
    STATISTICS_WINDOW_SIZE,
    TITLE_FONT,
    TEXT_FONT,
)

class StatisticsView():
    def __init__(self):
        self.stats_window = tk.Tk()
        get_window_settings(self.stats_window, STATISTICS_WINDOW_NAME, STATISTICS_WINDOW_SIZE)
        self._build_widgets()
        self.stats_window.mainloop()

    def _build_widgets(self):
        title = get_display_textbox(self.stats_window, 1, 85, TITLE_FONT)
        title.place(x=30, y=30)
        title.insert(tk.END, "Statistics")
        title.config(state=DISABLED)

        statistics = get_display_textbox(self.stats_window, 40, 85, TEXT_FONT)
        statistics.place(x=30, y=80)
        statistics.insert(tk.END, "Nothing to see here yet.")
        statistics.config(state=DISABLED)

        get_basic_button(
            self.stats_window,
            "Got it!",
            command=self._close_window,
        ).place(x=370, y=620, anchor="center")

    def _close_window(self):
        self.stats_window.destroy()

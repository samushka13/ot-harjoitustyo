import tkinter as tk
from tkinter import DISABLED
from ui.widgets import display_textbox, button
from ui.stylings import (
    get_window_settings,
    STATISTICS_WINDOW_NAME,
    STATISTICS_WINDOW_SIZE,
    TITLE_FONT,
    TEXT_FONT,
)

class StatisticsView:
    """Class that describes the UI of the statistics view.

    Attributes:
        service: The current services class entity.
    """

    def __init__(self, service):
        """Class constructor that initializes the class with appropriate services.

        Args:
            service: The current services class entity.
        """

        self.service = service
        self.window = None

    def initialize_window(self):
        """Initializes the window with appropriate settings and widgets."""

        self.window = tk.Tk()
        self.window.grab_set()
        get_window_settings(self.window, STATISTICS_WINDOW_NAME, STATISTICS_WINDOW_SIZE)
        self._build_widgets()
        self.window.mainloop()

    def _build_widgets(self):
        """Builds the widgets of the parent window."""

        title = display_textbox(self.window, 1, 85, TITLE_FONT)
        title.place(x=30, y=30)
        title.insert(tk.END, "Laps per player")
        title.config(state=DISABLED)

        y_increase = 0
        for i, player in enumerate(self.service.players):
            player = display_textbox(self.window, 1, 25, TEXT_FONT)
            player.place(x=30, y=90+y_increase, anchor="w")
            player.insert(tk.END, self.service.players[i])
            player.config(state=DISABLED)
            laps = display_textbox(self.window, 1, 5, TEXT_FONT)
            laps.place(x=310, y=90+y_increase, anchor="w")
            laps.insert(tk.END, self.service.laps[i])
            laps.config(state=DISABLED)
            y_increase += 25

        button(self.window, "Got it!", self._close_window,
        ).place(x=180, y=260, anchor="center")

    def _close_window(self):
        """Closes the statistics window."""

        self.window.destroy()

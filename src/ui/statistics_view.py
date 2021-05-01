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

        self.window = None
        self.service = service

    def initialize_window(self):
        """Initializes the window with appropriate settings and widgets."""

        self.window = tk.Tk()
        get_window_settings(self.window, STATISTICS_WINDOW_NAME, STATISTICS_WINDOW_SIZE)
        self._build_widgets()
        self.window.mainloop()

    def _build_widgets(self):
        """Builds the widgets of the parent window."""

        title = get_display_textbox(self.window, 1, 85, TITLE_FONT)
        title.place(x=30, y=30)
        title.insert(tk.END, "Laps per player")
        title.config(state=DISABLED)

        i = 0
        y_increase = 0
        players = self.service.get_players()
        while i < len(players):
            player = get_display_textbox(self.window, 1, 25, TEXT_FONT)
            player.place(x=30, y=90+y_increase, anchor="w")
            player.insert(tk.END, players[i])
            player.config(state=DISABLED)
            laps = get_display_textbox(self.window, 1, 5, TEXT_FONT)
            laps.place(x=200, y=90+y_increase, anchor="w")
            laps.insert(tk.END, self.service.get_laps()[i])
            laps.config(state=DISABLED)
            i += 1
            y_increase += 25

        get_basic_button(self.window, "Got it!", self._close_window,
        ).place(x=370, y=620, anchor="center")

    def _close_window(self):
        """Closes the statistics window."""

        self.window.destroy()

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

        self._draw_player_names()
        self._draw_player_laps()

        button(self.window, "Got it!", self.window.destroy
        ).place(x=180, y=260, anchor="center")

    def _draw_player_names(self):
        """Draws player names with a loop."""

        for i, player in enumerate(self.service.players):
            player = display_textbox(self.window, 1, 25, TEXT_FONT)
            player.place(x=30, y=90+(i*25), anchor="w")
            player.insert(tk.END, self.service.players[i])
            player.config(state=DISABLED)

    def _draw_player_laps(self):
        """Draws laps traveled per player with a loop."""

        for i in range(len(self.service.players)):
            laps = display_textbox(self.window, 1, 5, TEXT_FONT)
            laps.place(x=310, y=90+(i*25), anchor="w")
            laps.insert(tk.END, self.service.laps[i])
            laps.config(state=DISABLED)

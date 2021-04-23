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
    """Class that describes the UI of the statistics view.

    Attributes:
        service: The current services class entity.
        player_tokens: List of players' tokens.
    """

    def __init__(self, service, player_tokens):
        """Class constructor that initializes the window
        with appropriate settings and widgets.

        Args:
            service: The current services class entity.
            player_tokens: List of players' tokens.
        """

        self.service = service
        self.stats_window = tk.Tk()
        get_window_settings(self.stats_window, STATISTICS_WINDOW_NAME, STATISTICS_WINDOW_SIZE)
        self.players = self.service.get_players()
        self.player_tokens = player_tokens
        self._build_widgets()
        self.stats_window.mainloop()

    def _build_widgets(self):
        """Builds the widgets of the parent window."""

        title = get_display_textbox(self.stats_window, 1, 85, TITLE_FONT)
        title.place(x=30, y=30)
        title.insert(tk.END, "Laps per player")
        title.config(state=DISABLED)

        i = 0
        y_increase = 0
        while i < len(self.players):
            player = get_display_textbox(self.stats_window, 1, 25, TEXT_FONT)
            player.place(x=30, y=90+y_increase, anchor="w")
            player.insert(tk.END, self.players[i])
            player.config(state=DISABLED)
            laps = get_display_textbox(self.stats_window, 1, 5, TEXT_FONT)
            laps.place(x=200, y=90+y_increase, anchor="w")
            laps.insert(tk.END, self.service.get_laps()[i])
            laps.config(state=DISABLED)
            i += 1
            y_increase += 25

        get_basic_button(
            self.stats_window,
            "Got it!",
            command=self._close_window,
        ).place(x=370, y=620, anchor="center")

    def _close_window(self):
        """Closes the statistics window."""

        self.stats_window.destroy()

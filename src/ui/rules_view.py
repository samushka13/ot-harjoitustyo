import tkinter as tk
from tkinter import DISABLED
from ui.stylings import (
    get_window_settings,
    RULES_WINDOW_NAME,
    RULES_WINDOW_SIZE,
    TITLE_FONT,
    TEXT_FONT,
)
from ui.widgets import (
    get_display_textbox,
    get_basic_button,
)

class RulesView:
    """Class that describes the UI of the rules view."""

    def __init__(self):
        """Class constructor that initializes the class."""

        self.window = None

    def initialize_window(self):
        """Initializes the window with appropriate settings and widgets."""

        self.window = tk.Tk()
        self.window.grab_set()
        get_window_settings(self.window, RULES_WINDOW_NAME, RULES_WINDOW_SIZE)
        self._build_widgets()
        self.window.mainloop()

    def _build_widgets(self):
        """Build the widgets of the parent window."""

        title = get_display_textbox(self.window, 1, 85, TITLE_FONT)
        title.place(x=30, y=30)
        title.insert(tk.END, "Trivioboros")
        title.config(state=DISABLED)

        rules = get_display_textbox(self.window, 40, 85, TEXT_FONT)
        rules.place(x=30, y=80)
        rules.insert(tk.END, self._game_rules_text())
        rules.config(state=DISABLED)

        get_basic_button(
            self.window,
            "Got it!",
            command=self._close_window,
        ).place(x=370, y=620, anchor="center")


    def _game_rules_text(self):
        """Provides the text content for the game rules view.

        Returns:
            The text as a multiline string value.
        """

        return """Game start:

- All players start from the unique starting segment.
- The highlighted player starts the game, and turns change in order.


Game progression:

1. The player whose turn it is casts the die.
2. The player token is moved clockwise by the number declared by the die.
3. The player is presented with a question from the category segment on which the player token is.
    - If the player's answer is correct, they receive the category point.
    - If the player already has this category point, they get nothing.
    - If the player's answer is incorrect, they lose the category point.
    - If the player does not have this category point, they lose nothing.    
4. The player turn changes.


Game ending:

- The game is won by the player who first gets on or over the starting segment with all the category points.


Note on game difficulty:

- The difficulty level can be modified in many ways, and there are various combinations.
- In general, the difficulty is increased as the board size and the number of categories are increased.
- Try different combinatations to see what works for you!
"""

    def _close_window(self):
        """Destroys the current window."""

        self.window.destroy()


rules_view = RulesView()

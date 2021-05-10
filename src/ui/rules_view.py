import tkinter as tk
from tkinter import DISABLED
from ui.widgets import display_textbox, button
from ui.stylings import (
    get_window_settings,
    RULES_WINDOW_NAME,
    RULES_WINDOW_SIZE,
    TITLE_FONT,
    TEXT_FONT,
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
        """Builds the widgets of the parent window."""

        title = display_textbox(self.window, 1, 60, TITLE_FONT)
        title.place(x=30, y=30)
        title.insert(tk.END, "Trivioboros")
        title.config(state=DISABLED)

        rules = display_textbox(self.window, 40, 87, TEXT_FONT)
        rules.place(x=30, y=80)
        rules.insert(tk.END, self._game_rules_text())
        rules.config(state=DISABLED)

        button(self.window, "Got it!", self.window.destroy,
        ).place(x=370, y=580, anchor="center")

    def _game_rules_text(self):
        """Provides the text content for the game rules view.

        Returns:
            rules (str): The game rules as a multiline string value.
        """

        rules_text = """How does the game start?

1. The player tokens are placed next to the unique starting segment.
2. The highlighted player starts the game.


What happens during a turn?

1. The highlighted player casts the die.
2. The player's token is moved clockwise by the number declared by the die.
3. The player is presented with a question from the category on which the player token is.
    - If the player's answer is correct, they receive the category point.
        - If the player already has the category point, they get to keep the point.
    - If the player's answer is incorrect, they lose the category point.
        - If the player does not have this category point, they lose nothing.    
4. The turn ends, and the next player is highlighted.


Who wins the game?

The game is won by the player who first gets on or over the starting segment with all the category points.


Notes on game difficulty:

- The difficulty level can be modified in many ways, and there are various combinations.
- In general, the difficulty is increased as the board size and the number of categories are increased.
- Try different combinations to see what works for you!
"""

        return rules_text


rules_view = RulesView()

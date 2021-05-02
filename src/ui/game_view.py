import tkinter as tk
from tkinter import DISABLED
from PIL import ImageTk, Image
from services.game_services import GameServices
from ui.game_view_elements.scoreboard import Scoreboard
from ui.game_view_elements.category_board import CategoryBoard
from ui.game_view_elements.game_board import GameBoard
from ui.game_view_elements.player_tokens import PlayerTokens
from ui.rules_view import rules_view
from ui.statistics_view import StatisticsView
from ui.settings_view import settings_view
from ui.dialogs import quit_game_dialog
from ui.widgets import (
    get_display_textbox,
    get_basic_button,
    get_canvas,
)
from ui.stylings import (
    get_window_settings,
    BOARD_WINDOW_NAME,
    BOARD_WINDOW_SIZE,
)

class GameView:
    """Class that describes the UI of the game view."""

    def __init__(self):
        """Class constructor that initializes the class with appropriate services."""

        self.service = GameServices()
        self.window = None
        self.img = None
        self.question_textbox = None
        self.answer_textbox = None
        self.show_answer_btn = None
        self.answer_correct_btn = None
        self.answer_incorrect_btn = None
        self.right_side = None
        self.left_side = None
        self.scoreboard = None
        self.category_board = None
        self.player_tokens = None

    def initialize_window(self, player_colors, category_colors):
        """Initializes the window with appropriate settings and widgets.

        Args:
            player_colors (list): Player colors.
            category_colors (list): Category colors.
        """

        self.window = tk.Tk()
        get_window_settings(self.window, BOARD_WINDOW_NAME, BOARD_WINDOW_SIZE)
        self._build_background()
        self._build_scoreboard(player_colors, category_colors)
        self._build_category_board(category_colors)
        self._build_game_board(player_colors, category_colors)
        self._build_cast_button()
        self._build_left_side_buttons()
        self.window.mainloop()

    def _build_background(self):
        """Builds a canvas for the scoreboard, question and categories,
        and a second one for the game board. Builds also a line that
        separates the scoreboard from the question, and a second one
        that separates the question from the categories."""

        self.right_side = get_canvas(self.window, 720, 560)
        self.right_side.place(x=280, y=360, anchor="center")

        self.right_side.create_line(30, 190, 530, 190)
        self.right_side.create_line(30, 530, 530, 530)

        self.left_side = get_canvas(self.window, 720, 720)
        self.left_side.place(x=920, y=360, anchor="center")

    def _build_scoreboard(self, player_colors, category_colors):
        """Builds the scoreboard."""

        self.scoreboard = Scoreboard(
            self.service,
            self.window,
            self.right_side,
            player_colors,
            category_colors,
            self.service.get_default_player_points()
        )
        self.scoreboard.highlight_player(0)

    def _build_category_board(self, category_colors):
        """Builds the category board."""

        self.category_board = CategoryBoard(
            self.service,
            self.window,
            self.right_side,
            category_colors,
        )

    def _build_game_board(self, player_colors, category_colors):
        """Builds the game board, player tokens and die."""

        GameBoard(
            self.service,
            self.left_side,
            category_colors,
        )

        self.player_tokens = PlayerTokens(
            self.service,
            self.left_side,
            player_colors,
        )

        self._build_die(self.service.get_die_faces()[5][0])

    def _build_left_side_buttons(self):
        """Builds buttons for showing rules and statistics,
        and quitting the current game session."""

        get_basic_button(self.window, "Quit", self._quit_game,
        ).place(x=1260, y=30, anchor="e")

        get_basic_button(self.window, "Rules", self._open_rules_view,
        ).place(x=1260, y=655, anchor="e")

        get_basic_button(self.window, "Statistics", self._open_statistics_view,
        ).place(x=1260, y=690, anchor="e")

    def _build_die(self, die_face):
        """Builds the die on the parent canvas.

        Args:
            die_face = Path of the die face image asset.
        """

        self.img = ImageTk.PhotoImage(Image.open(die_face))
        self.left_side.create_image(360, 340, anchor="center", image=self.img)

    def _build_cast_button(self):
        """Builds a button for casting the die."""

        cast_btn = get_basic_button(self.window, "Cast", lambda: self._cast_die(cast_btn))
        cast_btn.place(x=917,y=420, anchor="center")

    def _cast_die(self, cast_btn):
        """Selects a random number from the die, builds the corresponding die face image,
        removes the die cast button, shows the question, highlights the category,
        and moves the player's token to the correct position on the game board."""

        current_turn = self.service.current_turn
        die_face = self.service.get_die_face()
        starting_positions = self.service.player_positions

        cast_btn.destroy()
        self._build_die(die_face[0])
        self._show_question()
        self.category_board.highlight_category(self.service.current_category)

        positions = self.service.update_player_positions(current_turn, die_face[1])
        self.player_tokens.move_token(current_turn, positions[current_turn], starting_positions)

    def _show_question(self):
        """Shows the current category and question,
        and builds a button for showing the correct answer."""

        self.service.get_category_for_player()
        self.question_textbox = get_display_textbox(self.window, 7, 45)
        self.question_textbox.place(x=30, y=285, anchor="w")
        self.question_textbox.insert(tk.END, self.service.get_question_for_player())
        self.question_textbox.config(state=DISABLED)
        self.show_answer_btn = get_basic_button(
            self.window,
            "Show answer",
            self._show_confirmation_buttons,
        )
        self.show_answer_btn.place(x=280, y=420, anchor="center")

    def _show_confirmation_buttons(self):
        """Shows the correct answer and buttons for confirming
        whwther the player's answer was correct."""

        self.answer_textbox = get_display_textbox(self.window, 3, 45)
        self.answer_textbox.place(x=30, y=420, anchor="w")
        self.answer_textbox.insert(tk.END, self.service.get_answer_for_player())
        self.answer_textbox.config(state=DISABLED)

        self.answer_correct_btn = get_basic_button(
            self.window,
            "Player's answer was correct",
            self._handle_correct_answer,
        )
        self.answer_correct_btn.place(x=30, y=490, anchor="w")

        self.answer_incorrect_btn = get_basic_button(
            self.window,
            "Player's answer was incorrect",
            self._handle_incorrect_answer,
        )
        self.answer_incorrect_btn.place(x=300, y=490, anchor="w")

    def _handle_correct_answer(self):
        """Calls a services class method which returns an updated list of players' points,
        then calls another method in this class which handles the turn end operations."""

        points = self.service.add_point_to_player()
        self._handle_turn_end(points)

    def _handle_incorrect_answer(self):
        """Calls a services class method which returns an updated list of players' points,
        then calls another method in this class which handles the turn end operations."""

        points = self.service.remove_point_from_player()
        self._handle_turn_end(points)

    def _handle_turn_end(self, points):
        """Redraws the scoreboard, removes unnecessary widgets and highlighters,
        calls a services class method which updates the player turn tracker,
        highlights the current player, and rebuilds the die cast button.

        Args:
            points (list): The players' points.
        """

        self.scoreboard.draw_player_points(points)
        self.question_textbox.destroy()
        self.answer_textbox.destroy()
        self.show_answer_btn.destroy()
        self.answer_correct_btn.destroy()
        self.answer_incorrect_btn.destroy()
        self.scoreboard.remove_previous_highlighter()
        self.category_board.remove_previous_highlight()
        self.service.update_current_turn()
        self.scoreboard.highlight_player(self.service.current_turn)
        self._build_cast_button()

    def _quit_game(self):
        """Shows a dialog with confirmation buttons.
        If the user clicks 'yes', closes the current window
        and initiates a new SettingsView instance."""

        if quit_game_dialog() == 'yes':
            self.service.remove_game_active_status()
            self.window.destroy()
            settings_view.initialize_window()

    def _open_statistics_view(self):
        """Opens a new window on top of the current one."""

        StatisticsView(self.service).initialize_window()

    def _open_rules_view(self):
        """Opens a new window on top of the current one."""

        rules_view.initialize_window()

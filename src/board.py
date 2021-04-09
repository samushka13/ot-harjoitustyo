import tkinter as tk
import random
from tkinter import DISABLED
from PIL import ImageTk, Image
from services.database_operations import (
    get_category_for_player,
    get_question_for_player,
    get_answer_for_player,
)
from services.ui_services import get_window_settings
from ui.rules import show_rules
from ui.statistics import show_statistics
from ui.widgets import (
    get_display_textbox,
    get_basic_button,
    get_canvas,
)
from ui.dialogs import (
    remove_player_dialog,
    quit_game_dialog,
)
from ui.stylings import (
    BOARD_WINDOW_NAME,
    BOARD_WINDOW_SIZE,
    DIE_FACES,
    DEFAULT_DIE_FACE,
)
from entities.settings import (
    PLAYERS,
    PLAYER_COLORS,
    BOARD_SIZE,
    CATEGORIES,
    CATEGORY_COLORS,
    SEGMENT,
)
from entities.category_board import CategoryBoard
from entities.scoreboard import Scoreboard
from entities.game_board import GameBoard
from entities.player_tokens import PlayerTokens

class GameView:
    def __init__(self):
        self.window = tk.Tk()
        get_window_settings(
            self.window,
            BOARD_WINDOW_NAME,
            BOARD_WINDOW_SIZE,
        )

        # -------------------------------------------------
        # These build the game board in its default state:
        # -------------------------------------------------

        self.build_background()

        CategoryBoard(
            self.window,
            CATEGORIES,
            CATEGORY_COLORS,
        )._build()

        Scoreboard(
            self.window,
            self.scores,
            PLAYERS,
            PLAYER_COLORS,
            CATEGORIES,
            CATEGORY_COLORS,
        )._build()

        GameBoard(
            self.window,
            self.board,
            BOARD_SIZE,
            CATEGORIES,
            CATEGORY_COLORS,
        )._build()
        self.player_tokens = PlayerTokens(self.board, PLAYERS, PLAYER_COLORS, SEGMENT)
        self.player_tokens._build()

        self.turn_counter = 0
        self.question = ""

        self.img = ImageTk.PhotoImage(Image.open(DEFAULT_DIE_FACE))
        self.board.create_image(360, 340, anchor="center", image=self.img)

        self.build_cast_button()
        self.build_left_side_buttons()

        # -------------------------------------------------

        self.window.mainloop()

    # -------------------------------------------------
    # These functions build game board elements:
    # -------------------------------------------------

    def get_question(self):
        self.question = get_question_for_player(get_category_for_player())
        textbox = get_display_textbox(self.window, 6, 45)
        textbox.place(x=30, y=305, anchor="w")
        textbox.insert(tk.END, self.question['question'])
        textbox.config(state=DISABLED)
        get_basic_button(
            self.window,
            "Show answer",
            15,
            self.show_answer,
        ).place(x=280, y=420, anchor="center")

    def show_answer(self):
        answer = get_answer_for_player(self.question)
        textbox = get_display_textbox(self.window, 3, 45)
        textbox.place(x=30, y=420, anchor="w")
        textbox.insert(tk.END, answer['answer'])
        textbox.config(state=DISABLED)
        self.build_answer_confirmation_buttons()

    def build_answer_confirmation_buttons(self):
        get_basic_button(
            self.window,
            f"{PLAYERS[0]} answered correctly",
            25,
            self.end_player_turn,
        ).place(x=30, y=490, anchor="w")

        get_basic_button(
            self.window,
            f"{PLAYERS[0]} answered incorrectly",
            25,
            self.end_player_turn,
        ).place(x=300, y=490, anchor="w")

    def hide_question(self):
        placeholder = get_display_textbox(self.window, 13, 45)
        placeholder.place(x=30, y=370, anchor="w")
        placeholder.insert(tk.END, "")
        placeholder.config(state=DISABLED)

    def hide_cast_button(self):
        placeholder = get_display_textbox(self.window, 1, 15)
        placeholder.place(x=900, y=420, anchor="center")
        placeholder.insert(tk.END, "")
        placeholder.config(state=DISABLED)

    def end_player_turn(self):
        self.hide_question()
        self.build_cast_button()
        self.turn_counter += 1
        if self.turn_counter == len(PLAYERS):
            self.turn_counter = 0

    def build_cast_button(self):
        get_basic_button(
            self.window,
            "Cast",
            8,
            self.cast_die,
        ).place(x=917,y=420, anchor="center")

    def cast_die(self):
        number = random.choice(DIE_FACES)
        self.img = ImageTk.PhotoImage(Image.open(number[0]))
        self.board.create_image(360, 340, anchor="center", image=self.img)
        self.hide_cast_button()
        self.get_question()
        self.player_tokens.move_token(self.turn_counter, number[1])

# ------------------------------------------------
# These belong to GameView:
# ------------------------------------------------

    def build_background(self):
        # Canvas for the scoreboard, questions and categories.
        self.scores = get_canvas(self.window, 720, 560)
        self.scores.place(x=280, y=360, anchor="center")

        # Line that separates the scoreboard from questions.
        self.scores.create_line(30, 220, 530, 220)

        # Line that separates the questions from categories.
        self.scores.create_line(30, 530, 530, 530)

        # Canvas for the game board etc.
        self.board = get_canvas(self.window, 720, 720)
        self.board.place(x=920, y=360, anchor="center")

    def build_left_side_buttons(self):
        get_basic_button(
            self.window,
            "Remove Player",
            12,
            command=self.remove_player,
        ).place(x=1260, y=30, anchor="e")

        get_basic_button(
            self.window,
            "Quit",
            6,
            command=self.quit_game,
        ).place(x=1260, y=65, anchor="e")

        get_basic_button(
            self.window,
            "Rules",
            6,
            command=show_rules,
        ).place(x=1260, y=655, anchor="e")

        get_basic_button(
            self.window,
            "Statistics",
            12,
            command=show_statistics,
        ).place(x=1260, y=690, anchor="e")

    def quit_game(self):
        from ui.settings import SettingsView
        if quit_game_dialog() == 'yes':
            self.window.destroy()
            SettingsView()

    def remove_player(self):
        if remove_player_dialog() == 'yes':
            # Remove player somehow.
            pass
        self.window.focus()

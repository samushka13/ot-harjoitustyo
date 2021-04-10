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
from ui.rules import RulesView
from ui.statistics import StatisticsView
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
    PLAYER_COLORS,
    CATEGORY_COLORS,
)
from entities.category_board import CategoryBoard
from entities.scoreboard import Scoreboard
from entities.game_board import GameBoard
from entities.player_tokens import PlayerTokens

class GameView:
    def __init__(self, players: list, board_size: str, categories: list):
        self.window = tk.Tk()
        get_window_settings(
            self.window,
            BOARD_WINDOW_NAME,
            BOARD_WINDOW_SIZE,
        )
        self.players = players
        self.board_size = board_size
        self.categories = categories

        # -------------------------------------------------
        # These build the game board in its default state:
        # -------------------------------------------------

        self.build_background()

        self.category_board = CategoryBoard(
            self.window,
            self.scores,
            self.categories,
            CATEGORY_COLORS,
        )
        self.category_board._build()

        self.scoreboard = Scoreboard(
            self.window,
            self.scores,
            self.players,
            PLAYER_COLORS,
            self.categories,
            CATEGORY_COLORS,
        )
        self.scoreboard._build()

        self.gameboard = GameBoard(
            self.window,
            self.board,
            self.board_size,
            self.categories,
            CATEGORY_COLORS,
        )
        self.gameboard.build()

        self.player_tokens = PlayerTokens(
            self.board,
            self.players,
            PLAYER_COLORS,
            360/(len(self.categories[1:])*self.board_size+1),
        )
        self.player_tokens._build()

        self.turn_counter = 0
        self.scoreboard.highlight_player(self.turn_counter)

        self.current_category = ""
        self.category_board.highlight_category(self.current_category)

        self.category = ""
        self.question = ""
        self.img = ImageTk.PhotoImage(Image.open(DEFAULT_DIE_FACE))
        self.board.create_image(360, 340, anchor="center", image=self.img)

        self.question_textbox = None
        self.answer_textbox = None
        self.show_answer_btn = None
        self.answer_correct_btn = None
        self.answer_incorrect_btn = None

        self.build_cast_button()
        self.build_left_side_buttons()

        # -------------------------------------------------

        self.window.mainloop()

    # -------------------------------------------------
    # These functions build game board elements:
    # -------------------------------------------------

    def get_question(self):

        # This should actually be determined by the player's position on the game board.
        # -------------------------------------------------
        self.category = get_category_for_player(random.choice(self.categories))
        # -------------------------------------------------
        self.question = get_question_for_player(self.category)
        self.question_textbox = get_display_textbox(self.window, 7, 45)
        self.question_textbox.place(x=30, y=285, anchor="w")
        self.question_textbox.insert(tk.END, self.question['question'])
        self.question_textbox.config(state=DISABLED)
        self.show_answer_btn = get_basic_button(
            self.window,
            "Show answer",
            15,
            self.show_answer,
        )
        self.show_answer_btn.place(x=280, y=420, anchor="center")
        return self.category, self.question_textbox, self.show_answer_btn

    def show_answer(self):
        answer = get_answer_for_player(self.question)
        self.answer_textbox = get_display_textbox(self.window, 3, 45)
        self.answer_textbox.place(x=30, y=420, anchor="w")
        self.answer_textbox.insert(tk.END, answer['answer'])
        self.answer_textbox.config(state=DISABLED)
        self.build_answer_confirmation_buttons()
        return self.answer_textbox

    def build_answer_confirmation_buttons(self):
        self.answer_correct_btn = get_basic_button(
            self.window,
            f"{self.players[self.turn_counter]} answered correctly",
            25,
            self.end_player_turn,
        )
        self.answer_correct_btn.place(x=30, y=490, anchor="w")

        self.answer_incorrect_btn = get_basic_button(
            self.window,
            f"{self.players[self.turn_counter]} answered incorrectly",
            25,
            self.end_player_turn,
        )
        self.answer_incorrect_btn.place(x=300, y=490, anchor="w")

        return self.answer_correct_btn, self.answer_incorrect_btn

    def end_player_turn(self):
        self.question_textbox.destroy()
        self.answer_textbox.destroy()
        self.show_answer_btn.destroy()
        self.answer_correct_btn.destroy()
        self.answer_incorrect_btn.destroy()
        self.build_cast_button()
        self.scoreboard.remove_previous_highlight()
        self.category_board.remove_previous_highlight()
        self.turn_counter += 1
        if self.turn_counter == len(self.players):
            self.turn_counter = 0
        self.scoreboard.highlight_player(self.turn_counter)

    def build_cast_button(self):
        self.cast_btn = get_basic_button(
            self.window,
            "Cast",
            8,
            self.cast_die,
        )
        self.cast_btn.place(x=917,y=420, anchor="center")
        return self.cast_btn

    def cast_die(self):
        number = random.choice(DIE_FACES)
        self.img = ImageTk.PhotoImage(Image.open(number[0]))
        self.board.create_image(360, 340, anchor="center", image=self.img)
        self.cast_btn.destroy()
        self.get_question()
        self.category_board.highlight_category(self.category['category'])
        self.player_tokens.move_token(self.turn_counter, number[1])


# ------------------------------------------------
# These belong to GameView:
# ------------------------------------------------

    def build_background(self):
        # Canvas for the scoreboard, questions and categories.
        self.scores = get_canvas(self.window, 720, 560)
        self.scores.place(x=280, y=360, anchor="center")

        # Line that separates the scoreboard from questions.
        self.scores.create_line(30, 190, 530, 190)

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
            command=RulesView,
        ).place(x=1260, y=655, anchor="e")

        get_basic_button(
            self.window,
            "Statistics",
            12,
            command=StatisticsView,
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

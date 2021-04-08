import tkinter as tk
import random
from tkinter import DISABLED, WORD, messagebox
from PIL import ImageTk, Image
from ui.rules import show_rules
from ui.stylings import (
    BOARD_WINDOW_NAME,
    BOARD_WINDOW_SIZE,
    BACKGROUND,
    BOARD_TEXT_FONT,
    BASIC_CURSOR,
    DIE_FACES,
    DEFAULT_DIE_FACE,
)
from services.database_connection import db
from entities.settings import (
    CATEGORIES,
    CATEGORY_COLORS,
    SPECIAL,
    SPECIAL_COLOR,
    PLAYERS,
    PLAYER_COLORS,
    BOARD_SIZES,
    BOARD_SIZE,
)

segments = len(CATEGORIES)*BOARD_SIZE+1
segment = 360/segments
starting_positions = [360, 360, 360, 360, 360, 360]

class GameView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title(BOARD_WINDOW_NAME)
        self.window.geometry(BOARD_WINDOW_SIZE)
        self.window.resizable(False, False)
        self.window.configure(bg=BACKGROUND)
        self.window.bind_class("Button", "<Return>", self.bind_key_to_button)
        self.window.focus()
        self.build_everything()
        self.window.mainloop()

    def build_everything(self):
        self.build_board()
        self.build_cast_button()
        self.build_left_side_buttons()
        self.build_scoreboard()
        self.build_category_board()

    def build_scoreboard(self):
        i = 0
        j = 0
        while i < len(PLAYERS):
            player = tk.Text(self.window, height=1, width=15, font=BOARD_TEXT_FONT, cursor=BASIC_CURSOR, wrap=WORD, bg=BACKGROUND, highlightbackground=BACKGROUND)
            player.place(x=30, y=30+j, anchor="w")
            player.insert(tk.END, PLAYERS[i])
            player.config(state=DISABLED, fg=PLAYER_COLORS[i])
            i += 1
            j += 30

        i = 0
        l = 0
        while i < len(PLAYERS):
            j = 0
            k = 0
            self.scores.create_oval(530, 20+l, 510, 40+l, fill="", outline=SPECIAL_COLOR)
            while j < len(CATEGORIES):
                self.scores.create_oval(500-k, 20+l, 480-k, 40+l, fill="", outline=CATEGORY_COLORS[j])
                j += 1
                k += 30
            i += 1
            l += 30

    def build_category_board(self):
        i = 0
        j = 0
        k = 0
        special_category = tk.Text(self.window, height=1, width=20, font=BOARD_TEXT_FONT, cursor=BASIC_CURSOR, wrap=WORD, bg=BACKGROUND, highlightbackground=BACKGROUND)
        special_category.place(x=30+k, y=560+j, anchor="w")
        special_category.insert(tk.END, SPECIAL)
        special_category.config(state=DISABLED, fg=SPECIAL_COLOR)
        while i < len(CATEGORIES):
            category = tk.Text(self.window, height=1, width=20, font=BOARD_TEXT_FONT, cursor=BASIC_CURSOR, wrap=WORD, bg=BACKGROUND, highlightbackground=BACKGROUND)
            category.place(x=30+k, y=590+j, anchor="w")
            category.insert(tk.END, CATEGORIES[i])
            category.config(state=DISABLED, fg=CATEGORY_COLORS[i])
            i += 1
            j += 30
            if i == 4:
                k += 250
                j = -30

    def get_question(self):
        # This should be determined by the player's position on the game board.
        select = 'Computer Science'
        category = db.execute(f"SELECT category FROM Questions WHERE category='{select}'").fetchone()

        self.question = db.execute(f"SELECT question FROM Questions WHERE category='{category['category']}' ORDER BY RANDOM()").fetchone()
        q_text = tk.Text(self.window, height=6, width=45, font=BOARD_TEXT_FONT, cursor=BASIC_CURSOR, wrap=WORD, bg=BACKGROUND, highlightbackground=BACKGROUND)
        q_text.place(x=30, y=305, anchor="w")
        q_text.insert(tk.END, self.question['question'])
        q_text.config(state=DISABLED)

        self.btn_show_answer = tk.Button(
            self.window,
            text="Show answer",
            width=15,
            highlightbackground=BACKGROUND,
            command=self.show_answer,
        )
        self.btn_show_answer.place(x=280, y=420, anchor="center")

    def build_placeholder(self):
        placeholder = tk.Text(self.window, height=13, width=45, font=BOARD_TEXT_FONT, cursor=BASIC_CURSOR, wrap=WORD, bg=BACKGROUND, highlightbackground=BACKGROUND)
        placeholder.place(x=30, y=370, anchor="w")
        placeholder.insert(tk.END, "")
        placeholder.config(state=DISABLED)

    def hide_cast_button(self):
        placeholder = tk.Text(self.window, height=1, width=15, font=BOARD_TEXT_FONT, cursor=BASIC_CURSOR, wrap=WORD, bg=BACKGROUND, highlightbackground=BACKGROUND)
        placeholder.place(x=900, y=420, anchor="center")
        placeholder.insert(tk.END, "")
        placeholder.config(state=DISABLED)

    def show_answer(self):
        self.btn_show_answer.forget()
        answer = db.execute(f"SELECT answer FROM Questions WHERE question='{self.question['question']}'").fetchone()
        self.answer_text = tk.Text(self.window, height=3, width=45, font=BOARD_TEXT_FONT, cursor=BASIC_CURSOR, wrap=WORD, bg=BACKGROUND, highlightbackground=BACKGROUND)
        self.answer_text.place(x=30, y=420, anchor="w")
        self.answer_text.insert(tk.END, answer['answer'])
        self.answer_text.config(state=DISABLED)
        self.build_answer_confirmation_buttons()

    def build_answer_confirmation_buttons(self):
        self.btn_correct = tk.Button(
            self.window,
            text=f"{PLAYERS[0]} answered correctly",
            width=25,
            highlightbackground=BACKGROUND,
            command=self.correct_answer,
        )
        self.btn_correct.place(x=30, y=490, anchor="w")

        self.btn_incorrect = tk.Button(
            self.window,
            text=f"{PLAYERS[0]} answered incorrectly",
            width=25,
            highlightbackground=BACKGROUND,
            command=self.incorrect_answer,
        )
        self.btn_incorrect.place(x=300, y=490, anchor="w")

    def correct_answer(self):
        self.btn_correct.forget()
        self.btn_incorrect.forget()
        self.answer_text.forget()
        self.build_placeholder()
        self.build_cast_button()

    def incorrect_answer(self):
        self.btn_correct.forget()
        self.btn_incorrect.forget()
        self.answer_text.forget()
        self.build_placeholder()
        self.build_cast_button()

    def build_board(self):
        # Left-side stuff.
        self.scores = tk.Canvas(self.window, bg=BACKGROUND, height=720, width=560, highlightbackground=BACKGROUND)
        self.scores.place(x=280, y=360, anchor="center")
        self.scores.create_line(30, 220, 530, 220)
        self.scores.create_line(30, 530, 530, 530)

        # Right-side stuff.
        self.board = tk.Canvas(self.window, bg=BACKGROUND, height=720, width=720, highlightbackground=BACKGROUND)
        self.board.place(x=920, y=360, anchor="center")

        # This calculates the segments where categories are.
        # Required to allow changing the amount of categories in Game Settings.
        i = 0
        all_category_segments = []
        while i < len(CATEGORIES):
            j = 0
            k = 1 + i
            category_segments = []
            while j <= BOARD_SIZE:
                category_segments.append(k)
                k += len(CATEGORIES)
                j += 1
            i += 1
            all_category_segments.append(category_segments)

        i = 0
        j = 0
        while j < segments:
            if j == 0:
                self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=SPECIAL_COLOR, width=5)
            if j in all_category_segments[0]:
                self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=CATEGORY_COLORS[0], width=5)
            if len(CATEGORIES) >= 2:
                if j in all_category_segments[1]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=CATEGORY_COLORS[1], width=5)
            if len(CATEGORIES) >= 3:
                if j in all_category_segments[2]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=CATEGORY_COLORS[2], width=5)
            if len(CATEGORIES) >= 4:
                if j in all_category_segments[3]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=CATEGORY_COLORS[3], width=5)
            if len(CATEGORIES) >= 5:
                if j in all_category_segments[4]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=CATEGORY_COLORS[4], width=5)
            if len(CATEGORIES) >= 6:
                if j in all_category_segments[5]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=CATEGORY_COLORS[5], width=5)
            if len(CATEGORIES) >= 7:
                if j in all_category_segments[6]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=CATEGORY_COLORS[6], width=5)
            if len(CATEGORIES) >= 8:
                if j in all_category_segments[7]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=CATEGORY_COLORS[7], width=5)
            if len(CATEGORIES) >= 9:
                if j in all_category_segments[8]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=CATEGORY_COLORS[8], width=5)
            if len(CATEGORIES) >= 10:
                if j in all_category_segments[9]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=CATEGORY_COLORS[9], width=5)
            i += segment
            j += 1

        # Inner circle that helps form the shape of the gameboard.
        self.board.create_oval(100, 100, 620, 620, fill=BACKGROUND, width=5)

        # Player tokens.
        i = 0
        j = 0
        self.tokens = []
        while i < len(PLAYERS):
            token = self.board.create_arc(115+j, 115+j, 605-j, 605-j, start=starting_positions[i], extent=-segment, outline=PLAYER_COLORS[i], width=10, style=tk.ARC)
            self.tokens.append(token)
            i += 1
            j += 15

        # Die at the start of the game.
        self.img = ImageTk.PhotoImage(Image.open(DEFAULT_DIE_FACE))
        self.board.create_image(360, 340, anchor="center", image=self.img)

    def build_left_side_buttons(self):
        btn_remove_player = tk.Button(
            self.window,
            text="Remove Player",
            width=12,
            highlightbackground=BACKGROUND,
            command=self.remove_player,
        )
        btn_remove_player.place(x=1260, y=30, anchor="e")

        btn_quit = tk.Button(
            self.window,
            text="Quit",
            width=6,
            highlightbackground=BACKGROUND,
            command=self.quit_game,
        )
        btn_quit.place(x=1260, y=65, anchor="e")

        btn_rules = tk.Button(
            self.window,
            text="Rules",
            width=6,
            highlightbackground=BACKGROUND,
            command=show_rules,
        )
        btn_rules.place(x=1260, y=655, anchor="e")

        btn_stats = tk.Button(
            self.window,
            text="Statistics",
            width=12,
            highlightbackground=BACKGROUND,
            command=None,
        )
        btn_stats.place(x=1260, y=690, anchor="e")

    def build_cast_button(self):
        self.btn_cast_die = tk.Button(
            self.window,
            text="Cast",
            width=8,
            highlightbackground=BACKGROUND,
            command=self.cast_die,
        )
        self.btn_cast_die.place(x=917,y=420, anchor="center")

    def cast_die(self):
        self.number = random.choice(DIE_FACES)
        self.img = ImageTk.PhotoImage(Image.open(self.number[0]))
        self.board.create_image(360, 340, anchor="center", image=self.img)
        self.hide_cast_button()
        self.get_question()
        self.move_token()

    def move_token(self):
        self.new_position = starting_positions[0]-segment*(self.number[1])
        self.board.delete(self.tokens[0])
        starting_positions[0] = self.new_position
        token = self.board.create_arc(115, 115, 605, 605, start=self.new_position, extent=-segment, outline=PLAYER_COLORS[0], width=10, style=tk.ARC)
        # This helps keep track of the token's position in terms of the category segments.
        # (Tokens and categories are matched by their 'start' arguments.)
        if self.new_position >= 360:
            self.new_position -= 360
            # Statistiikkoja varten tähän voisi myös lisätä jonkun counterin,
            # joka kasvaa aina yhdellä, kun 360 tulee täyteen.
        self.tokens[0] = token

    def quit_game(self):
        from settings import SettingsView
        confirmation = messagebox.askquestion("Quit Game", "Are you sure you want to quit this game?")
        if confirmation == 'yes':
            self.window.destroy()
            SettingsView()

    def remove_player(self):
        confirmation = messagebox.askquestion("Remove Player", "Are you sure you want to remove this player?")
        if confirmation == 'yes':
            # Remove player somehow.
            pass
        self.window.focus()

    def bind_key_to_button(self, window):
        window.widget.invoke()

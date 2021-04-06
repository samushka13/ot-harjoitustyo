import tkinter as tk
import sqlite3
import random
from tkinter import DISABLED, WORD, messagebox
from PIL import ImageTk, Image

db = sqlite3.connect("test.db")
db.isolation_level = None
db.row_factory = sqlite3.Row

X = 20
Y = 0
text_font = ('Helvetica', 18, 'bold')
background = "lightblue"
categories = ["Category 1", "Category 2", "Category 3", "Category 4", "Category 5", "Category 6", "Category 7", "Category 8"]
players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6"]
colors = ["red", "yellow", "green", "purple", "orange", "blue", "grey", "brown"]

class GameView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Trivioboros')
        self.window.geometry('1280x720')
        self.window.resizable(False, False)
        self.window.bind_class("Button", "<Return>", self.bind_key_to_button)
        self.window.focus()
        self.build_everything()
        self.window.mainloop()

    def build_everything(self):
        self.build_board()
        self.build_cast_button()
        self.build_left_side_buttons()
        self.build_scoreboard()

    def build_scoreboard(self):
        i = 0
        j = 0
        while i < len(players):
            player = tk.Text(self.window, height=1, width=20, font=text_font, cursor="arrow", wrap=WORD, bg=background, highlightbackground=background)
            player.place(x=30, y=30+j, anchor="w")
            player.insert(tk.END, players[i])
            player.config(state=DISABLED, fg=colors[i])
            i += 1
            j += 30

        i = 0
        l = 0
        while i < len(players):
            j = 0
            k = 0
            while j < len(categories):
                self.scores.create_oval(530-k, 20+l, 510-k, 40+l, fill="", outline=colors[j])
                j += 1
                k += 30
            i += 1
            l += 30

    def get_question(self):
        # This should be determined by the player's position on the game board.
        select = 'Computer Science'
        category = db.execute(f"SELECT category FROM Questions WHERE category='{select}'").fetchone()

        self.question = db.execute(f"SELECT question FROM Questions WHERE category='{category['category']}' ORDER BY RANDOM()").fetchone()
        q_text = tk.Text(self.window, height=12, width=45, font=text_font, cursor="arrow", wrap=WORD, bg=background, highlightbackground=background)
        q_text.place(x=30, y=360, anchor="w")
        q_text.insert(tk.END, self.question['question'])
        q_text.config(state=DISABLED)

        self.btn_show_answer = tk.Button(
            self.window,
            text="Show answer",
            width=15,
            highlightbackground=background,
            command=self.show_answer,
        )
        self.btn_show_answer.place(x=280, y=410, anchor="center")

    def build_placeholder(self):
        placeholder = tk.Text(self.window, height=12, width=45, font=text_font, cursor="arrow", wrap=WORD, bg=background, highlightbackground=background)
        placeholder.place(x=30, y=360, anchor="w")
        placeholder.insert(tk.END, "")
        placeholder.config(state=DISABLED)

    def hide_cast_button(self):
        placeholder = tk.Text(self.window, height=1, width=15, font=text_font, cursor="arrow", wrap=WORD, bg=background, highlightbackground=background)
        placeholder.place(x=900, y=420, anchor="center")
        placeholder.insert(tk.END, "")
        placeholder.config(state=DISABLED)

    def show_answer(self):
        self.btn_show_answer.forget()
        answer = db.execute(f"SELECT answer FROM Questions WHERE question='{self.question['question']}'").fetchone()
        self.answer_text = tk.Text(self.window, height=2, width=45, font=text_font, cursor="arrow", wrap=WORD, bg=background, highlightbackground=background)
        self.answer_text.place(x=30, y=400, anchor="w")
        self.answer_text.insert(tk.END, answer['answer'])
        self.answer_text.config(state=DISABLED)
        self.build_answer_confirmation_buttons()

    def build_answer_confirmation_buttons(self):
        self.btn_correct = tk.Button(
            self.window,
            text="Player 1 answered correctly",
            width=25,
            bg="green",
            highlightbackground=background,
            command=self.correct_answer,
        )
        self.btn_correct.place(x=30, y=470, anchor="w")

        self.btn_incorrect = tk.Button(
            self.window,
            text="Player 1 answered incorrectly",
            width=25,
            bg="red",
            highlightbackground=background,
            command=self.incorrect_answer,
        )
        self.btn_incorrect.place(x=300, y=470, anchor="w")

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
        self.scores = tk.Canvas(self.window, bg=background, height=720, width=560, highlightbackground=background)
        self.scores.place(x=280, y=360, anchor="center")
        self.scores.create_line(30, 220, 530, 220)
        self.scores.create_line(30, 500, 530, 500)

        # Right-side stuff.
        self.board = tk.Canvas(self.window, bg=background, height=720, width=720, highlightbackground=background)
        self.board.place(x=920, y=360, anchor="center")
        difficulty = [9,7,5,3,1]
        segments = len(categories)*difficulty[2]+1
        segment = 360/segments

        # This calculates the segments where categories are.
        # Required to allow changing the amount of categories in Game Settings.
        i = 0
        all_category_segments = []
        while i < len(categories):
            j = 0
            k = 1 + i
            category_segments = []
            while j <= difficulty[2]:
                category_segments.append(k)
                k += len(categories)
                j += 1
            i += 1
            all_category_segments.append(category_segments)

        i = 0
        j = 0
        while j < segments:
            if j == 0:
                self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill="black", width=5)
            if j in all_category_segments[0]:
                self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=colors[0], width=5)
            if len(categories) >= 2:
                if j in all_category_segments[1]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=colors[1], width=5)
            if len(categories) >= 3:
                if j in all_category_segments[2]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=colors[2], width=5)
            if len(categories) >= 4:
                if j in all_category_segments[3]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=colors[3], width=5)
            if len(categories) >= 5:
                if j in all_category_segments[4]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=colors[4], width=5)
            if len(categories) >= 6:
                if j in all_category_segments[5]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=colors[5], width=5)
            if len(categories) >= 7:
                if j in all_category_segments[6]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=colors[6], width=5)
            if len(categories) >= 8:
                if j in all_category_segments[7]:
                    self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=colors[7], width=5)
            i += segment
            j += 1

        # Inner circle that helps form the shape of the gameboard.
        self.board.create_oval(100, 100, 620, 620, fill=background, width=5)

        # Player tokens.
        i = 0
        j = 0
        while i < len(players):
            self.board.create_arc(115+j, 115+j, 605-j, 605-j, start=360, extent=-segment, outline=colors[i], width=10, style=tk.ARC)
            i += 1
            j += 15

        # Die at the start of the game.
        self.img = ImageTk.PhotoImage(Image.open(r'src/assets/die_6.png'))
        self.board.create_image(360, 340, anchor="center", image=self.img)

    def build_left_side_buttons(self):
        btn_remove_player = tk.Button(
            self.window,
            text="Remove Player",
            width=12,
            highlightbackground=background,
            command=self.remove_player,
        )
        btn_remove_player.place(x=1260, y=30, anchor="e")

        btn_quit = tk.Button(
            self.window,
            text="Quit",
            width=6,
            highlightbackground=background,
            command=self.quit_game,
        )
        btn_quit.place(x=1260, y=65, anchor="e")

        btn_rules = tk.Button(
            self.window,
            text="Rules",
            width=6,
            highlightbackground=background,
            command=None,
        )
        btn_rules.place(x=1260, y=655, anchor="e")

        btn_stats = tk.Button(
            self.window,
            text="Statistics",
            width=12,
            highlightbackground=background,
            command=None,
        )
        btn_stats.place(x=1260, y=690, anchor="e")

    def build_cast_button(self):
        self.btn_cast_die = tk.Button(
            self.window,
            text="Cast",
            width=8,
            highlightbackground=background,
            command=self.cast_die,
        )
        self.btn_cast_die.place(x=917,y=420, anchor="center")

    def cast_die(self):
        die_faces = [
            r'src/assets/die_1.png',
            r'src/assets/die_2.png',
            r'src/assets/die_3.png',
            r'src/assets/die_4.png',
            r'src/assets/die_5.png',
            r'src/assets/die_6.png',
        ]
        self.img = ImageTk.PhotoImage(Image.open(random.choice(die_faces)))
        self.board.create_image(360, 340, anchor="center", image=self.img)
        self.hide_cast_button()
        self.get_question()

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

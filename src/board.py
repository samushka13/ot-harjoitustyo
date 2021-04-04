import tkinter as tk
import sqlite3
from tkinter import DISABLED, WORD, messagebox

db = sqlite3.connect("test.db")
db.isolation_level = None
db.row_factory = sqlite3.Row

X = 20
Y = 0

class GameView:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Trivioboros')
        self.window.geometry('1280x720')
        self.window.resizable(False, False)
        self.window.configure(background="lightblue")

        for i in range(0,15):
            self.window.grid_rowconfigure(i, weight=1)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=1)
        self.window.grid_columnconfigure(2, weight=3)

        self.board = tk.Canvas(self.window, bg="lightblue", height=720, width=720, highlightthickness=0)
        self.board.grid(column=2, row=0, rowspan=15, sticky="E")
        self.build_board()

        self.get_questions()

        btn_remove_player = tk.Button(
            self.window,
            text="Remove Player",
            width=12,
            highlightthickness=0,
            command=self.remove_player,
        )
        btn_remove_player.grid(column=2, row=0, padx=X, pady=Y, sticky="E")

        btn_quit = tk.Button(
            self.window,
            text="Quit",
            width=6,
            highlightthickness=0,
            command=self.quit_game,
        )
        btn_quit.grid(column=2, row=1, padx=X, pady=Y, sticky="NE")

        btn_rules = tk.Button(
            self.window,
            text="Rules",
            width=6,
            highlightthickness=0,
            command=None,
        )
        btn_rules.grid(column=2, row=13, padx=X, pady=Y, sticky="SE")

        btn_stats = tk.Button(
            self.window,
            text="Statistics",
            width=12,
            highlightthickness=0,
            command=None,
        )
        btn_stats.grid(column=2, row=14, padx=X, pady=Y, sticky="E")

        self.window.mainloop()

    def build_board(self):
        i = 0
        j = 0
        categories = 5
        difficulty = [7,5,3,1]
        segments = categories*difficulty[1]+1
        segment = 360/segments
        fills = ["red", "yellow", "green", "purple", "orange"]
        while j < segments:
            if j == 0:
                self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill="black", width=5)
            if j in (1,6,11,16,21,26,31):
                self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=fills[0], width=5)
            if j in (2,7,12,17,22,27,32):
                self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=fills[1], width=5)
            if j in (3,8,13,18,23,28,33):
                self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=fills[2], width=5)
            if j in (4,9,14,19,24,29,34):
                self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=fills[3], width=5)
            if j in (5,10,15,20,25,30,35):
                self.board.create_arc(20, 20, 700, 700, start=360-i, extent=-segment, fill=fills[4], width=5)
            i += segment
            j += 1

        # Inner circle that helps form the shape of the gameboard.
        self.board.create_oval(100, 100, 620, 620, fill="lightblue", width=5)

        # Player tokens.
        i = 0
        j = 0
        players = 6
        outlines = ["red", "yellow", "green", "black", "grey", "orange"]
        while i < players:
            self.board.create_arc(190-j, 190-j, 530+j, 530+j, start=360, extent=-segment, outline=outlines[i], width=10, style=tk.ARC)
            i += 1
            j += 15

    def get_questions(self):
        # Placeholder:
        player = "Player 1"

        title = tk.Label(self.window, text=f"{player}", font=('Helvetica', 30, 'bold'), bg="lightblue", highlightthickness=0)
        title.grid(column=0, row=0, columnspan=2, padx=X, pady=Y, sticky="W")

        select = 'Computer Science' # ''.join(random.choice(string.ascii_uppercase) for i in range(1))

        category = db.execute(f"SELECT category FROM Questions WHERE category='{select}'").fetchone()
        text = tk.Text(self.window, height=1, width=25, font=('Helvetica', 24, 'bold'), cursor="arrow", wrap=WORD, bg="lightblue", highlightthickness=0)
        text.grid(column=0, row=2, columnspan=2, padx=X, pady=Y, sticky="W")
        text.insert(tk.END, category['category'])
        text.config(state=DISABLED)

        global question
        question = db.execute(f"SELECT question FROM Questions WHERE category='{category['category']}' ORDER BY RANDOM()").fetchone()
        text = tk.Text(self.window, height=5, width=30, font=('Helvetica', 18, 'bold'), cursor="arrow", wrap=WORD, bg="lightblue", highlightthickness=0)
        text.grid(column=0, row=4, columnspan=2, padx=X, pady=Y, sticky="W")
        text.insert(tk.END, question['question'])
        text.config(state=DISABLED)

        global placeholder
        placeholder = tk.Text(self.window, height=4, width=30, font=('Helvetica', 18, 'bold'), cursor="arrow", wrap=WORD, bg="lightblue", highlightthickness=0)
        placeholder.grid(column=0, row=6, columnspan=2, padx=X, pady=Y, sticky="W")

        global btn_show_answer
        btn_show_answer = tk.Button(
            self.window,
            text="Show answer",
            width=15,
            highlightthickness=0,
            command=self.show_answer,
        )
        btn_show_answer.grid(column=0, row=6, columnspan=2, padx=X, pady=Y)

        # Button to show the answer...

        # Buttons that ask:
        # correct = input("Was the player's answer correct? (y/n) ")
        # if correct == "y":
        #     print("Well done!")
        #     Give point to player if they don't already have one in that category.
        # else:
        #     print("Better luck next time!")

    def show_answer(self):
        answer = db.execute(f"SELECT answer FROM Questions WHERE question='{question['question']}'").fetchone()
        text = tk.Text(self.window, height=5, width=40, font=('Helvetica', 18, 'bold'), cursor="arrow", wrap=WORD, bg="lightblue", highlightthickness=0)
        text.grid(column=0, row=7, columnspan=2, padx=X, pady=Y, sticky="W")
        text.insert(tk.END, answer['answer'])
        text.config(state=DISABLED)
        btn_show_answer.grid_remove()
        placeholder.grid_remove()

        label = tk.Label(self.window, text="The player's answer was", font=('Helvetica', 24, 'bold'), bg="lightblue", highlightthickness=0)
        label.grid(column=0, row=8, columnspan=2, padx=X, pady=Y, sticky="W")

        btn_correct = tk.Button(
            self.window,
            text="Correct",
            width=15,
            highlightthickness=0,
            command=None,
        )
        btn_correct.grid(column=0, row=9, padx=X, pady=Y, sticky="W")

        btn_incorrect = tk.Button(
            self.window,
            text="Incorrect",
            width=15,
            highlightthickness=0,
            command=None,
        )
        btn_incorrect.grid(column=1, row=9, padx=X, pady=Y, sticky="W")

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

import sqlite3
import pygame as pg
from entities.board import Board


db = sqlite3.connect("test.db")
db.isolation_level = None
db.row_factory = sqlite3.Row

X = 15
Y = 10

class GameView:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Trivioboros')
        board = Board(2, 30, ["Computer Science", "TV Shows", "Memes", "Sports", "Leisure"])
        Board.display(board)
        pg.display.flip()

        pg_running = True
        while pg_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg_running = False



    # def create_ask_question_window(self):
    #     self.window = tk.Tk()
    #     self.window.title('Trivioboros')
    #     self.window.minsize(360, 280)
    #     self.window.geometry('%dx%d+0+0' % (self.window.winfo_screenwidth(), self.window.winfo_screenheight()))
    #     self.window.bind_class("Button", "<Return>", self.bind_key_to_button)

    #     title = tk.Label(self.window, text="Ask Questions")
    #     title.grid(column=0, row=0, padx=X, pady=Y)

    #     label = tk.Label(text="Select category")
    #     label.grid(column=0, row=1, padx=X, pady=Y)

    #     self.get_category_combobox()

    #     self.window.mainloop()

        # select = input("Select category: ")
        # category = db.execute(f"SELECT category FROM Questions WHERE category='{select}'").fetchone()
        # question = db.execute(f"SELECT question FROM Questions WHERE category='{category['category']}' ORDER BY RANDOM()").fetchone()
        # answer = db.execute(f"SELECT answer FROM Questions WHERE question='{question['question']}'").fetchone()

        # print()
        # print(f"Question: {question['question']}")
        # print()
        # input("Press 'Enter' to show the correct answer.")
        # print()
        # print(f"Answer: {answer['answer']}")
        # print()

        # correct = input("Was the player's answer correct? (y/n) ")
        # if correct == "y":
        #     print()
        #     print("Well done!")
        #     print()
        # else:
        #     print()
        #     print("Better luck next time!")
        #     print()

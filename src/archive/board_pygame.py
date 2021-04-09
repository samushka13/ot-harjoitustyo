import sqlite3
from textwrap import fill
from math import sin,cos,radians
import pygame as pg


db = sqlite3.connect("test.db")
db.isolation_level = None
db.row_factory = sqlite3.Row

X = 15
Y = 10

class GameViewPygame:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Trivioboros')
        board = Board(6, 24, ["Computer Science", "Memes", "Leisure"])
        Board.display(board)
        pg.display.flip()
        pg_running = True
        while pg_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg_running = False

class Board:
    def __init__(self, players: int, parts: int, categories: list):
        self.players = players
        self.parts = parts
        self.categories = categories

    def display(self):
        width = 1280
        height = 720
        background = (155,200,255)
        self.window = pg.display.set_mode((width, height))
        pg.display.set_caption("Trivioboros")
        self.window.fill(background)
        self.font = pg.font.SysFont('Helvetica', 20)
        self.bold_font = pg.font.SysFont('Helvetica', 20, bold=True)
        self.surface = pg.Surface((width,height), pg.SRCALPHA)

        self.get_board()

        pg.draw.circle(self.surface, background, (900, height/2), 240)

        self.tokens()

        self.get_questions()

        self.window.blit(self.surface, (0,0))
        self.window.blit(self.c_label, (50,50))
        self.window.blit(self.q_label, (50,250))
        self.window.blit(self.a_label, (50,450))

    def pie(self, start, stop, color):
        self.start = start
        self.stop = stop
        self.color = color
        center = (900, 720/2)
        radius = 320
        theta = start
        while theta <= stop:
            pg.draw.line(self.surface,color,center,(center[0]+radius*cos(radians(theta)),center[1]+radius*sin(radians(theta))),2)
            theta+=0.01

    def get_board(self):
        i,size = 360/26,360/26
        j,red,green,blue = 1,0,0,0
        self.pie(0, 360/26, (255,100,100))
        while j <= 25:
            if j in (1,6,11,16,21):
                red,green,blue = 50,50,50
                self.pie(i, i+size, (red,green,blue))
            if j in (2,7,12,17,22):
                red,green,blue = 100,100,100
                self.pie(i, i+size, (red,green,blue))
            if j in (3,8,13,18,23):
                red,green,blue = 150,150,150
                self.pie(i, i+size, (red,green,blue))
            if j in (4,9,14,19,24):
                red,green,blue = 200,200,200
                self.pie(i, i+size, (red,green,blue))
            if j in (5,10,15,20,25):
                red,green,blue = 250,250,250
                self.pie(i, i+size, (red,green,blue))
            i += size
            j += 1

    def tokens(self):
        i = 0
        while i < 5:
            pg.gfxdraw.arc(self.surface, 900, 360, 180+i, 0, 360//26, (255,0,0))
            pg.gfxdraw.arc(self.surface, 900, 360, 190+i, 0, 360//26, (0,255,0))
            pg.gfxdraw.arc(self.surface, 900, 360, 200+i, 0, 360//26, (0,0,255))
            pg.gfxdraw.arc(self.surface, 900, 360, 210+i, 0, 360//26, (255,255,0))
            pg.gfxdraw.arc(self.surface, 900, 360, 220+i, 0, 360//26, (255,0,255))
            pg.gfxdraw.arc(self.surface, 900, 360, 230+i, 0, 360//26, (0,255,255))
            i += 1

    def get_questions(self):
        # Placeholder:
        select = 'A' # ''.join(random.choice(string.ascii_uppercase) for i in range(1))

        self.c_label = self.bold_font.render('Category', True, (0, 0, 0))
        category = db.execute(f"SELECT category FROM Questions WHERE category='{select}'").fetchone()
        str_cat = category['category']
        split_text = fill(str(str_cat), 40)
        i = 0
        for line in split_text.splitlines():
            text = self.font.render(f'{line}', True, (0, 0, 0))
            rect = text.get_rect(width=100, height=25)
            rect.center = (100,100+i)
            self.window.blit(text, rect)
            i += 25

        self.q_label = self.bold_font.render('Question', True, (0, 0, 0))
        question = db.execute(f"SELECT question FROM Questions WHERE category='{str_cat}' ORDER BY RANDOM()").fetchone()
        str_que = question['question']
        split_text = fill(str(str_que), 40)
        i = 0
        for line in split_text.splitlines():
            text = self.font.render(f'{line}', True, (0, 0, 0))
            rect = text.get_rect(width=100, height=25)
            rect.center = (100,300+i)
            self.window.blit(text, rect)
            i += 25

        self.a_label = self.bold_font.render('Answer', True, (0, 0, 0))
        answer = db.execute(f"SELECT answer FROM Questions WHERE question='{str_que}'").fetchone()
        str_ans = answer['answer']
        split_text = fill(str(str_ans), 40)
        i = 0
        for line in split_text.splitlines():
            text = self.font.render(f'{line}', True, (0, 0, 0))
            rect = text.get_rect(width=100, height=25)
            rect.center = (100,500+i)
            self.window.blit(text, rect)
            i += 25

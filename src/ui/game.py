import pygame as pg
from entities.board import Board


class GameView:
    def __init__(self):
        pg.init()
        board = Board(2, 30, ["Computer Science", "TV Shows", "Memes", "Sports", "Leisure"])
        Board.display(board)
        pg.display.flip()

        pg_running = True
        while pg_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg_running = False

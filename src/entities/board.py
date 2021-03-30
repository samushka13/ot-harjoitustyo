import pygame as pg


class Board:
    def __init__(self, players: int, parts: int, categories: list):
        self.players = players
        self.parts = parts
        self.categories = categories

    def display(self):
        width = 800
        height = 600
        background = (155,200,255)
        window = pg.display.set_mode((width, height))
        pg.display.set_caption("Trivioboros")
        window.fill(background)
        surface = pg.Surface((width,height), pg.SRCALPHA)
        pg.draw.circle(surface, (255, 0, 255, 100), (width/2, height/2), 280, 100)
        window.blit(surface, (0,0))

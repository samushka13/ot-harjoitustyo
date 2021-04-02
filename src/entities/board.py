from textwrap import fill
import pygame as pg


class Board:
    def __init__(self, players: int, parts: int, categories: list):
        self.players = players
        self.parts = parts
        self.categories = categories

    def display(self):
        width = 1280
        height = 720
        background = (155,200,255)
        window = pg.display.set_mode((width, height))
        pg.display.set_caption("Trivioboros")
        window.fill(background)
        font = pg.font.SysFont('Helvetica', 20)
        surface = pg.Surface((width,height), pg.SRCALPHA)
        pg.draw.circle(surface, (255, 0, 255, 100), (900, height/2), 300, 100)
        window.blit(surface, (0,0))

        c = 1
        q = 2
        a = 3

        category = font.render(f'Category:\n{c}', True, (0, 0, 0))
        question = font.render(f'Question:\n{q}', True, (0, 0, 0))
        answer = font.render(f'Answer:\n{a}', True, (0, 0, 0))

        window.blit(category, (100,100))
        window.blit(question, (100,200))
        window.blit(answer, (100,300))

        raw_text = 'Lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum?'
        split_text = fill(raw_text, 40)
        test = []
        i = 0
        for line in split_text.splitlines():
            test.append(line)
            text = font.render(f'{line}', True, (0, 0, 0))
            rect = text.get_rect(width=100, height=25)
            rect.center = (150,400+i)
            window.blit(text, rect)
            i += 25

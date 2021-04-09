import tkinter as tk
from tkinter import (
    DISABLED,
    WORD,
)
from ui.stylings import (
    RULES_WINDOW_NAME,
    RULES_WINDOW_SIZE,
    BACKGROUND,
    TITLE_FONT,
    BASIC_CURSOR,
    TEXT_FONT,
)
from entities.settings import (
    GAME_RULES_TITLE,
    GAME_RULES_TEXT,
)

def show_rules():
    window = tk.Tk()
    window.title(RULES_WINDOW_NAME)
    window.geometry(RULES_WINDOW_SIZE)
    window.resizable(False, False)
    window.configure(bg=BACKGROUND)
    window.focus()

    title = tk.Text(window, height=1, width=85, font=TITLE_FONT, cursor=BASIC_CURSOR, wrap=WORD, bg=BACKGROUND, highlightbackground=BACKGROUND)
    title.place(x=30, y=30)
    title.insert(tk.END, GAME_RULES_TITLE)
    title.config(state=DISABLED)

    rules = tk.Text(window, height=40, width=85, font=TEXT_FONT, cursor=BASIC_CURSOR, wrap=WORD, bg=BACKGROUND, highlightbackground=BACKGROUND)
    rules.place(x=30, y=80)
    rules.insert(tk.END, GAME_RULES_TEXT)
    rules.config(state=DISABLED)

    window.mainloop()
